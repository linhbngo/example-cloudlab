import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.igext as IG

pc = portal.Context()
request = rspec.Request()

pc.defineParameter("workerCount",
                   "Number of Hadoop DataNodes",
                   portal.ParameterType.INTEGER, 3)

pc.defineParameter("controllerHost", "Name of NameNode",
                   portal.ParameterType.STRING, "namenode", advanced=True,
                   longDescription="The short name of the Hadoop NameNode.  You shold leave \
                   this alone unless you really want the hostname to change.")

params = pc.bindParameters()

tourDescription = "This profile provides a configurable Hadoop testbed with one NameNode \
and customizable number of DataNodes."

tourInstructions = \
  """
### Basic Instructions
Once your experiment nodes have booted, and this profile's configuration scripts 
have finished deploying Hadoop inside your experiment, you'll be able to visit 
[the HDFS Web UI](http://{host-%s}:9870) and [the Yarn Web UI](http://{host-%s}:8088) (approx. 5-15 minutes). 
""" % (params.controllerHost, params.controllerHost)

#
# Setup the Tour info with the above description and instructions.
#  
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
tour.Instructions(IG.Tour.MARKDOWN,tourInstructions)
request.addTour(tour)

# Create a link with type LAN
link = request.LAN("lan")

# Generate the nodes
for i in range(params.workerCount + 1):
    if  i == 0:
      node = request.RawPC("namenode")
    else: 
      node = request.RawPC("datanode-" + str(i))
      
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-ARM"
    
    iface = node.addInterface("if" + str(i))
    iface.component_id = "eth1"
    iface.addAddress(rspec.IPv4Address("192.168.1." + str(i + 1), "255.255.255.0"))
    link.addInterface(iface)
    node.addService(rspec.Execute(shell="/bin/sh",
                                  command="sudo bash /local/repository/setup_ssh.sh"))
    node.addService(rspec.Execute(shell="/bin/sh",
                                  command="sudo wget http://apache.cs.utah.edu/hadoop/common/hadoop-3.1.1/hadoop-3.1.1.tar.gz"))
    node.addService(rspec.Execute(shell="/bin/sh",
                                  command="sudo tar xzf hadoop-3.1.1.tar.gz -C /opt/"))
    node.addService(rspec.Execute(shell="/bin/sh",
                                  command="sudo apt-get update -y"))
    node.addService(rspec.Execute(shell="/bin/sh",
                                  command="sudo apt-get install -y default-jdk"))    
    node.addService(rspec.Execute(shell="/bin/sh",
                                  command="sudo bash /local/repository/setup_xml.sh"))
    if i != 0:
        node.addService(rspec.Execute(shell="/bin/sh",
                                      command="sudo sleep 30"))
        node.addService(rspec.Execute(shell="/bin/sh",
                                      command="sudo /opt/hadoop-3.1.1/bin/hdfs --daemon start datanode"))
        node.addService(rspec.Execute(shell="/bin/sh",
                                      command="sudo /opt/hadoop-3.1.1/bin/yarn --daemon start nodemanager"))
    else:
        node.routable_control_ip = True        
        node.addService(rspec.Execute(shell="/bin/sh",
                                      command="sudo /opt/hadoop-3.1.1/bin/hdfs namenode -format CloudLab-Hadoop"))
        node.addService(rspec.Execute(shell="/bin/sh",
                                      command="sudo /opt/hadoop-3.1.1/bin/hdfs --daemon start namenode"))
        node.addService(rspec.Execute(shell="/bin/sh",
                                      command="sudo /opt/hadoop-3.1.1/bin/yarn --daemon start resourcemanager"))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec(request)

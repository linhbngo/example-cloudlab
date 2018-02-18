import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.igext as IG

pc = portal.Context()
request = rspec.Request()

tourDescription = "This profile automatically launches a Hadoop cluster with 1 headnode and 3 datanode on 4 VMs"

#
# Setup the Tour info with the above description.
#  
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
request.addTour(tour)


# Create a Request object to start building the RSpec.
#request = portal.context.makeRequestRSpec()
#request 
# Create a link with type LAN
link = request.LAN("lan")

# Generate the nodes
for i in range(4):
    node = request.XenVM("node" + str(i))
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU14-64-STD"
    iface = node.addInterface("if" + str(i))
    iface.component_id = "eth1"
    iface.addAddress(rspec.IPv4Address("192.168.1." + str(i + 1), "255.255.255.0"))
    link.addInterface(iface)
    
    node.addService(rspec.Execute(shell="/bin/sh",
                                  command="sudo wget http://apache.cs.utah.edu/hadoop/common/hadoop-3.0.0/hadoop-3.0.0.tar.gz"))
    node.addService(rspec.Execute(shell="/bin/sh",
                                  command="sudo tar xzf hadoop-3.0.0.tar.gz -C /opt/hadoop"))
    node.addService(rspec.Execute(shell="/bin/sh",
                                  command="sudo wget https://github.com/linhbngo/example-cloudlab/raw/master/master -O /opt/hadoop/conf/master"))
    node.addService(rspec.Execute(shell="/bin/sh",
                                  command="sudo wget https://github.com/linhbngo/example-cloudlab/raw/master/slaves -O /opt/hadoop/conf/slaves"))
    node.addService(rspec.Execute(shell="/bin/sh",
                                  command="sudo sleep 60"))
    node.addService(rspec.Execute(shell="/bin/sh",
                                  command="sudo /opt/hadoop/hadoop-daemon.sh start datanode"))
    if i == 0:
        node.routable_control_ip = True
        node.addService(rspec.Execute(shell="/bin/sh",
                                      command="sudo /opt/hadoop/bin/hdfs namenode -format PEARC18"))
        node.addService(rspec.Execute(shell="/bin/sh",
                                      command="sudo /opt/hadoop/bin/hdfs --daemon start namenode"))

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec(request)

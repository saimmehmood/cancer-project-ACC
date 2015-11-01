import os
import swiftclient.client
import time

config = {'username':os.environ['OS_USERNAME'], 
          'api_key':os.environ['OS_PASSWORD'],
          'project_id':os.environ['OS_TENANT_NAME'],
          'auth_url':os.environ['OS_AUTH_URL'],
           }
from novaclient.client import Client
nc = Client('2',**config)

print "Launching a new instance, may take some time."

# Make sure we are in the right directory
os.chdir('/Users/Jonas/Documents/Applied Cloud Computing/assignment3')

# Variables needed to boot a new instance
images = nc.images.list()
flavors = nc.flavors.list()
keys = nc.keypairs.list()
imageID = 0
flavorID = 0
publicKey = 0

# Get the right ID of the image we want to use when the instance is booted. 
for image in images:
    if (image.name == "Working Cell Profiler Grupp 7"):
        imageID = image.id
        
# Get the right ID of the flavor we want to use when the instance is booted.
for flavor in flavors:
    if (flavor.name == "m1.medium"):
        flavorID = flavor.id
        
# Get the public key which will be associated with the new instance
for key in keys:
    if (key.name == "jonasACCkey"):
        publicKey = key.name
        
# Read script file that will be used on instance boot
scriptFd = file("instance-script.sh")
scriptContent = scriptFd.read()

# Boot the new instance         
# newServer = nc.servers.create("Jonas-for-Cellprofiler", 
#               imageID, flavorID, key_name=publicKey, userdata=scriptContent)
newServer = nc.servers.create("Jonas-for-Cellprofiler", 
              imageID, flavorID, key_name=publicKey)

''' Now we want to assign a floating ip to the new 
    instance, but we have to wait a little while 
    to be sure that the instance has booted. '''
time.sleep(60)

# Find an avaiable floating IP
new_floatingIP = nc.floating_ips.create(
    nc.floating_ip_pools.find(name="ext-net").name)

# Assign the floating IP to the instance
newServer.add_floating_ip(new_floatingIP)

print "The new server IP is: " + str(new_floatingIP.ip)

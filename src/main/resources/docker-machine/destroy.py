#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from overtherepy import LocalConnectionOptions, OverthereHost, OverthereHostSession
from com.xebialabs.overthere import OperatingSystemFamily


print "Removing docker '{0}' machine ".format(machine_name)
command_line = "docker-machine rm --force {0}".format(machine_name)

localOpts = LocalConnectionOptions(os=OperatingSystemFamily.UNIX)
host = OverthereHost(localOpts)
session = OverthereHostSession(host)

print "Executing '{0}'....".format(command_line)
try:
    response = session.execute(command_line, check_success=False)
    for s in response.stdout:
        print s
    for s in response.stderr:
        print s
except:
    tb = traceback.format_exc()
    print "Error"
    print tb
finally:
    session.close_conn()

if response.rc != 0:
    sys.exit(response.rc)

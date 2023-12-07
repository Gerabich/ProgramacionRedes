# Fecha Moday 7 december
# Profesor: Gabriel Barrón R.
# Alumno Gerardo Antonio Garcia Vazquez
#Lab 2.8 - script 2

from ncclient import manager
import xml.dom.minidom

m = manager.connect(
         host="10.10.20.48",
         port=830,
         username="developer",
         password="C1sco12345",
         hostkey_verify=False
         )

netconf_reply = m.get_config(source="running")
print(netconf_reply)

netconf_data = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>NEWHOSTNAME</hostname>
  </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
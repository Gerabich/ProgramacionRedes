# Fecha Moday 7 december
# Profesor: Gabriel Barrón R.
# Alumno Gerardo Antonio Garcia Vazquez
#Lab 2.8 - script 1

from ncclient import manager 

m = manager.connect(
    host ="10.10.20.48",
    port=830,
    username="developer",
    password="C1sco12345",
    hostkey_verify=False
)

netconf_reply = m.get_config(source="running")
print(netconf_reply)

import xml.dom.minidom
print( xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml() )

netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
netconf_reply = m.get_config(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
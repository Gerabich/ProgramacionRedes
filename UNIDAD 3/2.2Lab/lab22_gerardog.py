'''
    Conexion 
    Nombre Gerardo Antonio Garcia Vazquez
    Fecha 24 nov 2023
'''
from netmiko import ConnectHandler

sshCli = ConnectHandler (
    device_type ='cisco_ios',
    host='10.10.20.48',
    port=22,
    username='developer',
    password='cisco123!'
)

Salida = sshCli.send_command('show ip int brief')
print(Salida)

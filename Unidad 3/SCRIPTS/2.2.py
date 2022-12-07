from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type= 'cisco_ios',
    host= '10.10.20.48',
    port= 22,
    username= 'developer',
    password= 'C1sco12345'
    )

config_commands = [
    'int loopback 1',
    'ip add 1.1.1.1 255.255.255.0',
    'description LABORATORIO 2.2'
]

resultado = sshCli.send_config_set(config_commands)
print(resultado)

from netmiko import ConnectHandler

username = 'admin'
password = 'cisco'
device_ip = '10.0.15.112'
device_par = {'device_type': 'cisco_ios',
                  'ip': device_ip,
                  'username': username,
                  'password': password,
                  }

with ConnectHandler(**device_par) as ssh:
    """config loopback / ACL for ssh / CDP interface description"""
    file_config = 'config.txt'
    config_sent = ssh.send_config_from_file(config_file=file_config)


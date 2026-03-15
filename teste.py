import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f' -> Hostname: {hostname}')
print(f' -> IP: {ip}')


# https://www.w3schools.com/python/ref_module_socket.asp
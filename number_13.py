# 10569

# from ipaddress import *
#
# net = ip_network('10.8.248.131/255.255.224.0', 0)
# print(net)


# 10575

# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f'118.193.30.139/{mask}', 0)
#     print(net, net.netmask)


# 10570

# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f'154.201.208.17/{mask}', 0)
#     print(net, net.netmask)


# 10571

# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f'122.21.49.91/{mask}', 0)
#     print(net)


# 10572

# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f'173.103.25.118/{mask}', 0)
#     print(net, 32 - mask)


# 10574

# from ipaddress import *
#
# k = 0
#
# for mask in range(33):
#     net = ip_network(f'158.116.11.146/{mask}', 0)
#     print(net)


# 10573

# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f'191.173.145.240/{mask}', 0)
#     print(net, net.num_addresses)


# 10576

# from ipaddress import *
#
# net = ip_network('0.0.0.0/255.255.240.0', 0)
# print(net.num_addresses - 2)


# 10577
#
# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f'162.112.200.70/{mask}', 0)
#     net1 = ip_network(f'162.112.175.80/{mask}', 0)
#     if net1 == net:
#         print(net)


# 10578

# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f'10.96.180.231/{mask}', 0)
#     net1 = ip_network(f'10.96.140.118/{mask}', 0)
#     if net != net1:
#         print(net, 32 - mask)


# 10579

# from ipaddress import *
#
# net = ip_network('192.168.240.0/255.255.255.0', 0)
# k = 0
#
# for ip in net:
#     bin_n = f"{ip:b}"
#     if bin_n.count('1') == bin_n.count('0'):
#         print(bin_n)
#         k += 1
#
# print(k)


# 10580

from ipaddress import *

net = ip_network('10.48.96.0/255.255.240.0', 0)
k = 0

for ip in net:
    bin_n = f"{ip:b}"
    if bin_n.count('1') > bin_n.count('0'):
        k += 1
print(k)

# 12467

# from ipaddress import *
#
# for a in range(256):
#     net = ip_network(f'183.192.{a}.0/255.255.252.0', 0)
#     b = f'{net.network_address:b}'
#
#     if b[16:].count('1') > 3:
#         print(a, net)


# 12245

# from ipaddress import *
#
# net = ip_network('192.168.32.48/255.255.255.240', 0)
#
# k = 0
# for n in net:
#     b = f'{n:b}'
#     if b.count('1') % 2 != 0:
#         k += 1
# print(k)


# 12102

# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f'175.184.52.103/{mask}', 0)
#     print(net)

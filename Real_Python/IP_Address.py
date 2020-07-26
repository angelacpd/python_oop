"""
IP Address Concepts With Python's ipaddress Module
https://realpython.com/python-ipaddress-module/
"""

import re

from ipaddress import IPv4Address
from ipaddress import IPv4Network
from ipaddress import IPv4Interface


# From string
addr = IPv4Address("220.14.9.37")
print(addr)
# From integer
print(IPv4Address(3691907365))
# From bytes
print(IPv4Address(b"\xdc\x0e\t%"))

# Return integer
print(int(addr))
# Return bytes
print(addr.packed)

# Instances of IPv4Address are hashable
print(hash(IPv4Address("220.14.9.37")))

num_connections = {IPv4Address("220.14.9.37"): 2,
                   IPv4Address("100.201.0.4"): 16,
                   IPv4Address("8.240.12.2"): 4}

print(num_connections)

print(IPv4Address("220.14.9.37") > IPv4Address("8.240.12.2"))

for a in sorted(num_connections):
    print(a)


# CIDR Notation
# Classless Inter-Domain Routing

net = IPv4Network("192.4.2.0/24")
print(net.num_addresses)
print(net.prefixlen)  # routing prefix
print(net.netmask)
print(IPv4Address("192.4.2.12") in net)
print(IPv4Address("192.4.20.2") in net)
IPv4Network("192.4.2.0/255.255.255.0")
net.broadcast_address

# Looping Through Networks

net2 = IPv4Network("192.4.2.0/28")
for address in net2:
    print(address)

h = net.hosts()
print(type(h))
print(next(h))
print(next(h))

# Subnets

small_net = IPv4Network("192.0.2.0/28")
big_net = IPv4Network("192.0.0.0/16")
small_net.subnet_of(big_net)
big_net.supernet_of(small_net)

net = IPv4Network("200.100.10.0/24")
for sn in net.subnets():
    print(sn)

for sn in net.subnets(new_prefix=28):
    print(sn)

# Host Interfaces

ifc = IPv4Interface("192.168.1.6/24")
ifc.ip  # The host IP address
ifc.network  # Network in which the host IP resides

# Special Address Ranges

IPv4Address("10.243.156.214") in IPv4Network("10.0.0.0/8")
timesync_addr = IPv4Address("169.254.169.123")
timesync_addr.is_link_local
IPv4Address("10.243.156.214").is_private
IPv4Address("127.0.0.1").is_loopback

[i for i in dir(IPv4Address) if i.startswith("is_")]  # "is_X" properties


# Composition’s Core Role

addr = IPv4Address("220.14.9.37")
addr._ip


# Extending IPv4Address

class MyIPv4(IPv4Address):
    def __and__(self, other: IPv4Address):
        if not isinstance(other, (int, IPv4Address)):
            raise NotImplementedError
        return self.__class__(int(self) & int(other))


addr = MyIPv4("100.127.40.32")
mask = MyIPv4("255.192.0.0")  # A /10 prefix
addr & mask
addr & 0xffc00000  # Hex literal for 255.192.0.0


class MyIPv4(IPv4Address):
    @property
    def binary_repr(self, sep=".") -> str:
        """Represent IPv4 as 4 blocks of 8 bits."""
        return sep.join(f"{i:08b}" for i in self.packed)

    @classmethod
    def from_binary_repr(cls, binary_repr: str):
        """Construct IPv4 from binary representation."""
        # Remove anything that's not a 0 or 1
        i = int(re.sub(r"[^01]", "", binary_repr), 2)
        return cls(i)


MyIPv4("220.14.9.37").binary_repr
MyIPv4("255.255.0.0").binary_repr  # A /16 netmask
MyIPv4.from_binary_repr("11011100 00001110 00001001 00100101")

```
Ip Addresses
```
- This Internet Protocol is from Layer 3 according to OSI Model.
- This IP is used to identify the devices in the internet.
- These IP's work as Source and Destination addresses when sending packets in an network.

```
IPv4
```
- IPv4 is 32 bit   ex: 192.168.0.1
- 2^32 IP's can be assigned. Total 4.3 Billion (4,294,967,296)
- But the population in the world is more that 8Billion. Hence, IPv4's are insufficient.
		To overcome this situation new NAT(Network Address Translator) was invented

```
			NAT
```
				This NAT helps in assigning multiple private IP's to one single 
				public IP. In this way the IPv4 is still being used.
				
```
IPv6
```
- The reason behind the invention of IPv6 is depletion of IPv4.
- IPv6 is 128 bit ex: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
		In this if we have continuous 0's we can compress it as 2001:0db8:85a3::8a2e:0370:7334
		2001:db8:0:0:0:0:0:1 ----->  2001:db8::1
		0:0:0:0:0:0:0:1  ------> ::1
- As IPv6 is 128 bit it can generate 2^128 IP's which is approximately (340,282,366,920,938,463,463,374,607,431,768,211,456) 340 undecillion i.e.;  3.4 x 10^38 addresses.
- From the above number these addressed can never be finished.

```
MAC Address
```

- This comes under the layer 2 in OSI model.
- It is a 48bit address which identifies each individual devices in a network.
- **Manufacturer's Identity (First Half):** The first 3 bytes (or the first 24 bits) of the MAC address represent the **Organizationally Unique Identifier (OUI)**. This part identifies the manufacturer or vendor of the network device. The IEEE Registration Authority assigns these OUIs to various manufacturers.
- **Device Identity (Second Half):** The last 3 bytes (or the last 24 bits) of the MAC address are assigned by the manufacturer itself and represent the unique identifier for the specific device. This ensures that each network interface card (NIC) produced by that manufacturer has a unique MAC address.

```
TCP and UDP
```

- These protocols falls under Layer 4 of OSI model.
- TCP (Transmission Control Protocol) is a connection oriented protocol while UDP (User Datagram Protocol) is a connection less protocol.
- Now, talking about the TCP is follows a 3 way handshake. Something like the following:
		Syn > Syn Ack > Ack
		#Note: It follows some flags like (Synchronization, Acknowledgement, Finish, Push, Reset, Urgent)......
![[Repo/Images/Pasted image 20250611173423.png]]

		The above diagram represents the 3 way handshake.
			This protocol guarantee that the packet reach the right destination at 
			any cost.
- Now, lets talk about the UDP. In this protocol there's no guarantee that the packet which is sent will reach the destination. It's something like throwing the packet towards the destination.
- This protocol is mainly used in Video Streaming, Gaming.
- This is faster comparing to the TCP protocol.

```
Subnetting
```

Follow the link: https://www.practicalnetworking.net/stand-alone/subnetting-mastery/


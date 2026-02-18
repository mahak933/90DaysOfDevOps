# Day 15 – Networking Concepts: DNS, IP, Subnets & Ports

🔹 Task 1: DNS – Converting Names into IP Addresses

1️⃣ What happens when you type google.com in a browser?

1.Your computer first checks its local DNS cache.
2.If the record isn’t cached, it forwards the request to the DNS resolver (ISP or configured DNS server).
3.The resolver performs a lookup through multiple layers:

Once the IP address is found, the browser uses it to establish a connection.

👉 In simple terms: DNS translates domain names into IP addresses the computer understands.

2️⃣ Common DNS Record Types

A → Maps a domain to an IPv4 address

AAAA → Maps a domain to an IPv6 address

CNAME → Points one domain name to another domain

MX → Directs email to mail servers

NS → Specifies the authoritative name servers for the domain


3️⃣ Using dig google.com
Command:
dig google.com

Findings:

A record: Something like 142.250.x.x

TTL : Usually around 300 seconds (but can vary)

TTL defines how long a DNS response can remain cached before it must be refreshed.

🔹 Task 2: IP Addressing

1️⃣ What is an IPv4 address?
1.An IPv4 address is a 32‑bit numeric label written in dotted‑decimal format, e.g.:
192.168.1.10
2.It consists of four octets and uniquely identifies a device on a network.

2️⃣ Public vs. Private IPs

Public IPs → Reachable over the internet (8.8.8.8)

Private IPs → Used inside internal networks (192.168.1.5)

Private IPs are non‑routable on the public internet.

3️⃣ Private IP Ranges

10.0.0.0 – 10.255.255.255

172.16.0.0 – 172.31.255.255

192.168.0.0 – 192.168.255.255


4️⃣ Using ip addr show

Command:
`ip addr show`

Observation:

My system shows a 192.168.x.x address → meaning it’s within a private LAN.

🔹 Task 3: CIDR & Subnetting

1️⃣ What does /24 mean?

192.168.1.0/24 means:

1.First 24 bits represent the network

2.Last 8 bits represent hosts

3.Subnet mask → 255.255.255.0


2️⃣ Usable Hosts per Subnet

/24 → 256 total → 254 usable

/16 → 65,536 total → 65,534 usable

/28 → 16 total → 14 usable

(Network and broadcast addresses are not assignable to hosts.)

3️⃣ Why subnet?

Subnetting helps by:

1.Structuring networks
2.Enhancing security
3.Reducing broadcast traffic
4.Improving address allocation

It’s especially essential in cloud environments like AWS VPCs.

4️⃣ CIDR Quick Reference Table

CIDRSubnet MaskTotal IPsUsable Hosts/24255.255.255.0256254/16255.255.0.065,53665,534/28255.255.255.2401614

🔹 Task 4: Ports – Where Services Live

1️⃣ What is a port?

A port is a logical endpoint inside a device.

IP identifies which machine

Port identifies which service on that machine


2️⃣ Common Ports

`Port`    `Service`
22 ----- SSH

80 ----- HTTP

443 ------ HTTPS

53 ----- DNS

3306 ----- MySQL

6379 ----- Redis

27017 ----- MongoDB

3️⃣ Using ss -tulpn

Command:
`ss -tulpn`

Observations:

Port 22 → SSH

Port 631 → CUPS (printing service)

Shows active services and listening ports.

🔹 Task 5: Bringing It All Together

1️⃣ What happens in curl http://myapp.com:8080?

1.DNS resolves the domain
2.IP routing sends the traffic to the destination
3.TCP establishes the connection
4.Port 8080 identifies the application backend
5.HTTP handles request–response communication

Multiple networking layers working in harmony.

2️⃣ App can't reach DB at 10.0.1.50:3306 — What to check?

1.Is the database service running?
2.Is port 3306 open/listening?
3.Firewall / Security Group rules?
4.Correct subnet routing?
5.Are both resources in the same network or VPC?

Since 10.x.x.x is private, connectivity depends heavily on internal network configuration.

🌟 What I Learned (Summary)

1.DNS is a structured lookup system, not magic.
2.CIDR defines network size and available hosts.
3.IP identifies a machine; Port identifies a specific service.

Networking feels much more logical now, and not just a set of random commands.

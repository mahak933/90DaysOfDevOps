## Hands-on Checklist (run these; add 1–2 line observations)

- Identity: `hostname -I` (or `ip addr show`) — note your IP.
- Reachability: `ping <target>` — mention latency and packet loss.
- Path: `traceroute <target>` (or `tracepath`) — note any long hops/timeouts.
- Ports: `ss -tulpn` (or `netstat -tulpn`) — list one listening service and its port.
- Name resolution: `dig <domain>` or `nslookup <domain>` — record the resolved IP.
- HTTP check: `curl -I <http/https-url>` — note the HTTP status code.
- Connections snapshot: `netstat -an | head` — count ESTABLISHED vs LISTEN (rough).

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/ff93f9390ac04dca8ca17e27c5224cb8fb22be18/2026/day-14/netwrk1.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/ff93f9390ac04dca8ca17e27c5224cb8fb22be18/2026/day-14/netwrk2.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/ff93f9390ac04dca8ca17e27c5224cb8fb22be18/2026/day-14/netwrk3.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/ff93f9390ac04dca8ca17e27c5224cb8fb22be18/2026/day-14/netwrk4.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/ff93f9390ac04dca8ca17e27c5224cb8fb22be18/2026/day-14/netwrk5.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/ff93f9390ac04dca8ca17e27c5224cb8fb22be18/2026/day-14/netwrk6.png)

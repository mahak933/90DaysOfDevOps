# Linux Troubleshooting Runbook

- Day 05 – CPU, Memory & Logs Analysis
----------
Today’s goal was to practice a structured troubleshooting workflow—capturing system state, validating service health, and reviewing logs to build a repeatable approach for incident response.

- Target Service
-----------
Service: `ssh`

Reason: Always running, essential for system access, and easy to inspect through logs and network checks.

-  Environment Validation
----------

1️⃣ OS & Kernel

`uname -a`
`cat /etc/os-release`

Observation:

Kernel version and OS distribution verified successfully.

📁 Filesystem Check

2️⃣ Temporary Workspace

`mkdir /tmp/runbook-demo`

`cp /etc/hosts /tmp/runbook-demo/hosts-copy`

`ls -l /tmp/runbook-demo`

Observation:

Filesystem is writable; permissions are normal and consistent.

- CPU & Memory Snapshot

3️⃣ System-wide Resource View
`top`

- Observation:

Low CPU load and stable memory usage; nothing abnormal.

4️⃣ Process-specific Usage

`ps -o pid`,`pcpu`,`pmem`,`comm -C sshd`

Observation:

shd is using negligible CPU and memory.

5️⃣ Memory Overview

`free -h`

Observation:

Plenty of free memory; no swap pressure detected.

- Disk & I/O Snapshot

6️⃣ Disk Usage

`df -h`

Observation:

Root filesystem has adequate free space.

7️⃣ Log Directory Size

`du -sh /var/log`

Observation:

Log directory size is normal; no excessive log growth.

-  Network Snapshot

8️⃣ Listening Ports

`ss -tulpn | grep ssh`

Observation:

SSH is actively listening on port 22.

9️⃣ Local Connectivity

`curl -I localhost`

Observation:

Local network stack responding correctly.

- Log Review

🔟 systemd Logs

`journalctl -u ssh -n 50`

Observation:

No recent failures or warnings.

1️⃣1️⃣ Authentication Logs

`tail -n 50 /var/log/auth.log`

Observation:

Only normal login attempts; no suspicious activity.

------- 

✅ Quick Summary

1.SSH service is healthy and stable
2.CPU, memory, disk, and network usage all within normal ranges
3.No error patterns detected in recent logs
4.verall system is functioning normally


- If the Issue Escalates: Recommended Next Steps
  
1️⃣ Safe Restart

`systemctl restart ssh`

-Monitor CPU, memory, and logs immediately afterward.

2️⃣ Increase Visibility

`journalctl -u ssh -f`

- Capture real-time logging.

3️⃣ Deep Diagnostics

`strace -p <PID>`

Monitor system calls for unusual behavior.

--------------

# Final Notes

This exercise helped reinforce a structured troubleshooting approach—gathering evidence across CPU, memory, disk, network, and logs before taking action.

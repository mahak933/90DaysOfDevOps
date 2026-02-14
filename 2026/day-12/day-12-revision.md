# Day 12 Review – Mindset Reset & Progress Check
------------

- SECTION 1: MINDSET & PLAN REVISIT
---------

🔹 Original Day 01 Goals

My initial objectives were clear and foundational:

1.Build strong Linux fundamentals for DevOps
2.Become confident with the command line
3.Learn system administration basics
4.Prepare for real-world server management
5.Develop structured troubleshooting skills

🔹 Progress After 11 Days

✅ What I’ve Successfully Achieved

1.Confident with essential navigation (cd, ls, pwd, cat)
2.Solid with file operations (create, copy, move, edit)
3.Comfortable using chmod (symbolic + numeric)
4.Confident using chown & chgrp for ownership
5.Understand user & group management basics
6.Can monitor processes and system state effectively

🎯 Still in Progress
-------

1.Service management (limited systemd exposure)
2.Log analysis and deeper troubleshooting
3.Complex permissions and ACL scenarios
4.Multi-step incident investigation flow

📌 Not Started Yet
------

.1Advanced network troubleshooting
2.Package management (apt/yum)
3.Shell scripting
4.Automation + CI/CD techniques


🔹 Plan Adjustments

✔️ What’s Working Well

1.Hands-on daily practice
2.Documenting every command & observation
3.Structured challenges enhancing clarity
4.Combining theory + practice

Tweaks Needed
------

1.Need more practice in full systemd environments
2.Add weekly “incident simulation”
3.Start building a personal runbook/playbook
4.Begin timing myself for speed
5.Practice explaining concepts aloud

🎯 New Focus for the Next Phase
-------

1.Continue daily structured learning
2.Add realistic troubleshooting scenarios
3.Build a personal cheat sheet/runbook
4.Practice in production-like setups
5.Start combining multiple skills into complex tasks


- SECTION 2: PROCESSES & SERVICES
--------

Command 1: Memory-Based Process Sorting

`ps aux--sort=-%mem` | `head -10`

🔍 Observations

1.Main daemon ~19MB RSS (normal)
2.VSZ > RSS (expected for most processes)
3.Short-lived processes have tiny footprints
4.No memory pressure
5.Process states understood: Ssl, S, R

🧠 Key Learnings
-------

1.RSS = actual physical memory used
2.VSZ = total virtual allocation (not real RAM)
3.Focus on RSS + %MEM for real memory evaluation
4.Sorting helps detect leaks quickly


Command 2: System Snapshot via top

`top -b -n 1` | `head -20`

🔍 Observations

1.Load average 0.00 → system fully idle
2.1 running task, 0 zombies → healthy state
3.100% CPU idle, 0% I/O wait
4.9GB+ memory free, no swap usage
5.Top process only 9% CPU

🧠 Key Learnings

1.Load < CPU cores = healthy
2.Zero zombies = clean process lifecycle
3.High I/O wait (“wa”) = disk bottlenecks
4.Idle CPU is ideal for server workloads


Service Management Attempt

System returned:

System has not been booted with systemd as init system

🔍 Observations

1.Environment doesn’t use systemd
2.PID 1 = process_api
3.Likely containerized/minimal environment
4.systemctl unavailable

🧠 Production Checklist
------

`systemctl status <service>`

`systemctl list-units --type=service --state=running`

`systemctl --failed`

`journalctl -u <service> -n 50`

`journalctl -u <service> -f`

Key Learning

1.Always check PID 1 to identify init system
2.Containers often use minimal init systems


- SECTION 3: FILE SKILLS PRACTICE
--------

1️⃣ Append to File

✔ Correct use of >> operator

Preserves existing content.

2️⃣ Directory Creation

mkdir -p app/src app/docs app/tests

✔ Nested directories created successfully.

3️⃣ Permissions

chmod 755 script.sh

chmod 640 config.conf

✔ Proper permission models applied.

4️⃣ Copy Files

cp practice.txt practice-backup.txt

✔ Identical copy validated.

5️⃣ Ownership Change

chown devuser:devops devops-file.txt

✔ Ownership updated correctly.

- SECTION 4: TOP 5 INCIDENT COMMANDS
------------

1️⃣ ps aux --sort=-%cpu | head

Find CPU hogs immediately.

2️⃣ top

Instant system-wide status.

3️⃣ df -h

Disk full = #1 cause of failures.

4️⃣ systemctl status / journalctl -u

Direct service health & logs.

5️⃣ tail -f /var/log/syslog

Live log monitoring.

Honorable Mentions

free -h, ss -tulpn, last, grep -i error, ls -lh /var/log/

- SECTION 5: USER/GROUP SCENARIO
----------

✔ Create user + group

✔ Assign ownership

✔ Verify with id and ls -l

Key takeaway: Always verify before & after changes.

📝 MINI SELF-CHECK

Q1: Top 3 time-saving commands

ls -lh

ps aux --sort

chown user:group file

Q2: How to check if a service is healthy?

systemctl status <service>

journalctl -u <service> -n 50

pgrep -a <service>

Q3: Safely change ownership/permissions

Check → Change → Verify

Example:

chown webapp:www-data file

chmod 640 file

Q4: Focus for next 3 days

Network troubleshooting

Log analysis

Multi-step incident drills

Speed + automation


📊 KEY TAKEAWAYS FROM REVISION
--------------

Solid Skills Built

1.File operations
2.Permissions
3.Ownership
4.Process monitoring
5.User/group management
6.Navigation

Skills Needing More Practice
--------

1.systemd
2.journalctl
3.Network diagnostics
4.Scripting
5.Speed under pressure


🎓 REFLECTION: PROGRESS SINCE DAY 1
-----------

Before:

Hesitant with CLI

Afraid of breaking things

Needed Google for everything

Now:

Confident navigating Linux

Understand what commands do, not just how to run them

Prefer CLI for many tasks

Have strong mental models

Practical Growth

Week 1: survival skills

Week 2: confidence & real problem-solving


📋 RETENTION CHECKLIST

Commands I can recall instantly

ls, cd, pwd, cat, echo, chmod, chown, ps, top, df, mkdir, cp

Concepts I understand well

permissions, ownership, process states, CPU/memory metrics

Areas developing

systemd, journalctl, network tools, scripting, log correlation

🎯 ACTION PLAN FOR NEXT 3 DAYS
----------
`Today`

Review

Practice incident commands

Revisit user/group tasks

`Day 13`

Network troubleshooting

Time-based drills

Build runbook v1

`Day 14`

Log parsing with grep/awk/sed

Journalctl filters

Simulate incidents

`Day 15`

Speed drills

Complex multi-step tasks

Plan next learning phase


💡 INSIGHTS & OBSERVATIONS
--------

What made learning stick

Hands-on repetition

Documenting observations

Real scenarios

Connecting concepts

What I’d do differently

Start cheat sheet earlier

More realistic environments

Weekly reviews sooner

Practice teaching concepts

Best discoveries

ls -l is incredibly powerful

Process states reveal system health

Permissions + ownership = security foundation

80% of incidents solved with top 5 commands

Muscle memory grows fast


# FINAL NOTES
------

These first 12 days built a strong foundation:

✔ File operations

✔ Permissions

✔ Ownership

✔ Process monitoring

✔ User/group management

The next phase will focus on:

🔥 Network troubleshooting

🔥 Deep log analysis

🔥 Faster incident response

🔥 Real-world DevOps readiness

- Biggest win:
I’m no longer intimidated by the command line — I understand what I’m doing, why I’m doing it, and how systems behave.
Excited and ready for Day 13!Provide your feedback on BizChat

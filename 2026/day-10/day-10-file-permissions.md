Day 10 Challenge - File Permissions & File Operations
------------------------------------------------------

- Task 1: Create Files (10 minutes)
1. Create empty file `devops.txt` using touch
2. Create  `notes.txt` with some content using cat or echo
3. Create `script.sh` using vim with content: echo "Hello DevOps"
Verify: `ls -l` to see permissions

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/fc73c35ab02321c08b61a93fb5344f0e30693553/2026/day-10/step1.png)

----------------------------------------------------------------------------------------------------------------------------

- Task 2: Read Files (10 minutes)
1. Read notes.txt using cat
2. View script.sh in vim read-only mode
3. Display first 5 lines of /etc/passwd using head
4. Display last 5 lines of /etc/passwd using tail

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/fc73c35ab02321c08b61a93fb5344f0e30693553/2026/day-10/step2.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/fc73c35ab02321c08b61a93fb5344f0e30693553/2026/day-10/step3.png)

-----------------------------------------------------------------------------------------------------------------------------
- Task 3: Understand Permissions (10 minutes)
 Format: rwxrwxrwx (owner-group-others)
`r = read (4), w = write (2), x = execute (1)`
Check your files: ls -l devops.txt notes.txt script.sh
Answer: What are current permissions? Who can read/write/execute?

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/fc73c35ab02321c08b61a93fb5344f0e30693553/2026/day-10/step4.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/fc73c35ab02321c08b61a93fb5344f0e30693553/2026/day-10/step5.png)

----------------------------------------------------------------------------------------------------------------------------

- Task 4: Modify Permissions (20 minutes)
1. Make script.sh executable → run it with `./script.sh`
2. Set `devops.txt` to read-only (remove write for all)
3. Set notes.txt to 640 (owner: rw, group: r, others: none)
4. Create directory project/ with `permissions 755`
Verify: ls -l after each change

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/fc73c35ab02321c08b61a93fb5344f0e30693553/2026/day-10/step6.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/fc73c35ab02321c08b61a93fb5344f0e30693553/2026/day-10/step7.png)

----------------------------------------------------------------------------------------------------------------------------


- What I Learned
1. Permission Structure and Numeric Notation
Linux permissions use a three-tier system (owner-group-others) with three types of access (read-write-execute). The numeric notation (e.g., 755, 644) is calculated by adding permission values: read=4, write=2, execute=1. This makes permission management precise and efficient. For example, 755 means owner has full access (7=4+2+1), while group and others can read and execute (5=4+1).

2. Execute Permission is Essential for Scripts
A file containing valid shell code cannot run as a script without the execute permission bit set. Even with a proper shebang (#!/bin/bash) and correct syntax, the system will return "Permission denied" (exit code 126) when attempting to execute. The chmod +x command grants this permission, transforming a text file into an executable program.

3. Read-Only Protection is Fundamental to Security
Setting files to read-only (444 or using chmod -w) provides protection against accidental or unauthorized modification. This is crucial for configuration files, logs, and critical system data. Regular users cannot override read-only permissions, ensuring data integrity. Combined with proper ownership and group permissions (like 640), you can create fine-grained access control for multi-user systems.



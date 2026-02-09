Challenge Tasks
-----------------

- Task 1: Create Users (20 minutes)
Create three users with home directories and passwords:
`useradd -m username -p password`
Verify: Check /etc/passwd and /home/ directory

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/16e86072278d822111502a2981db8e29123046cd/2026/day-09/task1_create_user.png)

-----------------------------------------------------------------------------------------------------------------------------

- Task 2: Create Groups (10 minutes)
Create two groups:
`groupadd groupname`
Verify: Check /etc/group

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/16e86072278d822111502a2981db8e29123046cd/2026/day-09/task2_create_group.png)

-----------------------------------------------------------------------------------------------------------------------------

- Task 3: Assign to Groups (15 minutes)
Assign users:
`usermod -aG groupname username`
Verify: Use appropriate command to check group membership

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/16e86072278d822111502a2981db8e29123046cd/2026/day-09/task3_assigntogroup.png)

-----------------------------------------------------------------------------------------------------------------------------

- Task 4: Shared Directory (20 minutes)
Create directory: `/opt/dev-project`
Set group owner to developers
Set permissions to 775 (rwxrwxr-x)
Test by creating files as tokyo and berlin
Verify: Check permissions and test file creation

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/16e86072278d822111502a2981db8e29123046cd/2026/day-09/task4_create_files.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/16e86072278d822111502a2981db8e29123046cd/2026/day-09/task4_shared_dir.png)

-----------------------------------------------------------------------------------------------------------------------------

- Task 5: Team Workspace (20 minutes)
Create user `nairobi` with home directory
Create group `project-team`
Add `nairobi` and `tokyo` to `project-team`
Create `/opt/team-workspace` directory
Set group to project-team, permissions to 775
Test by creating file as nairobi

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/16e86072278d822111502a2981db8e29123046cd/2026/day-09/task5.1.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/16e86072278d822111502a2981db8e29123046cd/2026/day-09/task5.2.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/16e86072278d822111502a2981db8e29123046cd/2026/day-09/task5.3.png)


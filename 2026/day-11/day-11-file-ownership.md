Challenge Tasks
----------------

## Task 1: Understanding Ownership (10 minutes)

Run `ls -l` in your home directory

Identify the owner and group columns

Check who owns your files

Format: -rw-r--r-- 1 owner group size date filename

Document: What's the difference between owner and group?


![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/670bd2a6b38246b59d37d4bd2e9233e175fba263/2026/day-11/task1.png)

---------

## Task 2: Basic chown Operations (20 minutes)

Create file `devops-file.txt`

Check current owner: `ls -l devops-file.txt`

Change owner to `tokyo` (create user if needed)

Change owner to `berlin`

Verify the changes

Try:`sudo chown tokyo devops-file.txt`

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/670bd2a6b38246b59d37d4bd2e9233e175fba263/2026/day-11/task2.1.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/670bd2a6b38246b59d37d4bd2e9233e175fba263/2026/day-11/task2.2.png)


------------

## Task 3: Basic chgrp Operations (15 minutes)

Create file `team-notes.txt`

Check current group: `ls -l team-notes.txt`

Create group: `sudo groupadd heist-team`

Change file group to `heist-team`

Verify the change

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/670bd2a6b38246b59d37d4bd2e9233e175fba263/2026/day-11/task3.png)


-------------

## Task 4: Combined Owner & Group Change (15 minutes)
  
Using chown you can change both owner and group together:

Create file `project-config.yaml`

Change owner to `professor` AND group to `heist-team` (one command)

Create directory `app-logs/`

Change its owner to `berlin` and group to `heist-team`

Syntax: `sudo chown owner:group filename`

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/670bd2a6b38246b59d37d4bd2e9233e175fba263/2026/day-11/task4.1.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/670bd2a6b38246b59d37d4bd2e9233e175fba263/2026/day-11/task4.2.png)


------

## Task 5: Recursive Ownership (20 minutes)
  
Create group planners: `sudo groupadd planners`

Change ownership of entire `heist-project/` directory:

Owner: `professor`
Group: `planners`

Use recursive flag (-R)

Verify all files and subdirectories changed: `ls -lR heist-project/`

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/670bd2a6b38246b59d37d4bd2e9233e175fba263/2026/day-11/task5.png)

--------

## Task 6: Practice Challenge (20 minutes)

Create users: `tokyo`, `berlin`, `nairobi` (if not already created)

Create groups: `vault-team`, `tech-team`

Create directory: `bank-heist/`

# Set different ownership:

- access-codes.txt → owner: tokyo, group: vault-team
- blueprints.pdf → owner: berlin, group: tech-team
- escape-plan.txt → owner: nairobi, group: vault-team
  
Verify: `ls -l` bank-heist/

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/670bd2a6b38246b59d37d4bd2e9233e175fba263/2026/day-11/task6.png)


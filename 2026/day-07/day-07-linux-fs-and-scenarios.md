Day 07 – Linux File System Hierarchy & Scenario-Based Practice
----------------------------------------------------------------
`/ directory`

- it is the root directory & everying is inside / directory`
  
`/home`

- home directory for normal user user
- it conatins user folder inside home directory
  
`/root`  or `~`

-it is home directory for root user contains .bashrc , .bash_history ,.ssh
-it contains .ssh file which contains authorised key file in which we have add a public key of other user
-it also conatins .bashrc file which is used to add root user level alias

`/etc` 

-it contains system configuration file`
-it contains passwd , group , shadow ,hosts files

`/var`

-its contains log folder which contains system & application logs
-it aslo conatins mail folder

`/tmp`

-it contains termparary files & be auto cleaned on reboot

`/bin`

-it contains system cmds for system boot & recovey cmds

`usr/bin`

- it contains user cmds

`/opt`

- install external applications inside this directory

`/mount`

- is used to tempararily mount external storage blocks

`/media`

-it will shows external connected device files


Step 1: Check service status
-----------------------------


Step 2: If service is not found, list all services
---------------------------------------------------



Step 3: Check if service is enabled on boot
--------------------------------------------




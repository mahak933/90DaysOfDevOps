Day-13 Challenge Tasks
-----------------------

- Task 1: Check Current Storage

`lsblk`

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/f39e10eff117540697dea5c1396541ea8525cc15/2026/day-13/step1.png)


- Task 2: Create Physical Volume

`pvcreate /dev/block_name`   # or your loop device
 pvs
![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/f39e10eff117540697dea5c1396541ea8525cc15/2026/day-13/step2.png)


- Task 3&4: Create Volume Group and Logical Volume

`vgcreate group_name /dev/block_name`
 vgs
`lvcreate -L 500M -n lvm_name group_name`
 lvs
 
![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/f39e10eff117540697dea5c1396541ea8525cc15/2026/day-13/step3%264.png)


- Task 5: Format and Mount
  
`mkfs.ext4 /dev/group_name/lvm_name`

`mkdir -p /mnt/app-data`

`mount /dev/group_name/lvm_name /mnt/app-data`

`df -h /mnt/app-data`

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/f39e10eff117540697dea5c1396541ea8525cc15/2026/day-13/file-format.png)


-Task 6: Extend the Volume

`lvextend -L 5G /dev/group_name/lvm_name`

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/f39e10eff117540697dea5c1396541ea8525cc15/2026/day-13/volum-extend.png)


-Volume Tree

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/f39e10eff117540697dea5c1396541ea8525cc15/2026/day-13/volumetree.png)


-Mounting

`df -h /mnt/app-data`

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/f39e10eff117540697dea5c1396541ea8525cc15/2026/day-13/mount.png)

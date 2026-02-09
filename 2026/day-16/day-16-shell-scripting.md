Challenge Tasks
----------------

- Task 1: Your First Script
1. Create a file `hello.sh`
2. Add the shebang line `#!/bin/bash` at the top
3. Print `Hello, DevOps!` using echo
Make it executable and run it
`chmod +x hello.sh`
`./hello.sh`
Document: What happens if you remove the shebang line?

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/dc93daa3b2ccb85309890fea5f92b5b665366d06/2026/day-16/task1.png)


-----------------------------------------------------------------------------------------------------------------------------

- Task 2: Variables
1. Create variables.sh with:
2. A variable for your NAME
3. A variable for your ROLE (e.g., "DevOps Engineer")
Print: Hello, I am <NAME> and I am a <ROLE>
Try using single quotes vs double quotes — what's the difference?

`example`

name = mahak

echo '$name'

echo "$name"

`output`

$name

mahak


-----------------------------------------------------------------------------------------------------------------------------

- Task 3: User Input with read
Create greet.sh that:
Asks the user for their name using read
Asks for their favourite tool
Prints: Hello <name>, your favourite tool is <tool>

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/dc93daa3b2ccb85309890fea5f92b5b665366d06/2026/day-16/task2_task3.png)

-----------------------------------------------------------------------------------------------------------------------------

- Task 4: If-Else Conditions
1. Create check_number.sh that:

Takes a number using read

Prints whether it is positive, negative, or zero

Create `file_check.sh` that:

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/dc93daa3b2ccb85309890fea5f92b5b665366d06/2026/day-16/check_num.sh.png)


2. Asks for a filename

Checks if the file exists using `-f`

Prints appropriate message

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/dc93daa3b2ccb85309890fea5f92b5b665366d06/2026/day-16/file_check.png)

-----------------------------------------------------------------------------------------------------------------------------

- Task 5: Combine It All
1. Create `server_check.sh` that:

Stores a service name in a variable (e.g., nginx, sshd)

Asks the user: "Do you want to check the status? (y/n)"

If y — runs systemctl status <service> and prints whether it's active or not

If n — prints "Skipped."

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/dc93daa3b2ccb85309890fea5f92b5b665366d06/2026/day-16/server_check.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/dc93daa3b2ccb85309890fea5f92b5b665366d06/2026/day-16/task5.png)

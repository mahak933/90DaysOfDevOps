## Challenge Tasks

- Task 1: Basic Functions
  
1. Create `functions.sh` with:
2. A function greet that takes a name as argument and prints `Hello, <name>!`
3. A function add that takes two numbers and prints their `sum`
4. Call both functions from the script

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/ba6fea5100a31f740a2ebb150df2db8102bf4a6c/2026/day-18/task1.png)


-------------------------------

- Task 2: Functions with Return Values
  
1. Create `disk_check.sh` with:
2. A function check_disk that checks disk usage of / `using df -h`
3. A function check_memory that checks free memory using `free -h`
4. A `main` section that calls both and prints the results

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/ba6fea5100a31f740a2ebb150df2db8102bf4a6c/2026/day-18/task2.png)


------------------------------------

- Task 3: Strict Mode — set -euo pipefail

1. Create `strict_demo.sh` with `set -euo pipefail` at the top
2. Try using an undefined variable — what happens with `set -u`?
3. Try a command that fails — what happens with `set -e`?
4. Try a piped command where one part fails — what happens with `set -o pipefail`?

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/ba6fea5100a31f740a2ebb150df2db8102bf4a6c/2026/day-18/task3.png)


Document: What does each flag do?
Flag             Meaning                             Effect
set -e           Exit on error                       Script stops if any command fails
set -u           Undefined variable is an error      Prevents using variables that were not initialized
set -o pipefail  Pipeline fails if any step fails    Ensures reliable piped commands

------------------------------------------

- Task 4: Local Variables

1. Create `local_demo.sh` with:
2. A function that uses `local keyword` for variables
3. Show that local variables don't leak outside the function
4. Compare with a function that uses regular variables

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/ba6fea5100a31f740a2ebb150df2db8102bf4a6c/2026/day-18/task4.png)


----------------------------

- Task 5: Build a Script — System Info Reporter
1. Create `system_info.sh` that uses functions for everything:
2. A function to print `hostname` and `OS info`
3. A function to print `uptime`
4. A function to print `disk usage` (top 5 by size)
5. A function to print `memory usage`
6. A function to print `top 5 CPU-consuming processes`
7. A main function that calls all of the above with section headers
8. Use `set -euo pipefail` at the top

Output should look clean and readable.

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/ba6fea5100a31f740a2ebb150df2db8102bf4a6c/2026/day-18/task5_script.png)

![image alt](https://github.com/mahak933/90DaysOfDevOps/blob/ba6fea5100a31f740a2ebb150df2db8102bf4a6c/2026/day-18/task5_output.png)


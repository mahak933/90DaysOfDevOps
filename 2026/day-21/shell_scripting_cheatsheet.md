# 🐚 Shell Scripting Cheat Sheet

## 📌 Quick Reference Table

| Topic      | Key Syntax              | Example                              |
| ---------- | ----------------------- | ------------------------------------ |
| Variable   | `VAR="value"`           | `NAME="DevOps"`                      |
| Argument   | `$1`, `$2`              | `./script.sh arg1`                   |
| If         | `if [ cond ]; then`     | `if [ -f file ]; then`               |
| For        | `for i in list; do`     | `for i in 1 2 3; do`                 |
| Function   | `name() { … }`          | `greet() { echo Hi; }`               |
| Grep       | `grep pattern file`     | `grep -i error log.txt`              |
| Awk        | `awk '{print $1}'`      | `awk -F: '{print $1}' /etc/passwd`   |
| Sed        | `sed 's/a/b/g' file`    | `sed -i 's/foo/bar/g' f.txt`         |

---

## 1️⃣ Basics

### Shebang
```bash
#!/bin/bash
```
Tells the system which interpreter to use.

### Run a Script
```bash
chmod +x script.sh
./script.sh
bash script.sh
```

### Comments
```bash
# Single line
echo "Hi"   # Inline comment
```

### Variables
```bash
NAME="DevOps"
echo "$NAME"     # expands
"$NAME"         # preserves spaces
'$NAME'         # literal string
```

### Read Input
```bash
read -p "Enter name: " NAME
```

### Arguments & Special Vars
```bash
$0  # script name
$1  # first arg
$#  # total args
$@  # all args (split as words)
$*  # all args (single word if quoted)
$?  # last command exit code
$$  # current script PID
```

---

## 2️⃣ Operators & Conditionals

### String Tests
```bash
[ "$a" = "$b" ]
[ -z "$a" ]
[ -n "$a" ]
```

### Integer Tests
```bash
[ "$a" -eq 5 ]
[ "$a" -gt 3 ]
[ "$a" -le 10 ]
```

### File Tests
```bash
[ -f file ]  # regular file
[ -d dir  ]  # directory
[ -e path ]  # exists
[ -r file ]  # readable
[ -w file ]  # writable
[ -x file ]  # executable
[ -s file ]  # size > 0
```

### If / Else
```bash
if [ cond ]; then
  echo yes
elif [ cond ]; then
  echo maybe
else
  echo no
fi
```

### Logical Operators
```bash
cmd1 && cmd2   # run cmd2 if cmd1 succeeds
cmd1 || cmd2   # run cmd2 if cmd1 fails
! cmd          # negate exit status
```

### Case
```bash
case "$var" in
  start) echo "Starting" ;;
  stop)  echo "Stopping" ;;
  *)     echo "Unknown" ;;
esac
```

---

## 3️⃣ Loops

### For Loops
```bash
for i in 1 2 3; do echo "$i"; done

for ((i=0; i<5; i++)); do
  echo "$i"
done
```

### While Loop
```bash
i=1
while [ "$i" -le 5 ]; do
  echo "$i"
  ((i++))
done
```

### Until Loop
```bash
i=1
until [ "$i" -gt 5 ]; do
  echo "$i"
  ((i++))
done
```

### Loop Control
```bash
break
continue
```

### Loop Through Files
```bash
for f in *.log; do echo "$f"; done
```

### Read File Line-by-Line
```bash
# Safe IFS + read loop (handles spaces) without UUOC
while IFS= read -r line; do
  echo "$line"
done < file
```

---

## 4️⃣ Functions

```bash
greet() {
  local name=$1
  echo "Hello $name"
}

greet DevOps
```

**Return vs Echo**
```bash
return 0   # exit status only
echo data  # prints value to stdout
```

---

## 5️⃣ Text Processing

### grep
```bash
grep -i pattern file
grep -r pattern dir
grep -c pattern file
grep -n pattern file
grep -v pattern file
grep -E "a|b" file
```

### awk
```bash
awk '{print $1}' file
awk -F: '{print $1}' /etc/passwd
awk 'BEGIN{print "Start"} {print $1} END{print "End"}' file
```

### sed
```bash
sed 's/old/new/g' file
sed -i 's/old/new/g' file
sed '3d' file
```

### Other Handy Tools
```bash
cut -d, -f1 file
sort -n file
uniq -c file
tr 'a-z' 'A-Z'
wc -l file
head -n 10 file
tail -f file
```

---

## 6️⃣ Useful One-Liners
```bash
find . -type f -mtime +7 -delete
wc -l *.log
sed -i 's/foo/bar/g' *.conf
systemctl is-active nginx
watch -n 5 df -h
```

---

## 7️⃣ Error Handling & Debugging
```bash
exit 0
exit 1
echo $?

set -e          # exit on error
set -u          # error on undefined vars
set -o pipefail # pipeline fails if any command fails
set -x          # print commands (debug)

trap 'echo Cleanup' EXIT
```

---

## ✅ Tips & Best Practices
- Always **quote variables**: `"$var"` to avoid word-splitting and globbing.
- Prefer `[[ ... ]]` for Bash-specific conditionals when available.
- Use `shellcheck` to lint scripts: `shellcheck script.sh`.
- Keep scripts **idempotent** and **fail-fast** with `set -euo pipefail` where suitable.
- For portability, target POSIX `sh`; for features, use Bash and declare `#!/usr/bin/env bash`.

---

# Git Commands Cheat Sheet

1. Setup & Config

`git --version`
to know the version of the git

`git config user.name <name>`
to configure the username

`git config user.email <email>`
to configure the email address

`git init`
Initializes a new Git repository.

`git checkout -b <branchname>`
to create new branch and redirect on same

`git branch -m <new-name>`
Renames the current branch.

`git remote add origin <url>`
Adds a remote repository.


---

## 2. Basic Workflow

`git add <file>`
Stages a file.

`git add .`
Stages all changes.

`git commit -m "<message>"`
Creates a commit with a message.

`git push -u origin <branch>`
Pushes commits to a remote repository.


---

## 3. Viewing Changes

`git status`
Shows repository status.

`git branch`
Lists local branches.

`git log`
Shows commit history.

`git diff`
Shows differences between working files.

---

## Extra Commands

`git clone <url>`
Clones a remote repository.

`git pull`
Fetches and merges changes from remote.


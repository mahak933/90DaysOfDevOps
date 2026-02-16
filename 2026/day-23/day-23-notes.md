
## Challenge Tasks

### Task 1: Understanding Branches

1. What is a branch in Git?

A **branch** in Git is a movable pointer to a commit. It represents an independent line of development, allowing you to work on new features, bug fixes, or experiments without affecting the main project history.

---

2. Why do we use branches instead of committing everything to `main`?
We use branches because:

- They **isolate changes** so work in progress doesn’t break stable code.
- They allow **multiple features** to be developed independently.
- They make it easier to **review code** before merging.
- They help maintain a clean and predictable **project history**.
- Teams can collaborate without interfering with each other’s work.

This keeps the `main` branch stable, production‑ready, and clean.

---

3. What is HEAD in Git?
**HEAD** is a reference that points to your **current branch** and the **latest commit** you are working on. 

In simple terms: 
> HEAD tells you “where you currently are” in the repository.

Examples:
- If you are on the `main` branch → HEAD points to `main`.
- After a commit → HEAD points to the new commit.
- In detached HEAD state → HEAD points directly to a specific commit, not a branch.

---

4. What happens to your files when you switch branches?

When you switch branches using `git switch <branch>` or `git checkout <branch>`:

- Git **updates files in your working directory** to match the state of that branch.
- Any tracked files will change to reflect the version stored in the branch you just switched to.
- Uncommitted changes may cause conflicts or prevent switching branches.

In short:
> Git rewrites your working directory to look exactly like the branch you're moving to.

---

### Task 2: Branching Commands — Hands-On
In your `devops-git-practice` repo, perform the following:
1. List all branches in your repo
2. Create a new branch called `feature-1`
3. Switch to `feature-1`
4. Create a new branch and switch to it in a single command — call it `feature-2`

![alt text](./images/task2.1.png.png)

5. Try using `git switch` to move between branches — how is it different from `git checkout`?

git switch → branch switching only 
git checkout → branch switching + file restore


6. Make a commit on `feature-1` that does **not** exist on `main`
7. Switch back to `main` — verify that the commit from `feature-1` is not there

![alt text](./images/task2.2.png.png)

8. Delete a branch you no longer need

![alt text](./images/task2.3.png.png)


9. Add all branching commands to your `git-commands.md`

---

### Task 3: Push to GitHub
1. Create a **new repository** on GitHub (do NOT initialize it with a README)
2. Connect your local `devops-git-practice` repo to the GitHub remote
3. Push your `main` branch to GitHub

![alt text](./images/task3.1.png.png)

4. Push `feature-1` branch to GitHub

![alt text](./images/task3.2.png.png)

5. Verify both branches are visible on GitHub

![alt text](./images/task3.3.png.png)

6. Answer in your notes: What is the difference between `origin` and `upstream`?

`origin`: The default name for your own remote repository.It is where you push your work.Created automatically when you clone your repo (your GitHub repo URL).

`upstream`: A second remote usually used when you fork someone else’s repository.
It refers to the original project you forked from.
You do not push to upstream (usually).
Instead, you pull updates from it to keep your fork in sync.

---

### Task 4: Pull from GitHub
1. Make a change to a file **directly on GitHub** (use the GitHub editor)
2. Pull that change to your local repo

![alt text](./images/task4.png.png)

3. Answer in your notes: What is the difference between `git fetch` and `git pull`?

`git fetch`: Downloads new commits, branches, tags from the remote
Does NOT merge changes into your local branch
Safe — it only updates your remote‑tracking branches (origin/main)

`git pull`: Does everything git fetch does AND merges the changes into your current branch.


---

### Task 5: Clone vs Fork
1. **Clone** any public repository from GitHub to your local machine
2. **Fork** the same repository on GitHub, then clone your fork
3. Answer in your notes:
   - What is the difference between clone and fork?

    ans: `Fork` :

    Creates a copy of someone else’s repository in your GitHub account.
    Used when you don’t have write access to the original repo.
    Enables you to make changes independently.


    `Clone` :

    Creates a local copy on your machine of a GitHub repo (your own repo or someone else’s).
    You clone either your own repo or a forked repo.



   - When would you clone vs fork?

    ans: `clone when` :

    You want to work on your own repository.
    You have write access.
    You only need a local working copy.

    `fork when` :

    You want to contribute to a repo you don’t own.
    You don’t have write access to the original project.
    You want your own independent copy on GitHub.


   - After forking, how do you keep your fork in sync with the original repo?

    step1: Add the original repo as upstream (git remote add upstream <URL>)

    step2: fetch the lastest changes(git fetch upstream)

    step3: Merge upstream chaneg into your local main ( git checkout main , git merge 
    upstream/main)

    step4: push updtae  code back to fork (git push origin main)


---
## ✅ Task 1 — The Problem

1. What can go wrong when 5 developers manually deploy to production?

- Overwrites & conflicts — one person’s deployment overwrites another’s changes.
- Inconsistent environments — different machines = different dependencies or versions.
- Human errors — missing a file, wrong command, wrong branch, wrong server.
- Outages — downtime caused by deploying untested or incompatible code.
- No audit/history — no clear record of who deployed what and when.


2. What does “it works on my machine” mean & why is it a real problem?

- “It works on my machine” means the code runs on the developer’s computer but fails elsewhere (test, staging, production) due to:
- Different OS, dependencies, configs, environment variables
- Missing packages or different versions
- Differences in runtime (Python/Node/Java versions, etc.)
- It’s a real problem because software should behave the same everywhere, not just on one laptop.

3. How many times a day can a team safely deploy manually?

- Realistically: 0–1 times per day, depending on:
-  Developer availability
- Risk tolerance
- Time required for manual testing & verification
- Manual deployments are slow, risky, and prone to mistakes. Modern teams use automation to deploy multiple times per day safely.


--- 

## ✅ Task 2 — CI vs CD

1. Continuous Integration (CI)

CI automatically builds and tests code every time a developer pushes changes.

It catches bugs early — especially merge conflicts, failing tests, lint issues.

Example:
GitHub Actions runs tests automatically when you push a pull request.

2. Continuous Delivery (CD)

CD means every change that passes CI is packaged and ready for deployment.
A human usually presses the final “Deploy” button.

Goal: The software is always in a deployable state.

Example:
After CI, a Docker image is pushed to a registry, waiting for a manual deploy.

3. Continuous Deployment (CDp)

This is the next step after Delivery: every change that passes CI is deployed automatically to 
production with no human approval.

Used by high-velocity teams with strong test automation.

Example:
A code change passes tests → automatically deployed to production (e.g., Netflix).

----- 


## ✅ Task 3 — Pipeline Anatomy


`Trigger`

Something that starts the pipeline — a Git push, PR, schedule, or manual click.


`Stage`

A group of related jobs (e.g., Build, Test, Deploy).


`Job`

A collection of steps executed on a runner.

Example: "Run unit tests"


`Step`

A single command/action inside a job.

Example: npm install


`Runner`

The machine that executes the pipeline (GitHub-hosted or self-hosted).


`Artifact`

Output from the pipeline — build files, test reports, Docker images, binaries.


----


## ✅ Task 4 — Draw a Pipeline

CI/CD Pipeline for Your Scenario

Here’s a simple ASCII diagram (you may still draw your own by hand):

Developer Pushes Code → GitHub

        ▼
   [Stage 1: Test]
        - Install dependencies
        - Run unit tests

        ▼
 [Stage 2: Build Docker Image]
        - Build image
        - Tag image
        - Push to Docker registry

        ▼
 [Stage 3: Deploy to Staging]
        - Pull image on staging server
        - Restart service


--- 


## ✅ Task 5 — Explore in the Wild
(Example based on the FastAPI repository — easy to understand for beginners)


Notes:


- What triggers it?

push to main branches

pull_request

schedule: (runs daily)



- How many jobs does it have?

Usually 2–3 jobs like:

Lint

Test

Build (optional)



- What does it do?

Installs dependencies

Runs linting (flake8, etc.)

Runs the test suite

Ensures FastAPI is stable across Python versions

Makes sure new contributions don’t break the project
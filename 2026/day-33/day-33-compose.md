## Challenge Tasks

### Task 1: Install & Verify
1. Check if Docker Compose is available on your machine
2. Verify the version
![alt text](./images/task1.png)

---

### Task 2: Your First Compose File
1. Create a folder `compose-basics`
2. Write a `docker-compose.yml` that runs a single **Nginx** container with port mapping
3. Start it with `docker compose up`
![alt text](./images/task2.1.png)

4. Access it in your browser

5. Stop it with `docker compose down`
![alt text](./images/task2.2.png)


---

### Task 3: Two-Container Setup
Write a `docker-compose.yml` that runs:
- A **WordPress** container
- A **MySQL** container

They should:
- Be on the same network (Compose does this automatically)
- MySQL should have a named volume for data persistence
- WordPress should connect to MySQL using the service name
![alt text](./images/task3.1.png)
![alt text](./images/task3.2.png)

Start it, access WordPress in your browser, and set it up.
![alt text](./images/task3.3.png)

**Verify:** Stop and restart with `docker compose down` and `docker compose up` — is your WordPress data still there?

![alt text](./images/task3.png)
---

### Task 4: Compose Commands
Practice and document these:
1. Start services in **detached mode**
![alt text](./images/task4.1.png)

2. View running services
3. View **logs** of all services
![alt text](./images/task4.2.png)

4. View logs of a **specific** service
![alt text](./images/task4.3.png)

5. **Stop** services without removing
![alt text](./images/task4.4.png)

![alt text](./images/task4.5.png)

6. **Remove** everything (containers, networks)
![alt text](./images/task4.6.png)

7. **Rebuild** images if you make a change

---

### Task 5: Environment Variables
1. Add environment variables directly in your `docker-compose.yml`
2. Create a `.env` file and reference variables from it in your compose file
3. Verify the variables are being picked up

![alt text](./images/task5.png)

---
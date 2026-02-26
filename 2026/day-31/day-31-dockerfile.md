## Challenge Tasks

### Task 1: Your First Dockerfile
1. Create a folder called `my-first-image`
2. Inside it, create a `Dockerfile` that:
   - Uses `ubuntu` as the base image
   - Installs `curl`
   - Sets a default command to print `"Hello from my custom image!"`
3. Build the image and tag it `my-ubuntu:v1`
![alt text](./images/task1.1.png)

4. Run a container from your image
![alt text](./images/task1.2.png)

**Verify:** The message prints on `docker run`

---

### Task 2: Dockerfile Instructions
Create a new Dockerfile that uses **all** of these instructions:
- `FROM` — base image
- `RUN` — execute commands during build
- `COPY` — copy files from host to image
- `WORKDIR` — set working directory
- `EXPOSE` — document the port
- `CMD` — default command

![alt text](./images/task2.1.png)

Build and run it. Understand what each line does.

![alt text](./images/task2.2.png)

---

### Task 3: CMD vs ENTRYPOINT
1. Create an image with `CMD ["echo", "hello"]` — run it, then run it with a custom command. What happens?
![alt text](./images/task3.1.png)

2. Create an image with `ENTRYPOINT ["echo"]` — run it, then run it with additional arguments. What happens?

![alt text](./images/task3.2.png)

3. Write in your notes: When would you use CMD vs ENTRYPOINT?

---

### Task 4: Build a Simple Web App Image
1. Create a small static HTML file (`index.html`) with any content
![alt text](./images/task4.1.png)

2. Write a Dockerfile that:
   - Uses `nginx:alpine` as base
   - Copies your `index.html` to the Nginx web directory

![alt text](./images/task4.2.png)

3. Build and tag it `my-website:v1`
![alt text](./images/task4.3.png)

4. Run it with port mapping and access it in your browser
![alt text](./images/task4.4.png)

![alt text](./images/task4.5.png)

---

### Task 5: .dockerignore
1. Create a `.dockerignore` file in one of your project folders
2. Add entries for: `node_modules`, `.git`, `*.md`, `.env`
3. Build the image — verify that ignored files are not included

---

### Task 6: Build Optimization
1. Build an image, then change one line and rebuild — notice how Docker uses **cache**
![alt text](./images/task6.1.png)

2. Reorder your Dockerfile so that frequently changing lines come **last**

![alt text](./images/task6.2.png)

3. Write in your notes: Why does layer order matter for build speed?

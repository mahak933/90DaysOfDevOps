---

## 🌐 About the Page

The included `index.html` file is a minimal styled webpage featuring:

- A header with a welcome message  
- A card section describing the setup  
- A footer  
- Clean UI using simple CSS (no external libraries)

It is meant to show how easily Nginx can serve static content.

---

## 🐳 Docker Setup

### **1. Build the Docker Image**

Run the following command from the project folder:

```bash
docker build -t my-website:v1 .


### **2. Run the Docker Image**

```basg
docker run -d -p 80:80 my-website:v1



from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Docker Flask ✨</title>
        <style>
            body {
                background: linear-gradient(135deg, #4facfe, #00f2fe);
                font-family: 'Arial', sans-serif;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: white;
                text-align: center;
                margin: 0;
            }
            .card {
                background: rgba(255, 255, 255, 0.15);
                padding: 40px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
                animation: fadeIn 1.5s ease-in-out;
            }
            h1 {
                font-size: 48px;
                font-weight: bold;
                margin-bottom: 20px;
                text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
            }
            p {
                font-size: 22px;
            }
            .btn {
                margin-top: 20px;
                padding: 12px 25px;
                font-size: 18px;
                color: white;
                background: #ff7eb3;
                border: none;
                border-radius: 30px;
                cursor: pointer;
                transition: 0.3s;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
            }
            .btn:hover {
                background: #ff65a3;
                transform: scale(1.1);
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>🚀 Hello from Docker + Flask!</h1>
            <p>This page is running inside a Docker container, styled with ❤️ and CSS.</p>
            <button class="btn" onclick="alert('You clicked a Docker button! 🐋')">Click Me</button>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

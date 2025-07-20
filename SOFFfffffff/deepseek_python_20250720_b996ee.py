import os
import sys

def create_frontend():
    # Create frontend directory
    os.makedirs("frontend", exist_ok=True)
    
    # HTML File
    with open("frontend/index.html", "w") as f:
        f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Hello World! 👋</h1>
    <p>This is a basic frontend template</p>
    <button id="clickBtn">Click Me</button>
    <script src="script.js"></script>
</body>
</html>""")
    
    # CSS File
    with open("frontend/style.css", "w") as f:
        f.write("""body {
    font-family: Arial, sans-serif;
    background-color: #f0f8ff;
    text-align: center;
    padding: 50px;
}

h1 {
    color: #2c3e50;
}

button {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #3498db;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}""")
    
    # JavaScript File
    with open("frontend/script.js", "w") as f:
        f.write("""document.getElementById('clickBtn').addEventListener('click', () => {
    alert('Button Clicked!');
    console.log('Event working perfectly!');
});""")
    
    print("✅ Frontend code created in /frontend folder!")

def create_backend():
    # Create backend directory
    os.makedirs("backend", exist_ok=True)
    
    # server.js File
    with open("backend/server.js", "w") as f:
        f.write("""const express = require('express');
const app = express();
const PORT = 3000;

// Basic route
app.get('/', (req, res) => {
    res.send('🚀 Backend Server is Running!');
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});""")
    
    # package.json File
    with open("backend/package.json", "w") as f:
        f.write("""{
    "name": "backend",
    "version": "1.0.0",
    "description": "Basic Node.js Backend",
    "main": "server.js",
    "scripts": {
        "start": "node server.js"
    },
    "dependencies": {
        "express": "^4.18.2"
    }
}""")
    
    print("✅ Backend code created in /backend folder!")
    print("👉 Run 'npm install' in /backend folder to install dependencies")

def main():
    print("""
███████╗██╗   ██╗██████╗  ██████╗ 
██╔════╝██║   ██║██╔══██╗██╔═══██╗
███████╗██║   ██║██████╔╝██║   ██║
╚════██║██║   ██║██╔══██╗██║   ██║
███████║╚██████╔╝██║  ██║╚██████╔╝
╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ 
    """)
    print("Welcome! Auto Website Code Generator")
    
    choice = input("What do you need?\n1. Frontend (HTML/CSS/JS)\n2. Backend (Node.js)\n3. Both\nEnter choice (1/2/3): ")
    
    if choice == "1":
        create_frontend()
    elif choice == "2":
        create_backend()
    elif choice == "3":
        create_frontend()
        create_backend()
        print("\n🎉 Full-stack code generated! Frontend in /frontend, Backend in /backend")
    else:
        print("Invalid choice! Exiting...")
        sys.exit()

if __name__ == "__main__":
    main()
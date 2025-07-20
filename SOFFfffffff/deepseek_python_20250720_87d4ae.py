import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import shutil
import webbrowser

class WebsiteGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Website Code Generator")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f2f5")
        
        self.create_widgets()
        self.setup_notebook()
        
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            header_frame, 
            text="Website Code Generator", 
            font=("Segoe UI", 18, "bold"), 
            fg="white", 
            bg="#2c3e50"
        )
        title_label.pack(pady=15)
        
        # Main content frame
        self.main_frame = tk.Frame(self.root, bg="#f0f2f5")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Project details
        project_frame = tk.LabelFrame(
            self.main_frame, 
            text="Project Details", 
            font=("Segoe UI", 10, "bold"),
            bg="#ffffff",
            padx=10,
            pady=10
        )
        project_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            project_frame, 
            text="Project Name:", 
            bg="#ffffff", 
            font=("Segoe UI", 9)
        ).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        self.project_name = tk.Entry(
            project_frame, 
            width=40, 
            font=("Segoe UI", 9),
            highlightthickness=1,
            highlightbackground="#d1d8e0"
        )
        self.project_name.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.project_name.insert(0, "MyWebsite")
        
        tk.Label(
            project_frame, 
            text="Output Directory:", 
            bg="#ffffff", 
            font=("Segoe UI", 9)
        ).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        self.output_dir = tk.Entry(
            project_frame, 
            width=40, 
            font=("Segoe UI", 9),
            highlightthickness=1,
            highlightbackground="#d1d8e0"
        )
        self.output_dir.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.output_dir.insert(0, os.path.join(os.path.expanduser("~"), "Documents"))
        
        browse_btn = ttk.Button(
            project_frame, 
            text="Browse", 
            command=self.browse_directory,
            style="Accent.TButton"
        )
        browse_btn.grid(row=1, column=2, padx=5, pady=5)
        
        # Generate button
        generate_btn = ttk.Button(
            self.main_frame, 
            text="Generate Website Code", 
            command=self.generate_code,
            style="Accent.TButton"
        )
        generate_btn.pack(pady=10)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready to generate website code")
        self.status_bar = tk.Label(
            self.root, 
            textvariable=self.status_var,
            bd=1, 
            relief=tk.SUNKEN, 
            anchor=tk.W,
            bg="#e9ecef",
            font=("Segoe UI", 9)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Style configuration
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), background="#3498db", foreground="white")
        style.map("Accent.TButton", background=[("active", "#2980b9")])
        
    def setup_notebook(self):
        # Notebook for templates and code preview
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
        
        # Template selection tab
        template_frame = ttk.Frame(self.notebook)
        self.notebook.add(template_frame, text="Templates")
        
        tk.Label(
            template_frame, 
            text="Select a Website Template:", 
            font=("Segoe UI", 10, "bold"),
            background="#ffffff"
        ).pack(anchor="w", pady=(10, 5), padx=10)
        
        self.template_var = tk.StringVar(value="business")
        
        templates = [
            ("Business Website", "business"),
            ("E-commerce Store", "ecommerce"),
            ("Portfolio", "portfolio"),
            ("Blog", "blog"),
            ("Landing Page", "landing")
        ]
        
        for text, value in templates:
            rb = ttk.Radiobutton(
                template_frame, 
                text=text, 
                variable=self.template_var, 
                value=value,
                style="TRadiobutton"
            )
            rb.pack(anchor="w", padx=30, pady=2)
        
        # Code preview tab
        preview_frame = ttk.Frame(self.notebook)
        self.notebook.add(preview_frame, text="Code Preview")
        
        # Create a frame for the preview text widgets
        preview_container = tk.Frame(preview_frame, bg="#2d2d2d")
        preview_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs for different file previews
        preview_notebook = ttk.Notebook(preview_container)
        preview_notebook.pack(fill=tk.BOTH, expand=True)
        
        # HTML preview
        html_frame = ttk.Frame(preview_notebook)
        preview_notebook.add(html_frame, text="index.html")
        self.html_preview = tk.Text(
            html_frame, 
            bg="#2d2d2d", 
            fg="#f8f8f2", 
            insertbackground="white",
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.html_preview.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.html_preview.insert(tk.END, self.get_html_template())
        self.html_preview.config(state=tk.DISABLED)
        
        # CSS preview
        css_frame = ttk.Frame(preview_notebook)
        preview_notebook.add(css_frame, text="styles.css")
        self.css_preview = tk.Text(
            css_frame, 
            bg="#2d2d2d", 
            fg="#f8f8f2", 
            insertbackground="white",
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.css_preview.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.css_preview.insert(tk.END, self.get_css_template())
        self.css_preview.config(state=tk.DISABLED)
        
        # JavaScript preview
        js_frame = ttk.Frame(preview_notebook)
        preview_notebook.add(js_frame, text="script.js")
        self.js_preview = tk.Text(
            js_frame, 
            bg="#2d2d2d", 
            fg="#f8f8f2", 
            insertbackground="white",
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.js_preview.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.js_preview.insert(tk.END, self.get_js_template())
        self.js_preview.config(state=tk.DISABLED)
        
        # Server preview
        server_frame = ttk.Frame(preview_notebook)
        preview_notebook.add(server_frame, text="server.js")
        self.server_preview = tk.Text(
            server_frame, 
            bg="#2d2d2d", 
            fg="#f8f8f2", 
            insertbackground="white",
            font=("Consolas", 10),
            wrap=tk.WORD
        )
        self.server_preview.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.server_preview.insert(tk.END, self.get_server_template())
        self.server_preview.config(state=tk.DISABLED)
        
    def browse_directory(self):
        directory = filedialog.askdirectory(
            initialdir=self.output_dir.get(),
            title="Select Output Directory"
        )
        if directory:
            self.output_dir.delete(0, tk.END)
            self.output_dir.insert(0, directory)
    
    def generate_code(self):
        project_name = self.project_name.get().strip()
        output_dir = self.output_dir.get().strip()
        template = self.template_var.get()
        
        if not project_name:
            messagebox.showerror("Error", "Please enter a project name")
            return
            
        if not output_dir:
            messagebox.showerror("Error", "Please select an output directory")
            return
            
        if not os.path.exists(output_dir):
            try:
                os.makedirs(output_dir)
            except Exception as e:
                messagebox.showerror("Error", f"Could not create directory: {str(e)}")
                return
                
        project_path = os.path.join(output_dir, project_name)
        
        if os.path.exists(project_path):
            if not messagebox.askyesno("Confirm", f"Directory '{project_name}' already exists. Overwrite?"):
                return
            try:
                shutil.rmtree(project_path)
            except Exception as e:
                messagebox.showerror("Error", f"Could not remove existing directory: {str(e)}")
                return
                
        try:
            # Create project structure
            os.makedirs(project_path)
            os.makedirs(os.path.join(project_path, "public"))
            os.makedirs(os.path.join(project_path, "public", "css"))
            os.makedirs(os.path.join(project_path, "public", "js"))
            os.makedirs(os.path.join(project_path, "public", "images"))
            os.makedirs(os.path.join(project_path, "backend"))
            
            # Write files
            with open(os.path.join(project_path, "public", "index.html"), "w") as f:
                f.write(self.get_html_template(template))
                
            with open(os.path.join(project_path, "public", "css", "styles.css"), "w") as f:
                f.write(self.get_css_template(template))
                
            with open(os.path.join(project_path, "public", "js", "script.js"), "w") as f:
                f.write(self.get_js_template(template))
                
            with open(os.path.join(project_path, "backend", "server.js"), "w") as f:
                f.write(self.get_server_template())
                
            # Create a simple README
            with open(os.path.join(project_path, "README.md"), "w") as f:
                f.write(f"# {project_name}\n\nWebsite project generated with Website Code Generator\n")
                
            self.status_var.set(f"Project created successfully at: {project_path}")
            messagebox.showinfo("Success", f"Website project created successfully!\n\nLocation: {project_path}")
            
            # Open the project folder
            if messagebox.askyesno("Open Folder", "Would you like to open the project folder?"):
                if os.name == 'nt':
                    os.startfile(project_path)
                elif os.name == 'posix':
                    os.system(f'open "{project_path}"' if sys.platform == 'darwin' else f'xdg-open "{project_path}"')
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create project: {str(e)}")
            self.status_var.set("Error creating project")
    
    def get_html_template(self, template="business"):
        templates = {
            "business": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Business Website</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Business Solutions</h1>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section id="hero">
        <div class="container">
            <h2>Professional Business Solutions</h2>
            <p>We help businesses grow and succeed in the digital age</p>
            <a href="#contact" class="btn">Get Started</a>
        </div>
    </section>

    <section id="services" class="section">
        <div class="container">
            <h2>Our Services</h2>
            <div class="services-grid">
                <div class="service">
                    <h3>Web Development</h3>
                    <p>Custom websites and web applications built to your specifications.</p>
                </div>
                <div class="service">
                    <h3>Digital Marketing</h3>
                    <p>Reach your target audience with our strategic marketing campaigns.</p>
                </div>
                <div class="service">
                    <h3>Consulting</h3>
                    <p>Expert advice to help your business navigate the digital landscape.</p>
                </div>
            </div>
        </div>
    </section>

    <section id="about" class="section">
        <div class="container">
            <h2>About Us</h2>
            <p>We are a team of experienced professionals dedicated to helping businesses succeed. With over 10 years of industry experience, we've helped hundreds of clients achieve their goals.</p>
            <p>Our approach combines technical expertise with business acumen to deliver solutions that drive real results.</p>
        </div>
    </section>

    <section id="contact" class="section">
        <div class="container">
            <h2>Contact Us</h2>
            <form id="contact-form">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" required>
                </div>
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" rows="5" required></textarea>
                </div>
                <button type="submit" class="btn">Send Message</button>
            </form>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 Business Solutions. All rights reserved.</p>
        </div>
    </footer>

    <script src="js/script.js"></script>
</body>
</html>""",
            "ecommerce": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Store</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>ShopSmart</h1>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#products">Products</a></li>
                    <li><a href="#deals">Deals</a></li>
                    <li><a href="#cart">Cart</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section id="hero">
        <div class="container">
            <h2>Summer Sale - Up to 50% Off!</h2>
            <p>Limited time offer on our best-selling products</p>
            <a href="#products" class="btn">Shop Now</a>
        </div>
    </section>

    <section id="featured-products" class="section">
        <div class="container">
            <h2>Featured Products</h2>
            <div class="products-grid">
                <!-- Products will be loaded via JavaScript -->
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 ShopSmart. All rights reserved.</p>
        </div>
    </footer>

    <script src="js/script.js"></script>
</body>
</html>"""
        }
        return templates.get(template, templates["business"])
    
    def get_css_template(self, template="business"):
        return """/* Global Styles */
:root {
    --primary: #3498db;
    --secondary: #2c3e50;
    --accent: #e74c3c;
    --light: #ecf0f1;
    --dark: #34495e;
    --success: #2ecc71;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
}

.btn {
    display: inline-block;
    padding: 10px 20px;
    background-color: var(--primary);
    color: white;
    text-decoration: none;
    border-radius: 4px;
    font-weight: 600;
    transition: background-color 0.3s;
}

.btn:hover {
    background-color: #2980b9;
}

.section {
    padding: 60px 0;
}

/* Header */
header {
    background-color: var(--secondary);
    color: white;
    padding: 15px 0;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

header .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header h1 {
    font-size: 24px;
}

nav ul {
    display: flex;
    list-style: none;
}

nav ul li {
    margin-left: 20px;
}

nav ul li a {
    color: white;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s;
}

nav ul li a:hover {
    color: var(--primary);
}

/* Hero Section */
#hero {
    background: linear-gradient(rgba(0, 0, 0, 0.7), url('https://via.placeholder.com/1920x600') no-repeat center center/cover;
    color: white;
    text-align: center;
    padding: 100px 0;
}

#hero h2 {
    font-size: 2.5rem;
    margin-bottom: 20px;
}

#hero p {
    font-size: 1.2rem;
    margin-bottom: 30px;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

/* Services Section */
#services h2 {
    text-align: center;
    margin-bottom: 40px;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
}

.service {
    background: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    text-align: center;
    transition: transform 0.3s;
}

.service:hover {
    transform: translateY(-10px);
}

.service h3 {
    margin-bottom: 15px;
    color: var(--secondary);
}

/* Contact Section */
#contact {
    background-color: var(--light);
}

#contact h2 {
    text-align: center;
    margin-bottom: 40px;
}

#contact-form {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 5px;
    font-weight: 500;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-family: inherit;
    font-size: 16px;
}

.form-group textarea {
    min-height: 150px;
}

/* Footer */
footer {
    background-color: var(--secondary);
    color: white;
    text-align: center;
    padding: 20px 0;
}

/* Responsive Design */
@media (max-width: 768px) {
    header .container {
        flex-direction: column;
        text-align: center;
    }
    
    nav ul {
        margin-top: 15px;
    }
    
    nav ul li {
        margin: 0 10px;
    }
    
    .services-grid {
        grid-template-columns: 1fr;
    }
    
    #hero {
        padding: 60px 0;
    }
    
    #hero h2 {
        font-size: 2rem;
    }
}"""
    
    def get_js_template(self, template="business"):
        return """// DOM Content Loaded
document.addEventListener('DOMContentLoaded', function() {
    // Form submission handling
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
            
            // Basic validation
            if (!name || !email || !message) {
                alert('Please fill in all fields');
                return;
            }
            
            // In a real app, you would send this to a server
            console.log('Form submitted:', { name, email, message });
            alert('Thank you for your message! We will get back to you soon.');
            
            // Reset form
            contactForm.reset();
        });
    }
    
    // For e-commerce template
    if (document.querySelector('.products-grid')) {
        loadProducts();
    }
});

// Sample product loading function for e-commerce template
function loadProducts() {
    const products = [
        { id: 1, name: "Wireless Headphones", price: 99.99, image: "https://via.placeholder.com/300" },
        { id: 2, name: "Smart Watch", price: 199.99, image: "https://via.placeholder.com/300" },
        { id: 3, name: "Bluetooth Speaker", price: 79.99, image: "https://via.placeholder.com/300" },
        { id: 4, name: "Phone Charger", price: 29.99, image: "https://via.placeholder.com/300" }
    ];
    
    const productsGrid = document.querySelector('.products-grid');
    
    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.className = 'product';
        productElement.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>$${product.price.toFixed(2)}</p>
            <button class="btn add-to-cart" data-id="${product.id}">Add to Cart</button>
        `;
        productsGrid.appendChild(productElement);
    });
    
    // Add event listeners to cart buttons
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-id');
            addToCart(productId);
        });
    });
}

function addToCart(productId) {
    // In a real app, you would update the cart state
    console.log(`Product ${productId} added to cart`);
    alert('Item added to cart!');
}"""
    
    def get_server_template(self):
        return """const express = require('express');
const path = require('path');
const app = express();
const port = process.env.PORT || 3000;

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, '../public')));

// API routes would go here
app.get('/api/data', (req, res) => {
    res.json({ message: 'Hello from the server!' });
});

// All other routes go to the frontend
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../public', 'index.html'));
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});"""

if __name__ == "__main__":
    root = tk.Tk()
    app = WebsiteGenerator(root)
    root.mainloop()
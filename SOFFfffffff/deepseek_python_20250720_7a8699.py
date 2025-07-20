import pyttsx3
import speech_recognition as sr

def generate_website():
    return """<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            margin: 0;
            padding: 0;
            background-color: #f0f8ff;
        }
        header {
            background: #4CAF50;
            color: white;
            padding: 20px;
            text-align: center;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
    </header>
    <div class="container">
        <p>This is a sample website created through voice commands</p>
    </div>
    <script>
        console.log("Website loaded successfully!");
    </script>
</body>
</html>"""

def generate_login_page():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login-container {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            width: 300px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 3px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: none;
            width: 100%;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form>
            <input type="text" placeholder="Username" required>
            <input type="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    </div>
    <script>
        document.querySelector('form').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Login attempted!');
        });
    </script>
</body>
</html>"""

def generate_payment_page():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Payment Gateway</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .payment-container {
            background: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            width: 350px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background: #4CAF50;
            color: white;
            padding: 12px;
            border: none;
            width: 100%;
            cursor: pointer;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="payment-container">
        <h2>Make Payment</h2>
        <form>
            <div class="form-group">
                <label>Card Number</label>
                <input type="text" placeholder="1234 5678 9012 3456" required>
            </div>
            <div class="form-group">
                <label>Expiry Date</label>
                <input type="text" placeholder="MM/YY" required>
            </div>
            <div class="form-group">
                <label>CVV</label>
                <input type="text" placeholder="123" required>
            </div>
            <div class="form-group">
                <label>Amount (₹)</label>
                <input type="number" placeholder="1000" required>
            </div>
            <button type="submit">Pay Now</button>
        </form>
    </div>
    <script>
        document.querySelector('form').addEventListener('submit', function(e) {
            e.preventDefault();
            window.location.href = 'payment-success.html';
        });
    </script>
</body>
</html>"""

def generate_success_page():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Payment Successful</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0fff0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }
        .success-container {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        .checkmark {
            color: #4CAF50;
            font-size: 60px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="success-container">
        <div class="checkmark">✓</div>
        <h2>Payment Successful!</h2>
        <p>Your transaction was completed successfully.</p>
        <p>Thank you for your payment!</p>
    </div>
</body>
</html>"""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)
        
    try:
        command = r.recognize_google(audio, language='hi-IN')
        print(f"You said: {command}")
        return command.lower()
    except:
        return ""

def main():
    speak("Voice Website Builder started. Give commands in Hindi")
    
    while True:
        command = listen_command()
        
        if "वेबसाइट बनाकर दो" in command:
            with open("website.html", "w") as f:
                f.write(generate_website())
            speak("Website created successfully. File saved as website.html")
            
        elif "लॉगिन पेज बनाकर दो" in command:
            with open("login.html", "w") as f:
                f.write(generate_login_page())
            speak("Login page created successfully. File saved as login.html")
            
        elif "पेमेंट भेज बनाकर दो" in command:
            with open("payment.html", "w") as f:
                f.write(generate_payment_page())
            speak("Payment page created successfully. File saved as payment.html")
            
        elif "सक्सेसफुल पेमेंट का पेज बनाकर दो" in command:
            with open("payment-success.html", "w") as f:
                f.write(generate_success_page())
            speak("Payment success page created. File saved as payment-success.html")
            
        elif "बंद करो" in command:
            speak("Closing the program")
            break
            
        else:
            speak("Please give a valid command")

if __name__ == "__main__":
    main()
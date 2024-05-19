from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_client():
    # Get the CLIENT environment variable
    client_name = os.getenv('CLIENT', 'World')  # Default to 'World' if CLIENT is not set
    
    # Define the message
    message = f"Hello, {client_name}!"
    
    # Define an HTML template with inline CSS for styling
    html_template = f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Greeting</title>
        <style>
          body {{
            display: flex;
            justify-content: center;
            align-items: flex-start;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            padding-top: 50px;
          }}
          .container {{
            text-align: center;
          }}
          .message {{
            font-size: 2em;
            color: #343a40;
          }}
          .image {{
            margin-top: 20px;
          }}
        </style>
      </head>
      <body>
        <div class="container">
          <div class="message">{message}</div>
          <div class="image">
            <img src="https://via.placeholder.com/150" alt="Placeholder Image">
          </div>
        </div>
      </body>
    </html>
    """
    
    return html_template

if __name__ == '__main__':
    app.run(debug=True)

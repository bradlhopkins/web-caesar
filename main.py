from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <!-- create your form here -->
           
            <form action="/" method="post">
                <label>
                    Rotate by:
                    <input type="text" value="0" name="rot"/>
                </label>
                <br>
                <label>
                    <textarea name="text"/>{0}</textarea>
                    <input type="submit" value="Submit Query"
                </label>
            </form>     
        </body>
    </html>
    """    

@app.route("/")

def index():
    return form.format("")

@app.route("/", methods=['POST'])

def encrypt():
    message = request.form['text']
    rotate = request.form['rot']

    new_message = rotate_string(message, rotate)

    
    return form.format(new_message)
    

app.run()
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
        <form method='POST'>
        <label for"rotate_id">
        <b>Rotate by: </b>
        </label>
        <input id="rotate_id" type="text" name="rot" value='0' />
        <br>
        <textarea name="text">{0}</textarea> 
        <br>
        <input type ="submit" value="Submit Query" />
    </body>
</html>
""" 

@app.route("/")
def index():
   return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    encripted=""
    rot_local_variable = int(request.form['rot'])
    text_local_variable = request.form['text']
    encripted= rotate_string(text_local_variable, rot_local_variable)
    return form.format(encripted)


app.run()



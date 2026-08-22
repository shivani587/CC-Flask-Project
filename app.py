from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return """
    <html>
    <head>web-application</head>
      <body>
      <h1>HELLO RGUKT</h1>
      </body>
    </html>"""
    return "flask running Successfully"
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)

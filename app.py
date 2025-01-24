from flask import Flask ,render_template

app = Flask(__name__,template_folder="template",static_folder="static")


@app.route("/")
def myindex():
    return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=3000)
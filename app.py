
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate_cgpa():
    if request.method == "POST":
        sem1 = float(request.form["sem1"])
        sem2 = float(request.form["sem2"])
        sem3 = float(request.form["sem3"])
        sem4 = float(request.form["sem4"])
        sem5 = float(request.form["sem5"])
        sem6 = float(request.form["sem6"])
        
        cgpa = (20 * (sem1 + sem2) + 26 * (sem3 + sem4) + 24 * (sem5 + sem6)) / 140
        cgpa=round(cgpa,3)
        return render_template("index.html", cgpa=cgpa)
    
    return render_template("index.html", cgpa=None)

if __name__ == "__main__":
    app.run(debug=False)
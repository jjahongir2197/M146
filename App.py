from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/currency", methods=["GET", "POST"])
def currency():
    if request.method == "POST":
        som = int(request.form["som"])

        dollar_rate = 12500

        usd = som / dollar_rate

        return render_template("result25.html", usd=usd)

    return render_template("index25.html")

if __name__ == "__main__":
    app.run(debug=True)

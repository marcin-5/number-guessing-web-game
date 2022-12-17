from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/game3", methods=["GET", "POST"])
def game3():
    if request.method == "POST":
        min_number = int(request.form["rmin"])
        max_number = int(request.form["rmax"])
        result = request.form["res"]
        guess = int(request.form["guess"])
        if result == "too small":
            min_number = guess
        elif result == "too big":
            max_number = guess
        guess = int((max_number - min_number) / 2) + min_number
        return render_template("game3.html",
                               rmin=min_number, rmax=max_number,
                               guess=guess, res=result)
    else:
        return render_template("game3init.html",
                               rmin=0, rmax=1000,
                               guess=500)


if __name__ == "__main__":
    app.run(debug=True)

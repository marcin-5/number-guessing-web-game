from flask import Flask, render_template, request

app = Flask(__name__)
MIN_NUMBER = 0
MAX_NUMBER = 1000


def calculate_guess_num(rmin, rmax, answer=""):
    def guess(rmin, rmax):
        return int((rmax - rmin) / 2) + rmin
    if answer == "too small":
        rmin = guess(rmin, rmax)            # rmin = previous guess
    elif answer == "too big":
        rmax = guess(rmin, rmax)            # rmax = previous guess
    elif answer == "you won":
        return (guess(rmin, rmax), ) * 3    # rmin = rmax = previous guess
    return rmin, rmax, guess(rmin, rmax)


@app.route("/game3", methods=["GET", "POST"])
def game3():
    if request.method == "POST":
        min_number, max_number, guess = calculate_guess_num(int(request.form["rmin"]),
                                                            int(request.form["rmax"]),
                                                            request.form["res"])
        return render_template("game3.html",
                               rmin=min_number, rmax=max_number,
                               guess=guess)
    else:
        return render_template("game3init.html",
                               rmin=MIN_NUMBER, rmax=MAX_NUMBER,
                               guess=calculate_guess_num(MIN_NUMBER, MAX_NUMBER))


if __name__ == "__main__":
    app.run(debug=True)

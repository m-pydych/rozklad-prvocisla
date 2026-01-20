from flask import Flask, request, render_template

app = Flask(__name__)

def rozklad(n):
    faktory = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            faktory.append(d)
            n //= d
        d += 1
    if n > 1:
        faktory.append(n)
    return faktory

@app.route("/", methods=["GET", "POST"])
def index():
    vysledek = None
    if request.method == "POST":
        n = int(request.form["number"])
        vysledek = rozklad(n)
    return render_template("index.html", vysledek=vysledek)

if __name__ == "__main__":
    app.run()
from flask import Flask, render_template, request, redirect
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # ⬅️ aktifkan monitoring

tasks = []

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect("/")
    return render_template("add_task.html")

if __name__ == "__main__":
    app.run(debug=True)

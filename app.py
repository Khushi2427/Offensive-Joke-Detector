from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get form responses
        responses = request.form.getlist("joke_features")
        count = len(responses)

        # Determine joke safety level
        if count == 0:
            message = "✅ Your joke seems safe!"
            level = "safe"
        elif count == 1 or count == 2:
            message = "⚠️ Your joke **might be offensive!** Be careful."
            level = "slightly-offensive"
        elif count == 3:
            message = "❗ Your joke is **offensive!** Consider modifying it."
            level = "offensive"
        elif 4 <= count <= 5:
            message = "🚨 **Your joke is VERY dangerous!** This might cause serious issues."
            level = "very-dangerous"
        else:
            message = "🔥 **Your joke is EXTREMELY OFFENSIVE!** Get underground! 🏃💨"
            level = "extremely-offensive"

        return render_template("index.html", message=message, level=level, responses=responses)

    return render_template("index.html", message=None)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, send_from_directory, url_for

app = Flask(__name__, static_folder="static", template_folder="templates")


# ------------------ HOME PAGE ------------------ #
@app.route("/")
def home():
    return render_template("index.html")


# ------------------ INVITE LINK ROUTE ------------------ #
@app.route("/invite")
def invite():
    # Replace this with your actual Discord bot invite link
    return "https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=8"


# ------------------ STATIC FILES ------------------ #
# If needed explicitly, Flask serves from /static by default
@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)


# ------------------ RUN APP ------------------ #
if __name__ == "__main__":
    # Use 0.0.0.0 for Vercel or container deployments
    app.run(host="0.0.0.0", port=5000, debug=True)

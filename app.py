from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route("/")
def home():
    bot_stats = {
        "guilds": 123,
        "status": "online"
    }
    return render_template("index.html", bot_stats=bot_stats)

@app.route("/invite")
def invite():
    return redirect(
        "https://discord.com/oauth2/authorize"
        "?client_id=YOUR_BOT_ID"
        "&permissions=8"
        "&scope=bot%20applications.commands"
    )

# Required for Vercel
def handler(request):
    return app(request.environ, start_response=lambda *args: None)
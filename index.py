from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)  

bot = ChatBot("MyBot")
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.persian")  

@app.route("/")
def home():
    return render_template("index.html")  

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    bot_response = bot.get_response(user_input)
    return jsonify({"response": str(bot_response)})

if __name__ == "__main__":
    app.run(debug=True)

from flask.app import Flask
from flask.templating import render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
socketio = SocketIO(app)

messages = [] #substitudo do banco de dados.

@app.route("/")
def home():
    return render_template("chat.html")


#Função que recebe a mensagem enviada pelo usuario.
@socketio.on('sendMessage')
def send_message_handler(msg):
    messages.append(msg) #adiciona a mensagem ao banco de dados (um array).
    emit('getMessage', msg, broadcast=True) #emite para o Frontend(usuario) através do evento getMessage, eviando como argumento a mensagem em formato broadcast(para todos);


#Função que envia o array messages para o front através do evento message.
@socketio.on('message')
def handle_message(msg):
    send(messages)

if __name__ == "__main__":
    socketio.run(app, debug=True)
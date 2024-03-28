from flask import Flask , render_template
app = Flask(__name__)
@app.route("/")
def homepage():
    return render_template("homepage2.html")
@app.route("/contats")
def contats():
 return render_template("contats.html")
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
  return render_template("usuarios.html",nome_usuario=nome_usuario)
if __name__ == "__main__": 
 app.run(debug=True)
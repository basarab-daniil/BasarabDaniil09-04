from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

#inizializza l'app Flask
app = Flask(__name__)
df=pd.read_csv("profilo.csv")
dizionario=df.to_dict()

#rotta principale
@app.route('/')
def home():
    titolo_index="Profilo di "
    df=pd.read_csv("profilo.csv")
    dizionario=df.to_dict()
    nome = dizionario.get('Nome', {}).get(0)
    cognome = dizionario.get('Cognome', {}).get(0)
    scuola = dizionario.get('Scuola', {}).get(0)
    hobby = dizionario.get('Hobby', {}).get(0)
    return render_template('index.html', titolo_index=titolo_index, nome=nome, cognome=cognome, scuola=scuola, hobby=hobby)

@app.route('/modifica')
def modifica():
    titolo_modifica="Modifica il tuo profilo"
    nome = dizionario.get('Nome', {}).get(0)
    cognome = dizionario.get('Cognome', {}).get(0)
    scuola = dizionario.get('Scuola', {}).get(0)
    hobby = dizionario.get('Hobby', {}).get(0)
    return render_template('modifica.html', titolo_modifica=titolo_modifica, nome=nome, cognome=cognome, scuola=scuola, hobby=hobby)

@app.route('/change', methods=['POST'])
def change():
    nome_new = request.form['input_nome']
    cognome_new = request.form['input_cognome']
    scuola_new = request.form['input_scuola']
    hobby_new = request.form['input_hobby']
    dizionario['Nome']=nome_new
    dizionario['Cognome']=cognome_new
    dizionario['Scuola']=scuola_new
    dizionario['Hobby']=hobby_new
    df.clear()
    df.from_dict(dizionario)
    df.to_csv("profilo.csv", index=False)

    
#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)
    
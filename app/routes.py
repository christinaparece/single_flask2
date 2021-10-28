from flask import Flask, render_template, request
import requests
from app import app
from .forms import PokeForm


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/poke', methods=['GET', 'POST'])
def poke():
    form= PokeForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = request.form.get('name')
        url = f'https://pokeapi.co/api/v2/pokemon/{name}'
        print(url)
        response = requests.get(url)
        if response.ok:
            if not response.json():
                error_string="ERROR loading"
                return render_template('poke.html.j2' , error = error_string, form=form) 
            data = response.json()
            new_data=[]
            pokemon_name = data['name']
            pokemon_dict={}
            pokemon_dict= {
                'name': data['name'],
                'ability_name': data['ability_name'],
                'base experience': data['base experience'],
                'sprite front shiny': data['sprite front shiny']
                }
            new_data.append(pokemon_dict)
            return render_template('poke.html.j2', names=new_data)     
        else:
            error_string="ERROR loading"
            return render_template('poke.html.j2' , error = error_string)


    return render_template('poke.html.j2')


    
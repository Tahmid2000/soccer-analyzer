from flask import Flask, render_template, url_for, request, flash, redirect
from forms import SearchPlayerForm, SearchTeamForm
from playerName import getPlayers
from secrets import *

application = Flask(__name__)
application.config['SECRET_KEY'] = SECRET_KEY


@application.route("/")
def index():
    return render_template('index.html')


@application.route("/teams", methods=['GET', 'POST'])
def teams():
    form = SearchTeamForm()
    if form.validate_on_submit():
        request.form['name']
        return redirect(url_for('index'))
    return render_template('teams.html', title='SearchTeam', form=form)


@application.route("/players", methods=['GET', 'POST'])
def players():
    form = SearchPlayerForm()
    if form.validate_on_submit():
        """ players = [{'player_id': 186320, 'player_name': 'Neymar', 'image_path': 'https://cdn.sportmonks.com/images/soccer/players/16/186320.png', 'nationality': 'Brazil'}, {'player_id': 465793, 'player_name': 'Junior Neymar', 'image_path': 'https://cdn.sportmonks.com/images/soccer/placeholder.png', 'nationality': 'Brazil'},
                   {'player_id': 7692466, 'player_name': 'Jayson Neymar', 'image_path': 'https://cdn.sportmonks.com/images/soccer/placeholder.png', 'nationality': 'Brazil'}, {'player_id': 512563, 'player_name': 'Martin Jimenez Bedoya', 'image_path': 'https://cdn.sportmonks.com/images/soccer/placeholder.png', 'nationality': 'Panama'}] """
        players = getPlayers(request.form['name'])
        return render_template('players.html', players=players, title='SearchPlayer', form=form)
    return render_template('players.html', title='SearchPlayer', form=form)


@application.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    application.debug = True
    application.run()

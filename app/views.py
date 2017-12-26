from flask import render_template
from app import app
from .requests import get_pitches

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    all_pitches = get_pitches()  
    title = 'Home - Welcome to The best Pitching Website Online'
    return render_template('index.html', title = title , all_pitches= all_pitches)

@app.route('/pitch/<int:pitch_id>')
def movie(pitch_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    title = pitch_id
    return render_template('pitch.html',title= title)
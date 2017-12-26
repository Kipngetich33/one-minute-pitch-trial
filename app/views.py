from flask import render_template
from app import app
from .requests import get_pitches,get_pitch,search_pitch

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
    found_pitch= get_pitch(pitch_id)
    title = pitch_id
    return render_template('pitch.html',title= title ,found_pitch= found_pitch)

@app.route('/search/<pitch_name>')
def search(pitch_name):
    '''
    View function to display the search results
    '''
    searched_pitches = search_pitch(pitch_name)
    title = f'search results for {pitch_name}'
    return render_template('search.html',pitches = searched_pitches)

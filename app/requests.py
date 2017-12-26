from app import app
from .models import pitch 

# Getting api key
secret_key = app.config['SECRET_KEY']

Pitch = pitch.Pitch


def get_pitches():
    '''
    Function that will get list of pitches from the database
    '''
    requested_pitches = process_pitches(pitch.list_of_pitches)
    return requested_pitches

def process_pitches(list_of_pitches_objects):
    '''
    Function that will define the results retrived from the database
    '''
    processed_pitches =[]
    for obj in list_of_pitches_objects:
        id= obj[0]
        pitch= obj[1]

        pitch_object = Pitch(id,pitch)
        processed_pitches.append(pitch_object)

    return processed_pitches






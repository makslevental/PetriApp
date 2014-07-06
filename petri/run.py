__author__ = 'max'



import sys
sys.path.insert(0,'~/apps/PetriApp/petri')
from app import app
application = app

if __name__ == '__main__':
    app.run(debug=True)


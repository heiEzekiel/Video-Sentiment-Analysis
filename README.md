# MLA-project

## How to run the project
1. Create your python virtual environment - (Optional)
2.  Run Command `` pip install -r requirements.txt `` (Do note that it might take awhile as there are alot of depedencies)
3. go into the directory ``ezekiel/Facial Emotions with Flask app/``
4. Run Command ``python app.py``
5. Open your browser and go to http://localhost:5000/

## Important to note 
Some External modules/api require API token to access their services, they may have expired. List of modules that require API token are as follows:
- https://docs.audd.io/#api-methods - get music attributes (title & artist, etc)

- require env file to use spotipy API
CLIENT_ID=""
CLIENT_SECRET="""

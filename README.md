# Minimal_DnD_character_server
The goal of this project is to create a dnd server one can run locally or deploy to a server like fly.io.  It should run out of the box with authentication and character sheets. Users should be able to have multiple characters that are saved to a database, and sheets should have fields that auto-update when other values are introduced and save explicitly or periodically. It will eventually have a dice roller component along with saving rolls and a graphics for results over time.

Todo:
    - set up models (User, character, dice-data)
        - character models todo
            - figure out spell list
            - figure out how to translate between json and attack options
            - set up how armor items will modify ac
    - set up dice app
    - figure out how to have attributes in elements modify attributes in other elements
    - save to json feature / print to pdf feature
    - implement race maker


    - instructions for setup locally and deploy
        - local: create .env file, then execute this command and save the output `python -c "import secrets; print(secrets.token_urlsafe())"`
        - in the .env file, which will be referenced by our `settings.py`, add the lines `SECRET_KEY=saved_output_of_previous_python_command` and DEBUG=True
        - also in the .env file add whatever the link to your database file is, like the postgres link if where you're deploying it to has one, but you will change this based if you'll deploy it
        - edit `DATABASES` in `settings.py` to `{"default": env.dj_db_url("DATABASE_URL", default="sqlite:///db.sqlite3"),}`
    - web setup for character sheet
        - https://github.com/lckynmbrsvn/DnD-5e-Character-Sheet use
            - https://lckynmbrsvn.github.io/DnD-5e-Character-Sheet/ example

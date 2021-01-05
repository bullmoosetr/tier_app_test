import os

from flask import Flask, request, jsonify, flash, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=False):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
    
    if test_config is False:
        app.config.from_object("config.Config")
    else:
        app.config.from_object("config.ConfigTesting")


    db.init_app(app)

    with app.app_context():
        db.create_all()

        @app.route('/shorten_url', methods=['POST'])
        def shorten_url():
            payload = request.form.to_dict()
            print(payload)
            from tier_app.shorten_url import get_or_create_shortened_url
            response = get_or_create_shortened_url(payload['long_url'])
            message = f"Your new shorter Url tier.app/{response.new_url}  "
            return message

        @app.route('/tier.app/<shortened_url>')
        def tier_app(shortened_url):
            from tier_app.shorten_url import get_original_url
            # Lookup long url for redirection
            url = get_original_url(shortened_url)
            if url:
                flash("Succes!")
                return redirect(url)
            else:
                flash("An Error Occured", category='error')
                return 'Either No Url was found with that code  or The Url Code is too short or wrong so take another look :('
    
        return app
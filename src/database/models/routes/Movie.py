from flask import Blueprint

main=Blueprint('movie_blueprint,_name_')

@main.rout('/')
def get_movies():
    return jsonify('message':MiguelGilF)

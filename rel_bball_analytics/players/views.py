import pandas as pd
from flask import Blueprint, render_template, request

players_bp = Blueprint("players", __name__, url_prefix="/players")


@players_bp.route("", methods=["GET", "POST"])
def search():
    from .search import get_search_result
    from .styles import format_search_result, format_season

    if request.method == "POST":
        name = request.form["name"]
        season = int(request.form["season"])

        search_result = get_search_result(name=name, season=season)

        if search_result is None:
            search_result = (
                '<p class="message">Sorry, no data available for this search!</p>'
            )
        else:
            search_result = format_search_result(search_result=search_result)

        return render_template(
            "players/search_result.html",
            search_result=search_result,
            season=format_season(season),
        )

    return render_template("players/search.html")


@players_bp.route("/<id>_<season>", methods=["GET"])
def details(id, season):
    from rel_bball_analytics.games.game_log import get_game_log

    from .search import get_player_details
    from .styles import format_player_details

    player_data = get_player_details(id=id, season=season)
    game_log = get_game_log(player_id=id, season=season)

    if game_log is None:
        game_log = (
            '<p class="message">Sorry, no game data available for this season!</p>'
        )

    return render_template(
        "players/details.html",
        player_data=format_player_details(player_data=player_data),
        game_log=game_log,
    )

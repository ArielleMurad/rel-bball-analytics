from flask import Blueprint, render_template, request

players_bp = Blueprint("players", __name__, url_prefix="/players")


@players_bp.route("", methods=("GET", "POST"))
def search():
    from .player_search import format_search_result, player_search

    if request.method == "POST":
        name = request.form["name"]
        season = request.form["season"]

        search_result = player_search(name=name, season=season)

        if search_result is None:
            message = '<p class="message">Sorry, no data available for this search!</p>'
            return render_template("players/search_result.html", search_result=message)

        return render_template(
            "players/search_result.html",
            search_result=format_search_result(search_result=search_result),
        )

    return render_template("players/search.html")

from flask import Blueprint, flash, redirect, render_template, request, url_for

players_bp = Blueprint("players", __name__, url_prefix="/players")


@players_bp.route("", methods=("GET", "POST"))
def search():
    from .player_search import player_search

    if request.method == "POST":
        name = request.form["name"]
        season = request.form["season"]

        search_result = player_search(name=name, season=season)

        if search_result is None:
            message = "<p>Sorry, no data available for this search!</p>"
            return render_template("players/search_result.html", search_result=message)
        else:
            return render_template(
                "players/search_result.html", search_result=search_result.to_html()
            )

    return render_template("players/search.html")

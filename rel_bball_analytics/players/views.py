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
            message = '<p class="message">Sorry, no data available for this search!</p>'
            return render_template(
                "players/search_result.html",
                search_result=message,
                season=format_season(season),
            )

        return render_template(
            "players/search_result.html",
            search_result=format_search_result(search_result=search_result),
            season=format_season(season),
        )

    return render_template("players/search.html")


@players_bp.route("/<id>", methods=["GET"])
def details(id):
    from .models import fetch_player_records
    from .styles import format_player_details

    player_data = fetch_player_records(id=id)[0]
    player_data = format_player_details(player_data=player_data)

    return render_template("players/details.html", player_data=player_data)

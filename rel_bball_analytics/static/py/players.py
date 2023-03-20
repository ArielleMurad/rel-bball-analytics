TEXT_PRIMARY = "black"
TEXT_SECONDARY = "#dc6300"

BG_PRIMARY = "#ff943d"
BG_LIGHT = "hsl(30deg 100% 62% / 44%)"

BORDER_PRIMARY = "2px solid #ff943d"

PADDING = "12px"

FONT_FAMILY = "Helvetica, sans-serif"


def players_table():
    return [
        {
            "selector": "",
            "props": [
                ("border-collapse", "collapse"),
                ("font-family", FONT_FAMILY),
            ],
        },
        {
            "selector": "td",
            "props": [
                ("padding", PADDING),
                ("text-align", "center"),
                ("border-top", BORDER_PRIMARY),
            ],
        },
        {
            "selector": "thead th",
            "props": [
                ("background-color", BG_PRIMARY),
                ("color", "#ffffff"),
                ("font-weight", "bold"),
                ("padding", PADDING),
                ("text-align", "center"),
            ],
        },
        {
            "selector": "tbody tr:hover",
            "props": [
                ("background-color", BG_LIGHT),
            ],
        },
        {
            "selector": "a",
            "props": [
                ("color", TEXT_PRIMARY),
                ("font-style", "italic"),
            ],
        },
        {
            "selector": "a:hover",
            "props": [
                ("color", TEXT_SECONDARY),
                ("text-decoration", "none"),
            ],
        },
    ]

TEXT_PRIMARY = "black"
TEXT_SECONDARY = "#dc6300"

BG_LIGHT = "hsl(30deg 100% 62% / 44%)"

BORDER_PRIMARY = "2px solid black"

PADDING = "12px"

FONT_FAMILY = "Helvetica, sans-serif"
FONT_SIZE = "14px"


def game_log_table():
    return [
        {
            "selector": "",
            "props": [
                ("border-collapse", "collapse"),
                ("font-family", FONT_FAMILY),
                ("font-size", FONT_SIZE),
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
    ]

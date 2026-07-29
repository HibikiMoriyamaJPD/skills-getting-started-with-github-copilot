from pathlib import Path


def test_activity_card_markup_includes_participants_section():
    app_js = Path("src/static/app.js").read_text(encoding="utf-8")

    assert "Participants" in app_js
    assert "participants-list" in app_js

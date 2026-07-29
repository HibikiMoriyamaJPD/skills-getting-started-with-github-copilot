from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_remove_participant_from_activity():
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    remove_response = client.delete(f"/activities/{activity_name}/participants?email={email}")
    assert remove_response.status_code == 200

    data = remove_response.json()
    assert "Removed" in data["message"]

    activities = client.get("/activities").json()
    assert email not in activities[activity_name]["participants"]

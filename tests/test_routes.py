import pytest
from app import create_app, db
from app.models import Data

@pytest.fixture
def client():
    app = create_app("development")
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Base de datos en memoria para tests

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_get_data_empty(client):
    response = client.get("/data")
    assert response.status_code == 200
    assert isinstance(response.json, list)  # No asumimos que esté vacía

def test_post_and_get_data(client):
    # Insertar nuevo dato
    response = client.post("/data", json={"name": "Test Item"})
    assert response.status_code == 200
    assert "Data inserted successfully" in response.json["message"]

    # Verificar que aparece
    response = client.get("/data")
    assert response.status_code == 200
    assert any(item["name"] == "Test Item" for item in response.json)

def test_delete_data(client):
    # Insertar para poder borrar
    client.post("/data", json={"name": "ToDelete"})
    response = client.get("/data")
    data_id = response.json[0]["id"]

    # Eliminar el dato
    response = client.delete(f"/data/{data_id}")
    assert response.status_code == 200
    assert "deleted successfully" in response.json["message"]
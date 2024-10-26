from app import hello_world

async def test_hello_world():
    response = await hello_world()
    assert response.response == "Hello world!"

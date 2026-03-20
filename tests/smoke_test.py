from skinmate import create_app

app = create_app()

with app.test_client() as client:
    for path in ['/', '/introduction', '/analysis', '/login', '/healthz']:
        resp = client.get(path)
        print(path, resp.status_code)

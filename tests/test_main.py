import logging
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_index() -> None:
    response = client.get('/api')
    try: 
        assert response.status_code == 200
    except:
        logging.warning(f"""
        status code: {response.status_code}
        header: {response.headers}
        body: {response.json()}
        """)


def test_company_id() -> None:
    company_id: str = '47602c23-a1a2-4f40-9405-88e033d5cf24'
    response = client.get(f'/api/piodash-colors/{company_id}')
    
    assert response.status_code == 200
    assert response.json() == [
        "0e988b",
        "78c5be",
        "fdfefe"
    ]


def test_fake_company_id() -> None:
    fake_company_ids: list = ['45', '37-4383-48', '9', '0', '1', '2', '2333333',
                         '34789', '4444444444444444444444444444444', '64752856354723464']
    for id in fake_company_ids:
        response = client.get(f'/api/piodash-colors/{id}')
        try:
            assert response.status_code == 404
        except:
            logging.warning(f"""
            A status code other than 404 has been returned.
            Status code: {response.status_code}
            Passing company_id: {id}""")


if __name__ == '__main__':
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARNING)

    test_index()
    test_company_id()
    test_fake_company_id()

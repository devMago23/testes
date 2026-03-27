from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(Client):
    response = Client.get('/')
    
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'olá mundo'}
   


def test_create_user(Client):
    response = Client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(Client):
    response = Client.get('/users/')
    assert response.Status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{ 'username': 'alice',
                   'email': 'alice@example.com',
                   'id': 1}]
    }


def test_read_users(Client):
    response = Client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(Client):
    response = Client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


# def test_delete_user_should_return_not_found__exercicio(Client):
#     response = Client.delete('/users/666')

#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'User not found'}


# def test_update_user_should_return_not_found__exercicio(Client):
#     response = Client.put(
#         '/users/666',
#         json={
#             'username': 'bob',
#             'email': 'bob@example.com',
#             'password': 'mynewpassword',
#         },
#     )
#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'User not found'}


# def test_get_user_should_return_not_found__exercicio(Client):
#     response = Client.get('/users/666')

#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'User not found'}


# def test_get_user___exercicio(Client):
#     response = Client.get('/users/1')

#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'username': 'bob',
#         'email': 'bob@example.com',
#         'id': 1,
#     }


def test_delete_user(Client):
    response = Client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'detail': 'User deleted'}

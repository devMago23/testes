from sqlalchemy import select
from fast_zero.models import UserModel


def test_create_user(session):
    new_user = UserModel(username='test', email='test@test', password='secret')

    session.add(new_user)
    session.commit()
    new_user=session.scalar(
        select(new_user).where(new_user.username=='test')
    )
    assert new_user.username == 'test'

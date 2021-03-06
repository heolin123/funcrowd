import datetime

import pytest

from users.models import ActivationToken


@pytest.mark.django_db
def test_multiple_tokens(user1):
    # test expiration
    token = user1.create_activation_token()
    assert token.is_expired is False

    token.created = token.created - datetime.timedelta(hours=30)
    assert token.is_expired is True

    # test multiple
    old_token_id = token.id
    token = user1.create_activation_token()

    old_token = ActivationToken.objects.get(id=old_token_id)

    assert token.token_used is False
    assert old_token.token_used is True

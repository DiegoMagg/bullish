from decimal import Decimal

import pytest
from model_bakery import baker


@pytest.fixture
def share():
    '''Real data obtained in 26/09/23 3:06PM'''
    return baker.make(
        'Share',
        ticker='VGHF11',
        name='VALORA HEDGE FUND',
        heritage=Decimal(881632478),
        market_value=Decimal(906087511),
        reservation=Decimal(112404848),
        shareholders_amount=291930,
        quota_amount=94187891,
    )


@pytest.fixture
def share_price(share):
    return baker.make('SharePrice', share=share, price=Decimal(9.63))


@pytest.fixture
def dividend(share):
    return baker.make('Dividend', share=share, amount=Decimal(0.12), paid=True)

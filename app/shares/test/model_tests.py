from decimal import Decimal

import pytest

pytestmark = pytest.mark.django_db


def test_share_instance_str_method_should_return_share_ticker(share):
    assert share.__str__() == share.ticker


def test_share_instance_should_calculate_expected_p_over_vp(share):
    expected_output = Decimal('1.027738353123601691996650786')
    assert share.p_over_vp == expected_output


def test_share_instance_should_return_the_reservation_percentage(share):
    expected_output = Decimal('12.74962649459018681931996611')
    assert share.reservation_percentage == expected_output


def test_share_instance_should_return_zeroed_magic_number_if_no_share_price(share, dividend):
    expected_output = 0
    assert share.magic_number == expected_output


def test_share_instance_should_return_zeroed_magic_number_if_no_dividend(share, share_price):
    expected_output = 0
    assert share.magic_number == expected_output


def test_share_instance_should_return_expected_magic_number(share, share_price, dividend):
    expected_output = 81
    assert share.magic_number == expected_output

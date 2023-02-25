import pytest

from beaker import Application
from calculator import Calculator
from calculator import demo as calc_demo
from counter import CounterApp
from counter import demo as count_demo
from hello import HelloBeaker
from hello import demo as hello_demo
from decorators import ExternalExample
from tests.conftest import check_application_artifacts_output_stability


def test_calc():
    calc_demo()


def test_count():
    count_demo()


def test_hello():
    hello_demo()


@pytest.mark.parametrize(
    "app_class", [Calculator, CounterApp, HelloBeaker, ExternalExample]
)
def test_output_stability(app_class: type[Application]):
    app = app_class()
    check_application_artifacts_output_stability(app)

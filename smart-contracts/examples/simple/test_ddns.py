import pytest

from beaker import Application
from examples.simple.calculator import Calculator
from examples.simple.calculator import demo as calc_demo
from examples.simple.counter import CounterApp
from examples.simple.counter import demo as count_demo
from examples.simple.ddns import DDNS
from examples.simple.ddns import main as ddns_main
from examples.simple.decorators import ExternalExample
from tests.conftest import check_application_artifacts_output_stability


def test_calc():
    calc_demo()


def test_count():
    count_demo()


def test_main():
    ddns_main()


@pytest.mark.parametrize(
    "app_class", [Calculator, CounterApp, DDNS, ExternalExample]
)
def test_output_stability(app_class: type[Application]):
    app = app_class()
    check_application_artifacts_output_stability(app)

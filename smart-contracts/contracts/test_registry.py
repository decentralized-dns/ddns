import pytest
from beaker import Application
from contracts.registry import Registry
from contracts.registry import demo as registry_demo
from tests.conftest import check_application_artifacts_output_stability


def test_registry():
    registry_demo()


@pytest.mark.parametrize("app_class", [Registry])
def test_output_stability(app_class: type[Application]):
    app = app_class()
    check_application_artifacts_output_stability(app)

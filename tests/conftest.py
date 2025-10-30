from typing import Type
from unittest.mock import Mock

import pytest

from interfaces import IMovingObj, IRotatingObj, IFuelObj
from dto import Velocity, Fuel, Point, Consumption


@pytest.fixture
def mock_moving__fuel_obj():
    class Ship(IMovingObj, IFuelObj):

        def __init__(self, location: Point, velocity: Velocity, fuel: Fuel, consumption: Consumption) -> None:
            self.__location = location
            self.__velocity = velocity
            self.__fuel = fuel
            self.__consumption = consumption

        @property
        def location(self) -> Point:
            return self.__location

        @location.setter
        def location(self, new_value: Point) -> None:
            self.__location = new_value

        @property
        def velocity(self) -> Velocity:
            return self.__velocity

        @property
        def fuel(self) -> float:
            return self.__fuel

        @fuel.setter
        def fuel(self, new_value: float) -> None:
            self.__fuel = new_value

        @property
        def consumption(self) -> float:
            return self.__consumption

    return Ship(Point(0, 0), Velocity(2, 3), 27, 13)


@pytest.fixture
def moving_mock_obj_without_location() -> Type[IMovingObj]:
    class MockMovingObj(IMovingObj):  # noqa
        @property
        def velocity(self) -> Mock:
            return Mock()

    return MockMovingObj


@pytest.fixture
def moving_mock_obj_without_velocity() -> Type[IMovingObj]:
    class MockMovingObj(IMovingObj):  # noqa
        @property
        def location(self) -> Mock:
            return Mock()

        @location.setter
        def location(self, new_value: Velocity) -> None:
            self.location = new_value

    return MockMovingObj


@pytest.fixture
def moving_mock_obj_without_ability_set_location() -> Type[IMovingObj]:
    class MockMovingObj(IMovingObj):  # noqa
        @property
        def location(self) -> Mock:
            return Mock()

        @property
        def velocity(self) -> Mock:
            return Mock()

    return MockMovingObj


@pytest.fixture
def rotating_mock_obj_without_angle() -> Type[IRotatingObj]:
    class MockRotatingObj(IRotatingObj):  # noqa
        @property
        def angular_velocity(self) -> Mock:
            return Mock()

    return MockRotatingObj


@pytest.fixture
def rotating_mock_obj_without_angular_velocity() -> Type[IRotatingObj]:
    class MockRotatingObj(IRotatingObj):  # noqa
        @property
        def angle(self) -> Mock:
            return Mock()

        @angle.setter
        def angle(self, new_value: IRotatingObj) -> None:
            self.angle = new_value

    return MockRotatingObj


@pytest.fixture
def rotating_mock_obj_without_ability_set_angle() -> Type[IRotatingObj]:
    class MockRotatingObj(IRotatingObj):  # noqa
        @property
        def angle(self) -> Mock:
            return Mock()

        @property
        def angle_velocity(self) -> Mock:
            return Mock()

    return MockRotatingObj


@pytest.fixture
def fuel_mock_obj_without_fuel() -> Type[IFuelObj]:
    class MockFuelObj(IFuelObj):  # noqa
        @property
        def consumption(self) -> Mock:
            return Mock()

    return MockFuelObj


@pytest.fixture
def fuel_mock_obj_without_consumption() -> Type[IFuelObj]:
    class MockFuelObj(IFuelObj):  # noqa
        @property
        def fuel(self) -> Mock:
            return Mock()

        @fuel.setter
        def fuel(self, new_value: Fuel) -> None:
            self.fuel = new_value

    return MockFuelObj


@pytest.fixture
def fuel_mock_obj_without_ability_set_fuel() -> Type[IFuelObj]:
    class MockFuelObj(IFuelObj):  # noqa
        @property
        def fuel(self) -> Mock:
            return Mock()

        @property
        def consumption(self) -> Mock:
            return Mock()

    return MockFuelObj

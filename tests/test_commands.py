from typing import Type
from unittest.mock import Mock

import pytest

from interfaces import IMovingObj, IRotatingObj, IFuelObj
from dto import Point, Velocity
from macro_commands import MacroCommand
from commands import MoveCommand, RotateCommand, CheckFuelCommand, BurnFuelCommand
from exceptions import CommandException


class TestMoveCommand:

    def test_move_from_12_5__with_velocity_minus_7_3(self) -> None:
        """Движение объекта с точки 12,5 и скорость -7,3 в точку 5,8."""

        movable_mock_obj = Mock(location=Point(12, 5), velocity=Velocity(-7, 3))

        result_before_move = movable_mock_obj.location
        MoveCommand(movable_mock_obj).execute()
        result_after_move = movable_mock_obj.location

        expected_result_before_move = Point(12, 5)
        expected_result_after_move = Point(5, 8)

        assert result_before_move == expected_result_before_move, f'Ожидаемый результат: {expected_result_before_move}, полученный результат: {result_before_move}'
        assert result_after_move == expected_result_after_move, f'Ожидаемый результат: {expected_result_after_move}, полученный результат: {result_after_move}'

    def test_move_obj_without_location(self, moving_mock_obj_without_location: Type[IMovingObj]) -> None:
        """Попытка выполнить движение без возможности получения положения в пространстве."""

        with pytest.raises(TypeError):
            moving_mock_obj = moving_mock_obj_without_location()
            MoveCommand(moving_mock_obj).execute()

    def test_move_obj_without_velocity(self, moving_mock_obj_without_velocity: Type[IMovingObj]) -> None:
        """Попытка выполнить движение без возможности получения мгновенной скорости."""

        with pytest.raises(TypeError):
            moving_mock_obj = moving_mock_obj_without_velocity()
            MoveCommand(moving_mock_obj).execute()

    def test_move_obj_without_set_velocity(
            self, moving_mock_obj_without_ability_set_location: Type[IMovingObj]
    ) -> None:
        """Попытка выполнить движение без возможности изменения положения в пространстве."""

        with pytest.raises(AttributeError):
            moving_mock_obj = moving_mock_obj_without_ability_set_location()
            MoveCommand(moving_mock_obj).execute()


class TestRotateCommand:

    def test_rotate_from_23_degree__to_34_point_5_degree(self) -> None:
        """Поворот объекта с 23 градусов на 34.5 градуса."""

        rotating_mock_obj = Mock(angle=23, angular_velocity=11.5)

        result_before_rotate = rotating_mock_obj.angle
        RotateCommand(rotating_mock_obj).execute()
        result_after_rotate = rotating_mock_obj.angle

        expected_result_before_rotate = 23
        expected_result_after_rotate = 34.5

        assert result_before_rotate == expected_result_before_rotate, f'Ожидаемый результат: {expected_result_before_rotate}, полученный результат: {result_before_rotate}'
        assert result_after_rotate == expected_result_after_rotate, f'Ожидаемый результат: {expected_result_after_rotate}, полученный результат: {result_after_rotate}'

    def test_rotate_obj_without_location(self, rotating_mock_obj_without_angle: Type[IRotatingObj]) -> None:
        """Попытка выполнить поворот без возможности получения угла."""

        with pytest.raises(TypeError):
            rotate_mock_obj = rotating_mock_obj_without_angle()
            RotateCommand(rotate_mock_obj).execute()

    def test_rotate_obj_without_velocity(self, rotating_mock_obj_without_angular_velocity: Type[IRotatingObj]) -> None:
        """Попытка выполнить поворот без возможности получения угловой скорости."""

        with pytest.raises(TypeError):
            rotate_mock_obj = rotating_mock_obj_without_angular_velocity()
            RotateCommand(rotate_mock_obj).execute()

    def test_rotate_obj_without_set_velocity(
            self, rotating_mock_obj_without_ability_set_angle: Type[IRotatingObj]
    ) -> None:
        """Попытка выполнить поворот без возможности изменения угла."""

        with pytest.raises(TypeError):
            rotate_mock_obj = rotating_mock_obj_without_ability_set_angle()
            RotateCommand(rotate_mock_obj).execute()


class TestCheckFuelCommand:

    def test_fuel_value_not_changed(self) -> None:
        """Проверка того, что уровень топлива не поменяется при выполнении проверки."""

        check_fuel_mock_obj = Mock(fuel=14.3, consumption=6.5)

        result_before_rotate = check_fuel_mock_obj.fuel
        CheckFuelCommand(check_fuel_mock_obj).execute()
        result_after_rotate = check_fuel_mock_obj.fuel

        expected_result_before_rotate = 14.3
        expected_result_after_rotate = 14.3

        assert result_before_rotate == expected_result_before_rotate, f'Ожидаемый результат: {expected_result_before_rotate}, полученный результат: {result_before_rotate}'
        assert result_after_rotate == expected_result_after_rotate, f'Ожидаемый результат: {expected_result_after_rotate}, полученный результат: {result_after_rotate}'

    def test_fuel_raise_exc_if_fuel_not_enough(self) -> None:
        """Проверка того, что выбросится исключение, если уровень топлива ниже, чем необходимо."""

        check_fuel_mock_obj = Mock(fuel=3, consumption=4)

        with pytest.raises(CommandException):
            CheckFuelCommand(check_fuel_mock_obj).execute(), 'Должно выброситься исключение CommandException'

    def test_fuel_not_raise_exc_if_fuel_equal_0(self) -> None:
        """Проверка того, что не выбросится исключение, если уровень топлива равен 0."""

        check_fuel_mock_obj = Mock(fuel=3, consumption=3)

        CheckFuelCommand(check_fuel_mock_obj).execute(), 'Ошибка не должна выбрасываться, если уровень топлива 0'

    def test_fuel_obj_without_fuel(self, fuel_mock_obj_without_fuel: Type[IFuelObj]) -> None:
        """Попытка проверить топливо без возможности получения топлива."""

        with pytest.raises(TypeError):
            mock_fuel_obj = fuel_mock_obj_without_fuel()
            CheckFuelCommand(mock_fuel_obj).execute()

    def test_rotate_obj_without_velocity(self, fuel_mock_obj_without_consumption: Type[IFuelObj]) -> None:
        """Попытка проверить топливо без возможности получения скорости расхода топлива."""

        with pytest.raises(TypeError):
            mock_fuel_obj = fuel_mock_obj_without_consumption()
            CheckFuelCommand(mock_fuel_obj).execute()

    def test_rotate_obj_without_set_fuel(self, rotating_mock_obj_without_ability_set_angle: Type[IFuelObj]) -> None:
        """Попытка проверить топливо без возможности изменения значения топлива."""

        with pytest.raises(TypeError):
            mock_fuel_obj = rotating_mock_obj_without_ability_set_angle()
            CheckFuelCommand(mock_fuel_obj).execute()


class TestBurnFuelCommand:

    @pytest.mark.parametrize('fuel, consumption, expected_result', [
        (14, 6, 8), (3, 5, -2), (0, 0, 0)
    ])
    def test_reduce_fuel(self, fuel: int, consumption: int, expected_result: int) -> None:
        """Проверка того, что уровень топлива уменьшится."""

        burn_fuel_mock_obj = Mock(fuel=fuel, consumption=consumption)

        BurnFuelCommand(burn_fuel_mock_obj).execute()
        result = burn_fuel_mock_obj.fuel

        assert result == expected_result, f'Ожидаемый результат: {expected_result}, полученный результат: {result}'

    def test_fuel_obj_without_fuel(self, fuel_mock_obj_without_fuel: Type[IFuelObj]) -> None:
        """Попытка выполнить поворот без возможности получения угла."""

        with pytest.raises(TypeError):
            mock_fuel_obj = fuel_mock_obj_without_fuel()
            CheckFuelCommand(mock_fuel_obj).execute()

    def test_rotate_obj_without_velocity(self, fuel_mock_obj_without_consumption: Type[IFuelObj]) -> None:
        """Попытка выполнить поворот без возможности получения угловой скорости."""

        with pytest.raises(TypeError):
            mock_fuel_obj = fuel_mock_obj_without_consumption()
            CheckFuelCommand(mock_fuel_obj).execute()

    def test_rotate_obj_without_set_fuel(self, rotating_mock_obj_without_ability_set_angle: Type[IFuelObj]) -> None:
        """Попытка выполнить поворот без возможности изменения угла."""

        with pytest.raises(TypeError):
            mock_fuel_obj = rotating_mock_obj_without_ability_set_angle()
            CheckFuelCommand(mock_fuel_obj).execute()


class TestMacroCommand:

    def test_without_exc(self, mock_moving__fuel_obj) -> None:
        """Тестирование списка команд."""

        commands = [
            CheckFuelCommand(mock_moving__fuel_obj),
            MoveCommand(mock_moving__fuel_obj),
            BurnFuelCommand(mock_moving__fuel_obj),
            CheckFuelCommand(mock_moving__fuel_obj),
            MoveCommand(mock_moving__fuel_obj),
            BurnFuelCommand(mock_moving__fuel_obj),
        ]

        MacroCommand(commands).execute()

        result = mock_moving__fuel_obj.fuel

        expected_result = 1

        assert result == expected_result, f'Ожидаемый результат: {expected_result}, полученный результат: {result}'

    def test_with_exc(self, mock_moving__fuel_obj):
        commands = [
            CheckFuelCommand(mock_moving__fuel_obj),
            MoveCommand(mock_moving__fuel_obj),
            BurnFuelCommand(mock_moving__fuel_obj),
            CheckFuelCommand(mock_moving__fuel_obj),
            MoveCommand(mock_moving__fuel_obj),
            BurnFuelCommand(mock_moving__fuel_obj),
            CheckFuelCommand(mock_moving__fuel_obj),
            MoveCommand(mock_moving__fuel_obj),
            BurnFuelCommand(mock_moving__fuel_obj),
        ]

        with pytest.raises(CommandException):
            MacroCommand(commands).execute()

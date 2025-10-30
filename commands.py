import math

from interfaces import ICommand, IMovingObj, IRotatingObj, IFuelObj
from exceptions import CommandException


class MoveCommand(ICommand):
    """Объект для выполнения движения."""

    def __init__(self, obj: IMovingObj) -> None:
        self.obj = obj

    def execute(self) -> None:
        self.obj.location = self.obj.location.move_to(self.obj.velocity)


class RotateCommand(ICommand):
    """Объект для поворота."""

    def __init__(self, obj: IRotatingObj) -> None:
        self.obj = obj

    def execute(self) -> None:
        self.obj.angle = self.obj.angle + self.obj.angular_velocity


class CheckFuelCommand(ICommand):
    """Объект для проверки топлива."""

    def __init__(self, obj: IFuelObj) -> None:
        self.obj = obj

    def execute(self) -> None:
        if self.obj.fuel - self.obj.consumption < 0:
            raise CommandException('Недостаточно топлива для движения!')


class BurnFuelCommand(ICommand):
    """Объект расхода топлива."""

    def __init__(self, obj: IFuelObj) -> None:
        self.obj = obj

    def execute(self) -> None:
        self.obj.fuel -= self.obj.consumption


class ChangeVelocityCommand(ICommand):
    """Объект изменения вектора мгновенной скорости."""

    def __init__(self, moving_obj: IMovingObj, rotate_obj: IRotatingObj) -> None:
        self.moving_obj = moving_obj
        self.rotate_obj = rotate_obj

    def execute(self) -> None:
        """Изменение вектора мгновенной скорости."""

        v_dx = self.moving_obj.velocity.dx
        v_dy = self.moving_obj.velocity.dy
        angle = self.rotate_obj.angle

        dx = v_dx * math.cos(angle) - v_dy * math.sin(angle)
        dy = v_dx * math.sin(angle) + v_dy * math.cos(angle)

import math

from interfaces import ICommand, IMovingObj, IRotatingObj, IFuelObj, IChangeVelocityObj
from exceptions import CommandException
from dto import Velocity


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

    def __init__(self, obj: IChangeVelocityObj) -> None:
        self.obj = obj

    def execute(self) -> None:
        """Изменение вектора мгновенной скорости."""

        dx = self.obj.velocity.dx
        dy = self.obj.velocity.dy
        angle_radians = math.radians(self.obj.angle)

        new_dx = dx * math.cos(angle_radians) - dy * math.sin(angle_radians)
        new_dy = dx * math.sin(angle_radians) + dy * math.cos(angle_radians)

        self.obj.velocity = Velocity(round(new_dx, 10), round(new_dy, 10))

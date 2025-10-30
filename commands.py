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


class MacroCommand:
    def __init__(self, commands: list[ICommand]) -> None:
        self.commands = commands

    def execute(self) -> None:
        for command in self.commands:
            command.execute()

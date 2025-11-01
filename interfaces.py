import abc

from dto import Point, Velocity, Degree, Radian, Fuel, Consumption


class ICommand(abc.ABC):
    """Интерфейс команд."""

    @abc.abstractmethod
    def execute(self) -> None:
        """Метод для взаимодействия с командой."""


class IMovingObj(abc.ABC):
    """Интерфейс для движущихся объектов."""

    @property
    @abc.abstractmethod
    def location(self) -> Point:
        """Возвращает местоположение объекта."""

    @location.setter
    @abc.abstractmethod
    def location(self, new_location: Point) -> None:
        """Изменяет местоположение объекта."""

    @property
    @abc.abstractmethod
    def velocity(self) -> Velocity:
        """Возвращает скорость объекта."""


class IRotatingObj(abc.ABC):
    """Интерфейс для поворачивающихся объектов."""

    @property
    @abc.abstractmethod
    def angle(self) -> Radian:
        """Возвращает угол поворота."""

    @angle.setter
    @abc.abstractmethod
    def angle(self, new_value: Radian) -> None:
        """Переопределяет угол."""

    @property
    @abc.abstractmethod
    def angular_velocity(self) -> Degree:
        """Возвращает угловую скорость."""


class IFuelObj(abc.ABC):

    @property
    @abc.abstractmethod
    def fuel(self) -> Fuel:
        """Возвращает количество топлива."""

    @fuel.setter
    @abc.abstractmethod
    def fuel(self, new_value: Fuel) -> None:
        """Переназначает количество топлива."""

    @property
    @abc.abstractmethod
    def consumption(self) -> Consumption:
        """Скорость расхода топлива."""


class IChangeVelocityObj(abc.ABC):
    """Интерфейс для изменения вектора мгновенной скорости."""

    @property
    @abc.abstractmethod
    def angle(self) -> Radian:
        """Возвращает угол поворота."""

    @property
    @abc.abstractmethod
    def velocity(self) -> Velocity:
        """Возвращает мгновенную скорость объекта."""

    @velocity.setter
    @abc.abstractmethod
    def velocity(self, new_value: Velocity) -> None:
        """Переопределяет вектор мгновенной скорости."""

from datetime import datetime
from models.user import User
from models.resource import Resource


class Reservation:
    def __init__(
        self,
        reservation_id: int,
        user: User,
        resource: Resource,
        start_time: datetime,
        end_time: datetime
    ):
        if start_time >= end_time:
            raise ValueError("Data de inceput trebuie sa fie inainte de data de sfarsit")

        self._reservation_id = reservation_id
        self._user = user
        self._resource = resource
        self._start_time = start_time
        self._end_time = end_time
        self._status = "ACTIVE"

    def get_id(self) -> int:
        return self._reservation_id

    def get_user(self) -> User:
        return self._user

    def get_resource(self) -> Resource:
        return self._resource

    def get_start_time(self) -> datetime:
        return self._start_time

    def get_end_time(self) -> datetime:
        return self._end_time

    def get_status(self) -> str:
        return self._status

    def cancel(self):
        if self._status == "CANCELLED":
            raise Exception("Rezervarea este deja anulata")
        self._status = "CANCELLED"
        self._resource.mark_as_available()

    def __str__(self):
        return (
            f"Reservation(id={self._reservation_id}, "
            f"user={self._user.get_name()}, "
            f"resource={self._resource.get_name()}, "
            f"start={self._start_time}, "
            f"end={self._end_time}, "
            f"status={self._status})"
        )

from datetime import datetime
from models.user import User
from models.resource import Resource
from models.reservation import Reservation
from exceptions.reservation_error import ReservationError


class ReservationService:

    def __init__(self):
        self._reservations = []

    def create_reservation(
        self,
        reservation_id: int,
        user: User,
        resource: Resource,
        start_time: datetime,
        end_time: datetime
    ) -> Reservation:
        if not resource.is_available():
            raise ReservationError("Resursa nu este disponibila")

        for reservation in self._reservations:
            if (
                reservation.get_resource().get_id() == resource.get_id()
                and reservation.get_status() == "ACTIVE"
                and not (
                    end_time <= reservation.get_start_time()
                    or start_time >= reservation.get_end_time()
                )
            ):
                raise Exception("Exista deja o rezervare in acest interval")

        resource.mark_as_reserved()
        reservation = Reservation(
            reservation_id, user, resource, start_time, end_time
        )
        self._reservations.append(reservation)
        return reservation

    def cancel_reservation(self, reservation_id: int):
        for reservation in self._reservations:
            if reservation.get_id() == reservation_id:
                reservation.cancel()
                return
        raise Exception("Rezervare inexistenta")

    def list_active_reservations(self):
        return [
            r for r in self._reservations if r.get_status() == "ACTIVE"
        ]

    def list_all_reservations(self):
        return self._reservations
    

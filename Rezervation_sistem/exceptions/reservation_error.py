class ReservationError(Exception):
    
    def __init__(self, message):
        super().__init__(f"[ReservationError] {message}")

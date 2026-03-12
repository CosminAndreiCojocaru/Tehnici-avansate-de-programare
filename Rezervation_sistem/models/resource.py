class Resource:
    def __init__(self, resource_id: int, name: str, capacity: int):

        if not name:
            raise ValueError("Numele nu poate fi gol")
        self._resource_id = resource_id
        self._name = name
        self._capacity = capacity
        self._is_available = True

    def get_id(self) -> int:
        return self._resource_id

    def get_name(self) -> str:
        return self._name

    def get_capacity(self) -> int:
        return self._capacity

    def is_available(self) -> bool:
        return self._is_available

    def set_name(self, name: str):
        if not name:
            raise ValueError("Numele resursei nu poate fi gol")
        self._name = name

    def set_capacity(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacitatea trebuie să fie > 0")
        self._capacity = capacity

    def mark_as_reserved(self):
        if not self._is_available:
            raise Exception("Resursa este deja rezervata")
        self._is_available = False

    def mark_as_available(self):
        self._is_available = True

    def __str__(self):
        status = "disponibila" if self._is_available else "rezervata"
        return (
            f"Resource(id={self._resource_id}, "
            f"name='{self._name}', "
            f"capacity={self._capacity}, "
            f"status={status})"
        )


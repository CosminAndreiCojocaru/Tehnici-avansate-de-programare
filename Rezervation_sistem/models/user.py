class User:
    def __init__(self, user_id: int, name: str, email: str):
        if not name:
            raise ValueError("Numele nu poate fi gol")
        
        elif not name.isalpha():
            raise ValueError("Numele trebuie sa contina doar litere")
        
        if "@" not in email:
            raise ValueError("Email invalid")
        
        self._user_id = user_id
        self._name = name
        self._email = email

    def get_id(self) -> int:
        return self._user_id

    def get_name(self) -> str:
        return self._name

    def get_email(self) -> str:
        return self._email

    def set_name(self, name: str):
        self._name = name

    def set_email(self, email: str):
        self._email = email

    def __str__(self):
        return f"User(id={self._user_id}, name='{self._name}', email='{self._email}')"

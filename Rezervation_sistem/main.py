from datetime import datetime
from models.user import User
from models.resource import Resource
from models.reservation import Reservation
from services.reservation_service import ReservationService
from exceptions.reservation_error import ReservationError

def read_int(promt):
    value = input(promt)
    if not value.isdigit():
        raise ValueError("Id-ul trebuie sa contina doar cifre")
    return int(value)

def main():
    users = {}
    resources = {}
    reservation_service = ReservationService()

    while True:
        print("\n=== Sistem Rezervari ===")
        print("1. Creeaza utilizator")
        print("2. Creeaza resursa")
        print("3. Creeaza rezervare")
        print("4. Listeaza rezervari active")
        print("5. Anuleaza rezervare")
        print("6. Iesire")
        choice = input("Alege optiunea: ")

        try:
            if choice == "1":
                user_id = read_int("ID user: ")
                if user_id in users:
                    print("User deja exista!")
                    continue
                name = input("Nume: ")
                email = input("Email: ")
                user = User(user_id, name, email)
                users[user_id] = user
                print(f"User creat: {user}")

            elif choice == "2":
                resource_id = read_int("ID resursa: ")
                if resource_id in resources:
                    print("Resursa deja exista!")
                    continue
                name = input("Nume resursa: ")
                capacity = read_int("Capacitate: ")
                if capacity < 1:
                    raise ValueError("Cacitatea treubie sa fie mai mare ca 0")
                resource = Resource(resource_id, name, capacity)
                resources[resource_id] = resource
                print(f"Resursa creata: {resource}")

            elif choice == "3":
                reservation_id = read_int("ID rezervare: ")
                user_id = read_int("ID user: ")
                resource_id = read_int("ID resursa: ")

                if user_id not in users or resource_id not in resources:
                    print("User sau resursa inexistenta!")
                    continue

                start_str = input("Start (YYYY-MM-DD HH:MM): ")
                end_str = input("End (YYYY-MM-DD HH:MM): ")
                start = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
                end = datetime.strptime(end_str, "%Y-%m-%d %H:%M")

                reservation = reservation_service.create_reservation(
                    reservation_id,
                    users[user_id],
                    resources[resource_id],
                    start,
                    end
                )
                print(f"Rezervare creata: {reservation}")

            elif choice == "4":
                active = reservation_service.list_active_reservations()
                if not active:
                    print("Nu exista rezervari active.")
                else:
                    print("\nRezervari active:")
                    for r in active:
                        print(r)

            elif choice == "5":
                reservation_id = int(input("ID rezervare de anulat: "))
                reservation_service.cancel_reservation(reservation_id)
                print(f"Rezervarea {reservation_id} a fost anulata.")

            elif choice == "6":
                print("La revedere!")
                break

            else:
                print("Optiune invalida. Reincearca!")

        except ReservationError as e:
            print(f" Eroare la rezervare: {e}")
        except ValueError as e:
            print(f" Valoare invalida: {e}")
        except Exception as e:
            print(f" Eroare neasteptata: {e}")

main()
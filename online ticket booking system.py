import mysql.connector
from mysql.connector import Error
import hashlib
from datetime import datetime

# Establish connection to MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="Sairam2003!123",  # Replace with your MySQL password
            database="movie_ticket_online"  # Replace with your database name
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None

# Register a new user
def register_user(connection, username, password, role='user'):
    cursor = connection.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    try:
        cursor.execute("INSERT INTO Users (username, password, role) VALUES (%s, %s, %s)", 
                       (username, hashed_password, role))
        connection.commit()
        print("User registered successfully.")
    except Error as e:
        print(f"Error: '{e}'")

# Login a user
def login_user(connection, username, password):
    cursor = connection.cursor()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM Users WHERE username = %s AND password = %s", (username, hashed_password))
    user = cursor.fetchone()
    if user:
        print("Login successful!")
        return user[0], user[3]  # Return user_id and role
    else:
        print("Invalid credentials!")
        return None, None

# Admin adds a movie
def add_movie(connection, title, showtime, price):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Movies (title, showtime, price) VALUES (%s, %s, %s)", 
                   (title, showtime, price))
    connection.commit()
    print("Movie added successfully.")

# View all movies
def view_movies(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Movies")
    movies = cursor.fetchall()
    for movie in movies:
        print(f"Movie ID: {movie[0]}, Title: {movie[1]}, Showtime: {movie[2]}, Price: {movie[3]}")

# View available seats for a movie
def view_available_seats(connection, movie_id):
    cursor = connection.cursor()
    cursor.execute("SELECT seat_id, seat_number FROM Seats WHERE movie_id = %s AND is_booked = 0", (movie_id,))
    available_seats = cursor.fetchall()
    return available_seats

# Book a ticket
def book_ticket(connection, user_id, movie_id, seat_number):
    cursor = connection.cursor()
    cursor.execute("SELECT seat_id FROM Seats WHERE movie_id = %s AND seat_number = %s AND is_booked = 0", 
                   (movie_id, seat_number))
    seat = cursor.fetchone()

    if seat:
        cursor.execute("UPDATE Seats SET is_booked = 1 WHERE seat_id = %s", (seat[0],))
        booking_time = datetime.now()
        cursor.execute("INSERT INTO Bookings (user_id, movie_id, seat_id, booking_time) VALUES (%s, %s, %s, %s)",
                       (user_id, movie_id, seat[0], booking_time))
        connection.commit()
        print("Booking successful!")
    else:
        print("Seat not available!")

# View booking history for a user
def view_booking_history(connection, user_id):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT Movies.title, Seats.seat_number, Bookings.booking_time 
        FROM Bookings
        JOIN Movies ON Bookings.movie_id = Movies.movie_id
        JOIN Seats ON Bookings.seat_id = Seats.seat_id
        WHERE Bookings.user_id = %s
    """, (user_id,))
    bookings = cursor.fetchall()
    for booking in bookings:
        print(f"Movie: {booking[0]}, Seat: {booking[1]}, Time: {booking[2]}")

# View all bookings (Admin function)
def view_all_bookings(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT Users.username, Movies.title, Seats.seat_number, Bookings.booking_time
        FROM Bookings
        JOIN Users ON Bookings.user_id = Users.user_id
        JOIN Movies ON Bookings.movie_id = Movies.movie_id
        JOIN Seats ON Bookings.seat_id = Seats.seat_id
    """)
    bookings = cursor.fetchall()
    for booking in bookings:
        print(f"User: {booking[0]}, Movie: {booking[1]}, Seat: {booking[2]}, Time: {booking[3]}")

# Main logic to interact with the system
def main():
    connection = create_connection()

    if connection is None:
        print("Failed to connect to the database.")
        return

    # Simulate the system flow
    while True:
        print("\nWelcome to the Movie Ticket Booking System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (user/admin): ")
            register_user(connection, username, password, role)

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id, role = login_user(connection, username, password)

            if user_id:
                if role == 'admin':
                    while True:
                        print("\nAdmin Menu")
                        print("1. Add Movie")
                        print("2. View All Bookings")
                        print("3. Logout")
                        admin_choice = input("Choose an option: ")

                        if admin_choice == '1':
                            title = input("Enter movie title: ")
                            showtime = input("Enter showtime (YYYY-MM-DD HH:MM:SS): ")
                            price = float(input("Enter movie price: "))
                            add_movie(connection, title, showtime, price)

                        elif admin_choice == '2':
                            view_all_bookings(connection)

                        elif admin_choice == '3':
                            break

                else:  # Regular user
                    while True:
                        print("\nUser Menu")
                        print("1. View Movies")
                        print("2. Book Ticket")
                        print("3. View Booking History")
                        print("4. Logout")
                        user_choice = input("Choose an option: ")

                        if user_choice == '1':
                            view_movies(connection)

                        elif user_choice == '2':
                            movie_id = int(input("Enter movie ID: "))
                            available_seats = view_available_seats(connection, movie_id)
                            if available_seats:
                                print("Available seats:", [seat[1] for seat in available_seats])
                                seat_number = int(input("Enter seat number to book: "))
                                book_ticket(connection, user_id, movie_id, seat_number)
                            else:
                                print("No available seats for this movie.")

                        elif user_choice == '3':
                            view_booking_history(connection, user_id)

                        elif user_choice == '4':
                            break

        elif choice == '3':
            connection.close()
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

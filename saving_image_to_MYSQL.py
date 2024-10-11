import mysql.connector

def convert_to_binary_data(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binary_data = file.read()
    return binary_data

def insert_image(name, photo):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Sairam2003!123",
            database="saveimage"
        )

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO images (name, data) VALUES (%s,%s)"""

        binary_data = convert_to_binary_data(photo)

        # Convert data into tuple format
        insert_blob_tuple = (name, binary_data)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image inserted successfully as a BLOB into images table")

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insert_image("dogs.jpeg", "Dogs.jpeg")
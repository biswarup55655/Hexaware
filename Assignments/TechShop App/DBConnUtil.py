import mysql.connector


class DBConnUtil:
    @staticmethod
    def get_connection(connection_properties: dict):
        try:
            connection = mysql.connector.connect(
                host=connection_properties['host'],
                port=connection_properties['port'],
                user=connection_properties['user'],
                password=connection_properties['password'],
                database=connection_properties['database']
            )
            return connection
        except mysql.connector.Error as e:
            print(f"Error connecting to database: {e}")

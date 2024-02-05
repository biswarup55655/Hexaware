class DBPropertyUtil:
    @staticmethod
    def get_connection_properties(file_name: str) -> dict:
        connection_properties = {}
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    key, value = line.strip().split('=')
                    connection_properties[key.strip()] = value.strip()
            return connection_properties
        except FileNotFoundError:
            print(f"Error: File {file_name} not found.")
            return {}
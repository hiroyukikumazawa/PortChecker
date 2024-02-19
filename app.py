import socket

def check_port(host, port, timeout=3):
    """
    Attempts to establish a TCP connection to the specified host and port.
    If the connection is successful, the port is considered open.

    :param host: The hostname or IP address to check.
    :param port: The port number to check.
    :param timeout: Connection timeout in seconds.
    :return: True if the port is open, False otherwise.
    """
    try:
        # Create a new socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            # Attempt to connect to the host and port
            s.connect((host, port))
            # Connection was successful, the port is open
            return True
    except socket.error:
        # Connection was unsuccessful, the port is closed or unreachable
        return False

# Example usage
host = '65.109.109.14'  # Replace with the host you want to check
port = 3000  # Replace with the port you want to check

if check_port(host, port):
    print(f"The port {port} on {host} is open.")
else:
    print(f"The port {port} on {host} is closed or unreachable.")

import socket
import sys
import time


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
            start_time = time.time()
            # Attempt to connect to the host and port
            s.connect((host, port))
            end_time = time.time()
            # Connection was successful, the port is open
            return True, (end_time - start_time) * 1000  # time in milliseconds
    except Exception as e:  # noqa
        # Connection was unsuccessful, the port is closed or unreachable
        return False, 0.0


# Example usage
host = "65.109.109.14"  # Replace with the host you want to check
port = 3000  # Replace with the port you want to check
try:
    port = int(sys.argv[1])
except Exception as e:  # noqa
    pass
num_checks = 5  # Number of connection attempts

times = []

for i in range(num_checks):
    is_open, time_taken = check_port(host, port)
    status = "open" if is_open else "closed"
    print(
        f"[INFO] [{time.strftime('%Y-%m-%dT%H:%M:%S')}Z] - MESSAGE: "
        f"Sent Request to {host}:{port} in {time_taken:.2f}ms - The port is {status}"
    )
    if is_open:
        times.append(time_taken)

if times:
    average_time = sum(times) / len(times)
    print(
        f"[SUCCESS] [{time.strftime('%Y-%m-%dT%H:%M:%S')}Z] - MESSAGE: "
        f"Finished testing RPC with average time of {average_time:.2f}ms"
    )
else:
    print("[ERROR] No connection attempts were made.")

# Press enter to return to the main menu...
input("Press enter to return to the main menu...")

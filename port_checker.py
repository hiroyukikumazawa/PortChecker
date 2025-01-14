import socket
import sys
import time

import matplotlib.pyplot as plt


def check_port(host, port, timeout=3):
    """
    Attempts to establish a TCP connection to the specified host and port.
    If the connection is successful, the port is considered open.

    :param host: The hostname or IP address to check.
    :param port: The port number to check.
    :param timeout: Connection timeout in seconds.
    :return: True if the port is open, False otherwise.
    """
    start_time = time.time()
    port_status = None
    try:
        # Create a new socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            # Attempt to connect to the host and port
            s.connect((host, port))
            # Connection was successful, the port is open
            port_status = True
    except Exception as e:  # noqa
        # Connection was unsuccessful, the port is closed or unreachable
        port_status = False
    finally:
        end_time = time.time()
        return port_status, (end_time - start_time) * 1000  # time in milliseconds


# Example usage
host = "rpc.seigma.xyz"  # Replace with the host you want to check
port = 25567  # Replace with the port you want to check
try:
    port = int(sys.argv[1])
except Exception as e:  # noqa
    pass
num_checks = 5  # Number of connection attempts

times = []

for i in range(num_checks):
    is_open, time_taken = check_port(host, port)
    status = "open" if is_open else "closed"
    times.append(time_taken)
    if is_open:
        print(
            f"\x1b[34;1m[INFO] [{time.strftime('%Y-%m-%dT%H:%M:%S')}Z] - MESSAGE: \x1b[0m"
            f"Sent Request to {host}:{port} in {time_taken:.2f}ms - The port is {status}"
        )
    else:
        print(
            f"\x1b[33;1m[WARNING] [{time.strftime('%Y-%m-%dT%H:%M:%S')}Z] - MESSAGE: \x1b[0m"
            f"Sent Request to {host}:{port} in {time_taken:.2f}ms - The port is {status}"
        )

# Graph the ping times
plt.figure(figsize=(10, 6))
plt.plot(times, marker="o", linestyle="-", color="b")
plt.title(f"Ping times to {host}:{port}")
plt.xlabel("Attempt")
plt.ylabel("Time (ms)")
plt.grid(True)
plt.xticks(range(num_checks), [f"Attempt {i+1}" for i in range(num_checks)])
plt.show()

if times:
    average_time = sum(times) / len(times)
    print(
        f"\x1b[32;1m[SUCCESS] [{time.strftime('%Y-%m-%dT%H:%M:%S')}Z] - MESSAGE: \x1b[0m"
        f"Finished testing RPC with average time of {average_time:.2f}ms"
    )
else:
    print(
        f"\x1b[31;1m[ERROR] [{time.strftime('%Y-%m-%dT%H:%M:%S')}Z] - MESSAGE: \x1b[0m"
        "No connection attempts were made."
    )

# Press enter to return to the main menu...
input("Press enter to return to the main menu...")

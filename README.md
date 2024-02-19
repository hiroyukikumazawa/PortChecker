# Port Checker

A Python script to check the status of a port by attempting to establish a TCP connection.

## Description

This script utilizes Python's `socket` module to attempt to establish a TCP connection to a specified host and port. If the connection is successful, the port is considered open; otherwise, it's considered closed or unreachable.

## Usage

### Prerequisites

- Python 3.x

### Installation

No installation is required. Simply download or clone the script to your local machine.

### Usage Example

```bash
python port_checker.py [port]
```

Replace `[port]` with the port number you want to check. If no port number is provided, the script will default to the port specified in the script.

### Options

- `host`: The hostname or IP address to check.
- `port`: The port number to check.
- `timeout`: Connection timeout in seconds (default is 3 seconds).

## Example

```python
python port_checker.py 26657
```

This command will check if port 26657 on the host `eu-rpc.seigma.xyz` is open or closed.

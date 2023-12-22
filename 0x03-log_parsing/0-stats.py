#!/usr/bin/env python3
import sys
import signal

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def process_line(line):
    try:
        parts = line.split()
        ip, date, method, path, protocol, status_code, file_size = (
            parts[0], parts[3][1:], parts[5][1:], parts[6], parts[7], int(parts[8]), int(parts[9])
        )

        if method == "GET" and path == "/projects/260" and protocol == "HTTP/1.1":
            update_stats(status_code, file_size)
            return True

    except (IndexError, ValueError):
        pass

    return False

def update_stats(status_code, file_size):
    global total_size
    total_size += file_size

    if status_code in status_codes:
        status_codes[status_code] += 1
    else:
        status_codes[status_code] = 1

def main():
    global total_size, status_codes
    total_size = 0
    status_codes = {}

    line_count = 0

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            line = line.strip()
            if process_line(line):
                line_count += 1

            if line_count == 10:
                print_stats()
                line_count = 0

    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)

if __name__ == "__main__":
    main()

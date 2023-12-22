#!/usr/bin/python3
"""
log parsing
"""

import sys
import re

HTTP_STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]
LOG_PATTERN = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)'
)


def output(log: dict) -> None:
    """
    Helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


def parse_line(line: str, log: dict) -> None:
    """
    Parse a log line and update the log dictionary
    """
    match = LOG_PATTERN.fullmatch(line)
    if match:
        code = match.group(1)
        file_size = int(match.group(2))

        # File size
        log["file_size"] += file_size

        # Status code
        if code.isdecimal() and int(code) in HTTP_STATUS_CODES:
            log["code_frequency"][code] += 1


if __name__ == "__main__":
    line_count = 0
    log = {"file_size": 0, "code_frequency": {str(code): 0 for code in HTTP_STATUS_CODES}}

    try:
        for line in sys.stdin:
            line = line.strip()
            parse_line(line, log)
            line_count += 1

            if line_count % 10 == 0:
                output(log)
    finally:
        output(log)

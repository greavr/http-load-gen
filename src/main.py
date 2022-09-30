import threading
import time
import sys
import os
import requests

target_url = os.getenv('TARGET_URL')
average_rps = int(os.environ.get('AVERAGE_RPS', 10))
max_rps = int(os.environ.get('MAX_RPS', 100))
cycle_duration = int(os.environ.get('DURATION', 60))
loop_count = int(os.environ.get('LOOPS', 0))

# Function to make request
def make_request(request_id):
    """ Make Request """
    x = requests.get(url = target_url, verify=False)
    print(f"{request_id}: {x.status_code}")

if __name__ == "__main__":
    """ Main Entry Point"""

    if not target_url:
        # Validate required parameter
        print(f"TARGET_URL not set, exiting")
        sys.exit(os.EX_DATAERR)

    # Output running config
    print(f"""
    Running HTTP LoadGen
    Target: {target_url}
    Avg RPS: {average_rps}
    Max RPS: {max_rps}
    Cycle Duration: {cycle_duration}
    Loop Count: {loop_count}
    """)

    if loop_count != 0:
        loop_num = 0
    else:
        loop_num = 1

    total_requests = 0 
    growth_per_loop = round(((max_rps-average_rps) / cycle_duration))
    current_thread_count = average_rps

    while loop_num != loop_count:
        print(f"Loop: {loop_num+1}/{loop_count}")
        for i in range(current_thread_count):
            print(f"Request: {i+1}/{current_thread_count}")
            x = threading.Thread( target=make_request, args=(i,))
            x.start
            total_requests += 1

        current_thread_count += growth_per_loop
        loop_num += 1

        # Reset climb
        if loop_num % cycle_duration == 0:
            current_thread_count = average_rps
        time.sleep(1)

    # Loop complete
    print(f"Completed a total of {total_requests} request(s)")

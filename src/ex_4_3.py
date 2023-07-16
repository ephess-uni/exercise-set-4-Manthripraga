import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    
    shutdowns = get_shutdown_events(logfile)
    
    sh1 = shutdowns[0]
    
    sh2 = shutdowns[-1]
       
    sh1_date = logstamp_to_datetime(sh1.split()[1])
    
    sh2_date = logstamp_to_datetime(sh2.split()[1])
    
    dfr = sh2_date-sh1_date
    
    return dfr


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
	


"""ex_5_0.py"""


def line_count(infile):
    with open(infile, "r") as f:
        print(len(f.readlines()))
        


if __name__ == "__main__":
    # get the utility function for path discovery
    try:
        from src.util import get_repository_root
    except ImportError:
        from util import get_repository_root

    # Test line_count with a file from the data directory
    data_directory = get_repository_root() / "data"
    line_count(data_directory / "ex_5_2-data.csv")
	

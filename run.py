import requests, os
from rich.console import Console
from rich.table import Table
from rich.progress import track

def te_get(api_url: str):
    headers = {"Accept": "application/json"}
    url = base_url + api_url
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return(response.json())
        else:
            print(f"Error: {response.json()['errorMessage']}")
    except:
        print("Error: Failed to get response")
        return (None)


# Setting up the environment
try:
    token = os.environ.get('TE_TOKEN')
    user = os.environ.get('TE_USER')
except:
    print("Error: Missing ThousandEyes User/Token...")
base_url = f"http://{user}:{token}@api.thousandeyes.com/v6/"
results = {}

# Define test rules
min_interval = 300
max_agents = 10
http_default_timeout = 5
pageload_default_timeout = 10

# Get test list
test_list = te_get("tests.json")['test']
print(f"\n\nReceived {len(test_list)} tests\n\n")

# Check agaist test rules
for test in track(test_list):
    # Check the test only if the following conditions apply:
    # 1. The test is enabled (disabled tests do not consume units).
    # 2. The test is not a saved event from the past.
    # 3. The test is not a live share (which consumes units from the source account).
    if test['enabled'] == 1 and test['savedEvent'] == 0 and test['liveShare'] == 0:
        test_details = te_get(f"tests/{test['testId']}.json")['test'][0]
        results[test_details['testName']] = []
        # Check number of agents
        if len(test_details['agents']) > max_agents:
            results[test_details['testName']].append(f"Test has {len(test_details['agents'])} agents > {max_agents}")
        # Check test interval
        if test_details['interval'] < min_interval:
            results[test_details['testName']].append(f"Test interval is {test_details['interval']} < {min_interval}")
        # Check http timeout
        if 'httpTimeLimit' in test_details:
            if test_details['httpTimeLimit'] != http_default_timeout:
                results[test_details['testName']].append(f"HTTP timeout is {test_details['httpTimeLimit']} != {http_default_timeout}")
        # Check page load timeout
        if 'pageLoadTimeLimit' in test_details:
            if test_details['pageLoadTimeLimit'] != pageload_default_timeout:
                results[test_details['testName']].append(f"Page load timeout is {test_details['pageload_default_timeout']} != {pageload_default_timeout}")

# Print results
print("\n\n")
console = Console()
table = Table(title="ThousandEyes Test Limit Check")
table.add_column("Test Name", justify="left", no_wrap=True)
table.add_column("Status", justify="left", no_wrap=True)
table.add_column("Details", justify="left", no_wrap=True)
#
for test_name, result in results.items():
    if len(result) == 0:
        table.add_row(test_name, "V", "")
    else:
        for i in range(len(result)):
            table.add_row(test_name, ":X::X::X:", result[i])
console.print(table)
# ThousandEyes Test Limit Verification

## The Challenge

ThousandEyes is an amazing solution for monitoring and analyzing customers' digital experience, as well as employees' digital experience. The system is very intuitive to operate, and it's hard not to turn everything on at once.
If the organization has guidance on the number of tests to run, the number of agents per test and/or the interval between tests - how will you track it?

## The Solution

This simple script will run a set of rules agaist the tests configured in your ThousandEyes account, and identify tests that are not in line with the rules.

## How to run the script
1. Create and activate a virtual environment
`python3 -m venv venv`
`source venv/bin/activate`
2. Install required packages
`pip install -r requirements.txt`
3. Set the environment variables
`export TE_USER=<Your ThousandEyes username>`
`export TE_TOKEN=<Your ThousandEyes token>`
.
    > The ThousandEyes basic authentication token can be found in the ThousandEyes dashboard > Account Settings > Users and roles > Profile
    
4. Run the script
`python run.py`
----
### Licensing info
Copyright (c) 2020 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

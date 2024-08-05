*** Settings ***
Library    OperatingSystem
Library    Process
*** Test Cases ***
Verify in robot
    ${result}=    Run Process    python3     get_ip.py    input1.json    shell=True    stdout=PIPE    stderr=PIPE
    Should Be Equal    ${result.rc}    0
    ${output}=    Get File    ${result.stdout}
    should be equal as numbers    ${output}    192.168.101.101

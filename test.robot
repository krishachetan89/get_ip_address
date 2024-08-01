*** Settings ***
Library    get_ip.py

*** Test Cases ***
Setting Variables
    ${result}=   get_ip.filename
    Should be equal as integers    ${result.rc}    0
    Should be equal as strings    ${result.stdout}    Hello World
# Lab 5: Static Code Analysis — Issue Report

## Objective

To identify and resolve code quality, security, and formatting issues in electricity_bill.py using Pylint, Bandit, and Flake8.

## Identified Issues and Fixes

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| B605 - Shell Command Injection | Security (High) | 63 | os.system() executed a shell command containing a user-supplied meter IP address, creating a command injection risk. | Replaced os.system() with http.client.HTTPConnection and validated the IP address using ipaddress. |
| B314 - Unsafe XML Parsing | Security (Medium) | 18 | xml.etree.ElementTree.fromstring() was used to parse XML and could be unsafe for untrusted input. | Replaced the standard XML parser with defusedxml.ElementTree. |
| B405 - Unsafe XML Import | Security (Low) | 3 | The program imported xml.etree.ElementTree, which Bandit flagged for potential XML security vulnerabilities. | Replaced the import with defusedxml.ElementTree. |
| B105 - Hardcoded Password | Security (Low) | 13 | A password was stored directly in the source code. | Removed the unused hardcoded password. |
| W0102 - Mutable Default Argument | Bug | 42 | The generateBill() function used extras={} as a default argument, which could cause shared mutable state. | Replaced the default dictionary with None and initialized a new dictionary inside the function. |
| C0103 - Invalid Naming Convention | Code Quality | 17, 22, 29, 42, 50, 56, 61 | Several functions and variables used camelCase instead of snake_case. | Renamed functions, arguments, and variables to follow Python naming conventions. |
| C0114/C0116 - Missing Docstrings | Documentation | 1, 17, 22, 29, 42, 50, 56, 61, 66 | The module and functions lacked documentation strings. | Added descriptive module and function docstrings. |
| W0613 - Unused Argument | Code Quality | 50 | The currency parameter in averageBill() was never used. | Removed the unused parameter and updated the function call. |
| W1514 - Missing Encoding | Code Quality | 57 | The file was opened without explicitly specifying its encoding. | Added encoding="utf-8" to the open() call. |
| E302 - Missing Blank Line | Formatting | 22 | There were insufficient blank lines between top-level functions. | Added the required blank line. |
| E203 - Whitespace Before Colon | Formatting | 44 | An unnecessary space appeared before a dictionary colon. | Removed the extra whitespace. |
| E501 - Line Too Long | Formatting | 72 | A print statement exceeded the recommended maximum line length. | Split the statement across multiple lines. |
| E225 - Missing Operator Whitespace | Formatting | 76 | An assignment operator lacked surrounding spaces. | Added spaces around the assignment operator. |

Note: Line numbers refer to the original source file and original analysis reports.

## Analysis Results

| Tool | Before Fixes | After Fixes |
|---|---|---|
| Pylint | 5.44/10 | 10.00/10 |
| Bandit | 4 security issues | 0 security issues |
| Flake8 | 4 formatting violations | 0 formatting violations |

## Functional Verification

The electricity billing program was executed before and after the corrections.

The final output remained consistent:

- Highest bill: M2
- Average bill: Rs. 934.50
- Total billed: Rs. 3738.00
- Number of bills generated: 4

The static analysis findings were resolved without changing the demonstrated electricity bill calculations.

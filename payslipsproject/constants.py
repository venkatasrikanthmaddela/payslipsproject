__author__ = 'oliverqueen'

PAYSLIPS_UPLOAD_FORMAT_VERSION = ["1.0"]

PAYSLIPS_UPLOAD_FORMAT = {
    "1.0": {"employee name": ["<type 'str'>", "<type 'unicode'>"],
            "email id": ["<type 'str'>", "<type 'unicode'>"],
            "department": ["<type 'str'>", "<type 'unicode'>"],
            "designation": ["<type 'str'>", "<type 'unicode'>"],
            "basic and da": ["<type 'float'>", "<type 'int'>"],
            "house rent allowance": ["<type 'float'>", "<type 'int'>"],
            "conveyance": ["<type 'float'>", "<type 'int'>"],
            "special allowance": ["<type 'float'>", "<type 'int'>"],
            "o.t": ["<type 'float'>", "<type 'int'>"],
            "leave travel allowance": ["<type 'float'>", "<type 'int'>"],
            "other deduction reimbt": ["<type 'float'>", "<type 'int'>"],
            "edu allow": ["<type 'float'>", "<type 'int'>"],
            "med. allowance": ["<type 'float'>", "<type 'int'>"],
            "gross earnings": ["<type 'float'>", "<type 'int'>"],
            "provident fund": ["<type 'float'>", "<type 'int'>"],
            "esi": ["<type 'float'>", "<type 'int'>"],
            "prof tax": ["<type 'float'>", "<type 'int'>"],
            "income tax": ["<type 'float'>", "<type 'int'>"],
            "salary advance": ["<type 'float'>", "<type 'int'>"],
            "cug": ["<type 'float'>", "<type 'int'>"],
            "lwf": ["<type 'float'>", "<type 'int'>"],
            "other deductions": ["<type 'float'>", "<type 'int'>"],
            "arrears pf deduction": ["<type 'float'>", "<type 'int'>"],
            "arrears esi deduction": ["<type 'float'>", "<type 'int'>"],
            "total deduction": ["<type 'float'>", "<type 'int'>"],
            "net pay": ["<type 'float'>", "<type 'int'>"],
            "month":["<type 'int'>", "<type 'float'>"], "year":["<type 'int'>", "<type 'float'>"],
            "employee number":["<type 'str'>", "<type 'unicode'>"],
            "bank name":["<type 'str'>", "<type 'unicode'>"],
            "bank account number":["<type 'str'>", "<type 'unicode'>", "<type 'float'>"],
            "pan number":["<type 'str'>", "<type 'unicode'>"],
            "ppf number":["<type 'str'>", "<type 'unicode'>"],
            "location":["<type 'str'>", "<type 'unicode'>"],
            "effective work days":["<type 'int'>", "<type 'float'>"],
            "earned basic and da":["<type 'int'>", "<type 'float'>"],
            "earned house rent allowance":["<type 'int'>", "<type 'float'>"],
            "earned conveyance":["<type 'int'>", "<type 'float'>"],
            "earned special allowance":["<type 'int'>", "<type 'float'>"],
            "earned o.t":["<type 'int'>", "<type 'float'>"],
            "earned leave travel allowance":["<type 'int'>", "<type 'float'>"],
            "earned other deduction reimbt":["<type 'int'>", "<type 'float'>"],
            "increment":["<type 'int'>", "<type 'float'>"],
            "earned increment":["<type 'int'>", "<type 'float'>"],
            "earned edu allow":["<type 'int'>", "<type 'float'>"],
            "earned med. allowance":["<type 'int'>", "<type 'float'>"],
            "house maintenance":["<type 'int'>", "<type 'float'>", "<type 'unicode'>"],
            "earned house maintenance":["<type 'int'>", "<type 'float'>", "<type 'unicode'>"],
            "driver salary":["<type 'int'>", "<type 'float'>", "<type 'unicode'>"],
            "earned driver salary":["<type 'int'>", "<type 'float'>", "<type 'unicode'>"],
            "car maintenance":["<type 'int'>", "<type 'float'>", "<type 'unicode'>"],
            "earned car maintenance":["<type 'int'>", "<type 'float'>", "<type 'unicode'>"],
            "fuel reimbursement":["<type 'int'>", "<type 'float'>", "<type 'unicode'>"],
            "earned fuel reimbursement":["<type 'int'>", "<type 'float'>", "<type 'unicode'>"],
            "incentives":["<type 'int'>", "<type 'float'>", "<type 'unicode'>"],
            "earned incentives":["<type 'int'>", "<type 'float'>", "<type 'unicode'>"]
            }
}

PAYSLIPS_UPLOAD_TUPLE_FORMAT = {
    "1.0":('employee name', 'email id',
           'employee number', 'designation',
           'location', 'department',
           'bank name',
           'bank account number',
           'ppf number',
           'month',
           'year',
           'pan number',
           'effective work days',
           "basic and da",
           "earned basic and da",
           "house rent allowance",
           "earned house rent allowance",
           "conveyance",
           "earned conveyance",
           "special allowance",
           "earned special allowance",
           "o.t",
           "earned o.t",
           "leave travel allowance",
           "earned leave travel allowance",
           "other deduction reimbt",
           "earned other deduction reimbt",
           "increment",
           "earned increment",
           "edu allow",
           "earned edu allow",
           "med. allowance",
           "earned med. allowance",
           "house maintenance",
           "earned house maintenance",
           "driver salary",
           "earned driver salary",
           "car maintenance",
           "earned car maintenance",
           "fuel reimbursement",
           "earned fuel reimbursement",
           "incentives",
           "earned incentives",
           "provident fund", "esi", "prof tax", "income tax", "salary advance",
           "cug", "lwf", "other deductions",
           "arrears pf deduction", "arrears esi deduction"
           )
}
SAMPLE_DATA = ("srikanthmv", "mvsrikanth230@gmail.com", "HIN80",
               "software developer", "kukatpalli", "IT",
               "IDBI Bank ltd.", "0280104000225373", "12345",
               "4", "2017", "COUP2563",
               "28", "19500", "19500", "9750", "9750",
               "1600", "1600", "4700", "4700", "0",
               "0", "2000", "2000", "0", "0", "0", "0",
               "200", "200", "1250", "1250", "0", "0",
               "0", "0", "0", "0", "0", "0", "0", "0")


BASIC_DETAILS = [
    'employee name', 'email id',
    'employee number', 'designation',
    'location', 'department',
    'bank name',
    'bank account number',
    'ppf number',
    'month',
    'year',
    'pan number',
    'effective work days'
]

DEDUCTION_FIELDS = ["provident fund", "esi", "prof tax", "income tax", "salary advance", "cug", "lwf", "other deductions", "arrears pf deduction", "arrears esi deduction"]

EARNING_FIELDS = [
    "basic and da",
    "house rent allowance",
    "conveyance",
    "special allowance",
    "o.t",
    "leave travel allowance",
    "other deduction reimbt",
    "increment",
    "edu allow",
    "med. allowance",
    "house maintenance",
    "driver salary",
    "car maintenance",
    "fuel reimbursement",
    "incentives"]

ACTUAL_EARNING_FIELDS = [
    "earned basic and da",
    "earned house rent allowance",
    "earned conveyance",
    "earned special allowance",
    "earned o.t",
    "earned leave travel allowance",
    "earned other deduction reimbt",
    "earned increment",
    "earned edu allow",
    "earned med. allowance",
    "earned house maintenance",
    "earned driver salary",
    "earned car maintenance",
    "earned fuel reimbursement",
    "earned incentives"
]

EXEMPTION_FIELDS = [
    "earned house maintenance",
    "earned driver salary",
    "earned car maintenance",
    "earned fuel reimbursement",
    "earned incentives",
    "house maintenance",
    "driver salary",
    "car maintenance",
    "fuel reimbursement",
    "incentives",
    "salary advance",
    "earned other deduction reimbt",
    "other deduction reimbt",
    "increment",
    "arrears pf deduction",
    "earned increment",
    "cug",
    "esi",
    "arrears esi deduction",
    "lwf",
    "o.t",
    "earned o.t"

]

COMPANY_DETAILS = {
    "NameOfTheOrganization":"HINSHITSU MANUFACTURING PVT LTD",
    "AddressOfTheOrganization":"GSR Estates, D Block,II Floor, H No : 11-6-56,Sr No 257&258/1,IDPL Railway Sliding Road, Moosapat ,Kukatpally ,Hyderabad."
}


BULK_IMPORT_ERROR_SCHEMA = {
    "HEADER MISMATCH": "4201",
    "DATA MISSING": "4281",
    "SHEET EMPTY": "4000",
    "DATA FORMAT ERROR": "4222",
    "INVALID EMAILS":"4223",
    "DUPLICATES": "4533",
    "INTERNET CONNECTION":"2500",
    "MAILS LIMIT EXCEEDED": "2501"
}
BULK_IMPORT_ERROR_CODES = {
    "4201": "Header values Doesn't match. please check with the sample template and try again. Thank you",
    "4281": "The data for a mandatory field is missing. we cannot allow as it is a mandatory field. please try again. Thank you",
    "4000": "The sheet is empty. The uploaded sheet dont have any data in it. please check and try again. Thank you",
    "4222": "The data which you are trying to upload has different format. please check the sheet and try again. Thank you",
    "4223": "Some emails are not valid in the given data. please correct them and try again. Thank you",
    "4533": "We found some duplicates on the given data. please remove them and try again. Thank you",
    "2500": "No internet connection found. please check",
    "2501": "Email limit for today is exceeded."
}

MANDATORY_FIELDS_FOR_PAYSLIP = list(set(BASIC_DETAILS + DEDUCTION_FIELDS + EARNING_FIELDS + ACTUAL_EARNING_FIELDS) - set(EXEMPTION_FIELDS))



# MANDATORY_FIELDS_FOR_PAYSLIP = [
#     "employee name","email id","department","designation","Basic and DA","House Rent Allowance",
#     "Conveyance",
#     "Special Allowance",
#     "O.T",
#     "Leave Travel Allowance",
#     "Other Deduction Reimbt",
#     "Arrears",
#     "Edu Allow",
#     "Med. Allowance",
#     "Gross Earnings",
#     "Provident Fund",
#     "Prof Tax",
#     "Income Tax",
#     "Salary Advance",
#     "CUG",
#     "LWF",
#     "Other Deductions",
#     "Arrears PF Deduction",
#     "Arrears ESI Deduction",
#     "Total Deduction",
#     "Net Pay",
#     "month",
#     "year",
#     "employee number",
#     "bank account number",
#     "ppf number",
#     "location",
#     "effective work days",
# ]

# MANDATORY_FIELDS_FOR_PAYSLIP = ["income tax"]

SAMPLE_DICT = {u'gross earnings': 39000, u'net pay': 33677, u'total deduction': 5323, u'other deduction reimbt': 0, u'special allowance': 4700, u'arrears': 0, u'salary advance': 0, u'employee name': u'mv srikanth', u'arrears pf deduction': 0, u'leave travel allowance': 2000, u'provident fund': 1800, u'cug': 0, u'department': u'IT', u'basic and da': 19500, u'lwf': 0, u'esi': 0, u'income tax': 1523, u'arrears esi deduction': 0, u'med. allowance': 1250, u'o.t': 0, u'other deductions': 1800, u'house rent allowance': 9750, u'prof tax': 200, u'designation': u'software developer', u'edu allow': 200, u'conveyance': 1600, u'email id': u'srikk1309@live.com', u'month':2, u'year':2017}

MONTHS = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",

    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}
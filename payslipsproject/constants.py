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
            "arrears": ["<type 'float'>", "<type 'int'>"],
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
            "net pay": ["<type 'float'>", "<type 'int'>"]
            }
}

DEDUCTION_FIELDS = ["provident fund","esi","prof tax", "income tax", "salary advance", "cug", "lwf", "other deductions", "arrears pf deduction", "arrears esi deduction"]

EARNING_FIELDS = ["basic and da", "house rent allowance", "conveyance", "special allowance", "o.t", "leave travel allowance", "other deduction reimbt", "arrears", "edu allow", "med. allowance"]

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

MANDATORY_FIELDS_FOR_PAYSLIP = ["employee name","email id","department","designation","Basic and DA","House Rent Allowance",
                                "Conveyance",
                                "Special Allowance",
                                "O.T",
                                "Leave Travel Allowance",
                                "Other Deduction Reimbt",
                                "Arrears",
                                "Edu Allow",
                                "Med. Allowance",
                                "Gross Earnings",
                                "Provident Fund",
                                "ESI",
                                "Prof Tax",
                                "Income Tax",
                                "Salary Advance",
                                "CUG",
                                "LWF",
                                "Other Deductions",
                                "Arrears PF Deduction",
                                "Arrears ESI Deduction",
                                "Total Deduction",
                                "Net Pay"]

SAMPLE_DICT = {u'gross earnings': 39000, u'net pay': 33677, u'total deduction': 5323, u'other deduction reimbt': 0, u'special allowance': 4700, u'arrears': 0, u'salary advance': 0, u'employee name': u'mv srikanth', u'arrears pf deduction': 0, u'leave travel allowance': 2000, u'provident fund': 1800, u'cug': 0, u'department': u'IT', u'basic and da': 19500, u'lwf': 0, u'esi': 0, u'income tax': 1523, u'arrears esi deduction': 0, u'med. allowance': 1250, u'o.t': 0, u'other deductions': 1800, u'house rent allowance': 9750, u'prof tax': 200, u'designation': u'software developer', u'edu allow': 200, u'conveyance': 1600, u'email id': u'srikk1309@live.com'}

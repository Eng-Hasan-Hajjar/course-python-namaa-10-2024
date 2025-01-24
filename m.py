import pandas as pd

# إنشاء قائمة بالدوال المتعلقة بالتاريخ والوقت في Excel مع شرح وأمثلة
data = {
    "Function": [
        "TODAY()", "NOW()", "DATE(year, month, day)", "TIME(hour, minute, second)",
        "YEAR(date)", "MONTH(date)", "DAY(date)", "HOUR(time)", "MINUTE(time)", "SECOND(time)",
        "WEEKDAY(date, [return_type])", "WEEKNUM(date, [return_type])", "EOMONTH(start_date, months)",
        "EDATE(start_date, months)", "DATEDIF(start_date, end_date, unit)", "TEXT(value, format_text)"
    ],
    "Description": [
        "Returns the current date without time.",
        "Returns the current date and time.",
        "Creates a date from year, month, and day values.",
        "Creates a time from hour, minute, and second values.",
        "Extracts the year from a date.",
        "Extracts the month from a date.",
        "Extracts the day from a date.",
        "Extracts the hour from a time.",
        "Extracts the minute from a time.",
        "Extracts the second from a time.",
        "Returns the day of the week (1=Sunday, 7=Saturday).",
        "Returns the week number of the year.",
        "Returns the last day of the month after a given number of months.",
        "Returns the date before or after a specified number of months.",
        "Calculates the difference between two dates in years, months, or days.",
        "Formats a date or time as text with a specific format."
    ],
    "Example": [
        "=TODAY() → 2025-01-20",
        "=NOW() → 2025-01-20 14:30:00",
        "=DATE(2025, 1, 20) → 2025-01-20",
        "=TIME(14, 30, 0) → 14:30:00",
        "=YEAR(A1) → 2025 (if A1 contains 2025-01-20)",
        "=MONTH(A1) → 1 (if A1 contains 2025-01-20)",
        "=DAY(A1) → 20 (if A1 contains 2025-01-20)",
        "=HOUR(A2) → 14 (if A2 contains 14:30:00)",
        "=MINUTE(A2) → 30 (if A2 contains 14:30:00)",
        "=SECOND(A2) → 0 (if A2 contains 14:30:00)",
        "=WEEKDAY(A1) → 2 (Monday, if A1 contains 2025-01-20)",
        "=WEEKNUM(A1) → 4 (if A1 contains 2025-01-20)",
        "=EOMONTH(A1, 0) → 2025-01-31 (if A1 contains 2025-01-20)",
        "=EDATE(A1, 2) → 2025-03-20 (if A1 contains 2025-01-20)",
        "=DATEDIF(A1, A2, 'Y') → 5 (years difference if A1=2020-01-20 and A2=2025-01-20)",
        "=TEXT(A1, 'YYYY-MM-DD') → 2025-01-20 (if A1 contains a date)"
    ]
}

# تحويل البيانات إلى DataFrame
df = pd.DataFrame(data)

# حفظ الملف بصيغة Excel
file_path = "/Excel_Date_Time_Functions.xlsx"
df.to_excel(file_path, index=False)

file_path

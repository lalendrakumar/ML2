import sys
from src.logger import logging

# 1️⃣ Function to get error details
def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    return f"Error occurred in Python script name [{file_name}] line number [{line_number}] error message [{error}]"

# 2️⃣ Custom Exception Class
class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message



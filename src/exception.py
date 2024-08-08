import sys

def error_message_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occoured in script : {file_name}, line no : {exc_tb.tb_lineno} and error message is {str(error)}"
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_details:sys) -> str:
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_details=error_details)

    def __str__(self) -> str:
        return self.error_message
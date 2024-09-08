import sys
from src.logger import logging

def error_message_details(error,error_details:sys):
    '''
        error_details.exc_info() returns a tuple of three values: the type of the exception, the exception instance, and a traceback object.
        _, _, exc_tb = error_details.exc_info(): Unpacks the traceback object (exc_tb).
    '''
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
    



# testing exception.py
# if __name__== "__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info(e)
#         raise CustomException(e,sys)
        


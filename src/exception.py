import sys 
## sys: Used to access exception details.
##logging: Presumably your custom logger from src/logger.py.
from src.logger import logging



##error: The actual exception.
##error_detail: A reference to sys, so it can dig into technical error info.
##It then:
##Extracts details about where the error occurred: filename, line number.
##Creates a descriptive message like: "Error occurred in python script name [main.py] line number [42] error message [ZeroDivisionError: division by zero]"
def error_message_detail(error,error_detail:sys):

    _,_,exc_tb=error_detail.exc_info() ##exc_info() gives a tuple with three parts: type, value, and traceback , You're ignoring the first two (_) and capturing the traceback object (exc_tb) — which shows where the error occurred.
    file_name=exc_tb.tb_frame.f_code.co_filename #Digs into the traceback to find the file name of the script where the error happened.
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error)) #Builds a neat string with:the file name the line number where the error occurred (exc_tb.tb_lineno)the actual error message (converted to a string)

    return error_message

    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(str(e), sys)
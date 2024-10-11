import logging

#The below one just prints just like that
logging.basicConfig(level=logging.INFO,filename="log1.log",filemode="w")

#This one we are using format parameter



#logging.basicConfig(level=logging.DEBUG,filename="log.log",filemode="w",
                    #format="%(asctime)s - %(levelname)s - %(message)s")

'''
try:
    1/0
except ZeroDivisionError:
    #logging.error("zero division error")
    logging.error("zero division error",exc_info=True)

x=2
#logging.info("the value of x is %d",x)
logging.info("the value of x is {}".format(x))
'''
logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.error("this is error message")
logging.critical("this is critical message")

'''
#creating an object
logger=logging.getLogger()

#setting threshold
logger.setLevel(logging.DEBUG)

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
'''
'''
#logging exceptions:
def perform_operation(x):
    if x<0:
        raise ValueError("Number should not be less than 0")
    else:
        logging.info(f"the value of x is {x}")

try:
    x=int(input("Enter a number:"))
    perform_operation(x)
except ValueError as ve:
    logging.exception("exception occured %s",ve)
'''
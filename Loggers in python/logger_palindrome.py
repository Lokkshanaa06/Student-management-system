import logging
import os

log_directory="Loggers in python"
log_file="palindrome.log"
log_path=os.path.join(log_directory,log_file)

logging.basicConfig(level=logging.DEBUG,filename=log_path,
                    format="%(asctime)s - %(levelname)s - %(message)s")

os.makedirs(log_directory,exist_ok=True)

def main():
    
    def palindrome(n):
        n1=n
        res=0
        while n>0:
            n2=n%10
            res=(res*10)+n2
            n//=10
        if n1==res:
            logging.info(f"{n1} is palindrome")
        else:
            logging.info(f"{n1} is not palindrome")  
    
    try:
        num=int(input("Enter the number:"))
        palindrome(num)
    except ValueError as ve:
        logging.exception("Exception occured %s",ve)

if __name__=='__main__':
    main()
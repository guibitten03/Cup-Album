from persistence import *

def check_type(e, compair_type):
    if not (isinstance(e, compair_type)):
            raise Exception(f"Recived object is not of {compair_type.__name__} Type")
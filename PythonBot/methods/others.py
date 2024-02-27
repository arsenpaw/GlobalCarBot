import logging
import re
async def is_vin_valid(msg:str)-> bool:
    logging.info('is_vin_valid')
    pattern = r'^[A-HJ-NPR-Za-hj-npr-z\d]{8}[\dX][A-HJ-NPR-Za-hj-npr-z\d]{2}\d{6}$'
    match = re.match(pattern, msg)
    return True if match is not None or 'https://' in msg  else False
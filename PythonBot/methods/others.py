import re
async def is_vin_valid(vin:str)-> bool:
    pattern = r'^[A-HJ-NPR-Za-hj-npr-z\d]{8}[\dX][A-HJ-NPR-Za-hj-npr-z\d]{2}\d{6}$'
    vin.strip()
    match = re.match(pattern, vin)
    return True if match is True else False
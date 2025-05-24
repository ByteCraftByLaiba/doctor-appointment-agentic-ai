import re # importing regular expression
from pydantic import BaseModel, Field, field_validator

class DateTimeModel(BaseModel):
    Date : str = Field(description="Date Format DD-MM-YYYY HH:MM", pattern = r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$')

    # self → You already have the object (e.g., a DateTimeModel with a filled-in value).
    # cls → You're defining rules before the object is fully created.
    @field_validator("Date")
    def check_format_date(cls, value):
        if not re.match('^\d{2}-\d{2}-\d{4} \d{2}:\d{2}$', value):
            raise ValueError("Date should be in this format : DD-MM-YYYY HH:MM")
        else:
            return value
        

class DateModel(BaseModel):
    Date : str = Field(description="Date Format DD-MM-YYYY", pattern = r'^\d{2}-\d{2}-\d{4}$')

    # self → You already have the object (e.g., a DateTimeModel with a filled-in value).
    # cls → You're defining rules before the object is fully created.
    @field_validator("Date")
    def check_format_date(cls, value):
        if not re.match('^\d{2}-\d{2}-\d{4}$', value):
            raise ValueError("Date should be in this format : DD-MM-YYYY")
        else:
            return value
        
class IdentificationNumberModel(BaseModel):
    id : int = Field(description="Identification number must be of length 6-7.")

    @field_validator("id")
    def check_format_id(cls, value):
        if not re.match('^\d{6,7}&', str(value)):
            raise ValueError("Identification number must be of length 6-7.")
        return value
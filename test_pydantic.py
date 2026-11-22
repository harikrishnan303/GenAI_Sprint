from pydantic import BaseModel,field_validator

class MovieReview(BaseModel):##BaseModel is the blueprint for creating data 
    titile:str
    rating:float
    is_recommended:bool=True

    @field_validator("rating") #used to validate input with constraints + runs the function below it
    @classmethod
    
    def check_rating_range(cls,value:float)->float:
        if value<0 or value>5:
            raise ValueError("Rating must be betwee 0 and 5")
        return value


good_review=MovieReview("interstellar",4.5)
print(good_review)
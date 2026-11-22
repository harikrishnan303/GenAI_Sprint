from typing import Optional
from pydantic import BaseModel,field_validator


class MovieReview(BaseModel):

    title:str
    rating:float
    summary:Optional[str]=None
    is_recommended:bool=True

    @field_validator("rating")
    @classmethod

    def check_rating_range(cls,value:float)->float:
            if value<0 or value>5:
                raise ValueError("Rating must be betwee 0 and 5")
            return value

review=MovieReview(title="Interstellar",rating=4.5)

print("As python dict:",review.model_dump())
print("As JSON text:\n",review.model_dump_json(indent=2))
from pydantic import BaseModel, Field, ValidationError
class NutritionEstimate(BaseModel):
    name: str = Field(min_length=1)
    calories: float = Field(ge=0, description="Energy in kcal")
    protein: float = Field(ge=0, description="Protein in grams")
    carbs: float = Field(ge=0, description="Carbohydrates in grams")
    fat: float = Field(ge=0, description="Fat in grams")
    note: str
    source: str = Field(min_length=1)

class FoodItem(BaseModel):
    name: str = Field(min_length=1)
    quantity: float = Field(gt=0)
    unit: str = Field(min_length=1)
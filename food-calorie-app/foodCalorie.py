from pydantic import BaseModel, Field, ValidationError ,validator

# Input after parsing the user's meal description
class FoodItem(BaseModel):
    name: str = Field(min_length=1)
    quantity: float = Field(gt=0)
    unit: str = Field(min_length=1)

# Standard output from any estimation stage
class NutritionEstimate(BaseModel):
    name: str = Field(min_length=1)
    calories: float = Field(ge=0, description="Energy in kcal")
    protein: float = Field(ge=0, description="Protein in grams")
    carbs: float = Field(ge=0, description="Carbohydrates in grams")
    fat: float = Field(ge=0, description="Fat in grams")
    note: str
    source: str = Field(min_length=1)

#nutrition_estimate = NutritionEstimate(name="Apple", calories=52, protein=0.3, carbs=14, fat=0.2, note="Red delicious", source="inmemory json")
#print(nutrition_estimate)    
food = FoodItem(name="Banana", quantity=1, unit="piece")
print(food)
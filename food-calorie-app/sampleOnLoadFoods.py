from foodCalorie import NutritionEstimate

# Illustrative sample values for testing.
# Each entry describes the portion stated in its note.
FOOD_DATA = [
    {
        "name": "Banana",
        "calories": 105,
        "protein": 1.3,
        "carbs": 27,
        "fat": 0.4,
        "note": "One medium banana. Approximate sample values.",
        "source": "sample_local_table",
    },
    {
        "name": "Apple",
        "calories": 95,
        "protein": 0.5,
        "carbs": 25,
        "fat": 0.3,
        "note": "One medium apple. Approximate sample values.",
        "source": "sample_local_table",
    },
    {
        "name": "Cooked rice",
        "calories": 130,
        "protein": 2.7,
        "carbs": 28,
        "fat": 0.3,
        "note": "100 grams of cooked white rice. Approximate sample values.",
        "source": "sample_local_table",
    },
    {
        "name": "Idli",
        "calories": 60,
        "protein": 2,
        "carbs": 12,
        "fat": 0.5,
        "note": "One medium idli. Approximate sample values.",
        "source": "sample_local_table",
    },
    {
        "name": "Chapati",
        "calories": 100,
        "protein": 3,
        "carbs": 20,
        "fat": 1,
        "note": "One medium chapati without added oil. Approximate sample values.",
        "source": "sample_local_table",
    },
    {
        "name": "Boiled egg",
        "calories": 78,
        "protein": 6.3,
        "carbs": 0.6,
        "fat": 5.3,
        "note": "One large boiled egg. Approximate sample values.",
        "source": "sample_local_table",
    },
]

# Validate every sample against your Pydantic schema.
FOOD_ESTIMATES = [
    NutritionEstimate.model_validate(item)
    for item in FOOD_DATA
]


if __name__ == "__main__":
    for food in FOOD_ESTIMATES:
        print(food.model_dump_json(indent=2))
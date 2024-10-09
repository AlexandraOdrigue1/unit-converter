def conversion_process(value, unit_from, unit_to, category):
    conversions = {
        'length': {
            'm': 1,
            'km': 1000,
            'cm': 0.01,
            'mm': 0.001,
            'inch': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mile': 1609.34
        },
        'weight': {
            'kg': 1,
            'g': 0.001,
            'mg': 0.000001,
            'lb': 0.453592,
            'oz': 0.0283495
        },
        'temperature': {
            'C': lambda c: c,
            'F': lambda c: (c * 9/5) + 32,
            'K': lambda c: c + 273.15
        }
    }
    
    if category == 'temperature':
        # Convert to Celsius first
        if unit_from == 'F':
            value = (value - 32) * 5/9
        elif unit_from == 'K':
            value = value - 273.15
        
        # Then convert from Celsius to target unit
        return conversions[category][unit_to](value)
    else:
        # For length and weight, convert to base unit then to target unit
        base_value = value * conversions[category][unit_from]
        return base_value / conversions[category][unit_to]

def calculate_conversion(value, unit_from, unit_to, category):
    result = conversion_process(value, unit_from, unit_to, category)
    return round(result, 4)

def get_user_input():
    categories = ['length', 'weight', 'temperature']
    
    print("Welcome to the Unit Converter!")
    print("Available categories: length, weight, temperature")
    
    category = input("Enter the category: ").lower()
    while category not in categories:
        category = input("Invalid category. Please enter length, weight, or temperature: ").lower()
    
    value = float(input("Enter the value to convert: "))
    unit_from = input("Enter the unit to convert from: ")
    unit_to = input("Enter the unit to convert to: ")
    
    return value, unit_from, unit_to, category

def main():
    value, unit_from, unit_to, category = get_user_input()
    result = calculate_conversion(value, unit_from, unit_to, category)
    print(f"{value} {unit_from} is equal to {result} {unit_to}")

if __name__ == "__main__":
    main()

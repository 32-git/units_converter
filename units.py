# Map the units to their symbols for easier processing afterwards
unit_mappings = {
    "Length": {
        'Centimeter (cm)': 'cm',
        'Meter (m)': 'm',
        'Kilometer (km)': 'km',
        'Inch (in)': 'in',
        'Foot (ft)': 'ft',
        'Mile (mi)': 'mi'
    },
    "Area": {
        'Square centimeter (cm\u00b2)': 'cm^2',
        'Square meter (m\u00b2)': 'm^2',
        'Square kilometer (km\u00b2)': 'km^2', 
        'Acre (a)': 'a',  
        'Hectare (ha)': 'ha'
    },
    "Volume": {
        'Cubic centimeter (cm\u00b3)': 'cm^3',
        'Cubic meter (m\u00b3)': 'm^3',
        'Millileter (ml)': 'ml',
        'Liter (l)': 'l'
    },
    "Mass": {
        'Milligram (mg)': 'mg',
        'Gram (g)': 'g',
        'Kilogram (kg)': 'kg',
        'Pounds (lbs)': 'lbs',
        'Ounce (oz)': 'oz'
    },
    "Temperature":{
        'Celsius (°C)': '°C',
        'Fahrenheit (°F)': '°F',
        'Kelvin (K)': 'K'
    }
}

def convert(field, input_unit, output_unit, i): # i is the input value
    try:
        i = float(i)
    except ValueError:
        return "Invalid input."

    units = {
        "Length": {
            "cm": {
                'm': i/100,
                'km': i/100000,
                'in': i/2.54,
                'ft': i/30.48,
                'mi': i/160900,
            },
            "m": {
                'cm': i*100,
                'km': i/1000,
                'in': i*39.37,
                'ft': i*3.280839895,
                'mi': i/1609,
            },
            "km": {
                'cm': i*100000,
                'm': i*1000,
                'in': i*39370.1,
                'ft': i*3280.84,
                'mi': i/1.609,
            },
            "in": {
                'cm': i*2.54,
                'm': i/39.37,
                'km': i/39370.1,
                'ft': i*30.48,
                'mi': i/63360,
            },
            "ft": {
                'cm': i*30.48,
                'm': i*0.3048,
                'km': i/3280.84,
                'in': i*12,
                'mi': i/5280,
            },
            "mi": {
                'cm': i*160934.4,
                'm': i*1609.344,
                'km': i*1.609344,
                'in': i*63360,
                'ft': i*5280,
            }
        },
        "Area": {
            "cm^2": {
                'm^2': 1/10000,
            }
        },
        "Volume": {
            "cm^3": {
                'ml': i*1
            }
        },
        "Mass": {
            "g": {

            }
        },
        "Temperature": {
            "°C": {
                '°F': (i * 9/5) + 32,
                'K': i + 273.15
            },
            "°F": {
                '°C': 5/9 * (i - 32),
                'K': 5/9 * (i + 459.67)
            },
            "K": {
                '°C': i - 273.15,
                '°F': i * 9/5 - 459.67
            }
        },
    }
    
    try:
        return units[field][input_unit][output_unit]
    except KeyError:
        return "Are you dumb?"
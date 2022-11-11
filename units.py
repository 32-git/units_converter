# Map the units to their symbols for easier processing afterwards
unit_mappings = {
    "Length": {
        'Millimeter (mm)': 'mm',
        'Centimeter (cm)': 'cm',
        'Meter (m)': 'm',
        'Kilometer (km)': 'km',
        'Inch (in)': 'in',
        # 'Foot (ft)': 'ft',
        # 'Yard (yd)': 'yd',
        'Mile (mi)': 'mi',
        # '* Feet and inches (ft in)': 'ft_in'
    },
    "Area": {
        'Square meter (m\u00b2)': 'm\u00b2',
        'Square kilometer (km\u00b2)': 'km\u00b2', 
        'Square inch (in\u00b2)': 'in\u00b2',
        'Square foot (ft\u00b2)': 'ft\u00b2',
        'Acre (ac)': 'ac',  
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
                'km': i/100_000,
                'in': i/2.54,
                'ft': i/30.48,
                'mi': i/160900
            },
            "m": {
                'cm': i*100,
                'km': i/1000,
                'in': i*39.37,
                'ft': i*3.280839895,
                'mi': i/1609
            },
            "km": {
                'cm': i*100_000,
                'm': i*1000,
                'in': i*39370.1,
                'ft': i*3280.84,
                'mi': i/1.609
            },
            "in": {
                'cm': i*2.54,
                'm': i/39.37,
                'km': i/39370.1,
                'ft': i*30.48,
                'mi': i/63360
            },
            "ft": {
                'cm': i*30.48,
                'm': i*0.3048,
                'km': i/3280.84,
                'in': i*12,
                'mi': i/5280
            },
            "mi": {
                'cm': i*160934.4,
                'm': i*1609.344,
                'km': i*1.609344,
                'in': i*63360,
                'ft': i*5280
            }
        },
        "Area": {
            "m\u00b2": {
                'km\u00b2': i/1_000_000,
                'in\u00b2': i*1550.0031,
                'ft\u00b2': i*10.764,
                'ac': i/4_046.8564,
                'ha': i/10_000
            },
            "km\u00b2": {
                'm\u00b2': i*1_000_000,
                'in\u00b2': i*1_550_003_100,
                'ft\u00b2': i*10_763_910.4167,
                'ac': i*247.1054,
                'ha': i*100 
            },
            "in\u00b2": {
                'm\u00b2': i/1550.0031,
                'km\u00b2': i/1_550_003_100,
                'ft\u00b2': i/144,
                'ac': i/6_272_640,
                'ha': i/15_500_031
            },
            "ft\u00b2": {
                'm\u00b2': i/10.764,
                'km\u00b2': i/10_763_910.4167,
                'in\u00b2': i*144,
                'ac': i/43_560,
                'ha': i/107_639.1042,
            },
            "ac": {
                'm\u00b2': i*4_046.8564,
                'km\u00b2': i/247.1054,
                'in\u00b2': i*6_272_640,
                'ft\u00b2': i*43_560,
                'ha': i/2.4711
            },
            "ha": {
                'm\u00b2': i*10_000,
                'km\u00b2': i/100,
                'in\u00b2': i*6_272_640,
                'ft\u00b2': i*107_639.1042,
                'ac': i*2.4711, 
            }
        },
        "Volume": {
            "cm^3": {
                'm^3': i/1_000_000,
                'ml': i,
                'l': i/1000
            },
            "m^3": {
                'cm^3': i*1_000_000,
                'ml': i*1_000_000,
                'l': i*1000 
            },
            "ml": {
                'cm^3': i,
                'm^3': i/1_000_000,
                'l': i/1000
            },
            "l": {
                'cm^3': i*1000,
                'm^3': i/1000,
                'ml': i*1000
            }
        },
        "Mass": {
            "mg": {
                'g': i/1000,
                'kg': i/1_000_000,
                'lbs': i/453_600,
                'oz': i/28350
            },
            "g": {
                'mg': i*1000,
                'kg': i/1000,
                'lbs': i/453.5924,
                'oz': i/28.3495
            },
            "kg": {
                'mg': i*1_000_000,
                'g': i*1000,
                'lbs': i*2.205,
                'oz': i*35.274
            },
            "lbs": {
                'mg': i*453600,
                'g': i*453.5924,
                'kg': i/2.205,
                'oz': i*16
            },
            "oz": {
                'mg': i*28350,
                'g': i*28.3495,
                'kg': i/35.274,
                'lbs': i/16
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
        number = units[field][input_unit][output_unit]
        # Format the output:
        #  - Larger number: separate it and limit the decimal places.
        #  - Smaller number: allow more decimal places.
        if number > 0.9999:
            output = float("{:.2f}".format(number)) # round to 2 decimal places
            output = '{:,}'.format(output)  # separation every 3 digits  
        else:
            output = "{:.4e}".format(number)  # 4 decimal places before scientific notation
        return output

    except KeyError: # if the same unit is selected on both sides
        return "Are you dumb?"
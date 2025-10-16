def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit -32 ) /1.8
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius*1.8)+32
    return fahrenheit


def kilometer_to_miles (kilometers):
    miles= (kilometers*0.621371)
    return miles

print (kilometer_to_miles(30))


def calculate_total(price, tax_rate=0.20, discount=0, default_tip=0.12):
    subtotal = price - discount
    tax = subtotal * tax_rate
    tip = default_tip * subtotal
    total = subtotal + tax+ tip
    return total

print(f"£{calculate_total(100,0.20,40,0.12):.2f}")
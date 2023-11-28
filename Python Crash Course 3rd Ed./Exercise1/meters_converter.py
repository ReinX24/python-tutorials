info = "This will convert meters to mm, cm, km, and feet"
print(info)
meter = int(input("Enter a length in METERS: "))
mm = meter * 1000
cm = meter * 100
km = meter / 1000
feet = meter * 3.28084

results = f"""
    [Meter Unit Conversion]
    {meter}m = {mm}mm
    {meter}m = {cm}cm
    {meter}m = {km}km
    {meter}m = {feet}ft"""

print(results)

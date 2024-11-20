import pandas as pd
property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4],
    'location': ['A', 'B', 'A', 'C'],
    'bedrooms': [3, 5, 4, 6],
    'area_sqft': [1500, 2000, 1800, 2500],
    'listing_price': [300000, 450000, 400000, 500000]
})
avg_price_per_location = property_data.groupby('location')['listing_price'].mean()
properties_4plus_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]
largest_area_property = property_data.loc[property_data['area_sqft'].idxmax()]
print("Average listing price per location:\n", avg_price_per_location)
print("Number of properties with more than 4 bedrooms:", properties_4plus_bedrooms)
print("Property with the largest area:\n", largest_area_property)

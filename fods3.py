import numpy as np
house_data = np.array([
    [3, 1500, 300000],
    [5, 2000, 450000],
    [4, 1800, 400000],
    [6, 2500, 500000]
]
                      )
houses_with_4plus_bedrooms = house_data[house_data[:, 0] > 4]
average_price_4plus_bedrooms = np.mean(houses_with_4plus_bedrooms[:, 2])
print("Average sale price of houses with more than 4 bedrooms:", average_price_4plus_bedrooms)

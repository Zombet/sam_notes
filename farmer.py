def sales_from_chemical_free_farming():
    tomato_land = 80 / 5
    potato_land = 80 / 5
    cabbage_land = 80 / 5
    sunflower_land = 80 / 5
    sugarcane_land = 80 / 5
    
    tomato_yield_1 = 0.30 * tomato_land * 10
    tomato_yield_2 = 0.70 * tomato_land * 12
    total_tomato_yield = tomato_yield_1 + tomato_yield_2
    tomato_sales = total_tomato_yield * 7 * 1000
    
    potato_yield = potato_land * 10
    potato_sales = potato_yield * 20 * 1000
    
    cabbage_yield = cabbage_land * 14
    cabbage_sales = cabbage_yield * 24 * 1000
    
    sunflower_yield = sunflower_land * 0.7
    sunflower_sales = sunflower_yield * 200 * 1000
    
    sugarcane_yield = sugarcane_land * 45
    sugarcane_sales = sugarcane_yield * 4000 * 1000
    
    total_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales
    return total_sales

def sales_after_11_months():
    tomato_land = 80 / 5
    potato_land = 80 / 5
    cabbage_land = 80 / 5
    sunflower_land = 80 / 5
    sugarcane_land = 80 / 5
    
    # 6 months for vegetables (tomatoes, potatoes, cabbage)
    tomato_yield_1 = 0.30 * tomato_land * 10
    tomato_yield_2 = 0.70 * tomato_land * 12
    total_tomato_yield = tomato_yield_1 + tomato_yield_2
    tomato_sales = total_tomato_yield * 7 * 1000
    
    potato_yield = potato_land * 10
    potato_sales = potato_yield * 20 * 1000
    
    cabbage_yield = cabbage_land * 14
    cabbage_sales = cabbage_yield * 24 * 1000
    
    # 10 months for sunflower (fully converted by 10th month)
    sunflower_yield = sunflower_land * 0.7
    sunflower_sales = sunflower_yield * 200 * 1000
    
    
    
    total_sales_chemical_free = tomato_sales + potato_sales + cabbage_sales + sunflower_sales
    return total_sales_chemical_free

overall_sales = sales_from_chemical_free_farming()
sales_11_months = sales_after_11_months()

print("Results: ")
print("Overall Sales from 80 acres of land:", overall_sales)
print("Sales Realization after 11 months from chemical-free farming:", sales_11_months)


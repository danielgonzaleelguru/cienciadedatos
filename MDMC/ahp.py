import ahpy

drink_comparisons  = {
('coffee', 'wine'): 9, 
('coffee', 'tea'): 5, 
('coffee', 'beer'): 2, 
('coffee', 'soda'): 1,
('coffee', 'milk'): 1,
('coffee', 'water'): 1 / 2,                         
('wine', 'tea'): 1 / 3, 
('wine', 'beer'): 1 / 9, 
('wine', 'soda'): 1 / 9,
('wine', 'milk'): 1 / 9, 
('wine', 'water'): 1 / 9,
('tea', 'beer'): 1 / 3, 
('tea', 'soda'): 1 / 4, 
('tea', 'milk'): 1 / 3,
('tea', 'water'): 1 / 9,
('beer', 'soda'): 1 / 2,
('beer', 'milk'): 1, 
('beer', 'water'): 1 / 3,
('soda', 'milk'): 2, 
('soda', 'water'): 1 / 2,
('milk', 'water'): 1 / 3}

drinks = ahpy.Compare(name='Drinks', comparisons=drink_comparisons, precision=3, random_index='saaty')


print(drinks.target_weights)

print(drinks.consistency_ratio)
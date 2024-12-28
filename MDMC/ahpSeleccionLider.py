import ahpy

experience_comparisons = {('Moll', 'Nell'): 1/4, ('Moll', 'Sue'): 4, ('Nell', 'Sue'): 9}
education_comparisons = {('Moll', 'Nell'): 3, ('Moll', 'Sue'): 1/5, ('Nell', 'Sue'): 1/7}
charisma_comparisons = {('Moll', 'Nell'): 5, ('Moll', 'Sue'): 9, ('Nell', 'Sue'): 4}
age_comparisons = {('Moll', 'Nell'): 1/3, ('Moll', 'Sue'): 5, ('Nell', 'Sue'): 9}


criteria_comparisons = {('Experience', 'Education'): 4, 
                        ('Experience', 'Charisma'): 3,
                        ('Experience', 'Age'): 7,
			            ('Education', 'Charisma'): 1/3, 
                        ('Education', 'Age'): 3,
			            ('Charisma', 'Age'): 5}

experience = ahpy.Compare('Experience', experience_comparisons, precision=3, random_index='saaty')
education = ahpy.Compare('Education', education_comparisons, precision=3, random_index='saaty')
charisma = ahpy.Compare('Charisma', charisma_comparisons, precision=3, random_index='saaty')
age = ahpy.Compare('Age', age_comparisons, precision=3, random_index='saaty')

criteria = ahpy.Compare('Criteria', criteria_comparisons, precision=3, random_index='saaty')

criteria.add_children([experience, education, charisma, age])

print("Pesos de las alternativas(Lideres)")
print(criteria.target_weights)

print("Pesos locales de la experiencia")
print(experience.local_weights)

print("Pesos globales del criterio educacion")
print(education.global_weights)

print("Consistencia de la experiencia")
print(experience.consistency_ratio)

print("Consistencia de la educación")
print(education.consistency_ratio)

print("Pesos de la experiencia  global")
print(experience.global_weight)

print("Pesos locales de la educacion")
print(education.local_weight)

print("Informe Final")
report = criteria.report(show=True)
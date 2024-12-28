from ahp_fuzzy_lib import AHP_FuzzyAHP

# Initialize the AHP_FuzzyAHP object
ahp_fuzzy = AHP_FuzzyAHP()

# Define a comparison matrix and evaluation matrix
comp_mat = [[1, 3, 5], [1/3, 1, 3], [1/5, 1/3, 1]]
eval_mat = [[0.8, 0.2, 0.5], [0.6, 0.7, 0.3]]

# Calculate weights and scores
weights_ahp, weights_fuzzy_ahp, final_scores = ahp_fuzzy.calculate_weights(comp_mat, eval_mat)

# Plot fuzzy triangular number distribution
ahp_fuzzy.plot_fuzzy_tfn()
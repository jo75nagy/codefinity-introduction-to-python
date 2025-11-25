# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]
shelf1_update_tuple = tuple(shelf1_update)

# Concatenate the new tuple with the existing tuple
shelf1_concat = shelf1 + shelf1_update_tuple

# Count and index
celery_count = shelf1_concat.count("celery")
celery_index = shelf1_concat.index("celery")

# Fixed prints to match exact expected output
print("updated shelf #1:" + str(shelf1_concat))
print("number of celery:" + str(celery_count))
print("celery index:" + str(celery_index))
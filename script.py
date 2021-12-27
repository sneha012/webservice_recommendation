with open("dataset_reviews.txt") as f:
    text = f.read()

sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
print sentences
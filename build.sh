set -o errexit

# Create the network
jupyter nbconvert --execute integrate.ipynb --inplace --ExecutePreprocessor.timeout=-1

# Create permuted networks
jupyter nbconvert --execute permute.ipynb --inplace --ExecutePreprocessor.timeout=-1

# Evaluate permution effectiveness
jupyter nbconvert --execute data/permuted/evaluate-permutations.ipynb --inplace --FilesWriter.build_directory=data/permuted --ExecutePreprocessor.timeout=-1

# Export to neo4j
jupyter nbconvert --execute neo4j-import.ipynb --inplace --ExecutePreprocessor.timeout=-1


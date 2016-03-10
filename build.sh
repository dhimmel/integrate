set -o errexit

# Create the network
jupyter nbconvert --execute integrate.ipynb --inplace --ExecutePreprocessor.timeout=-1

# Create permuted networks
jupyter nbconvert --execute permute.ipynb --inplace --ExecutePreprocessor.timeout=-1

# Export to neo4j
jupyter nbconvert --execute neo4j-import.ipynb --inplace --ExecutePreprocessor.timeout=-1


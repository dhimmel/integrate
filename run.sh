jupyter nbconvert --execute compile/AeG-expression.ipynb --inplace --FilesWriter.build_directory=compile --ExecutePreprocessor.timeout=-1
jupyter nbconvert --execute compile/DaG-association.ipynb --inplace --FilesWriter.build_directory=compile --ExecutePreprocessor.timeout=-1
jupyter nbconvert --execute compile/CbG-binding.ipynb --inplace --FilesWriter.build_directory=compile --ExecutePreprocessor.timeout=-1

#jupyter nbconvert --execute integrate.ipynb --inplace --ExecutePreprocessor.timeout=-1
#jupyter nbconvert --execute permute.ipynb --inplace --ExecutePreprocessor.timeout=-1
#jupyter nbconvert --execute neo4j-import.ipynb --inplace --ExecutePreprocessor.timeout=-1

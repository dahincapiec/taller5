import pandas as pd
from model.predict import make_prediction

sample_input_data = pd.read_csv("test\test-package.py")
result = make_prediction(input_data=sample_input_data)
print(result)
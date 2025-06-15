# Convert a HuggingFace model to Intel OpenVino
from transformers import BertTokenizer, BertModel

model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')

import openvino as ov
ov_model = ov.convert_model(model, example_input={**encoded_input})

###### Option 1: Save to OpenVINO IR:

# save model to OpenVINO IR for later use
ov.save_model(ov_model, 'openvino1.xml')

###### Option 2: Compile and infer with OpenVINO:

# compile model
compiled_model = ov.compile_model(ov_model)

# prepare input_data using HF tokenizer or your own tokenizer
# encoded_input is reused here for simplicity

# run inference
result = compiled_model({**encoded_input})
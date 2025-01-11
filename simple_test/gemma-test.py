from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import warnings
warnings.filterwarnings('ignore')

# Initialize tokenizer and model
model_name = "google/gemma-2b-it"  # Using the 2B instruction-tuned version
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.float16, 
    device_map="auto"
)

# Format the conversation (Gemma's specific format)
def format_message(messages):
    prompt = ""
    for message in messages:
        if message["role"] == "user":
            prompt += f"<start_of_turn>user\n{message['content']}<end_of_turn>\n<start_of_turn>model\n"
    return prompt

# Example conversation
messages = [
    {"role": "user", "content": "Who are you?"},
]

# Generate response
prompt = format_message(messages)
inputs = tokenizer(prompt, return_tensors="pt", padding=True)
# Move everything to the model's device
for key in inputs:
    inputs[key] = inputs[key].to(model.device)

outputs = model.generate(
    input_ids=inputs["input_ids"],
    attention_mask=inputs["attention_mask"],  # Explicitly provide attention mask
    max_length=512,
    temperature=0.7,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)

# Decode and print response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
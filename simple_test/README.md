The script will generate a response to "Who are you?". Modify the `messages` list to ask different questions! 💬

## ⚙️ Customization

You can modify:
- `temperature`: Controls randomness (0.0 to 1.0) 🎲
- `max_length`: Maximum length of generated response 📝
- `model_name`: Currently uses "google/gemma-2b-it" 🧠

## 🍎 Note for Mac Users

The script is optimized for Mac (including M1/M2/M3 chips) using MPS backend when available. No additional configuration needed! 

## 💡 Pro Tips
- Use `python` (not `python3`) when in your Conda environment
- Ignore the startup messages - they're just the model loading! 🔄
- Have fun chatting with your new AI friend! 🤗

## Conda Environment

```
conda create -n llama python=3.10
```

```
conda install -c huggingface transformers
```

```
conda install pytorch torchvision torchaudio -c pytorch
```

```
conda install -c conda-forge accelerate
```

## Troubleshooting

1. **ModuleNotFoundError**: Make sure all required packages are installed in your active environment
2. **CUDA/MPS errors**: The script is configured for Mac's MPS backend, but will fall back to CPU if needed
3. **Memory issues**: Try reducing `max_length` or using a smaller model

## Models

The script currently uses Google's Gemma 2B model (`google/gemma-2b-it`). Other options include:
- `microsoft/phi-2`
- `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
- `HuggingFaceH4/zephyr-7b-beta` (requires more RAM)

# Agentic AI Copilot

A local AI chatbot application powered by Ollama and Streamlit. Run a fully-featured AI assistant directly on your machine without relying on cloud services.

> **Current Version**: v1.0 - Simple chatbot with streaming responses and memory management
> 
> **Roadmap**: This project will eventually evolve into a full agentic framework with advanced reasoning, tool integration, and autonomous task execution capabilities.

## Features

- **Local LLM Support**: Uses Ollama for running language models locally
- **Streaming Responses**: Real-time streaming of AI responses for improved user experience
- **Chat Memory**: Maintains conversation history within a session
- **Configurable Models**: Easy model selection and parameter tuning via `config.yaml`
- **System Prompts**: Customizable system prompts to guide AI behavior
- **Web Interface**: Clean and intuitive Streamlit-based user interface

## Requirements

- Python 3.8+
- Ollama (installed and running locally)
- pip dependencies (see `requirements.txt`)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/vanadnarayane26/agentic-ai-copilot.git
cd agentic-ai-copilot
```

2. Create a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Ensure Ollama is installed and running on your system. If not, download from [ollama.ai](https://ollama.ai)

## Configuration

Edit `config.yaml` to customize the application:

```yaml
model: 'qwen2:7b'  # LLM model to use
generation:
  temperature: 0.7  # Creativity (0.0-1.0)
  top_p: 0.9        # Diversity (0.0-1.0)
  max_tokens: 512   # Maximum response length
```

Available models can be found at [Ollama's model library](https://ollama.ai/library). Make sure the model is pulled before running:
```bash
ollama pull qwen2:7b
```

## Usage

Run the Streamlit application:
```bash
streamlit run app/main.py
```

The application will open in your default browser at `http://localhost:8501`

## Project Structure

```
agentic-ai-copilot/
├── app/
│   ├── main.py              # Streamlit application entry point
│   ├── chat/
│   │   └── memory.py        # Session memory management
│   ├── llm/
│   │   └── ollama_client.py # Ollama API integration
│   ├── prompts/
│   │   └── system_prompt.txt # System prompt for AI behavior
│   └── utils/
├── config.yaml              # Configuration file
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Dependencies

- **streamlit**: Web UI framework
- **ollama**: Python client for Ollama
- **pyyaml**: YAML configuration parsing
- **python-dotenv**: Environment variable management

## License

See [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

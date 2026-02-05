# Translate API

A simple, offline neural machine translation API powered by [ArgosTranslate](https://www.argosmtengine.com/). Currently supports English to Portuguese translation with a REST API interface.

**Live Demo:** https://translate.tarsislima.com

## Features

- 🔄 **Offline Translation** - No internet required after initial model download
- ⚡ **Fast Inference** - Neural machine translation with low latency
- 🔗 **Simple REST API** - Easy to integrate with POST or GET requests
- 🐳 **Docker Ready** - Containerized for easy deployment
- 📦 **Self-Contained** - Models bundled on startup

## Quick Start

### Prerequisites
- Python 3.12+ or Docker

### Local Development

```bash
# Install dependencies
pip install flask argostranslate argostranslategui

# Run the server
python -m flask --app main run
```

The API will be available at `http://localhost:5000`

### Docker

```bash
# Build and run with Docker Compose
docker-compose up
```

## API Documentation

### Endpoints

#### Health Check
```bash
GET /
GET /api/v1
```
Returns: `"Translate API v1"`

#### Translate Text (POST - Recommended)
```bash
POST /api/v1/translate
Content-Type: application/json

{
  "text": "hello"
}
```

Response:
```json
{
  "status": "ok",
  "message": null,
  "data": {
    "text": "hello",
    "translated": "olá"
  }
}
```

#### Translate Text (GET)
```bash
GET /api/v1/translate?text=hello
```

Same response format as POST.

#### List Available Languages
```bash
POST /api/v1/languages
```

Response:
```json
{
  "status": "ok",
  "message": null,
  "data": {
    "languages": [...]
  }
}
```

### Example Requests

**Using curl (POST):**
```bash
curl -X POST "http://localhost:5000/api/v1/translate" \
  --header "Content-Type: application/json" \
  --data '{"text":"hello"}'
```

**Using curl (GET):**
```bash
curl "http://localhost:5000/api/v1/translate?text=hello"
```

**Using JavaScript/Fetch:**
```javascript
fetch('http://localhost:5000/api/v1/translate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ text: 'hello' })
})
.then(res => res.json())
.then(data => console.log(data.data.translated));
```

**Using Python:**
```python
import requests

response = requests.post('http://localhost:5000/api/v1/translate', 
                        json={'text': 'hello'})
print(response.json()['data']['translated'])
```

## Architecture

The application consists of:
- **Flask** - Lightweight web framework
- **ArgosTranslate** - Neural machine translation engine
- **Docker** - Containerization for consistent deployment

On startup, the application downloads and installs the English-Portuguese translation model. This one-time process takes ~30-60 seconds.

## Current Limitations

- **Single Language Pair** - English to Portuguese only. Supporting additional languages requires code modification.
- **No Authentication** - API is publicly accessible without credentials
- **No Rate Limiting** - No request throttling in place
- **Minimal Validation** - Basic error handling for malformed requests

## Extending the Project

### Add a New Language Pair

1. Modify the model download logic in `main.py` (lines 16-21)
2. Update the `translate()` function (line 12) to accept language parameters
3. Add new route handlers or extend existing ones

### Add Authentication

Consider adding:
- API key validation via headers
- Rate limiting middleware
- Request logging

### Production Deployment

For production use, consider:
- Nginx reverse proxy
- Gunicorn WSGI server
- Health check endpoints
- Request/response logging
- Error monitoring (Sentry, etc.)

## License

See LICENSE file for details.

## Contributing

Contributions welcome! Feel free to submit issues and pull requests.

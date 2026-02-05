# Copilot Instructions for translate-api

## Build & Run Commands

### Local Development
```bash
# Run the Flask API server
python -m flask --app main run
```

The server starts on `http://0.0.0.0:5000` by default.

### Docker
```bash
# Build and run with Docker Compose
docker-compose up

# Build only
docker build -t translate-api .
```

## Testing

Manual API testing is the primary approach:

```bash
# POST request (recommended)
curl -X POST "http://0.0.0.0:5000/api/v1/translate" \
  --header "Content-Type: application/json" \
  --data '{"text":"hello"}'

# GET request
curl "http://0.0.0.0:5000/api/v1/translate?text=hello"

# List installed languages
curl -X POST "http://0.0.0.0:5000/api/v1/languages" \
  --header "Content-Type: application/json"
```

## Architecture Overview

### Technology Stack
- **Framework**: Flask (Python web framework)
- **Translation Engine**: ArgosTranslate (offline neural machine translation)
- **Containerization**: Docker & Docker Compose

### Request/Response Format
All API responses follow a consistent JSON structure:
```json
{
  "status": "ok|error",
  "message": null|"error message",
  "data": {}
}
```

### Translation Flow
1. Application starts by downloading and installing the English-to-Portuguese translation model from ArgosTranslate
2. API endpoints accept text in POST or GET requests
3. Text is translated using the pre-installed model
4. Response includes both original and translated text

### API Endpoints
- `GET /` and `GET /api/v1` - Health check endpoints
- `GET /api/v1/translate?text=...` - GET-based translation (optional query param)
- `POST /api/v1/translate` - POST-based translation (takes JSON body with "text" field)
- `POST /api/v1/languages` - List installed translation languages

## Key Conventions

### Response Helpers
Two utility functions handle all API responses:
- `make_ok(data={})` - Creates success responses with the given data
- `make_error(error_message="")` - Creates error responses with message

Always use these functions to maintain response consistency. Both return JSON strings.

### Translation Handler
The `translate(text)` function is the single point for translation. Currently hardcoded to translate English → Portuguese. To support dynamic language pairs, modify this function and the model installation logic.

### Dependencies
Dependencies are only specified in the Dockerfile, not in a requirements.txt:
- `argostranslate` - Translation engine
- `argostranslategui` - GUI dependency (not used by API, but included)
- `flask` - Web framework

Install locally with: `pip install argostranslate argostranslategui flask`

## Important Notes

- ArgosTranslate models are downloaded and installed at application startup, which adds startup time (~30-60 seconds on first run)
- Currently configured for English-to-Portuguese translation only; extending to other language pairs requires changes to model installation and the `translate()` function
- No authentication, rate limiting, or input validation beyond Content-Type checking
- GET requests for translation don't validate that "text" parameter exists; will translate `None` if omitted

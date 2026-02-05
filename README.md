# [translate api](https://translate.tarsislima.com)

Just translate "any" language

## how to run

```bash
python -m flask --app main run
```

## how to request

```bash
curl -X POST "http://0.0.0.0:5000/api/v1/translate" \
  --header "Content-Type: application/json" \
  --data-raw '{"text":"hello"}' 
```

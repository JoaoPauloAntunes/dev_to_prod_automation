from uvicorn import run


if __name__ == "__main__":
    run(app='source.main:app', host='0.0.0.0', port=8001, reload=True, debug=False)
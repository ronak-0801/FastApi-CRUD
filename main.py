import uvicorn
# from src.app import app
  # Import the FastAPI instance from the module


if __name__ == "__main__":
    uvicorn.run("src.app:app", host="127.0.0.1", port=8000, log_level="info" , reload= True)
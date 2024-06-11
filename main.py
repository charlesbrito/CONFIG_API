from fastapi import FastAPI
from routes import posts, users

app = FastAPI()

app.include_router(users.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

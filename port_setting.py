import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define the FastAPI app
app = FastAPI()

# Get the port from the environment variable or default to 8000
port = int(os.getenv("PORT", 8000))

# Request body model for embedding input
class EmbeddingRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}

# Endpoint to generate embeddings
@app.post("/api/embeddings")
def generate_embedding(request: EmbeddingRequest):
    # Check if input text is valid
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    
    # Example embedding generation logic (replace with actual model logic)
    embedding = [0.1, 0.2, 0.3]  # Replace with real embedding logic
    
    # Return the embedding in the response
    return {"embedding": embedding}

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)

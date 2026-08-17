from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Backend API")

# simple in memory user counter
view_counter = {"views":0}

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str

@app.get("/api/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status":"healthy","service":"Lightsail through AWS"}

@app.get("/api/stats", status_code=status.HTTP_200_OK)
def get_stats():

    view_counter["views"] += 1

    return {"total_views":view_counter["views"]}

@app.post("/api/contact", status_code=status.HTTP_201_CREATED)
def submit_contact(userContact: ContactForm):

    # Check for any errors
    if not userContact.name.strip():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Name field cannot be empty")
    elif not userContact.email.strip():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email field cannot be empty")
    elif not userContact.message.strip():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Message field cannot be empty")

    
    return {"status":"success","message":f"Thank you {userContact.name} for your message!"}
from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()

@app.get("/iban/{iban}")
async def get_iban_response(iban: str = Path(...)):
    import http.client
    conn = http.client.HTTPSConnection("anyapi.io")
    conn.request("GET", f"/api/v1/iban?iban={iban}&apiKey=cl87eruibr8jll4d8t7m8qfksnp55vjgob395as8g68iuu8e397ln")
    res = conn.getresponse()
    data = res.read()
    return {"response": data.decode("utf-8")}
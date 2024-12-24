from fastapi import FastAPI
from MainModuleADM.Encryption.aes import i_decrypt, i_encrypt
import uvicorn


app = FastAPI()

@app.get("/")
def read_root():
    key = 'MGP@ssW0rd30182933123213'
    asd = 'apa iya'
    hasil = i_encrypt(key,asd)
    decrypt = i_decrypt(key,hasil)
    return f'{decrypt} : {hasil}'


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
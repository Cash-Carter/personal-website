import ssl
import uvicorn
import sys

development_mode: bool = "--dev" in sys.argv
if development_mode:
    print("Development mode enabled")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=443, reload=development_mode,
                ssl_version=ssl.PROTOCOL_TLS_SERVER,
                ssl_keyfile="private_key",
                ssl_certfile="origin_certificate")

import ssl
import uvicorn
import sys

reload: bool = "--reload" in sys.argv
if reload: print("Reload enabled")
development_mode: bool = "--dev" in sys.argv
if development_mode: print("Development mode enabled")

if __name__ == "__main__":
    if development_mode:
        uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=reload)
    else:
        uvicorn.run("app:app", host="0.0.0.0", port=443, reload=reload,
                    ssl_version=ssl.PROTOCOL_TLS_SERVER,
                    ssl_keyfile="private_key",
                    ssl_certfile="origin_certificate")

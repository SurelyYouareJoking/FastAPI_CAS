#!/usr/bin/env python3
# coding: utf-8
"""
:author: jj
:brief: FastAPI cas
"""
from sys import argv as rd
from app import app
from config import DEBUG
import uvicorn


def main():
    try:
        port = int(rd[1])
    except:
        port = 8000
    finally:
        uvicorn.run(app=app, host='127.0.0.1', port=port, debug=DEBUG)


if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""__init__ methodfor storage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

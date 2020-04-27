# !/usr/bin/python
# coding=utf-8
import re

symbols = {
    "implementation": "🤯",
    "practicality": '🤩',
    "Although": "🥺",
    "is better than": "✅",
    "to explain": '😘',
    "silen": '😅',
    "the": "🍬",
    "never": "🍭",
    "one": "🎯",
    "compl": "🍩",
    "plicit": "❌"   
}



def compress(content):
    compressed_content = content
    for x in symbols:
        compressed_local = compressed_content.replace(x, symbols[x])
        compressed_content = compressed_local

    return compressed_content
    
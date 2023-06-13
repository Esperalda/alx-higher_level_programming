#!/usr/bin/python3
def multiple_returns(sentences):
    if len(sentences) == 0:
        return (0, None)
    else:
        return (len(sentences), sentences[0])

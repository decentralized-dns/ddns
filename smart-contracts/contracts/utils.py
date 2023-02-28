def sign_msg(msg: str, sk: str) -> bytes:
    """utility function for signing arbitrary data"""
    pk: list[int] = list(base64.b64decode(sk))
    return SigningKey(bytes(pk[:32])).sign(msg.encode()).signature

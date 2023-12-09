import logging

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from cryptography.exceptions import InvalidSignature
from fastapi import (
    HTTPException,
    Header,
    Request,
)


class DiscordSignedRequest:
    def __init__(self, public_key):
        self.public_key = public_key

    async def sigverify(self, signature: str, timestamp: str, body: str):
        verify_key = Ed25519PublicKey.from_public_bytes(bytes.fromhex(self.public_key))
        verify_key.verify(bytes.fromhex(signature), timestamp.encode() + body)

    async def signed_request(
        self,
        request: Request,
        x_signature_ed25519: str = Header(...),
        x_signature_timestamp: str = Header(...),
    ):
        body = await request.body()

        try:
            await self.sigverify(
                x_signature_ed25519, x_signature_timestamp, body
            )
        except Exception as e:
            logger = logging.getLogger("uvicorn.error")
            logger.error(f"Signature failure exception: {e.__repr__()}")
            raise HTTPException(status_code=401, detail="Invalid signature")

        return True


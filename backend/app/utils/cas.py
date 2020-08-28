from cas import CASClient


class CAS:
    client: CASClient = CASClient(
        version=3,
        service_url="http://127.0.0.1:8000/core/login?next=%2F",
        server_url="http://218.95.164.199:4065/cas/"
    )


cas_client = CAS()


async def get_cas() -> CAS:
    return cas_client.client

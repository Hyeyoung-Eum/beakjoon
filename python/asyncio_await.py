import asyncio

async def add(a, b):
    print('add: {0} + {1}'.format(a, b))
    await asyncio.sleep(1.0)
    return a + b

async def print_add(a, b):
    result = await add(a, b) #코루틴 함수를 await를 사용하여 실행하고, 반환값을 변수에 저장
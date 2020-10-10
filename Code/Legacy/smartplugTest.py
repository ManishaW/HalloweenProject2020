import asyncio
from kasa import SmartPlug
from kasa import Discover
devices = asyncio.run(Discover.discover())
# for addr, dev in devices.items():
#     asyncio.run(dev.update())
#     print(f"{addr} >> {dev}")

async def main():
    p = SmartPlug("192.168.1.29")
    await p.turn_on()
    # await p.update()
    # print(p.alias)



if __name__ == "__main__":
    asyncio.run(main())
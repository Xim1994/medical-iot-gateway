from bleak import BleakScanner

async def run():
    scanner = BleakScanner()
    devices = await scanner.discover()
    for device in devices:
        print(device)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())

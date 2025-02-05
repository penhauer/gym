import asyncio
import websockets

async def receive_stream():
    try:
        async with websockets.connect("ws://129.97.168.82:8765") as websocket:
            while True:
                packet_data_hex = await websocket.recv()
                packet_data = bytes.fromhex(packet_data_hex)
                print(f"Received packet: {packet_data}")
    except websockets.ConnectionClosed:
        print("Connection closed by server.")
    except Exception as e:
        print(f"Client error: {e}")

asyncio.run(receive_stream())

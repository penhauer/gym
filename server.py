import asyncio
import websockets
import os

def get_next_packet():
    return os.urandom(32)

async def stream_packets(websocket):
    try:
        while True:
            packet_data = get_next_packet()
            await websocket.send(packet_data.hex())
            await asyncio.sleep(1)
    except websockets.ConnectionClosed:
        print("Client disconnected.")
    except Exception as e:
        print(f"Server error: {e}")
        await websocket.close()

async def main():
    server = await websockets.serve(stream_packets, "0.0.0.0", 8765)
    print("WebSocket server started on ws://0.0.0.0:8765")
    await server.wait_closed()

asyncio.run(main())

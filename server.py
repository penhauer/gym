import asyncio
import websockets
import time
import csv
import os

file_name = "./csv_packet_trace/embb.csv"

async def stream_messages(websocket, path):
    with open(file_name, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        row1 = next(datareader)
        row2 = next(datareader)
        print("waiting for the client!")
        packet = await websocket.recv()
        start_time = time.time()

        for r_ix, row in enumerate(datareader):
            if r_ix % 100 == 0:
                print('Server progress ' + str(r_ix)) # +'/'+str(rowcount))
            if row[3] == '172.30.1.250':
                data_size = int(row[6])-70
                Sdata = os.urandom(data_size)
                wait_time = float(row[2]) - (time.time() - start_time)
                if wait_time > 0:
                    await asyncio.sleep(wait_time)
                await websocket.send(Sdata)
                print("data_size sent", data_size)

start_server = websockets.serve(stream_messages, "0.0.0.0", 6789)

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
print("Server running at ws://localhost:6789")
loop.run_forever()

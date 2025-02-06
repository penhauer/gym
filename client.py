import asyncio
import websockets
import time
import csv
import os

uri = "ws://localhost:6789"
file_name = "./csv_packet_trace/embb.csv"

async def receive_messages():
    with open(file_name, 'r') as csvfile:
        async with websockets.connect(uri) as websocket:
            datareader = csv.reader(csvfile)
            row1 = next(datareader)
            row2 = next(datareader)
            
            if row2[3] != '172.30.1.1':
                print('Server starts!')
                await websocket.send("Start!")
                packet = await websocket.recv()
                if packet:
                    start_time = time.time()
                    print("Starting experiment")
            else:
                print('Client starts')
                data_size = int(row2[6])-70
                start_time = time.time()
                Sdata = os.urandom(data_size)
                await websocket.send(Sdata)

            for r_ix, row in enumerate(datareader):
                if r_ix % 100 == 0:
                    print('Client Progress '+str(r_ix)) # +'/'+str(rowcount))
                if row[3] == '172.30.1.1':
                    data_size = int(row[6])-70
                    Sdata = os.urandom(data_size)
                    wait_time = float(row[2]) - (time.time() - start_time)
                    if wait_time > 0:
                        await asyncio.sleep(wait_time)
                    await websocket.send(Sdata)
                    print("data_size sent", data_size)

loop = asyncio.get_event_loop()
loop.run_until_complete(receive_messages())

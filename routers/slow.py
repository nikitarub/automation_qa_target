from fastapi import APIRouter, BackgroundTasks
import time
import asyncio
import concurrent.futures
import random

router = APIRouter(
    prefix="/slow",
    tags=["slow"],
    responses={404: {"description": "Not found"}},
)

N_ARRAY = 1_00

def metric_send(metric, metric_time=3):  # менять на async def можно
    # эту часть менять нельзя vvvvvvv
    time.sleep(metric_time)
    print(f"[{time.time()}] Sent metrics: {metric}")
    # эту часть менять нельзя ^^^^^^^


def process_something_long(data, log=False):  # менять на async def можно
    # эту часть менять нельзя vvvvvvv
    start = time.time()
    arr = [i for i in range(N_ARRAY * data['time'])]
    random_array = []
    for a in arr:
        for b in arr:
            _ = random.random() * random.random()
            if log:
                random_array.append(str(_))
    if log:
        with open("./random.log", "w") as f:
            f.write("\n".join(random_array))
    end = time.time()
    print(f"[{time.time()}] Done processing: {data['input']} in {end - start} seconds")
    return "result " + data['input']
    # эту часть менять нельзя ^^^^^^^


@router.get("/")
def slow(
    log: bool,
    background_tasks: BackgroundTasks):  # менять на async def можно
    start = time.time()
    data = [
        {
            'time': 3,
            'input': "3 sec."
        },
        {
            'time': 4,
            'input': "4 sec."
        },
        {
            'time': 5,
            'input': "5 sec."
        }
    ]
    # сделать обработку data с помощью process_something_long
    # отправить метрику `metric_send("Done processing all")`
    # задача: сделать обработку всех элементов из data и отправку метрик как можно быстрее
    # можно менять metric_send и process_something_long на ассинхронные по своему усмотрению
    # разрешается использование корутин и тредов, например: concurrent.futures.ThreadPoolExecutor
    result = []  # ["result 3 sec.", "result 4 sec.", "result 5 sec."]

    for d in data:
        result.append(process_something_long(d, log))

    # работу со вычислением времени трогать нельзя – время работы ручки должно быть близко к 5 секундам 
    end = time.time()
    print("Time elapsed: ", end - start)
    return result


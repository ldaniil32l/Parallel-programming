import multiprocessing as mp


def worker(p, is_odd):
    if is_odd:
        print(f"Имя процесса {mp.current_process().name}, получено число - {p.recv()}")
    else:
        print(f"Имя процесса {mp.current_process().name}, похоже, что он четный...")



if __name__ == "__main__":
    number = 10
    jobs = []
    procs = 10
    main_proc = mp.current_process()
    for i in range(procs):
        main_proc, p = mp.Pipe()
        if (i + 1) % 2:
            prc = mp.Process(target=worker, args=(p, 1))
        else:
            prc = mp.Process(target=worker, args=(p, 0))
        main_proc.send(number)
        prc.start()
        jobs.append(prc)
    for j in jobs:
        j.join()

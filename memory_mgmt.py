import gc
import micropython

micropython.alloc_emergency_exception_buf(100)

def long_running_task():
    buf = bytearray(1000)
    # Do memory-intensive operations
    del buf

def main_task():
    gc.collect()  # Run garbage collection to free up memory
    long_running_task()
    gc.collect()

main_task()

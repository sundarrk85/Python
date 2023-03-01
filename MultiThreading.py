# to execute the functions simulataneously when other func gets executed
import threading 
import time


def update_db():
    print("updating db...")
    time.sleep(5)               # introducing 5 secs delay
    print("updated db")

def display_num(n):
    for i in range(1,n+1):
        print(i)

# calling functions
# update_db()
a = threading.Thread(target=update_db)  # creates a new thread for update_db
a.start()                               # execution of thread 'a'
display_num(50)



# to see how many threads are running
print(f"The no of active threads running is {threading.active_count()}")

# to see what thread is running
print(f"\nThe name of the thread running is {threading.enumerate()}")
# O/P The name of the thread running is [<_MainThread(MainThread, started 12772)>]

# to print bye after all threads got executed 
a.join()
print("bye")



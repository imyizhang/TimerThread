# TimerThread

TimerThread is

* A lightweight task scheduling timer
* written in [Python (3.7+) Standard Library](https://docs.python.org/3.7/library/)



TimerThread supports to

* schedule task execution after a given delay
* schedule recurring task execution
* run in the background
* use `@task` decorator to define task



## Quickstart

Define your function, `now(cost)` as an example:

```python
import time

def now(cost=1):
    time.sleep(cost)
    print( time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime()) )
```

Create a TimerThread scheduler and start it:

```python
import timerthread

timer = timerthread.Scheduler('recur', 3, now, args=(1,))
timer.start()
```

Shutdown the scheduler:

```python
timer.cancel()
```



### Play with the `@task` decorator

Use `@task` decorator to define your function, then schedule it and start the scheduler, `now(cost)` as an example:

```python
import time
import timerthread

@timerthread.task('recur', 3)
def now(cost=1):
    time.sleep(cost)
    print( time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime()) )

timer = now.sched(cost=1)
timer.start()
```

When you'd like to cancel the recurring execution, shutdown the scheduler as usual:

```python
timer.cancel()
```



### Install TimerThread

```bash
$ pip install timerthread
```



## Documentation

### `Scheduler`

```python
class timerthread.Scheduler(trigger, interval, fn, args=(), kwargs={})
```

`trigger` must be `'delay'` or `'recur'`.

* `stopped`

  The scheduler is stopped or not, `True` (default) or `False`.

* `result`

  The execution result, `{}` as default.

* `start()`

  Let scheduler start executing your function as scheduled in the background.

* `cancel()`

  Shutdown the scheduler.



### `task`

```python
class timerthread.task(trigger, interval)
```

`trigger` must be `'delay'` or `'recur'`.

* Use `@task` decorator to define your function, then schedule it and start the scheduler:

  ```python
  @timerthread.task(trigger, interval)
  def fn(args, kwargs):
      pass
    
  timer = fn.sched(*args, **kwargs)
  ```

  `fn.sched(*args, **kwargs)` returns `timerthread.Scheduler` instance.



## Related Projects

* [`threading.Timer`](https://github.com/python/cpython/blob/3.7/Lib/threading.py#L1153) ([Timer Objects](https://docs.python.org/3.7/library/threading.html?highlight=thread#timer-objects))


# HoloPy
A python file that can receive streaming information from the official hololive website, https://schedule.hololive.tv/.

## Example
```python
import holopy

schedule = holopy.connect()

for date in schedule:
    print(date)
    for info in schedule[date]:
        print(info.getInfo())
    print()
```

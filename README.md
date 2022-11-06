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

## Usage
### old_connect() and old_beautify()
Get information except any thumbnail and url, but faster than normal connect function

### connect()
Get whole information including thumbnails and urls, but slower than old style.

# hovsearch

hovsearch is a Python Module to download and search youtube videos.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install hovsearch.

```bash
pip install hovsearch
```

## Usage

```python
import hovsearch
youtube = hovsearch.youtube_search()

print(youtube.search(search="Never gonna give you up"))
#returns first url result default
```

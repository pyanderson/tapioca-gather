# Tapioca Gather

## Installation
```
pip install tapioca-gather
```

## Documentation

[Gather HTTP API Documentation](https://gathertown.notion.site/Gather-HTTP-API-3bbf6c59325f40aca7ef5ce14c677444)

### Auth
Generate your `API_KEY` here: [https://gather.town/apiKeys](https://gather.town/apiKeys)

### Usage
NOTE: forward slashes in `space_id` need to be replaced by backslashes (e.g. `dkj63wrer8/spaceName` becomes `dkj63wrer8\spaceName`)

``` python
from tapioca_gather import Gather

api = Gather(api_key=API_KEY)
space_id = 'dkj63wrer8\\spaceName'

assignment = api.game_server_assignment(space_id=space_id).get()
print(assignment().data)
wss://engine-aaaaa.aaa0-a.prod.do.gather.town:443/

space = api.space(space_id=space_id).get()
print(space().data['level'])
1
```



No more documentation needed.

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html)
- Explore this package using iPython
- Have fun!

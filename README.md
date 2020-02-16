# University notes
Notes from my course at Durham University

### Changing to input rather than usepackage
To change all cases of usepackage to input, I used the following command, it may be useful in the future
```
find . -type f -name "*.tex" -exec sed -i 's/usepackage{\(.*format\)}/input{\1}/' {} +

```
### Replacing verb with mintinline
In the search section put
```regex
verb\!([^\!]+)\!
```
and in the replace section put
```regex
mintinline{c}{\1}
```

### Windows compatibility
These notes can't be cloned into windows due to illegal characters in file names. At the moment I'm not going to fix this, but I plan to in the future.


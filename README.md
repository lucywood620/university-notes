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
These notes should be able to be cloned into windows, but I may put an illegal character in by accident, raise an issue if you find one


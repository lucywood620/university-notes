# University notes
Notes from my course at Durham University

### Changing to input rather than usepackage
To change all cases of usepackage to input, I used the following command, it may be useful in the future
```
find . -type f -name "*.tex" -exec sed -i 's/usepackage{\(.*format\)}/input{\1}/' {} +

```

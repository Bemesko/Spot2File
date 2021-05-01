# Command-Line Interface Planning

This file's purpose is to help me plan the command-line interface
before I actually go and implement it. It will also be useful in
the event of me not knowing what to do next.

# Expected Functions

## Input playlist link
```
main.py -l [playlist-link] [playlist2-link] ...
```

### Input file with playlist links?

```
main.py --input-file [path-to-file]
```

## Specify which directory to download the videos in

```
main.py -o [directory-path]
```

## Set the desired format to get the videos in

```
main.py -f [format]
```

## Set max downloaded songs per playlist
```
main.py -m [max-songs]
```

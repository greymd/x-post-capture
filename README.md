# x-post-capture

### Build

```bash
$ docker build -t x-post-capture .
```

### Run

```bash
$ docker run -it -v $PWD:/app --rm x-post-capture https://x.com/username/status/123456789
$ ls
screenshot_123456789.png    # screenshot will be created on the current directory.
text_123456789.png          # text will be created on the current directory.
```

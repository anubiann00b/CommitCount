# CommitCount

Simple python script to count all your commits for projects hosted on GitHub.

#### Setup:

```
pip install -r requirements.txt
```

#### Usage:

```
python commitcount.py username password
```

You can also supply your username and password through the CREDS file, with each on a seperate line. For example:

```
anubiann00b
hunter2
```

And then call it without any parameters:

```
python commitcount.py
```

#### Output:

```
> python commitcount.py

anubiann00b/2048                                  0        0
anubiann00b/acr                                   0        0
anubiann00b/adventure-quest                       0        0
anubiann00b/agar.io-key-movement                  0        0
anubiann00b/AlexanderBot                          6        6
anubiann00b/algorithmic-complexity-demo           0        6
anubiann00b/Alias                                 8       14
anubiann00b/android_packages_apps_Torch           0       14
anubiann00b/AnimeDownloader                       32      46
anubiann00b/AnimeDownloaderWeb                    10      56
anubiann00b/anubiann00b.github.io                 2       58
anubiann00b/APCS-Review                           4       62
anubiann00b/Aphrodite                             3       65
anubiann00b/AsciiPanel                            0       65
anubiann00b/Bang                                  0       65
anubiann00b/Berserker                             61     126
...

Total Commits: 1337
```

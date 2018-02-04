from distutils.core import setup

setup(
    name = 'mr-streams',
    packages = ['mr_streams'],  # this must be the same as the name above
    version = 0.01,
    description= "A wrapper that makes chaining iterable-comprehensions simpler",
    author = "u/caffeine_potent",
    author_email= "caffeine-potent@protonmail.com",
    url = 'https://github.com/caffeine-potent/Mr-Streams',
    download_url= 'https://github.com/caffeine-potent/Mr-Streams/archive/0.03.tar.gz',
    keywords = ['map-reduce', 'list-comprehension', 'map', 'reduce', 'stream'],  # arbitrary keywords
    classifiers= []
)
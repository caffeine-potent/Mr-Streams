## Map Reduce Filter Chain

If you're familiar with the concept of map-reduce or Apache spark, then you may also be familiar with the workings of this library.  
  
This is a sparse and deadpan writeup of what you should expect from this library.  
  
Functions included:  

- `map(func)` - standard map function. Applies function in the argument to all values in the stream.  
- `flatmap(func)` - takes a stream of iterables and emits individual values in those streams.    
- `filter(func)` - boolean filter. Takes a function as a parameter. This function will be called with each element of the stream. If this function returns `True` when evaluating an object in the stream, then that object is re-emited to the stream. 
- `take(num)` - a rate limiter. `.take(5)` will only emit the first 5 elements of the stream. 
- `tap(func)` - a passive function. Takes a single function as a parameter and passes iteratively passes objects from the stream to it. 

Consumers: 

- `print_stream()`- iterates through all values of the stream and prints them. 

## Usage

Listed below are some over complicated solutions to trivial problems.  

**Import:**  

	from pstream.pstream import pStream as _

**Add Two**:  

	def add_two(x):
		return x + 2

	stream = _([1,2,3,4,5])

	stream.map(add_two)

    stream.print_stream()


>[3, 4, 5, 6, 7]

**Every other even number between 0 and 100**  
  
		
	def is_odd(x):
		return x%2 != 0

	def times_two(x):
		return 2*x

	stream = _(range(100)) \
	    .filter(is_odd)\
	    .take(25)\
	    .map(times_two)

	stream.print_stream()


> [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98]


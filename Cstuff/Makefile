FLAGS = -g -Wall -std=gnu99




all: max_heap
	./max_heap

max_heap: helper.o max_heap.o
	gcc ${FLAGS} -o $@ $^


# the stuff below is for my sorting algorithm stuff
test: test_sort
	./test_sort

test_sort: test_sort.o radix_sort.o helper.o
	gcc ${FLAGS} -o $@ $^

%.o: %.c helper.h
	gcc ${FLAGS} -c $<

clean:
	rm -f *.o test_sort max_heap

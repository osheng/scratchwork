FLAGS = -g -Wall -std=gnu99

all: test

test: test_sort
	./test_sort

test_sort: test_sort.o quick_sort.o helper.o
	gcc ${FLAGS} -o $@ $^

%.o: %.c helper.h
	gcc ${FLAGS} -c $<

clean:
	rm -f *.o test_sort

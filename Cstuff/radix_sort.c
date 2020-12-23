#include "radix_sort.h"
#include "helper.h"
#include <stdlib.h>
/*
  Bucket sort an array of unsigned ints
*/
void radix_sort(unsigned int *arr, unsigned int length) {
  paritition(arr, 3, 0, length);
}

/*
  Copy the contents of arr to designated sectino of buf.
  Assume buf is long enough to handle this
  and that arr has enough values to fill them
*/
static void copy_arr(unsigned int *buf, unsigned int *arr, unsigned int from,
                     unsigned int to) {
  for (unsigned int i = from; i < to; i++) {
    *(buf + i) = *(arr + i - from);
  }
}

static void paritition(unsigned int *arr, int on, unsigned int from,
                       unsigned int to) {
  if (on >= 0) {
    unsigned int *zeros =
        malloc_or_exit((to - from) * sizeof(unsigned int), __FILE__, __LINE__);
    unsigned int *ones =
        malloc_or_exit((to - from) * sizeof(unsigned int), __FILE__, __LINE__);
    unsigned int zero_count = 0;
    unsigned int one_count = 0;
    unsigned int pivot = 1 << on;
    for (unsigned int num = from; num < to; num++) {
      if (*(arr + num) & pivot) {
        *(ones + one_count) = *(arr + num);
        one_count++;
      } else {
        *(zeros + zero_count) = *(arr + num);
        zero_count++;
      }
    }
    copy_arr(arr, zeros, from, from + zero_count);
    copy_arr(arr, ones, from + zero_count, to);
    free(zeros);
    free(ones);
    paritition(arr, on - 1, from, from + zero_count);
    paritition(arr, on - 1, from + zero_count, to);
  }
}

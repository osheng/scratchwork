#include "helper.h"
#include "quick_sort.h"
#include "radix_sort.h"
#include <stdlib.h>

#define TEST_SIZE 15
int main(int argc, char const *argv[]) {
  // setup array of 15 random numbers from 0 to 10, and display it
  srand(1);
  int *arr = malloc_or_exit(TEST_SIZE * sizeof(int), __FILE__, __LINE__);
  for (int i = 0; i < TEST_SIZE; i++) {
    arr[i] = rand() % 10;
  }
  print_arr(arr, TEST_SIZE);

  // sort the array
  // quick_sort(arr, 0, TEST_SIZE - 1);
  radix_sort(arr, TEST_SIZE);
  print_arr(arr, TEST_SIZE);
  free(arr);

  return 0;
}

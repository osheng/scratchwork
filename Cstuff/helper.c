#include "helper.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*an error checked version of malloc*/
void *malloc_or_exit(size_t size, char *file_name, int line_number) {
  void *p = malloc(size);
  if (p == NULL) {
    char buffer[LINE];
    sprintf(buffer, "malloc_or_exit: %s: %d\n", file_name, line_number);
    perror(buffer);
    exit(1);
  }
  return p;
}

/*print an array to standard output*/
void print_arr(int *arr, int length) {
  printf("[ ");
  for (int i = 0; i < length - 2; i++) {
    printf("%d, ", arr[i]);
  }
  printf("%d]\n", arr[length - 1]);
}

void print_helper(char *file_name, int line) {
  printf("I called a helper function in %s on line %d\n", file_name, line);
}

/*
Implement a priority queue by writing
insert(PQ, x, priority): here priority is given by the value of x
find_max(PQ)
extract_max()
is_pq(PQ)
*/
#include "helper.h"
#include <stdlib.h>

/*Return 1 if pq is a priority queue and 0 otherwise,
assume the first element in pq is its size*/
int is_pq(int *pq){
  int size = pq[0];
  int i = 1;
  while (i <= size){
    if (2 * i <= size && pq[i] < pq[2 * i]){
      return 0;
    }
    if (2 * i + 1 <= size && pq[i] < pq[2 * i + 1]){
      return 0;
    }
    i++;
  }
  return 1;
}

int find_max(int *pq){
  if (pq[0] > 0){return pq[1];}
  return 0;
}

void swap(int **pq, int a, int b){
  int temp = (*pq)[a];
  (*pq)[a] = (*pq)[b];
  (*pq)[b] = temp;
}

void insert(int **pq, int value){
  // insert
  (**pq)++;
  (*pq)[**pq] = value;
  // bubble up
  int i = **pq;
  while (i > 1 && (*pq)[i/2] < (*pq)[i]){
    swap(pq, i/2, i);
    i = i/2;
  }
}

int extract_max(int **pq){
  // assume pq is not empty
  //save the max to return later
  int m = (*pq)[1];
  // set last element to be the first
  (*pq)[1] = (*pq)[**pq];
  //decrement size
  **pq = **pq - 1 ;
  // bubble down
  int size = **pq;
  int i = 1;
  while( i < size){
    if (2*i +1 <= size && (*pq)[2*i +1] >= (*pq)[2*i] && (*pq)[i] < (*pq)[2 * i + 1]){
      swap(pq, i, 2*i+1);
      i = 2*i+1;
    }
    else if (2*i <= size && (*pq)[i] < (*pq)[2 * i]){
      swap(pq, i, 2*i);
      i = 2 * i;

    }
    else {i = size+1;}
  }
  return m;
}

int main(int argc, char const *argv[]){
  int * pq = malloc_or_exit(sizeof(int) * 256, __FILE__, __LINE__);
  pq[0] = 0;
  insert(&pq, 8);
  insert(&pq, 5);
  insert(&pq, 10);
  insert(&pq, 3);
  print_arr(pq, pq[0]+1); // print the size and the heap
  printf("is_pq(pq) returns %d\n", is_pq(pq));
  printf("find_max(pq) returns %d\n", find_max(pq));
  insert(&pq, 16);
  printf("extract_max(&pq) returns %d\n", extract_max(&pq));
  print_arr(pq, pq[0]+1); // print the size and the heap
  printf("extract_max(&pq) returns %d\n", extract_max(&pq));
  print_arr(pq, pq[0]+1); // print the size and the heap
  insert(&pq, 7);
  print_arr(pq, pq[0]+1); // print the size and the heap


  free(pq);
}

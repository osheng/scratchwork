/*
  A basic implementation of quick sort
  To sort an entire array, call quick_sort with low=0 and high=arr.lenghth - 1
*/
static int partition(int *arr, int low, int high) {
  int pivot = arr[(low + high) / 2];
  while (low <= high) {
    while (arr[low] < pivot)
      low++;
    while (arr[high] > pivot)
      high--;
    if (low <= high) { // swap
      int temp = arr[high];
      arr[high] = arr[low];
      arr[low] = temp;
      low++;
      high--;
    }
  }
  //  print_helper(__FILE__, __LINE__)
  return low;
}

void quick_sort(int *arr, int low, int high) {
  int index = partition(arr, low, high);
  if (low < index - 1) {
    quick_sort(arr, low, index - 1);
  }
  if (index < high) {
    quick_sort(arr, index, high);
  }
}

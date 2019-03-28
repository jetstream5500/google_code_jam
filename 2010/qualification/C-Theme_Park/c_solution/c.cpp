#include <iostream>
#include <math.h>

using namespace std;

int sum(int a[], int size) {
  int sum = 0;
  for (int i = 0; i<size; i++) {
    sum += a[i];
  }
  return sum;
}

void compute_memo(int memo_totals[], int memo_counts[], int k, int groups[], int n) {
  int total = 0;
  int base_index = 0;
  int index = 0;
  while (base_index < n) {
    if (total + groups[index] > k) {
      memo_totals[base_index] = total;
      memo_counts[base_index] = (index-base_index+n) % n;
      total -= groups[base_index];
      base_index++;
    } else if (total == sum(groups, n)) {
      memo_totals[base_index] = total;
      memo_counts[base_index] = n;
      total -= groups[base_index];
      base_index++;
    } else {
      total += groups[index];
      index = (index + 1) % n;
    }
  }
}

void print_array(int a[], int size) {
  for (int i = 0; i<size; i++) {
    cout << a[i] << " ";
  }
  cout << endl;
}

int main() {
  int test_cases;
  cin >> test_cases;
  for (int i = 0; i<test_cases; i++) {
    int r, k, n;
    cin >> r >> k >> n;
    //cout << "------------------" << endl;
    //cout << r << " " << k << " " << n << endl;

    int * groups = new int[n];
    for (int j = 0; j<n; j++){
      cin >> groups[j];
    }
    //print_array(groups, n);

    int * memo_totals = new int[n];
    int * memo_counts = new int[n];

    compute_memo(memo_totals, memo_counts, k, groups, n);
    //print_array(memo_totals, n);
    //print_array(memo_counts, n);

    int index = 0;
    long euros = 0;
    int ride = 1;
    while (ride <= r) {
      euros += memo_totals[index];
      index = (index+memo_counts[index]) % n;
      ride++;
    }

    cout << "Case #" << (i+1) << ": " << euros << endl;

    delete[] groups;
    delete[] memo_totals;
    delete[] memo_counts;
  }
}

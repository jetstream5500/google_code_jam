#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

double dist(double x, double y) {
  return sqrt(x*x + y*y);
}

bool inside_ring(double big_r, double x, double y) {
  return (dist(x,y) <= big_r);
}

bool intersects_ring(double f, double big_r, double t, double x, double y) {
  return (dist(x,y)+f >= big_r-t);
}

bool intersects_strings(double f, double r, double g, double x, double y) {
  double vertical_string = round(x/(g+2*r)) * (g+2*r);
  if (abs(x-vertical_string) <= r+f) {
    return true;
  }

  double horizontal_string = round(y/(g+2*r)) * (g+2*r);
  if (abs(y-horizontal_string) <= r+f) {
    return true;
  }

  return false;
}

int main() {
  srand(time(NULL));

  int num_test_cases;
  cin >> num_test_cases;
  for (int n = 0; n<num_test_cases; n++) {
    double f, big_r, t, r, g;
    cin >> f >> big_r >> t >> r >> g;

    double hits = 0.0;
    double misses = 0.0;
    int count = 0;
    int size = 100000000;

    while (count < size) {
      double x = ((double) rand() / (RAND_MAX))*(big_r+t);
      double y = ((double) rand() / (RAND_MAX))*(big_r+t);
      if (inside_ring(big_r, x, y)) {
        if (intersects_ring(f, big_r, t, x, y) || intersects_strings(f, r, g, x, y)) {
          hits+=1;
        } else {
          misses+=1;
        }
        count+=1;
      }
    }
    cout << (hits/(hits+misses)) << endl;
  }
}

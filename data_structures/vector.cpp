#include <iostream>
#include <vector>

using namespace std;

int main() {
    int x = 5;
    int *ptr = &x;
    int &ref = x;

    cout << x << " stored at " << &x << endl;
    cout << " dereferencing pointer to x: " << *ptr << endl;
    cout << " referencing x through ref: " << ref << " stored at " << &ref << endl;

    ref = 6;
    cout << "updating x through ref, x is now: " << x << endl;

    vector<int> arr = {1, 2, 3};
    vector<int> *arr_ptr = &arr;
    vector<int> &arr_ref = arr;

    for (int i = 0; i < arr_ref.size(); i++) {
        cout << i << ": " << arr[i] << endl;
    }
    cout << "range based for loop to increment" << endl;

    for (auto &a : arr_ref) {
        a++;
        cout << a << endl;
    }
    return 0;
}


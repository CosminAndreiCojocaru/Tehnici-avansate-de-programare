#include <iostream>
#include <vector>
using namespace std;

void CountingSort(vector<int>& array, int exponent) {
	int number = array.size();
	vector<int> output(number);
	int count[10] = { 0 };

	for (int i = 0; i < number; i++) {
		count[(array[i] / exponent) % 10]++;
	}

	for (int i = 1; i < 10; i++) {
		count[i] += count[i - 1];
	}

	for (int i = number - 1; i >= 0; i--) {
		int digit = (array[i] / exponent) % 10;
		output[count[digit] - 1] = array[i];
		count[digit]--;
	}
	
	for (int i = 0; i < number; i++) {
		array[i] = output[i];
	}
}


void RadixSort(vector<int>& array) {
	int maxval = array[0];
	for (int x : array) {
		if (x > maxval) {
			maxval = x;
		}
	}

	for (int exponent = 1; maxval / exponent > 0; exponent *= 10) {
		CountingSort(array, exponent);
	}
}

int main()
{
	int n;
	cout << "Introduceti numarul de elemente: ";
	cin >> n;

	vector<int> array(n);
	cout << "Introduceti elemetele: ";
	for (int i = 0; i < n; i++) {
		cin >> array[i];
	}

	RadixSort(array);

	cout << "Vector sortat: ";
	for (int x : array) {
		cout << x << " ";
	}
	cout << endl;

	return 0;
}
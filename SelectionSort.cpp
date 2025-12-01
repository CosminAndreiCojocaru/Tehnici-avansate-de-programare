#include <iostream>
using namespace std;

void swap(int &x, int &y) {
	int n;
	n = x;
	x = y;
	y = n;

}

void SelectionSort(int *array, int size){

	int i, j, min;

	for (i = 0; i < size - 1; i++) {
		min = i;

		for (j = i + 1; j < size; j++)
			if (array[j] < array[min])
				min = j;


		swap(array[i], array[min]);
	}
}


int main()
{
	int n;

	n = 5;

	int array[5] = { 21, 5, 23, 52, 9 };

	cout << "Sirul inainte: " ;
	for (int i = 0; i < n; i++) {
		cout << array[i]<< " ";
	}
	cout << endl;

	SelectionSort(array, n);

	cout << "Sirul dupa: ";
	for (int i = 0; i < n; i++) {
		cout << array[i] << " ";
	}
}

#include <iostream>
#include <vector>
using namespace std;

vector<int> CountingSort(vector<int>& array) {
	int number = array.size();

	int max_value = 0;

	for (int i = 0; i < number; i++) {
		max_value = max(max_value, array[i]);
	}

	vector<int> CountArray(max_value + 1, 0);

	for (int i = 0; i < number; i++) {
		CountArray[array[i]]++;
	}

	for (int i = 1; i <= max_value; i++) {
		CountArray[i] += CountArray[i - 1];
	}

	vector<int> ans(number);
	for (int i = number - 1; i >= 0; i--) {
		ans[CountArray[array[i]] - 1] = array[i];
		CountArray[array[i]]--;
	}

	return ans;
}




int main()
{

	vector<int> array = { 2, 5, 7, 3, 1, 0, 8, 4 };
	vector<int> ans = CountingSort(array);

	for (int x : ans) {
		cout << x << " ";
	}

	return 0;


}

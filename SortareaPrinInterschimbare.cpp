#include <iostream>
using namespace std;

int main() {

    int n;
    cout << "Introdu numarul de valori: ";
    cin >> n;

    int v[100];
    for (int i = 0; i < n; i++) {
        cout << "Introdu valorile: ";
        cin >> v[i];
    }

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (v[i] > v[j]) {
                int aux = v[i];
                v[i] = v[j];
                v[j] = aux;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << v[i] << " ";
    }

    return 0;
}

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main(){
    ifstream input;
    input.open("1.txt");

    vector<int> n;
    string a;

    while (getline(input, a)){
        n.push_back(stoi(a));
    }

    input.close();
    /* part one
    int size = n.size();
    for (int i=0; i < size; i++){
        for (int j=i+1; j<size; j++){
            int a = n[i];
            int b = n[j];
            if (a + b == 2020){
                cout << a * b << endl;
                return 0;
            }
        }
    } */

    int size = n.size();
    for (int i=0; i < size; i++){
        for (int j=i+1; j<size; j++){
            for (int k=i+2; k<size; k++){
                int a = n[i];
                int b = n[j];
                int c = n[k];
                if (a + b + c == 2020){
                    cout << a * b * c << endl;
                    return 0;
                }
            }
        }
    }
};

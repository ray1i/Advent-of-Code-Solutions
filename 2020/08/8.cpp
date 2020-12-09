#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

int main(){
    ifstream input;
    input.open("8.txt");

    vector<string> inst;
    string a;

    while (getline(input, a)) inst.push_back(a);

    input.close();

//part one:

    int acc = 0;
    unordered_set<int> seen;
    int curr = 0;

    while (seen.count(curr) != 1){
        seen.insert(curr);
        if (inst[curr].substr(0, 3) == "acc"){
            acc += stoi(inst[curr].substr(4, 5));
            curr++;
        } else if (inst[curr].substr(0, 3) == "jmp"){
            curr += stoi(inst[curr].substr(4, 5));
        } else if (inst[curr].substr(0, 3) == "nop"){
            curr++;
        }
    }
    cout << "part one: " << acc << endl;

//part two:
    for (int i = 0; i<inst.size(); i++){
        vector<string> temp = inst;
        
        bool proceed = true;
        if (temp[i].substr(0, 3) == "jmp") temp[i].replace(0, 3, "nop");
        else if (temp[i].substr(0, 3) == "nop") temp[i].replace(0, 3, "jmp");
        else proceed = false;

        if (proceed){
            acc = 0;
            seen.clear();
            curr = 0;

            while (seen.count(curr) != 1){
                seen.insert(curr);
                if (temp[curr].substr(0, 3) == "acc"){
                    acc += stoi(temp[curr].substr(4, 5));
                    curr++;
                } else if (temp[curr].substr(0, 3) == "jmp"){
                    curr += stoi(temp[curr].substr(4, 5));
                } else if (temp[curr].substr(0, 3) == "nop"){
                    curr++;
                }

                if (curr == temp.size()){
                    cout << "part two: " << acc;
                    return 0;
                }
            }
        }
    }

    return 0;
}
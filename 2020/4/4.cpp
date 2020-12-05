// this code is disgusting

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <unordered_set>
#include <regex>

using namespace std;

bool values_good(map<string, string> v){
    int trues = 0;
    if (regex_match(v["byr"], regex("[0-9]{4}")) && stoi(v["byr"]) >= 1920 && stoi(v["byr"]) <= 2002) trues++;
    if (regex_match(v["iyr"], regex("[0-9]{4}")) && stoi(v["iyr"]) >= 2010 && stoi(v["iyr"]) <= 2020) trues++;
    if (regex_match(v["eyr"], regex("[0-9]{4}")) && stoi(v["eyr"]) >= 2020 && stoi(v["eyr"]) <= 2030) trues++;
    if (regex_match(v["hgt"], regex("[0-9]+cm"))){
        if (stoi(v["hgt"].substr(0, v["hgt"].find("c"))) >= 150 && stoi(v["hgt"].substr(0, v["hgt"].find("c"))) <= 193) trues++;
    } else if (regex_match(v["hgt"], regex("[0-9]+in"))){
        if (stoi(v["hgt"].substr(0, v["hgt"].find("i"))) >= 59 && stoi(v["hgt"].substr(0, v["hgt"].find("i"))) <= 76) trues++;
    }
    if (regex_match(v["hcl"], regex("#([a-z]|[0-9]){6}"))) trues++;
    if (regex_match(v["ecl"], regex("(amb|blu|brn|gry|grn|hzl|oth)"))) trues++;
    if (regex_match(v["pid"], regex("([0-9]{9})"))) trues++;
    if (trues == 7) return true;
    return false;
}

int main(){
    ifstream input;
    input.open("4.txt");

    vector<string> lines;
    string a;
    while (getline(input, a)) lines.push_back(a);

    input.close();

    unordered_set<string> good1 = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"};
    unordered_set<string> good2 = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};

/* part one:
    int count = 0;
    unordered_set<string> cur;
    for (int i = 0; i<lines.size(); i++){
        string curline = lines[i];
        if (curline == "") {
            if (cur == good1 || cur == good2) count++;
            cur.clear();
        } else {
            while (curline.find(":") != -1){
                string temp = "";
                for (int j=3; j > 0; j--){
                    temp += curline[curline.find(":") - j];
                }
                curline.erase(curline.find(":"), 1);
                cur.insert(temp);
            }
        }
    }
    if (cur == good1 || cur == good2) count++;
    cout << count;
*/

    int count = 0;
    unordered_set<string> cur;
    map<string, string> curvalues;

    for (int i = 0; i<lines.size(); i++){
        string curline = lines[i];
        if (curline == "") {
            if (cur == good1 || cur == good2 ){
                if (values_good(curvalues)) count++;
            }
            cur.clear();
            curvalues.clear();
        } else {
            while (curline.find(":") != -1){
                string temp = curline.substr(curline.find(":") - 3, 3);
                cur.insert(temp);
                string temp2;
                if (curline.find(" ") == -1) temp2 = curline.substr(curline.find(":") + 1, 100);
                else temp2 = curline.substr(curline.find(":") + 1, curline.find(" ") - curline.find(":") - 1);
                curvalues[temp] = temp2;

                curline.erase(curline.find(":"), 1);
                try {
                    curline.erase(curline.find(" "), 1);
                } catch (const exception& e) {
                    ;
                }
            }
        }
    }
    if (cur == good1 || cur == good2){
        if (values_good(curvalues)) count++;
    }
    cout << count;

    return 0;
}

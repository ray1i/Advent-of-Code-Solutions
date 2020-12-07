#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <regex>
#include <map>
#include <unordered_set>

using namespace std;

int total_bags(string s, map<string, vector<string>> contains, map<string, vector<int>> contains_count){
    if (contains[s].empty()) return 1;
    else {
        int c = 0;
        for (int i = 0; i<contains[s].size(); i++){
            c += total_bags(contains[s][i], contains, contains_count) * contains_count[s][i];
        }
        return c + 1;
    }
}

int main(){
    ifstream input;
    input.open("7.txt");

    vector<string> rules;
    string a;

    while (getline(input, a)) rules.push_back(a);

    input.close();

    map<string, vector<string>> contains;
    map<string, vector<int>> contains_count;
    map<string, vector<string>> contained_by;

    for (int i = 0; i<rules.size(); i++){
        smatch big_bag;
        smatch small_bags;
        regex_search(rules[i], big_bag, regex("(.+) bags contain "));

        string s = rules[i];
        while (regex_search(s, small_bags, regex("([0-9]) ([^,]+) bag"))){
            if (contains.find(big_bag[1]) == contains.end()){
                contains[big_bag[1]] = {};
                contains_count[big_bag[1]] = {};
            }
            contains[big_bag[1]].push_back(small_bags[2]);
            contains_count[big_bag[1]].push_back(stoi(small_bags[1]));
            
            if (contained_by.find(small_bags[2]) == contained_by.end()) contained_by[small_bags[2]] = {};
            contained_by[small_bags[2]].push_back(big_bag[1]);

            s = small_bags.suffix().str();
        }
    }

// part one:
    unordered_set<string> seen;
    vector<string> queue = {"shiny gold"};
    int count = 0;
    while (queue.size() > 0){
        for (int i = 0; i<contained_by[queue[0]].size(); i++){

            if (seen.find(contained_by[queue[0]][i]) == seen.end()){
                queue.push_back(contained_by[queue[0]][i]);
                seen.insert(contained_by[queue[0]][i]);

                count++;
            }
        }
        queue.erase(queue.begin());
    }
    cout << "part one: " << count << endl;

// part two:
    
    cout << "part two: " << total_bags("shiny gold", contains, contains_count) - 1;

    return 0;
}
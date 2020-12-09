#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int pre_len = 25;

bool int_possible(vector<vector<int>> v, int to_check){
    for (int i = 0; i<pre_len; i++){
        for (int j=0; j<pre_len; j++){
            if (v[i][j] == to_check) return true; 
        }
    }
    return false;
}

int main(){
    ifstream input;
    input.open("9.txt");

    vector<long long int> nums;
    string a;

    while (getline(input, a)) {
        nums.push_back(stoll(a));
    }
    input.close();


//part one:
    vector<vector<int>> possible;

    for (int i = 0; i<pre_len; i++){
        vector<int> temp;
        possible.push_back(temp);
        for (int j = 0; j<pre_len; j++){
            if (i == j) possible[i].push_back(-1);
            else possible[i].push_back(nums[i] + nums[j]);
        }
    }

    int bad;
    for (int i=25; i<nums.size(); i++){
        if (int_possible(possible, nums[i])){
            possible.erase(possible.begin());
            vector<int> temp;
            possible.push_back(temp);
            for (int j = 0; j<pre_len; j++){
                if (i == j) possible[pre_len-1].push_back(-1);
                else possible[pre_len-1].push_back(nums[i] + nums[i-j]);
        }
        } else{
            bad = nums[i];
            break;
        }
    }
    cout << "part one: " << bad << endl;

//part two:
    vector<int> range;
    long long int sum = 0;

    for (int i = 0; i<nums.size(); i++){
        range.push_back(nums[i]);
        sum += nums[i];
        if (bad < sum) {
            do {
                sum -= range[0];
                range.erase(range.begin());
            } while(bad < sum);
        }
        if (bad == sum) break; 
    }

    long long int max = range[0];
    long long int min = range[0];
    for (int i = 0; i<range.size(); i++){
        if (range[i] > max) max = range[i];
        if (range[i] < min) min = range[i];
    }

    cout << "part two: " << max + min;

    return 0;
}
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;


vector<double> reversed_henon_map(double x, double y, double a, double b){
	double x_next = y/b;
	double y_next = a* pow((y/b), 2) + x - 1;
	vector<double> result;
	result.push_back(x_next); result.push_back(y_next);
	return result;
}

int main() {
	vector<vector<double>> values {{0.5688254014690528, -0.08255572592986403}};
	double a = 1.4; double b = 0.3;
	for (int i=0; i<25; i++){
		vector<double> pair;
		pair.push_back(values[values.size()-1][0]);
		pair.push_back(values[values.size()-1][1]);
		values.push_back(reversed_henon_map(pair[0], pair[1], a, b));
	}
	for (int i = 0; i < values.size(); i++){
		cout << values[i][0] << ", ";
		cout << values[i][1] << endl;
	}
	return 0;
}




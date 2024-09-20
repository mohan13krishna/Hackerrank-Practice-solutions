// author: mohan13krishna

#include <iostream>
#include <string>
using namespace std;
int main()
{
    string a, b;

    cin >> a;
    cin >> b;

    int len1 = a.size();
    int len2 = b.size();

    cout << len1 << " " << len2 << endl;

    cout << a << b << endl;

    char c;
    c = a[0];
    a[0] = b[0];
    b[0] = c;

    cout << a << " " << b;

    return 0;
}

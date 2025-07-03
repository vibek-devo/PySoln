#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;
const ll MOD = 1e9 + 7;

vector<vector<ll>> multiply(vector<vector<ll>>& A, vector<vector<ll>>& B) {
    int n=A.size();
    vector<vector<ll>> result(n, vector<ll>(n, 0));

    for(int i= 0;i<n; i++)
        for(int j=0; j<n;j++)
            for(int k= 0; k< n; k++)
                result[i][j]=(result[i][j] + A[i][k] * B[k][j]) % MOD;

    return result;
}

vector<vector<ll>> matrixPower(vector<vector<ll>> base, ll power) {
    int n = base.size();
    vector<vector<ll>> result(n, vector<ll>(n, 0));


    for(int i=0; i< n; i++)
        result[i][i]= 1;

    while(power> 0) {
        if(power % 2 == 1)
            result = multiply(result, base);
        base = multiply(base, base);
        power /= 2;
    }

    return result;
}

ll countWays(ll n) {
    if(n == 0) return 1;
    if(n == 1) return 1;
    if(n == 2) return 2;

    vector<ll> base = {2, 1, 1};

    vector<vector<ll>> T = {
        {2, 0, 1},
        {1, 0, 0},
        {0, 1, 0}
    };


    vector<vector<ll>> T_power = matrixPower(T, n - 2);


    ll result = 0;
    for(int i = 0; i < 3; i++) {
        result = (result + T_power[0][i] * base[i]) % MOD;
    }

    return result;
}

int main() {
    ll n;
    cout << "Enter value of N: ";
    cin >> n;

    cout << "Ways to tile 2x" << n << " corridor: " << countWays(n) << endl;
    return 0;
}

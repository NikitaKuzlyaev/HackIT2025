#include<iostream>
#include<vector>

using namespace std;

int main()
{
	int K, N;
	cin >> K >> N;
	string S;
	cin >> S;
	vector<vector<short int> > a(K, vector<short int>(K));
	int ans = 0;
	for (int r = 0; r < K; ++r)
	{
		ans += 1; // Подстрока s[r..r]
		for (int l = r - 1; l >= 0; --l)
		{
			a[l][r] = a[l + 1][r - 1];
			if (S[l] != S[r])
				a[l][r]++;
			if (a[l][r] <= N)
				ans++;
		}
	}
	cout << ans << endl;
	return 0;
}

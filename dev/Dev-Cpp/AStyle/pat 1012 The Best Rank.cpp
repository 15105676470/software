#include <iostream>
#include <cstdio>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;
struct Stu {
	string sno;
	int C,M,E,A;
	void ini(string _sno, int _C, int _M, int _E) {
		sno = _sno;
		C = _C;
		M = _M;
		E = _E;
		A = (C+M+E)/3;
	}
	int cr,mr,er,ar;
} stu[2500];
bool cmp(pair<string, int> A, pair<string, int> B) {
	return A.second > B.second;
}
int main() {
	int n,m;
	cin >> n >> m;
	unordered_map<string, int> s2i;
	vector<pair<string,int> > C,M,E,A;
	for (int i = 0; i < n; i++) {
		string sno;
		int c,m,e;
		cin >> sno >> c >> m >> e;
		stu[i].ini(sno, c, m, e);
		s2i[sno] = i;
		C.push_back(make_pair(sno, c));
		M.push_back(make_pair(sno, m));
		E.push_back(make_pair(sno, e));
		A.push_back(make_pair(sno, (c+m+e)/3));
	}
	sort(C.begin(), C.end(), cmp);
	sort(M.begin(), M.end(), cmp);
	sort(E.begin(), E.end(), cmp);
	sort(A.begin(), A.end(), cmp);
	for (int i = 0; i < n; i++) {
		int idx = s2i[C[i].first];
		if (i == 0) {
			stu[idx].cr = 1;
			continue;
		}
		if (C[i].second != C[i-1].second) stu[idx].cr = i+1;
		else stu[idx].cr = stu[s2i[C[i-1].first]].cr;
	}
	for (int i = 0; i < n; i++) {
		int idx = s2i[M[i].first];
		if (i == 0) {
			stu[idx].mr = 1;
			continue;
		}
		if (M[i].second != M[i-1].second) stu[idx].mr = i+1;
		else stu[idx].mr = stu[s2i[M[i-1].first]].mr;
	}
	for (int i = 0; i < n; i++) {
		int idx = s2i[E[i].first];
		if (i == 0) {
			stu[idx].er = 1;
			continue;
		}
		if (E[i].second != E[i-1].second) stu[idx].er = i+1;
		else stu[idx].er = stu[s2i[E[i-1].first]].er;
	}
	for (int i = 0; i < n; i++) {
		int idx = s2i[A[i].first];
		if (i == 0) {
			stu[idx].ar = 1;
			continue;
		}
		if (A[i].second != A[i-1].second) stu[idx].ar = i+1;
		else stu[idx].ar = stu[s2i[A[i-1].first]].ar;
	}
	//cout<<stu[0].ar<<endl<<endl;
	//cout<<stu[0].er<<" "<<stu[1].er<<" "<<stu[3].er<<endl<<endl;
	for (int i = 0; i < m; i++) {
		string cur;
		cin >> cur;
		if (!s2i.count(cur)) cout<<"N/A"<<endl;
		else {
			int idx = s2i[cur];
			int ans = stu[idx].ar;
			char sub = 'A';
			if (ans > stu[idx].cr) ans = stu[idx].cr, sub = 'C';
			if (ans > stu[idx].mr) ans = stu[idx].mr, sub = 'M';
			if (ans > stu[idx].er) ans = stu[idx].er, sub = 'E';
			cout<<ans<<" "<<sub<<endl;
		}
	}
	return 0;
}


N, K = map(int, input().split())

Nfac = 1
NminKfac = 1
Kfac = 1

for i in range(1, N + 1):
    Nfac *= i

for j in range(1, K + 1):
    Kfac *= j

for k in range(1, N - K + 1):
    NminKfac *= k

result = Nfac // (NminKfac * Kfac)
print(result)
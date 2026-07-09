k1, n1, m1 = map(int, input().split())
k2, n2, m2 = map(int, input().split())

bolt = k1 - k1 * n1 // 100
gaika = k2 - k2 * n2 // 100

if bolt < gaika:
    bo = gaika - bolt
    print(bo * m2 + k1 * n1 // 100 * m1 + k2 * n2 // 100 * m2)
elif bolt > gaika:
    ga = bolt - gaika
    print(ga * m1 + k1 * n1 // 100 * m1 + k2 * n2 // 100 * m2)
elif bolt == gaika:
    print(bolt*m1+gaika*m2)
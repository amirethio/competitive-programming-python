# Problem: Insomnia cure
# Difficulty: 800
# Link: https://codeforces.com/problemset/problem/785/A
# Status: Solved 


# -------------------------------
# Approach: 
# 1.accpt no of polyhedron and loop by no of it 
# 2. in each loop accept the shapes and add up in some variable
# 3. print the var
# -------------------------------

poly_no = int(input())
result = 0
for i in range(poly_no):
    shape =  input().strip()
    if(shape == "Tetrahedron"):
        result += 4
    elif(shape == "Cube"):
        result += 6
    elif(shape == "Dodecahedron"):
        result += 12
    elif(shape == "Octahedron" ):
        result += 8
    else:
        result +=20
print(result)
score=float(input())
if 80 <= score <= 100:
    print("A")
else:
    if 80 > score >= 70:
        print("B")
    else:
        if 70 > score >= 60:
            print("C")
        else:
            if 60 > score >= 50:
                print("D")
            else:
                if score < 50:
                    print("F")
                else:
                    if score > 100 or score < 0:
                        print("Error")
count = 0
def fun():
    global count
    if count == 4:
        return
    print("Shaurya")
    count+=1
    fun()

fun()
array = ["indigo", "groc", "verd", "vermell", "blau", "cian", "taronja"]

longitut_ona = {
"indigo": 400,
"groc": 575,
"verd": 520,
"vermell": 650,
"blau": 470,
"cian": 495,
"taronja": 620
}
def bubble_sort(array):
    for i in range(0,len(array)-1):
        for j in range(len(array)-1):
                array[j] = array[j+1]
print(array)

## Dictionary method
student={
    "name":"devanshi",
    "subject":{
        "phy":45,
        "chem":90,
        "bio":78
    }
}
## mydict.keys()
print(student.keys())

## mydict.values()
print(list(student.values()))

##mydict.length()
print(len(list(student.keys())))

## mydict.items()
print(list(student.items()))

## mydict.update()
student.update({"color":"blue"})
print(student)


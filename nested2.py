myfamily = {

    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },

    "child3" : {
        "name" : "Emil",
        "year" : 2004
    },

        "child2" : {
        "name" : "fatta",
        "year" : 2004
    }

}
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

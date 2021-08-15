x = {1: "one", 2: "two"}
x
type(x)

x["first"] = "one"
x

x[("Delorme", "Ryan", 1995)] = (1, 2, 3)
x
type(x)

list(x.keys())

x[1]
x.get(1, "not available")

x.get(4, "not available")
x
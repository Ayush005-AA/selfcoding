# strings methods


a = "my name is bob"
print(a.capitalize())
 

b = "my name is bob"
print(b.casefold())



c = "bob"
print(c.center(10,"$"))



d = "my name is bob i love my name"
print(d.count("name"))


e = "my name is bob"
print(e.find("name"))



f = "my name is bob"
print(f.endswith("bob"))
print(f.startswith("my"))



g = "my\tname\tis\tbob"
print(g.expandtabs(1))


h  = "my name is bob"
print(h.index("a"))


i = "my name is bob"
print(i.isalpha())


j = "23"
print(j.isdecimal())


k = "456"
print(k.isdigit())

l = "my name is bob","my name is bob"
m = "$"

print(m.join(l))


n = "##my name is bob"
print(n.lstrip("#"))





o = "my name is bob"
print(o.replace("bob","ayush"))


p = "strangers   things    "

print(p.rsplit())


q = "my# name# is #bob"
print(q.split("#"))
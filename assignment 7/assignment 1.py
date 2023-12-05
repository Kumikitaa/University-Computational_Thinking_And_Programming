def chop (l):
    l.remove(l[0]);
    l.remove(l[-1]);

def middle (l):
    l = l[1:3];
    return l;

my_list = [1,2,3,4];
print(f"my list before call chop function => {my_list}");
chop(my_list);
print(f"my list after call chop function => {my_list}\n");

my_list = [1,2,3,4];
print (f"my list before call middle function => {my_list}");
new_list = middle(my_list);
print (f"my list after call middle function => {my_list}");
print(f"new list after  call middle fucntion => {new_list}");
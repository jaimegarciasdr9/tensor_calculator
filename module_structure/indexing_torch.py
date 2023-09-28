import torch

example = [[4.0, 1.0], [5.0, 3.0], [2.0, 1.0]]
my_tensor = torch.tensor(example)
print(my_tensor)

a = torch.ones(3, 2)

a_t = torch.transpose(a, 0, 1)

print(a.shape, a_t.shape)

a = torch.ones(3, 2)

a_t = a.transpose(0, 1)

print(a.shape, a_t.shape)



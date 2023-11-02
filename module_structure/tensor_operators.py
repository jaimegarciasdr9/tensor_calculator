import torch

__all__ = ['TensorCalculator']


class TensorCalculator:
    def __init__(self):
        pass

    def tensor_zeros(self, dim_x, dim_y, dim_z):
        zeros = torch.zeros([dim_x, dim_y, dim_z])
        return zeros

    def tensor_ones(self, dim_x, dim_y, dim_z):
        ones = torch.ones([dim_x, dim_y, dim_z])
        return ones

    def tensor_random(self, dim_x, dim_y, dim_z):
        random_tensor = torch.rand([dim_x, dim_y, dim_z])
        return random_tensor

    def tensor_sum(self, tensor1, tensor2):
        if tensor1.shape == tensor2.shape:
            result = tensor1 + tensor2
            return result
        else:
            raise ValueError("Tensors must have the same shape for addition.")

    def tensor_multiply(self, tensor1, tensor2):
        if tensor1.shape == tensor2.shape:
            result = tensor1 * tensor2
            return result
        else:
            raise ValueError("Tensors must have the same shape for multiplication.")


tc = TensorCalculator()
tc_zero = tc.tensor_zeros(3, 4, 5)    # • Returns an all-Zeros Tensor
tc_one = tc.tensor_ones(3, 4, 5)     # • Returns an all-Ones Tensor
tc_random = tc.tensor_random(3, 4, 5)   # • Returns a Tensor with random values
a = torch.ones([3, 4, 5])
b = torch.ones([3, 4, 5]) * 2
tc_sum = tc.tensor_sum(a, b)     # • Returns the sum of two tensor
tc_mult = tc.tensor_multiply(a, b)    # • Returns the multiplication of two tensors

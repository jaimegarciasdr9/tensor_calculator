# -------
# Author: Jaime García
# Last update: 02/11/2023

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

    def tensor_transpose(self, tensor):
        transposed = torch.transpose(tensor, 0, 1)
        return transposed

    def tensor_mean(self, tensor):
        mean_value = torch.mean(tensor)
        return mean_value

    def tensor_stddev(self, tensor):
        std_dev = torch.std(tensor)
        return std_dev

# module_structure

#### Project description
First professional module sketch.
The Tensor Calculator is a Python class that provides several methods for performing operations on tensors using PyTorch. This readme will explain how to use the Tensor Calculator and its methods.
###
#### Installation instructions
To install the Tensor Calculator, follow these steps:
####
1. Clone the repository to your local machine using git clone.
####
2. Install PyTorch by following the instructions on the PyTorch website.
####
3. Install any other dependencies by running pip install -r requirements.txt.
####
4. Run the setup.py script to install the Tensor Calculator:
   

    python setup.py install

5. Verify that the installation was successful by running the tests:

    
    python tests.py
###
#### Usage instructions
To use the Tensor Calculator, you need to create an instance of the TensorCalculator class and then call the desired method on that instance.
The class TensorCalculator has the following methods:

  1 ) tensor_ones(dim_x, dim_y, dim_z): Returns a tensor filled with ones of the specified dimensions.

  2 ) tensor_zeros(dim_x, dim_y, dim_z): Returns a tensor filled with zeros of the specified dimensions.

  3 ) tensor_random(dim_x, dim_y, dim_z): Returns a tensor with random values of the specified dimensions.

  4 ) tensor_sum(tensor1, tensor2): Returns the sum of two tensors if they have the same shape.

  5 ) tensor_multiply(tensor1, tensor2): Returns the element-wise multiplication of two tensors if they have the same shape.
#### Extra:
  6 ) tensor_transpose(self, tensor): This function takes a single input tensor as its argument and returns a new tensor that is the transpose of the input tensor. 

  7 ) tensor_mean(self, tensor): This function calculates the mean value of all elements in the input tensor.

  8 ) tensor_stddev(self, tensor): This function calculates the standard deviation of the elements in the input tensor. 
###
#### Examples
tc = TensorCalculator()
####
tc_zero = tc.tensor_zeros(3, 4, 5)    # • Returns an all-Zeros Tensor
####
tc_one = tc.tensor_ones(3, 4, 5)     # • Returns an all-Ones Tensor
####
tc_random = tc.tensor_random(3, 4, 5)   # • Returns a Tensor with random values
####
a = torch.ones([3, 4, 5])
b = torch.ones([3, 4, 5]) * 2
####
tc_sum = tc.tensor_sum(a, b)     # • Returns the sum of two tensor
####
tc_mult = tc.tensor_multiply(a, b)    # • Returns the multiplication of two tensors
###
#### License information
MIT License

Copyright (c) 2023 Jaime García

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

###
#### Contact information
author: Jaime García Sainz de Rozas
####
Data Analyst studying at Universidad Francisco de Vitoria
####
github: https://github.com/jaimegarciasdr9





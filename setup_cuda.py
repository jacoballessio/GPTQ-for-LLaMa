from setuptools import setup, Extension
from torch.utils import cpp_extension

arch_list = ['sm_80']

class custom_BuildExtension(cpp_extension.BuildExtension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build_extensions(self):
        for extension in self.extensions:
            extension.extra_compile_args = {'nvcc': ['-arch={}'.format(arch) for arch in arch_list]}
        super().build_extensions()

setup(
    name='quant_cuda',
    ext_modules=[cpp_extension.CUDAExtension(
        'quant_cuda', ['quant_cuda.cpp', 'quant_cuda_kernel.cu']
    )],
    cmdclass={'build_ext': custom_BuildExtension}
)

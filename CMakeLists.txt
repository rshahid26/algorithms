cmake_minimum_required(VERSION 3.10)
project(algorithms)

set(CMAKE_CXX_STANDARD 14)
add_executable(AlgorithmsExecutable AVL.cpp data_structures/vector.cpp
        data_structures/Array.h)

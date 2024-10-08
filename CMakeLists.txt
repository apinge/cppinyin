cmake_minimum_required(VERSION 3.15 FATAL_ERROR)

project(cppinyin)

set(CPPINYIN_VERSION "0.5")

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")

set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(BUILD_RPATH_USE_ORIGIN TRUE)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

if(NOT APPLE)
  set(CPPINYIN_RPATH_ORIGIN "$ORIGIN")
else()
  set(CPPINYIN_RPATH_ORIGIN "@loader_path")
endif()

set(CMAKE_INSTALL_RPATH ${CPPINYIN_RPATH_ORIGIN})
set(CMAKE_BUILD_RPATH ${CPPINYIN_RPATH_ORIGIN})

option(CPPINYIN_ENABLE_TESTS "Whether to build tests" ON)
option(CPPINYIN_BUILD_PYTHON "Whether to build Python" OFF)
option(BUILD_SHARED_LIBS "Whether to build shared libraries" ON)

# for env witout setting utf-8 for Chinese 
#if(WIN32)
#  add_compile_options("$<$<CXX_COMPILER_ID:MSVC>:/execution-charset:utf-8>")
#  add_compile_options("$<$<CXX_COMPILER_ID:MSVC>:/source-charset:utf-8>")
#  add_compile_options("$<$<CXX_COMPILER_ID:MSVC>:/bigobj>")
#endif()

if(WIN32)
  message(STATUS "Set BUILD_SHARED_LIBS to OFF for Windows")
  set(BUILD_SHARED_LIBS OFF CACHE BOOL "" FORCE)
endif()

if(NOT CMAKE_BUILD_TYPE)
  message(STATUS "No CMAKE_BUILD_TYPE given, default to Release")
  set(CMAKE_BUILD_TYPE Release)
endif()


list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake/Modules)
list(APPEND CMAKE_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)

set(CMAKE_CXX_STANDARD 20)  


#include(CheckCXXCompilerFlag)
#if(NOT WIN32)
#  check_cxx_compiler_flag("-std=c++14" CPPINYIN_COMPILER_SUPPORTS_CXX14)
#else()
  # windows x86 or x86_64
#  check_cxx_compiler_flag("/std:c++14" CPPINYIN_COMPILER_SUPPORTS_CXX14)
#endif()
#if(NOT CPPINYIN_COMPILER_SUPPORTS_CXX14)
#  message(FATAL_ERROR "
#    cppinyin requires a compiler supporting at least C++14.
#    If you are using GCC, please upgrade it to at least version 7.0.
#    If you are using Clang, please upgrade it to at least version 3.4.")
#endif()

set(CMAKE_CXX_STANDARD 20 CACHE STRING "The C++ version to be used.")
set(CMAKE_CXX_STANDARD_REQUIRED ON)  
set(CMAKE_CXX_EXTENSIONS OFF) # Disable compiler-specific extensions to ensure strict C++ standard compliance
message(STATUS "C++ Standard version: ${CMAKE_CXX_STANDARD}")

# Add /Zc:__cplusplus flag for Visual Studio to properly set the __cplusplus macro
if (MSVC)
  add_compile_options(/Zc:__cplusplus)
  set(CMAKE_CONFIGURATION_TYPES "Debug;Release" CACHE STRING "Choose the configuration types" FORCE)
  set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded")# refer to https://developercommunity.visualstudio.com/t/debug-build-works-but-release-build-failsas-well-a/428160
endif()

if(CPPINYIN_BUILD_PYTHON)
  include(pybind11)
endif()

include_directories(${CMAKE_SOURCE_DIR})

if(WIN32)
  # disable various warnings for MSVC
  # 4244: 'initializing': conversion from 'float' to 'int32_t',
  # 4267: 'argument': conversion from 'size_t' to 'uint32_t', possible loss of data
  set(disabled_warnings
      /wd4244
      /wd4267
  )
  message(STATUS "Disabled warnings: ${disabled_warnings}")
  foreach(w IN LISTS disabled_warnings)
    string(APPEND CMAKE_CXX_FLAGS " ${w} ")
  endforeach()
endif()

if(CPPINYIN_ENABLE_TESTS)
  include(googletest)
  enable_testing()
endif()

add_subdirectory(cppinyin)

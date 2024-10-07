# Cppinyin
This repository is forked from [cppinyin](https://github.com/pkufool/cppinyin) and aims to provide a pure C++ implementation for generating Pinyin from text. The original repository handled homographs in Chinese characters very well, and this repository further enhances compatibility with the C++ environment.

## Update Notes

* **Enhanced C++20 Compatibility**: Improved support for C++20 features and standards.
* **Removed Python Components**: The Python parts of the project have been removed to streamline the implementation.
* **Default Pinyin Mode Update**: Changed the default Pinyin representation (e.g., from `ǎ` to `a3`) to avoid the use of special characters.


# Build 

```
mkdir build && cd build
cmake -S ..
cmake --build . --config Release
```

# Usage
```C++
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include "cppinyin/csrc/cppinyin.h"

int main(){
system("chcp 65001"); //Using UTF-8 Encoding
std::string vocab_path = "cpp_pinyin.raw";
cppinyin::PinyinEncoder processor(vocab_path);

std::string str = "于谦参加了会计培训班 虽然他的会计基础参差不齐，但他仍然会努力学习";

std::ostringstream oss;
std::vector<std::string> pieces;

processor.Encode(str, &pieces);
for (auto piece : pieces) {
    oss << piece << " ";
}
std::cout << oss.str() << std::endl;
/*
result:
yu2 qian1 can1 jia1 le5 kuai4 ji4 pei2 xun4 ban1 sui1 ran2 ta1 de5 kuai4 ji4 ji1 chu3 cen1 ci1 bu4 qi2 ， dan4 ta1 reng2 ran2 hui4 nu3 li4 xue2 xi2
*/
}
```

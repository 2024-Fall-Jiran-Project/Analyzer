#include <iostream>
#include <cstring> // for strcpy

void vulnerableFunction(const char* input) {
    char buffer[10];
    // 입력값이 버퍼 크기를 초과할 경우 버퍼 오버플로우 발생
    strcpy(buffer, input);
    std::cout << "Buffer content: " << buffer << std::endl;
}

int main() {
    const char* input = "This input is too long and will overflow the buffer.";
    vulnerableFunction(input);
    return 0;
}

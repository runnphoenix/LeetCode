#include <stdio.h>

int getSum(int a, int b) {
	while (b != 0) {
		int c = a & b; // 进位信息
		a = a ^ b;     // 不带进位的结果
		b = c << 1;    // 进位信息左移1位，作为一个加数再于a相加
	}
	return a;
}

int main(int argc, char *argv[]) {
	int result = getSum(-2, 7);
	printf("result = %d",result);
	
	return 0;
}
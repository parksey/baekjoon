package level2;

import java.util.*;

public class P154539 {
    public int[] solution(int[] numbers) {
        int[] answer = {};
        NextBig nb = new NextBig(numbers);
        return nb.makeNext();
    }
}

class NextBig {
    int[] numbers;

    Stack<Integer> nextNumber;

    public NextBig(int[] numbers) {
        this.numbers = numbers;
        this.nextNumber = new Stack<>();
    }
    // 9, 1, 5, 3, 6, 2
    public int[] makeNext() {
        int[] result = new int[numbers.length];
        for (int i = 0; i < this.numbers.length; i++) {
            checkUp(result, i);
        }

        while(!this.nextNumber.isEmpty()) {
            result[this.nextNumber.pop()] = -1;
        }
        result[result.length-1] = -1;

        return result;
    }

    public void checkUp(int[] result, int index) {
        if (this.nextNumber.isEmpty()) {
            this.nextNumber.add(index);
            return;
        }

        while (!this.nextNumber.isEmpty()) {
            if (this.numbers[this.nextNumber.peek()] >= this.numbers[index]) {
                break;
            }

            int i = this.nextNumber.pop();
            result[i] = this.numbers[index];
        }
        this.nextNumber.add(index);
    }
}
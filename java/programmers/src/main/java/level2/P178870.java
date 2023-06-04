package level2;

import java.util.Stack;

public class P178870 {
    public int[] solution(int[] sequence, int k) {
        Seq seq = new Seq(sequence);
        seq.findK(k);
        return seq.getResult();
    }
}

class Seq {
    int[] sequence;
    int[] partSum;
    int[] result;

    public Seq(int[] sequence) {
        this.partSum = new int[sequence.length+1];
        this.result = new int[]{-1, -1};
        calcPartSum(sequence);
    }

    public void calcPartSum(int[] sequence) {
        this.partSum[1] = sequence[0];
        for(int i=2; i < this.partSum.length; i++) {
            this.partSum[i] = sequence[i-1] + this.partSum[i-1];
        }
    }

    public void findK(int k) {
        int left = 0;
        int right = 1;

        while (left < right) {
            if (outOfRange(left, right)) {
                break;
            }
            int part = this.partSum[right] - this.partSum[left];

            if (part < k) {
                right++;
            }
            else if (part > k) {
                left++;
            }
            else {
                setLowwer(left, right-1);
                right++;
            }
        }
    }

    public boolean outOfRange(int left, int right) {
        return left >= this.partSum.length || right >= this.partSum.length;
    }

    public void setLowwer(int left, int right) {
        if (this.result[1] == this.result[0] && this.result[0] == -1) {
            setData(left, right);
            return;
        }

        if (this.result[1] - this.result[0] <= right - left) {
            return;
        }

        this.result[0] = left;
        this.result[1] = right;
    }

    public void setData(int left, int right) {
        this.result[0] = left;
        this.result[1] = right;
    }

    public int[] getResult() {
        return this.result;
    }
}
// 1 2 3 4 5
/*
1 3 6 10 15
*/
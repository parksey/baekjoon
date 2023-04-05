import java.util.*;
public class P138477 {
    public void solve() {
        Solution s = new Solution();
        s.solution(3, new int[]{1,2,3,4,5});
    }
}

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        ScoreList scList = new ScoreList(k);

        for (int i=0; i < score.length; i++) {
            scList.add(score[i]);
            answer[i] = scList.getLastData();
        }


        return answer;
    }
}
class ScoreList {
    List<Integer> scoreList;
    final int k;

    public ScoreList(int k) {
        this.scoreList = new LinkedList<>();
        this.k = k;
    }

    public void add(int data) {
        int index = -1;

        for (int i=0; i < this.scoreList.size(); i++) {
            if (i >= k) {
                return;
            }
            if (this.scoreList.get(i) < data) {
                index = i;
                break;
            }
        }

        if (index == -1) {
            this.scoreList.add(this.scoreList.size(), data);
            return;
        }

        this.scoreList.add(index, data);
    }

    public int getLastData() {
        if (this.scoreList.size() < this.k) {
            return this.scoreList.get(this.scoreList.size()-1);
        }
        return this.scoreList.get(k-1);
    }

    public List<Integer> getScoreList() {
        return scoreList;
    }
}

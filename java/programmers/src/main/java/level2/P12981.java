package level2;
import java.util.*;

public class P12981 {

    public int[] solution(int n, String[] words) {
            int[] answer = {};
            Game game = new Game(n, words);

            answer = game.play();
            return answer;
    }
}

class Game {
    private int n;
    private String[] words;
    private int[] counts;

    private Set<String> used;

    public Game(int total, String[] words) {
        this.n = total;
        this.words = words;
        this.counts = new int[total];
        this.used = new HashSet<>();
    }

    public int[] play() {
        int id = 0;
        int count = 0;

        used.add(words[0]);
        System.out.println(used);
        for (int i=1; i < words.length; i++) {
            System.out.println(used);
            if ( words[i].length() < 2
                    || !equal(words[i-1], words[i])
                    || this.used.contains(words[i])
            ) {
                id = (i % n)+1;
                count = (i / n) + 1;
                break;
            }
            used.add(words[i]);
        }
        return new int[]{id,count};
    }

    private boolean equal(String firstWord, String secondWord) {
        if (firstWord.charAt(firstWord.length()-1)
                == secondWord.charAt(0)) {
            return true;
        }
        return false;
    }

}

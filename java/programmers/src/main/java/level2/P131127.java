package level2;
import java.util.*;
public class P131127 {
    public int solution(String[] want, int[] number, String[] discount) {
        Buy buy = new Buy(want, number);
        buy.calc(discount);
        return buy.getResult();
    }
}

class Buy {
    private static final int DISCOUNT_DATE = 10;

    private Map<String, Integer> buyList;
    private int result;

    public Buy(String[] want, int[] number) {
        this.buyList = new HashMap<>();
        this.result = 0;
        initList(want, number);

    }

    private void initList(String[] want, int[] number) {
        for (int i = 0; i < want.length; i++) {
            this.buyList.put(want[i], number[i]);
        }
    }

    public void calc(String[] discount) {
        for (int i = 0; i < discount.length - DISCOUNT_DATE + 1; i++) {
            Map<String, Integer> copy = new HashMap<>(this.buyList);

            if (!check(copy, i, discount)) {
                continue;
            }

            if (canBuy(copy)) {
                this.result++;
            }
        }

    }

    public boolean check(Map<String, Integer> copy, int index, String[] discount) {
        for (int i = index; i < index+DISCOUNT_DATE; i++) {
            if (!copy.containsKey(discount[i])) {
                return false;
            }

            copy.put(discount[i], copy.get(discount[i])-1);
        }
        return true;
    }


    public boolean canBuy(Map<String, Integer> copy) {
        return copy.values().stream()
                .allMatch(v -> v==0);
    }

    public int getResult() {
        return this.result;
    }
}
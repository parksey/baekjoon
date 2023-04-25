package level2;

import java.util.*;
import java.util.stream.*;
class P92341 {
    public int[] solution(int[] fees, String[] records) {

        Park park = new Park(fees);
        park.setRecords(records);
        park.calcAmount();
        park.calcFee();
        return park.getTotalFee();
    }
}

class Park {
    private Map<String, List<Recipe>> parks;
    private Map<String, Integer> totalAmount;
    private Map<String, Integer> totalFee;
    private int[] fees;

    public Park(int[] fees) {
        this.parks = new HashMap<>();
        this.totalAmount = new HashMap<>();
        this.totalFee = new HashMap<>();
        this.fees = fees;
    }

    public void setRecords(String[] records) {
        for (String record : records) {
            eachRecord(record);
        }
    }

    private void eachRecord(String record) {
        String[] infos = record.split(" ");
        Recipe recipe = new Recipe(infos[2], infos[0]);

        if (!parks.containsKey(infos[1])) {
            List<Recipe> re = new ArrayList<>();
            re.add(recipe);
            parks.put(infos[1], re);
            return;
        }

        List<Recipe> re = parks.get(infos[1]);
        re.add(recipe);
        parks.put(infos[1], re);
        return;
    }

    public void calcAmount() {
        for (String carPlate : this.parks.keySet()) {
            this.totalAmount.put(carPlate, calc(this.parks.get(carPlate)));
        }
    }

    public void calcFee() {
        for (String carPlate : this.totalAmount.keySet()) {
            int time = this.totalAmount.get(carPlate);

            if (time <= this.fees[0]) {
                this.totalFee.put(carPlate, this.fees[1]);
                continue;
            }

            time -= this.fees[0];

            if (time % this.fees[2] != 0) {
                time += this.fees[2];
            }
            time /= this.fees[2];

            this.totalFee.put(carPlate, time * fees[3] + fees[1]);
        }
    }

    private int calc(List<Recipe> recipes) {
        int ret = 0;
        List<Recipe> recipeCopy = sortByTime(recipes);

        int size =recipeCopy.size() /2 * 2;

        for (int i = 0; i < size; i+=2) {
            ret += calcTime(recipeCopy.get(i+1), recipeCopy.get(i));
        }

        if (size < recipeCopy.size()) {
            String[] timeIn = recipeCopy.get(size).getTime().split(":");
            int hour = calcBetween("23", timeIn[0]);
            int min = calcBetween("59", timeIn[1]);
            ret += (hour*60 + min);
        }

        return ret;
    }

    private int calcTime(Recipe rOut, Recipe rIn) {
        String[] timeOut = rOut.getTime().split(":");
        String[] timeIn = rIn.getTime().split(":");

        int hour = calcBetween(timeOut[0], timeIn[0]);
        int min = calcBetween(timeOut[1], timeIn[1]);
        return hour*60 + min;
    }

    private int calcBetween(String out, String in) {
        return Integer.parseInt(out) - Integer.parseInt(in);
    }

    private List<Recipe> sortByTime(List<Recipe> recipes) {
        return recipes.stream()
                .sorted((r1, r2) -> {
                    return r1.getTime().compareTo(r2.getTime());
                })
                .collect(Collectors.toList());
    }

    public int[] getTotalFee() {
        int[] result = new int[this.totalFee.size()];

        List<String> sorted = this.totalFee.keySet().stream()
                .sorted((name1, name2)-> {
                    return name1.compareTo(name2);
                })
                .collect(Collectors.toList());

        for (int i = 0; i < sorted.size(); i++) {
            result[i] = this.totalFee.get(sorted.get(i));
        }

        return result;
    }
}

class Recipe {
    private String info;
    private String time;

    public Recipe(String info, String time) {
        this.info = info;
        this.time = time;
    }


    public String getTime() {
        return time;
    }

    @Override
    public String toString(){
        return time+":"+info;
    }
}

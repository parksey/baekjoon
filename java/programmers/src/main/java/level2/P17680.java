package level2;

public class P17680 {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        Cache cache = new Cache(cacheSize);
        for (String city : cities) {
            answer += cache.setData(city);
        }
        return answer;
    }
}

class Cache {
    private static final int CACHE_HIT = 1;
    private static final int CACHE_MISS = 5;

    String[] dataList;
    int size;

    public Cache(int size) {
        this.dataList = new String[size];
        this.size = size;
    }

    public String parseCity(String city){
        if (city.length() > 20) {
            city = city.substring(0,20);
        }
        return city.toLowerCase();
    }

    public int setData(String city) {
        if (this.size == 0) {
            return CACHE_MISS;
        }

        city = parseCity(city);
        int index = findDataIndex(city);

        if ( index != -1 ) {
            updateCache(city, index);
            return CACHE_HIT;
        }

        updateCache(city, this.size-1);
        return CACHE_MISS;
    }

    private int findDataIndex(String city) {
        for (int i = 0; i < this.size; i++) {
            if (city.equals(this.dataList[i])) {
                return i;
            }
        }

        return -1;
    }

    private void updateCache(String city, int index) {
        for (int i = index; i > 0; i--) {
            this.dataList[i] = this.dataList[i-1];
        }
        this.dataList[0] = city;
    }
}
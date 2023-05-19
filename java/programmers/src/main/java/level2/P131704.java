package level2;

import java.util.*;
import java.util.stream.*;

public class P131704 {
    public int solution(int[] order) {
        int answer = 0;

        Container container = new Container();
        container.setMainContainer(order.length);
        container.put(order);
        return container.getResult();
    }
}

class Container {
    Stack<Integer> subContainer;
    Queue<Integer> mainContainer;
    int result;

    public Container() {
        this.result = 0;

        this.subContainer = new Stack<>();
        this.mainContainer = new LinkedList<>();
    }

    public void setMainContainer(int orderSize) {
        IntStream.range(1, orderSize+1)
                .forEach(mainContainer::add);
    }

    public void put(int[] order) {
        for (int or : order) {
            if(findMainContainer(or) || findSubContainer(or)) {
                this.result += 1;
                continue;
            }
            return;
        }
    }

    public boolean findMainContainer(int data) {
        while (!this.mainContainer.isEmpty()) {
            Integer peek = this.mainContainer.peek();
            if (peek < data) {
                this.subContainer.add(this.mainContainer.poll());
                continue;
            }

            if (peek == data) {
                this.mainContainer.poll();
                return true;
            }
            break;
        }

        return false;
    }

    public boolean findSubContainer(int data) {
        if (this.subContainer.isEmpty()) {
            return false;
        }

        return this.subContainer.pop() == data;
    }

    public int getResult() {
        return this.result;
    }
}

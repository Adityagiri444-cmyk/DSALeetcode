import java.util.*;

class Solution {
    public List<List<Integer>> generate(int numRows) {

        List<List<Integer>> answer = new ArrayList<>();

        for (int i = 0; i < numRows; i++) {

            List<Integer> row = new ArrayList<>();

            for (int j = 0; j <= i; j++) {

                
                if (j == 0 || j == i) {
                    row.add(1);
                } 
                else {
                
                    List<Integer> previousRow = answer.get(i - 1);

                    
                    int c1 = j - 1;
                    int c2 = j;

                    int value = previousRow.get(c1)
                              + previousRow.get(c2);

                    row.add(value);
                }
            }

            answer.add(row);
        }

        return answer;
    }
}
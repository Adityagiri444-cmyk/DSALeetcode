class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        Map<Integer, Integer> loss = new HashMap<>();

        for (int[] m : matches)
            loss.put(m[1], loss.getOrDefault(m[1], 0) + 1);

        Set<Integer> players = new HashSet<>();
        for (int[] m : matches) {
            players.add(m[0]);
            players.add(m[1]);
        }

        List<Integer> zero = new ArrayList<>();
        List<Integer> one = new ArrayList<>();

        for (int p : players) {
            int l = loss.getOrDefault(p, 0);
            if (l == 0) zero.add(p);
            else if (l == 1) one.add(p);
        }

        Collections.sort(zero);
        Collections.sort(one);

        return Arrays.asList(zero, one);
    }
}
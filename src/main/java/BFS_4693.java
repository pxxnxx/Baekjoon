import java.util.*;
public class BFS_4693 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        while (true){
            int w = sc.nextInt();
            int h = sc.nextInt();
            if (w == 0 && h == 0)
                break;
            int[][] arr = new int[h][w];
            for (int i=0; i<h; i++){
                for (int j=0; j<w; j++){
                    arr[i][j] = sc.nextInt();
                }
            }
            int[] dx = {0,0,1,-1,1,-1,1,-1};
            int[] dy = {1,-1,0,0,1,1,-1,-1};
            int[][] visit = new int[h][w];
            int answer = 0;
            int x, y;
            Queue<Integer> queue = new LinkedList<>();
            for (int i=0; i<h; i++){
                for (int j=0; j<w; j++){
                    if (arr[i][j] == 1 && visit[i][j] == 0) {
                        visit[i][j] = 1;
                        queue.add(i);
                        queue.add(j);
                        while (!queue.isEmpty()) {
                            y = queue.poll();
                            x = queue.poll();
                            for (int k = 0; k < 8; k++) {
                                int yy = y + dy[k];
                                int xx = x + dx[k];
                                if (xx >= 0 && xx < w && yy >= 0 && yy < h) {
                                    if (arr[yy][xx] == 1 && visit[yy][xx] == 0) {
                                        queue.add(yy);
                                        queue.add(xx);
                                        visit[yy][xx] = 1;
                                    }
                                }
                            }
                        }
                        answer++;
                    }
                }
            }
            System.out.println(answer);
        }
    }
}

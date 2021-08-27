import java.util.*;
import java.io.*;

public class DP_11722 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        int[] minus = new int[n];
        st = new StringTokenizer(bf.readLine());
        for (int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            minus[i] = 1;
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<i; j++) {
                if (arr[n-1-i] > arr[n-1-j])
                    minus[n-1-i] = Math.max(minus[n-1-i],minus[n-1-j]+1);
            }
        }
        int max = 0;
        for (int i=0; i<n; i++) {
            if (max < minus[i])
                max = minus[i];
        }
        System.out.println(max);
    }
}

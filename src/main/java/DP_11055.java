import java.util.*;
import java.io.*;
public class DP_11055 {
    public static void main (String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        int[] dp = new int[n];
        int max = 0;
        st = new StringTokenizer(bf.readLine());
        for (int i=0; i<n; i++)
            arr[i] = Integer.parseInt(st.nextToken());
        for (int i=0; i<n; i++) {
            dp[i] = arr[i];
            for (int j=0; j<i; j++) {
                if (arr[i] > arr[j] && dp[i] < dp[j] + arr[i])
                    dp[i] = dp[j] + arr[i];
            }
        }
        for (int i=0; i<n; i++) {
            if (max < dp[i])
                max = dp[i];
        }
        System.out.println(max);

    }
}

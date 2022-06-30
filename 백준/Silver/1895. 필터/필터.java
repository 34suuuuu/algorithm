import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] dp = new int[9];
        int[][] arr = new int[n][m];

        int filter_size = (n - 2) * (m - 2);
        int[] result = new int[filter_size];


        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        int x = sc.nextInt();

        int tmp, median = 0, cnt = 0;
        for (int i = 0; i < n - 2; i++) {
            tmp = 0;
            for (int j = 0; j < m - 2; j++) {
                dp[tmp] = arr[i][j];
                dp[tmp + 1] = arr[i][j + 1];
                dp[tmp + 2] = arr[i][j + 2];
                dp[tmp + 3] = arr[i + 1][j];
                dp[tmp + 4] = arr[i + 1][j + 1];
                dp[tmp + 5] = arr[i + 1][j + 2];
                dp[tmp + 6] = arr[i + 2][j];
                dp[tmp + 7] = arr[i + 2][j + 1];
                dp[tmp + 8] = arr[i + 2][j + 2];
                Arrays.sort(dp);
                result[median] = dp[4];
                median++;

            }
        }
        for (int i = 0; i < median; i++) {
            if(result[i] >= x) cnt++;
        }
        System.out.println(cnt);
    }
}

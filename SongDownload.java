package 爬取音乐;
import java.lang.ProcessBuilder;
import java.io.IOException;
import java.lang.Process;
public class SongDownload {
    public static void downloadSong(String url, String dath) {
        ProcessBuilder processBuilder = new ProcessBuilder(
                "you-get",
                "--output-dir", dath,
                "--debug",
                url
        );
        try {
            Process process = processBuilder.start();
          int exitCode=process.waitFor();
          if(exitCode!=0){
              System.err.println("下载失败,退出码："+exitCode);
          }else{
              System.out.println("下载成功");
          }
        } catch (IOException | InterruptedException e) {
           e.printStackTrace();
        }
    }
}

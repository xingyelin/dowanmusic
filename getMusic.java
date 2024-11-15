package 爬取音乐;
import java.util.Scanner;
import java.io.File;

class FileCheck{
    public static boolean checkFile(String path,String songname){
        File file=new File(path);
        File[] files=file.listFiles();
        if(files!=null){
            for(File dir:files){
                if(dir.getName().equals(songname)){
                    return true;
                }
            }
        }
        return false;
    }
}

public class getMusic {
    public static void main(String args[]){
          Scanner sc=new Scanner(System.in);
          System.out.println("请输入歌曲名:");
          String songname=sc.nextLine();
          System.out.println("请输入歌曲的url:");
          String songline=sc.nextLine();
          String path="F:\\music";
          long startTime=System.currentTimeMillis();
          if(FileCheck.checkFile(path,songname)){
              System.out.println("歌曲已经存在!!!");
          }else{
              SongDownload.downloadSong(songline,path);
              Filerename.renameFile(path,5,2);
          }
          long endTime=System.currentTimeMillis();
          System.out.println("下载完成,耗时:"+(endTime-startTime)/1000+"秒");
    }
}

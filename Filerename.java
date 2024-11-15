package 爬取音乐;
import java.io.File;
import java.util.regex.*;
public class Filerename {
    public static void renameFile(String path,int maxRetries,int retry_Delay){
        File file=new File(path);
        File[] files=file.listFiles();
        if(files!=null){
            Pattern pattern=Pattern.compile("^\\d+\\.\\s*(.*)");
            for(File dir:files){
                Matcher matcher=pattern.matcher(dir.getName());
                if(matcher.find()){
                      String newfileName=matcher.group(1);
                      File newFile=new File(file,newfileName);
                      int retriy=0;
                      while(retriy<maxRetries){
                          try{
                              if(dir.renameTo(newFile)){
                                  System.out.println("重命名成功!旧文件名称:"+dir.getName()+"更改为新文件名称："+newfileName);
                              break;
                              }else {
                        System.err.println("重命名失败，尝试重命名.......");
                              }
                          }catch(SecurityException e){
                              System.err.println("权限不足，无法重命名文件");
                              try{
                                  Thread.sleep(retry_Delay*1000);
                              }catch(InterruptedException ex){
                                  ex.printStackTrace();
                              }
                              retriy++;
                          }
                      }
                      if(retriy>=maxRetries){
                          System.err.println("重命名失败!");
                      }
                }
            }
        }
    }
}

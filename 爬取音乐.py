import subprocess
import os
import re
import time
def download_song(url, output_path):
    #创建列表，保存执行you-get命令的参数
    options = [
        '--output-dir', output_path,
        '--debug'  # 可选：启用调试模式
    ]
    """在终端的you-get执行命令  you-get -o ./downloads --debug https://example.com/video.mp4
    其中 you-get相当于python中的 pip install 是固定格式  -o用于指定下载歌曲的保存目录  也就是列表中的 output-dir 二者是等价的 
    同理，在终端中 也可以使用--output-dir命令指定歌曲的保存目录  不过要注意 相比o参数 output是双破折号   
    而在代码中 也可以使用o命令指定歌曲的保存目录 比如修改options
    options = [
    '-o', output_path,
    '--debug'
]  
    output_path是歌曲的具体保存路径
   debug是启用调试模式来查看详细的日志信息
    """
    command = ['you-get'] + options + [url]
    #command是一个列表   内容是：command = ['you-get', '--output-dir', output_path, '--debug', url]
    subprocess.run(command)#执行命令   依靠内部机制将command中存储的元素传递给操作系统 从而实现命令的执行

    """subprocess模块：subprocess 模块是 Python 标准库的一部分，用于生成新的进程，连接到它们的输入/输出/错误管道，
    并获取它们的返回码。subprocess 模块提供了多种方法来创建和管理子进程，
    其中最常用的是 subprocess.run、subprocess.Popen 和一些高级函数如 subprocess.call、subprocess.check_call 和 subprocess.check_output。
    
    subprocess.run:subprocess.run 是 Python 标准库 subprocess 模块中的一个函数，
    用于运行外部命令并等待其完成。它返回一个 CompletedProcess 对象，该对象包含命令的执行结果，包括返回码、标准输出和标准错误。
    
    详情见python官网：https://docs.python.org/3.11/   
    """
def rename_files(directory, max_retries=5, retry_delay=2):#重命名文件函数
    for filename in os.listdir(directory):#遍历保存歌曲文件夹中的所有文件名
        """
        os模块:os 模块是 Python 标准库中的一个重要模块，提供了许多与操作系统交互的功能。这些功能包括文件和目录操作、环境变量管理、进程管理等。详情见python官方文档
os.listdir 是 Python 标准库 os 模块中的一个函数，用于列出指定目录下的所有文件和子目录名称，以及其中文件名称
功能：返回指定路径下的所有文件和子目录的名称列表。
参数：
path：指定的目录路径，可以是相对路径或绝对路径。
返回值：一个包含目录中所有文件和子目录名称的列表。 注意 返回值是列表
        """
        # 使用正则表达式去掉数字前缀
        match = re.match(r'^\d+\.\s*(.*)', filename)
        """re.match 是 Python 标准库 re 模块中的一个函数，用于从字符串的起始位置匹配一个模式。如果匹配成功，返回一个匹配对象；如果匹配失败，返回 None。
        re.match(pattern, string, flags=0)
        pattern：要匹配的正则表达式模式。
       string：要搜索的字符串。
       flags：可选参数，用于指定匹配模式，如忽略大小写、多行模式等。
r'^\d+\.\s*(.*)':
^ 表示字符串的开始。
\d+ 匹配一个或多个数字。
\. 匹配一个点号。
\s* 匹配零个或多个空白字符。
(.*) 匹配任意字符（除了换行符），并将其捕获为一个组。                   filename是匹配的文件名
        """
        if match:#如果match对象不为None 即不为空
            """ 假设文件名为： 1. My Song.mp3   则返回的match对象是： <re.Match object; span=(0, 14), match='1. My Song.mp3'>这种形式
            match.group(0) 返回整个匹配的字符串，即 1. My Song.mp3。
            match.group(1) 返回第一个捕获组的内容，即 My Song.mp3。
            """
            new_filename = match.group(1)  #所以此处返回去掉数字前缀的文件名
            old_path = os.path.join(directory, filename)#组合旧文件路径  旧的文件名
            new_path = os.path.join(directory, new_filename)#组合新的文件路径  新的文件名
            #其中 directory是保存歌曲的文件夹路径
            """os.path.join函数：os.path.join(path, *paths) 
参数:
path：第一个路径组件。
*paths：后续的路径组件，可以有多个
返回值：一个字符串，表示组合后的完整路径。   
功能:
os.path.join 函数用于将一个或多个路径组件组合成一个完整的路径。它会根据操作系统的路径分隔符（例如，Windows 使用 \，Unix/Linux 使用 /）来正确地组合路径。         
            """
            # 尝试重命名文件
            retries = 0#临时变量
            while retries < max_retries: #max_retries是重命名重试的最大次数 在函数的参数中默认为5
                try:
                    os.rename(old_path, new_path)
                    """os.rename 是 Python 标准库 os 模块中的一个函数，用于重命名文件或目录
函数原型：os.rename(src, dst)
参数：参数：
src：原始文件或目录的路径。
dst：目标文件或目录的路径。
功能：
将 src 路径下的文件或目录重命名为 dst 路径。
如果 dst 已经存在，os.rename 会覆盖 dst。
返回值：
无返回值。      
         异常：
如果 src 不存在，会抛出 FileNotFoundError。
如果没有足够的权限执行重命名操作，会抛出 PermissionError。
其他可能的异常包括 OSError 等，具体取决于操作系统和文件系统的行为。 """
                    print(f'重命名文件成功!重命名旧路径: {old_path} 为新路径 {new_path}')
                    break
                except PermissionError as e:
                    print("出现异常：文件权限不够！请重试！！！")
                    time.sleep(retry_delay) #retry_daly是重试间隔时间 在函数的参数中默认为2
                    """time.sleep 是 Python 标准库 time 模块中的一个函数，用于使当前线程暂停执行指定的秒数。
                    它的主要用途是在程序中引入延迟，以便在某些情况下等待特定的时间间隔。
函数原型：time.sleep(seconds)   
seconds：浮点数或整数，表示暂停的秒数     
seconds：浮点数或整数，表示暂停的秒数。
功能
暂停执行：使当前线程暂停执行指定的秒数，这段时间内程序不会进行任何操作。
用途：
在网络请求中等待服务器响应。
在文件操作中等待文件释放锁。
在多线程或多进程环境中协调任务。
在定时任务中实现定时触发。             """
                    retries += 1#重试次数加一
            else:
                print("文件重命名失败！")

def check_song_name(out_directory,song_name):
      for filename in os.listdir(out_directory):
          if filename==song_name:
              return True
          else:
              return False

if __name__ == "__main__":
    print("请输入歌曲的url:")
    song_url = input()
    output_directory = "F:\\music"  # 注意使用双反斜杠或原始字符串
    print("请输入歌曲名称：")
    song_name=input()
    time_start=time.time()#函数开始运行时间
    if(check_song_name(output_directory,song_name)):
        # 下载歌曲
        download_song(song_url, output_directory)
        # 重命名文件
        rename_files(output_directory)
    else:
        print("文件已经存在，不再下载!")
    time_end=time.time()#函数结束运行时间
    print("下载完成，耗时：",time_end-time_start,"s")

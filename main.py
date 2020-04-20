import os
import logging
import time


# ========增加代码--开始========
def produce_stop_bat(pid, tmpfile="stop_xxx.bat"):
    # 待写入内容
    stop_cmd = 'taskkill /pid ' + str(pid) + ' /f'  # 关闭指定进程
    del_self_cmd = "del %0"  # 删除自身文件
    # 文件路径和名称
    tmp_all = "stop_" + tmpfile + ".bat"
    # 写入文件
    with open(file=tmp_all, mode="w") as f:
        f.write(stop_cmd + "\n" + del_self_cmd)


# 进程号
pid = os.getpid()
# 本文件名（不含后缀.py）
myfilename = os.path.split(__file__)[-1].split(".")[0]
# 生成关闭进程的脚本文件
produce_stop_bat(pid, myfilename)

# ========增加代码--结束========



# (1)如果日志文件夹不存在，则创建
log_dir = "log"  # 日志存放文件夹名称
log_path = os.getcwd() + os.sep + log_dir
if not os.path.isdir(log_path):
    os.makedirs(log_path)

# 设置logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
main_log_handler = logging.FileHandler(
    log_dir + "/dd_%s.log" % time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time())), mode="w+",
    encoding="utf-8")
main_log_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
main_log_handler.setFormatter(formatter)
logger.addHandler(main_log_handler)

# 控制台打印输出日志
console = logging.StreamHandler()  # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象
console.setLevel(logging.INFO)  # 设置要打印日志的等级，低于这一等级，不会打印
formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

while True:
    time_stamp = time.time()
    # print("时间戳",time_stamp)
    logger.info("时间戳 %s" % time_stamp)

    sec = 3
    logger.info("睡眠 %s 秒" % sec)
    time.sleep(sec)
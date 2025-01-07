from colorama import Fore
from datetime import datetime
import GPUtil
import cpuinfo
import psutil


TOKEN='7941646633:AAFBnFsyWQgUHANbq5ba9Cv8Cd5j4TxvIhg'
time = datetime.now().replace(microsecond=0)
b = f'{time}'
gpu_info = GPUtil.getGPUs()
cpu_info =  cpuinfo.get_cpu_info()['brand_raw']
dskinf = psutil.disk_usage('/')
disk_info = dskinf.total >> 30
minfo = psutil.virtual_memory()
meminfo = minfo.total >> 30

for i, gpu in enumerate(gpu_info):  
    gpun = f"{gpu.name}"
    cpun = f"{cpu_info}"
    dskinfo = f"Емкость Диска: {disk_info} GB"
    meminf = f"ОЗУ: {meminfo} GB"


icon_tg = print(Fore.CYAN + """

            ********                   
         **************                      
        *********+--****        
       ********+-..:*****       
       ******=:.-:.-*****       
       ****-...=:..=*****       
       *****=-+:...+*****       
       ********:...******       
        ********=.:*****                    
         **************                 
            ********            

        -TELEGRAT BOT-
        — by lzkamods —
""")
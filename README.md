# upgrade
service can upgrade back and repair app version

1.1	编写目的：
	使相关人员使用升级服务对交易客户端进行高效、统一的升级
  
1.2	适用范围：
	多个交易客户端
  
2 	升级服务模块及配置介绍：
升级服务分为服务端和客户端两部分
  
2.1	升级服务端介绍及配置
  升级服务端及升级客户端所需要交互的服务端，服务端所存放路径类似于："D:\project\pythonProject\client"
	交易客户端目录下所存放的文件为：需要发布的zip文件和configs.yaml配置文件，该配置文件内容为：
    app_id: 'MTC'  # 交易客户端名称
    version: '1.3.16'  # 交易客户端版本
    app_path: 'D:\project\pythonProject\client\MTC\TradeClient_V1.3.10_20160805.zip'  # 交易客户端zip文件路径
    ver_desc: ''  # 该版本的介绍
注：在某个目录（不包含中文目录）下新建client目录，在client目录下新建一个以该app命名的目录，如MTC，在MTC目录下放入发布的交易客户端zip文件和configs.yaml配置文件；

2.2	升级服务中的配置文件介绍
  升级服务配置文件内容（修改服务器ip即可）:
    ip: '192.168.15.55'  # 存放升级服务程序的计算机ip
    port: 6000  # 升级服务程序启动的端口
    root_dir: 'D:\project\pythonProject\client'  # 存放需要发布的交易客户端路径
    
2.3	升级服务客户端中的配置文件介绍
  升级客户端配置文件(修改升级服务端ip即可)：
    app_file_name: 'client_info.yaml'  # 客户端应用所在的根目录
    remote:
      host: '192.168.15.55'  # 升级服务端ip
      port: 5000  # 升级服务端口
      url: '/upgrade/get_lastest_version'  # 升级服务访问地址
      access_type: 'POST'  # 请求类型



# golang 使用docker 快速交叉编译

## 原理

使用docker快速生成一个和本地一样版本的golang环境，映射本地的GOPATH到docker镜像，编译后删除镜像

## 使用环境

运行环境中安装有docker，并已经运行

## 使用方法

可以将此文件放入系统的bin目录下，快速启动

```sh
chmod +x build.py
mv build.py /usr/local/bin/cross
```

### 推荐使用方法

```sh
cross
```

### 高级使用方法（不推荐使用）

```sh
cross --GOVersion=<goversion> --GOOS=<goos> --GOARCH=<goarch>
```

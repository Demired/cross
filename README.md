# golang 使用docker 快速交叉编译

## 原理

使用docker快速生成一个和本地一样版本的golang环境，映射本地的GOPATH到docker镜像，编译后删除镜像

## 使用方法

可以将此文件放入系统的bin目录下，快速启动

```sh
chmod +x build.py
mv build.py /usr/local/bin/cross
```

### 推荐

```sh
build.py
```

### 高级

```sh
build.py -v <golangversion> --GOOS=<os> --GOARCH=<goarch>
```
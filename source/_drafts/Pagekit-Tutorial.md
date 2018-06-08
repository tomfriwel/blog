---
title: Pagekit Tutorial
tags:
    - 工具
---

上传到服务器后，打开页面可能会看到需要将很多文件设置为可写：

`$ chmod 777 <dir>`

上传不了文件也是这个原因，也需要变为可写状态。

可能也会遇到这个问题：
```
{
    "error": true,
    "message": "文件上传错误 (The file \"IMG_4673.JPG\" exceeds your upload_max_filesize ini directive (limit is 2048 KiB).)"
}
```

![](file-upload-error0.png)

需要改一下php配置。我用的是`Ubuntu`，更改：

- 找到`/etc/php5/apache2/php.ini`
- 将其中的`upload_max_filesize`改为自己想要的大小
- `$ service apache2 restart`重启一下
# alert

> a simple notifyer which show the title and message that you specify in the terminal

---

> __how to install__
>
>```bash
>git clone https://github.com/shabane/alert.git && cd alert
>sudo ./install.sh
>```



> __Usage__:
>
>  ```alert 'title' 'message'```

> Example
> 
> ![alert](https://s4.uupload.ir/files/alert_82hb.gif)

> the __reasen__ that made me to write this was that i need to notify my self whenever a script run automaticly, so i decided to write a this.
> my script to backup is this:

```
#!/bin/bash
alert 'backup' 'geting backup started...'
NOW=`date`
tar --lzma -cvf /media/hdd/personal/tmp/$NOW.tar /home
alert 'backup' 'backup done'

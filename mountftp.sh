#!/bin/sh
#
# Run-level Startup script for curlftpfs
#
# chkconfig: 345 91 19
# description: Startup/Shutdown the curlftpfs


host='192.168.1.232'
mount='/home/sftpuser/mnt'
user='serverbackup'
pass='i7>c3jRsp6ea<PQ<'

# Mount the CurlFtpFS

if [ ! -d $mount ]; then
    mkdir -p $mount
fi


ase "$1" in
    start)
        curlftpfs $host $mount -o user=$user:$pass,allow_other
        ;;
    stop)
        fusermount -u $mount        
        ;;
    reload|restart)
        $0 stop
        $0 start
        ;;
    *)
        echo "Usage: $0 start|stop|restart|reload"
        exit 1
esac
exit 0

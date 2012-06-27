#Delete Older Backup Files
find /www/backup -type d -ctime +5 -exec rm -rf {} \

#Define Date
DATE_NAME=`date +%y%m%d`
#Back Up Path
BACKUP_PATH=/www/backup/$DATE_NAME
#Make Dictionary
mkdir $BACKUP_PATH

#Goto Backup Dictionary
cd $BACKUP_PATH

#Backup MySQl
/usr/local/mysql/bin/mysqldump -uUser -pPassword  --all-databases  > all_$DATE_NAME.sql

# Tar Database
tar -zcf all_sql_$DATE_NAME.tar.gz all_$DATE_NAME.sql

# Tar Files
tar -zcf jidongtuan_$DATE_NAME.tar.gz /www/jidongtuan/
tar -zcf gpoogp_$DATE_NAME.tar.gz /www/gpoogp/

tar -zcf config_$DATE_NAME.tar.gz /usr/local/apache/conf/httpd.conf /usr/local/apache/conf/extra/httpd-vhosts.conf /etc/my.cnf

#Remove Temp Files
rm -rf all_$DATE_NAME.sql

#uplpad to OSS
python /www/backup/oss/ossupload.py -d $DATE_NAME -l /www/backup/$DATE_NAME


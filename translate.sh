if [ $1 ] && [ $1 != '-c' ] ; then
  cd $1
  django-admin makemessages -l es -e html,py
elif [ $1 == '-c' ] && [ $2 ] ; then
  cd $2
  django-admin compilemessages
fi

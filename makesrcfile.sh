if [ $# -eq 1 ]
then
    section=`echo $1 | tr '.' '\n' | tail -1`
    file="/usr/share/man/man${section}/$1.gz"
    pkg=`pkgfile ${file} | tr '/' '\n' | tail -1`
    ver=`pacman -Q ${pkg} | tr ' ' '\n' | tail -1`
    echo '{\n    "package": "'$pkg'",\n    "version": "'$ver'",\n    "man": "'$file'"\n}' > ./src/$1.json
else
    echo "Please specify man page's name"
fi

if [ $# -eq 1 ]
then
    json="./src/$1.json"
    file=`cat ${json} | jq -r .man`
    pkg=`cat ${json} | jq -r .package`
    ver=`cat ${json} | jq -r .version`
    firstletter=`echo ${pkg} | cut -c 1-1`
    mkdir -p /tmp/man-page-compare
    wget https://archive.archlinux.org/packages/${firstletter}/${pkg}/${pkg}-${ver}-any.pkg.tar.xz -O /tmp/man-page-compare/original.tar.xz
    tar xvf /tmp/man-page-compare/original.tar.xz -C /tmp/man-page-compare
    meld /tmp/man-page-compare${file} ${file}
else
    echo "Please specify man page's name"
fi

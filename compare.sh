if [ $# -eq 1 ]
then
    json="./src/$1.json"
    file=`cat ${json} | jq -r .man`
    pkg=`cat ${json} | jq -r .package`
    ver=`cat ${json} | jq -r .version`
    mkdir -p /tmp/man-page-compare
    wget https://archive.archlinux.org/packages/.all/${pkg}-${ver}-x86_64.pkg.tar.xz -O /tmp/man-page-compare/original.tar.xz
    tar xvf /tmp/man-page-compare/original.tar.xz -C /tmp/man-page-compare
    meld /tmp/man-page-compare${file} ${file}
else
    echo "Please specify man page's name"
fi

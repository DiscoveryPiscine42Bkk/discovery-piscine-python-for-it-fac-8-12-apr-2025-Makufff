count=0
find /mnt/d/discovery-piscine-python-for-it-fac-8-12-apr-2025-Makufff/ -type f -name "*.py" -exec sh -c 'echo "Converting: $1"; dos2unix "$1"; count=$((count+1))' _ {} \;
echo "Total files converted: $count"


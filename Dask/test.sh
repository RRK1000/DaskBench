ssh hpt10@10.2.22.45 << 'HERE'
        out=$(ps -ef | grep "kworker" | head -n 1)
        echo "Killed collectl PID=$out" 
HERE
echo "bashed"
rqalpha run -fq 1d \
    -f ./strategy.py \
    --start-date 2015-01-01 \
    --end-date 2016-01-01 \
    --output-file ./result.pkl \
    --plot-save ./result.jpg \
    --account stock 100000 \
    --progress -bm 000001.XSHE \
    --extra-vars ''

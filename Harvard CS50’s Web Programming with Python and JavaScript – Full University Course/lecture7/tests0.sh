# To run this script, use chmod u+x tests0.sh to have access for executing the
# script and ./tests0.sh to execute the script itelf.
python3 -c "from tests0 import test_is_prime; test_is_prime(1, False)"
python3 -c "from tests0 import test_is_prime; test_is_prime(2, True)"
python3 -c "from tests0 import test_is_prime; test_is_prime(8, False)"
python3 -c "from tests0 import test_is_prime; test_is_prime(11, True)"
python3 -c "from tests0 import test_is_prime; test_is_prime(25, False)"
python3 -c "from tests0 import test_is_prime; test_is_prime(28, False)"
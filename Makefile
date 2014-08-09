




.PHONY: clean

clean:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -name "test.hdf5" -exec rm -f {} \;

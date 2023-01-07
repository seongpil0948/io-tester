
# python -m unittest -v --locals src.test_front
CREDENTIAL_PATH=$GOOGLE_APPLICATION_DEV_CREDENTIALS \
    python -m src.io_front
    # python -m src.io_front.common.redirect
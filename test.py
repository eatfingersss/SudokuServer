import log

def test(a, f):
    log.debug("test => {}", a)
    if a <= 1:
        return 1
    else:
        return f(a-1, f)+f(a-3,f)

def main():
    # test log
    log.error("Error Test Data:{}", True)
    log.info("Result => {}", test(10, test))

main()

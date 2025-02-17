import sys

if __name__ == '__main__':
    cur_path = sys.path[0]
    print("Working Path is:", cur_path)

    if len(sys.argv) == 2:
        network_id = str(sys.argv[1]).upper()
        if network_id in ["MAINNET", "TESTNET"]:
            pass
        else:
            print("Error, network_id should be MAINNET or TESTNET")
            exit(1)
    else:
        print("Error, must put NETWORK_ID as arg")
        exit(1)

    exec_lines = []
    tmpl = open("%s/backend_farm_and_pool.sh.tmpl" % cur_path, mode='r')
    while True:
        line = tmpl.readline()
        if not line:
            break
        exec_lines.append(line.replace("[CUR_PATH]", cur_path).replace("[NETWORK_ID]", network_id))
    tmpl.close()

    target_file = open("%s/backend_farm_and_pool.sh" % cur_path, mode='w')
    target_file.writelines(exec_lines)
    target_file.close()

    print("Note: backend_farm_and_pool.sh should be generated at that Path, ")
    print("please make it excuteable, such as chmod a+x backend_farm_and_pool.sh. ")
    print("and then put it into crontab for periodically invoke!")
    print("Crontab eg: ")
    print("  */5 * * * * /working_path/backend_farm_and_pool.sh > /dev/null")


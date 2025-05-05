

# For Example only
MO_MONITORING_EPICS    = ["123456", "234567", "345678"]
MO_OBSERVABILITY_EPICS = ["098765", "987654", "876543"]
MO_PERFORMANCE_EPICS   = ["012345", "019283", "928374"]
MO_AUTOMATION_EPICS    = ["000000", "111111", "222222"]
MO_SECURITY_EPICS      = ["999999", "888888", "777777"]

epic_lists = {
    "M&O_MONITORING_EPICS":     MO_MONITORING_EPICS,
    "M&O_OBSERVABILITY_EPICS":  MO_OBSERVABILITY_EPICS,
    "M&O_PERFORMANCE_EPICS":    MO_PERFORMANCE_EPICS,
    "M&O_AUTOMATION_EPICS":     MO_AUTOMATION_EPICS,
    "M&O_SECURITY_EPICS":       MO_SECURITY_EPICS,
}

def main():
    global epic_arry
    scnt = 30
    
    try:
        for epic_arry, epic_list_arry in epic_lists.items():
            # init_msg = f'{epic_arry}' + ": " + f'{epic_list_arry}'

                print(f'\n##### {epic_arry} #####') 
                for value in epic_list_arry:
                    print(f' - {value}')

        char0 = "#"
        main_repeated = 30
        main_sep = f"{'':{char0}>{main_repeated}}"

        print(f"\n{main_sep}\nTotal remaining stories is: {scnt}\n{main_sep}")



    except Exception as e:
        print(f"There was an exception in '{main.__module__}' : ", e)

if __name__ == '__main__':
    main()

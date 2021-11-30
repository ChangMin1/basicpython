inventory = {}




def add_item(item, amount, t_inventory):

    if check_item(item, t_inventory):
        t_inventory[item] += amount
        print(item+"의 수량은 "+str(t_inventory[item])+"입니다.")

    else:
        t_inventory[item] = amount
        print(item+"이 추가되었습니다.")



def remove_item(item, t_inventory):
    if check_item(item, t_inventory):
        t_inventory[item] = 0
        print(item+"의 수량이 0이 되었습니다.")
    else:
        print(item+"이 존재하지 않습니다.")


def consume_item(item):
    pass



def check_item(item, t_inventory):
    return item in t_inventory


def print_menu():
    print("0. 끝내기")
    print("1. 아이템 추가")
    print("2. 아이템 삭제")
    print("3. 아이템 확인")
    print("4. 아이템 사용")


def use_item():
    while True:
        print_menu()
        option = int(input("메뉴 번호를 입력하세요)"))
        if option == 0:
            print("종료합니다.")
            break
        elif option == 1:
            new_item = input("아이템을 입력하세요.)")
            amount = int(input("수량을 입력하세요.)"))


            add_item(new_item, amount, inventory)
        elif option == 2:
            elimiinated_item = input("아이템을 입력하세요.)")
            remove_item(eliminated_item, inventory)
        elif option == 3:
            print(inventory)
        elif option == 4:
            pass
        else:
            print("잘못된 번호를 입력하셨습니다.")


use_item()

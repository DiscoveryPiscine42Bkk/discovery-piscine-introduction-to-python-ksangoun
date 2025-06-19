import datetime

# List to store tasks. Each task is a dictionary.
# รายการสำหรับเก็บงาน แต่ละงานเป็น dictionary
tasks = []

def display_menu():
    """Displays the main menu of the cafe Task Organizer."""
    # แสดงเมนูหลักของโปรแกรม
    print("\n====== cafe Task Organizer ======")
    print("1. เพิ่มงานในcafe")
    print("2. แสดงรายการอาหารทั้งหมด")
    print("3. ยกเลิกอาหาร")
    print("4. สรุปจำนวนอาหารในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")
    print("---------------------------------------")

def add_task():
    """Adds a new task to the task list."""
    # เพิ่มงานใหม่ลงในรายการอาหาร
    print("\n=== เพิ่มงานในcafe ===")
    task_name = input("ป้อนชื่ออาหาร: ")
    
    while True:
        task_date_str = input("ป้อนวันที่ (dd/mm/yyyy): ")
        try:
            # Validate date format and convert to datetime object
            # ตรวจสอบรูปแบบวันที่และแปลงเป็น object วันที่
            task_date = datetime.datetime.strptime(task_date_str, "%d/%m/%Y").date()
            break
        except ValueError:
            print("รูปแบบวันที่ไม่ถูกต้อง กรุณาป้อนในรูปแบบ dd/mm/yyyy")

    task_type = input("ประเภทอาหาร (เช่น น้ำ/อาหารคาว/อื่นๆ): ")

    tasks.append({
        "name": task_name,
        "date": task_date,
        "type": task_type
    })
    print("เพิ่มงานสำเร็จ!")

def view_tasks():
    """Displays all tasks currently in the list."""
    # แสดงงานทั้งหมดในรายการ
    print("\n=== รายการอาหารทั้งหมด ===")
    if not tasks:
        print("ยังไม่มีอาหารในรายการ")
        return

    # Sort tasks by date for better readability
    # จัดเรียงอาหารตามวันที่เพื่อให้ดูง่ายขึ้น
    sorted_tasks = sorted(tasks, key=lambda x: x["date"])

    for i, task in enumerate(sorted_tasks):
        print(f"{i + 1}. {task['date'].strftime('%d/%m/%Y')}")
        print(f"   {task['name']} (ประเภท: {task['type']})")
    print("-------------------------")

def delete_task():
    """Deletes a task from the list based on user input."""
    # ลบงานออกจากรายการตาม input ของผู้ใช้
    print("\n=== ลบงาน ===")
    if not tasks:
        print("ยังไม่มีอาหารให้ลบ")
        return

    view_tasks() # Show tasks with numbers so user can pick
    # แสดงงานพร้อมหมายเลขเพื่อให้ผู้ใช้เลือก

    while True:
        try:
            task_index_to_delete = int(input("ลำดับของอาหารที่ต้องการลบ: ")) - 1
            if 0 <= task_index_to_delete < len(tasks):
                # Need to use the original `tasks` list for deletion after displaying `sorted_tasks`
                # Find the task in the original list based on its content (name, date, type)
                # เพื่อให้แน่ใจว่าลบอาหารที่ถูกต้องหลังจากแสดงผลงานที่จัดเรียงแล้ว
                # ต้องค้นหางานในลิสต์ `tasks` (ที่ยังไม่ได้จัดเรียง) โดยใช้ข้อมูลของงานนั้นๆ (ชื่อ, วันที่, ประเภท)
                task_to_remove = sorted(tasks, key=lambda x: x["date"])[task_index_to_delete]
                
                # Iterate through the original tasks to find and remove the matching task
                # วนซ้ำในลิสต์ tasks เดิมเพื่อค้นหาและลบอาหารที่ตรงกัน
                for i, task in enumerate(tasks):
                    if task["name"] == task_to_remove["name"] and \
                       task["date"] == task_to_remove["date"] and \
                       task["type"] == task_to_remove["type"]:
                        removed_task = tasks.pop(i)
                        print(f"ลบอาหาร: {removed_task['name']} แล้ว")
                        break
                break
            else:
                print("ลำดับงานไม่ถูกต้อง กรุณาป้อนลำดับที่อยู่ในรายการ")
        except ValueError:
            print("ป้อนเป็นตัวเลขเท่านั้น")

def summarize_tasks_by_type():
    """Summarizes the number of tasks for each type."""
    # สรุปจำนวนอาหารในแต่ละประเภท
    print("\n=== สรุปจำนวนอาหารแต่ละประเภท ===")
    if not tasks:
        print("ยังไม่มีอาหารในรายการเพื่อสรุป")
        return

    task_type_counts = {}
    for task in tasks:
        task_type = task["type"]
        task_type_counts[task_type] = task_type_counts.get(task_type, 0) + 1

    for task_type, count in task_type_counts.items():
        print(f"{task_type}: {count} อาหาร")
    print("---------------------------------")

def main():
    """Main function to run the cafe Task Organizer program."""
    # ฟังก์ชันหลักสำหรับเรียกใช้โปรแกรม cafe Task Organizer
    while True:
        display_menu()
        choice = input("เลือกเมนู (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            summarize_tasks_by_type()
        elif choice == '5':
            print("ขอบคุณที่ใช้โปรแกรม cafe!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาเลือก 1-5")

if __name__ == "__main__":
    main()
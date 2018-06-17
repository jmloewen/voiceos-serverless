
todos = []

def addTodo(item):
	todos.append(item)

def showToDOs():
	print("todolist app")

def main():
	showToDOs()
	addTodo("hello")

if __name__ == "__main__":
	main()
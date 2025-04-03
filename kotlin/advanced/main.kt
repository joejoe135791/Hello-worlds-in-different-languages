var name: String? = null

fun getinput(){
    print("Enter your name: ")
    name = readln()
}

fun main(){
    getinput()
    println("Hello, $name")
}
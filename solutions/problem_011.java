interface Animal {
    public bool eat(String item);
}

class Bird implements Animal{
    public bool eat(String item) {
        return item == "seeds";
    }
}

class Cat implements Animal{
    public bool eat(String item){
        return item == "meat";
    }
}

class Cat implements Animal{
    public bool eat(String item) {
        return item == "bones";
    }
}

class Cafe {
    public feed(Animal a) {
        a.eat("meat");
    }
}
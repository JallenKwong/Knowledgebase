---
title: Java反射机制
date: 2019-03-30 13:11:41
tags:
- 反射
categories:
- Java
---

[本文转自此处](https://www.cnblogs.com/yrstudy/p/6500982.html)

## 是什么 ##

Java Reflaction in Action有这么一句话，可以解释。反射是运行中的程序检查自己和软件运行环境的能力，它可以根据它发现的进行改变。**通俗的讲就是反射可以在运行时根据指定的类名获得类的信息。**


## 为什么 ##

我们为什么要使用反射，它的作用是什么，它在实际的编程中有什么应用。

首先我们先明确两个概念，静态编译和动态编译。

- 静态编译：在编译时确定类型，绑定对象,即通过。 
- 动态编译：运行时确定类型，绑定对象。动态编译最大限度发挥了java的灵活性，体现了多态的应用，有以降低类之间的藕合性。   

我们可以明确的看出动态编译的好处，而反射就是运用了动态编译创建对象。

那么我们再来看看实际中反射又有什么好处那？

往往对比能更加直观的向我们展示两者的不同。

---

若是不用反射，它是这样的

	interface Fruit{  
	    public abstract void eat();  
	}  
	    
	class Apple implements Fruit{  
	    public void eat(){  
	        System.out.println("Apple");  
	    }  
	}  
	    
	class Orange implements Fruit{  
	    public void eat(){  
	        System.out.println("Orange");  
	    }  
	}  
	    
	// 构造工厂类  
	// 也就是说以后如果我们在添加其他的实例的时候只需要修改工厂类就行了  
	class Factory{  
	    public static Fruit getInstance(String fruitName){  
	        fruit f=null;  
	        if("Apple".equals(fruitName)){  
	            f=new Apple();  
	        }  
	        if("Orange".equals(fruitName)){  
	            f=new Orange();  
	        }  
	        return f;  
	    }  
	}  
	class Hello{  
	    public static void main(String[] a){  
	        fruit f=Factory.getInstance("Orange");  
	        f.eat();  
	    }  
	    
	}

可以发现，每当我们要添加一种新的水果的时候，我们将不得不修改Factory中的源码。而且随着水果种类的增加，你会发现你的factory类会越来越臃肿，

不得不说这是一种十分不聪明的做法。

而反射无疑是一种聪明的办法，看代码。

	
	class Factory2{  
	    public static fruit getInstance(String ClassName){  
	        Fruit f=null;  
	        try{  
	            f=(Fruit)Class.forName(ClassName).newInstance();  
	        }catch (Exception e) {  
	            e.printStackTrace();  
	        }  
	        return f;  
	    }  
	}  

	class Hello2{  
	    public static void main(String[] a){  
	        Fruit f = Factory.getInstance("Reflect.Apple");  
	        if(f!=null){  
	            f.eat();  
	        }  
	    }  
	}

在出现新品种水果的时候，你完全不用去修改原有代码。

从上面的案例中，我们可以清楚的体会到反射的优越性。

---

那么有的人又会问，这个例子能完全明白，但是如果放到实际的编程，应用中，**我们又会在什么情况下用到反射？**

举一个看到过的例子，在实际开发中，我们需要把一个包中的class new出来，但是这个包中的类总是需要变动，那么怎么办，难道总是修改main方法中xxx=new xxx()吗。这样无疑是麻烦的。而运用反射。我们可以相应的增加一个配置文件，在里面记录包中所有的类名，包中类增加时就加一个类名，删除时就删除一个类名。让main方法去读取这个配置文件中的类名，通过反射获得实例，完全不用我们去修改main方法中的代码。

反射还有什么用？他甚至可以修改其他类中的私有属性。开发中，我们需要改变一个私有标志位的时候，源码并没有提供set方法，我们又不能改变源码，怎么办，反射可以完美解决这个问题。

说了这么多，那么我们的开发中，为什么不全部都用反射那？一个原因，**开销**，它的开销是什么昂贵的，随意尽量在最需要的地方使用反射。

## 怎么用 ##

说完是什么，为什么，我们必然需要掌握如何使用反射，先看反射中涉及了那些方法。

	Class c = Class.forName("className");//注明：className必须为全名，也就是得包含包名，比如，com.lun.UserInfo;

	Object obj=c.newInstance();//创建对象的实例

获得构造函数的方法 

    Constructor getConstructor(Class[] params)//根据指定参数获得public构造器

    Constructor[] getConstructors()//获得public的所有构造器

    Constructor getDeclaredConstructor(Class[] params)//根据指定参数获得public和非public的构造器

    Constructor[] getDeclaredConstructors()//获得public的所有构造器 

获得类方法的方法 

    Method getMethod(String name, Class[] params),根据方法名，参数类型获得方法

    Method[] getMethods()//获得所有的public方法

    Method getDeclaredMethod(String name, Class[] params)//根据方法名和参数类型，获得public和非public的方法

    Method[] getDeclaredMethods()//获得所以的public和非public方法 

获得类中属性的方法 

    Field getField(String name)//根据变量名得到相应的public变量

    Field[] getFields()//获得类中所以public的方法

    Field getDeclaredField(String name)//根据方法名获得public和非public变量

    Field[] getDeclaredFields()//获得类中所有的public和非public方法

看到这些方法，你就可以明白，反射是多么的强大了，当你正确使用这些方法的时候，基本上是掌握了反射的技巧。


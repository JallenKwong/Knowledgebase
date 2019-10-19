# Java clone – deep and shallow copy – copy constructors #

[Java clone – deep and shallow copy – copy constructors](https://howtodoinjava.com/java/cloning/a-guide-to-object-cloning-in-java)

[1.What is Java clone?](#what-is-java-clone?)

[2.Java Cloneable interface and clone() method](#java-cloneable-interface-and-clone-method)

[3.Java Shallow Copy](#java-shallow-copy)

[4.Java Deep Copy](#java-deep-copy)

[5.Java Copy Constructors](#java-copy-constructors)

[6.Java deep copy with serialization](#java-deep-copy-with-serialization)

[7.SerializationUtils](#serializationutils)

[8.Java clone best practices](#java-clone-best-practices)

[8.1.one](#one)

[8.2.two](#two)

A clone is an exact copy of the original. **In java, it essentially means the ability to create an object with similar state as the original object.** The java `clone()` method provides this functionality.

## What is Java clone? ##

So cloning is about creating the copy of original object. Its dictionary meaning is : “**make an identical copy of**“.

**By default, java cloning is ‘field by field copy’** i.e. as the Object class does not have idea about the structure of class on which `clone()` method will be invoked.

So, JVM when called for cloning, do following things:

- If the class has only primitive data type members then a completely new copy of the object will be created and the reference to the new object copy will be returned.
- If the class contains members of any class type then only the object references to those members are copied and hence the member references in both the original object as well as the cloned object refer to the same object.

Apart from above default behavior, you can always override this behavior and specify your own. This is done using overriding `clone()` method.

## Java Cloneable interface and clone() method ##

Every language which supports cloning of objects has its own rules and so does java. In java, if a class needs to support cloning it has to do following things:

1. You must implement `Cloneable` interface.
2. You must override `clone()` method from Object class. [Its weird. `clone()` method should have been in Cloneable interface.]

Java docs about `clone()` method are given below (formatted and extract).

	/*
	Creates and returns a copy of this object. The precise meaning of "copy" may depend on the class of the object.
	The general intent is that, for any object x, the expression:
	1) x.clone() != x will be true
	2) x.clone().getClass() == x.getClass() will be true, but these are not absolute requirements.
	3) x.clone().equals(x) will be true, this is not an absolute requirement.
	*/
	 
	protected native Object clone() throws CloneNotSupportedException;


1. First statement guarantees that cloned object will have separate memory address assignment.

2. Second statement suggest that original and cloned objects should have same class type, but it is not mandatory强制的.

3. Third statement suggest that original and cloned objects should have be equal using equals() method, but it is not mandatory.

---

Let’s understand Java clone with example. Our first class is `Employee` class with 3 attributes – `id`, `name` and `department`.

	public class Employee implements Cloneable{
	 
	    private int empoyeeId;
	    private String employeeName;
	    private Department department;
	 
	    public Employee(int id, String name, Department dept)
	    {
	        this.empoyeeId = id;
	        this.employeeName = name;
	        this.department = dept;
	    }
	    @Override
	    protected Object clone() throws CloneNotSupportedException {
	        return super.clone();
	    }
	     
	    //Getters and Setters
	}

`Department` class has two attributes – `id` and `name`.

	public class Department
	{
	    private int id;
	    private String name;
	 
	    public Department(int id, String name)
	    {
	        this.id = id;
	        this.name = name;
	    }
	 
	    //Getters and Setters
	}

So, if we need to clone the Employee class, then we need to do something like this.

	public class TestCloning{
	 
	    public static void main(String[] args) throws CloneNotSupportedException{
	        
	    	Department dept = new Department(1, "Human Resource");
	        Employee original = new Employee(1, "Admin", dept);
	 
	        //Lets create a clone of original object
	        Employee cloned = (Employee) original.clone();
	 
	        //Let verify using employee id, if cloning actually workded
	        System.out.println(cloned.getEmpoyeeId());
	 
	        //Verify JDK's rules
	 
	        //Must be true and objects must have different memory addresses
	        System.out.println(original != cloned);
	 
	        //As we are returning same class; so it should be true
	        System.out.println(original.getClass() == cloned.getClass());
	 
	        //Default equals method checks for references so it should be false. If we want to make it true,
	        //then we need to override equals method in Employee class.
	        System.out.println(original.equals(cloned));
	    }
	}

Output

	1
	true
	true
	false

Great, we successfully cloned the `Employee` object. But, remember we have two references to the same object and now both will change the state of the object in different parts of the application. 

	public class TestCloning {
	 
	    public static void main(String[] args) throws CloneNotSupportedException {
	        Department hr = new Department(1, "Human Resource");
	        Employee original = new Employee(1, "Admin", hr);
	        Employee cloned = (Employee) original.clone();
	 
	        //Let change the department name in cloned object and we will verify in original object
	        cloned.getDepartment().setName("Finance");
	 
	        System.out.println(original.getDepartment().getName());
	        System.out.println(cloned.getDepartment().getName());
	    }
	}

Output：

	Finance
	Finance

Oops, cloned object changes are visible in original also. This way cloned objects can make havoc in the system if allowed to do so. Anybody can come and clone your application objects and do whatever he likes. **Can we prevent this??**

Answer is yes, we can. We can prevent this by creating **Java deep copy** and **use copy constructors**. 

## Java Shallow Copy ##

**Shallow clone** is “default implementation” in Java. In overridden clone method, if you are not cloning all the object types (not primitives), then you are making a shallow copy.

All above examples are of shallow copy only, because we have not cloned the `Department` object on `Employee` class’s `clone` method.

## Java Deep Copy ##

**Deep clone** is the desired behavior in most the cases. **In the deep copy, we create a clone which is independent of original object and making changes in the cloned object should not affect original object.**

	//Modified clone() method in Employee class
	@Override
	protected Object clone() throws CloneNotSupportedException {
	    Employee cloned = (Employee)super.clone();
	    cloned.setDepartment((Department)cloned.getDepartment().clone());  
	    return cloned;
	}

I modified the `Employee` classes `clone()` method and added following `clone` method in `Department` class.

	//Defined clone method in Department class.
	@Override
	protected Object clone() throws CloneNotSupportedException {
	    return super.clone();
	}

Now testing our cloning code gives desired result and name of the department will not be modified.

	public class TestCloning2 {
		 
	    public static void main(String[] args) throws CloneNotSupportedException {
	        Department hr = new Department(1, "Human Resource");
	        Employee original = new Employee(1, "Admin", hr);
	        Employee cloned = (Employee) original.clone();
	 
	        //Let change the department name in cloned object and we will verify in original object
	        cloned.getDepartment().setName("Finance");
	 
	        System.out.println(original.getDepartment().getName());
	        System.out.println(cloned.getDepartment().getName());
	    }
	}

Output

	Human Resource
	Finance

Here, changing state of the cloned object does not affect the original object.

So deep cloning requires satisfaction of following rules –

- No need to separately copy primitives.
- All the member classes in original class should support cloning and in clone method of original class in context should call super.clone() on all member classes.
- If any member class does not support cloning then in clone method, one must create a new instance of that member class and copy all its attributes one by one to new member class object. This new member class object will be set in cloned object.

## Java Copy Constructors ##

Copy constructors are special constructors in a class which takes argument for its own class type. **So, when you pass an instance of class to copy constructor, then constructor will return a new instance of class with values copied from argument instance.** It helps you to clone object with Cloneable interface.

	public class PointOne
	{
	    private Integer x;
	    private Integer y;
	 
	    public PointOne(PointOne point){
	        this.x = point.x;
	        this.y = point.y;
	    }
	}

This method looks simple and it is until comes inheritance. When you define a class by extending above class, you need to define a similar constructor there also. In child class, you need to copy child specific attributes and pass the argument to the super class’s constructor. 

	public class PointTwo extends PointOne
	{
	    private Integer z;
	 
	    public PointTwo(PointTwo point){
	        super(point); //Call Super class constructor here
	        this.z = point.z;
	    }
	}

So, are we fine now? NO. The problem with inheritance is that exact behavior is identified only at runtime. So, in our case if some class passed the instance of `PointTwo` in constructor of `PointOne`.

In this case, you will get the instance of `PointOne` in return where you passed instance of `PointTwo` as argument.

	class Test
	{
	    public static void main(String[] args)
	    {
	        PointOne one = new PointOne(1,2);
	        PointTwo two = new PointTwo(1,2,3);
	 
	        PointOne clone1 = new PointOne(one);
	        PointOne clone2 = new PointOne(two);
	 
	        //Let check for class types
	        System.out.println(clone1.getClass());
	        System.out.println(clone2.getClass());
	    }
	}

Output

	class com.lun.other.clone.PointOne
	class com.lun.other.clone.PointOne

Another way of creating a copy constructor is to have **static factory methods**. They take class type in argument and create a new instance using another constructor of the class. Then these factory methods will copy all the state data to new class instance just created in the previous step, and return this updated instance.

	public class PointOne implements Cloneable
	{
	    private Integer x;
	    private Integer y;
	 
	    public PointOne(Integer x, Integer y)
	    {
	        this.x = x;
	        this.y = y;
	    }
	 
	    public PointOne copyPoint(PointOne point) throws CloneNotSupportedException
	    {
	        if(!(point instanceof Cloneable))
	        {
	            throw new CloneNotSupportedException("Invalid cloning");
	        }
	 
	        //Can do multiple other things here
	        return new PointOne(point.x, point.y);
	    }
	}

## Java deep copy with serialization ##

Serialization is another easy way of deep cloning. In this method, you just serialize the object to be cloned and de-serialize it. Obviously, the object which need to be cloned should implement `Serializable` interface.

Before going any further, I should caution that this technique is not to be used lightly.

1. First of all, serialization is hugely expensive. It could easily be a hundred times more expensive than the clone() method.

2. Second, not all objects are Serializable.

3. Third, making a class Serializable is tricky and not all classes can be relied on to get it right.

	@SuppressWarnings("unchecked")
	public static  T clone(T t) throws Exception {
		//Check if T is instance of Serializeble other throw CloneNotSupportedException
		ByteArrayOutputStream bos = new ByteArrayOutputStream();
	
		//Serialize it
		serializeToOutputStream(t, bos);
		byte[] bytes = bos.toByteArray();
		ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(bytes));
	
		//Deserialize it and return the new instance
		return (T)ois.readObject();
	}

## SerializationUtils ##

In Apache commons, SerializationUtils class also has utility function for deep cloning. If you feel interested the follow their official docs.

	<dependency>
	    <groupId>org.apache.commons</groupId>
	    <artifactId>commons-lang3</artifactId>
	    <version>3.7</version>
	</dependency>

---

	SomeObject cloned = org.apache.commons.lang.SerializationUtils.clone(someObject);

## Java clone best practices ##

### one ###

When you don’t know whether you can call the `clone()` method of a particular class as you are not sure if it is implemented in that class, you can check with checking if the class is instance of “`Cloneable`” interface as below.

	if(obj1 instanceof Cloneable){
	    obj2 = obj1.clone();
	}
	 
	//Dont do this. Cloneable dont have any methods
	obj2 = (Cloneable)obj1.clone();

### two ###

**No constructor is called on the object being cloned.** As a result, it is your responsibility, to make sure all the members have been properly set. Also, if you are keeping track of the number of objects in the system by counting the invocation of constructors, you got a new additional place to increment the counter.



# Testing with Hamcrest #

tag:JUnit Hamcrest

## Index ##

Matcher|Method
---|---
[Object](#)|hasToString<br/>typeCompatibleWith
[Bean](#)|hasProperty<br/>samePropertyValuesAs<br/>
[Collection](#)|---List---<br/>empty<br/>hasSize<br/>containsInAnyOrder<br/>contains<br/>---Array---<br/>arrayWithSize<br/>hasItemInArray<br/>isOneOf<br/>isIn<br/>arrayContainingInAnyOrder<br/>arrayContaining<br/>---Map---<br/>hasKey<br/>hasValue<br/>hasEntry<br/>
[Number](#)|greaterThan<br/>greaterThanOrEqualTo<br/>lessThan<br/>lessThanOrEqualTo<br/>closeTo
[Text](#)|isEmptyString<br/>isEmptyOrNullString<br/>equalToIgnoringWhiteSpace<br/>stringContainsInOrder
[Core](#)|is<br/>not<br/>containsString<br/>endsWith<br/>startsWith<br/>sameInstance<br/>instanceOf<br/>everyItem<br/>notNullValue<br/>anyOf<br/>allOf
[Custom](#)|<br/>


## Overview ##

Hamcrest is the well-known framework used for unit testing in the Java ecosystem. It’s bundled in JUnit and simply put, it uses existing predicates – called matcher classes – for making assertions.

## Hamcrest Setup ##

We can use Hamcrest with maven by adding the following dependency to our pom.xml file:

	<dependency>
	    <groupId>org.hamcrest</groupId>
	    <artifactId>hamcrest-all</artifactId>
	    <version>1.3</version>
	</dependency>

## An Example Test ##

Hamcrest is commonly used with junit and other testing frameworks for making assertions. Specifically, instead of using junit‘s numerous assert methods, we only use the API’s single assertThat statement with appropriate matchers.

Let’s look at an example that tests two Strings for equality regardless of case. This should give us a clear idea about how Hamcrest fits in to a testing method:

	@Test
	public void given2Strings_whenEqual_thenCorrect() {
		String a = "foo";
		String b = "FOO";
		assertThat(a, equalToIgnoringCase(b));
	}

## The Object Matcher ##

Hamcrest provides matchers for making assertions on arbitrary Java objects.

To assert that the toString method of an Object returns a specified String:

	@Test
	public void givenBean_whenToStringReturnsRequiredString_thenCorrect(){
	    Person person=new Person("Barrack", "Washington");
	    String str=person.toString();
	    assertThat(person,hasToString(str));
	}

We can also check that one class is a sub-class of another:


	@Test
	public void given2Classes_whenOneInheritsFromOther_thenCorrect(){
	        assertThat(Cat.class,typeCompatibleWith(Animal.class));
	    }
	}

## The Bean Matcher ##

We can use Hamcrest‘s Bean matcher to inspect properties of a Java bean.

Assume the following Person bean:

	public class Person {
	    String name;
	    String address;
	 
	    public Person(String personName, String personAddress) {
	        name = personName;
	        address = personAddress;
	    }
	}

We can check if the bean has the property, name like so:


	@Test
	public void givenBean_whenHasValue_thenCorrect() {
	    Person person = new Person("Baeldung", 25);
	    assertThat(person, hasProperty("name"));
	}

We can also check if Person has the address property, initialized to New York:


	@Test
	public void givenBean_whenHasCorrectValue_thenCorrect() {
	    Person person = new Person("Baeldung", "New York");
	    assertThat(person, hasProperty("address", equalTo("New York")));
	}

We can as well check if two Person objects are constructed with the same values:

	@Test
	public void given2Beans_whenHavingSameValues_thenCorrect() {
	    Person person1 = new Person("Baeldung", "New York");
	    Person person2 = new Person("Baeldung", "New York");
	    assertThat(person1, samePropertyValuesAs(person2));
	}

## The Collection Matcher ##

Hamcrest provides matchers for inspecting Collections.

Simple check to find out if a Collection is empty:


	@Test
	public void givenCollection_whenEmpty_thenCorrect() {
	    List<String> emptyList = new ArrayList<>();
	    assertThat(emptyList, empty());
	}

To check the size of a Collection:

	@Test
	public void givenAList_whenChecksSize_thenCorrect() {
	    List<String> hamcrestMatchers = Arrays.asList(
	      "collections", "beans", "text", "number");
	    assertThat(hamcrestMatchers, hasSize(4));
	}

We can also use it to assert that an array has a required size:

	@Test
	public void givenArray_whenChecksSize_thenCorrect() {
	    String[] hamcrestMatchers = { "collections", "beans", "text", "number" };
	    assertThat(hamcrestMatchers, arrayWithSize(4));
	}

To check if a Collection contains given members, regardless of order:

	@Test
	public void givenAListAndValues_whenChecksListForGivenValues_thenCorrect() {
	    List<String> hamcrestMatchers = Arrays.asList(
	      "collections", "beans", "text", "number");
	    assertThat(hamcrestMatchers,
	    containsInAnyOrder("beans", "text", "collections", "number"));
	}

To further assert that the Collection members are in given order:

	@Test
	public void givenAListAndValues_whenChecksListForGivenValuesWithOrder_thenCorrect() {
	    List<String> hamcrestMatchers = Arrays.asList(
	      "collections", "beans", "text", "number");
	    assertThat(hamcrestMatchers,
	    contains("collections", "beans", "text", "number"));
	}

To check if an array has a single given element:

	@Test
	public void givenArrayAndValue_whenValueFoundInArray_thenCorrect() {
	    String[] hamcrestMatchers = { "collections", "beans", "text", "number" };
	    assertThat(hamcrestMatchers, hasItemInArray("text"));
	}

We can also use an alternative matcher for the same test:

	@Test
	public void givenValueAndArray_whenValueIsOneOfArrayElements_thenCorrect() {
	    String[] hamcrestMatchers = { "collections", "beans", "text", "number" };
	    assertThat("text", isOneOf(hamcrestMatchers));
	}

Or still we can do the same with a different matcher like so:

	@Test
	public void givenValueAndArray_whenValueFoundInArray_thenCorrect() {
	    String[] array = new String[] { "collections", "beans", "text",
	      "number" };
	    assertThat("beans", isIn(array));
	}

We can also check if the array contains given elements regardless of order:

	@Test
	public void givenArrayAndValues_whenValuesFoundInArray_thenCorrect() {
	    String[] hamcrestMatchers = { "collections", "beans", "text", "number" };
	      assertThat(hamcrestMatchers,
	    arrayContainingInAnyOrder("beans", "collections", "number",
	      "text"));
	}

To check if the array contains given elements but in the given order:

	@Test
	public void givenArrayAndValues_whenValuesFoundInArrayInOrder_thenCorrect() {
	    String[] hamcrestMatchers = { "collections", "beans", "text", "number" };
	    assertThat(hamcrestMatchers,
	    arrayContaining("collections", "beans", "text", "number"));
	}
When our Collection is a Map, we can use the following matchers in these respective functions:

To check if it contains a given key:

	@Test
	public void givenMapAndKey_whenKeyFoundInMap_thenCorrect() {
	    Map<String, String> map = new HashMap<>();
	    map.put("blogname", "baeldung");
	    assertThat(map, hasKey("blogname"));
	}

and a given value:

	@Test
	public void givenMapAndValue_whenValueFoundInMap_thenCorrect() {
	    Map<String, String> map = new HashMap<>();
	    map.put("blogname", "baeldung");
	    assertThat(map, hasValue("baeldung"));
	}

and finally a given entry (key, value):

	@Test
	public void givenMapAndEntry_whenEntryFoundInMap_thenCorrect() {
	    Map<String, String> map = new HashMap<>();
	    map.put("blogname", "baeldung");
	    assertThat(map, hasEntry("blogname", "baeldung"));
	}

## The Number Matcher ##

The Number matchers are used to perform assertions on variables of the Number class.

To check greaterThan condition:

	@Test
	public void givenAnInteger_whenGreaterThan0_thenCorrect() {
	    assertThat(1, greaterThan(0));
	}

To check greaterThan or equalTo condition:

	@Test
	public void givenAnInteger_whenGreaterThanOrEqTo5_thenCorrect() {
	    assertThat(5, greaterThanOrEqualTo(5));
	}

To check lessThan condition:

	@Test
	public void givenAnInteger_whenLessThan0_thenCorrect() {
	    assertThat(-1, lessThan(0));
	}

To check lessThan or equalTo condition:

	@Test
	public void givenAnInteger_whenLessThanOrEqTo5_thenCorrect() {
	    assertThat(-1, lessThanOrEqualTo(5));
	}

To check closeTo condition:

	@Test
	public void givenADouble_whenCloseTo_thenCorrect() {
	    assertThat(1.2, closeTo(1, 0.5));
	}

## The Text Matcher ##

Assertion on Strings is made easier, neater and more intuitive with Hamcrest‘s text matchers. We are going to take a look at them in this section.

To check if a String is empty:

	@Test
	public void givenString_whenEmpty_thenCorrect() {
	    String str = "";
	    assertThat(str, isEmptyString());
	}

To check if a String is empty or null:

	@Test
	public void givenString_whenEmptyOrNull_thenCorrect() {
	    String str = null;
	    assertThat(str, isEmptyOrNullString());
	}

To check for equality of two Strings while ignoring white space:

	@Test
	public void given2Strings_whenEqualRegardlessWhiteSpace_thenCorrect() {
	    String str1 = "text";
	    String str2 = " text ";
	    assertThat(str1, equalToIgnoringWhiteSpace(str2));
	}

We can also check for the presence of one or more sub-strings in a given String in a given order:

	@Test
	public void givenString_whenContainsGivenSubstring_thenCorrect() {
	    String str = "calligraphy";
	    assertThat(str, stringContainsInOrder(Arrays.asList("call", "graph")));
	}

Finally, we can check for equality of two Strings regardless of case:

	@Test
	 public void given2Strings_whenEqual_thenCorrect() {
	    String a = "foo";
	    String b = "FOO";
	    assertThat(a, equalToIgnoringCase(b));
	}

## The Core API ##

The Hamcrest core API is to be used by third-party framework providers. However, it offers us some great constructs to make our unit tests more readable and also some core matchers that can be used just as easily.

Readability with the is construct on a matcher:

	@Test
	public void given2Strings_whenIsEqualRegardlessWhiteSpace_thenCorrect() {
	    String str1 = "text";
	    String str2 = " text ";
	    assertThat(str1, is(equalToIgnoringWhiteSpace(str2)));
	}

The is construct on a simple data type:

	@Test
	public void given2Strings_whenIsEqual_thenCorrect() {
	    String str1 = "text";
	    String str2 = "text";
	    assertThat(str1, is(str2));
	}

Negation with the not construct on a matcher:

	@Test
	public void given2Strings_whenIsNotEqualRegardlessWhiteSpace_thenCorrect() {
	    String str1 = "text";
	    String str2 = " texts ";
	    assertThat(str1, not(equalToIgnoringWhiteSpace(str2)));
	}

The not construct on a simple data type:

	@Test
	public void given2Strings_whenNotEqual_thenCorrect() {
	    String str1 = "text";
	    String str2 = "texts";
	    assertThat(str1, not(str2));
	}

Check if a String contains a given sub-string:

	@Test
	public void givenAStrings_whenContainsAnotherGivenString_thenCorrect() {
	    String str1 = "calligraphy";
	    String str2 = "call";
	    assertThat(str1, containsString(str2));
	}

Check if a String starts with given sub-string:

	@Test
	public void givenAString_whenStartsWithAnotherGivenString_thenCorrect() {
	    String str1 = "calligraphy";
	    String str2 = "call";
	    assertThat(str1, startsWith(str2));
	}

Check if a String ends with given sub-string:

	@Test
	public void givenAString_whenEndsWithAnotherGivenString_thenCorrect() {
	    String str1 = "calligraphy";
	    String str2 = "phy";
	    assertThat(str1, endsWith(str2));
	}

Check if two Objects are of the same instance:

	@Test
	public void given2Objects_whenSameInstance_thenCorrect() {
	    Cat cat=new Cat();
	    assertThat(cat, sameInstance(cat));
	}

Check if an Object is an instance of a given class:

	@Test
	public void givenAnObject_whenInstanceOfGivenClass_thenCorrect() {
	    Cat cat=new Cat();
	    assertThat(cat, instanceOf(Cat.class));
	}

Check if all members of a Collection meet a condition:

	@Test
	public void givenList_whenEachElementGreaterThan0_thenCorrect() {
	    List<Integer> list = Arrays.asList(1, 2, 3);
	    int baseCase = 0;
	    assertThat(list, everyItem(greaterThan(baseCase)));
	}

Check that a String is not null:

	@Test
	public void givenString_whenNotNull_thenCorrect() {
	    String str = "notnull";
	    assertThat(str, notNullValue());
	}

Chain conditions together, test passes when target meets any of the conditions, similar to logical OR:

	@Test
	public void givenString_whenMeetsAnyOfGivenConditions_thenCorrect() {
	    String str = "calligraphy";
	    String start = "call";
	    String end = "foo";
	    assertThat(str, anyOf(startsWith(start), containsString(end)));
	}

Chain conditions together, test passes only when target meets all conditions, similar to logical AND:

	@Test
	public void givenString_whenMeetsAllOfGivenConditions_thenCorrect() {
	    String str = "calligraphy";
	    String start = "call";
	    String end = "phy";
	    assertThat(str, allOf(startsWith(start), endsWith(end)));
	}

## A Custom Matcher ##

We can define our own matcher by extending TypeSafeMatcher. In this section, we will create a custom matcher which allows a test to pass only when the target is a positive integer.

	public class IsPositiveInteger extends TypeSafeMatcher<Integer> {
	 
	    public void describeTo(Description description) {
	        description.appendText("a positive integer");
	    }
	 
	    @Factory
	    public static Matcher<Integer> isAPositiveInteger() {
	        return new IsPositiveInteger();
	    }
	 
	    @Override
	    protected boolean matchesSafely(Integer integer) {
	        return integer > 0;
	    }
	 
	}

We need only to implement the matchSafely method which checks that the target is indeed a positive integer and the describeTo method which produces a failure message in case the test does not pass.

Here is a test that uses our new custom matcher:

	@Test
	public void givenInteger_whenAPositiveValue_thenCorrect() {
	    int num = 1;
	    assertThat(num, isAPositiveInteger());
	}

and here is a failure message we get since we have passed in a non-positive integer:

	java.lang.AssertionError: Expected: a positive integer but: was <-1>

## Conclusion ##

In this tutorial, we have explored the Hamcrest API and learnt how we can write better and more maintainable unit tests with it.

## Reference ##

[Testing with Hamcrest | Baeldung](https://www.baeldung.com/java-junit-hamcrest-guide)

[The Hamcrest Tutorial](https://github.com/hamcrest/JavaHamcrest/wiki/The-Hamcrest-Tutorial)


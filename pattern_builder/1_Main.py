from builder import PersonBuilder

#Note how each method returns self, allowing method chaining. This is called a fluent interface, and it’s commonly used with builders.

builder = PersonBuilder()
person = (
    builder
    .set_name("Alice")
    .set_age(30)
    .set_city("Berlin")
    .build()
)

print(person)
# Output: Person(name=Alice, age=30, city=Berlin)

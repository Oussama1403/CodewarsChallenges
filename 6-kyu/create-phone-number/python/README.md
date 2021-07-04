Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

<h3>Example:</h3>

```javascript
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
```
```cpp
createPhoneNumber(int[10]{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) // => returns "(123) 456-7890"
```
```crystal
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```
```ruby
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```
```coffeescript
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```
```java
Kata.createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) // => returns "(123) 456-7890"
```
```dart
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
```
```haskell
createPhoneNumber [1,2,3,4,5,6,7,8,9,0] -- => returns "(123) 456-7890"
```
```csharp
Kata.CreatePhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) // => returns "(123) 456-7890"
```
```python
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
```
```scala
Kata.createPhoneNumber(Seq(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)) # => returns "(123) 456-7890"
```
```php
createPhoneNumber([1,2,3,4,5,6,7,8,9,0]); // => returns "(123) 456-7890"
```
```f#
createPhoneNumber [1; 2; 3; 4; 5; 6; 7; 8; 9; 0] // => returns "(123) 456-7890"
```
```clojure
(create-phone-number [1 2 3 4 5 6 7 8 9 0]) ;; => returns "(123) 456-7890"
```
```rust
create_phone_number(&[1,2,3,4,5,6,7,8,9,0]); // returns "(123) 456-7890"
```
```go
CreatePhoneNumber([10]uint{1,2,3,4,5,6,7,8,9,0})  // returns "(123) 456-7890"
```
```c
create_phone_number(phnum, (const unsigned char[]){1,2,3,4,5,6,7,8,9,0});
    /* phnum <- "(123) 456-7890" */
```
```nasm
phnum:  resb 15
nums:   db  1,2,3,4,5,6,7,8,9,0

mov rdi, phnum
mov rsi, nums
call create_phone_number  ; RAX <- phnum <- "(123) 456-7890" 
```
```typescript
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"
```
```julia
createphonenumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # -> returns "(123) 456-7890"
```
```cfml
createPhoneNumber( [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] ) // => returns "(123) 456-7890"
```
```factor
{ 1 2 3 4 5 6 7 8 9 0 } create-phone-number ! returns "(123) 456-7890"
```

The returned format must be correct in order to complete this challenge. <br/>
Don't forget the space after the closing parentheses!
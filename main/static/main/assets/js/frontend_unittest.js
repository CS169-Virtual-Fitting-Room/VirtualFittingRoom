test("capitaliseFirstLetter single char Test", function(){
	var a= "a";
	ok("A"==capitaliseFirstLetter(a), "Passed!");
});
test("capitaliseFirstLetter single word Test", function(){
	var a= "apple";
	ok("Apple"==capitaliseFirstLetter(a), "Passed!");
});
test("capitaliseFirstLetter empty string Test", function(){
	var a= "";
	ok(""==capitaliseFirstLetter(a), "Passed!");
});
test("rendergrids Success Test", function(){
	ok(rendergrids(123,[],[],[],[]), "Passed!");
});
test("rendergrids Failed Test", function(){
	ok(!rendergrids("boy",[],123,[],"aaa"), "Passed!");
});
test("renderpage Success Test", function(){
	ok(renderpage("boy","what","girl",123), "Passed!");
});
test("renderpage Failed Test", function(){
	ok(!renderpage("boy",[],123,[]), "Passed!");
});
//iteration 2

test("rendercomments Failed Test With Wrong Input Type -- number and string are tested", function(){
	ok(!rendercomments(123), "Passed!");
	ok(!rendercomments("abc"), "Passed!");
});

test("rendercomments Success Input Type Test", function(){
	ok(rendercomments(["apple"]), "Passed!");
});


test("rendercomment Failed Test With Wrong Input Type", function(){
	ok(!rendercomment(12, "a", "a"), "Passed!");
	ok(!rendercomment("a", [], "a"), "Passed!");
	ok(!rendercomment("a", "a", 1), "Passed!");
});

test("rendercomment Success Input Type Test", function(){
	ok(rendercomment("aaa", "aaa", "aaa"), "Passed!");
});

test("renderwishlistelement Success Input Type Test", function(){
	ok(renderwishlistelement("a", "a","a", 12,12,"a"), "Passed!");
});

test("renderwishlist Failed Test With Wrong Input Type", function(){
	ok(!renderwishlist("a"), "Passed!");
	ok(!renderwishlist(12), "Passed!");
});

test("renderwishlistelement Success Input Type Test", function(){
	ok(renderwishlist([]), "Passed!");
});

test("clickContinueEvent Failed Test With Wrong Input Type", function(){
	ok(!clickContinueEvent([]), "Passed!");
	ok(!clickContinueEvent(12), "Passed!");
});












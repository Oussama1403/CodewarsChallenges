<div class="markdown prose max-w-5xl mx-auto" id="description"><p>The Vigenère cipher is a classic cipher originally developed by Italian cryptographer Giovan Battista Bellaso and published in 1553. It is named after a later French cryptographer Blaise de Vigenère, who had developed a stronger autokey cipher (a cipher that incorporates the message of the text into the key). </p>
<p>The cipher is easy to understand and implement, but survived three centuries of attempts to break it, earning it the nickname "le chiffre indéchiffrable" or "the indecipherable cipher."</p>
<p><a href="https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher" data-turbolinks="false" target="_blank">From Wikipedia</a>:</p>
<blockquote>
<p>The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution.</p>
<p>. . .</p>
<p>In a Caesar cipher, each letter of the alphabet is shifted along some number of places; for example, in a Caesar cipher of shift <code>3</code>, <code>A</code> would become <code>D</code>, <code>B</code> would become <code>E</code>, <code>Y</code> would become <code>B</code> and so on. The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.</p>
</blockquote>
<p>Assume the key is repeated for the length of the text, character by character. Note that some implementations repeat the key over characters only if they are part of the alphabet -- <strong>this is not the case here.</strong></p>
<p>The shift is derived by applying a Caesar shift to a character with the corresponding index of the key in the alphabet.</p>
<p>Visual representation:</p>
<pre><code class="language-javascript"><span class="cm-string">"my secret code i want to secure"</span>  <span class="cm-comment">// message</span>
<span class="cm-string">"passwordpasswordpasswordpasswor"</span>  <span class="cm-comment">// key</span>
</code></pre>
<p>Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.</p>
<h2 id="example">Example</h2>
<pre><code class="language-javascript"><span class="cm-keyword">var</span> <span class="cm-def">alphabet</span> <span class="cm-operator">=</span> <span class="cm-string">'abcdefghijklmnopqrstuvwxyz'</span>;
<span class="cm-keyword">var</span> <span class="cm-def">key</span> <span class="cm-operator">=</span> <span class="cm-string">'password'</span>;

<span class="cm-comment">// creates a cipher helper with each letter substituted</span>
<span class="cm-comment">// by the corresponding character in the key</span>
<span class="cm-keyword">var</span> <span class="cm-def">c</span> <span class="cm-operator">=</span> <span class="cm-keyword">new</span> <span class="cm-variable">VigenèreCipher</span>(<span class="cm-variable">key</span>, <span class="cm-variable">alphabet</span>);

<span class="cm-variable">c</span>.<span class="cm-property">encode</span>(<span class="cm-string">'codewars'</span>); <span class="cm-comment">// returns 'rovwsoiv'</span>
<span class="cm-variable">c</span>.<span class="cm-property">decode</span>(<span class="cm-string">'laxxhsj'</span>);  <span class="cm-comment">// returns 'waffles'</span>
</code></pre>
<p>Any character not in the alphabet must be left as is. For example (following from above):</p>
<pre><code class="language-javascript"><span class="cm-variable">c</span>.<span class="cm-property">encode</span>(<span class="cm-string">'CODEWARS'</span>); <span class="cm-comment">// returns 'CODEWARS'</span>
</code></pre>
</div>

<!--
author:    Masub.Makhdoom
email:     masub.makhdoom@ovgu.de
version:   0.0.1
language:  en
narrator:  US English Female
comment:   Template for SpeechRecognition-powered quizzes in LiaScript
logo:      logo.jpg

@SpeechRecognition.support
<script modify="false" run-once>
// Vendor prefix
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
if (!SpeechRecognition) {
  "LIASCRIPT: > 'Speech Recognition' not supported in this browser. Try Chrome, Opera, or Edge.";
} else {
  "LIASCRIPT: > Your browser does support 'Speech Recognition' ..."
}
</script>
@end

@SpeechRecognition
<script>
// Vendor prefix
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
if (!SpeechRecognition) {
  alert('SpeechRecognition not supported. Try Chrome, Opera, or Edge.');
} else {
  const recognition = new SpeechRecognition();
  recognition.lang = '@0';
  recognition.interimResults = false;
  recognition.continuous = false;

  const solution = "@1".toLowerCase()
    .replace(/(\.|\?|\!|\,|\-|\;)/g," ")
    .replace(/[ ]+/g," ")
    .trim();

  recognition.onresult = ev => {
    let t = ev.results[0][0].transcript?.toLowerCase().trim() || '';
    if (t === solution) {
      send.lia("true");
    } else {
      send.lia("Please try again …",[],false);
    }
  };
  recognition.onerror = ev => send.lia("Error: "+ev.error,[],false);
  recognition.onend   = () => console.log('Speech recognition ended.');
  recognition.start();
}
"LIA: wait"
</script>
@end

@SpeechRecognition.withFeedback
<script>
// Vendor prefix
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
if (!SpeechRecognition) {
  alert('SpeechRecognition not supported. Try Chrome, Opera, or Edge.');
} else {
  const recognition = new SpeechRecognition();
  recognition.lang = '@0';
  recognition.interimResults = false;
  recognition.continuous = false;

  const solution = "@1".toLowerCase()
    .replace(/(\.|\?|\!|\,|\-|\;)/g," ")
    .replace(/[ ]+/g," ")
    .trim();

  recognition.onresult = ev => {
    let t = ev.results[0][0].transcript?.toLowerCase().trim() || '';
    if (t === solution) {
      send.lia("true");
    } else {
      send.lia(t,[],false);
    }
  };
  recognition.onerror = ev => send.lia("Error: "+ev.error,[],false);
  recognition.onend   = () => console.log('Speech recognition ended.');
  recognition.start();
}
"LIA: wait"
</script>
@end
-->

# test
<!-- data-solution-button="off" -->
What about "Good morning" in German? 

[[!]]
@SpeechRecognition(de-DE,`Guten Morgen`)
---
How to pronounced "one" in german?

[[!]]
@SpeechRecognition(de-DE,`eins`)
---

How to pronounced "two" in german?

[[!]]
@SpeechRecognition(de-DE,`zwei`)

---

How to pronounced "three" in german?

[[!]]
@SpeechRecognition(de-DE,`drei`)
---

How to pronounced "four" in german?

[[!]]
@SpeechRecognition(de-DE,`vier`)
---

How to pronounced "five" in german?

[[!]]
@SpeechRecognition(de-DE,`fünf`)

---

How to pronounced "six" in german?

[[!]]
@SpeechRecognition(de-DE,`sechs`)
---

How to pronounced "seven" in german?

[[!]]
@SpeechRecognition(de-DE,`sieben`)
---

How to pronounced "Eight" in german?

[[!]]
@SpeechRecognition(de-DE,`acht`)
---

How to pronounced "nine" in german?

[[!]]
@SpeechRecognition(de-DE,`neun`)
---

How to pronounced "Ten" in german?

[[!]]
@SpeechRecognition(de-DE,`zehn`)
---

How to pronounced "Twenty" in german?

[[!]]
@SpeechRecognition(de-DE,`zwanzig`)
---

How to pronounced "Thirty" in german?

[[!]]
@SpeechRecognition(de-DE,`dreißig`)
---

How to pronounced "fourty" in german?

[[!]]
@SpeechRecognition(de-DE,`vierzig`)
---

How to pronounced "fifty" in german?

[[!]]
@SpeechRecognition(de-DE,`fünfzig`)
---

How to pronounced "sixty" in german?

[[!]]
@SpeechRecognition(de-DE,`sechzig`)
---

How to pronounced "seventy" in german?

[[!]]
@SpeechRecognition(de-DE,`siebzig`)
---

How to pronounced "eighty" in german?

[[!]]
@SpeechRecognition(de-DE,`achtzig`)
---

How to pronounced "ninty" in german?

[[!]]
@SpeechRecognition(de-DE,`neunzig`)
---

How to pronounced "hundred" in german?

[[!]]
@SpeechRecognition(de-DE,`hundert`)
---
















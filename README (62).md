<!--

author: André Dietrich

email:  LiaScript@web.de

logo:   media/logo.jpg

script: https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js

import: https://raw.githubusercontent.com/liaTemplates/ABCjs/main/README.md

@CSV
<script run-once style="display:block" modify="false">
async function csvToMarkdownTable(csvFile) {
  const response = await fetch(csvFile);
  const text = await response.text();
  const rows = Papa.parse(text).data;
  let markdownTable = "| " + rows[0].join(" | ") + " |\n"; // Header
  markdownTable += "| " + rows[0].map(() => "---").join(" | ") + " |\n"; // Separator
  for (let i = 1; i < rows.length; i++) {
    if (rows[i].length === rows[0].length) {
      markdownTable += "| " + rows[i].join(" | ") + " |\n";
    }
  }
  send.lia("LIASCRIPT: <!-- data-type='none' --" + ">" + markdownTable);
}
csvToMarkdownTable("@0")
"LIA: wait"
</script>
@end

@WebSerial
<script>
(async function() {
  // Check if the Web Serial API is supported.
  if (!("serial" in navigator)) {
    console.error("Web Serial API is not supported in this browser.");
    return;
  }

  // Declare connection-related variables for later cleanup.
  let port = null;
  let reader = null;

  try {
    // Request and open the serial port.
    port = await navigator.serial.requestPort();
    await port.open({ baudRate: 115200 });

    // Create a TextEncoder instance.
    const encoder = new TextEncoder();
    // Function to stop any currently running code by sending Ctrl-C.
    async function stopCurrentProgram() {
      try {
        const writer = port.writable.getWriter();
        // Send Ctrl-C (ASCII 0x03) to interrupt any running code.
        await writer.write(encoder.encode("\x03"));
        // Wait briefly to allow the interrupt to be processed.
        await new Promise(resolve => setTimeout(resolve, 100));
        // Send a second Ctrl-C in case the first one was missed.
        await writer.write(encoder.encode("\x03"));
        writer.releaseLock();
      } catch (e) {
        console.error("Error sending Ctrl-C:", e);
      }
    }

    // Stop any running code before sending new code.
    await stopCurrentProgram();

    // Retrieve the entire Python code from the liascript input.
    const pythonCode = `@input(0)`;

    // Function to send code using MicroPython's paste mode.
    // In paste mode, the REPL buffers all lines until Ctrl‑D is received,
    // then it compiles and executes the entire code block at once.
    async function sendCodeInPasteMode(code) {
      const writer = port.writable.getWriter();
      // Enter paste mode (Ctrl‑E, ASCII 0x05).
      await writer.write(encoder.encode("\x05"));
      // Wait briefly for paste mode to be activated.
      await new Promise(resolve => setTimeout(resolve, 100));

      // Split the code into lines, preserving all indentation.
      const codeLines = code.split(/\r?\n/);
      for (const line of codeLines) {
        // Send each line exactly as-is, with CR+LF.
        await writer.write(encoder.encode(line + "\r\n"));
      }
      // Exit paste mode by sending Ctrl‑D (ASCII 0x04).
      await writer.write(encoder.encode("\x04"));
      writer.releaseLock();
      send.lia("LIA: terminal");
    }

    // Function that sends the code and reads output until the REPL prompt (">>>") is detected.
    // This ensures the entire block is executed before further input is allowed.
    async function sendCodeAndWaitForPrompt(code) {
      await sendCodeInPasteMode(code);
      let outputBuffer = "";
      const tempReader = port.readable.getReader();
      const decoder = new TextDecoder();
      let promptFound = false;

      while (!promptFound) {
        const { value, done } = await tempReader.read();
        if (done) break;
        if (value) {
          const text = decoder.decode(value);
          outputBuffer += text;
          console.stream(text);
          // Look for the REPL prompt (adjust if your prompt differs).
          if (outputBuffer.includes(">>>")) {
            promptFound = true;
          }
        }
      }
      await tempReader.releaseLock();
      return outputBuffer;
    }

    // Send the Python code and wait until the prompt is detected.
    await sendCodeAndWaitForPrompt(pythonCode);
    console.log("Python code executed and prompt detected.");

    // Now that execution is complete, enable terminal input.
    send.lia("LIA: terminal");

    // Start a global read loop to capture and display subsequent output.
    reader = port.readable.getReader();
    const globalDecoder = new TextDecoder();
    (async function readLoop() {
      try {
        while (true) {
          const { value, done } = await reader.read();
          if (done) {
            console.debug("Stream closed");
            send.lia("LIA: stop");
            break;
          }
          if (value) {
            console.stream(globalDecoder.decode(value));
          }
        }
      } catch (error) {
        console.error("Read error:", error);
      } finally {
        try { reader.releaseLock(); } catch (e) { /* ignore */ }
      }
    })();

    // Handler to send terminal input lines to MicroPython.
    send.handle("input", input => {
      (async function() {
        try {
          const writer = port.writable.getWriter();
          // Send the terminal input (preserving any whitespace) with CR+LF.
          await writer.write(encoder.encode(input + "\r\n"));
          writer.releaseLock();
        } catch (e) {
          console.error("Error sending input to MicroPython:", e);
        }
      })();
    });

    // Handler to clean up all connections and variables when a "stop" command is received.
    send.handle("stop", async () => {
      console.log("Cleaning up connections and stopping execution.");

      // Cancel the reader if it exists.
      if (reader) {
        try {
          await reader.cancel();
        } catch (e) {
          console.error("Error canceling reader:", e);
        }
        try { reader.releaseLock(); } catch (e) { /* ignore */ }
      }

      // Close the serial port if it's open.
      if (port) {
        try {
          await port.close();
        } catch (e) {
          console.error("Error closing port:", e);
        }
      }

      // Reset connection variables.
      port = null;
      reader = null;
      console.log("Cleanup complete.");
    });

  } catch (error) {
    console.error("Error connecting to the MicroPython device:", error);
    send.lia("LIA: stop");
  }
})();

"LIA: wait"
</script>
@end

@WebSerial2
<script>
(async function() {
  // Check if the Web Serial API is supported.
  if (!("serial" in navigator)) {
    console.error("Web Serial API is not supported in this browser.");
    return;
  }

  // Declare connection-related variables for later cleanup.
  let port = null;
  let reader = null;

  try {
    // First, check if a port was previously granted.
    const ports = await navigator.serial.getPorts();
    if (ports.length > 0) {
      port = ports[0];
      console.log("Reusing previously granted port.");
    } else {
      // If no port is available, request a new one.
      port = await navigator.serial.requestPort();
    }

    // Open the port at the typical MicroPython baud rate.
    await port.open({ baudRate: 115200 });

    // Create a TextEncoder instance.
    const encoder = new TextEncoder();

    // Function to stop any currently running code by sending Ctrl-C.
    async function stopCurrentProgram() {
      try {
        const writer = port.writable.getWriter();
        // Send Ctrl-C (ASCII 0x03) to interrupt any running code.
        await writer.write(encoder.encode("\x03"));
        // Wait briefly to allow the interrupt to be processed.
        await new Promise(resolve => setTimeout(resolve, 100));
        // Send a second Ctrl-C in case the first was missed.
        await writer.write(encoder.encode("\x03"));
        writer.releaseLock();
      } catch (e) {
        console.error("Error sending Ctrl-C:", e);
      }
    }

    // Stop any running code before sending new code.
    await stopCurrentProgram();

    // Retrieve the entire Python code from the liascript input.
    const pythonCode = `@input(0)`;

    // Function to send code using MicroPython's paste mode.
    // In paste mode, the REPL buffers all lines until Ctrl‑D is received,
    // then it compiles and executes the entire code block at once.
    async function sendCodeInPasteMode(code) {
      const writer = port.writable.getWriter();
      // Enter paste mode (Ctrl‑E, ASCII 0x05).
      await writer.write(encoder.encode("\x05"));
      // Wait briefly for paste mode to be activated.
      await new Promise(resolve => setTimeout(resolve, 100));
      
      // Split the code into lines, preserving all indentation.
      const codeLines = code.split(/\r?\n/);
      for (const line of codeLines) {
        // Send each line exactly as-is, with CR+LF.
        await writer.write(encoder.encode(line + "\r\n"));
      }
      // Exit paste mode by sending Ctrl‑D (ASCII 0x04).
      await writer.write(encoder.encode("\x04"));
      writer.releaseLock();
      send.lia("LIA: terminal");
    }

    // Function that sends the code and reads output until the REPL prompt (">>>") is detected.
    // This ensures the entire block is executed before further input is allowed.
    async function sendCodeAndWaitForPrompt(code) {
      await sendCodeInPasteMode(code);
      let outputBuffer = "";
      const tempReader = port.readable.getReader();
      const decoder = new TextDecoder();
      let promptFound = false;
      
      while (!promptFound) {
        const { value, done } = await tempReader.read();
        if (done) break;
        if (value) {
          const text = decoder.decode(value);
          outputBuffer += text;
          console.stream(text);
          // Look for the REPL prompt (adjust if your prompt differs).
          if (outputBuffer.includes(">>>")) {
            promptFound = true;
          }
        }
      }
      await tempReader.releaseLock();
      return outputBuffer;
    }

    // Send the Python code and wait until the prompt is detected.
    await sendCodeAndWaitForPrompt(pythonCode);
    console.log("Python code executed and prompt detected.");

    // Now that execution is complete, enable terminal input.
    send.lia("LIA: terminal");

    // Start a global read loop to capture and display subsequent output.
    reader = port.readable.getReader();
    const globalDecoder = new TextDecoder();
    (async function readLoop() {
      try {
        while (true) {
          const { value, done } = await reader.read();
          if (done) {
            console.debug("Stream closed");
            send.lia("LIA: stop");
            break;
          }
          if (value) {
            console.stream(globalDecoder.decode(value));
          }
        }
      } catch (error) {
        console.error("Read error:", error);
      } finally {
        try { reader.releaseLock(); } catch (e) { /* ignore */ }
      }
    })();

    // Handler to send terminal input lines to MicroPython.
    send.handle("input", input => {
      (async function() {
        try {
          const writer = port.writable.getWriter();
          // Send the terminal input (preserving any whitespace) with CR+LF.
          await writer.write(encoder.encode(input + "\r\n"));
          writer.releaseLock();
        } catch (e) {
          console.error("Error sending input to MicroPython:", e);
        }
      })();
    });

    // Handler to clean up all connections and variables when a "stop" command is received.
    send.handle("stop", async () => {
      console.log("Cleaning up connections and stopping execution.");

      // Cancel the reader if it exists.
      if (reader) {
        try {
          await reader.cancel();
        } catch (e) {
          console.error("Error canceling reader:", e);
        }
        try { reader.releaseLock(); } catch (e) { /* ignore */ }
      }

      // Close the serial port if it's open.
      if (port) {
        try {
          await port.close();
        } catch (e) {
          console.error("Error closing port:", e);
        }
      }

      // Reset connection variables.
      port = null;
      reader = null;
      console.log("Cleanup complete.");
    });

  } catch (error) {
    console.error("Error connecting to the MicroPython device:", error);
    send.lia("LIA: stop");
  }
})();

"LIA: wait"
</script>
@end

@style
@keyframes burn {
  0% {
    text-shadow: 0 0 5px #ff0, 0 0 10px #ff0, 0 0 15px #f00, 0 0 20px #f00,
      0 0 25px #f00, 0 0 30px #f00, 0 0 35px #f00;
  }
  50% {
    text-shadow: 0 0 10px #ff0, 0 0 15px #ff0, 0 0 20px #ff0, 0 0 25px #f00,
      0 0 30px #f00, 0 0 35px #f00, 0 0 40px #f00;
  }
  100% {
    text-shadow: 0 0 5px #ff0, 0 0 10px #ff0, 0 0 15px #f00, 0 0 20px #f00,
      0 0 25px #f00, 0 0 30px #f00, 0 0 35px #f00;
  }
}

.burning-text {
  font-weight: bold;
  color: #fff;
  animation: burn 1.5s infinite alternate;
}
@end

@burn: <span class="burning-text">@0</span>

-->

# Understanding Turnitin 
Mahwish Kanwal 
07-April-2025
# What is Turnitin?


    --{{0}}--
!?[](media/liascript_0.webm)
Turnitin® is a tool that students and instructors can use to identify potential instances of plagiarism. When you submit your paper to Turnitin®, you will get a similarity report that should be reviewed carefully so you can make any needed revisions to your paper.  
(Writing Center UAGC, 2025)

# What Does Turnitin Do?

    --{{0}}--
!?[](media/liascript_0.webm)
Turnitin® highlights sentences or phrases that are similar to works or papers that have already been published, submitted, or found online. Similarity is not always the same as plagiarism.

!?[](https://github.com/Masub27/Quantitative-Research-/blob/main/Research%20Question2.mp4?raw=true)

* Turnitin® highlights sentences or phrases that are similar to works or papers that have already been published, submitted, or found online. Similarity is not always the same as plagiarism. You might have something similar in your paper to what has been published, such as a direct quote, but this does not always mean that you have plagiarized. If you have put quotation marks around that direct quote, and you’ve cited it, you have not plagiarized. Items on your references list are also going to show up as similar, but because these are citations, these similarities do not equal plagiarism.
* If the highlighted area in your similarity report contains information or wording that you have obtained from a source, be sure you have properly summarized, paraphrased, or quoted that material and you have cited the source. If you do not cite outside sources, it is considered plagiarizing.                                                                 

     (Writing Center UAGC, 2025)

# How to Register for Turnitin? 
# Step 1
https://www.turnitin.com/?svr=6&lang=de&r=60.0321490546044

Click on Login.  
![](https://github.com/Masub27/Intro/blob/main/Picture160.png?raw=true)
# Step 2
* Click on New User as mentioned (Click here) 

![](https://github.com/Masub27/Intro/blob/main/Picture61.png?raw=true)

# Step 3
* Click on Student.
![](https://github.com/Masub27/Intro/blob/main/Picture62.png?raw=true)

# Step 4
* Create New student profile.
* Fill in relevant information.
* Use your OVGU email address only. 
* You can choose any ONE course for creating student’s profile.  
* You have to create student’s profile only ONCE.
* Once the student’s profile is created you can enrol in any course you want through simple Login. (See step 5 in next slide)
* The Class IDs and Class Enrolment Keys for all courses will be shared through email.
![](https://github.com/Masub27/Intro/blob/main/Picture63.png?raw=true)


# Step 5
* To Enroll in a course after the student’s profile have been created.
* Use the link below:
* https://www.turnitin.com/?svr=6&lang=de&r=60.0321490546044
*  Use you email address and password which you used for Turnitin account.
* Click Login
![](https://github.com/Masub27/Intro/blob/main/Picture64.png?raw=true)
 
# How do I Upload Assignments or Presentations on Turnitin? 
 ## Guidelines for uploading assignments on Turnitin
  ### Accessing Turnitin
 You can log in to Turnitin using the following link: Turnitin Login.

 ### Enrolling in Your Class
After logging in, you will need to enroll in your designated class by entering the Class ID and the corresponding Enrollment Key.Note: Class IDs and Enrollment Keys are updated each semester, so ensure you have the correct information for the current semester.

 #### Uploading Assignments and Presentations
All assignments and presentations for your respective courses must be uploaded to Turnitin before submitting them to your professors. This ensures your work is properly checked for originality.

# Guidelines for uploading assignments on Turnitin 

 #### Submission Deadline
Once the submission deadline has passed, the submission portal will automatically close. Please make sure to upload your work on time.

 #### Upload Limitations
You are allowed a maximum of two uploads per assignment. Please review your file carefully before submitting, as additional uploads will not be accepted after the second one.

 #### Turnitin Similarity Report
After uploading, Turnitin will generate a similarity report. You can view this report to assess the originality of your work.Please review the report carefully and make any necessary revisions to your document before submitting again.
# Guidelines for uploading assignments on Turnitin 
 ## No Deletions
Once an assignment is uploaded to Turnitin, it cannot be deleted. Please ensure that the file you upload is final before submitting it.

 ### File Format Requirements
Turnitin supports common file formats like Word .docx, and Power points .pptx. Ensure your assignment is uploaded in one of these formats.

 #### Group Submissions
If your assignment or presentation is a group project, only one group member should upload the final presentation or assignment on behalf of all members. Uploading multiple versions may be flagged as plagiarism.Make sure to include the names of all group members in the uploaded document to ensure proper grading.
# Dealing with Queries and Issues
* If you experience any issues while uploading your assignment, please contact the following email for assistance.
* masub.makhdoom@ovgu.de
* mahwish.kanwal@ovgu.de
* Please do not share your queries via WhatsApp such as sharing screenshots etc. because this your confidential information and must not be shared on WhatsApp. 


# Information for Registration on Turnitin

* You can use the following link to register for Turnitin accounts
* https://www.turnitin.com/?svr=6&lang=de&r=60.0321490546044
* You can use any ONE Class ID and Enrolment Key from the following for creating your Turnitin accounts.
* The Class ID and Enrolment Key for all courses are given below.
* Once you have registered for Turnitin account you can enrol yourself in all the classes. 

> Enrolment Key:  ITVETSS25

__Module 4: International Comparative Technical and Vocational Education and Training__

~~Seminar:International Vocational Education I ~~

Class ID: 48255252

Enrolment Key: ITVETSS25

~~Seminar:International Vocational Education II ~~

Class ID: 48255280

Enrolment Key: ITVETSS25

# Information for Registration on Turnitin

__Module 5: Management and evaluation of International Technical and Vocational Education and Training__

~~Seminar:Quality Management ~~

Class ID: 48255304

Enrolment Key: ITVETSS25

~~Seminar:Vocational Education Management ~~

Class ID: 48255318

Enrolment Key: ITVETSS25

__Module 6: Curriculum and Media development__

~~Seminar:Development of Curricula ~~

Class ID: 48255329

Enrolment Key: ITVETSS25

~~Seminar:Action Fields of TVET Trainers ~~

Class ID: 48255342

Enrolment Key: ITVETSS25

# Information for Registration on Turnitin

> Specialization Modules 

__WPF Module 1: Organizational and Human Resource Development__

~~Seminar:Organizational and Human Resource Development I~~ 

Class ID: 48255371

Enrolment Key: ITVETSS25

~~Seminar:Organizational and Human Resource Development II~~

Class ID: 48255379

Enrolment Key: ITVETSS25

__WPF Module 2:  Vocational training for sustainable development__

~~Seminar:Didactics for Sustainable Development ~~

Class ID : 48255389

Enrolment Key: ITVETSS25

~~Seminar:Vocational Education for Sustainable Development~~

Class ID : 48255399

Enrolment Key: ITVETSS25

# Information for Registration on Turnitin

__WPF Module 3: Methods of In-Company Training __

~~Seminar:Methods of Vocational Training ~~

Class ID: 48255405

Enrolment Key: ITVETSS25

~~Seminar: Workshop Methods of In-Company Training ~~

Class ID : 48255417

Enrolment Key: ITVETSS25

__WPF Module 4: Research Methods__

~~Seminar:Qualitative Research Methods ~~

Class ID: 48255425

Enrolment Key: ITVETSS25

~~Seminar: Introduction in Research and Academic Writing ~~

Class ID: 48255443

Enrolment Key: ITVETSS25




~~Seminar: Quantitative Research Methods~~

Class ID: 48255425

Enrolment Key: ITVETSS25






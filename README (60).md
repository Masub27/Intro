<!--
author:   Masub Makhdoom
email:    masub.makhdoom@ovgu.de & mahwish.kanwal@ovgu.de
date:     13/08/2026
version:  31.0.0
language: en
narrator: UK English Female

repository: https://github.com/LiaScript/docs

logo:     img/logo.png

comment:  Windows version of the LiaScript-to-Android WebView training.

script:   https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js
          https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

link:     https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css
link:     https://raw.githubusercontent.com/OVGU-VET-TechEd/Integrating_AI_in_TVET_UNESCO/refs/heads/main/VorlageUN.css
link:     https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css

import:   https://raw.githubusercontent.com/liaTemplates/ABCjs/main/README.md

link:     https://fonts.googleapis.com/css2?family=Noto+Sans+Egyptian+Hieroglyphs
          https://fonts.googleapis.com/css2?family=Noto+Sans+Ogham

font:     Noto Sans Egyptian Hieroglyphs, Noto Sans Ogham
-->

# Training: Create a Latest Android App for a LiaScript Course — Windows

## 1. Final App Idea

```text
LiaScript course
→ GitHub Pages web app
→ Android Studio WebView app
→ APK file
→ Android phone
```

This Windows version uses the same method as the Mac version: the Android app opens the published LiaScript course from GitHub Pages inside an Android WebView.

---

# Part A: Install Required Software

## 2. Required Tools

```text
1. Windows 10 or Windows 11
2. Android Studio
3. Android SDK
4. Microsoft OpenJDK 17
5. Gradle
6. Kotlin
7. GitHub Pages course link
8. Android phone
9. USB cable or file transfer method
10. Internet connection
```

---

## 3. Install Android Studio on Windows

Open:

```text
https://developer.android.com/studio
```

Steps:

```text
1. Click Download Android Studio
2. Accept the terms
3. Download the Windows .exe installer
4. Open the installer
5. Keep Android Studio and Android SDK selected
6. Complete the installation
7. Open Android Studio
```

---

## 4. Install Android SDK

When Android Studio opens:

```text
1. Complete the first-time setup
2. Choose Standard installation
3. Let Android Studio install the Android SDK and Build Tools
4. Wait until installation finishes
5. Click Finish
```

The Android SDK is normally here:

```text
C:\Users\YOUR_USERNAME\AppData\Local\Android\Sdk
```

Portable Windows form:

```text
%LOCALAPPDATA%\Android\Sdk
```

Open **Command Prompt (CMD)** and run:

```cmd
dir "%LOCALAPPDATA%\Android\Sdk"
```

You should see folders such as:

```text
build-tools
platform-tools
platforms
sources
```

---

## 5. Install Java 17

Download Microsoft OpenJDK 17:

```text
https://learn.microsoft.com/en-us/java/openjdk/download
```

Choose:

```text
OpenJDK 17
Windows x64
MSI
```

Install it.

Close Command Prompt and open a new Command Prompt.

Run:

```cmd
dir "C:\Program Files\Microsoft" /ad /b
```

You should see a folder similar to:

```text
jdk-17.0.xx.x-hotspot
```

Set Java 17:

```cmd
for /d %D in ("C:\Program Files\Microsoft\jdk-17*") do set "JAVA_HOME=%D"
```

Then:

```cmd
set "PATH=%JAVA_HOME%\bin;%PATH%"
```

Check:

```cmd
java -version
```

It should show Java 17.

---

# Part B: Prepare LiaScript Course

## 6. Prepare the LiaScript Course

Example file:

```text
A1_Part_1_Chapter_1_2.md
```

The course can contain:

```text
Lessons
Text
Images
Audio
Video
Quizzes
Exercises
```

---

## 7. Publish the LiaScript Course on GitHub Pages

For this WebView method, publish the LiaScript course online.

Example course link:

```text
https://masub27.github.io/a1-iphone-part1/
```

Open the link in Chrome first and make sure the course loads correctly.

---

## 8. Why GitHub Pages Is Used

The Android app loads the LiaScript course from GitHub Pages.

This avoids the earlier white-screen problem that occurred when local LiaScript files were loaded directly inside Android WebView.

The app therefore needs internet access.

---

# Part C: Create Android Studio Project

## 9. Create a New Android Project

Open Android Studio.

Choose:

```text
New Project
→ Empty Views Activity
```

Use:

```text
Project name: A1.1 German Part 1
Package name: io.github.masubmakhdoom.a1part1modern
Language: Kotlin
Minimum SDK: 23
```

Example project location:

```text
C:\Users\YOUR_USERNAME\AndroidStudioProjects\A11GermanPart1
```

Click:

```text
Finish
```

Wait for Gradle Sync.

---

## 10. Open the Project Folder in CMD

Open Command Prompt:

```cmd
cd /d "%USERPROFILE%\AndroidStudioProjects\A11GermanPart1"
```

Check:

```cmd
dir
```

You should see files such as:

```text
app
gradle
gradlew
gradlew.bat
settings.gradle.kts
```

---

# Part D: Gradle Configuration

## 11. Project-Level Gradle File

In Android Studio open:

```text
build.gradle.kts
```

Replace its content with:

```kotlin
plugins {
    id("com.android.application") version "8.7.3" apply false
    id("org.jetbrains.kotlin.android") version "2.0.21" apply false
}
```

Important:

```text
Do not put android { ... } inside this project-level file.
```

Save the file.

Click:

```text
Sync Now
```

---

## 12. App-Level Gradle File

Open:

```text
app/build.gradle.kts
```

Replace its content with:

```kotlin
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "io.github.masubmakhdoom.a1part1modern"
    compileSdk = 35

    defaultConfig {
        applicationId = "io.github.masubmakhdoom.a1part1modern"
        minSdk = 23
        targetSdk = 35
        versionCode = 1
        versionName = "1.0"
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
}

kotlin {
    jvmToolchain(17)
}
```

Save.

Click:

```text
Sync Now
```

---

## 13. Gradle Settings

```text
namespace
```

Internal package name.

```text
compileSdk = 35
```

Compile using Android SDK 35.

```text
targetSdk = 35
```

Target Android SDK 35.

```text
minSdk = 23
```

Support Android 6.0 and newer.

```text
JavaVersion.VERSION_17
jvmToolchain(17)
```

Use Java 17 for Java and Kotlin.

---

# Part E: Theme

## 14. Normal Theme

Open:

```text
app/src/main/res/values/themes.xml
```

Replace the content with:

```xml
<resources>
    <style name="Theme.A11GermanPart1" parent="@android:style/Theme.Material.Light.NoActionBar">
        <item name="android:windowNoTitle">true</item>
        <item name="android:windowActionBar">false</item>
        <item name="android:windowLightStatusBar">true</item>
        <item name="android:statusBarColor">#FFFFFF</item>
        <item name="android:navigationBarColor">#FFFFFF</item>
    </style>
</resources>
```

---

## 15. Dark Theme

Open:

```text
app/src/main/res/values-night/themes.xml
```

If `values-night` does not exist:

```text
Right-click res
→ New
→ Android Resource Directory
→ Directory name: values-night
→ OK
```

Use:

```xml
<resources>
    <style name="Theme.A11GermanPart1" parent="@android:style/Theme.Material.NoActionBar">
        <item name="android:windowNoTitle">true</item>
        <item name="android:windowActionBar">false</item>
        <item name="android:statusBarColor">#000000</item>
        <item name="android:navigationBarColor">#000000</item>
    </style>
</resources>
```

---

# Part F: Android Manifest

## 16. Replace AndroidManifest.xml

Open:

```text
app/src/main/AndroidManifest.xml
```

Replace with:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-permission android:name="android.permission.INTERNET" />

    <application
        android:allowBackup="true"
        android:supportsRtl="true"
        android:theme="@style/Theme.A11GermanPart1"
        android:label="A1 German Modern Online">

        <activity
            android:name=".MainActivity"
            android:exported="true">

            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>

        </activity>

    </application>

</manifest>
```

Internet permission:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

This is required because the app loads the online LiaScript course.

---

# Part G: MainActivity WebView

## 17. Replace MainActivity.kt

Open:

```text
app/src/main/java/io/github/masubmakhdoom/a1part1modern/MainActivity.kt
```

Replace all content with:

```kotlin
package io.github.masubmakhdoom.a1part1modern

import android.annotation.SuppressLint
import android.app.Activity
import android.os.Bundle
import android.webkit.WebChromeClient
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient

class MainActivity : Activity() {

    private lateinit var webView: WebView

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        webView = WebView(this)
        setContentView(webView)

        webView.webViewClient = WebViewClient()
        webView.webChromeClient = WebChromeClient()

        val settings: WebSettings = webView.settings
        settings.javaScriptEnabled = true
        settings.domStorageEnabled = true
        settings.databaseEnabled = true
        settings.allowFileAccess = true
        settings.allowContentAccess = true
        settings.mediaPlaybackRequiresUserGesture = false
        settings.cacheMode = WebSettings.LOAD_DEFAULT
        settings.mixedContentMode = WebSettings.MIXED_CONTENT_ALWAYS_ALLOW

        webView.loadUrl("https://masub27.github.io/a1-iphone-part1/")
    }

    @Deprecated("Deprecated in Java")
    override fun onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack()
        } else {
            super.onBackPressed()
        }
    }
}
```

If your GitHub Pages URL is different, change:

```kotlin
webView.loadUrl("https://masub27.github.io/a1-iphone-part1/")
```

---

# Part H: Set Java 17 in Android Studio

## 18. Gradle JDK

Open:

```text
File
→ Settings
→ Build, Execution, Deployment
→ Build Tools
→ Gradle
```

Find:

```text
Gradle JDK
```

Select Microsoft Java 17.

Example:

```text
C:\Program Files\Microsoft\jdk-17...
```

Click:

```text
Apply
→ OK
```

Wait for Gradle Sync.

---

# Part I: Build the APK

## 19. Build from Android Studio

Open:

```text
Build
→ Generate Bundle(s) / APK(s)
→ Generate APK(s)
```

Wait until the build finishes.

Click:

```text
Locate
```

The debug APK is normally here:

```text
app\build\outputs\apk\debug\app-debug.apk
```

---

## 20. Build from Command Prompt

Open CMD:

```cmd
cd /d "%USERPROFILE%\AndroidStudioProjects\A11GermanPart1"
```

Set Java 17:

```cmd
for /d %D in ("C:\Program Files\Microsoft\jdk-17*") do set "JAVA_HOME=%D"
```

```cmd
set "PATH=%JAVA_HOME%\bin;%PATH%"
```

Check:

```cmd
java -version
```

Check Gradle:

```cmd
gradlew.bat -version
```

Build:

```cmd
gradlew.bat clean
```

Then:

```cmd
gradlew.bat assembleDebug
```

Wait for:

```text
BUILD SUCCESSFUL
```

---

## 21. Copy APK to Desktop

Run:

```cmd
copy "app\build\outputs\apk\debug\app-debug.apk" "%USERPROFILE%\Desktop\A1_German_Modern_Online.apk"
```

Check:

```cmd
dir "%USERPROFILE%\Desktop\A1_German_Modern_Online.apk"
```

Final APK:

```text
A1_German_Modern_Online.apk
```

---

# Part J: Install on Android Phone

## 22. Transfer APK

Transfer:

```text
A1_German_Modern_Online.apk
```

using:

```text
USB cable
Google Drive
Telegram
WhatsApp document
USB flash drive
```

---

## 23. Allow Unknown Apps

If Android blocks installation:

```text
Settings
→ Security
→ Install unknown apps
→ Allow from this source
```

Install again.

---

## 24. Install with ADB

Enable Developer Options and USB debugging.

Connect the phone.

Check:

```cmd
"%LOCALAPPDATA%\Android\Sdk\platform-tools\adb.exe" devices
```

Install:

```cmd
"%LOCALAPPDATA%\Android\Sdk\platform-tools\adb.exe" install "%USERPROFILE%\Desktop\A1_German_Modern_Online.apk"
```

If already installed:

```cmd
"%LOCALAPPDATA%\Android\Sdk\platform-tools\adb.exe" install -r "%USERPROFILE%\Desktop\A1_German_Modern_Online.apk"
```

Successful result:

```text
Success
```

---

# Part K: Testing

## 25. Test

```text
1. App opens
2. Course loads
3. No white screen
4. Audio works
5. Video works
6. Links work
7. Quizzes work
8. Back button works
9. Screen size is readable
10. Internet is connected
```

---

# Part L: Common Windows Errors

## 26. Error: ./gradlew Does Not Work

On Windows do not use:

```text
./gradlew
```

Use:

```cmd
gradlew.bat assembleDebug
```

---

## 27. Error: Unsupported Class File Major Version 69

Check:

```cmd
java -version
```

Use Java 17:

```cmd
for /d %D in ("C:\Program Files\Microsoft\jdk-17*") do set "JAVA_HOME=%D"
```

```cmd
set "PATH=%JAVA_HOME%\bin;%PATH%"
```

Then:

```cmd
java -version
```

and:

```cmd
gradlew.bat -version
```

For this project, Gradle should use Java 17.

---

## 28. Error: MaterialComponents Theme Not Found

Use the built-in Android themes shown earlier in:

```text
values/themes.xml
values-night/themes.xml
```

---

## 29. Error: JVM Target Mismatch

Use:

```kotlin
compileOptions {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}

kotlin {
    jvmToolchain(17)
}
```

Also set Android Studio's Gradle JDK to Java 17.

---

## 30. Error: White Screen

First test the GitHub Pages URL in Chrome.

Check:

```kotlin
webView.loadUrl("https://masub27.github.io/a1-iphone-part1/")
```

Also make sure the manifest contains:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

---

## 31. Error: Android SDK Not Found

Run:

```cmd
dir "%LOCALAPPDATA%\Android\Sdk"
```

If it does not exist:

```text
Android Studio
→ Tools
→ SDK Manager
```

Check the actual Android SDK Location.

---

# Part M: Final Result

The final app uses:

```text
Kotlin
Android WebView
GitHub Pages
LiaScript
compileSdk 35
targetSdk 35
minSdk 23
Java 17
```

Final APK:

```text
A1_German_Modern_Online.apk
```

Installed app name:

```text
A1 German Modern Online
```

Complete Windows process:

```text
Install Android Studio
→ Install Android SDK
→ Install Java 17
→ Publish LiaScript on GitHub Pages
→ Create Android Studio project
→ Configure Gradle
→ Add themes
→ Add Internet permission
→ Add WebView MainActivity
→ Set Gradle JDK to Java 17
→ Build APK
→ Copy APK
→ Install on Android phone
→ Test
```

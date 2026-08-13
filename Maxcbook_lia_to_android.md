<!--

author:   Masub Makhdoom
email:    masub.makhdoom@ovgu.de & mahwish.kanwal@ovgu.de
date:     27/01/2026
version:  30.0.0
language: en
narrator: UK English Female

repository: https://github.com/LiaScript/docs

logo:     img/logo.png

comment:  This document shall provide an entire compendium and course on the
          development of Open-courSes with [LiaScript](https://LiaScript.github.io).
          As the language and the systems grows, also this document will be updated.
          Feel free to fork or copy it, translations are very welcome...

script:   https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js
          https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

link:     https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css

link: https://raw.githubusercontent.com/OVGU-VET-TechEd/Integrating_AI_in_TVET_UNESCO/refs/heads/main/VorlageUN.css

link:     https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css

import:   https://raw.githubusercontent.com/liaTemplates/ABCjs/main/README.md

link:     https://fonts.googleapis.com/css2?family=Noto+Sans+Egyptian+Hieroglyphs
          https://fonts.googleapis.com/css2?family=Noto+Sans+Ogham

font:     Noto Sans Egyptian Hieroglyphs, Noto Sans Ogham

-->

# Training: Create a Latest Android App for a LiaScript Course

## 1. Learning Goal

In this training, you will learn how to create a **modern Android app** for a LiaScript course.

The app will:

* open a LiaScript course inside an Android app
* use Android WebView
* use Kotlin
* use modern Android SDK settings
* create an APK file
* install the APK on an Android phone

---

## 2. Final App Idea

The final structure is:

```text
LiaScript course
→ GitHub Pages web app
→ Android Studio WebView app
→ APK file
→ Android phone
```

This method is useful because the course already works as a website, and the Android app opens that website inside the app.

---

# Part A: Install Required Software

## 3. Required Tools

Before starting, we need:

```text
1. Android Studio
2. Android SDK
3. Java / JDK support
4. Gradle
5. Kotlin
6. GitHub Pages course link
7. Android phone
8. USB cable or file transfer method
9. Internet connection
```

---

## 4. Install Android Studio

Open the official Android Studio download page:

```text
https://developer.android.com/studio
```

Steps:

```text
1. Open https://developer.android.com/studio
2. Click Download Android Studio
3. Accept the terms
4. Download the Mac version
5. Open the downloaded .dmg file
6. Drag Android Studio to Applications
7. Open Android Studio
```

---

## 5. Install Android SDK

When Android Studio opens for the first time:

```text
1. Click Next
2. Choose Standard installation
3. Let Android Studio install SDK, Emulator, and Build Tools
4. Wait until installation finishes
5. Click Finish
```

Android SDK location on Mac is usually:

```text
/Users/masubmakhdoom/Library/Android/sdk
```

---

## 6. Check Android Studio Installation

Open Terminal and run:

```bash
ls "/Applications/Android Studio.app"
```

If Android Studio is installed, it should show:

```text
/Applications/Android Studio.app
```

---

# Part B: Prepare LiaScript Course

## 7. Create or Prepare LiaScript Course

First, create your LiaScript course as a Markdown file.

Example file name:

```text
A1_Part_1_Chapter_1_2.md
```

The course should include:

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

## 8. Publish LiaScript Course on GitHub Pages

In this app, we used this online LiaScript course link:

```text
https://masub27.github.io/a1-iphone-part1/
```

Before using this link inside Android app, open it in a normal browser and check that it works.

---

## 9. Why We Used GitHub Pages Link

At first, local LiaScript exported files were used inside Android WebView.

But the local version opened only a white screen.

So we changed the Android app to load the online GitHub Pages link.

This fixed the white screen problem.

---

# Part C: Create Android Studio Project

## 10. Create New Android Project

Open Android Studio.

Choose:

```text
New Project
→ Empty Activity or Empty Views Activity
```

Use these settings:

```text
Project name: A1.1 German Part 1
Package name: io.github.masubmakhdoom.a1part1modern
Language: Kotlin
Minimum SDK: 23
```

Project location:

```text
/Users/masubmakhdoom/AndroidStudioProjects/A11GermanPart1
```

---

## 11. Open Project in Terminal

Open Terminal and run:

```bash
cd "/Users/masubmakhdoom/AndroidStudioProjects/A11GermanPart1"
```

---

# Part D: Gradle Configuration

## 12. Project-Level Gradle File

The project-level file is:

```text
build.gradle.kts
```

Important:

```text
Do not put android { ... } inside this file.
```

Run this command:

```bash
cat > build.gradle.kts <<'EOF'
plugins {
    id("com.android.application") version "8.7.3" apply false
    id("org.jetbrains.kotlin.android") version "2.0.21" apply false
}
EOF
```

---

## 13. App-Level Gradle File

The app-level file is:

```text
app/build.gradle.kts
```

This file contains Android app settings.

Run this command:

```bash
cat > app/build.gradle.kts <<'EOF'
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
EOF
```

---

## 14. Explanation of Gradle Settings

```text
namespace
```

This is the internal package name of the Android app.

```text
compileSdk = 35
```

This tells Android Studio to compile the app using Android SDK 35.

```text
targetSdk = 35
```

This tells Android that the app is made for a modern Android version.

```text
minSdk = 23
```

This means the app can run on Android 6.0 and newer.

```text
versionCode = 1
versionName = "1.0"
```

These are app version settings.

```text
JavaVersion.VERSION_17
jvmToolchain(17)
```

These settings make Java and Kotlin use the same version.

---

# Part E: Theme Fix

## 15. Why We Changed the Theme

The project had MaterialComponents theme errors.

Example error:

```text
Theme.MaterialComponents.DayNight.DarkActionBar not found
colorPrimaryVariant not found
```

To fix this, we used simple built-in Android themes.

---

## 16. Create Normal Theme

Run:

```bash
mkdir -p app/src/main/res/values

cat > app/src/main/res/values/themes.xml <<'EOF'
<resources>
    <style name="Theme.A11GermanPart1" parent="@android:style/Theme.Material.Light.NoActionBar">
        <item name="android:windowNoTitle">true</item>
        <item name="android:windowActionBar">false</item>
        <item name="android:windowLightStatusBar">true</item>
        <item name="android:statusBarColor">#FFFFFF</item>
        <item name="android:navigationBarColor">#FFFFFF</item>
    </style>
</resources>
EOF
```

---

## 17. Create Dark Theme

Run:

```bash
mkdir -p app/src/main/res/values-night

cat > app/src/main/res/values-night/themes.xml <<'EOF'
<resources>
    <style name="Theme.A11GermanPart1" parent="@android:style/Theme.Material.NoActionBar">
        <item name="android:windowNoTitle">true</item>
        <item name="android:windowActionBar">false</item>
        <item name="android:statusBarColor">#000000</item>
        <item name="android:navigationBarColor">#000000</item>
    </style>
</resources>
EOF
```

---

# Part F: Android Manifest

## 18. Purpose of AndroidManifest.xml

The manifest file controls:

```text
App name
Internet permission
Main activity
Launcher activity
Android exported setting
```

File location:

```text
app/src/main/AndroidManifest.xml
```

---

## 19. Replace AndroidManifest.xml

Run:

```bash
cat > app/src/main/AndroidManifest.xml <<'EOF'
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
EOF
```

---

## 20. Important Manifest Code

Internet permission:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

This is required because the app loads an online LiaScript course.

App name:

```xml
android:label="A1 German Modern Online"
```

This is the name shown on the Android phone.

Main activity:

```xml
<activity
    android:name=".MainActivity"
    android:exported="true">
```

This tells Android which screen opens first.

---

# Part G: MainActivity WebView Code

## 21. Purpose of MainActivity.kt

The `MainActivity.kt` file controls the first screen of the Android app.

In this app, the first screen is a WebView.

The WebView opens the LiaScript course link.

File location:

```text
app/src/main/java/io/github/masubmakhdoom/a1part1modern/MainActivity.kt
```

---

## 22. Create MainActivity.kt

Run:

```bash
mkdir -p app/src/main/java/io/github/masubmakhdoom/a1part1modern

cat > app/src/main/java/io/github/masubmakhdoom/a1part1modern/MainActivity.kt <<'EOF'
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
EOF
```

---

## 23. Explanation of MainActivity Code

This line creates the WebView:

```kotlin
webView = WebView(this)
```

This line shows the WebView on the screen:

```kotlin
setContentView(webView)
```

This line keeps links inside the app:

```kotlin
webView.webViewClient = WebViewClient()
```

This line supports browser features like video and media:

```kotlin
webView.webChromeClient = WebChromeClient()
```

This line enables JavaScript:

```kotlin
settings.javaScriptEnabled = true
```

LiaScript needs JavaScript to work correctly.

This line enables browser storage:

```kotlin
settings.domStorageEnabled = true
```

This line allows media playback:

```kotlin
settings.mediaPlaybackRequiresUserGesture = false
```

This line opens the LiaScript course:

```kotlin
webView.loadUrl("https://masub27.github.io/a1-iphone-part1/")
```

---

# Part H: Build the APK

## 24. Build the Android App

Run:

```bash
./gradlew clean
./gradlew assembleDebug
```

Wait until Terminal shows:

```text
BUILD SUCCESSFUL
```

---

## 25. Copy APK to Desktop

Run:

```bash
cp app/build/outputs/apk/debug/app-debug.apk \
"/Users/masubmakhdoom/Desktop/A1_German_Modern_Online.apk"
```

Check the APK:

```bash
ls -lh "/Users/masubmakhdoom/Desktop/A1_German_Modern_Online.apk"
```

Final APK file:

```text
A1_German_Modern_Online.apk
```

---

# Part I: Install on Android Phone

## 26. Before Installing

First uninstall the old app from the phone:

```text
A1 German Part 1
```

This prevents confusion between old and new app versions.

---

## 27. Transfer APK to Phone

Send this file to Android phone:

```text
A1_German_Modern_Online.apk
```

You can transfer using:

```text
USB cable
Google Drive
Telegram
WhatsApp document
MacDroid
USB flash drive
```

---

## 28. Allow Unknown Apps

On Android phone, if installation is blocked:

```text
Settings
→ Security
→ Install unknown apps
→ Allow from this source
```

Then install the APK again.

---

## 29. Open the App

After installation, open:

```text
A1 German Modern Online
```

The app should open your LiaScript course.

---

# Part J: Testing

## 30. Testing Checklist

Test these points:

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

## 31. Important Internet Note

This app needs internet.

Reason:

```text
The app loads the LiaScript course from GitHub Pages.
```

Course link:

```text
https://masub27.github.io/a1-iphone-part1/
```

---

# Part K: Common Errors and Fixes

## 32. Error: Unresolved Reference android

Problem:

```text
android { ... } was pasted into the wrong Gradle file.
```

Fix:

```text
Put android { ... } only inside app/build.gradle.kts.
```

Project-level file:

```text
build.gradle.kts
```

App-level file:

```text
app/build.gradle.kts
```

---

## 33. Error: Kotlin Plugin Alias Not Found

Problem:

```text
alias(libs.plugins.kotlin.android) not found
```

Fix:

```text
Use direct plugin names.
```

Correct project-level plugin code:

```kotlin
plugins {
    id("com.android.application") version "8.7.3" apply false
    id("org.jetbrains.kotlin.android") version "2.0.21" apply false
}
```

---

## 34. Error: MaterialComponents Theme Not Found

Problem:

```text
Theme.MaterialComponents.DayNight.DarkActionBar not found
```

Fix:

```text
Use Android built-in theme instead of MaterialComponents theme.
```

---

## 35. Error: JVM Target Mismatch

Problem:

```text
compileDebugJavaWithJavac = 1.8
compileDebugKotlin = 21
```

Fix:

```text
Set both Java and Kotlin to version 17.
```

Correct code:

```kotlin
compileOptions {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}

kotlin {
    jvmToolchain(17)
}
```

---

## 36. Error: App Opens White Screen

Problem:

```text
Local LiaScript export did not load correctly inside Android WebView.
```

Fix:

```text
Use the online GitHub Pages course link.
```

Correct WebView load URL:

```kotlin
webView.loadUrl("https://masub27.github.io/a1-iphone-part1/")
```

---

# Part L: Final Result

## 37. Final APK

At the end, we created this APK:

```text
A1_German_Modern_Online.apk
```

The final installed app name is:

```text
A1 German Modern Online
```

The app uses:

```text
Kotlin
Android WebView
GitHub Pages
LiaScript
targetSdk 35
Java 17
```

---

# 38. Final Summary

In this training, we learned how to create a modern Android app for a LiaScript course.

The complete process was:

```text
Install Android Studio
Create LiaScript course
Publish it on GitHub Pages
Create Android Studio project
Fix Gradle files
Fix Android theme
Add Internet permission
Add WebView code
Build APK
Copy APK to Desktop
Install APK on Android phone
Test the app
```

This method is useful for creating mobile learning apps from LiaScript courses.

---

# 39. Reflection Questions

Answer these questions:

1. Why did we install Android Studio?
2. Why did we use GitHub Pages instead of local files?
3. Why does the Android app need Internet permission?
4. What is the purpose of WebView?
5. What does targetSdk 35 mean?
6. Why did we use Java 17?
7. What was the reason for the white screen problem?
8. What is the final APK file name?
9. What is the final app name on the phone?

---

# 40. Suggested Answers

1. We installed Android Studio to create, build, and test the Android app.
2. We used GitHub Pages because the local WebView version showed a white screen.
3. The app needs Internet permission because it opens an online course link.
4. WebView shows web content inside the Android app.
5. targetSdk 35 means the app targets a modern Android SDK.
6. Java 17 fixed the Java and Kotlin JVM target mismatch.
7. The white screen happened because local LiaScript files did not load correctly in WebView.
8. The final APK file name is `A1_German_Modern_Online.apk`.
9. The final app name is `A1 German Modern Online`.

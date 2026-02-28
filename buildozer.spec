[app]
title = Apple Doctor
package.name = appledoctor
package.domain = org.rahilafzal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,google-generativeai,pillow
orientation = portrait
android.permissions = INTERNET, CAMERA
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1


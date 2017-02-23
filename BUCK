
apple_bundle(
  name = 'Demo',
  binary = ':Binary',
  extension = 'app',
  info_plist = 'Info.plist',
)

apple_binary(
  name = 'Binary',
  deps = [':Library'],
)

apple_library(
    name = 'Library',
    preprocessor_flags = ['-fobjc-arc'],
    deps = ['//ViewController:ViewController'],
    headers = glob(['*.h']),
    srcs = glob(['*.m']),
    frameworks = [
        '$SDKROOT/System/Library/Frameworks/Foundation.framework',
        '$SDKROOT/System/Library/Frameworks/UIKit.framework',
    ],
),

apple_package(
  name = 'Package',
  bundle = ':Demo',
)

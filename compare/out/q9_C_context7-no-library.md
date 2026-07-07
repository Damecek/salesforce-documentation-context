# Q9: How do I get the list of picklist values for a given record type in Apex?

## Approach: C_context7-no-library
- latency: 4894 ms
- chosenLibrary: /llfbandit/record
- chosenTitle: Record

---

### resolve-library-id picked: /llfbandit/record (Record)

--- resolve-library-id ranking (top of list) ---
Available Libraries:

- Title: Record
- Context7-compatible library ID: /llfbandit/record
- Description: Record is a cross-platform Flutter plugin for audio recording from microphone to a file or stream with support for multiple encoders and formats.
- Code Snippets: 108
- Source Reputation: Medium
- Benchmark Score: 80.56
----------
- Title: Record
- Context7-compatible library ID: /websites/pub_dev_packages_record
- Description: Record is a Flutter audio recording library that captures audio from the microphone to file or stream with support for multiple codecs, bit rates, and sampling rates across all platforms.
- Code Snippets: 102
- Source Reputation: High
- Benchmark Score: 63.8
----------
- Title: XAF How to Get Role Code from the UI
- Context7-compatible library ID: /devexpress-examples/xaf_how-to-get-role-code-from-the-ui
- Description: Generate ModuleUpdater code for security roles created by XAF developers at runtime in test databases.
- Code Snippets: 4
- Source Reputation: High

--- query-docs against /llfbandit/record ---
### Audio Recording Usage

Source: https://github.com/llfbandit/record/blob/main/record/README.md

Demonstrates how to initialize the AudioRecorder, check for permissions, start recording to a file or stream, stop, cancel, and dispose of the recorder. Ensure permissions are handled before starting.

```dart
import 'package:record/record.dart';

final record = AudioRecorder();

// Check and request permission if needed
if (await record.hasPermission()) {
  // Start recording to file
  await record.start(const RecordConfig(), path: 'aFullPath/myFile.m4a');
  // ... or to stream
  final stream = await record.startStream(const RecordConfig(encoder: AudioEncoder.pcm16bits));
}

// Stop recording...
final path = await record.stop();
// ... or cancel it (and implicitly remove file/blob).
await record.cancel();

record.dispose(); // As always, don't forget this one.
```

--------------------------------

### RecordState enum with pause, record, stop values

Source: https://github.com/llfbandit/record/blob/main/record/record_platform_interface/lib/src/types/record_state.dart

Enum definition for RecordState with the three specified values: pause, record, stop

```dart
enum RecordState { pause, record, stop }
```

--------------------------------

### onStateChanged stream method

Source: https://github.com/llfbandit/record/blob/main/record/record/lib/src/record.dart

Method that returns a Stream<RecordState> for listening to recorder state changes

```dart
/// Listen to recorder states [RecordState].
  ///
  /// Provides pause, resume and stop states.
  ///
  /// Also, you can retrieve async errors from it by adding [Function? onError] callback to the subscription.
  Stream<RecordState> onStateChanged() =>
      _recordStateStream ?? _initStateStream();
```

--------------------------------

### isPaused Future method

Source: https://github.com/llfbandit/record/blob/main/record/record/lib/src/record.dart

Checks if recording session is paused. Returns a Future<bool> that resolves to true if the recording is currently paused.

```dart
/// Checks if recording session is paused.
  Future<bool> isPaused() {
    return _safeCall(() => _platform.isPaused(_recorderId));
  }
```

### Usage

Source: https://github.com/llfbandit/record/blob/main/record/README.md

The record package allows for audio recording. You can start recording to a file or a stream, stop it, cancel it, and dispose of the recorder instance. Permissions must be checked and requested before starting the recording.

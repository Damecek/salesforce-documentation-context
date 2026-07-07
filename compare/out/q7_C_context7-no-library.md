# Q7: How do I display a toast message in a Salesforce screen flow?

## Approach: C_context7-no-library
- latency: 4847 ms
- chosenLibrary: /calintamas/react-native-toast-message
- chosenTitle: React Native Toast Message

---

### resolve-library-id picked: /calintamas/react-native-toast-message (React Native Toast Message)

--- resolve-library-id ranking (top of list) ---
Available Libraries:

- Title: React Native Toast Message
- Context7-compatible library ID: /calintamas/react-native-toast-message
- Description: An animated and customizable toast message component for React Native with an imperative API, keyboard awareness, and a lightweight footprint.
- Code Snippets: 356
- Source Reputation: High
- Benchmark Score: 94

--- query-docs against /calintamas/react-native-toast-message ---
### Show Success or Error Toast in Screen Component

Source: https://github.com/calintamas/react-native-toast-message/blob/main/_autodocs/README.md

Use this pattern to display success or error messages to the user after an asynchronous operation within a screen component. Ensure 'react-native-toast-message' is imported.

```typescript
import Toast from 'react-native-toast-message';

export function MyScreen() {
  const handleSave = async () => {
    try {
      await saveData();
      Toast.show({
        type: 'success',
        text1: 'Saved',
        text2: 'Your changes have been saved'
      });
    } catch (error) {
      Toast.show({
        type: 'error',
        text1: 'Error',
        text2: error.message
      });
    }
  };

  return (
    <View>
      <Button title="Save" onPress={handleSave} />
    </View>
  );
}
```

--------------------------------

### Show Toast Message from Anywhere

Source: https://github.com/calintamas/react-native-toast-message/blob/main/docs/quick-start.md

Use the Toast.show() method to display toast messages. This can be called from any part of your application, including outside of React components. Ensure the Toast component is rendered in your app's entry file.

```jsx
// Foo.jsx
import Toast from 'react-native-toast-message';
import { Button } from 'react-native'

export function Foo(props) {
  const showToast = () => {
    Toast.show({
      type: 'success',
      text1: 'Hello',
      text2: 'This is some something 👋'
    });
  }

  return (
    <Button
      title='Show toast'
      onPress={showToast}
    />
  )
}
```

--------------------------------

### Show an Info Toast Message

Source: https://github.com/calintamas/react-native-toast-message/blob/main/docs/api.md

Call the show() method to display a toast. Specify the type and text content. Ensure Toast is imported.

```javascript
import Toast from 'react-native-toast-message'

Toast.show({
  type: 'info',
  text1: 'This is an info message'
});
```

--------------------------------

### Show a Success Toast

Source: https://github.com/calintamas/react-native-toast-message/blob/main/_autodocs/GETTING_STARTED.md

Use the static Toast.show API to display a success message. This is the basic method for showing toasts anywhere in your application.

```typescript
Toast.show({
  type: 'success',
  text1: 'Success',
  text2: 'Operation completed successfully'
});
```

--------------------------------

### Static API - Show Toast

Source: https://github.com/calintamas/react-native-toast-message/blob/main/_autodocs/README.md

Use the static `Toast.show()` method to display a toast message. You can configure its type, position, text content, visibility duration, and behavior like auto-hiding and swipeability.

```APIDOC
## Toast.show()

### Description
Displays a toast message with customizable properties.

### Method
Static method call on the Toast module.

### Parameters
#### Options Object
- **type** (string) - Required - The type of the toast (e.g., 'success', 'error', 'info', or a custom string).
- **position** (string) - Optional - The position of the toast ('top' or 'bottom'). Defaults to 'top'.
- **text1** (string) - Optional - The header text of the toast.
- **text2** (string) - Optional - The main message text of the toast.
- **visibilityTime** (number) - Optional - The duration in milliseconds the toast should be visible. Defaults to 4000.
- **autoHide** (boolean) - Optional - Whether the toast should automatically hide after `visibilityTime`. Defaults to true.
- **swipeable** (boolean) - Optional - Whether the toast can be dismissed by swiping. Defaults to true.

### Request Example
```javascript
Toast.show({
  type: 'success',
  position: 'top',
  text1: 'Hello',
  text2: 'This is a toast message.',
  visibilityTime: 3000,
  autoHide: true,
  swipeable: true
});
```
```

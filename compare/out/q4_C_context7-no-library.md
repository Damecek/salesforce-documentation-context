# Q4: How do I create a record-triggered flow that runs after a record is saved?

## Approach: C_context7-no-library
- latency: 4864 ms
- chosenLibrary: /aframevr/aframe
- chosenTitle: A-Frame

---

### resolve-library-id picked: /aframevr/aframe (A-Frame)

--- resolve-library-id ranking (top of list) ---
Available Libraries:

- Title: A-Frame
- Context7-compatible library ID: /aframevr/aframe
- Description: A web framework for building browser-based 3D, AR, and VR experiences using declarative HTML and an entity-component architecture.
- Code Snippets: 1863
- Source Reputation: High
- Benchmark Score: 87.2
----------
- Title: A-Frame Extras
- Context7-compatible library ID: /c-frame/aframe-extras
- Description: A-Frame Extras provides add-ons and helpers for A-Frame VR, including components for controls, model loaders, pathfinding, and various utilities.
- Code Snippets: 82
- Source Reputation: High
----------
- Title: A* Pathfinding Project
- Context7-compatible library ID: /websites/arongranberg_astar
- Description: The A* Pathfinding Project provides comprehensive documentation for a powerful pathfinding solution, including tutorials, class details, and examples for game development.
- Code Snippets: 12808
- Source Reputation: High
- Benchmark Score: 78.75
----------
- Title: Stripe Accept a Payment
- Context7-compatible library ID: /stripe-samples/accept-a-payment
- Description: Learn how to securely accept payments online with Stripe, offering examples for Prebuilt Checkout, P

--- query-docs against /aframevr/aframe ---
### Handle Entity Loading with a Component

Source: https://github.com/aframevr/aframe/blob/master/docs/introduction/javascript-events-dom-apis.md

Listen to the `loaded` event or use an A-Frame component to execute logic after an entity has been appended and loaded.

```javascript
var sceneEl = document.querySelector('a-scene');

AFRAME.registerComponent('do-something-once-loaded', {
  init: function () {
    // This will be called after the entity has properly attached and loaded.
    console.log('I am ready!');
  }
});

var entityEl = document.createElement('a-entity');
entityEl.setAttribute('do-something-once-loaded', '');
sceneEl.appendChild(entityEl);
```

--------------------------------

### .play ()

Source: https://github.com/aframevr/aframe/blob/master/docs/core/component.md

Called when the entity or scene resumes. Used to add event listeners and re-enable dynamic behavior.

```APIDOC
## .play ()

### Description
Called when the entity or scene resumes. This happens when the component is first attached (after `update`), or when the entity or scene was paused and then resumed.

### Usage
Often used to add event listeners or re-enable dynamic behavior that was previously stopped by the `pause` handler.

### Example
```js
AFRAME.registerComponent('sound', {
  // ...
  play: function () {
    if (this.data.autoplay) { this.playSound(); }
    this.updateEventListener();
  }
  // ...
});
```
```

--------------------------------

### play

Source: https://github.com/aframevr/aframe/blob/master/docs/core/entity.md

Starts any dynamic behavior, including animations and component updates. Automatically called when the entity is attached to the DOM. Automatically plays child entities.

```APIDOC
## play ()

### Description
Starts any dynamic behavior defined by animations and components. This method is automatically called when the entity is attached to the DOM and also calls `play()` on each of the entity's child entities.

### Usage Example
```js
// Play the entity and its dynamic behaviors
entity.play();
```
```

### Running Content Scripts on the Scene

Source: https://github.com/aframevr/aframe/blob/master/docs/core/scene.md

If you need to run scripts without creating a dedicated component, you must wait for the scene to finish initializing. This can be achieved by checking the `hasLoaded` property of the scene element or by listening for the `loaded` event.

--------------------------------

### Entity API — `<a-entity>` Methods and Properties

Source: https://context7.com/aframevr/aframe/llms.txt

Entities provide methods for lifecycle management, including `pause()` to stop updates and event listeners, `play()` to resume them, and `destroy()` to completely remove the entity and free associated memory. You can also manage entity states using `addState()`, `removeState()`, and `is()` methods, and emit custom events using `emit()`.

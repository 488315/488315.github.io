# MD3 Expressive OpenStreetMap Component

A beautiful, drop-in HTML component that displays interactive maps using OpenStreetMap data, styled with Material Design 3 (MD3) expressive design principles.

## Features

### 🎨 **Material Design 3 Expressive Styling**
- Complete MD3 color tokens implementation
- Expressive typography using Roboto font family
- Proper elevation and shadow system
- MD3-compliant interactive controls

### 🗺️ **OpenStreetMap Integration**
- Powered by Leaflet.js for smooth map interactions
- Multiple map layer options (Standard, Topographic, Humanitarian)
- Custom MD3-styled markers and popups
- Real-time coordinate and zoom level display

### 🎮 **Interactive Features**
- **Geolocation**: Find user's current location
- **Fullscreen**: Toggle fullscreen map view
- **Layer Switching**: Cycle through different map styles
- **Click to Place Markers**: Interactive marker placement
- **Responsive Design**: Optimized for mobile and desktop

## Usage

### Quick Start
1. Download the `md3-openstreetmap.html` file
2. Open it in any modern web browser
3. The map will load automatically with London as the default location

### Integration into Existing Projects
```html
<!-- Copy the CSS and HTML structure from md3-openstreetmap.html -->
<!-- Include the required dependencies: -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/icon?family=Material+Symbols+Outlined" rel="stylesheet">

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
```

### Local Development
```bash
# Start a local HTTP server to test the component
python3 -m http.server 8080

# Or with Node.js
npx http-server .

# Then open http://localhost:8080/md3-openstreetmap.html
```

## Customization

### Changing Default Location
Edit the `initializeMap()` function:
```javascript
// Default location (London)
const defaultLat = 51.505;
const defaultLng = -0.09;
const defaultZoom = 13;
```

### Adding Custom Map Layers
Extend the `mapLayers` object:
```javascript
const mapLayers = {
    // ... existing layers
    custom: {
        name: 'Custom Layer',
        url: 'https://your-tile-server/{z}/{x}/{y}.png',
        options: {
            maxZoom: 19,
            attribution: 'Your attribution'
        }
    }
};
```

### Modifying MD3 Colors
Update the CSS custom properties in the `:root` selector:
```css
:root {
    --md-sys-color-primary: #your-color;
    --md-sys-color-secondary: #your-color;
    /* ... other color tokens */
}
```

## Technical Details

### Dependencies
- **Leaflet.js 1.9.4**: Lightweight mapping library
- **Material Symbols**: Google's icon font
- **Roboto Font**: Material Design typography

### Browser Support
- Modern browsers with ES6+ support
- Requires geolocation API for location features
- Responsive design works on mobile and desktop

### Performance
- Lazy loads map tiles as needed
- Efficient marker management (single marker at a time)
- Optimized CSS with hardware acceleration

## Map Controls

| Button | Function | Description |
|--------|----------|-------------|
| 📍 | Geolocation | Centers map on user's location |
| ⛶ | Fullscreen | Toggles fullscreen map view |
| 🗂️ | Layers | Cycles through map layer styles |

## Features in Detail

- **Loading Animation**: MD3-styled spinner during map initialization
- **Custom Markers**: Circular markers following MD3 design principles
- **Interactive Popups**: Click anywhere to place a marker with coordinates
- **Real-time Info**: Live coordinate and zoom level display
- **Smooth Animations**: CSS transitions following MD3 motion guidelines
- **Accessibility**: Proper ARIA labels and keyboard navigation

## License

This component uses OpenStreetMap data and Leaflet.js, both under open licenses. The Material Design 3 implementation follows Google's design guidelines.

---

**Note**: This is a complete, self-contained HTML component that requires no build process or additional setup.
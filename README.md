# MD3 OpenStreetMap Component

A beautiful, responsive HTML drop-in component that combines Google Maps API with OpenStreetMap data, styled with Material Design 3 expressive design principles.

## Features

✨ **Material Design 3 Expressive Design**
- Complete MD3 color system with light/dark mode support
- Expressive typography and elevation system
- Smooth animations and transitions
- Responsive design for all devices

🗺️ **Interactive Map Features**
- OpenStreetMap integration with multiple tile layers (Street, Satellite, Terrain)
- Location search with geocoding via Nominatim
- Current location detection
- Click-to-add markers
- Zoom controls and fullscreen mode
- Scale indicators

🎨 **Modern UI Components**
- MD3-styled buttons with hover effects
- Search input with integrated search button
- Floating map controls
- Toast notifications
- Info panel with component details

## Quick Start

1. **Download the component**
   ```bash
   # Simply download the md3-osm-map.html file
   ```

2. **Open in browser**
   ```bash
   # Open md3-osm-map.html in any modern web browser
   # No server required - works offline!
   ```

3. **Drop into your project**
   ```html
   <!-- Copy the entire content of md3-osm-map.html -->
   <!-- and paste it into your HTML file or iframe -->
   ```

## Usage Examples

### Basic Integration
```html
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body>
    <!-- Paste the entire md3-osm-map.html content here -->
    <!-- Or use an iframe -->
    <iframe src="md3-osm-map.html" width="100%" height="600px" frameborder="0"></iframe>
</body>
</html>
```

### Custom Styling
```css
/* Override MD3 variables for custom theming */
:root {
    --md3-primary: #your-color;
    --md3-secondary: #your-color;
    /* ... other variables */
}
```

## API Reference

### Map Controls
- **Search**: Type location name and press Enter or click search button
- **My Location**: Get current GPS location (requires permission)
- **Fullscreen**: Toggle fullscreen mode
- **Zoom**: Use +/- buttons or mouse wheel
- **Layer Switch**: Choose between Street, Satellite, and Terrain views

### JavaScript API
```javascript
// Access the map instance
const mapInstance = new MD3OSMMap();

// Search for a location
mapInstance.searchLocation('New York, NY');

// Get current location
mapInstance.getCurrentLocation();

// Add a marker
mapInstance.addMarker([40.7128, -74.0060], 'New York City');
```

## Browser Support

- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 12+
- ✅ Edge 79+

## Dependencies

- **Leaflet.js** (v1.9.4) - Map library
- **OpenStreetMap** - Map tiles and data
- **Nominatim** - Geocoding service

All dependencies are loaded from CDN - no local installation required!

## Customization

### Colors
Modify the CSS custom properties in the `:root` selector:
```css
:root {
    --md3-primary: #6750a4;        /* Primary color */
    --md3-secondary: #625b71;      /* Secondary color */
    --md3-tertiary: #7d5260;       /* Tertiary color */
    /* ... */
}
```

### Map Settings
Adjust map behavior in the JavaScript:
```javascript
// Change default location
this.map = L.map('map').setView([40.7128, -74.0060], 13);

// Add custom tile layers
const customLayer = L.tileLayer('your-tile-url/{z}/{x}/{y}.png');
```

## License

This component is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests!

---

**Built with ❤️ using Material Design 3 and OpenStreetMap**
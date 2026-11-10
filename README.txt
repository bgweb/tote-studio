TOTE STUDIO — QR READER + FONT FIX

The decoder tries a local jsQR.js file first, then the online source.
To enable offline QR scanning:
1. While online, open https://cdn.jsdelivr.net/npm/jsqr@1.4.0/dist/jsQR.js
2. Save the page as jsQR.js (Ctrl+S) into this folder alongside decoder.html
3. Open decoder.html. The QR scanner uses the local library.

The library itself could not be bundled due to unavailable network access in the build environment.

The decoder now explicitly loads the selected design fonts before rendering/exporting.
Keep assets/fonts and the same numbered artwork on both devices.

PRINT PNG EXPORT FIX
The Save print PNG button now generates the PNG directly in its click handler and
triggers a normal browser download immediately, rather than waiting for an async
canvas.toBlob callback. An error message is shown if the browser cannot export.

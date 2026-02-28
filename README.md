# Python Course Resource System

This is an interactive exercise system designed for Python courses, allowing students to practice directly in the browser and record their progress.

## Development & Management

### 1. Environment Setup
This project uses `uv` for dependency management. Please create a `.env` file and set your backend URL:
```bash
GAS_URL="YOUR_BACKEND_URL"
```

### 2. Generate Web Pages
Run the build script to generate or update the static content in the `dist/` directory:
```bash
uv run build.py
```

## Backend Reference (GAS)
This section is provided for future administrator maintenance and reference:

```javascript
function doGet(e) {
  var params = e.parameter;
  var formId = 'GOOGLE FORM ID';

  try {
    var form = FormApp.openById(formId);
    var baseURL = form.getPublishedUrl().replace("viewform", "formResponse");

    var payload = {
      "entry.placeholder": params.stuID,
      "entry.placeholder": params.stuName,
      "entry.placeholder": params.exID,
      "entry.placeholder": "465",
      "submit": "Submit"
    };

    var res = UrlFetchApp.fetch(baseURL, {
      method: "post",
      payload: payload,
      muteHttpExceptions: true
    });

    var responseCode = res.getResponseCode();
    var responseBody = res.getContentText();

    if (responseCode == 200) {
      if (responseBody.indexOf("您的回覆已記錄") !== -1 ||
          responseBody.indexOf("Your response has been recorded") !== -1) {
        return ContentService.createTextOutput(JSON.stringify({"status": "success"}))
          .setMimeType(ContentService.MimeType.JSON);
      } else {
        return ContentService.createTextOutput(JSON.stringify({
          "status": "error",
          "message": "Validation failed: Check student ID format or form rules."
        })).setMimeType(ContentService.MimeType.JSON);
      }
    } else {
      return ContentService.createTextOutput(JSON.stringify({
        "status": "error",
        "code": responseCode,
        "message": "Google Form error (HTTP " + responseCode + ")"
      })).setMimeType(ContentService.MimeType.JSON);
    }
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      "status": "error",
      "message": "GAS Script Error: " + err.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
```

## Deploy
The system is automatically built and deployed via GitHub Actions. Ensure that the `GAS_URL` secret is configured in your Repository Settings.

Yes. This is feasible on Windows 11, but the cleanest approach is not to override Ctrl+C itself. Instead, monitor the clipboard and sanitize URLs immediately after they're copied. That way, copying continues to work normally in every application.
There are a few approaches:

Option 1: Clipboard listener (recommended)
Create a small background application that:
Registers as a clipboard listener using the Win32 API (AddClipboardFormatListener).
Waits for the WM_CLIPBOARDUPDATE message.
Reads the clipboard text.
If the text is a URL:
Parse it.
Remove tracking parameters such as:
utm_source
utm_medium
utm_campaign
utm_term
utm_content
utm_id
fbclid
gclid
msclkid
etc.
Write the cleaned URL back to the clipboard.
The user presses Ctrl+C as usual, but by the time they paste, the URL has already been cleaned.
Advantages:

Works with virtually every application.
Doesn't interfere with keyboard shortcuts.
Doesn't require keyboard hooks.
Low CPU usage.
Option 2: Keyboard hook
Install a global low-level keyboard hook (WH_KEYBOARD_LL) and intercept Ctrl+C.
When Ctrl+C is detected:

Let the target application perform the copy.
Wait a short time (10–50 ms).
Read the clipboard.
Sanitize URLs.
Replace the clipboard contents.
This works, but timing can be tricky because different applications update the clipboard at different speeds.
Option 3: Clipboard history integration
Windows doesn't provide a public API to transform clipboard contents before they're stored in clipboard history. You'd still use a clipboard listener.
URL sanitization
In languages like C#, the logic is straightforward:
Uri uri = new Uri(text);

var query = HttpUtility.ParseQueryString(uri.Query);

foreach (string key in query.AllKeys.ToList())
{
    if (key.StartsWith("utm_"))
        query.Remove(key);

    if (key == "fbclid")
        query.Remove(key);

    if (key == "gclid")
        query.Remove(key);
}

var builder = new UriBuilder(uri);
builder.Query = query.ToString();

Clipboard.SetText(builder.Uri.ToString());

You'd also want to preserve fragments (#section) and handle URLs without query strings gracefully.
Existing tools
Before building your own, you could look at tools such as:
AutoHotkey (with clipboard monitoring)
PowerToys Advanced Paste (extensible, though it doesn't currently strip UTM parameters automatically)
Browser extensions that clean copied links (these only work within the browser, not system-wide)
If you want it to feel native
A polished implementation would:
Start automatically when you log in.
Sit quietly in the system tray.
Wake only on clipboard updates.
Modify only URLs.
Leave all other copied content untouched.
Optionally allow configuring which parameters to remove.
This approach is more reliable than intercepting Ctrl+C because it works regardless of whether the copy was initiated with a keyboard shortcut, a context menu, a toolbar button, or another application's "Copy" command.
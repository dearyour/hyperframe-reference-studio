# Exact subtitle timing

Keep an unchanged copy of the user's SRT. Decode without silently normalizing its text. Store integer milliseconds for starts and ends; use decimal seconds only when serializing the composition.

- Preserve block boundaries and ordering. One subtitle block is one scene.
- Preserve Unicode characters, punctuation, spaces and internal line breaks. Use text nodes and `white-space: pre-wrap`; do not trim or collapse text. Escaping markup for HTML is fine only when the displayed text remains identical.
- Preserve each start and end. Do not close gaps, shift a late first subtitle to zero, merge blocks or split long captions. Handle overlapping blocks explicitly without hiding one to simplify the timeline.
- Set total duration to the last subtitle's end. If the file's ordering makes this conflict with another block ending later, report that conflict instead of silently dropping content.
- Emit a scene table and compare every block's displayed text and millisecond boundaries against the unchanged input.

Frame quantization matters: an arbitrary millisecond endpoint may not be exactly representable at 30 fps. Calculate `duration_seconds * fps`; if it is not integral, choose an appropriate supported frame rate or an explicitly verified encoding strategy. Do not round the input timestamp or label a duration mismatch successful. If the required combination cannot be produced, explain the exact limitation and obtain a changed constraint before changing the deliverable.

Motion must fit within the subtitle interval. Prefer short entrances and a readable hold; do not add an exit tail beyond the provided end. Inspect boundary frames after rendering. A perfect HTML timing table alone does not verify the encoded MP4.

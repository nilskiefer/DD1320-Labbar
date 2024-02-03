*Situated gaze*
Physical embodiment improves focus on speech
Mutual gaze and joint attention:
	
1. `startord[:i]` retrieves the substring of `startord` from the beginning up to (but not including) the letter at position `i`. This captures all the letters before the one we want to replace.
2. `j` represents the new letter that we want to insert at position `i`.
3. `startord[i+1:]` retrieves the substring of `startord` starting from the letter after the one at position `i`. This captures all the letters after the one we want to replace.
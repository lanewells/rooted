# Rooted

Rooted is a family-centered application where relatives can come together to build a shared digital timeline. By uploading written memories, relatives can record and preserve moments and celebrate their family's legacy in a meaningful way.

## Features

Build Your Family Tree - join with other relatives

Upload Memories

Add text to capture significant moments in the present or past

Attach a date to your memory

Stories and Comments

Share stories and comment on your relatives' posts

## Privacy & Security

Your family memories are kept private and secure, accessible only to user with an account.

## Tech Stack

Frontend: Python, Django, HTML, CSS

Backend: Django

Database: PSQL

Authentication: Django

Deployment: Heroku, GitHub

## New Things I Learned

### Reverse_lazy

Reverse lazy is similar to reverse, but is only called when necessary. I used this in several views, including my MemoryCreate view below.

```python
    def get_success_url(self):
        return reverse_lazy('memory-detail', kwargs={'pk': self.object.pk})
```

### Fieldset & legend tags

Fieldset and legend tags are in nearly every form and form view. I played around with the "hidden" (Django-native) form attributes using the dev tools in my browser. This enabled me to target specific values and change the styling to match the other pages.

```html
    <fieldset>
        <legend>Create my account</legend>
        <!--{{ table }}-->
    </fieldset>
```

## Build Out & Implications

The purpose of my application lies in the build out. While it is functional and fun as a smaller app, the bulk of the functionality (and fun) starts with a timeline view and multimedia uploading capabilities. Here are some other goals I have for the future of Rooted:

### Build Out

-   Map view via Google Maps API integration
-   Timeline sorting by date, specific date ranges
-   Closed 'Family Tree' groups of relatives
-   PDF, video, image, hyperlink, audio recording capabilities for memories
-   Add tags of custom words and tag other relatives, add locations to memories

### Implications

-   Track your ancestor's timeline, fill in blanks, and track their migration or immigration
-   Upload a PDF document of your grandmother's recipe
-   Take a photo on your phone of an old relic
-   Visualize your family tree
-   Upload family health conditions and deepen your understanding of your own genetics


### Created by Delaney Wells

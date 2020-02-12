# Updates and Changes

1. Sellers

- photo doesn't display on Seller list page. {{ seller.web_site }} was supposed to be {{ seller.logo }}
- Website was hardcoded as "lujack.com" for newly created Sellers. Changed to {{ seller.web_site}}. This was also linking to URL as an internal link, edited code to make it link to outside link:  
  `<a href="http://{{ seller.web_site }}">{{ seller.web_site }}</a>`

2. Styling -

- css styling not being applied. file was misplaced inside templates folder, moved to main folder under static/css.
- restyled seller detail page.

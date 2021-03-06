---
layout: post
title: Writing posts with emacs 
date: 2021-02-22
permalink: /posts/2021/02/Writing-posts-with-emacs tags:
---

From org-mode to html
=====================

For that I used

``` {.commonlisp}
  (setq org-publish-project-alist ;; https://thackl.github.io/blogging-with-emacs-org-mode-and-jekyll
        '(("vtrappler.github.io" ;; my blog )
     ;; Path to org files.
     :base-directory "~/vtrappler.github.io/org_posts/"
     :base-extension "org"
     ;; Path to Jekyll Posts
     :publishing-directory "~/vtrappler.github.io/_posts/"
     :recursive t
     :publishing-function org-html-publish-to-html
     :headline-levels 4
     :html-extension "html"
     :body-only t
     )))
```

Using yassnippets for the frontmatter used in jekyll
====================================================

``` {.commonlisp}
  # -*- mode: snippet -*-
  # name: jekyll-frontmatter-create
  # key: jekyll-autofilled-frontmatter
  # --

  ,#+BEGIN_EXPORT html
  ---
  layout: post
  title: `(s-replace "-" " " (substring (buffer-name) 11 -4))`
  date: `(shell-command-to-string "echo -n $(date +%Y-%m-%d)"))`
  permalink: /posts/`(shell-command-to-string "echo -n $(date +%Y/%m)")`/`(substring (buffer-name) 11 -4)`
  tags:
  ---
  ,#+END_EXPORT
```

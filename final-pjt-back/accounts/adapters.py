from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)

        like_genre1 = data.get("like_genre1")
        like_genre2 = data.get("like_genre2")
        like_genre3 = data.get("like_genre3")
        if like_genre1:
            user.like_genre1 = like_genre1
        if like_genre2:
            user.like_genre2 = like_genre2
        if like_genre3:
            user.like_genre3 = like_genre3
            
        user.save()
        return user

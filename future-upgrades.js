// For TweetComponents to add new tweet to the list when it's created
setNewTweets((prev) => [{content: newValue, likes: 0, id: Math.random() * 500}, ...prev])

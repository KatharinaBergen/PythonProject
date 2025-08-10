import Observer
import Observable

observable = Observable.Observable()

cat = Observer.Cat()
dog = Observer.Dog()

observable.subscribe(cat)
observable.subscribe(dog)

observable.notify("Yum, Sausages!")

observable.unsubscribe(cat)

observable.notify("Yum, Cat! (because dogs are evil^^)")
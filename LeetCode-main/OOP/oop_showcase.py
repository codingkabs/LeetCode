"""
oop_showcase.py — A compact but comprehensive tour of OOP in Python.

Run this file directly to see demos:
    python oop_showcase.py
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Tuple, Iterable, Iterator, Callable, Protocol, runtime_checkable, Any, Optional
import json
import math
import time


# ============================================================
# 1) BASIC CLASS: CONSTRUCTOR, REPR, EQUALITY, PROPERTY, CLASS/STATIC METHODS
# ============================================================

class User:
    def __init__(self, username: str, age: int):
        self._username = username
        self.age = age  # will use property validation below

    def __repr__(self) -> str:
        return f"User(username={self._username!r}, age={self._age})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, User):
            return NotImplemented
        return (self._username, self._age) == (other._username, other._age)

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Age must be non-negative")
        self._age = value

    @property
    def username(self) -> str:
        return self._username

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        return cls(username=data["username"], age=int(data["age"]))

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

# Explanation:
# - Encapsulates state with properties.
# - __repr__ aids debugging; __eq__ enables comparisons.
# - @classmethod used for alternate constructors; @staticmethod for utility logic.


# ============================================================
# 2) ENCAPSULATION & NAME MANGLING (private-ish)
# ============================================================

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = float(balance)  # name-mangled: _BankAccount__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    @property
    def balance(self) -> float:
        return round(self.__balance, 2)

# Explanation:
# - Double underscore triggers name-mangling to discourage accidental access.
# - Still not *truly* private, but communicates intent.


# ============================================================
# 3) INHERITANCE & POLYMORPHISM
# ============================================================

class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def speak(self) -> str:
        ...

class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says: woof!"

class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says: meow!"

def chorus(animals: Iterable[Animal]) -> List[str]:
    return [a.speak() for a in animals]

# Explanation:
# - Abstract base class defines interface; subclasses implement behavior.
# - Polymorphism: chorus() works for any Animal subtype.


# ============================================================
# 4) ABSTRACT BASE CLASSES (ABCs)
# ============================================================

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...
    @abstractmethod
    def perimeter(self) -> float: ...

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h
    def area(self) -> float:
        return self.w * self.h
    def perimeter(self) -> float:
        return 2 * (self.w + self.h)

class Circle(Shape):
    def __init__(self, r: float):
        self.r = r
    def area(self) -> float:
        return math.pi * self.r * self.r
    def perimeter(self) -> float:
        return 2 * math.pi * self.r

# Explanation:
# - ABCs enforce “must implement” methods.


# ============================================================
# 5) MIXINS & MULTIPLE INHERITANCE
# ============================================================

class JSONSerializableMixin:
    def to_json(self) -> str:
        if hasattr(self, "__dict__"):
            return json.dumps(self.__dict__, ensure_ascii=False)
        if dataclass_isinstance(self):
            return json.dumps(asdict(self), ensure_ascii=False)
        raise TypeError("Object not serializable")

def dataclass_isinstance(obj: Any) -> bool:
    # Lightweight check: dataclasses add __dataclass_fields__ attribute
    return hasattr(obj, "__dataclass_fields__")

class TimestampMixin:
    def timestamp(self) -> float:
        return time.time()

class LogEntry(TimestampMixin, JSONSerializableMixin):
    def __init__(self, level: str, message: str):
        self.level = level
        self.message = message

# Explanation:
# - Mixins supply orthogonal features (serialization, timestamps).
# - Multiple inheritance composes behavior cleanly when designed as mixins.


# ============================================================
# 6) COMPOSITION OVER INHERITANCE
# ============================================================

class Customer:
    def __init__(self, name: str):
        self.name = name

class LineItem:
    def __init__(self, product: str, qty: int, price: float):
        self.product = product
        self.qty = qty
        self.price = price
    def total(self) -> float:
        return self.qty * self.price

class Order:
    def __init__(self, customer: Customer, items: List[LineItem]):
        self.customer = customer
        self.items = items
    def total(self) -> float:
        return round(sum(i.total() for i in self.items), 2)

# Explanation:
# - Order “has a” Customer and LineItems (composition).
# - Prefer composition to avoid brittle inheritance trees.


# ============================================================
# 7) DUNDER METHODS / OPERATOR OVERLOADING
# ============================================================

class Vector:
    __slots__ = ("x", "y")  # memory optimization & attribute safety

    def __init__(self, x: float, y: float):
        self.x, self.y = x, y

    def __iter__(self) -> Iterator[float]:
        yield self.x
        yield self.y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __hash__(self) -> int:
        return hash((round(self.x, 9), round(self.y, 9)))

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def magnitude(self) -> float:
        return math.hypot(self.x, self.y)

# Explanation:
# - __slots__ prevents dynamic attributes and reduces memory.
# - Rich dunders enable natural arithmetic and hashing.


# ============================================================
# 8) PROTOCOLS (Structural Subtyping / Duck Typing)
# ============================================================

@runtime_checkable
class Renderer(Protocol):
    def render(self, data: Dict[str, Any]) -> str: ...

class HTMLRenderer:
    def render(self, data: Dict[str, Any]) -> str:
        items = "".join(f"<li>{k}: {v}</li>" for k, v in data.items())
        return f"<ul>{items}</ul>"

class JSONRenderer:
    def render(self, data: Dict[str, Any]) -> str:
        return json.dumps(data)

def show_report(renderer: Renderer, data: Dict[str, Any]) -> str:
    return renderer.render(data)

# Explanation:
# - Protocols allow “if it quacks like a duck” typing.
# - No inheritance required; only method presence matters.


# ============================================================
# 9) DATA CLASSES (boilerplate reduction)
# ============================================================

@dataclass(frozen=True)
class AppConfig:
    env: str
    debug: bool = False
    features: Tuple[str, ...] = field(default_factory=tuple)

# Explanation:
# - frozen=True makes instances immutable (hashable, safer to share).


# ============================================================
# 10) FACTORY PATTERN
# ============================================================

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str: ...

class StripeGateway(PaymentGateway):
    def pay(self, amount: float) -> str:
        return f"Stripe processed £{amount:.2f}"

class PaypalGateway(PaymentGateway):
    def pay(self, amount: float) -> str:
        return f"PayPal processed £{amount:.2f}"

class PaymentFactory:
    _map: Dict[str, Callable[[], PaymentGateway]] = {
        "stripe": StripeGateway,
        "paypal": PaypalGateway,
    }

    @classmethod
    def create(cls, name: str) -> PaymentGateway:
        try:
            return cls._map[name.lower()]()
        except KeyError:
            raise ValueError(f"Unknown gateway: {name!r}")

# Explanation:
# - Centralizes creation logic; easy to extend with new gateways.


# ============================================================
# 11) STRATEGY PATTERN
# ============================================================

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float: ...

class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent
    def apply(self, total: float) -> float:
        return round(total * (1 - self.percent / 100.0), 2)

class ThresholdDiscount(DiscountStrategy):
    def __init__(self, threshold: float, subtract: float):
        self.threshold = threshold
        self.subtract = subtract
    def apply(self, total: float) -> float:
        return round(total - self.subtract if total >= self.threshold else total, 2)

class Checkout:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy
    def final_total(self, order: Order) -> float:
        return self.strategy.apply(order.total())

# Explanation:
# - Behavior (discount) is injected and swappable at runtime.


# ============================================================
# 12) OBSERVER PATTERN (Publish/Subscribe)
# ============================================================

class EventEmitter:
    def __init__(self):
        self._listeners: Dict[str, List[Callable[..., None]]] = {}

    def on(self, event: str, listener: Callable[..., None]) -> None:
        self._listeners.setdefault(event, []).append(listener)

    def off(self, event: str, listener: Callable[..., None]) -> None:
        try:
            self._listeners[event].remove(listener)
        except (KeyError, ValueError):
            pass

    def emit(self, event: str, *args, **kwargs) -> None:
        for listener in self._listeners.get(event, []):
            listener(*args, **kwargs)

# Explanation:
# - Decouples publishers from subscribers; many-to-many notifications.


# ============================================================
# 13) CONTEXT MANAGER
# ============================================================

class Timer:
    def __enter__(self):
        self._start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self._start
        # Swallow no exceptions (return False / None)
        return False

# Explanation:
# - “with Timer() as t:” measures time reliably, even on exceptions.


# ============================================================
# 14) ITERATOR / ITERABLE
# ============================================================

class Fibonacci(Iterable[int]):
    def __init__(self, n: int):
        self.n = n
    def __iter__(self) -> Iterator[int]:
        count, a, b = 0, 0, 1
        while count < self.n:
            yield a
            a, b = b, a + b
            count += 1

# Explanation:
# - Classic iterable producing a finite Fibonacci sequence.


# ============================================================
# 15) DEPENDENCY INJECTION VIA PROTOCOLS
# ============================================================

class Notifier(Protocol):
    def send(self, to: str, message: str) -> None: ...

class EmailNotifier:
    def send(self, to: str, message: str) -> None:
        print(f"[Email] to={to} message={message}")

class SMSNotifier:
    def send(self, to: str, message: str) -> None:
        print(f"[SMS] to={to} message={message}")

class AuthService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier
    def signup(self, user: User) -> None:
        self.notifier.send(user.username, "Welcome aboard!")

# Explanation:
# - Depends on behavior (Notifier), not a specific implementation.


# ============================================================
# 16) METACLASS (MINIMAL EXAMPLE)
# ============================================================

class AutoRegister(type):
    registry: Dict[str, type] = {}
    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != "BaseRegistered":
            AutoRegister.registry[name] = cls
        return cls

class BaseRegistered(metaclass=AutoRegister):
    pass

class Alpha(BaseRegistered):
    pass

class Beta(BaseRegistered):
    pass

# Explanation:
# - Metaclass intercepts class creation to auto-register subclasses.


# ============================================================
# 17) SMALL UTILS FOR DEMO
# ============================================================

def demo_shapes(shapes: Iterable[Shape]) -> List[Tuple[str, float, float]]:
    return [(type(s).__name__, round(s.area(), 3), round(s.perimeter(), 3)) for s in shapes]


# ============================================================
# 18) MAIN DEMO
# ============================================================

def main() -> None:
    print("=== BASIC CLASS / PROPERTY / CLASS/STATIC METHODS ===")
    u1 = User("alice@example.com", 20)
    u2 = User.from_dict({"username": "alice@example.com", "age": 20})
    print(u1, u1 == u2, User.is_adult(u1.age))
    print()

    print("=== ENCAPSULATION (BankAccount) ===")
    acct = BankAccount("Alice", 100)
    acct.deposit(50); acct.withdraw(20)
    print("Balance:", acct.balance)
    print()

    print("=== INHERITANCE & POLYMORPHISM ===")
    songs = chorus([Dog("Rex"), Cat("Misty")])
    print("\n".join(songs))
    print()

    print("=== ABCs (Shape) ===")
    data = demo_shapes([Rectangle(3, 4), Circle(2.5)])
    for name, a, p in data:
        print(f"{name}: area={a}, perimeter={p}")
    print()

    print("=== MIXINS / MULTIPLE INHERITANCE ===")
    entry = LogEntry("INFO", "Started job")
    print("Serialized:", entry.to_json(), "| ts:", round(entry.timestamp(), 3))
    print()

    print("=== COMPOSITION (Order) ===")
    order = Order(
        Customer("Alice"),
        [LineItem("Book", 2, 12.49), LineItem("Pen", 5, 1.2)]
    )
    print("Order total:", order.total())
    print()

    print("=== DUNDER METHODS (Vector) ===")
    v1, v2 = Vector(3, 4), Vector(1, 2)
    print("v1:", v1, "magnitude:", round(v1.magnitude(), 3))
    print("v1 + v2:", v1 + v2)
    print("3 * v2:", 3 * v2)
    print()

    print("=== PROTOCOLS (Renderer) ===")
    report = {"users": 3, "active": 2}
    print("HTML:", show_report(HTMLRenderer(), report))
    print("JSON:", show_report(JSONRenderer(), report))
    print()

    print("=== DATA CLASSES (AppConfig) ===")
    cfg = AppConfig(env="prod", debug=False, features=("cache", "metrics"))
    print(cfg)
    print()

    print("=== FACTORY PATTERN (Payment) ===")
    gateway = PaymentFactory.create("stripe")
    print(gateway.pay(49.99))
    print()

    print("=== STRATEGY PATTERN (Discounts) ===")
    co1 = Checkout(NoDiscount())
    co2 = Checkout(PercentageDiscount(15))
    co3 = Checkout(ThresholdDiscount(threshold=20, subtract=5))
    print("NoDiscount:", co1.final_total(order))
    print("15% off:", co2.final_total(order))
    print("Threshold £5 off:", co3.final_total(order))
    print()

    print("=== OBSERVER PATTERN (EventEmitter) ===")
    emitter = EventEmitter()
    emitter.on("saved", lambda rid: print(f"Listener A: saved id={rid}"))
    def listener_b(rid): print(f"Listener B: saved id={rid}")
    emitter.on("saved", listener_b)
    emitter.emit("saved", 42)
    emitter.off("saved", listener_b)
    emitter.emit("saved", 99)
    print()

    print("=== CONTEXT MANAGER (Timer) ===")
    with Timer() as t:
        sum(i*i for i in range(1_000_0))
    print(f"Elapsed ~ {t.elapsed:.6f}s")
    print()

    print("=== ITERATOR / ITERABLE (Fibonacci) ===")
    print(list(Fibonacci(10)))
    print()

    print("=== DEPENDENCY INJECTION via Protocol ===")
    auth_email = AuthService(EmailNotifier())
    auth_sms = AuthService(SMSNotifier())
    auth_email.signup(u1)
    auth_sms.signup(u1)
    print()

    print("=== METACLASS (AutoRegister) ===")
    print("Registry keys:", list(AutoRegister.registry.keys()))
    print()

    print("=== __slots__ DEMO (Vector) ===")
    try:
        v1.new_attr = 123  # will raise AttributeError due to __slots__
    except AttributeError as e:
        print("Slots blocked dynamic attr:", e)

if __name__ == "__main__":
    main()

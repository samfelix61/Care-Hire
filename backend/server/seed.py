from faker import Faker
from models import db, User, CarOwner, Car, Review, Booking
from app import app, bcrypt

faker = Faker()

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Seed users
        user1 = User(
            name="John Doe",
            email="john.doe@example.com",
            password=bcrypt.generate_password_hash("hashed_password_1").decode("utf-8"),
            role="user",
            profile_image=None,
            phone_number="1234567890"
        )
        db.session.add(user1)
        
        user2 = User(
            name="Jane Smith",
            email="jane.smith@example.com",
            password=bcrypt.generate_password_hash("hashed_password_2").decode("utf-8"),
            role="admin",
            profile_image=None,
            phone_number="0987654321"
        )
        db.session.add(user2)
        
        db.session.commit()

        # Seed car owner
        car_owner = CarOwner(
            name="Car Owner 1",
            phone_number="111222333",
            profile_image=None
        )
        db.session.add(car_owner)
        db.session.commit()

        # Seed car
        car = Car(
            make="Toyota",
            model="Camry",
            year=2020,
            price_per_day=50,
            availability_status=True,
            car_image_url=None,
            owner_id=car_owner.id  # Ensure this matches the actual owner_id after creation
        )
        db.session.add(car)
        db.session.commit()

        # Seed review
        review = Review(
            user_id=user1.id,  # Ensure this matches the actual user_id after creation
            car_id=car.id,   # Ensure this matches the actual car_id after creation
            rating=5,
            comment="Great car!"
        )
        db.session.add(review)
        db.session.commit()

        # Seed booking
        booking = Booking(
            user_id=user1.id,  # Ensure this matches the actual user_id after creation
            car_id=car.id,   # Ensure this matches the actual car_id after creation
            start_date="2023-07-10",
            end_date="2023-07-15",
            car_owner_id=car_owner.id  # Ensure this matches the actual car_owner_id after creation
        )
        db.session.add(booking)
        db.session.commit()

        print("Database seeded!")

print("Started seeding data...")
seed_data()
print("Finished seeding data...")

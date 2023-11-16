from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

from form_template_obtainer.domain import entities
from form_template_obtainer.interfaces import FormTemplateRepository


class MongoDBFormTemplateRepository(FormTemplateRepository):
    def __init__(
            self,
            host: str,
            port: int,
            user: str,
            password: str,
            database_title: str,
            collection_title: str,
    ) -> None:
        client: MongoClient = AsyncIOMotorClient(
            host=host,
            port=port,
            username=user,
            password=password,
        )
        db = client[database_title]
        self._coll = db[collection_title]

    async def get_form_template_name(self, fields: list[entities.FormField]) -> str | None:

        pipeline = [
            {"$match": {field.name: {"$in": [field.type_, None]} for field in fields}},
            {
                "$addFields": {
                    "matchingCount": {
                        "$size": {
                            "$setIntersection": [
                                [
                                    {"k": field.name, "v": field.type_.value}
                                    for field in fields
                                ],
                                {"$objectToArray": "$$ROOT"},
                            ]
                        }
                    }
                }
            },
            {"$sort": {"matchingCount": -1}},
            {"$limit": 1},
        ]

        async_cursor = self._coll.aggregate(pipeline)

        result = await async_cursor.to_list(length=None)

        if not result:
            return
        # exclude _id name matchingCount
        if result[0]["matchingCount"] < max(len(result[0]) - 3, 0):
            return
        return result[0]["name"]

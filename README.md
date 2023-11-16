# test_task

## Configuration

### Environment

Environment variables for mongo
- host - ip of mongo
- port - port of mongo
- collection - name of target mongo collection
- database - name of target mongo database
- user - name of mongo user
- password - password of mongo user



### Docker-compose
```yaml
version: '3'
services:
  mongo:
    container_name: mongo
    image: mongo
    hostname: mongo
    command: mongod --auth
    environment:
      - MONGO_INITDB_ROOT_USERNAME=user
      - MONGO_INITDB_ROOT_PASSWORD=password
    ports:
      - "27017:27017"
    volumes:
      - "./data:/data/db"
  form_obtainer:
    container_name: form_obtainer
    build: .
    hostname: form_obtainer
    environment:
      - collection=templates
      - database=form
      - host=mongo
      - user=user
      - password=password
      - port=27017
    ports:
      - "10000:10000"
```

## Настройка mongo
Необходимо:

1. Добавить `database` с названием `form`
2. Добавить `collection` с названием `templates`
3. Загрузить документы в коллекцию (возможно тестовые шаблоны форм из файла `test_templates.json`)

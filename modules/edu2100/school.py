from dataclasses import dataclass


@dataclass
class School:
    name: str
    municipality: str
    okrs: list

    @classmethod
    def from_manifest(cls, data):
        school_data = data.get("escola", data)
        return cls(
            name=school_data.get("nome", "Escola não informada"),
            municipality=school_data.get("municipio", "Município não informado"),
            okrs=school_data.get("metas_okr", []),
        )
export interface IDataState{

    Countries: Country[];

}

export interface Country{
    country: country;
    country_id: number;
    id: number;

}


export interface country{
    about: string;
    area: string;
    capital: string;
    density: string;
    id: number;
    language: string;
    population: string;
    title: string;
    images: image[];
}


export interface image{
    id: number;
    path: string;
}
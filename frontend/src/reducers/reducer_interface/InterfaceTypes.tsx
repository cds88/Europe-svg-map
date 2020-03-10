import {Country} from '../reducer_data/DataTypes';

export interface IInterfaceState{
    isModalOpened: boolean;
    CurrentCountry : string;
    countryHovered: string;
    CurrentCountryDetails: Country
}


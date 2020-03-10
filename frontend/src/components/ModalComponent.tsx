
import * as React from "react";


import { AllAppActions } from '../reducers/actions/AllActionsTypes';

import { ThunkDispatch }  from "redux-thunk";
import { bindActionCreators }  from 'redux';
import {AppState} from "../reducers/ConfigureStore";
import {connect} from 'react-redux';

import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Slider from 'react-slick';
import { Country } from '../reducers/reducer_data/DataTypes'; 

import {CSSTransition} from 'react-transition-group';

import * as allActions from '../reducers/actions/AllActions';
import * as dataConstants from '../reducers/reducer_data/DataTypes';
export interface ModalProps{
        country_id: string;
        isModalOpened: boolean;

}

interface LinkStateToProps{
    currentCountry : dataConstants.Country
}

const mapStateToProps=(state:AppState,
ownProps:ModalProps):LinkStateToProps=>
({ 
    currentCountry: state.InterfaceReducer.CurrentCountryDetails
} ) 

interface LinkDispatchToProps{
    closeModal:()=>void;
}

const mapDispatchToProps=(
    dispatch: ThunkDispatch<any, any, AllAppActions>,
    ownProps: ModalProps
):LinkDispatchToProps=>({
    closeModal: bindActionCreators(allActions.CloseModal, dispatch),
})

type Props =ModalProps & LinkStateToProps & LinkDispatchToProps;

const ModalComponent=(Props:Props)=>{
    const modalWrapper = React.useRef(null);
    let imageGallery: any = null;


    const closeModal = (ref: any) => {
        function closePopup(event: any) {
            if (ref.current && !ref.current.contains(event.target)) {
                Props.closeModal();
            }
        }
        React.useEffect(() => {
            document.addEventListener('mousedown', closePopup)
        })
    }
    closeModal(modalWrapper);
    var imagesGallery = Props.currentCountry.country.images.map(
        (image, index) => {
            var path = "http://127.0.0.1:8000/storage/images/" + Props.currentCountry.country.title + "/" + image.path;
            return (
                <div className="page-scroll" key={index}>
                    <img src={path} alt="" />
                </div>
            )
        }
    )
    const galleryPrev = () => {
        imageGallery.slickPrev();
    }
    const galleryNext = () => {
        imageGallery.slickNext();
    }
 
   React.useEffect(()=>{
       //alert(Props.country_id);
   }, [ Props.country_id])


    return (

        <div className="modal-gallery" ref={modalWrapper}>
 

            <Slider
                speed={500}
                slidesToShow={1}
                slidesToScroll={1}
                infinite={true}
                dots={true}
                arrows={false}
                ref={slider => imageGallery = slider} >
              
 
            {imagesGallery}


            </Slider>
            <button onClick={galleryPrev} className="btn btn-secondary gallery-control">Back</button>
            <button onClick={galleryNext} className="btn btn-secondary gallery-control" >Next</button>


        </div>
    )

}

export default connect(mapStateToProps, mapDispatchToProps)(ModalComponent)
    
===============================================
===============================================

Autodesk FBX SDK
Version 2011.3

May 14th, 2010

--

Welcome to the FBX SDK 2011.3
 
This document includes the latest changes 
since the version 2011.2 of the 
Autodesk FBX SDK. 

Sincerely, 
Autodesk FBX SDK team

===============================================


Autodesk FBX SDK 2011.3

1.0 New features and deprecated code
2.0 Bugfixes
3.0 Readme from previous release
4.0 Legal Disclaimer 


========
1.0 New Features and deprecated code

    1.1 - Augmented the FBX SDK reference documentation for a certain number of classes.
    
    1.2 - Added the new class KFbxCachedEffect node attribute. 
    
    1.3 - The FBX SDK now ships as a dynamic library on all platforms. Please note that,
          on the Windows platform, you will need to define KFBX_DLLINFO in your projects
          to correctly build your application using the new FBX SDK dll libraries (see the 
          provided examples).

========
2.0 Bugfixes 
    
========
    2.1 - Fixed a crash in  EmulateNormalsByPolygonVertex.
    2.2 - Augmented the KFbxCache class to correctly support multiple data channels.
    
========
3.0 Readme from previous release
        
        Autodesk FBX SDK 2011.2
        
        1.0 New Features and deprecated code
        
            1.1 The class KFbxSystemUnit changed the use of the pMultiplier parameter.
                In previous versions of the FBX SDK, the pMultiplier was first multiplied by the pScaleFactor 
                before being stored (and used) inside the class. Starting from this version, the pMultiplier is stored
                (and used) without any modification to its value.
                
            1.2 Augmented the configurable options of the class KFbxSystemUnit.
                More options have been added to customize the behavior of the KFbxSystemUnit class. Note that it is
                strongly suggested to use the default configuration since it has been tested and approved to give the best
                results. Changing the default options will have a a direct impact on the whole scene behavior.

            1.3 KFbxTakeNodeContainer class is no more!
                This class has been removed with the introduction of the new animation system that now support
                animation layers. The new classes you will find are:
                   KFbxAnimStack - replaces the old KFbxTake class, contains the animation layers
                   KFbxAnimLayer - new class representing an animation layer
                   KFbxAnimCurveNode - replaces KFCurveNode, uses channels instead of hierarchy to describe property types
                   KFbxAnimCurve - replaces KFCurve, a re-implementable class that is now connectable

            1.4 New animation evaluation system
                We introduced a new class, KFbxAnimEvaluator, that can be re-implemented for your needs. It essentially
                extract the evaluation code that used to reside in KFbxNode. It also support evaluating animation layers.
                This class replaces the functions in KFbxNode: GetGlobalFromCurrentTake, GetPosition, etc. and centralize
                them in one single class. So, if you have TRS animation and/or property animation, you now have to use
                the evaluator to get the resulting animation.

            1.5 Default FBX version upgraded to 7.1!
                From now on, when export new FBX files, the FBX SDK will export them in FBX 7.1 format. This new format
                supports instances and reduce the file size considerably. It also make it possible to store objects with
                identical names, since connections are stored using IDs.

            1.6 FBX SDK Scripting support through Python Binding
                A new python binding is now available for use, check it out!

            1.7 New Import Progress functions
                It is now possible to retrieve the import/export progress using the function SetProgressCallback for single
                thread, or GetProgress if the import/export was done non-blocking.
              
            1.8 Support of float array in the KFbxCache class
                The KFbxCache class has been extended to support the array of float type.
                
            1.9 The assignment operator has been replaced by a Copy() method
                To avoid possible calls to the implicit assignment operator for KFbxObject (and derived classes), the assignment
                operator has been disabled and is replaced by the virtual function "Copy" that can be overloaded in the derived
                classes.
        
        ========
        2.0 Bugfixes 

            2.1 - Fixed a crashing bug when importing some legacy MotionBuilder FBX 5.0 files.
            2.2 - Corrected the computation of the smoothing groups for in mesh Triangulation function.
            2.3 - Fixed Localization problems on the DAE, DFX and OBJ readers/writers.
            2.4 - Extended the file size limit for FBX files from 2GB to 4GB.
        
        
        Autodesk FBX SDK 2010.2

        ========
        2.0 Bugfixes 
        
            2.1 Removed limitation of having the / (slash) character in user properties names.
            2.2 Fixed a "stack overflow near buffer" error in the KFbxRenamingStrategy.
            2.3 Added the support of the KFbxLayerElementTexture::eOVER blend mode in the FBX readers.

            
        Autodesk FBX SDK 2010.2 Beta 2
        
        1.0 New Features and deprecated code
        
            1.1 Added support for display layers by introducing the new class KFbxDisplayLayer.
            
            
        Autodesk FBX SDK 2010.2 Beta 1
        
        1.0 New Features and deprecated code

            1.1 Added a new blending mode for layered textures.
            1.2 Improved processing speed of the protected KFbxMesh::FindPolygonIndex() method used to
                find the polygon index for the given edge.
            1.3 Remove SetFileFormat() from KFbxImporter/KFbxExporter.
                KFbxImporter/KFbxExporter::Initialize() will detect the file format automatically. Or set the file format in Initialize().
            1.4 Added support for stereo cameras by introducint the new class KFbxCameraStereo.
            1.5 Extended the class KFbxMesh to provide support for mesh smoothing. The following functions have been added:
                    - Get/SetEdgeCreaseInfo
                    - Get/SetVertexCreaseInfo
                    - Get/SetMeshSmoothness
                    - GetMeshPreviewDivisionLevels
                    - Get/SetMeshRenderDivisionLevels
                    - Get/SetMeshContinuity
                    - Get/SetDisplaySubdivisions
                    - Get/SetPreserveBorders
                    - Get/SetPreserveHardEdges
            1.6 Added support for selection sets.
    
        ========
        2.0 Bugfixes 
            2.1 The FBX library can now open and read FBX files regardless of their extension.
            2.2 KFbxProperties Destroy() method now works on all properties.
            2.3 Support MotionBuilder datatype: TextureRotation.
            2.4 Fixed the FBX v5.0 reader to correctly set pivot information whne importing legacy files.
    
    
        Autodesk FBX SDK 2010.0
        
        1.0 New Features and deprecated code
            1.0 No changes from version "Jack" Beta Release Candidate

        1.0 Cleanup of dead code
        1.1 Removed libraries for VisualStudio .net 2003
    
        ========
        2.0 Bugfixes 
    
        2.1 Removed a memory leak.
       
        
        Autodesk FBX SDK "Jack" Beta 2
        1.0 New Features and deprecated code

        1.1 KFbxCache class supports int array.
        1.2 Added the Subdivision Display Smoothness to the KFbxSubdiv class.
        1.3 Added the optional argument to the IsValid() method in the 
            KFbxTrimSurface class to skip the check of boundary curves CV's
            overlaps.
        1.4 Refactoring of the KFbxCamera class
            - updates to class documentation 
            - added methods and properties to manipulate front/back planes & plates
            - deprecated ECameraBackgroundDrawingMode type and replaced with ECameraPlateDrawingMode
            - deprecated ECameraBackgroundPlacementOptions. This has been replaced with the 
              individual properties: FitImage, Center, KeepRatio and Crop
            - deprecated GetBackgroundPlacementOptions() since now the flags are stored in the above
              mentioned properties.
            - deprecated SetViewFrustum(bool pEnable), use SetViewNearFarPlanes()
            - deprecated GetViewFrustum(), use GetViewNearFarPlanes()    

        ========
        2.0 Bugfixes 

        2.1 Support of non-convex polygons in the triangulation algorithms.
        
        
        
        Autodesk FBX SDK "Jack" Beta 1

        1.0 New Features and deprecated code

        1.1 Overload of the new operator is not possible anymore (the FBXSDK_OVERLOAD_NEW_OPERATOR macro 
            has been removed). The usage of the custom memory allocator can only be achieve by using 
            the KFbxMemoryAllocator class.	See the ExportScene05 for an implementation example.
        1.2 Enhanced algorithm for smoothing groups generation.
        1.3 Support of displacement map channel.
        1.4 The class KFbxStreamOptions is now obsolete and is gradually being replaced by the 
            class KFbxIOSettings.
        1.5 Added KFbxConstraintCustom class.
        1.6 Added KFbxContainerTemplate class.
        1.7 Added KFbxSubdiv class.
        1.8 Added KFbxEmbeddedFilesAccumulator class.

        2.0 Bugfixes 

        2.1 Adjusted tangents to stay closer to the real value when the weight gets ridiculously small.
        2.2 Fixed Collada plug-in to handle operating system locale. Depending on the locale, the decimal 
            point for numbers may have been represented with the comma instead of the point causing 
            parsing errors.
        2.3 Fixed support for the floor contact to the KFbxCharacter.
        2.4 Fixed infinite loop when loading .obj files on MAC OS.
        2.5 Removed some more memory leaks.  

        
		Autodesk FBX SDK 2009.3
        
        1.0 New Features and deprecated code

        1.1	Added the HasDefaultValue(KFbxProperty&) function to check if a property value 
            has changed from its default one.
        1.2	Added the BumpFactor property to the SurfaceMaterial class.
        1.3 Defined plugins of plugins interface in the fbxsdk manager. See the 
            Autodesk FBX SDK PRW readme file for more details.
        1.4 Re-factoring of the renaming strategy object.
        1.5 Removed unused eCONSTRAINT from the KFbxNodeAttribute.
        1.6 Deprecated FillNodeArray and FillNodeArrayRecursive

            the two methods that used the EAttributeType argument have been marked deprecated.
        	The replacement functions are the ones receiving the kFbxClassId argument.
            
        2.0 Bugfixes 

        2.1	Overwrite empty relative filename in texture objects with the correct value.
        2.2 Fix for internal TRS cache so it correctly get reset when changing takes.
        2.3	Bug fixes in the Collada reader/writer.
        2.4 Fixed a bug that was causing the loss of Shape animation on NURBS objects.
        2.5	Fixed the fact that the layers were losing their name after a clone.
        2.6 Corrections for pivot conversion functions:
            - Set source pivot to ACTIVE in function ResetPivotSetAndConvertAnimation.
            - Update default transformation values to match the results of the pivot 
        	  conversion functions.
        2.7 Fixed the endless loop in the RemoveChar() method of the KString class.
        2.8 Fixed default values in the KFbxCharacter structure.	   
            

        Autodesk FBX SDK 2009.1

		1.0 New features and deprecated classes
		    1.1  Examples: New samples
		    1.2  Documentation: New programmer's guide
		    1.3  New material management
		    1.4  New classes
		    1.5  Deprecated classes
		    1.6  New way to access FCurves
		    1.7  Support of hardware shaders
		    1.8  Support for smoothing groups
		    1.9  Bugfixes and Enhancements
		    1.10 Support for Mac OS X Architectures
		    1.11 EULA
		    
		2.0 Legal Disclaimer 


		========
		1.1 Examples: New samples

		New examples have been added in directory 
		examples/UI Examples. These examples are for the
		Windows platform only. They are very simple examples
		for beginner users of the FBX SDK.
		- ImportExport - Import and Export a FBX file.
		- SceneTreeView - View a FBX scene.
		- CubeCreator - Create cubes dynamically, with
		  materials, textures, animation, etc.


		========
		1.2 Documentation: New programmer's guide

		A new document: FBX_SDK_Programmers_Guide_2009_1.pdf has
		been added to the documentation. This document targets
		starters and beginner users of the FBX SDK.


		========
		1.3 New material and textures management

		Materials are added directly to the node that they are
		applied to, i.e. the parent node of the geometry, 
		instead of being added to the direct array of the material
		layer element. This is the case whatever the reference mode
		is set on the material layer element.

		Because of this, materials must be added after the node 
		is created and the node attribute is set.
		The layer element material index array is still used. 
		Each element in the index array now represents an index 
		into the material connections to the node that places 
		the geometry in the scene.

		Example:

		Deprecated behavior:
		    lLayerElementMaterial->GetDirectArray().Add(lMaterial);

		New behavior:
		    KFbxNode* lNode = pMesh->GetNode();
		    if(lNode)   
		        lNode->AddMaterial(lMaterial);

		Textures are connected to material properties that they drive, 
		instead of being added to layer elements. The 
		KFbxTexture::UVSet property determines which UV set 
		is used for the texture, for a given geometry.

		Example:
		Connecting a diffuse texture to the first material of a mesh:

		if (pMesh->GetNode()) {
			int lNbMaterial = pMesh->GetNode()->GetSrcObjectCount( KFbxSurfaceMaterial::ClassId );
			if (lNbMaterial > 0)
			{
				KFbxSurfaceMaterial *lDiffuseMaterial = (KFbxSurfaceMaterial*)pMesh->GetNode()->GetSrcObject(KFbxSurfaceMaterial::ClassId, 0);
				KFbxProperty lPropDiffuse = lDiffuseMaterial->FindProperty( KFbxSurfaceMaterial::sDiffuse );
				if( lPropDiffuse.IsValid() )
					lPropDiffuse.ConnectSrcObject( lTexture );
			}
		}


		To read a texture connected to a of a Mesh:

		if (pMesh->GetNode()) 
		{
			int lNbMaterial = pMesh->GetNode()->GetSrcObjectCount( KFbxSurfaceMaterial::ClassId );
			for(int lMatCounter=0; lMatCounter < lNbMaterial; ++lMatCounter)
			{
				KFbxSurfaceMaterial *lMaterial = (KFbxSurfaceMaterial*)pMesh->GetNode()->GetSrcObject(KFbxSurfaceMaterial::ClassId, lMatCounter);
		    
		        KFbxProperty lPropDiffuse = lMaterial->FindProperty( KFbxSurfaceMaterial::sDiffuse );
		        if( lPropDiffuse.IsValid() )
		        {

		            int lLayeredTextureCount = lPropDiffuse.GetSrcObjectCount(KFbxLayeredTexture::ClassId);
		            if(lLayeredTextureCount > 0)
		            {
		                for(int j=0; j<lLayeredTextureCount; ++j)
		                {
		                    KFbxLayeredTexture *lLayeredTexture = (KFbxLayeredTexture*)lPropDiffuse.GetSrcObject(KFbxLayeredTexture::ClassId, 0);
		                    int lNbTextures = lLayeredTexture->GetSrcObjectCount(KFbxTexture::ClassId);
		                    for(int k =0; k<lNbTextures; ++k)
		                    {
		                        //let's say I want to blendmode of that layered texture:
		                        KFbxLayeredTexture::EBlendMode lBlendMode;
		                        lLayeredTexture->GetTextureBlendMode(k, lBlendMode);
		                        KFbxTexture* lTexture = KFbxCast <KFbxTexture> (lLayeredTexture->GetSrcObject(KFbxTexture::ClassId,j));
		                        KString lTemp = lTexture->GetRelativeFileName();
		                    }
		                }
		            }
		            else
		            {
		                int lNbTextures = lPropDiffuse.GetSrcObjectCount(KFbxTexture::ClassId);
		                for(int j =0; j<lNbTextures; ++j)
		                {
		                    KFbxTexture* lTexture = KFbxCast <KFbxTexture> (lPropDiffuse.GetSrcObject(KFbxTexture::ClassId,j));
		                    KString lTemp = lTexture->GetRelativeFileName();
		                }
		            }
		        }
		    }
		}

		UV layer elements are always stored in the "diffuse" slot
		of the layer on which they are set simply because the 
		diffuse slot is the default slot for UVs.

		Backwards compatibility:
		Users can still add materials and textures using the 
		layer elements. The FBX SDK will convert the layer
		elements into connections to the node. Similarly, 
		FBX files are converted internally when they are read 
		by the SDK.


		========
		1.4 New classes

		KFbxPropertyHandle - for property management

		KFbxDocument - a generalization of KFbxScene. A KFbxDocument
		can hold many scenes.
		KFbxCollection - container class for KFbxDocument.
		KFbxDocumentInfo - replaces KFbxSceneInfo.

		KFbxIOSettings - class to replace stream options.

		KFbxCloneManager - Utility for cloning entire networks of 
		KFbxObjects. Options are availible for specifying how the 
		clones inherit the connections of the original.

		KFbxDataType - New types definition.

		KFbxLayeredTexture - Layered textures can be defined within
		a single layer with this new class. No need to create 
		multiple layers and put a texture on each of them
		anymore.

		KFbxLibrary - Generic library of FBX objects

		KFbxCameraManipulator - Provides basic camera manipulation 
		in any program using it.

		// Type definitions
		KFbxDataTypes defines new types:
		DTBlob - Uninitialized data of a specfified size, to be
		filled by the user.
		DTDistance - distance
		DTDateTime - date and time

		KTimeModeObject - time mode information

		KFbxObjectMetaData - Meta data information.


		========
		1.5 Deprecated functions
		For KFbxMarker, KFbxNull, KFbxLight and KFbxNode, 
		properties are accessed directly. Accordingly, 
		the corresponding access and setting functions
		are deprecated.

		New properties to use (see class documentation for details)
		KFbxMarker
			KFbxTypedProperty<ELook> Look;
			KFbxTypedProperty<fbxDouble1> Size;
			KFbxTypedProperty<fbxBool1> ShowLabel;
			KFbxTypedProperty<fbxDouble3> IKPivot;
			
		KFbxNull
		    KFbxTypedProperty<fbxDouble1>       Size;
		    KFbxTypedProperty<ELook>            Look;
		    
		KFbxLight
			KFbxTypedProperty<ELightType>		LightType;
			KFbxTypedProperty<fbxBool1>			CastLight;
			KFbxTypedProperty<fbxBool1>			DrawVolumetricLight;
			KFbxTypedProperty<fbxBool1>			DrawGroundProjection;
			KFbxTypedProperty<fbxBool1>			DrawFrontFacingVolumetricLight;
			KFbxTypedProperty<fbxDouble3>		Color;
			KFbxTypedProperty<fbxDouble1>		Intensity;
			KFbxTypedProperty<fbxDouble1>		HotSpot;
			KFbxTypedProperty<fbxDouble1>		ConeAngle;
			KFbxTypedProperty<fbxDouble1>		Fog;
			KFbxTypedProperty<EDecayType>		DecayType;
			KFbxTypedProperty<fbxDouble1>		DecayStart;
			KFbxTypedProperty<fbxString>		FileName;
			KFbxTypedProperty<fbxBool1>			EnableNearAttenuation;
			KFbxTypedProperty<fbxDouble1>		NearAttenuationStart;
			KFbxTypedProperty<fbxDouble1>		NearAttenuationEnd;
			KFbxTypedProperty<fbxBool1>			EnableFarAttenuation;
			KFbxTypedProperty<fbxDouble1>		FarAttenuationStart;
			KFbxTypedProperty<fbxDouble1>		FarAttenuationEnd;
			KFbxTypedProperty<fbxBool1>			CastShadows;
			KFbxTypedProperty<fbxDouble3>		ShadowColor;
			
		KFbxNode
		    KFbxTypedProperty<fbxDouble3>               LclTranslation;
		    KFbxTypedProperty<fbxDouble3>               LclRotation;
		    KFbxTypedProperty<fbxDouble3>               LclScaling;

		    KFbxTypedProperty<KFbxXMatrix>              GlobalTransform;

		    KFbxTypedProperty<fbxDouble1>               Visibility;
		    KFbxTypedProperty<fbxDouble1>               Weight;
		    KFbxTypedProperty<fbxDouble3>               PoleVector;
		    KFbxTypedProperty<fbxDouble1>               Twist;
		    KFbxTypedProperty<fbxDouble3>               WorldUpVector;
		    KFbxTypedProperty<fbxDouble3>               UpVector;
		    KFbxTypedProperty<fbxDouble3>               AimVector;

		    KFbxTypedProperty<fbxBool1>                 QuaternionInterpolate;
		    KFbxTypedProperty<fbxDouble3>               RotationOffset;
		    KFbxTypedProperty<fbxDouble3>               RotationPivot;
		    KFbxTypedProperty<fbxDouble3>               ScalingOffset;
		    KFbxTypedProperty<fbxDouble3>               ScalingPivot;

		    KFbxTypedProperty<fbxBool1>                 TranslationActive;
		    KFbxTypedProperty<fbxDouble3>               Translation;
		    KFbxTypedProperty<fbxDouble3>               TranslationMin;
		    KFbxTypedProperty<fbxDouble3>               TranslationMax;
		    KFbxTypedProperty<fbxBool1>                 TranslationMinX;
		    KFbxTypedProperty<fbxBool1>                 TranslationMinY;
		    KFbxTypedProperty<fbxBool1>                 TranslationMinZ;
		    KFbxTypedProperty<fbxBool1>                 TranslationMaxX;
		    KFbxTypedProperty<fbxBool1>                 TranslationMaxY;
		    KFbxTypedProperty<fbxBool1>                 TranslationMaxZ;

		    KFbxTypedProperty<ERotationOrder>           RotationOrder;
		    KFbxTypedProperty<fbxBool1>                 RotationSpaceForLimitOnly;
		    KFbxTypedProperty<fbxDouble1>               RotationStiffnessX;
		    KFbxTypedProperty<fbxDouble1>               RotationStiffnessY;
		    KFbxTypedProperty<fbxDouble1>               RotationStiffnessZ;
		    KFbxTypedProperty<fbxDouble1>               AxisLen;

		    KFbxTypedProperty<fbxDouble3>               PreRotation;
		    KFbxTypedProperty<fbxDouble3>               PostRotation;
		    KFbxTypedProperty<fbxBool1>                 RotationActive;
		    KFbxTypedProperty<fbxDouble3>               RotationMin;
		    KFbxTypedProperty<fbxDouble3>               RotationMax;
		    KFbxTypedProperty<fbxBool1>                 RotationMinX;
		    KFbxTypedProperty<fbxBool1>                 RotationMinY;
		    KFbxTypedProperty<fbxBool1>                 RotationMinZ;
		    KFbxTypedProperty<fbxBool1>                 RotationMaxX;
		    KFbxTypedProperty<fbxBool1>                 RotationMaxY;
		    KFbxTypedProperty<fbxBool1>                 RotationMaxZ;

		    KFbxTypedProperty<ETransformInheritType>    InheritType;

		    KFbxTypedProperty<fbxBool1>                 ScalingActive;
		    KFbxTypedProperty<fbxDouble3>               Scaling;
		    KFbxTypedProperty<fbxDouble3>               ScalingMin;
		    KFbxTypedProperty<fbxDouble3>               ScalingMax;
		    KFbxTypedProperty<fbxBool1>                 ScalingMinX;
		    KFbxTypedProperty<fbxBool1>                 ScalingMinY;
		    KFbxTypedProperty<fbxBool1>                 ScalingMinZ;
		    KFbxTypedProperty<fbxBool1>                 ScalingMaxX;
		    KFbxTypedProperty<fbxBool1>                 ScalingMaxY;
		    KFbxTypedProperty<fbxBool1>                 ScalingMaxZ;

		    KFbxTypedProperty<fbxDouble3>               GeometricTranslation;
		    KFbxTypedProperty<fbxDouble3>               GeometricRotation;
		    KFbxTypedProperty<fbxDouble3>               GeometricScaling;

		    // Ik Settings
		    //////////////////////////////////////////////////////////
		    KFbxTypedProperty<fbxDouble1>               MinDampRangeX;
		    KFbxTypedProperty<fbxDouble1>               MinDampRangeY;
		    KFbxTypedProperty<fbxDouble1>               MinDampRangeZ;
		    KFbxTypedProperty<fbxDouble1>               MaxDampRangeX;
		    KFbxTypedProperty<fbxDouble1>               MaxDampRangeY;
		    KFbxTypedProperty<fbxDouble1>               MaxDampRangeZ;
		    KFbxTypedProperty<fbxDouble1>               MinDampStrengthX;
		    KFbxTypedProperty<fbxDouble1>               MinDampStrengthY;
		    KFbxTypedProperty<fbxDouble1>               MinDampStrengthZ;
		    KFbxTypedProperty<fbxDouble1>               MaxDampStrengthX;
		    KFbxTypedProperty<fbxDouble1>               MaxDampStrengthY;
		    KFbxTypedProperty<fbxDouble1>               MaxDampStrengthZ;
		    KFbxTypedProperty<fbxDouble1>               PreferedAngleX;
		    KFbxTypedProperty<fbxDouble1>               PreferedAngleY;
		    KFbxTypedProperty<fbxDouble1>               PreferedAngleZ;
		    ///////////////////////////////////////////////////////

		    KFbxTypedProperty<fbxReference*>            LookAtProperty;
		    KFbxTypedProperty<fbxReference*>            UpVectorProperty;

		    KFbxTypedProperty<fbxBool1>                 Show;
		    KFbxTypedProperty<fbxBool1>                 NegativePercentShapeSupport;

		    KFbxTypedProperty<fbxInteger1>              DefaultAttributeIndex;   
		    

		Default take node and current take node used to always
		be set, whatever the object, even if there was no 
		animation. Now default and current take node can be NULL.

		The syntax of the functions to get shape channels and
		fcurves has changed. The take node is not needed to get
		the shape channel.


		========
		1.6 New ways to access FCurves

		The FCurves and FCurveNodes are now accessed via the KFbxProperty 
		that holds them. To retrieve the pointer to the FCurve you need
		to use one of the two GetFCurve() methods. These methods will
		return NULL in the case where the property is not animated. This behavior
		is new.

		To add an animation to the property, you first need to make sure
		that the FCurveNode is present. You can call the GetKFCurveNode()
		method to create the KFCurveNode. Once this node is created, you can
		then call GetFCurve() to have access to the KFCurve object and fill
		it with keys.


		Example 1: Get the translation X fcurve 

		    // retrieve from current take
		    KFCurve* tx = LclTranslation.GetKFCurve("X"); 
		    if (tx) DoSomethingWith(tx);

		    // retrieve from "myTake" take
		    KFCurve* tx1= LclTranslation.GetKFCurve("X", "myTake");
		    if (tx) DoSomethingWith(tx);



		Example 2: Get the visibiltiy fcurve

		    // retrieve from the current take
		    KFCurve* vis = Visibility.GetKFCurve();



		Example 3: Create the Translation KFCurveNode

		    // on the current take
		    LclTranslation.GetKFCurveNode(true);

		    KFCurveNode *tx = LclTranslation.GetFCurve("X");
		    KFCurveNode *ty = LclTranslation.GetFCurve("Y");
		    KFCurveNode *tz = LclTranslation.GetFCurve("Z");

		    AddKeysTo(tx);
		    AddKeysTo(ty);
		    AddKeysTo(tz);       


		For Shapes, the method to access the FCurves (GetShapeChannel(...)) 
		now use the take name instead of the take node.


		========
		1.7 Support of hardware shaders

		CGFX and HLSL hardware shaders are supported.

		For CGFX shaders:
		The Maya FBX plug-in now supports export and import of cgfxShader nodes.
		Simple uniform parameters such as ints, floats and float3s are supported
		on export and import. File textures are also supported, as well as
		positional and directional bindings to other nodes.
		Limitations: Vertex varying parameters settings are not yet supported.

		For HLSL shaders:
		Import and export of HLSL Shader materials from 3ds Max is now supported.
		Simple uniform parameters such as floats, float3s, ints are exported 
		and imported. Bitmap texture parameters and their corresponding map 
		channels are also exported and imported. Light parameter bindings are 
		preserved on export and import.


		An example of how to read those files has been added to the ImportScene example.


		========
		1.8 Support for smoothing groups

		The FBX SDK now supports smoothing groups.  This is a perfect match for 
		smoothing groups exported from the 3ds Max FBX plug-in (2009.1). A polygon 
		is assigned to a group via the mapping mode eBY_POLYGON.

		In the eBY_POLYGON mapping mode, the integer represents a bit mask. 
		The first 32 bits represent the 33 allowed smoothing groups (0 to 32).  For 
		example, if the 32-bit integer value for a given polygon is 6, this would be 
		represented in binary as 00000000 00000000 00000000 00000110, indicating that 
		the polygon is part of groups 2 and 3.  A value of 0 (smoothing group 0) means 
		no smoothing and all of the edges of the polygon are hard.  When two adjacent
		polygons are part of the same smoothing group, their common edge(s) is/are soft.

		If the mapping mode is eBY_EDGE, then the value 0 means that edge is hard. 
		All other values mean the edge is soft (the FBX plug-in uses 1, but this isn't 
		a requirement).

		The KFbxLayerElementSmoothing is now a KFbxLayerElementTemplate <int> instead of
		a KFbxLayerElementTemplate <bool>.

		As in the previous version, the KFbxLayerElementSmoothing can only be set as 
		reference mode eDIRECT.

		For your convenience, there's converting functions in KFbxGeometryConverter called
		ComputePolygonSmoothingFromEdgeSmoothing and ComputeEdgeSmoothingFromPolygonSmoothing.

		Here's an example how to use them:

		//There's a KFbxMesh in the pointer pFbxMesh
		KFbxGeometryConverter lConverter(&lFbxSdkManager);
		bool lRet = lConverter.ComputePolygonSmoothingFromEdgeSmoothing(pFbxMesh);


		========
		1.9 Bugfixes and Enhancements

		The memory footprint has been improved.

		Fixes have been made for memory leaks.


		========
		1.10 Support for Mac OS X Architectures

		The FBX SDK is provided for these architectures:
		 - ppc on Mac OS 10.4 using GCC 3.3
		 - ppc on Mac OS 10.4 using GCC 4.0
		 - i386 on Mac OS 10.4 for GCC 4.0
		 - x86_64 on Mac OS 10.5 for GCC 4.0.
		 
		The FBX SDK is *NOT* available for this architecture:
		 - ppc64 on Mac OS 10.5 for GCC 4.0.


		========
		1.11 EULA

		The End User License Agreement has changed. Report to document License.rtf
		for details.

		===============================================

		2.0 Legal Disclaimer 

		Autodesk and FBX are registered trademarks or 
		trademarks of Autodesk, Inc., in the USA and/or 
		other countries. All other brand names, product 
		names, or trademarks belong to their respective 
		holders. 

		© 2008 Autodesk, Inc. All rights reserved.
		==================================================
		==================================================
		
========


===============================================

4.0 Legal Disclaimer 

Autodesk and FBX are registered trademarks or 
trademarks of Autodesk, Inc., in the USA and/or 
other countries. All other brand names, product 
names, or trademarks belong to their respective 
holders. 

© 2010 Autodesk, Inc. All rights reserved.


==================================================
==================================================

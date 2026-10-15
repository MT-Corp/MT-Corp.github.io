"""Build the static Atelier website. Python standard library only."""
from html import escape as esc
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
CONTACT = 'mtcorp0505@gmail.com'
HOST = 'https://mt-corp.github.io'

COPY = {
 'es': {
  'name':'Español', 'skip':'Ir al contenido', 'language':'Idioma del sitio',
  'nav':['Herramientas','Preguntas','Privacidad'], 'home':'Inicio',
  'title':'Atelier Tools — PDF, QR y documentos',
  'description':'Crea PDF, escanea páginas, genera QR y trabaja con documentos desde Android. Conoce Atelier Tools y su privacidad.',
  'eyebrow':'PDF · QR · Documentos', 'headline':'Dale forma a tus documentos.',
  'lead':'Crea un PDF, digitaliza tus apuntes, prepara un QR o anota una copia de un archivo externo. Tus herramientas documentales, en un mismo espacio.',
  'status':'Nueva versión en preparación', 'status_note':'Estas funciones describen el candidato de la próxima actualización. La versión disponible en Google Play puede ser anterior; algunas funciones requieren un desbloqueo.',
  'explore':'Explorar herramientas', 'privacy':'Leer privacidad', 'icon_alt':'Icono de Atelier Tools',
  'section_eyebrow':'Hecho para trabajar a tu manera', 'section_title':'Del archivo a la idea terminada.',
  'section_lead':'Crea, organiza y comparte sin cambiar de herramienta a cada paso.',
  'cards':[
   ('PDF','Crea y organiza PDF','Añade texto, imágenes y QR. Organiza páginas, ajusta propiedades y guarda tus proyectos para continuar después.'),
   ('✎','Anota y firma una copia','Abre un PDF externo y crea una copia para añadir texto, formas o una firma manuscrita de color. Incluye deshacer y rehacer.'),
   ('▤','Lee tus documentos','Consulta PDF con zoom, páginas y búsqueda. Visualiza PPTX en una presentación estática, con avisos sobre los elementos no compatibles.'),
   ('⌗','Crea y escanea QR','Genera códigos para texto, enlaces y otros datos compatibles. Guarda, comparte en PNG y organiza tus códigos favoritos.'),
   ('▧','Digitaliza páginas','Usa la cámara o tus imágenes, corrige el encuadre y ajusta filtros. El OCR local permite consultar y copiar el texto reconocido.'),
   ('↔','Convierte documentos','Trabaja con conversiones entre PDF, Word y PowerPoint. El resultado depende de la estructura del archivo; revisa siempre la maquetación.')],
  'copy_note':'Editar una copia de un PDF usa páginas rasterizadas como fondo: los elementos nuevos son editables, pero el texto original no se convierte automáticamente en objetos editables. Una firma manuscrita añadida no es una firma digital certificada.',
  'look_title':'Tu estilo también cuenta.', 'look_text':'Temas, superficies Glass y navegación Clásica o Semiluna. Ajusta colores y efectos; el Modo fluido reduce efectos visuales para dar prioridad al uso. Algunos estilos y herramientas tienen acceso temporal o requieren desbloqueo.',
  'faq_title':'Antes de empezar',
  'faq':[
   ('¿Necesito una cuenta?','Atelier no ofrece registro ni inicio de sesión. Tus proyectos se gestionan localmente.'),
   ('¿Todo funciona sin Internet?','La creación y el procesamiento documental son locales. Los anuncios, el consentimiento y los enlaces externos requieren conexión; los anuncios con recompensa dependen de su disponibilidad.'),
   ('¿El OCR y las conversiones son perfectos?','No. El reconocimiento puede fallar con escritura manuscrita, imágenes borrosas o alfabetos no compatibles. Las conversiones pueden alterar fuentes, posición y elementos complejos.'),
   ('¿El lector PPTX reproduce animaciones?','Ofrece visualización y presentación estática. No promete conservar animaciones, transiciones, multimedia ni compatibilidad completa con PowerPoint o Canva.'),
   ('¿Qué se está preparando?','La interfaz en español, inglés y francés está en desarrollo. La IA propia sigue en investigación y no está integrada como un asistente generativo. No hay fecha de disponibilidad anunciada para estas mejoras.')],
  'support_title':'¿Necesitas ayuda?', 'support_text':'Escríbenos con el modelo de tu dispositivo, la versión de Atelier y los pasos del problema. Evita adjuntar documentos personales o contraseñas.', 'contact':'Contactar con soporte',
  'privacy_title':'Política de privacidad', 'updated':'Última actualización: 15 de octubre de 2026',
  'policy_intro':'Esta política describe el tratamiento de datos en Atelier Tools para Android y en este sitio. El responsable de Atelier Tools se identifica públicamente como MT-Corp. Puedes contactar con él mediante el correo indicado al final.',
  'policy':[
   ('local','Documentos y procesamiento local',[
    'La creación y edición de PDF, el escaneo, el reconocimiento de texto y las conversiones documentales disponibles se procesan en el dispositivo. Atelier no envía el contenido de tus documentos, imágenes, firmas, códigos QR o texto reconocido a servidores propios para realizar estas tareas ni para entrenar nuestra IA experimental.',
    'El procesamiento local no significa que toda la aplicación carezca de comunicaciones de red: los SDK publicitarios y técnicos descritos más adelante pueden enviar sus propios datos. La aplicación no incorpora actualmente un servicio de conversación generativa remota.']),
   ('files','Archivos, proyectos y permisos',[
    'Los proyectos y preferencias se guardan en el almacenamiento de la aplicación. Los archivos exportados se guardan en la ubicación que elijas; si seleccionas un proveedor en la nube desde Android, ese proveedor trata los archivos conforme a sus propias condiciones.',
    'La cámara se utiliza al escanear documentos o códigos QR y al tomar fotografías para un proyecto. La selección de imágenes y documentos se realiza mediante los mecanismos disponibles de Android. Puedes denegar o revocar los permisos en los ajustes del sistema; las funciones que los necesitan dejarán de estar disponibles.',
    'Los proyectos pueden contener información sensible porque tú la incorporas, como firmas o datos de contacto codificados en un QR. No incluyas información que no quieras guardar o compartir.']),
   ('ads','Publicidad, datos técnicos y consentimiento',[
    'Atelier utiliza Google AdMob (Google Mobile Ads) para mostrar anuncios en las ubicaciones habilitadas. El SDK puede recoger y compartir dirección IP, ubicación aproximada inferida de ella, identificadores publicitarios o de instalación, interacciones con la aplicación y los anuncios, y datos de diagnóstico y fallos. Google declara su uso para publicidad, análisis y prevención del fraude.',
    'Los anuncios con recompensa son voluntarios y otorgan el acceso indicado en la aplicación cuando se recibe la confirmación de recompensa del proveedor. No se garantiza inventario publicitario ni una recompensa si el anuncio no puede completarse.',
    'Las opciones de consentimiento y privacidad se muestran mediante la plataforma de Google cuando corresponde. Puedes revisar las opciones que la app tenga disponibles y los controles publicitarios de Android. Rechazar la personalización no equivale necesariamente a detener todos los datos técnicos ni todos los anuncios. Eliminar el ID publicitario tampoco elimina necesariamente otros identificadores.',
    'Google declara cifrado TLS para los datos recogidos por su SDK de anuncios. La conservación y los demás tratamientos de esos datos dependen de Google y de los proveedores publicitarios que intervengan, de la configuración aplicable y de sus políticas. No fijamos ni prometemos un plazo de borrado de 90 días para estos datos.']),
   ('ocr','OCR y SDK de reconocimiento',[
    'El reconocimiento de texto con Google ML Kit se ejecuta en el dispositivo. El SDK puede transmitir información técnica como modelo del dispositivo, versión de Android y de la aplicación, identificadores de instalación, configuración, métricas de rendimiento y códigos de eventos o errores para diagnóstico y análisis de uso.',
    'Esta información técnica es distinta del contenido de las imágenes o del texto reconocido. Google declara HTTPS para estas transmisiones y, para los datos descritos en su divulgación de ML Kit, que no los transfiere a terceros.']),
   ('sharing','Compartir y enlaces externos',[
    'Cuando eliges compartir o abrir un resultado con otra aplicación, Android permite seleccionar el destino. El archivo o texto se entrega al destino elegido y su tratamiento posterior depende de esa aplicación. Una copia enviada a otra aplicación ya no se controla desde Atelier.',
    'Abrir un enlace de un QR puede llevarte a un sitio externo. Revisa el destino antes de abrirlo. Los sitios externos, YouTube y los proveedores de almacenamiento aplican sus propias políticas.']),
   ('retention','Conservación y eliminación',[
    'Los proyectos, preferencias y derechos de acceso se conservan localmente mientras sean necesarios o hasta que los elimines mediante las opciones disponibles. Las funciones pueden crear archivos temporales para procesar, exportar o compartir.',
    'Borrar los datos de la aplicación o desinstalarla elimina su almacenamiento privado conforme al comportamiento de Android. No necesariamente elimina exportaciones, copias compartidas ni copias de seguridad administradas por el sistema o por servicios que hayas elegido.',
    'Atelier no ofrece creación de cuentas. No mantenemos una biblioteca propia de tus documentos en un servidor que podamos borrar por correo. Para los datos de Google y otros proveedores, utiliza sus controles de privacidad. Puedes escribirnos para consultar cómo gestionar los datos locales; ese contacto no implica que podamos identificar o borrar todos los registros de un SDK.']),
   ('website','Este sitio web',[
    'Las páginas informativas se alojan en GitHub Pages. No incorporamos formularios de subida de documentos, analítica propia, píxeles publicitarios ni videos de terceros incrustados en estas páginas. GitHub puede tratar información técnica de las visitas, como la dirección IP, para prestar y proteger su servicio conforme a su política.',
    'Si nos escribes por correo, recibimos la dirección del remitente y el contenido que decidas enviarnos. Lo utilizamos para atender tu consulta y lo conservamos mientras sea necesario para ese fin y para las obligaciones aplicables. No envíes contraseñas ni documentos sensibles sin necesidad.']),
   ('rights','Controles y derechos',[
    'Según tu lugar de residencia y el tratamiento de datos aplicable, puedes tener derechos de acceso, corrección, eliminación, oposición o retirada del consentimiento. Para consultas sobre Atelier puedes utilizar el correo de contacto; para datos tratados por proveedores, consulta también sus mecanismos de solicitud.',
    'Los servicios de terceros pueden tratar datos en otros países conforme a sus propias condiciones y salvaguardas. Esta política no garantiza seguridad absoluta ni sustituye los controles de privacidad de Android o del proveedor.']),
   ('children','Menores y cambios',[
    'Atelier no solicita deliberadamente a menores que envíen información personal por soporte. Si crees que un menor nos ha proporcionado información personal, contacta con nosotros. La disponibilidad de anuncios y mensajes debe respetar la audiencia y las opciones de edad aplicables.',
    'Podemos actualizar esta política cuando cambien las funciones o los servicios. La fecha de actualización figura al principio. Las funciones futuras no se consideran activas por su mera mención en una hoja de ruta.'])],
  'provider_title':'Información de los proveedores', 'contact_title':'Contacto de privacidad',
  'contact_text':'Para consultas sobre esta política o sobre los datos que nos hayas enviado por soporte:',
  'toc_title':'Contenido', 'footer':'Herramientas para tus documentos. Información clara sobre tus datos.'
 },
 'en': {
  'name':'English', 'skip':'Skip to content', 'language':'Website language',
  'nav':['Tools','Questions','Privacy'], 'home':'Home', 'title':'Atelier Tools — PDFs, QR codes and documents',
  'description':'Create PDFs, scan pages, generate QR codes and work with documents on Android. Discover Atelier Tools and its privacy practices.',
  'eyebrow':'PDFs · QR codes · Documents', 'headline':'Bring your documents together.',
  'lead':'Create a PDF, scan your notes, make a QR code or annotate a copy of an existing file. Your document tools, in one place.',
  'status':'An update is in preparation', 'status_note':'These features describe the upcoming release candidate. The version available on Google Play may be older; some features require an unlock.',
  'explore':'Explore the tools', 'privacy':'Read the privacy policy', 'icon_alt':'Atelier Tools app icon',
  'section_eyebrow':'Work your way', 'section_title':'From file to finished work.', 'section_lead':'Create, organise and share without switching tools at every step.',
  'cards':[
   ('PDF','Create and organise PDFs','Add text, images and QR codes. Arrange pages, adjust properties and save your projects to continue later.'),
   ('✎','Annotate and sign a copy','Open an existing PDF and create a copy to add text, shapes or a coloured handwritten signature. Undo and redo are included.'),
   ('▤','Read your documents','Browse PDFs with zoom, page navigation and search. View PPTX files as static presentations, with notices about unsupported elements.'),
   ('⌗','Create and scan QR codes','Generate codes for text, links and other supported data. Save, share as PNG and organise your favourites.'),
   ('▧','Scan your pages','Use your camera or existing images, correct the crop and apply filters. On-device OCR lets you view and copy recognised text.'),
   ('↔','Convert documents','Convert between PDF, Word and PowerPoint formats. Results depend on the file structure; always check the layout.')],
  'copy_note':'Editing a copy of a PDF uses rasterised pages as a background: new elements remain editable, but existing text is not automatically turned into editable objects. Adding a handwritten signature does not create a certified digital signature.',
  'look_title':'Make it feel like yours.', 'look_text':'Themes, Glass surfaces and Classic or Semiluna navigation. Adjust colours and effects; Smooth mode reduces visual effects to prioritise usability. Some styles and tools require an unlock or provide temporary access.',
  'faq_title':'Before you start',
  'faq':[
   ('Do I need an account?','Atelier has no account registration or sign-in. Your projects are managed locally.'),
   ('Does everything work offline?','Document creation and processing run on your device. Ads, consent services and external links need a connection; rewarded ads depend on availability.'),
   ('Are OCR and conversions always accurate?','No. Recognition may fail with handwriting, blurred images or unsupported scripts. Conversions may change fonts, positioning and complex elements.'),
   ('Does the PPTX reader play animations?','It provides static viewing and presentation. It does not promise to preserve animations, transitions, multimedia or full PowerPoint or Canva compatibility.'),
   ('What is in development?','A Spanish, English and French app interface is in development. Our own AI remains a research project and is not integrated as a generative assistant. No release date has been announced for these improvements.')],
  'support_title':'Need a hand?', 'support_text':'Email your device model, Atelier version and the steps that led to the problem. Avoid attaching personal documents or passwords.', 'contact':'Contact support',
  'privacy_title':'Privacy policy', 'updated':'Last updated: 15 October 2026',
  'policy_intro':'This policy describes how data is handled in Atelier Tools for Android and on this website. The party responsible for Atelier Tools publicly operates as MT-Corp. You can contact it using the email address at the end of this policy.',
  'policy':[
   ('local','Documents and on-device processing',[
    'Available PDF creation and editing, scanning, text recognition and document conversions run on your device. Atelier does not send the contents of your documents, images, signatures, QR codes or recognised text to its own servers to perform these tasks or to train our experimental AI.',
    'On-device processing does not mean the entire app is free of network communications: the advertising and technical SDKs described below may transmit their own data. The app does not currently include a remote generative conversation service.']),
   ('files','Files, projects and permissions',[
    'Projects and preferences are stored in app storage. Exported files are saved to the location you choose; if you select a cloud provider through Android, that provider handles the files under its own terms.',
    'The camera is used to scan documents or QR codes and to take pictures for a project. Images and documents are selected through the mechanisms available on Android. You can deny or revoke permissions in system settings; features that need them will then be unavailable.',
    'Projects may contain sensitive information that you add, such as signatures or contact details encoded in a QR code. Do not include information you do not want to store or share.']),
   ('ads','Advertising, technical data and consent',[
    'Atelier uses Google AdMob (Google Mobile Ads) to show ads in enabled placements. The SDK may collect and share IP addresses, approximate location inferred from them, advertising or installation identifiers, app and ad interactions, and diagnostic and crash data. Google states that these data are used for advertising, analytics and fraud prevention.',
    'Rewarded ads are optional and grant the access shown in the app when the provider confirms the reward. Ad availability and rewards for an ad that cannot be completed are not guaranteed.',
    'Consent and privacy choices are presented through Google’s platform where applicable. You can review the options available in the app and Android’s advertising controls. Declining personalisation does not necessarily stop all technical data collection or all ads. Deleting the advertising ID does not necessarily remove other identifiers.',
    'Google states that data collected by its ads SDK is encrypted in transit using TLS. Retention and other processing depend on Google and participating advertising providers, the applicable configuration and their policies. We do not set or promise a 90-day deletion period for these data.']),
   ('ocr','OCR and recognition SDKs',[
    'Text recognition with Google ML Kit runs on your device. The SDK may transmit technical information such as device model, Android and app versions, installation identifiers, configuration, performance metrics and event or error codes for diagnostics and usage analytics.',
    'This technical information is separate from image contents and recognised text. Google states that it uses HTTPS for these transmissions and does not transfer the data described in its ML Kit disclosure to third parties.']),
   ('sharing','Sharing and external links',[
    'When you choose to share a result or open it in another app, Android lets you select the destination. The file or text is passed to that destination, whose subsequent handling depends on that app. Atelier no longer controls a copy sent to another app.',
    'Opening a QR link may take you to an external website. Check the destination before opening it. External websites, YouTube and storage providers apply their own policies.']),
   ('retention','Retention and deletion',[
    'Projects, preferences and access entitlements are stored locally for as long as needed or until you remove them using the available options. Features may create temporary files for processing, exporting or sharing.',
    'Clearing app data or uninstalling removes its private storage according to Android’s behaviour. This does not necessarily remove exports, shared copies or backups managed by the system or services you selected.',
    'Atelier has no account creation. We do not maintain our own server-based library of your documents that we can delete by email. For Google and other providers’ data, use their privacy controls. You can email us about managing local data; this does not mean we can identify or delete all SDK records.']),
   ('website','This website',[
    'These information pages are hosted on GitHub Pages. We do not embed document upload forms, our own analytics, advertising pixels or third-party videos in these pages. GitHub may process technical visit information, such as IP addresses, to provide and protect its service under its policy.',
    'If you email us, we receive the sender’s address and the content you choose to send. We use them to handle your enquiry and retain them for as long as necessary for that purpose and applicable obligations. Do not send passwords or sensitive documents unnecessarily.']),
   ('rights','Controls and rights',[
    'Depending on where you live and the processing involved, you may have rights of access, correction, deletion, objection or withdrawal of consent. Contact us with enquiries about Atelier; for data processed by providers, also consult their request mechanisms.',
    'Third-party services may process data in other countries under their own terms and safeguards. This policy does not guarantee absolute security or replace Android’s or a provider’s privacy controls.']),
   ('children','Children and policy changes',[
    'Atelier does not deliberately ask children to send personal information through support. If you believe a child has sent us personal information, contact us. Ad and message availability must respect the applicable audience and age settings.',
    'We may update this policy when features or services change. The update date appears above. Mentioning a future feature in a roadmap does not mean it is active.'])],
  'provider_title':'Provider information', 'contact_title':'Privacy contact', 'contact_text':'For questions about this policy or information you have sent through support:', 'toc_title':'Contents', 'footer':'Tools for your documents. Clear information about your data.'
 },
 'fr': {
  'name':'Français', 'skip':'Aller au contenu', 'language':'Langue du site',
  'nav':['Outils','Questions','Confidentialité'], 'home':'Accueil', 'title':'Atelier Tools — PDF, codes QR et documents',
  'description':'Créez des PDF, numérisez des pages, générez des codes QR et gérez vos documents sur Android. Découvrez Atelier Tools et sa politique de confidentialité.',
  'eyebrow':'PDF · Codes QR · Documents', 'headline':'Donnez forme à vos documents.',
  'lead':'Créez un PDF, numérisez vos notes, préparez un code QR ou annotez une copie d’un fichier existant. Vos outils documentaires, réunis au même endroit.',
  'status':'Une mise à jour est en préparation', 'status_note':'Ces fonctions décrivent la version candidate de la prochaine mise à jour. La version disponible sur Google Play peut être antérieure ; certaines fonctions nécessitent un déblocage.',
  'explore':'Découvrir les outils', 'privacy':'Lire la politique de confidentialité', 'icon_alt':'Icône de l’application Atelier Tools',
  'section_eyebrow':'Travaillez à votre façon', 'section_title':'Du fichier au document final.', 'section_lead':'Créez, organisez et partagez sans changer d’outil à chaque étape.',
  'cards':[
   ('PDF','Créez et organisez vos PDF','Ajoutez du texte, des images et des codes QR. Réorganisez les pages, ajustez les propriétés et enregistrez vos projets pour les reprendre plus tard.'),
   ('✎','Annotez et signez une copie','Ouvrez un PDF existant et créez une copie pour ajouter du texte, des formes ou une signature manuscrite en couleur. Annulez et rétablissez vos modifications.'),
   ('▤','Consultez vos documents','Parcourez les PDF avec le zoom, la navigation par page et la recherche. Affichez les PPTX sous forme de présentations statiques, avec des indications sur les éléments non pris en charge.'),
   ('⌗','Créez et scannez des codes QR','Générez des codes pour du texte, des liens et d’autres données compatibles. Enregistrez-les, partagez-les au format PNG et organisez vos favoris.'),
   ('▧','Numérisez vos pages','Utilisez l’appareil photo ou vos images, corrigez le cadrage et appliquez des filtres. La reconnaissance de texte sur l’appareil permet de consulter et de copier le texte reconnu.'),
   ('↔','Convertissez vos documents','Effectuez des conversions entre PDF, Word et PowerPoint. Le résultat dépend de la structure du fichier ; vérifiez toujours la mise en page.')],
  'copy_note':'L’édition d’une copie de PDF utilise des pages converties en images comme arrière-plan : les nouveaux éléments restent modifiables, mais le texte d’origine n’est pas automatiquement transformé en objets modifiables. Une signature manuscrite ajoutée ne constitue pas une signature numérique certifiée.',
  'look_title':'Un espace qui vous ressemble.', 'look_text':'Thèmes, surfaces Glass et navigation Classique ou Semiluna. Personnalisez les couleurs et les effets ; le mode fluide réduit les effets visuels pour privilégier l’utilisation. Certains styles et outils nécessitent un déblocage ou offrent un accès temporaire.',
  'faq_title':'Avant de commencer',
  'faq':[
   ('Faut-il un compte ?','Atelier ne propose ni inscription ni connexion à un compte. Vos projets sont gérés localement.'),
   ('Tout fonctionne-t-il hors connexion ?','La création et le traitement des documents s’effectuent sur votre appareil. Les annonces, les services de consentement et les liens externes nécessitent une connexion ; les annonces avec récompense dépendent de leur disponibilité.'),
   ('La reconnaissance et les conversions sont-elles toujours exactes ?','Non. La reconnaissance peut échouer avec du texte manuscrit, des images floues ou des systèmes d’écriture non pris en charge. Les conversions peuvent modifier les polices, le positionnement et les éléments complexes.'),
   ('Le lecteur PPTX reproduit-il les animations ?','Il propose un affichage et une présentation statiques. Il ne garantit pas la conservation des animations, transitions et contenus multimédias, ni une compatibilité complète avec PowerPoint ou Canva.'),
   ('Quelles améliorations sont en préparation ?','L’interface de l’application en espagnol, anglais et français est en cours de développement. Notre IA reste un projet de recherche et n’est pas intégrée comme assistant génératif. Aucune date de disponibilité n’est annoncée pour ces améliorations.')],
  'support_title':'Besoin d’aide ?', 'support_text':'Indiquez par courriel le modèle de votre appareil, la version d’Atelier et les étapes du problème. Évitez de joindre des documents personnels ou des mots de passe.', 'contact':'Contacter l’assistance',
  'privacy_title':'Politique de confidentialité', 'updated':'Dernière mise à jour : 15 octobre 2026',
  'policy_intro':'Cette politique décrit le traitement des données dans Atelier Tools pour Android et sur ce site. Le responsable d’Atelier Tools exerce publiquement sous le nom de MT-Corp. Vous pouvez le contacter à l’adresse électronique indiquée à la fin de cette politique.',
  'policy':[
   ('local','Documents et traitement sur l’appareil',[
    'Les fonctions disponibles de création et d’édition de PDF, de numérisation, de reconnaissance de texte et de conversion s’exécutent sur votre appareil. Atelier n’envoie pas le contenu de vos documents, images, signatures, codes QR ou textes reconnus à ses propres serveurs pour effectuer ces tâches ou entraîner notre IA expérimentale.',
    'Le traitement local ne signifie pas que l’application n’effectue aucune communication réseau : les SDK publicitaires et techniques décrits ci-dessous peuvent transmettre leurs propres données. L’application n’intègre actuellement aucun service distant de conversation générative.']),
   ('files','Fichiers, projets et autorisations',[
    'Les projets et les préférences sont conservés dans le stockage de l’application. Les fichiers exportés sont enregistrés à l’emplacement que vous choisissez ; si vous sélectionnez un service de stockage en ligne depuis Android, ce service traite les fichiers selon ses propres conditions.',
    'L’appareil photo sert à numériser des documents ou des codes QR et à prendre des photos pour un projet. Les images et documents sont sélectionnés avec les mécanismes disponibles sur Android. Vous pouvez refuser ou révoquer les autorisations dans les paramètres du système ; les fonctions qui en dépendent deviennent alors indisponibles.',
    'Les projets peuvent contenir des informations sensibles que vous y ajoutez, comme des signatures ou des coordonnées encodées dans un code QR. N’ajoutez pas d’informations que vous ne souhaitez pas conserver ou partager.']),
   ('ads','Publicité, données techniques et consentement',[
    'Atelier utilise Google AdMob (Google Mobile Ads) pour afficher des annonces aux emplacements activés. Le SDK peut collecter et partager l’adresse IP, la position approximative déduite de celle-ci, des identifiants publicitaires ou d’installation, les interactions avec l’application et les annonces, ainsi que des données de diagnostic et de plantage. Google indique utiliser ces données pour la publicité, l’analyse et la prévention de la fraude.',
    'Les annonces avec récompense sont facultatives et accordent l’accès indiqué dans l’application lorsque le fournisseur confirme la récompense. La disponibilité des annonces et l’obtention d’une récompense pour une annonce qui ne peut pas être terminée ne sont pas garanties.',
    'Les choix de consentement et de confidentialité sont présentés par la plateforme de Google lorsque cela s’applique. Vous pouvez consulter les options disponibles dans l’application et les réglages publicitaires d’Android. Refuser la personnalisation n’arrête pas nécessairement toute collecte technique ni toutes les annonces. Supprimer l’identifiant publicitaire ne supprime pas nécessairement les autres identifiants.',
    'Google déclare chiffrer en transit, avec TLS, les données collectées par son SDK publicitaire. Leur conservation et les autres traitements dépendent de Google, des fournisseurs publicitaires concernés, de la configuration applicable et de leurs politiques. Nous ne fixons ni ne promettons un délai de suppression de 90 jours pour ces données.']),
   ('ocr','Reconnaissance de texte et SDK',[
    'La reconnaissance de texte avec Google ML Kit s’exécute sur votre appareil. Le SDK peut transmettre des informations techniques : modèle de l’appareil, versions d’Android et de l’application, identifiants d’installation, configuration, mesures de performance et codes d’événements ou d’erreurs, à des fins de diagnostic et d’analyse d’utilisation.',
    'Ces informations techniques sont distinctes du contenu des images et du texte reconnu. Google déclare utiliser HTTPS pour ces transmissions et ne pas transférer à des tiers les données décrites dans sa déclaration relative à ML Kit.']),
   ('sharing','Partage et liens externes',[
    'Lorsque vous choisissez de partager un résultat ou de l’ouvrir dans une autre application, Android vous permet de sélectionner la destination. Le fichier ou le texte est transmis à cette destination, et son traitement ultérieur dépend de cette application. Une copie envoyée à une autre application n’est plus sous le contrôle d’Atelier.',
    'L’ouverture du lien d’un code QR peut vous conduire vers un site externe. Vérifiez la destination avant de l’ouvrir. Les sites externes, YouTube et les services de stockage appliquent leurs propres politiques.']),
   ('retention','Conservation et suppression',[
    'Les projets, préférences et droits d’accès sont conservés localement aussi longtemps que nécessaire ou jusqu’à leur suppression avec les options disponibles. Les fonctions peuvent créer des fichiers temporaires pour le traitement, l’exportation ou le partage.',
    'L’effacement des données de l’application ou sa désinstallation supprime son stockage privé selon le fonctionnement d’Android. Cela ne supprime pas nécessairement les exportations, copies partagées ou sauvegardes gérées par le système ou par les services que vous avez choisis.',
    'Atelier ne propose pas de création de compte. Nous ne conservons pas notre propre bibliothèque de vos documents sur un serveur dont nous pourrions supprimer les fichiers par courriel. Pour les données de Google et des autres fournisseurs, utilisez leurs contrôles de confidentialité. Vous pouvez nous écrire pour savoir comment gérer les données locales ; cela ne signifie pas que nous pouvons identifier ou supprimer tous les enregistrements d’un SDK.']),
   ('website','Ce site web',[
    'Ces pages d’information sont hébergées sur GitHub Pages. Nous n’y intégrons ni formulaire de dépôt de documents, ni outil d’analyse propre, ni pixel publicitaire, ni vidéo tierce intégrée. GitHub peut traiter des informations techniques de visite, comme l’adresse IP, pour fournir et protéger son service conformément à sa politique.',
    'Si vous nous écrivez, nous recevons votre adresse électronique et le contenu que vous choisissez d’envoyer. Nous les utilisons pour traiter votre demande et les conservons aussi longtemps que nécessaire à cette fin et au respect des obligations applicables. N’envoyez pas de mots de passe ou de documents sensibles sans nécessité.']),
   ('rights','Contrôles et droits',[
    'Selon votre lieu de résidence et le traitement concerné, vous pouvez disposer de droits d’accès, de rectification, d’effacement, d’opposition ou de retrait du consentement. Pour toute question sur Atelier, utilisez notre adresse de contact ; pour les données traitées par des fournisseurs, consultez également leurs mécanismes de demande.',
    'Des services tiers peuvent traiter des données dans d’autres pays conformément à leurs propres conditions et garanties. Cette politique ne garantit pas une sécurité absolue et ne remplace pas les contrôles de confidentialité d’Android ou des fournisseurs.']),
   ('children','Mineurs et modifications',[
    'Atelier ne demande pas délibérément aux mineurs d’envoyer des informations personnelles à l’assistance. Si vous pensez qu’un mineur nous en a envoyé, contactez-nous. La disponibilité des annonces et des messages doit respecter le public et les paramètres d’âge applicables.',
    'Nous pouvons modifier cette politique lorsque les fonctions ou services évoluent. La date de mise à jour figure en haut de cette page. La simple mention d’une fonction future dans une feuille de route ne signifie pas qu’elle est active.'])],
  'provider_title':'Informations des fournisseurs', 'contact_title':'Contact pour la confidentialité', 'contact_text':'Pour toute question sur cette politique ou sur les données envoyées à l’assistance :', 'toc_title':'Sommaire', 'footer':'Des outils pour vos documents. Des informations claires sur vos données.'
 }
}

PROVIDERS = [
 ('Google Privacy Policy','https://policies.google.com/privacy'),
 ('Google Mobile Ads — data disclosure','https://developers.google.com/admob/android/privacy/play-data-disclosure'),
 ('Google ML Kit — data disclosure','https://developers.google.com/ml-kit/android-data-disclosure'),
 ('Google privacy controls','https://safety.google/privacy/privacy-controls/'),
 ('GitHub Privacy Statement','https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement'),
]

def url(lang, page):
 return ('/' if lang == 'es' else f'/{lang}/') + page

def island(lang, page, name):
 data=json.loads((ROOT/'assets/components.json').read_text(encoding='utf-8'))[lang][page][name]
 return f'<div data-component="{name}" data-props="{esc(json.dumps(data["props"],ensure_ascii=False),quote=True)}">{data["html"]}</div>'

def header(lang, page):
 c = COPY[lang]
 links = ''.join(f'<a href="{url(lang,"index.html")}#{anchor}">{esc(text)}</a>' for anchor,text in zip(['herramientas','preguntas'],c['nav'][:2]))
 return f'''<a class="skip-link" href="#main">{esc(c['skip'])}</a>
 <div class="reading-progress" aria-hidden="true"></div>
 <header class="site-header"><div class="shell nav">
 <a class="brand" href="{url(lang,'index.html')}"><img src="/assets/atelier-icon.png" width="42" height="42" alt=""><span>Atelier Tools</span></a>
 <nav class="nav-links" aria-label="{esc(c['home'])}">{links}<a href="{url(lang,'privacy.html')}">{esc(c['nav'][2])}</a></nav>
 <div class="header-tools">{island(lang,page,'MotionToggle')}{island(lang,page,'LanguagePicker')}</div>
 </div></header>'''

def frame(lang, page, content):
 c=COPY[lang]; title = c['title'] if page=='index.html' else c['privacy_title']+' — Atelier Tools'
 alternates=''.join(f'<link rel="alternate" hreflang="{code}" href="{HOST}{url(code,page)}">' for code in COPY)
 return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#100b0f"><meta name="description" content="{esc(c['description'] if page=='index.html' else c['privacy_title'])}">
<title>{esc(title)}</title><link rel="canonical" href="{HOST}{url(lang,page)}">{alternates}
<link rel="icon" type="image/png" href="/assets/atelier-icon.png"><link rel="apple-touch-icon" href="/assets/atelier-icon.png">
<meta property="og:title" content="{esc(title)}"><meta property="og:image" content="{HOST}/assets/atelier-icon.png"><meta property="og:type" content="website">
<link rel="stylesheet" href="/assets/site.css"><script defer src="/assets/site.js"></script></head>
<body data-page="{'home' if page=='index.html' else 'privacy'}">{header(lang,page)}{content}<footer><div class="shell footer-row"><span>© 2026 MT-Corp · Atelier Tools<br>{esc(c['footer'])}</span><nav><a href="{url(lang,'index.html')}">{esc(c['home'])}</a><a href="{url(lang,'privacy.html')}">{esc(c['nav'][2])}</a><a href="mailto:{CONTACT}">{esc(c['contact'])}</a><a href="/assets/third-party-notices.txt">{'Licencias' if lang=='es' else 'Licences'}</a></nav></div></footer></body></html>\n'''

def home(lang):
 c=COPY[lang]
 cards=''.join(f'<article class="feature-card"><div class="feature-icon" aria-hidden="true">{esc(mark)}</div><h3>{esc(title)}</h3><p>{esc(text)}</p></article>' for mark,title,text in c['cards'])
 faqs=''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in c['faq'])
 content=f'''<main id="main"><section class="hero shell"><div class="hero-copy"><div class="eyebrow">{esc(c['eyebrow'])}</div><h1>{esc(c['headline'])}</h1><p class="lead">{esc(c['lead'])}</p><p class="status">{esc(c['status'])}</p><div class="actions"><a class="button" href="#herramientas">{esc(c['explore'])}<span aria-hidden="true">↗</span></a><a class="button secondary" href="{url(lang,'privacy.html')}">{esc(c['privacy'])}</a></div></div>{island(lang,'index.html','SpatialScene')}</section>
<section id="herramientas" class="section shell"><div class="section-heading"><div class="eyebrow">{esc(c['section_eyebrow'])}</div><h2>{esc(c['section_title'])}</h2><p>{esc(c['section_lead'])}</p></div><p class="notice">{esc(c['status_note'])}</p><div class="feature-grid">{cards}</div><p class="notice">{esc(c['copy_note'])}</p></section>
<section class="section shell"><div class="cta"><div><h2>{esc(c['look_title'])}</h2><p>{esc(c['look_text'])}</p></div></div></section>
<section id="preguntas" class="section shell"><div class="section-heading"><h2>{esc(c['faq_title'])}</h2></div><div class="faq">{faqs}</div></section>
<section class="section shell"><div class="cta"><div><h2>{esc(c['support_title'])}</h2><p>{esc(c['support_text'])}</p></div><a class="button" href="mailto:{CONTACT}">{esc(c['contact'])}</a></div></section></main>'''
 return frame(lang,'index.html',content)

def privacy(lang):
 c=COPY[lang]
 toc=''.join(f'<li><a href="#{key}">{esc(title)}</a></li>' for key,title,_ in c['policy'])
 sections=''.join(f'<section><h2 id="{key}">{i}. {esc(title)}</h2>'+''.join(f'<p>{esc(p)}</p>' for p in paragraphs)+'</section>' for i,(key,title,paragraphs) in enumerate(c['policy'],1))
 providers=''.join(f'<li><a href="{href}">{esc(title)}</a></li>' for title,href in PROVIDERS)
 content=f'''<main id="main" class="shell legal"><div class="privacy-intro"><div><div class="eyebrow">Atelier · MT-Corp</div><h1>{esc(c['privacy_title'])}</h1><p class="updated">{esc(c['updated'])}</p><p class="lead">{esc(c['policy_intro'])}</p></div>{island(lang,'privacy.html','SpatialScene')}</div><article><nav class="toc" aria-label="{esc(c['toc_title'])}"><strong>{esc(c['toc_title'])}</strong><ul>{toc}</ul></nav>{sections}<h2>{esc(c['provider_title'])}</h2><ul>{providers}</ul><h2 id="contact">{esc(c['contact_title'])}</h2><p>{esc(c['contact_text'])} <a href="mailto:{CONTACT}">{CONTACT}</a>.</p></article></main>'''
 return frame(lang,'privacy.html',content)

if __name__ == '__main__':
 for lang in COPY:
  folder=ROOT if lang=='es' else ROOT/lang
  folder.mkdir(exist_ok=True)
  (folder/'index.html').write_text(home(lang),encoding='utf-8')
  (folder/'privacy.html').write_text(privacy(lang),encoding='utf-8')
 print('Generated 6 static pages in es, en and fr.')

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class ParameterObject:
    name: str  # **REQUIRED** #The name of the parameter. Parameter names are *case sensitive*. <ul><li>If [in](#parameterIn) is "path", the name field MUST correspond to a template expression occurring within the [path](#pathsPath) field in the [Paths Object](#pathsObject). See [Path Templating](#pathTemplating) for further information.<li>If [in](#parameterIn) is "header" and the name field is "Accept", "Content-Type" or "Authorization", the parameter definition SHALL be ignored.<li>For all other cases, the name corresponds to the parameter name used by the [in](#parameterIn) property.</ul>
    _in: str  # **REQUIRED** #The location of the parameter. Possible values are "query", "header", "path" or "cookie".
    description: str  # A brief description of the parameter. This could contain examples of use. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    required: bool  # Determines whether this parameter is mandatory. If the [parameter location](#parameterIn) is "path", this property is **REQUIRED** #nd its value MUST be true. Otherwise, the property MAY be included and its default value is false.
    deprecated: bool  # Specifies that a parameter is deprecated and SHOULD be transitioned out of usage. Default value is false.
    allowEmptyValue: bool  # Sets the ability to pass empty-valued parameters. This is valid only for query parameters and allows sending a parameter with an empty value. Default value is false. If [style](#parameterStyle) is used, and if behavior is n/a (cannot be serialized), the value of allowEmptyValue SHALL be ignored. Use of this property is NOT RECOMMENDED, as it is likely to be removed in a later revision.

    # style: str  # Describes how the parameter value will be serialized depending on the type of the parameter value. Default values (based on value of in): for query - form; for path - simple; for header - simple; for cookie - form.
    # explode: bool  # When this is true, parameter values of type array or object generate separate parameters for each value of the array or key-value pair of the map. For other types of parameters this property has no effect. When [style](#parameterStyle) is form, the default value is true. For all other styles, the default value is false.
    # allowReserved: bool  # Determines whether the parameter value SHOULD allow reserved characters, as defined by [RFC3986](https://tools.ietf.org/html/rfc3986#section-2.2) :/?#[]@!$&'()*+,;= to be included without percent-encoding. This property only applies to parameters with an in value of query. The default value is false.
    # schema: [Schema Object](
    #     # schemaObject) : [Reference Object](#referenceObject)   #The schema defining the type used for the parameter.
    #     example: Any  # Example of the parameter's potential value. The example SHOULD match the specified schema and encoding properties if present. The example field is mutually exclusive of the examples field. Furthermore, if referencing a schema that contains an example, the example value SHALL _override_ the example provided by the schema. To represent examples of media types that cannot naturally be represented in JSON or YAML, a str value can contain the example with escaping where necessary.
    # examples: Dict[str, [Example Object](
    #     # exampleObject) : [Reference Object](#referenceObject)]   #Examples of the parameter's potential value. Each example SHOULD contain a value in the correct format as specified in the parameter encoding. The examples field is mutually exclusive of the example field. Furthermore, if referencing a schema that contains an example, the examples value SHALL _override_ the example provided by the schema.
    #     content: Dict[str, [Media Type
    #                        Object](  # mediaTypeObject)]   #A map containing the representations for the parameter. The key is the media type and the value describes it. The map MUST only contain one entry.


@dataclass()
class LinkObject:
    pass


#     operationRef: str  # A relative or absolute URI reference to an OAS operation. This field is mutually exclusive of the operationId field, and MUST point to an [Operation Object](#operationObject). Relative operationRef values MAY be used to locate an existing [Operation Object](#operationObject) in the OpenAPI definition.
#     operationId: str  # The name of an _existing_, resolvable OAS operation, as defined with a unique operationId.  This field is mutually exclusive of the operationRef field.
#     parameters: Dict[str,  runtimeExpression]   #A map representing parameters to pass to an operation as specified with operationId or identified via operationRef. The key is the parameter name to be used, whereas the value can be a constant or an expression to be evaluated and passed to the linked operation.  The parameter name can be qualified using the [parameter location](#parameterIn) [{in}.]{name} for operations that use the same parameter name in different locations (e.g. path.id).
#     requestBody: Any: [{expression}](
#         # runtimeExpression)   #A literal value or [{expression}](#runtimeExpression) to use as a request body when calling the target operation.
#         description: str  # A description of the link. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
#     server: [Server Object](  # serverObject)   #A server object to be used by the target operation.


@dataclass
class ExampleObject:
    summary: str  # Short description for the example.
    description: str  # Long description for the example. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    value: str  # Embedded literal example. The value field and externalValue field are mutually exclusive. To represent examples of media types that cannot naturally represented in JSON or YAML, use a str value to contain the example, escaping where necessary.
    externalValue: str  # A URL that points to the literal example. This provides the capability to reference examples that cannot easily be included in JSON or YAML documents.  The value field and externalValue field are mutually exclusive.


@dataclass
class ServerVariableObject:
    enum: List[str]  # An enumeration of str values to be used if the substitution options are from a limited set. The array SHOULD NOT be empty.
    default: str  # **REQUIRED** #The default value to use for substitution, which SHALL be sent if an alternate value is _not_ supplied. Note this behavior is different than the [Schema Object's](#schemaObject) treatment of default values, because in those cases parameter values are optional. If the [enum](#serverVariableEnum) is defined, the value SHOULD exist in the enum's values.
    description: str  # An optional description for the server variable. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.


@dataclass
class ServerObject:
    url: str  # **REQUIRED** #A URL to the target host.  This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the OpenAPI document is being served. Variable substitutions will be made when a variable is named in {brackets}.
    description: str  # An optional str describing the host designated by the URL. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    variables: Dict[str, ServerVariableObject]  # A map between a variable name and its value.  The value is used for substitution in the server's URL template.


@dataclass
class ReferenceObject:
    ref: str  # **REQUIRED** #The reference str.


@dataclass
class ContactObject:
    name: str  # The identifying name of the contact person/organization.
    url: str  # The URL pointing to the contact information. MUST be in the format of a URL.
    email: str  # The email address of the contact person/organization. MUST be in the format of an email address.


@dataclass
class LicenseObject:
    name: str  # **REQUIRED** #The license name used for the API.
    url: str  # A URL to the license used for the API. MUST be in the format of a URL.


@dataclass
class InfoObject:
    title: str  # **REQUIRED** #The title of the API.
    description: str  # A short description of the API. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    termsOfService: str  # A URL to the Terms of Service for the API. MUST be in the format of a URL.
    contact: ContactObject  # The contact information for the exposed API.
    license: LicenseObject  # The license information for the exposed API.
    version: str  # **REQUIRED** #The version of the OpenAPI document (which is distinct from the [OpenAPI Specification version](#oasVersion) or the API implementation version).


@dataclass
class SecurityRequirementObject:
    name: List[str]  # Each name MUST correspond to a security scheme which is declared in the [Security Schemes](#componentsSecuritySchemes) under the [Components Object](#componentsObject). If the security scheme is of type "oauth2" or "openIdConnect", then the value is a list of scope names required for the execution, and the list MAY be empty if authorization does not require a specified scope. For other security scheme types, the array MUST be empty.


@dataclass
class ExternalDocumentationObject:
    description: str  # A short description of the target documentation. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    url: str  # **REQUIRED** #The URL for the target documentation. Value MUST be in the format of a URL.


@dataclass
class XmlObject:
    name: str  # Replaces the name of the element/attribute used for the described schema property. When defined within items, it will affect the name of the individual XML elements within the list. When defined alongside type being array (outside the items), it will affect the wrapping element and only if wrapped is true. If wrapped is false, it will be ignored.
    namespace: str  # The URI of the namespace definition. Value MUST be in the form of an absolute URI.
    prefix: str  # The prefix to be used for the [name](#xmlName).
    attribute: bool  # Declares whether the property definition translates to an attribute instead of an element. Default value is false.
    wrapped: bool  # MAY be used only for an array definition. Signifies whether the array is wrapped (for example, <books><book/><book/></books>) or unwrapped (<book/><book/>). Default value is false. The definition takes effect only when defined alongside type being array (outside the items).


@dataclass
class HeaderObject:
    pass


@dataclass
class DiscriminatorObject:
    propertyName: str  # **REQUIRED** #The name of the property in the payload that will hold the discriminator value.
    mapping: Dict[str, str]  # An object to hold mappings between payload values and schema names or references.


@dataclass
class SchemaObject:
    nullable: bool  # A true value adds "null" to the allowed type specified by the type keyword, only if type is explicitly defined within the same Schema Object. Other Schema Object constraints retain their defined behavior, and therefore may disallow the use of null as a value. A false value leaves the specified or default type unmodified. The default value is false.
    discriminator: DiscriminatorObject  # Adds support for polymorphism. The discriminator is an object name that is used to differentiate between other schemas which may satisfy the payload description. See [Composition and Inheritance](#schemaComposition) for more details.
    readOnly: bool  # Relevant only for Schema "properties" definitions. Declares the property as "read only". This means that it MAY be sent as part of a response but SHOULD NOT be sent as part of the request. If the property is marked as readOnly being true and is in the required list, the required will take effect on the response only. A property MUST NOT be marked as both readOnly and writeOnly being true. Default value is false.
    writeOnly: bool  # Relevant only for Schema "properties" definitions. Declares the property as "write only". Therefore, it MAY be sent as part of a request but SHOULD NOT be sent as part of the response. If the property is marked as writeOnly being true and is in the required list, the required will take effect on the request only. A property MUST NOT be marked as both readOnly and writeOnly being true. Default value is false.
    xml: XmlObject  # This MAY be used only on properties schemas. It has no effect on root schemas. Adds additional metadata to describe the XML representation of this property.
    externalDocs: ExternalDocumentationObject  # Additional external documentation for this schema.
    example: object  # A free-form property to include an example of an instance for this schema. To represent examples that cannot be naturally represented in JSON or YAML, a str value can be used to contain the example with escaping where necessary.
    deprecated: bool  # Specifies that a schema is deprecated and SHOULD be transitioned out of usage. Default value is false.


@dataclass
class EncodingObject:
    contentType: str  # The Content-Type for encoding a specific property. Default value depends on the property type: for str with format being binary – application/octet-stream; for other primitive types – text/plain; for object - application/json; for array – the default is defined based on the inner type. The value can be a specific media type (e.g. application/json), a wildcard media type (e.g. image/*), or a comma-separated list of the two types.
    headers: Dict[str, HeaderObject]  # : [Reference Object](#referenceObject)]   #A map allowing additional information to be provided as headers, for example Content-Disposition.  Content-Type is described separately and SHALL be ignored in this section. This property SHALL be ignored if the request body media type is not a multipart.
    style: str  # Describes how a specific property value will be serialized depending on its type.  See [Parameter Object](#parameterObject) for details on the [style](#parameterStyle) property. The behavior follows the same values as query parameters, including default values. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.
    explode: bool  # When this is true, property values of type array or object generate separate parameters for each value of the array, or key-value-pair of the map.  For other types of properties this property has no effect. When [style](#encodingStyle) is form, the default value is true. For all other styles, the default value is false. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.
    allowReserved: bool  # Determines whether the parameter value SHOULD allow reserved characters, as defined by [RFC3986](https://tools.ietf.org/html/rfc3986#section-2.2) :/?#[]@!$&'()*+,;= to be included without percent-encoding. The default value is false. This property SHALL be ignored if the request body media type is not application/x-www-form-urlencoded.


@dataclass
class MediaTypeObject:
    schema: SchemaObject  # [Reference Object](#referenceObject)   #The schema defining the content of the request, response, or parameter.
    example: object  # Example of the media type.  The example object SHOULD be in the correct format as specified by the media type.  The example field is mutually exclusive of the examples field.  Furthermore, if referencing a schema which contains an example, the example value SHALL _override_ the example provided by the schema.
    examples: Dict[str, ExampleObject]  # : [Reference Object](#referenceObject)]   #Examples of the media type.  Each example object SHOULD  match the media type and specified schema if present.  The examples field is mutually exclusive of the example field.  Furthermore, if referencing a schema which contains an example, the examples value SHALL _override_ the example provided by the schema.
    encoding: Dict[str, EncodingObject]  # #A map between a property name and its encoding information. The key, being the property name, MUST exist in the schema as a property. The encoding object SHALL only apply to requestBody objects when the media type is multipart or application/x-www-form-urlencoded.


@dataclass
class ResponseObject:
    description: str  # **REQUIRED** #A short description of the response. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    headers: Dict[str, HeaderObject]  # : [Reference Object](#referenceObject)]   # Maps a header name to its definition. [RFC7230](https://tools.ietf.org/html/rfc7230#page-22) states header names are case insensitive. If a response header is defined with the name "Content-Type", it SHALL be ignored.
    content: Dict[str, MediaTypeObject]  # A map containing descriptions of potential response payloads. The key is a media type or [media type range](https://tools.ietf.org/html/rfc7231#appendix-D) and the value describes it.  For responses that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*
    links: Dict[str, LinkObject]  # : [Reference Object](#referenceObject)]   #A map of operations links that can be followed from the response. The key of the map is a short name for the link, following the naming constraints of the names for [Component Objects](#componentsObject).


@dataclass
class TagObject:
    name: str  # **REQUIRED** #The name of the tag.
    description: str  # A short description for the tag. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    externalDocs: ExternalDocumentationObject  # #Additional external documentation for this tag.


@dataclass
class RequestBodyObject:
    description: str  # A brief description of the request body. This could contain examples of use.  [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    content: Dict[str, MediaTypeObject]  # **REQUIRED** #The content of the request body. The key is a media type or [media type range](https://tools.ietf.org/html/rfc7231#appendix-D) and the value describes it.  For requests that match multiple keys, only the most specific key is applicable. e.g. text/plain overrides text/*
    required: bool  # Determines if the request body is required in the request. Defaults to false.


@dataclass
class OauthFlowObject:
    authorizationUrl: str  # : oauth2("implicit", "authorizationCode")  # **REQUIRED** #The authorization URL to be used for this flow. This MUST be in the form of a URL.
    tokenUrl: str  #: oauth2("password", "clientCredentials",        "authorizationCode")  # **REQUIRED** #The token URL to be used for this flow. This MUST be in the form of a URL.
    refreshUrl: str  # : oauth2  # The URL to be used for obtaining refresh tokens. This MUST be in the form of a URL.
    scopes: Dict[str, str]  #: oauth2  # **REQUIRED** #The available scopes for the OAuth2 security scheme. A map between the scope name and a short description for it. The map MAY be empty.


@dataclass
class OauthFlowsObject:
    implici: OauthFlowObject  # Configuration for the OAuth Implicit flow
    passwor: OauthFlowObject  # Configuration for the OAuth Resource Owner Password flow
    clientCredential: OauthFlowObject  # Configuration for the OAuth Client Credentials flow.  Previously called application in OpenAPI 2.0.
    authorizationCod: OauthFlowObject  # Configuration for the OAuth Authorization Code flow.  Previously called accessCode in OpenAPI 2.0.


@dataclass
class SecuritySchemeObject:
    type: str  # : Any  # **REQUIRED** #The type of the security scheme. Valid values are "apiKey", "http", "oauth2", "openIdConnect".
    description: str  # : Any  # A short description for security scheme. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    name: str  #: apiKey  # **REQUIRED** #The name of the header, query or cookie parameter to be used.
    _in: str  #: apiKey  # **REQUIRED** #The location of the API key. Valid values are "query", "header" or "cookie".
    scheme: str  #: http  # **REQUIRED** #The name of the HTTP Authorization scheme to be used in the [Authorization header as defined in RFC7235](https://tools.ietf.org/html/rfc7235#section-5.1).  The values used SHOULD be registered in the [IANA Authentication Scheme registry](https://www.iana.org/assignments/http-authschemes/http-authschemes.xhtml).
    bearerFormat: str  # A hint to the client to identify how the bearer token is formatted.  Bearer tokens are usually generated by an authorization server, so this information is primarily for documentation purposes.
    flows: OauthFlowsObject  #: oauth2   #**REQUIRED** #An object containing configuration information for the flow types supported.
    openIdConnectUrl: str  #: openIdConnect  # **REQUIRED** #OpenId Connect URL to discover OAuth2 configuration values. This MUST be in the form of a URL.


@dataclass
class ResponsesObject:
    default: ResponseObject  # : [Reference Object](#referenceObject)   #The documentation of responses other than the ones declared for specific HTTP response codes. Use this field to cover undeclared responses. A [Reference Object](#referenceObject) can link to a response that the [OpenAPI Object's components/responses](#componentsResponses) section defines.


@dataclass
class CallbackObject:
    expression: 'PathItemObject'  # A Path Item Object used to define a callback request and expected responses.  A [complete example](../examples/v3.0/callback-example.yaml) is available.


class ComponentsObject:
    schemas: Dict[str, SchemaObject]  # schemaObject) : [Reference Object](#referenceObject)]   #An object to hold reusable [Schema Objects](#schemaObject).
    responses: Dict[str, ResponseObject]  # : [Reference Object](#referenceObject)]   #An object to hold reusable [Response Objects](#responseObject).
    parameters: Dict[str, ParameterObject]  #: [Reference Object](#referenceObject)]   #An object to hold reusable [Parameter Objects](#parameterObject).
    examples: Dict[str, ExampleObject]  # : [Reference Object](#referenceObject)]   #An object to hold reusable [Example Objects](#exampleObject).
    requestBodies: Dict[str, RequestBodyObject]  # : [Reference Object](#referenceObject)]   #An object to hold reusable [Request Body Objects](#requestBodyObject).
    headers: Dict[str, HeaderObject]  # : [Reference Object](#referenceObject)]   #An object to hold reusable [Header Objects](#headerObject).
    securityScheme: Dict[str, SecuritySchemeObject]  # : [Reference Object](#referenceObject)]   #An object to hold reusable [Security Scheme Objects](#securitySchemeObject).
    links: Dict[str, LinkObject]  # : [Reference Object](#referenceObject)]   #An object to hold reusable [Link Objects](#linkObject).
    callbacks: Dict[str, CallbackObject]  # : [Reference Object](#referenceObject)]   #An object to hold reusable [Callback Objects](#callbackObject).


@dataclass
class OperationObject:
    tags: List[str]  # A list of tags for API documentation control. Tags can be used for logical grouping of operations by resources or any other qualifier.
    summary: str  # A short summary of what the operation does.
    description: str  # A verbose explanation of the operation behavior. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    externalDocs: ExternalDocumentationObject  # Additional external documentation for this operation.
    operationId: str  # Unique str used to identify the operation. The id MUST be unique among all operations described in the API. The operationId value is **case-sensitive**. Tools and libraries MAY use the operationId to uniquely identify an operation, therefore, it is RECOMMENDED to follow common programming naming conventions.
    parameters: List[ParameterObject]  # [Reference Object](#referenceObject)]   #A list of parameters that are applicable for this operation. If a parameter is already defined at the [Path Item](#pathItemParameters), the new definition will override it but can never remove it. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a [name](#parameterName) and [location](#parameterIn). The list can use the [Reference Object](#referenceObject) to link to parameters that are defined at the [OpenAPI Object's components/parameters](#componentsParameters).
    requestBody: RequestBodyObject  # : [Reference Object](#referenceObject)   #The request body applicable for this operation.  The requestBody is only supported in HTTP methods where the HTTP 1.1 specification [RFC7231](https://tools.ietf.org/html/rfc7231#section-4.3.1) has explicitly defined semantics for request bodies.  In other cases where the HTTP spec is vague, requestBody SHALL be ignored by consumers.
    responses: ResponsesObject  # #**REQUIRED** #The list of possible responses as they are returned from executing this operation.
    callbacks: Dict[str, CallbackObject]  # : [Reference Object](#referenceObject)]   #A map of possible out-of band callbacks related to the parent operation. The key is a unique identifier for the Callback Object. Each value in the map is a [Callback Object](#callbackObject) that describes a request that may be initiated by the API provider and the expected responses.
    deprecated: bool  # Declares this operation to be deprecated. Consumers SHOULD refrain from usage of the declared operation. Default value is false.
    security: List[SecurityRequirementObject]  # A declaration of which security mechanisms can be used for this operation. The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. To make security optional, an empty security requirement ({}) can be included in the array. This definition overrides any declared top-level [security](#oasSecurity). To remove a top-level security declaration, an empty array can be used.
    servers: List[ServerObject]  # An alternative server array to service this operation. If an alternative server object is specified at the Path Item Object or Root level, it will be overridden by this value.


@dataclass
class PathItemObject:
    ref: str  # Allows for an external definition of this path item. The referenced structure MUST be in the format of a [Path Item Object](#pathItemObject).  In case a Path Item Object field appears both in the defined object and the referenced object, the behavior is undefined.
    summary: str  # An optional, str summary, intended to apply to all operations in this path.
    description: str  # An optional, str description, intended to apply to all operations in this path. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation.
    get: OperationObject  # A definition of a GET operation on this path.
    put: OperationObject  # A definition of a PUT operation on this path.
    post: OperationObject  # A definition of a POST operation on this path.
    delete: OperationObject  # A definition of a DELETE operation on this path.
    options: OperationObject  # A definition of a OPTIONS operation on this path.
    head: OperationObject  # A definition of a HEAD operation on this path.
    patch: OperationObject  # A definition of a PATCH operation on this path.
    trace: OperationObject  # A definition of a TRACE operation on this path.
    servers: List[ServerObject]  # An alternative server array to service all operations in this path.
    parameters: List[ParameterObject]  # or List(referenceObject)  # A list of parameters that are applicable for all the operations described under this path. These parameters can be overridden at the operation level, but cannot be removed there. The list MUST NOT include duplicated parameters. A unique parameter is defined by a combination of a [name](#parameterName) and [location](#parameterIn). The list can use the [Reference Object](#referenceObject) to link to parameters that are defined at the [OpenAPI Object's components/parameters](#componentsParameters).


@dataclass
class PathsObject:
    path: PathItemObject  # A relative path to an individual endpoint. The field name MUST begin with a forward slash (/). The path is **appended** (no relative URL resolution) to the expanded URL from the [Server Object](#serverObject)'s url field in order to construct the full URL. [Path templating](#pathTemplating) is allowed. When matching URLs, concrete (non-templated) paths would be matched before their templated counterparts. Templated paths with the same hierarchy but different templated names MUST NOT exist as they are identical. In case of ambiguous matching, it's up to the tooling to decide which one to use.


@dataclass
class OasObject:
    openapi: str  # **REQUIRED** #This str MUST be the [semantic version number](https://semver.org/spec/v2.0.0.html) of the [OpenAPI Specification version](#versions) that the OpenAPI document uses. The openapi field SHOULD be used by tooling specifications and clients to interpret the OpenAPI document. This is *not* related to the API [info.version](#infoVersion) str.
    info: InfoObject  # **REQUIRED** #Provides metadata about the API. The metadata MAY be used by tooling as required.
    servers: List[ServerObject]  # An array of Server Objects, which provide connectivity information to a target server. If the servers property is not provided, or is an empty array, the default value would be a [Server Object](#serverObject) with a [url](#serverUrl) value of /.
    paths: PathsObject  # **REQUIRED** #The available paths and operations for the API.
    components: ComponentsObject  # An element to hold various schemas for the specification.
    security: List[SecurityRequirementObject]  # A declaration of which security mechanisms can be used across the API. The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. Individual operations can override this definition. To make security optional, an empty security requirement ({}) can be included in the array.
    tags: List[TagObject]  # A list of tags used by the specification with additional metadata. The order of the tags can be used to reflect on their order by the parsing tools. Not all tags that are used by the [Operation Object](#operationObject) must be declared. The tags that are not declared MAY be organized randomly or based on the tools' logic. Each tag name in the list MUST be unique.
    externalDocs: ExternalDocumentationObject  # Additional external documentation.

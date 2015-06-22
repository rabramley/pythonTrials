<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/breakfast_menu">
  <html>
  <body>
  <h2>Menu</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Food</th>
      <th>Price</th>
    </tr>
    <xsl:apply-templates select="food" />
  </table>
  </body>
  </html>
</xsl:template>


<xsl:template match="food">
    <tr>
      <td><xsl:value-of select="name"/></td>
      <td><xsl:value-of select="price"/></td>
    </tr>
</xsl:template>

</xsl:stylesheet>
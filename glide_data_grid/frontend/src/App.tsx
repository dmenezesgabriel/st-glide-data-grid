import React, { useState, useEffect, CSSProperties } from "react";
import "@glideapps/glide-data-grid/dist/index.css";

import {
  DataEditor,
  GridCell,
  GridCellKind,
  GridColumn,
  Item,
} from "@glideapps/glide-data-grid";
import {
  Streamlit,
  withStreamlitConnection,
  RenderData,
} from "streamlit-component-lib";

const App: React.FC = () => {
  const [theme, setTheme] = useState<RenderData["theme"] | null>(null);
  const [data, setData] = useState([]);
  const [columns, setColumns] = useState<GridColumn[]>([]);

  useEffect(() => {
    // This function is called every time the component is rendered by Streamlit.
    const onRender = (event: Event) => {
      const renderData = (event as CustomEvent<RenderData>).detail;
      setData(renderData.args["data"] || []);
      setColumns(renderData.args["columns"] || []);
      setTheme(renderData.theme || null);
    };

    Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
    // Indicate to Streamlit that the component is ready to receive data
    Streamlit.setComponentReady();
    // Adjust the component's height to fit its content
    Streamlit.setFrameHeight(200);

    // Cleanup the event listener on unmount
    return () => {
      Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRender);
    };
  }, []);

  function getData([col, row]: Item): GridCell {
    const person = data[row];
    if (columns[col]?.title && person[columns[col].title]) {
      return {
        kind: GridCellKind.Text,
        data: person[columns[col].title],
        allowOverlay: false,
        displayData: person[columns[col].title],
      };
    } else {
      throw new Error("Invalid column or row data");
    }
  }

  const style: CSSProperties = {};
  if (theme) {
    const borderStyling = `1px solid ${theme.primaryColor}`;
    style.border = borderStyling;
    style.outline = borderStyling;
  }

  return (
    <div>
      <DataEditor
        columns={columns}
        getCellContent={getData}
        rows={data.length}
      />
    </div>
  );
};

// Wrap the component with Streamlit's connection
const WrappedApp = withStreamlitConnection(App);

export default WrappedApp;

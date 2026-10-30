"""README.md of the export step (export_data.py): every file and every column, with units, built from the files the
run actually wrote; undocumented() lists any column without an entry (the step logs them; the tests require none)."""
import glob
import os
import re

import pyarrow.parquet as pq

LOG2 = "log2 units (a difference of 1 = 2-fold)"

# --------------------------------------------------------------------------------------------- the files
FILES = [  # (pattern relative to the export folder, description); {G} = the exposure gene (TRIM72 by default)
    ("README.md", "This file."),
    ("checks.csv", "The step's own checks: every exported number against the atlas (W1, W2, DD_lfc, plate_offset) "
                   "and genome_wide's tensor; what was present or missing. Columns: check, value, n (cells or rows "
                   "compared), note."),
    ("export_info.json", "What this export holds: exposure, thresholds (min_cells, min_lines), which sibling tables "
                         "were used, gene counts, sizes per folder (bytes), the parts and their status."),
    ("run_info.json", "Timings (seconds per stage), peak memory (GB), the free disk the run asked for (GB) and package "
                      "versions of the last run. The only file that differs between two identical runs."),
    ("metadata/cell_lines.csv", "One row per cell line (the atlas's 50 lines on the real data)."),
    ("metadata/drugs.csv", "One row per drug name in the atlas wells (DMSO included), with Tahoe's drug_metadata."),
    ("metadata/wells.csv", "One row per well of the atlas plus the wells the atlas dropped as failed: used or "
                           "excluded, and why."),
    ("metadata/drug_doses.csv", "One row per drug-dose of the atlas (drug x concentration; rows of the atlas's "
                                "drugdose.csv / DD_* arrays): wells used and flags."),
    ("metadata/plates.csv", "One row per plate."),
    ("{G}/{G}_per_profile.csv", "The core table for the exposure gene: one row per profile = (plate, well, drug, "
                                "concentration, cell line) with cells or UMIs, DMSO wells included and flagged; raw, "
                                "uncorrected, correction terms, corrected, flags. Under Excel's row limit."),
    ("{G}/{G}_per_well.csv", "One row per well (DMSO included): the atlas's well-level values of the gene next to "
                             "the medians over lines of the per-profile values."),
    ("{G}/{G}_per_drugdose_line.csv", "One row per (drug-dose, cell line): means over the drug-dose's used wells "
                                      "(as trim72_idarubicin/corrected/trim72_ida_per_line.py's per-line table)."),
    ("{G}/{G}_per_drugdose.csv", "One row per drug-dose: the atlas's corrected fold change, z and q next to the "
                                 "uncorrected medians over lines."),
    ("{G}/{G}_matrix_r2.csv", "Drug-dose x cell line: r2_mean (corrected, log2) of the per (drug-dose, line) table; "
                              "one column per cell line (Cellosaurus id)."),
    ("{G}/{G}_matrix_u_drugmedian.csv", "Drug-dose x cell line: u_drugmedian_mean (uncorrected, vs the plate's "
                                        "drug-well median, log2); one column per cell line."),
    ("{G}/{G}_matrix_u_dmso.csv", "Drug-dose x cell line: u_dmso_mean (uncorrected, vs the plate's DMSO wells, log2); "
                                  "one column per cell line."),
    ("upstream/{G}_per_drugdose.csv", "The exposure per drug-dose (as {G}/{G}_per_drugdose.csv) with the drug's "
                                      "approval status and, when upstream_coregulation's tables exist, the "
                                      "genome-wide readthrough (DoG) index of the drug-dose."),
    ("upstream/{G}_per_drugdose_line.csv", "The exposure per (drug-dose, cell line): the same table as "
                                           "{G}/{G}_per_drugdose_line.csv."),
    ("upstream/line_traits.csv", "One row per cell line: the exposure's untreated level, TP53 group, genotype "
                                 "features (the line traits the upstream analyses use)."),
    ("upstream/line_features.csv", "Long format of tahoe_atlas.genotype_features: one row per (feature, line)."),
    ("upstream/genes.csv", "The genes the DATA tie to the exposure upstream, one row each, with every reason it is "
                           "here and the statistic that selected it."),
    ("upstream/genes_per_profile.parquet", "Per-profile values of the upstream genes (one Parquet row group per "
                                           "gene; same columns as all_genes/per_profile plus correction_path)."),
    ("upstream/genes_per_drugdose_line.parquet", "Per (gene, drug-dose, cell line) means over the used wells "
                                                 "(columns as {G}/{G}_per_drugdose_line.csv)."),
    ("upstream/genes_per_drugdose.parquet", "Per (gene, drug-dose): columns as {G}/{G}_per_drugdose.csv plus reasons."),
    ("upstream/genes_per_drugdose.csv.gz", "The same as genes_per_drugdose.parquet, as gzipped CSV: genes x drug-doses "
                                           "rows (1,132 per gene on the real data), so above ~926 genes it exceeds "
                                           "Excel's 1,048,576 rows (Excel then drops the rest): open it in R / pandas, "
                                           "or write a subset with export_genes.py --genes ... --level drugdose."),
    ("upstream/NOTE.md", "What the upstream folder lacks in this run (e.g. genome_wide or upstream_coregulation "
                         "tables not present) and how to read its gene list (top-|t| genes that are not significant; "
                         "genes listed both upstream and downstream)."),
    ("downstream/genes.csv", "The genes the DATA tie to the exposure downstream (genome_wide's Tahoe p53 program and "
                             "screen hits), one row each, with every reason and the selecting statistics."),
    ("downstream/program_members.csv", "The members of genome_wide's Tahoe p53 programs P (WT-selective induction) "
                                       "and P-down (WT-selective repression), with their FALLBACK flag."),
    ("downstream/genes_per_profile.parquet", "Per-profile values of the downstream genes (as upstream/)."),
    ("downstream/genes_per_drugdose_line.parquet", "Per (gene, drug-dose, cell line) means (as upstream/)."),
    ("downstream/genes_per_drugdose.parquet", "Per (gene, drug-dose) (as upstream/)."),
    ("downstream/genes_per_drugdose.csv.gz", "The same as genes_per_drugdose.parquet, as gzipped CSV (the Excel row "
                                             "limit as for upstream/)."),
    ("downstream/program_flags.csv", "genome_wide's run-level flags of its Tahoe p53 program (its run_info.json 'B', "
                                     "the lines of GENOME_WIDE.md 'Flags'): FALLBACK of P and P-down, S1 / S2 sizes, "
                                     "fold status, every flag text."),
    ("downstream/program_scores_per_profile.csv", "Per profile: the mean over P's (and P-down's) members of r2, "
                                                  "u_drugmedian and u_dmso, over the members the line expresses."),
    ("downstream/program_scores_per_drugdose_line.csv", "The program scores per (drug-dose, cell line): means over "
                                                        "the used wells of the per-profile scores, with the wells "
                                                        "behind each mean and the program's FALLBACK flag."),
    ("downstream/NOTE.md", "Why downstream/ is empty in this run (genome_wide has not finished, finished for another "
                           "exposure, or its tables do not match this atlas)."),
    ("downstream/overlay/NOTE.md", "What the overlay folder is (curated lists, labelled overlay, not a basis)."),
    ("downstream/overlay/curated_sets.csv", "OVERLAY. The curated gene lists of the repo (the panel's 21-gene "
                                            "P53_ACTIVITY, gene_modules.csv modules, CollecTRI TP53 targets when "
                                            "cached): one row per (set, curated entry), entries that are no expressed "
                                            "atlas gene included. They select nothing in this export."),
    ("downstream/overlay/scores_per_drugdose_line.csv", "OVERLAY. Per (drug-dose, cell line): the mean over each "
                                                        "curated set's members of r2 and u_drugmedian (columns "
                                                        "<set>_r2_mean, <set>_u_drugmedian_mean)."),
    ("all_genes/profiles.parquet", "One row per profile (well x line with cells or UMIs), in the order every gene's "
                                   "rows follow: the profile-level columns once."),
    ("all_genes/plate_line.parquet", "One row per (plate, cell line): the pooled DMSO totals behind u_dmso."),
    ("all_genes/genes.csv", "The index: one row per gene -> its per_profile file and row group, its per_drugdose and "
                            "plate_baselines files."),
    ("all_genes/per_profile/chunk_*.parquet", "Every expressed atlas gene, one row per (gene, profile); one row "
                                              "group per gene (in the index order); 256 genes per file."),
    ("all_genes/per_profile/extra_genes.parquet", "The same for the non-atlas genes the export needed (e.g. "
                                                  "PYCARD-AS1), through the extra-gene path."),
    ("all_genes/per_drugdose/chunk_*.parquet", "One row per (gene, drug-dose): the atlas's DD values and the "
                                               "uncorrected medians over lines."),
    ("all_genes/per_drugdose/extra_genes.parquet", "The same for the extra genes (corrected_effects' values)."),
    ("all_genes/plate_baselines/chunk_*.parquet", "One row per (gene, plate, cell line): the two baselines the "
                                                  "uncorrected values are relative to."),
    ("all_genes/plate_baselines/extra_genes.parquet", "The same for the extra genes."),
    ("tahoe_deseq2/NOTE.md", "Where these rows come from, and how they compare with this export."),
    ("tahoe_deseq2/genes.csv", "The genes looked up in Tahoe's DESeq2 table: rows found, is_exposure."),
    ("tahoe_deseq2/genes.parquet", "Tahoe's own pseudobulk DESeq2 rows (drug vs the plate's DMSO, per gene x drug x "
                                   "concentration x plate x line) of the exposure and every upstream / downstream "
                                   "gene, with the atlas's join keys (plate_atlas, concentration_uM, drug_dose_row, "
                                   "cell_line_id; NOTE.md says how they join)."),
    ("tahoe_deseq2/{G}_deseq2.csv", "The exposure's rows of Tahoe's DESeq2 table (CSV), sorted by drug, "
                                    "concentration_uM, plate_atlas, cell_line_id."),
]

# --------------------------------------------------------------------------------------------- the columns
C = {
    # keys
    "gene": "gene label (the atlas symbol; 'SYMBOL (ENSG...)' for the rare duplicated symbols; extra genes: symbol)",
    "symbol": "gene symbol",
    "plate": "Tahoe plate (plate1 ... plate14)",
    "well": "well position on the plate (A1 ... H12)",
    "slot": "well position as a number 1-96 (A1 = 1, A2 = 2, ..., H12 = 96)",
    "sample": "Tahoe sample id of the well (sample_metadata)",
    "drug": "drug name as in Tahoe (the DMSO control wells: their DMSO name, e.g. DMSO_TF)",
    "dose": "the atlas's dose key of the drug-dose (text)",
    "concentration_uM": "drug concentration, micromolar (0.05, 0.5 or 5 uM; 0 for the DMSO wells)",
    "is_dmso": "True for the DMSO control wells",
    "cell_line_id": "cell line, Cellosaurus id (CVCL_...)",
    "cell_name": "cell line name",
    "tp53_group": "TP53 group used by every analysis: WT, altered, or empty (source: metadata/cell_lines.csv "
                  "tp53_source)",
    "drug_dose_row": "row of metadata/drug_doses.csv (= the atlas's drugdose.csv row and DD_* row); -1: none "
                     "(DMSO and failed wells)",
    "profile_id": "row number of the profile (all_genes/profiles.parquet); every gene's rows follow this order",
    # raw
    "n_cells": "cells of that line in that well (count)",
    "umi_count": "the gene's UMIs summed over those cells (count)",
    "total_umi": "all UMIs of the profile, all genes (count)",
    "cpm": "umi_count / total_umi x 1e6 (counts per million, no pseudocount)",
    "log2cpm": "log2((umi_count + 0.5) / (total_umi + 1) x 1e6): the atlas's log2 CPM with its pseudocount (0.5 "
               "count, 1 total UMI); computed for every profile with UMIs (the analyses use it only when usable and "
               "expressed)",
    "usable": "the profile has >= MIN_CELLS cells (export_info.json min_cells: 30 on the real data); else u_* and r2 "
              "are empty (the atlas's rule)",
    "expressed": "the line expresses the gene (the atlas's expr_mask: the line's pooled CPM >= 0.25 x the median "
                 "line's); else u_* and r2 are empty. Extra genes: True in every line",
    "well_used": "the well counts in its drug-dose (atlas used_in_drugdose): False for DMSO wells and for "
                 "unreliable-plate wells of drug-doses that also have reliable wells",
    "unreliable_plate": "the well is on a plate the atlas treats as unreliable (info.json; plate13 by default)",
    # uncorrected
    "u_dmso": "UNCORRECTED, " + LOG2 + ": log2cpm - the same line's pooled DMSO level on the same plate "
              "(all_genes/plate_baselines dmso_log2cpm; Tahoe's own reference, as its DESeq2). NOTE: the atlas found "
              "each plate's DMSO wells offset from its drug-well median (plate_offset; see plate_dmso_offset), so "
              "u_dmso carries that plate offset. Empty when not usable / not expressed / the line has < MIN_CELLS "
              "pooled DMSO cells on the plate. The DMSO pool is the atlas's plate_offset rule (all the line's DMSO "
              "profiles of the plate, one 0.5-count pseudocount per DMSO well); the gene panel's "
              "'log2FC_vs_DMSO_uncorrected' (e.g. trim72_idarubicin/corrected) pools only the usable DMSO profiles "
              "with one pseudocount: log2cpm - log2((sum umi_count + 0.5) / (sum total_umi + 1) x 1e6) over the DMSO "
              "rows with usable = True; at low counts (TRIM72) the two can differ by ~0.1 log2. In a DMSO well, "
              "u_dmso is relative to a pool that includes that well itself (it is the well's deviation from the "
              "plate's DMSO pool, not an effect)",
    "u_drugmedian": "UNCORRECTED, " + LOG2 + ": log2cpm - the median of the same line's log2cpm over the plate's "
                    "drug wells (all_genes/plate_baselines drug_median_log2cpm): the method's r1, before the "
                    "composition and position corrections",
    # corrections
    "composition_shift": LOG2 + ": the profile's composition (library-size) shift, subtracted from every gene "
                         "(atlas composition_shift.parquet: the median residual of the genes the line expresses at "
                         ">= 10 CPM; 0 when not computed)",
    "position_effect": LOG2 + ": the well-position effect removed for this gene in this well (atlas W1 - W2; the "
                       "same for every line of the well); empty when the well has no well-level value (< MIN_LINES "
                       "lines). Extra genes: their own two-pass position correction",
    "posunc": "atlas posunc: position correction uncertain for this gene and well (< 3 clean other-drug wells at the "
              "position: no correction, position_effect 0); empty for extra genes",
    # corrected
    "r2": "CORRECTED (method v3), " + LOG2 + ": u_drugmedian - composition_shift - position_effect; empty when the "
          "well has < MIN_LINES lines with a value for the gene, or not usable / not expressed. Identical to "
          "genome_wide's per (well x line) tensor; its median over lines is the atlas W2 of the well, whose mean over "
          "a drug-dose's used wells is DD_lfc",
    "correction_path": "how the row was corrected: 'atlas (method v3 ...)' for atlas genes; 'extra gene: "
                       "upstream_tf.corrected_effects ...' for non-atlas genes (e.g. PYCARD-AS1)",
    # per well
    "n_lines_profile": "lines with a profile in the well",
    "n_lines_r2": "lines with an r2 value in the well",
    "umi_count_sum": "the gene's UMIs summed over the row's profiles (per well: its lines; per drug-dose or "
                     "(drug-dose, "
                     "line): the used wells) (count)",
    "total_umi_sum": "total UMIs summed over the same profiles (count)",
    "n_cells_sum": "cells summed over the same profiles (count)",
    "cpm_pooled": "umi_count_sum / total_umi_sum x 1e6 (CPM, no pseudocount)",
    "W1_atlas": LOG2 + ": atlas W1, the well's effect before the position correction (median over lines of "
                "u_drugmedian - composition_shift)",
    "W2_atlas": LOG2 + ": atlas W2 = W1 - position effect (median over lines of r2)",
    "Z_atlas": "atlas Z: W2 scored against the spread of the drug wells (robust z, divided by the gene's plate factor)",
    "plate_dmso_offset": LOG2 + ": atlas plate_offset of the gene on the well's plate = the median over lines of "
                         "(drug_median_log2cpm - dmso_log2cpm): how far the plate's DMSO wells sit below its drug "
                         "median. Per (plate, line), u_dmso - u_drugmedian = drug_median_log2cpm - dmso_log2cpm of "
                         "that line (all_genes/plate_baselines), the same in every well of the plate and different "
                         "from line to line; plate_offset is the median over lines of that per-line difference (not "
                         "of a well's per-line differences)",
    "u_drugmedian_median_lines": LOG2 + ": median over the well's lines of u_drugmedian",
    "u_dmso_median_lines": LOG2 + ": median over the well's lines of u_dmso",
    "W1_recomputed": LOG2 + ": median over lines of u_drugmedian - composition_shift (>= MIN_LINES lines): equals "
                     "W1_atlas",
    "r2_median_lines": LOG2 + ": median over the well's lines of r2: equals W2_atlas (float32 rounding)",
    # per (drug-dose, line)
    "n_wells_r2": "used wells of the drug-dose with an r2 value for this line (the wells behind r2_mean, "
                  "u_drugmedian_mean_r2wells, composition_shift_mean and position_effect_mean)",
    "r2_mean": "CORRECTED, " + LOG2 + ": mean of r2 over the n_wells_r2 wells (the per-line corrected fold change of "
               "trim72_ida_per_line.py's per_line table). = u_drugmedian_mean_r2wells - composition_shift_mean - "
               "position_effect_mean",
    "fold_change": "2 ** the row's corrected log2 value (r2_mean per (drug-dose, line); DD_lfc per drug-dose)",
    "u_drugmedian_mean_r2wells": "UNCORRECTED, " + LOG2 + ": mean of u_drugmedian over the same n_wells_r2 wells as "
                                 "r2_mean (so that r2_mean = this - composition_shift_mean - position_effect_mean)",
    "composition_shift_mean": LOG2 + ": mean composition shift over the n_wells_r2 wells (the correction behind "
                              "r2_mean)",
    "position_effect_mean": LOG2 + ": mean position effect over the n_wells_r2 wells (the correction behind r2_mean)",
    "n_wells_u": "used wells of the drug-dose where this line has a u_drugmedian value (usable and expressed; can "
                 "exceed n_wells_r2 where a well has < MIN_LINES lines with a value)",
    "u_drugmedian_mean": "UNCORRECTED, " + LOG2 + ": mean of u_drugmedian over the n_wells_u wells (every used well "
                         "with a value)",
    "n_wells_u_dmso": "used wells of the drug-dose where this line has a u_dmso value (also needs >= min_cells pooled "
                      "DMSO cells of the line on the well's plate)",
    "u_dmso_mean": "UNCORRECTED, " + LOG2 + ": mean of u_dmso over the n_wells_u_dmso wells",
    # per drug-dose (atlas)
    "n_wells_used": "wells the drug-dose uses (reliable plates; all wells when it sits only on unreliable plates)",
    "n_lines_r2_mean": "mean over the drug-dose's used wells of the number of lines with an r2 value for the gene (the "
                       "lines behind each well's median, W2; lines lost to toxicity or not expressing it are not "
                       "among them)",
    "n_lines_r2_any": "lines with an r2 value for the gene in at least one used well (the lines the per (drug-dose, "
                      "line) table has an r2_mean for)",
    "plates": "plates of the drug-dose's wells (comma list)",
    "wells": "well positions of the drug-dose (comma list)",
    "DD_lfc": "CORRECTED, " + LOG2 + ": atlas DD_lfc, the drug-dose's fold change = mean over its used wells of W2",
    "DD_z": "atlas DD_z: Stouffer z over the used wells (each well's robust z scaled by the plate factor)",
    "DD_qup": "atlas BH q-value for an increase (within the gene, over drug-doses)",
    "DD_qdn": "atlas BH q-value for a decrease",
    "DD_poseff": LOG2 + ": atlas DD_poseff, the position effect removed (mean over the used wells)",
    "DD_posunc": "atlas DD_posunc: position correction uncertain in any used well",
    "W1_mean_used_wells": LOG2 + ": mean over the used wells of atlas W1 (before the position correction)",
    "r2_median_lines_mean": LOG2 + ": mean over the used wells of the median over lines of r2 (= DD_lfc recomputed)",
    "u_drugmedian_median_lines_mean": "UNCORRECTED, " + LOG2 + ": mean over the used wells of the median over lines "
                                      "of u_drugmedian",
    "u_dmso_median_lines_mean": "UNCORRECTED, " + LOG2 + ": mean over the used wells of the median over lines of "
                                "u_dmso (Tahoe's DMSO reference)",
    "plate_dmso_offset_mean": LOG2 + ": mean over the used wells of their plate's DMSO offset (plate_dmso_offset)",
    "flags": "the atlas's flags of the drug-dose (drug_doses.csv) plus the gene's own position / noisy-plate flags "
             "(tahoe_atlas.gene_flag_col) where a gene is named",
    "moa_broad": "Tahoe drug_metadata moa-broad", "moa_fine": "Tahoe drug_metadata moa-fine",
    "targets": "Tahoe drug_metadata targets",
    "human_approved": "Tahoe drug_metadata human-approved", "clinical_trials": "Tahoe drug_metadata clinical-trials",
    "pubchem_cid": "Tahoe drug_metadata pubchem_cid", "canonical_smiles": "Tahoe drug_metadata canonical_smiles",
    # readthrough (upstream_coregulation)
    "DoG_sense_index_z": "upstream_coregulation: genome-wide readthrough (downstream-of-gene) index of the drug-dose, "
                         "same-strand (sense) geometry, z",
    "DoG_antisense_index_z": "upstream_coregulation: the same for the antisense geometry (a control), z",
    "DoG_sense_index_log2": "upstream_coregulation: sense readthrough index, level-matched, " + LOG2,
    "DoG_antisense_index_log2": "upstream_coregulation: antisense readthrough index, level-matched, " + LOG2,
    "DoG_sense_index_robust_z": "upstream_coregulation: sense index as a robust z over drug-doses",
    "rank_sense_index": "upstream_coregulation: rank of the drug-dose by the sense index (1 = most readthrough)",
    # metadata
    "depmap_id": "DepMap id (Tahoe cell_line_metadata Cell_ID_DepMap)",
    "organ": "organ / lineage (Tahoe cell_line_metadata Organ)",
    "drivers": "driver genes with their variant type (Tahoe cell_line_metadata)",
    "driver_changes": "driver protein changes (Tahoe cell_line_metadata)",
    "genotype_features": "the atlas's genotype features the line belongs to (tahoe_atlas.genotype_features: driver "
                         "genes, protein changes, organ, MTAP loss; groups of 3 to n-3 lines), '; '-separated",
    "tp53_status": "TP53 status text of the gene panel (wild type: no TP53 driver row; altered: a TP53 driver row)",
    "tp53_changes": "TP53 protein changes (Tahoe cell_line_metadata)",
    "tp53_source": "where tp53_group comes from",
    "n_cells_total": "cells of the line over all atlas wells (count)",
    "in_growth_analysis": "atlas: the line has enough cells for the relative-abundance analyses",
    "wells_usable": "atlas: wells where the line has >= min_cells cells", "pct_wells_usable": "the same, % of wells",
    "in_drug_metadata": "the drug name matches a row of Tahoe's drug_metadata (after trimming spaces)",
    "n_doses": "drug-doses of the drug in the atlas", "concentrations_uM": "its concentrations, uM (';'-separated)",
    "n_wells": "wells of the drug in the atlas",
    "in_atlas": "the well is in the atlas (False: a failed well the atlas dropped)",
    "status": "used / DMSO control / excluded, and why (see reasons)",
    "reasons": "every flag of the row, ';'-separated (wells: unreliable plate, position not correctable, too few "
               "usable lines; genes: why the gene is in this folder)",
    "used_in_drugdose": "the well counts in its drug-dose (= well_used)",
    "cells": "cells in the well, all lines (count)",
    "n_lines_with_profile": "lines with cells or UMIs in the well", "n_lines_usable": "lines with >= min_cells cells",
    "position_not_correctable": "atlas: < 3 other-drug wells at the position on any plate: no position correction",
    "position_wells_used": "atlas: other-drug wells at the position (position-correction donors)",
    "plate_scale_group": "atlas: the plate-and-dose group whose spread scales the well's z",
    "plate_scale": "atlas: that group's z divisor (>= 1)",
    "composition_shift_log2": LOG2 + ": atlas, median over the well's lines (or the drug-dose's mean) of the "
                              "composition shift",
    "cells_log2_vs_plate": LOG2 + ": atlas, the well's cells vs the plate's median drug well (cell loss; drug-dose: "
                           "mean)",
    "umi_per_cell": "UMIs per cell in the well", "genes_per_cell": "genes detected per cell in the well",
    "n_wells_all": "all wells of the drug-dose, unreliable plates included",
    "wells_left_out": "wells of the drug-dose left out (plate:well, unreliable plates)",
    "unreliable_plate_only": "the drug-dose sits only on unreliable plates (then their wells are used)",
    "umi_per_cell_log2_vs_plate": LOG2 + ": atlas, UMIs per cell vs the plate (mean over used wells)",
    "genes_per_cell_log2_vs_plate": LOG2 + ": atlas, genes per cell vs the plate (mean over used wells)",
    "cells_log2_best_well": LOG2 + ": atlas, the largest cell-loss value of the used wells beyond the plate row",
    "n_sig_genes": "atlas: genes changed by the drug-dose (q < 0.1 and >= 1.2-fold)",
    "n_genes_up": "atlas: genes up (q < 0.1, >= 1.2-fold)", "n_genes_down": "atlas: genes down",
    "replicate_r": "atlas: mean pairwise r of the used wells' z over the top 500 genes",
    "unreliable": "the atlas treats the plate as unreliable",
    "n_wells_in_atlas": "wells of the plate in the atlas", "n_dmso_wells": "DMSO wells of the plate",
    "n_drug_wells_used": "drug wells of the plate used in drug-doses",
    "n_failed_wells": "wells of the plate the atlas dropped as failed",
    "drug_concentrations_uM": "concentrations of the plate's drug wells, uM",
    "feature": "a genotype feature (tahoe_atlas.genotype_features)",
    # gene lists
    "kind": "atlas (an expressed atlas gene) or extra (not an atlas gene: the extra-gene path)",
    "n_reasons": "how many selection rules picked the gene",
    "median_line_cpm": "atlas: the gene's median line level (CPM, all wells pooled)",
    "n_lines_expressing": "atlas: lines that express the gene (expr_mask)",
    "pooled_cpm": "atlas: the gene's level over all lines and wells (CPM)",
    "atlas_col": "column of the gene in the atlas effects arrays (W1.npy, DD_lfc.npy, ...); -1 for extra genes",
    "token": "Tahoe gene token (metadata/gene_metadata.parquet token_id)",
    "file": "the gene's per_profile file (relative to the store folder)",
    "row_group": "the gene's row group in its per_profile / per_drugdose / plate_baselines files",
    "drugdose_file": "the gene's per_drugdose file", "baselines_file": "the gene's plate_baselines file",
    "screen_b_common": "genome_wide screen: common slope of the gene's r2 on the exposure's r2 across lines within "
                       "drug-doses (log2 per log2)",
    "screen_se_common": "genome_wide screen: its conservative two-way (drug, line) cluster SE",
    "screen_t_common": "genome_wide screen: t of the common slope", "screen_p_common": "its p-value",
    "screen_q_common": "its BH q over the tested genes",
    "screen_rank_abs_t_common": "rank of |t_common| among the tested genes (1 = largest)",
    "screen_b_WT": "genome_wide screen: slope in TP53-WT lines", "screen_b_alt": "slope in TP53-altered lines",
    "screen_diff": "genome_wide screen: b_WT - b_alt (log2 per log2)", "screen_t_diff": "its t",
    "screen_q_diff": "its BH q over the tested genes",
    "screen_q_label_diff": "genome_wide: q of the TP53-relabelling null of diff",
    "coreg_r_z_raw": "upstream_coregulation: r of the gene's DD_z with TRIM72's across drug-doses (raw)",
    "coreg_q_raw": "its BH q", "coreg_r_z_minus_3pc": "the same r with 3 genome-wide components removed",
    "coreg_q_minus_3pc": "its BH q",
    "coreg_DoG_class": "upstream_coregulation: readthrough geometry class of the gene",
    "coreg_up_same_strand_expressed_gene": "upstream_coregulation: the expressed same-strand gene upstream of it",
    "dog_class": "upstream_coregulation c_DoG: readthrough geometry class (e.g. sense_exposed: low gene just "
                 "downstream of a strongly expressed same-strand gene)",
    "locus_rel_to_TRIM72": "upstream_coregulation: position relative to TRIM72 (upstream 5' / downstream 3')",
    "locus_same_strand_as_TRIM72": "upstream_coregulation: same strand as TRIM72",
    "locus_distance_bp": "upstream_coregulation: distance to TRIM72 (base pairs)",
    "locus_biotype": "upstream_coregulation: Ensembl biotype",
    "program": "genome_wide program: P (WT-selective induction) or P-down (WT-selective repression)",
    "program_is_fallback": "FALLBACK: fewer than 10 genes passed, so the program is the top 25 by z (exploratory)",
    "program_z_program": "genome_wide: the gene's program z over S2 (drug-equal, permutation-calibrated)",
    "program_q_up": "genome_wide: BH q for WT-selective induction", "program_q_down": "for WT-selective repression",
    "program_wt_minus_alt_log2": "genome_wide: WT minus altered mean response over S2, " + LOG2,
    "program_wt_mean_log2": "genome_wide: WT mean response over S2, " + LOG2,
    "program_rank_in_P": "genome_wide: rank in P by z",
    "program_loco_frequency": "genome_wide: share of leave-one-compound-out programs holding the gene",
    "z_S1_stage1": "genome_wide: program z over S1 (stage 1)", "z_program": "genome_wide: program z over S2",
    "m_drug_equal_z": "genome_wide: drug-equal mean z over S2 (uncalibrated)",
    "p_up": "genome_wide: p for WT-selective induction", "q_up": "its BH q",
    "p_down": "genome_wide: p for WT-selective repression", "q_down": "its BH q",
    "wt_minus_alt_log2": "genome_wide: WT minus altered, drug-weighted over S2, " + LOG2,
    "wt_mean_log2": "genome_wide: WT mean, drug-weighted over S2, " + LOG2,
    "frac_compounds_up": "share of S2 compounds where WT - altered > 0",
    "frac_compounds_down": "share of S2 compounds where WT - altered < 0",
    "frac_compounds_wt_up": "share of S2 compounds where the WT mean > 0",
    "frac_compounds_wt_down": "share of S2 compounds where the WT mean < 0",
    "n_compounds_with_z": "S2 compounds with a value", "in_P1_stage1": "in the stage-1 program",
    "in_P": "in P", "in_P_down": "in P-down", "in_P_noX": "in P without the exposure-moving drug-doses",
    "loco_frequency": "share of leave-one-compound-out programs holding the gene", "rank_in_P": "rank in P by z",
    "is_exposure": "the gene is the exposure", "n_folds_with_gene": "cross-fitted fold programs holding the gene",
    "label": "'overlay': a curated list, used only as a labelled overlay",
    "curated_entry": "the entry as the curated list writes it (gene_modules.csv 'gene/assay', e.g. 'TRIM72_total "
                     "(exon2-exon3 junction)'; the gene symbol for the other lists)",
    "gene_in_atlas": "the gene the curated entry names is an expressed atlas gene (False: not measured or not expressed "
                     "in the atlas: no values, not in the overlay scores)",
    "set": "the curated set's name (OVERLAY_...)", "source": "where the list comes from",
    "rows": "rows of Tahoe's DESeq2 table found for the gene",
    # DESeq2 (Tahoe's own)
    "gene_name": "Tahoe DESeq2: gene symbol", "baseMean": "Tahoe DESeq2: mean normalised count",
    "log2FoldChange": "Tahoe DESeq2: log2 fold change, drug vs the plate's DMSO (u_dmso's reference; but DESeq2's "
                      "size factors also remove library size and much of the composition shift, and the fold change "
                      "is per plate: closer to u_dmso - composition_shift than to u_dmso; tahoe_deseq2/NOTE.md), "
                      + LOG2,
    "lfcSE": "Tahoe DESeq2: its standard error", "stat": "Tahoe DESeq2: Wald statistic",
    "pvalue": "Tahoe DESeq2: p-value", "padj": "Tahoe DESeq2: BH-adjusted p (Tahoe's own adjustment)",
    "plate_atlas": "Tahoe's plate value as the atlas names it (plate<N>): joins to the export's plate",
    "n_cells_trt": "Tahoe DESeq2: treated cells", "n_cells_ctrl": "Tahoe DESeq2: DMSO cells",
    "Cell_ID_Cellosaur": "Cellosaurus id", "Cell_ID_DepMap": "DepMap id",
    "concentration": "Tahoe DESeq2: concentration (see concentration_unit)",
    "concentration_unit": "Tahoe DESeq2: unit of the concentration (uM)", "Cell_Name_Vevo": "Tahoe cell line name",
    "source_file": "the DESeq2 Parquet file the row came from",
    "item": "what the row reports (P_is_fallback, S1_drug_doses, ..., flag)",
    # plate baselines
    "drug_median_log2cpm": "log2 CPM: median over the plate's drug wells of the line's log2cpm (usable profiles; "
                           "the baseline of u_drugmedian)",
    "dmso_log2cpm": "log2 CPM: the line's pooled DMSO level on the plate = log2((dmso_umi + 0.5 k) / "
                    "(dmso_total_umi + k) x 1e6), k = n_dmso_wells_with_line (plate_line.parquet), the atlas's "
                    "plate_offset rule (the baseline of u_dmso; "
                    "empty when dmso_cells < min_cells or the line does not express the gene)",
    "dmso_umi": "the gene's UMIs summed over the plate's DMSO wells for the line (count)",
    "dmso_total_umi": "total UMIs over the plate's DMSO wells for the line (count)",
    "dmso_cells": "cells over the plate's DMSO wells for the line (count)",
    "n_dmso_wells_with_line": "DMSO wells of the plate where the line has UMIs (k, the pseudocount multiplier of "
                              "dmso_log2cpm; at least 1)",
    "check": "what was checked", "value": "the result", "n": "cells or rows compared", "note": "details",
}
_DESEQ_COLS = {
    "plate": "Tahoe DESeq2: the plate exactly as Tahoe stores it (a string such as '4'; plate_atlas names it as the "
             "atlas does)",
    "concentration": "Tahoe DESeq2: the concentration in concentration_unit, at the precision Tahoe stored it (float32 "
                     "in its files, written here as its shortest float32 text: 0.05, not 0.05000000074505806)",
    "concentration_uM": "the concentration in uM (from concentration and concentration_unit; uM when the unit is "
                        "missing): equals the export's concentration_uM",
    "drug_dose_row": "the atlas drug-dose of (drug, concentration_uM) (metadata/drug_doses.csv row); -1: not an atlas "
                     "drug-dose",
    "cell_line_id": "the atlas's cell line (Cellosaurus id): Cell_ID_Cellosaur when the file has it, else mapped from "
                    "Cell_ID_DepMap through metadata/cell_lines.csv depmap_id; empty when neither matches",
}
FILE_C = {  # column descriptions that hold for one file only (pattern as in FILES)
    "tahoe_deseq2/genes.parquet": _DESEQ_COLS,
    "tahoe_deseq2/{G}_deseq2.csv": _DESEQ_COLS,
    "downstream/program_flags.csv": {"value": "its value (True / False, a count, or the flag's text)"},
    "downstream/overlay/curated_sets.csv": {
        "gene": "the gene symbol the curated entry names (the first word without its assay suffix for "
                "gene_modules.csv entries)"},
}
PATTERNS = [  # (regex, description); {G} = the exposure gene
    (r"^{G}_umi_dmso$", "the exposure's UMIs over all DMSO wells of all plates (the unreliable plate included), per "
                        "line (count)"),
    (r"^{G}_total_umi_dmso$", "total UMIs over the same DMSO profiles (count)"),
    (r"^{G}_cpm_dmso$", "the exposure's untreated level: {G}_umi_dmso / {G}_total_umi_dmso x 1e6 (CPM; all plates, "
                        "the unreliable one included)"),
    (r"^{G}_log2cpm_dmso_median_plates$", "the exposure's untreated level per plate (pooled DMSO log2 CPM with the "
                                          "atlas's pseudocount), median over all plates (the unreliable one included; "
                                          "robust to the plate batch)"),
    (r"^{G}_umi_dmso_reliable_plates$", "as {G}_umi_dmso over the plates the atlas treats as reliable only (count)"),
    (r"^{G}_total_umi_dmso_reliable_plates$", "as {G}_total_umi_dmso over the reliable plates only (count)"),
    (r"^{G}_cpm_dmso_reliable_plates$", "as {G}_cpm_dmso over the reliable plates only (CPM)"),
    (r"^{G}_log2cpm_dmso_median_plates_reliable_plates$", "as {G}_log2cpm_dmso_median_plates, median over the "
                                                          "reliable plates only"),
    (r"^{G}_cpm_all_wells$", "atlas line_cpm of the exposure: all wells pooled (CPM)"),
    (r"^{G}_expressed$", "atlas expr_mask of the exposure (the line expresses it)"),
    (r"^{G}_plate_dmso_offset$", "atlas plate_offset of the exposure on the plate, " + LOG2),
    (r"^coreg_TRIM72_log2cpm_vs_plate_mean$", "upstream_coregulation: TRIM72's untreated log2 CPM vs the plate, mean "
                                              "over plates"),
    (r"^coreg_TRIM72_mean_rank_within_plate$", "upstream_coregulation: TRIM72's mean rank among lines within plates"),
    (r"^coreg_FUS_log2cpm_vs_plate_mean$", "upstream_coregulation: FUS's untreated log2 CPM vs the plate, mean"),
    (r"^P(_down)?_r2$", "program score: mean r2 of the program's members the line expresses (P: WT-selective "
                        "induction; P_down: repression), " + LOG2),
    (r"^P(_down)?_u_drugmedian$", "the same mean of u_drugmedian (uncorrected), " + LOG2),
    (r"^P(_down)?_u_dmso$", "the same mean of u_dmso (uncorrected, DMSO reference), " + LOG2),
    (r"^P(_down)?_n_genes_r2$", "members with an r2 value in the profile"),
    (r"^P(_down)?_is_fallback$", "the program is genome_wide's FALLBACK (fewer than 10 genes passed; the top 25 by "
                                 "z; exploratory): read its scores as exploratory"),
    (r"^P(_down)?_n_wells_r2$", "used wells of the drug-dose where the line has a program score (the wells behind "
                                "the _mean columns of r2)"),
    (r"^P(_down)?_(r2|u_drugmedian|u_dmso)_mean$", "the program score's mean over the drug-dose's used wells, " + LOG2),
    (r"^OVERLAY_.*_r2_mean$", "OVERLAY: mean over the used wells of the mean r2 of the set's members, " + LOG2),
    (r"^OVERLAY_.*_u_drugmedian_mean$", "OVERLAY: the same for u_drugmedian, " + LOG2),
    (r"^in_P(_down)?_minus_fold\d+$", "genome_wide: in the cross-fitted program without fold F"),
]
MATRIX_RE = re.compile(r"_matrix_(r2|u_drugmedian|u_dmso)\.csv$")

DOWNSTREAM_MISSING = """# downstream/ is empty in this run

The downstream gene list comes from the DATA: genome_wide's Tahoe p53 program (P, P-down) and its genome-wide screen
(q < 0.1 for the common slope or for WT minus altered). In this run: {reason}. So there is no data-defined downstream
set yet. The curated lists (P53_ACTIVITY and the other repo lists) are NOT exported in its place: they may only appear
as labelled overlays next to a data-defined result.

Run genome_wide (run_mg53_p53.py --steps genome_wide), then the export again (--steps export): the gene tables
(exposure, upstream, downstream) and, when Tahoe's DESeq2 table is present, its rows are rebuilt; the gene store is
kept (with all_genes off it is rebuilt too, because it holds only the selected genes).
"""

UPSTREAM_NOTE = """# upstream/: what this run lacks, and how to read its gene list

## Missing inputs

{lack}

Rerun the export after the missing step: the gene tables are rebuilt, the rest is kept.

## Reading the gene list

{caveats}
- Each gene's reasons (genes.csv) say why it is here: the genome_wide screen (data), upstream_coregulation's
  genome-wide co-regulation partners (data), or the TRIM72 locus (genomic geometry, not a pathway). Moving with the
  exposure is co-variation in mRNA 24 h after treatment, not regulation.
"""

OVERLAY_NOTE = """# overlay/: curated lists, labelled overlay

These are the repo's curated gene lists (the gene panel's 21-gene P53_ACTIVITY, the modules of mg53_p53/gene_modules.csv
and their p53 / MG53-pathway unions, the CollecTRI TP53-activated targets when upstream_tf has cached them). They are
shown next to the data-defined downstream results only to compare with them. They select no gene, drug-dose or line of
this export, and their scores are not an outcome of any analysis here. curated_sets.csv lists every entry, also those
that name no expressed atlas gene (gene_in_atlas False: no values, not in the scores).
"""

DESEQ2_NOTE = """# tahoe_deseq2/: Tahoe's own pseudobulk DESeq2 rows
{warn}
Rows of <data>/metadata/pseudobulk_differential_expression/*.parquet (Tahoe-100M's own table: per gene x drug x
concentration x plate x cell line, the drug wells vs the plate's DMSO wells, DESeq2) for the exposure gene and every
gene of upstream/genes.csv and downstream/genes.csv, read in one streamed pass (row groups whose gene_name statistics
cannot hold a wanted gene are skipped; only the matching rows' columns are kept). {n} rows.

## Joining them to the rest of the export

- Keys added here: plate_atlas (Tahoe's plate '4' -> 'plate4'), concentration_uM (the concentration in uM, at the
  precision Tahoe stored it: a float32 0.05 is written 0.05), drug_dose_row (the atlas drug-dose of drug and
  concentration_uM; -1 when the atlas has none: {nodd} rows) and cell_line_id (Cell_ID_Cellosaur, or mapped from
  Cell_ID_DepMap through metadata/cell_lines.csv depmap_id when the files lack the Cellosaurus id; empty for {nocl}
  rows).
- One Tahoe row is one (gene, drug, concentration, plate, line): the drug's wells of that plate against the plate's
  DMSO wells. Join it to the per-profile rows on (plate = plate_atlas, drug_dose_row, cell_line_id) (one well per
  drug-dose and plate in most cases), or to the per (drug-dose, line) tables on (drug_dose_row, cell_line_id) after
  averaging Tahoe's plates.

## What Tahoe's log2FoldChange is relative to

The plate's DMSO wells, as this export's u_dmso. But DESeq2's size factors already remove library size and much of the
composition shift, and its fold change is per plate (and model-based: possibly shrunk, as Tahoe ran it); so it sits
closer to u_dmso - composition_shift than to u_dmso, and it is not r2 (which is relative to the plate's drug-well
median, after the composition and position corrections). Tahoe's normalisation, model and padj are kept as they are.
"""

DESEQ2_ABSENT = """# tahoe_deseq2/: not available in this data folder

Tahoe's own pseudobulk DESeq2 table (<data>/metadata/pseudobulk_differential_expression/*.parquet: 1,026 files, ~92 GB)
is downloaded only with the setup's --mode full. It is not present here, so nothing was extracted. Everything else of
the export does not need it. With the table present (e.g. after a --mode full download), rerun the export: only this
part runs.
"""


def describe(col, G, pat=None):
    """The column's description: the file's own (FILE_C, pat = the FILES pattern with {G}) first, then C, then
    PATTERNS."""
    if pat is not None:
        for fp, d in FILE_C.items():
            if fp.replace("{G}", G) == pat and col in d:
                return d[col]
    if col in C:
        return C[col]
    for rx, d in PATTERNS:
        if re.match(rx.replace("{G}", re.escape(G)), col):
            return d.replace("{G}", G)
    return None


def pattern_of(rel, G):
    for pat, d in FILES:
        rx = "^" + re.escape(pat.replace("{G}", G)).replace(r"\*", ".*") + "$"
        if re.match(rx, rel):
            return pat.replace("{G}", G), d.replace("{G}", G)
    return None, None


def columns_of(path):
    if path.endswith(".parquet"):
        return pq.read_schema(path).names
    if path.endswith(".csv.gz"):
        import gzip
        with gzip.open(path, "rt", encoding="utf-8") as fh:
            return fh.readline().rstrip("\n").split(",")
    if path.endswith(".csv"):
        with open(path, encoding="utf-8") as fh:
            return fh.readline().rstrip("\n").split(",")
    return None


# always written (some after README.md): documented whether present yet or not
TOP = ("README.md", "checks.csv", "export_info.json", "run_info.json")


def walk(out):
    """The written files below the top level (relative paths)."""
    seen = {}
    for p in sorted(glob.glob(os.path.join(out, "**", "*"), recursive=True)):
        rel = os.path.relpath(p, out)
        if not os.path.isfile(p) or rel.split(os.sep)[0].startswith(".") or p.endswith(".tmp") or rel in TOP:
            continue
        seen.setdefault(rel.replace(os.sep, "/"), p)
    return seen


def undocumented(out, G):
    bad = []
    for rel, p in walk(out).items():
        pat, _d = pattern_of(rel, G)
        if pat is None:
            bad.append(f"{rel}: file not in the README")
            continue
        cols = columns_of(p) or []
        mat = MATRIX_RE.search(rel) is not None
        for c in cols:
            c = c.strip('"')
            if describe(c, G, pat) is None and not mat:     # a matrix's other columns are its cell lines
                bad.append(f"{rel}: {c}")
    return bad


def status_lines(info, gw_ok, co, dfiles, all_genes):
    s = []
    gst = info.get("genome_wide_state", "finished" if gw_ok else "not finished")
    if gw_ok:
        s.append("genome_wide: finished; its Tahoe p53 program and screen define downstream/ and part of upstream/")
    elif gst == "not finished":
        s.append("genome_wide: NOT finished: downstream/ is empty and upstream/ lacks the screen genes (rerun the "
                 "export after genome_wide)")
    else:
        s.append(f"genome_wide: NOT used ({info.get('genome_wide_reason', gst)}): downstream/ is empty and upstream/ "
                 "lacks the screen genes")
    pf = info.get("parts", {}).get("genes", {}).get("program_flags") or []
    if pf:
        s.append("genome_wide's Tahoe p53 program: " + "; ".join(pf) + " (downstream/program_flags.csv)")
    if info.get("r2_source") == "tensor":
        s.append("r2: genome_wide's per (well x line) tensor, reused, and checked here against u_drugmedian - "
                 "composition_shift - position_effect recomputed from the counts (checks.csv)")
    else:
        s.append("r2: computed by upstream_tf.plate_r2 in the pass that built the gene store (genome_wide's tensor was "
                 "absent or keyed to other inputs then); that function builds genome_wide's tensor, so the values are "
                 "the same (the step's tests compare them)")
    s.append("upstream_coregulation: " + (f"tables used ({', '.join(sorted(co))})" if co else
                                          "tables not present: no co-regulation partners, readthrough index or "
                                          "DoG classes in upstream/"))
    s.append("all_genes: " + ("written" if all_genes else "left out (--no-all-genes / MG53_EXPORT_ALL_GENES=0); the "
                              "selected genes are in <out>/.cache/store"))
    dp = info.get("parts", {}).get("deseq2", {})
    if not dfiles:
        s.append("tahoe_deseq2: not present in this data folder (setup --mode full downloads it)")
    elif dp.get("warning"):
        s.append("tahoe_deseq2: " + dp["warning"])
    else:
        s.append(f"tahoe_deseq2: {len(dfiles)} DESeq2 files scanned, {dp.get('rows_kept', '?')} rows kept")
    return s


def _pct(x):
    try:
        return f"{100 * float(x):.0f}%"
    except (TypeError, ValueError):
        return "n/a"


def caveats(info, G):
    """README's 'Reading caveats (mRNA at 24 h)': low counts and survivors, with this run's numbers."""
    r = info.get("parts", {}).get("genes", {}).get("exposure_reading") or {}
    L = ["## Reading caveats (mRNA at 24 h)\n"]
    if r.get("profiles_usable_expressed"):
        lo, hi = (r.get("log2cpm_of_zero_range") or [float("nan")] * 2)
        L.append(f"- **Low counts.** {G} has few UMIs per profile: of the {r['profiles_usable_expressed']:,} usable "
                 f"profiles of lines that express it, {_pct(r.get('frac_zero_umi'))} have 0 UMIs; the median and 90th "
                 f"percentile are {r.get('umi_median', float('nan')):g} and {r.get('umi_p90', float('nan')):g} UMIs "
                 f"(pooled over them: {r.get('cpm_pooled', float('nan')):.3g} CPM). A zero count still gets a log2cpm, "
                 "log2(0.5 / (total_umi + 1) x 1e6): a floor set by the library size alone (here "
                 f"{lo:g} to {hi:g}; {r.get('log2cpm_of_zero_at_median_total', float('nan')):g} at the median library "
                 f"of {r.get('total_umi_median', float('nan')):,.0f} UMIs). So the per-profile u_dmso, u_drugmedian and "
                 "r2 of a low-count gene are largely pseudocount and library-size values: pool the counts first "
                 "(umi_count_sum, total_umi_sum and cpm_pooled per well, per (drug-dose, line) and per drug-dose) and "
                 "read single-profile log ratios of such a gene with care. The same holds for any gene with few UMIs "
                 "(compare umi_count with total_umi).")
    L.append("- **Survivors only.** At 24 h, toxic drug-doses leave fewer cells. n_cells and usable mark what was "
             "measured: a line below min_cells cells in a well has no u_* and no r2 there. It is missing, not "
             "unchanged, and missing not at random (the lines a drug kills drop out first), so the medians and means "
             "over lines (W1, W2, DD_lfc, the per drug-dose medians, program scores) are over the surviving lines."
             + (f" In this run a used drug-well profile is usable in {_pct(r.get('usable_share_other'))} of cases in "
                f"the drug-doses without the atlas's 'toxic' flag and in {_pct(r.get('usable_share_toxic'))} in the "
                f"{r.get('n_drugdoses_toxic', 0)} drug-doses with it." if r.get("n_drugdoses_toxic") else "")
             + " Cell loss: cells_log2_vs_plate and cells_log2_best_well (metadata/wells.csv, metadata/drug_doses.csv, "
             "the per drug-dose tables), the 'toxic' flag in flags; n_lines_r2_mean and n_lines_r2_any count the lines "
             "behind a drug-dose's values, n_wells_r2 the wells behind a (drug-dose, line) mean.")
    L.append("- **Not in any per-profile table:** the wells the atlas dropped as failed (they are listed in "
             "metadata/wells.csv with in_atlas False and their cells), cell lines the atlas dropped (not in "
             "metadata/cell_lines.csv), and (well, line) pairs with neither cells nor UMIs.")
    L.append("- **DMSO wells** are in the per-profile tables and flagged (is_dmso); their u_dmso is relative to a DMSO "
             "pool that includes the well itself, and they belong to no drug-dose.")
    L.append("- **Associations only.** Every value is mRNA 24 h after treatment, and Tahoe has no MG53 perturbation: "
             "a gene moving with TRIM72 across drug-doses and lines is co-variation, not regulation, and says nothing "
             "about MG53 protein.\n")
    return L


def readme(out, info, status, G):
    L = []
    L.append("# MG53 (TRIM72) data export: raw, uncorrected and corrected values (Tahoe-100M, mRNA at 24 h)\n")
    L.append("Written by `mg53_p53/export/export_data.py` (step `export` of `run_mg53_p53.py`). Every value comes "
             "from this data folder's atlas (pseudobulk counts and method-v3 effects); nothing is re-estimated and "
             "nothing new is generated. Exposure gene: **" + G + "**. Tahoe has no MG53 perturbation and measures "
             "mRNA, so every relation between genes here is an association in mRNA 24 h after treatment.\n")
    L.append("## This run\n")
    L += [f"- {x}" for x in status]
    L.append(f"- profiles per gene: {info.get('profiles_per_gene')}; MIN_CELLS {info.get('min_cells')}; MIN_LINES "
             f"{info.get('min_lines')}; upstream genes "
             f"{info.get('parts', {}).get('genes', {}).get('n_upstream_genes', 0)}"
             f"; downstream genes {info.get('parts', {}).get('genes', {}).get('n_downstream_genes', 0)}\n")
    L += caveats(info, G)
    L.append("## How upstream and downstream are read\n")
    L.append("- **Upstream** (what sits above TRIM72 mRNA): which drug-doses raise or lower it (the exposure's "
             "per drug-dose and per (drug-dose, line) tables, with each drug's MoA and targets and the genome-wide "
             "readthrough index); which line traits set its level (line_traits.csv: untreated level, TP53 group, "
             "genotype features); which genes move with it, chosen by the data (genome_wide's common-slope screen, "
             "upstream_coregulation's genome-wide co-regulation partners) or by genomic geometry (the FUS-TRIM72 "
             "locus). Moving with TRIM72 is co-variation, not regulation.\n")
    L.append("- **Downstream** (what goes with more TRIM72): genes whose per-line response tracks TRIM72's within "
             "drug-doses with TP53 genotype as the control (genome_wide's screen), and the p53 program Tahoe itself "
             "defines (P / P-down: TP53-WT-selective response across p53-activating drug-doses chosen genome-wide). "
             "p53 output is read from the mRNA of that program; curated p53 lists are overlays only "
             "(downstream/overlay/).\n")
    L.append("- **Both folders.** A gene whose response tracks TRIM72's (genome_wide's common slope, q < 0.1) is "
             "listed in upstream/ and in downstream/ with the same reason: co-variation within drug-doses has no "
             "direction, so putting it above or below TRIM72 is a reading, not a result of the data. The top 200 "
             "genes by |t_common| are listed upstream even when none is significant; their reasons then say "
             "'not significant' (upstream/NOTE.md counts them).\n")
    L.append("## The values, and what each is relative to\n")
    L.append("| value | meaning |\n|---|---|")
    for c in ("umi_count", "total_umi", "n_cells", "cpm", "log2cpm", "u_dmso", "u_drugmedian", "composition_shift",
              "position_effect", "r2"):
        L.append(f"| `{c}` | {C[c]} |")
    L.append("")
    L.append("Derivations (exact): `cpm = umi_count / total_umi x 1e6`; `log2cpm = log2((umi_count + 0.5) / (total_umi "
             "+ 1) x 1e6)`; `u_drugmedian = log2cpm - drug_median_log2cpm[plate, line, gene]`; `u_dmso = log2cpm - "
             "dmso_log2cpm[plate, line, gene]` (both baselines in `all_genes/plate_baselines/`, so per (plate, line) "
             "`u_dmso - u_drugmedian = drug_median_log2cpm - dmso_log2cpm`, the same in every well of the plate; the "
             "atlas's plate_offset is its median over lines); `r2 = u_drugmedian - composition_shift - "
             "position_effect` (all_genes/profiles.parquet has composition_shift). all_genes/ leaves out cpm, log2cpm "
             "and composition_shift per row to stay ~21 GB on the real data; `export_genes.py` adds them back. Per "
             "(drug-dose, line): `r2_mean = u_drugmedian_mean_r2wells - composition_shift_mean - "
             "position_effect_mean` (all over the n_wells_r2 wells); u_drugmedian_mean and u_dmso_mean are over every "
             "used well with a value (n_wells_u, n_wells_u_dmso).\n")
    L.append("## Reading it\n")
    L.append("One gene or a few, as CSV with every column (fast: reads only those genes' row groups):\n")
    L.append("```bash\npython3 mg53_p53/export/export_genes.py --export <this folder> --genes FUS,ATF3 --out x.csv\n"
             "python3 mg53_p53/export/export_genes.py --export <this folder> --set upstream --level drugdose_line "
             "--out up.csv.gz\n```\n")
    L.append("(`--level drugdose_line` or `drugdose` for the summaries; `--set upstream` / `downstream` for a folder's "
             "genes; `.parquet` output for large sets.) In Python, through the index (`all_genes/genes.csv`: gene -> "
             "file and row group; one row group per gene, so this reads one gene only):\n")
    L.append("```python\nimport pandas as pd, pyarrow.parquet as pq\n"
             f"x = pd.read_csv('{G}/{G}_per_profile.csv')                      # one gene, every profile\n"
             "idx = pd.read_csv('all_genes/genes.csv').set_index('gene')\n"
             "e = idx.loc['FUS']\n"
             "t = pq.ParquetFile('all_genes/' + e['file']).read_row_group(int(e['row_group'])).to_pandas()\n```\n")
    L.append("DuckDB (fast, also for filters on other columns): `SELECT * FROM 'all_genes/per_profile/*.parquet' WHERE "
             "gene = 'FUS'`. R: `arrow::open_dataset('all_genes/per_profile') |> dplyr::filter(gene == 'FUS') |> "
             "dplyr::collect()`; this, like pyarrow.dataset's filter, scans every file's gene column (16,643 row "
             "groups on the real data: ~1-2 min per query), so prefer the index or DuckDB for single genes. "
             "concentration_uM is float64 everywhere, so `== 0.05` matches.\n")
    L.append("## Files and columns\n")
    for t in TOP:
        L.append(f"### `{t}`\n")
        L.append(dict(FILES)[t] + "\n")
        if t == "checks.csv":
            L += [f"- `{c}`: {C[c]}" for c in ("check", "value", "n", "note")]
            L.append("")
    files = walk(out)
    done = set(TOP)
    order = ["metadata/", "{G}/", "upstream/", "downstream/", "all_genes/", "tahoe_deseq2/"]
    pats = sorted((pd_ for pd_ in FILES if pd_[0] not in TOP),
                  key=lambda pd_: next((k for k, o in enumerate(order) if pd_[0].startswith(o)), len(order)))
    for pat0, d0 in pats:                                       # the README's order: the FILES table, by folder
        pat, d = pat0.replace("{G}", G), d0.replace("{G}", G)
        rx = "^" + re.escape(pat).replace(r"\*", ".*") + "$"
        hit = next((p for rel, p in files.items() if re.match(rx, rel)), None)
        if hit is None or pat in done:
            continue
        done.add(pat)
        L.append(f"### `{pat}`\n")
        L.append(d + "\n")
        cols = columns_of(hit)
        if cols:
            mat = MATRIX_RE.search(hit) is not None
            for c in cols:
                c = c.strip('"')
                if mat and describe(c, G, pat) is None:
                    continue
                L.append(f"- `{c}`: {describe(c, G, pat) or 'UNDOCUMENTED'}")
            if mat:
                L.append("- one column per cell line (Cellosaurus id): the value named in the file description")
            L.append("")
    missing = [pat.replace("{G}", G) for pat, _ in FILES if pat.replace("{G}", G) not in done
               and "*" not in pat and not pat.endswith(("README.md", "NOTE.md"))]
    if missing:
        L.append("## Not written in this run\n")
        L += [f"- `{m}`" for m in missing]
        L.append("")
    return "\n".join(L) + "\n"

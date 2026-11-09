---
symbol: "EPB41L3"
type: "gene"
col: 1345
ensembl_id: "ENSG00000082397"
name: "erythrocyte membrane protein band 4.1 like 3"
location: "18p11.31"
module: 19
arm: "+"
pooled_cpm: 76.34
n_lines_expressing: 16
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 12
direction_downstream: 11
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# EPB41L3

*erythrocyte membrane protein band 4.1 like 3* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.24× (z +11.4, q 1e-27, up in 10 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.62× (z +6.7, q 3e-09, up in 6 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.553× (z -5.8, q 5e-06, down in 9 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRD1]] (+0.71, fdr 8e-06), [[CTNND2]] (+0.71, fdr 8e-06), [[NCKAP5-AS2]] (+0.70, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[GREM2]] → it (grade C ⚠); 11 go from it, the strongest it → [[RIMS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1345.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +11.4 | 1e-27 | 10/15 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +9.0 | 9e-17 | 10/14 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +6.7 | 3e-09 | 6/14 (LoVo, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +6.7 | 3e-09 | 8/14 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.6 | 2e-06 | 4/14 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.52×** | +4.1 | 0.004 | 1/14 (C32) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.050 | 5/14 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.63×** | +3.4 | 0.050 | 1/14 (CHP-212) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1345.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.553×** | -5.8 | 5e-06 | 9/14 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.606×** | -4.5 | 0.002 | 1/14 (NCI-H460) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.737×** | -4.2 | 0.004 | 9/14 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.734×** | -4.2 | 0.004 | 1/14 (NCI-H460) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.680×** | -3.7 | 0.020 | 3/14 (NCI-H460, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.692×** | -3.4 | 0.056 | 7/14 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.712×** | -3.3 | 0.081 | 5/14 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.726× | -3.1 | 0.13 | 4/14 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Encorafenib (drug)]] 5 µM |  | 0.553× | -3.0 | 0.17 | 1/14 (LOX-IMVI) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1345. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1,147 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -21.2) |
| [[LoVo (line)]] | wt | 24.6 | 7 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +14.1) | — |
| [[HOP62 (line)]] | alt | 39.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 124 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 60.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 50.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.9) |
| [[A-427 (line)]] | wt | 67.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -8.9) |
| [[A498 (line)]] | wt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -10.5) |
| [[CHP-212 (line)]] | wt | 43.0 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.121× (z -8.5) |
| [[SNU-423 (line)]] | alt | 42.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.0) |
| [[A-172 (line)]] | wt | 7.44 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.87 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.49 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.37 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.95 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.92 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.26 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.05 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.54 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.44 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.79 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.8 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.26 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.59 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.91 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1345), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRD1]] | +0.71 | +0.58 / +0.71 | both halves | 8e-06 |  |
| [[CTNND2]] | +0.71 | +0.58 / +0.71 | both halves | 8e-06 |  |
| [[NCKAP5-AS2]] | +0.70 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[LINC03000]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[GTF2I-AS1]] | +0.69 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SPDYE10]] | +0.69 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[SERPINB11]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[GREM2]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SLITRK4]] | +0.67 | +0.51 / +0.68 | both halves | 1e-05 | pathway: Neuronal System |
| [[DPP10]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[KCNK2]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 | pathway: Neuronal System |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GREM2]] | C | GREM2 activity raises EPB41L3's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 4.24× lower at baseline in the lines without GREM2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises EPB41L3's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 3.26× lower at baseline in the lines without PDE3A | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[CHL1]] | C | CHL1 activity raises EPB41L3's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 5.26× lower at baseline in the lines without CHL1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[PDE1A]] | C | PDE1A activity raises EPB41L3's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 3.56× lower at baseline in the lines without PDE1A | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises EPB41L3's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 5.91× lower at baseline in the lines without GTF2I-AS1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises EPB41L3's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.26× lower at baseline in the lines without CTNND2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[FENDRR]] | C | FENDRR activity raises EPB41L3's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 3.59× lower at baseline in the lines without FENDRR | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises EPB41L3's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 4.88× lower at baseline in the lines without LINC03000 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises EPB41L3's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 3.74× lower at baseline in the lines without SCARA5 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[ADGRB3]] | C | ADGRB3 activity raises EPB41L3's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 2.95× lower at baseline in the lines without ADGRB3 | 0.088 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |
| [[PAPPA2]] | C | PAPPA2 activity raises EPB41L3's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without PAPPA2 | 0.091 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent; co-absent with the target |
| [[GASK1B]] | C | GASK1B activity raises EPB41L3's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 2.35× lower at baseline in the lines without GASK1B | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIMS1]] | B | EPB41L3 activity raises RIMS1's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 2.41× lower at baseline in the lines without EPB41L3 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R |
| [[SLCO1C1]] | B | EPB41L3 activity raises SLCO1C1's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 1.88× lower at baseline in the lines without EPB41L3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R |
| [[RADIL]] | B | EPB41L3 activity raises RADIL's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 1.78× lower at baseline in the lines without EPB41L3 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R |
| [[PDE3A]] | C | EPB41L3 activity raises PDE3A's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 4.16× lower at baseline in the lines without EPB41L3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |
| [[ADGRB3]] | C | EPB41L3 activity raises ADGRB3's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 5.39× lower at baseline in the lines without EPB41L3 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |
| [[CHL1]] | C | EPB41L3 activity raises CHL1's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 2.99× lower at baseline in the lines without EPB41L3 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |
| [[GREM2]] | C | EPB41L3 activity raises GREM2's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 2.95× lower at baseline in the lines without EPB41L3 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |
| [[PAPPA2]] | C | EPB41L3 activity raises PAPPA2's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 2.44× lower at baseline in the lines without EPB41L3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |
| [[SNCA]] | C | EPB41L3 activity raises SNCA's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 4.49× lower at baseline in the lines without EPB41L3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |
| [[FENDRR]] | C | EPB41L3 activity raises FENDRR's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 2.24× lower at baseline in the lines without EPB41L3 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |
| [[SEMA3D]] | C | EPB41L3 activity raises SEMA3D's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 2.26× lower at baseline in the lines without EPB41L3 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.5, 35.9); signed map (42.4, 44.6). **Vector** length 54.9, 18.3% of its response variance represented; |z| ≥ 3 in 348 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.3 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -4.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | erythrocyte membrane protein band 4.1 like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.31 — chr18:5,392,381-5,630,700 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DAL1, KIAA0987, 4.1B |
| Gene groups (HGNC) | Erythrocyte membrane protein band 4.1; FERM domain containing |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 7 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Neurexins and neuroligins; Sensory processing of sound by inner hair cells of the cochlea |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2J2](https://www.uniprot.org/uniprotkb/Q9Y2J2) (Band 4.1-like protein 3):

> Tumor suppressor that inhibits cell proliferation and promotes apoptosis. Modulates the activity of protein arginine N-methyltransferases, including PRMT3 and PRMT5.

**Summary**, from NCBI Gene [23136](https://www.ncbi.nlm.nih.gov/gene/23136):

> Predicted to enable cytoskeletal protein-membrane anchor activity. Predicted to be a structural constituent of cytoskeleton. Predicted to be involved in several processes, including nervous system development; paranodal junction maintenance; and protein localization to juxtaparanode region of axon. Located in cell-cell junction and plasma membrane. Implicated in esophagus squamous cell carcinoma. Biomarker of meningioma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3380) · Entrez [23136](https://www.ncbi.nlm.nih.gov/gene/23136) · UniProt [Q9Y2J2](https://www.uniprot.org/uniprotkb/Q9Y2J2) · Ensembl [ENSG00000082397](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082397)

## Data

Gene col 1345: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1345); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1345, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1345]; `tensor/DDL_lfc|DDL_z.npy` [1345]; `embed/gene_vectors.npy` [1345]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1345 or target_col == 1345). Every well: [[EPB41L3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPB41L3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

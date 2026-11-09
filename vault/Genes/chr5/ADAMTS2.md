---
symbol: "ADAMTS2"
type: "gene"
col: 1486
ensembl_id: "ENSG00000087116"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 2"
location: "5q35.3"
module: 13
arm: "+"
pooled_cpm: 12.23
n_lines_expressing: 21
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 38
direction_downstream: 42
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ADAMTS2

*ADAM metallopeptidase with thrombospondin type 1 motif 2* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.58× (z +17.0, q 0e+00, up in 4 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.677× (z -5.0, q 4e-04, down in 8 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND2A]] (+0.66, fdr 1e-05), [[COL5A1]] (+0.65, fdr 8e-06), [[LOX]] (+0.65, fdr 7e-06); moves opposite to [[SSTR2]] (-0.44, fdr 1e-04), [[DLEU1]] (-0.43, fdr 6e-05), [[AP1G2]] (-0.43, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[CACNA1C]] → it (grade B ⚠); 42 go from it, the strongest it → [[CACNA1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +17.0 | 0e+00 | 4/15 (AN3 CA, SW 900, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.07×** | +13.7 | 2e-40 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.93×** | +13.7 | 3e-40 | 1/12 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +10.6 | 3e-24 | 4/16 (C-33 A, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +5.3 | 1e-05 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 1e-03 | 4/16 (HOP62, SW 900, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +4.3 | 0.001 | 1/9 (A-172) | rises with dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.003 | 0/17 | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +4.0 | 0.004 | 5/16 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.004 | 3/16 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.005 | 3/18 (H4, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.013 | 3/17 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.5 | 0.019 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.033 | 4/18 (A498, J82, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.036 | 1/16 (HOP62) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.061 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.061 | 0/16 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.062 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1486.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -5.0 | 4e-04 | 8/17 (HOP62, J82, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 5 µM |  | **0.793×** | -4.2 | 0.008 | 4/18 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.733×** | -4.0 | 0.014 | 5/17 (H4, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.750×** | -3.7 | 0.035 | 11/17 (HOP62, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.771× | -3.3 | 0.10 | 11/17 (A498, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | 0.772× | -3.2 | 0.14 | 4/17 (HS-578T, hTERT-HPNE, …) | rises with dose | plate-row cell shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -3.1 | 0.18 | 1/19 (SW 900) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 53.8 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -23.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.155× (z -18.5) |
| [[CHP-212 (line)]] | wt | 86.7 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0262× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.0735× (z -10.6) |
| [[HS-578T (line)]] | alt | 180 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -16.0) |
| [[HOP62 (line)]] | alt | 29.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -12.5) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 90.0 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -10.9) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.154× (z -10.0) |
| [[A-427 (line)]] | wt | 11.6 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 24.1 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.202× (z -9.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -8.8) |
| [[A-172 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.136× (z -10.0) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SNU-423 (line)]] | alt | 50.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.287× (z -13.8) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A549 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.969 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND2A]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[COL5A1]] | +0.65 | +0.70 / +0.58 | both halves | 8e-06 | pathway: Collagen biosynthesis and modifying enzymes; STRING 826 |
| [[LOX]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 | pathway: Collagen formation; STRING 750 |
| [[PDGFRB]] | +0.63 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[PTGFR]] | +0.62 | +0.65 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[ITGA8]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[PRR16]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[CARMN]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[GPR173]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[COL6A3]] | +0.60 | +0.58 / +0.58 | both halves | 8e-06 | pathway: Collagen biosynthesis and modifying enzymes; STRING 487 |
| [[CPQ]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[WNT5A]] | +0.58 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSTR2]] | -0.44 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[DLEU1]] | -0.43 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[AP1G2]] | -0.43 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[PATJ]] | -0.42 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[LINC00958]] | -0.42 | -0.48 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 1, C 37. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1C]] | B | CACNA1C activity raises ADAMTS2's level | lines that do not express CACNA1C (13) vs lines expressing it (37) | 3.26× lower at baseline in the lines without CACNA1C | 0.094 | ⚠ within organs, on part of the lines; also absent: CNTNAP2, PSD2, LINC01579; maybe low, not absent |
| [[PDGFRB]] | C | PDGFRB activity raises ADAMTS2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 6.84× lower at baseline in the lines without PDGFRB | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[FBXL7]] | C | FBXL7 activity raises ADAMTS2's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 3.28× lower at baseline in the lines without FBXL7 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[ZNF667]] | C | ZNF667 activity raises ADAMTS2's level | lines that do not express ZNF667 (35) vs lines expressing it (15) | 2.95× lower at baseline in the lines without ZNF667 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667-AS1, ADAMTS2, COL11A1; co-absent with the target |
| [[EVC2]] | C | EVC2 activity raises ADAMTS2's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 3.55× lower at baseline in the lines without EVC2 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[ZEB2]] | C | ZEB2 activity raises ADAMTS2's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 4.12× lower at baseline in the lines without ZEB2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[TWIST1]] | C | TWIST1 activity raises ADAMTS2's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 2.77× lower at baseline in the lines without TWIST1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[LINC01615]] | C | LINC01615 activity raises ADAMTS2's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 3.53× lower at baseline in the lines without LINC01615 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises ADAMTS2's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 4.15× lower at baseline in the lines without ITGA4 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[MME]] | C | MME activity raises ADAMTS2's level | lines that do not express MME (30) vs lines expressing it (20) | 3.29× lower at baseline in the lines without MME | 0.025 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises ADAMTS2's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 3.99× lower at baseline in the lines without APCDD1L | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises ADAMTS2's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 4.86× lower at baseline in the lines without COL5A1 | 0.036 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 6, C 36. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1C]] | B | ADAMTS2 activity raises CACNA1C's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 3.19× lower at baseline in the lines without ADAMTS2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1 |
| [[TRAM2]] | B | ADAMTS2 activity raises TRAM2's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 2.38× lower at baseline in the lines without ADAMTS2 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1 |
| [[LTBP1]] | B | ADAMTS2 activity raises LTBP1's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 2.13× lower at baseline in the lines without ADAMTS2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1 |
| [[IPO9-AS1]] | B | ADAMTS2 activity raises IPO9-AS1's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 1.53× lower at baseline in the lines without ADAMTS2 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1 |
| [[CPQ]] | B | ADAMTS2 activity raises CPQ's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 3.32× lower at baseline in the lines without ADAMTS2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1 |
| [[KIAA1614]] | B | ADAMTS2 activity raises KIAA1614's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 1.51× lower at baseline in the lines without ADAMTS2 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1 |
| [[ZNF667]] | C | ADAMTS2 activity raises ZNF667's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 5.84× lower at baseline in the lines without ADAMTS2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[PDGFRB]] | C | ADAMTS2 activity raises PDGFRB's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 6.30× lower at baseline in the lines without ADAMTS2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[DKK3]] | C | ADAMTS2 activity raises DKK3's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 4.39× lower at baseline in the lines without ADAMTS2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[COL5A1]] | C | ADAMTS2 activity raises COL5A1's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 9.42× lower at baseline in the lines without ADAMTS2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[DENND2A]] | C | ADAMTS2 activity raises DENND2A's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 3.59× lower at baseline in the lines without ADAMTS2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[GLIS1]] | C | ADAMTS2 activity raises GLIS1's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 3.72× lower at baseline in the lines without ADAMTS2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.7, 20.3); signed map (27.1, 46.1). **Vector** length 60.2, 17.8% of its response variance represented; |z| ≥ 3 in 504 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +5.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +1.8 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.4 | +4.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.3 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +0.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.2 | +3.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.2 | +2.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:179,110,853-179,345,461 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADAMTS-3, hPCPNI, PCINP, ADAM-TS2, NPI |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 9 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O95450](https://www.uniprot.org/uniprotkb/O95450) (A disintegrin and metalloproteinase with thrombospondin motifs 2):

> Cleaves the propeptides of type I and II collagen prior to fibril assembly (By similarity). Does not act on type III collagen (By similarity). Cleaves lysyl oxidase LOX at a site downstream of its propeptide cleavage site to produce a short LOX form with reduced collagen-binding activity.

**Summary**, from NCBI Gene [9509](https://www.ncbi.nlm.nih.gov/gene/9509):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motifs) protein family. Members of the family share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. The encoded preproprotein is proteolytically processed to generate …

**Accessions** — [HGNC:218](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:218) · Entrez [9509](https://www.ncbi.nlm.nih.gov/gene/9509) · UniProt [O95450](https://www.uniprot.org/uniprotkb/O95450) · Ensembl [ENSG00000087116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087116)

## Data

Gene col 1486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1486); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1486]; `tensor/DDL_lfc|DDL_z.npy` [1486]; `embed/gene_vectors.npy` [1486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1486 or target_col == 1486). Every well: [[ADAMTS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "COL6A2"
type: "gene"
col: 6601
ensembl_id: "ENSG00000142173"
name: "collagen type VI alpha 2 chain"
location: "21q22.3"
module: 13
arm: "+"
pooled_cpm: 100.96
n_lines_expressing: 22
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 44
direction_downstream: 30
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# COL6A2

*collagen type VI alpha 2 chain* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +13.0, q 5e-36, up in 11 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.41× (z +4.5, q 9e-04, up in 6 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.491× (z -9.3, q 7e-18, down in 15 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL6A1]] (+0.86, fdr 7e-06), [[THBS2]] (+0.79, fdr 7e-06), [[RFX8]] (+0.72, fdr 7e-06); moves opposite to [[SH2D4A]] (-0.52, fdr 2e-04), [[SMAD1]] (-0.47, fdr 1e-04), [[DPY19L1P1]] (-0.47, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[GPR68]] → it (grade B ⚠); 30 go from it, the strongest it → [[LLGL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +13.0 | 5e-36 | 11/20 (HS-578T, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +10.1 | 2e-21 | 10/17 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +9.8 | 3e-20 | 9/17 (HS-578T, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 9e-04 | 6/21 (HS-578T, SNU-423, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.006 | 2/19 (SW 900, AN3 CA) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.007 | 4/20 (HS-578T, Panc 03.27, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.019 | 9/20 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6601.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.491×** | -9.3 | 7e-18 | 15/20 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.641×** | -8.9 | 1e-16 | 16/20 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.614×** | -6.6 | 6e-09 | 15/20 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -4.8 | 2e-04 | 6/20 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.736×** | -4.2 | 0.003 | 13/20 (CFPAC-1, hTERT-HPNE, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.813×** | -4.1 | 0.003 | 12/20 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.751×** | -4.1 | 0.004 | 6/19 (H4, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.818×** | -4.0 | 0.004 | 13/21 (SNU-423, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.749×** | -3.8 | 0.009 | 5/20 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.774×** | -3.4 | 0.044 | 10/20 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.845× | -3.3 | 0.044 | 4/20 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.793×** | -3.3 | 0.049 | 11/20 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.784×** | -3.3 | 0.050 | 1/20 (AN3 CA) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.727×** | -3.2 | 0.050 | 1/20 (A-427) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.807×** | -3.0 | 0.088 | 8/20 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.810×** | -3.0 | 0.096 | 10/20 (hTERT-HPNE, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 177 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -15.6) |
| [[hTERT-HPNE (line)]] | wt | 1,179 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -13.8) |
| [[HOP62 (line)]] | alt | 931 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -20.2) |
| [[LOX-IMVI (line)]] | wt | 237 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -20.3) |
| [[HS-578T (line)]] | alt | 408 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 51.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.7) |
| [[SNU-423 (line)]] | alt | 247 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -10.9) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.8) |
| [[A-172 (line)]] | wt | 173 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.8) |
| [[A-427 (line)]] | wt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -15.0) |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.0684× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 62.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0787× (z -19.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 660 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.4) |
| [[A498 (line)]] | wt | 90.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.48 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.1 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.80 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.26 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.79 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.87 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.89 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.15 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.72 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.72 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.88 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 611 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.29 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL6A1]] | +0.86 | +0.87 / +0.85 | both halves | 7e-06 | same gene group; pathway: Assembly of collagen fibrils and other multimeric structures; STRING 998 |
| [[THBS2]] | +0.79 | +0.79 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 754 |
| [[RFX8]] | +0.72 | +0.74 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[COL6A3]] | +0.70 | +0.76 / +0.64 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 994 |
| [[ITGA11]] | +0.69 | +0.64 / +0.65 | both halves | 7e-06 | pathway: Extracellular matrix organization; STRING 863 |
| [[SHANK1]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[CSPG4]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 | STRING 409 |
| [[COL5A1]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 862 |
| [[LINC01615]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TSHZ3]] | +0.63 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[FAM167A]] | +0.62 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH2D4A]] | -0.52 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[SMAD1]] | -0.47 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[DPY19L1P1]] | -0.47 | -0.45 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 3, C 41. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR68]] | B | GPR68 activity raises COL6A2's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 3.42× lower at baseline in the lines without GPR68 | 0.048 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[RAC2]] | B | RAC2 activity raises COL6A2's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 2.99× lower at baseline in the lines without RAC2 | 0.094 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[TOP2A]] | B | TOP2A activity raises COL6A2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[EDNRA]] | C | EDNRA activity raises COL6A2's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 8.90× lower at baseline in the lines without EDNRA | 0.001 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises COL6A2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 9.51× lower at baseline in the lines without PDGFRB | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises COL6A2's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 8.20× lower at baseline in the lines without APCDD1L | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[LINC01615]] | C | LINC01615 activity raises COL6A2's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 8.02× lower at baseline in the lines without LINC01615 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC; co-absent with the target |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises COL6A2's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 8.00× lower at baseline in the lines without HS3ST3A1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises COL6A2's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 6.00× lower at baseline in the lines without WNT5A | 0.009 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[RFX8]] | C | RFX8 activity raises COL6A2's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 5.55× lower at baseline in the lines without RFX8 | 0.014 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |
| [[COL6A1]] | C | COL6A1 activity raises COL6A2's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 7.12× lower at baseline in the lines without COL6A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN; co-absent with the target |
| [[TENM2]] | C | TENM2 activity raises COL6A2's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 5.73× lower at baseline in the lines without TENM2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 12, C 18. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LLGL1]] | B | COL6A2 activity raises LLGL1's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 1.48× lower at baseline in the lines without COL6A2 | 0.018 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[TMEM132B]] | B | COL6A2 activity weakens TMEM132B's drug response | lines that do not express COL6A2 (24) vs lines expressing it (17) | the lines without COL6A2 respond 1.74× as strongly (z diff -2.07); strongest at Homoharringtonine 5 µM: 2.02x vs 0.70x (z diff -5.9) | 0.020 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2; target measured in part of the lines; artifact flags |
| [[ANXA6]] | B | COL6A2 activity raises ANXA6's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 2.71× lower at baseline in the lines without COL6A2 | 0.020 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[COL23A1]] | B | COL6A2 activity raises COL23A1's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without COL6A2 | 0.026 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[TGFB1]] | B | COL6A2 activity raises TGFB1's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 2.77× lower at baseline in the lines without COL6A2 | 0.030 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[JARID2]] | B | COL6A2 activity raises JARID2's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 1.74× lower at baseline in the lines without COL6A2 | 0.032 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[RAC2]] | B | COL6A2 activity raises RAC2's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 3.59× lower at baseline in the lines without COL6A2 | 0.040 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[SORCS2]] | B | COL6A2 activity raises SORCS2's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 2.32× lower at baseline in the lines without COL6A2 | 0.050 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[SEMA7A]] | B | COL6A2 activity raises SEMA7A's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 1.92× lower at baseline in the lines without COL6A2 | 0.058 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[TGFB1I1]] | B | COL6A2 activity raises TGFB1I1's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 2.12× lower at baseline in the lines without COL6A2 | 0.059 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[HMGA2-AS1]] | B | COL6A2 activity raises HMGA2-AS1's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 1.42× lower at baseline in the lines without COL6A2 | 0.077 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[DPY19L1P1]] | B | COL6A2 activity lowers DPY19L1P1's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 1.33× higher at baseline in the lines without COL6A2 | 0.099 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.1, 17.8); signed map (24.3, 45.5). **Vector** length 75.3, 26.5% of its response variance represented; |z| ≥ 3 in 489 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | -1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.3 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -3.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -6.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.2 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | collagen type VI alpha 2 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:46,098,112-46,132,848 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Collagens |
| Hallmark sets | MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 15 pathways, smallest: NCAM1 interactions; Collagen chain trimerization; Collagen degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P12110](https://www.uniprot.org/uniprotkb/P12110) (Collagen alpha-2(VI) chain):

> Collagen VI acts as a cell-binding protein.

**Summary**, from NCBI Gene [1292](https://www.ncbi.nlm.nih.gov/gene/1292):

> This gene encodes one of the three alpha chains of type VI collagen, a beaded filament collagen found in most connective tissues. The product of this gene contains several domains similar to von Willebrand Factor type A domains. These domains have been shown to bind extracellular matrix proteins, an interaction that explains the importance of this collagen in organizing matrix components. Mutations in this gene are associated with Bethlem myopathy and Ullrich scleroatonic muscular dystrophy. …

**Accessions** — [HGNC:2212](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2212) · Entrez [1292](https://www.ncbi.nlm.nih.gov/gene/1292) · UniProt [P12110](https://www.uniprot.org/uniprotkb/P12110) · Ensembl [ENSG00000142173](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142173)

## Data

Gene col 6601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6601); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6601]; `tensor/DDL_lfc|DDL_z.npy` [6601]; `embed/gene_vectors.npy` [6601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6601 or target_col == 6601). Every well: [[COL6A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL6A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

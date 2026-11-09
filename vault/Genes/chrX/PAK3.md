---
symbol: "PAK3"
type: "gene"
col: 1182
ensembl_id: "ENSG00000077264"
name: "p21 (RAC1) activated kinase 3"
location: "Xq23"
module: 19
arm: "+"
pooled_cpm: 34.04
n_lines_expressing: 18
n_dd_up: 13
n_dd_down: 17
n_dd_up_clean: 5
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 16
direction_downstream: 7
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PAK3

*p21 (RAC1) activated kinase 3* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.24× (z +13.4, q 5e-38, up in 10 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.79× (z +7.6, q 3e-12, up in 10 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.613× (z -4.5, q 0.002, down in 8 of 16 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.711× (z -4.5, q 0.002, down in 13 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL4A6]] (+0.71, fdr 7e-06), [[ST8SIA4]] (+0.70, fdr 7e-06), [[SCUBE1]] (+0.69, fdr 1e-05); moves opposite to [[DGKH]] (-0.47, fdr 6e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[PLAC4]] → it (grade B ⚠); 7 go from it, the strongest it → [[SLC14A1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1182.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.24×** | +13.4 | 5e-38 | 10/14 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.54×** | +11.3 | 6e-27 | 8/12 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.08×** | +9.6 | 1e-19 | 6/14 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +7.6 | 3e-12 | 10/16 (NCI-H2347, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.007 | 10/16 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.4 | 0.058 | 3/15 (HOP62, A498, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.44×** | +3.4 | 0.058 | 6/16 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.071 | 0/16 | top dose only | cell-cycle shift (explains ~6% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.2 | 0.077 | 0/14 | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.41×** | +3.2 | 0.077 | 9/16 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.087 | 7/16 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.39×** | +3.1 | 0.097 | 7/15 (HOP62, A498, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.65×** | +3.0 | 0.100 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.5 µM |  | 1.64× | +3.0 | 0.10 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.613×** | -4.5 | 0.002 | 8/16 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.711×** | -4.5 | 0.002 | 13/16 (Hs 766T, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.620×** | -4.4 | 0.002 | 11/16 (Hs 766T, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.625×** | -4.3 | 0.002 | 13/16 (SK-MEL-2, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.629×** | -4.0 | 0.008 | 5/16 (SW 1088, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.671×** | -3.7 | 0.022 | 6/16 (NCI-H460, A498, …) | all doses, flat |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.657×** | -3.6 | 0.027 | 0/15 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.663×** | -3.5 | 0.032 | 0/15 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.689×** | -3.4 | 0.036 | 4/14 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.693×** | -3.4 | 0.039 | 6/16 (H4, RPMI-7951, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.779×** | -3.3 | 0.058 | 10/16 (Hs 766T, SW 900, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.707×** | -3.2 | 0.064 | 5/15 (Hs 766T, SNU-423, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -3.2 | 0.064 | 4/15 (SW 900, HOP62, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.714×** | -3.1 | 0.075 | 5/14 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.720×** | -3.0 | 0.092 | 9/16 (Hs 766T, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.723×** | -3.0 | 0.095 | 8/16 (SHP-77, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 372 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -13.2) |
| [[SHP-77 (line)]] | alt | 82.8 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -12.4) |
| [[Hs 766T (line)]] | wt | 320 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -18.0) |
| [[H4 (line)]] | wt | 30.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -10.2) |
| [[SW 900 (line)]] | alt | 73.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 9.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 11.2 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0829× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -9.2) |
| [[SNU-423 (line)]] | alt | 31.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -8.5) |
| [[A-172 (line)]] | wt | 5.34 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.23 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.65 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.62 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.51 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.39 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.59 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.22 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL4A6]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[ST8SIA4]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SCUBE1]] | +0.69 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[NCKAP5]] | +0.68 | +0.61 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SMOC1]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SLITRK4]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[CNTN1]] | +0.67 | +0.55 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[CDH11]] | +0.67 | +0.60 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[PDE7B]] | +0.64 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.62 | +0.57 / +0.63 | both halves | 8e-06 |  |
| [[TENM1]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PDE1C]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKH]] | -0.47 | -0.44 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 1, C 15. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAC4]] | B | PLAC4 activity raises PAK3's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without PLAC4 | 0.061 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[DPP10]] | C | DPP10 activity raises PAK3's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 4.05× lower at baseline in the lines without DPP10 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[ANGPTL2]] | C | ANGPTL2 activity raises PAK3's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 3.43× lower at baseline in the lines without ANGPTL2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |
| [[FENDRR]] | C | FENDRR activity raises PAK3's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 3.74× lower at baseline in the lines without FENDRR | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[KCNK2]] | C | KCNK2 activity raises PAK3's level | lines that do not express KCNK2 (27) vs lines expressing it (23) | 2.86× lower at baseline in the lines without KCNK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; co-absent with the target |
| [[SLC14A1]] | C | SLC14A1 activity raises PAK3's level | lines that do not express SLC14A1 (37) vs lines expressing it (13) | 3.92× lower at baseline in the lines without SLC14A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: APOD, ZNF208, GRIN2A; maybe low, not absent; co-absent with the target |
| [[SLITRK4]] | C | SLITRK4 activity raises PAK3's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 3.82× lower at baseline in the lines without SLITRK4 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises PAK3's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.80× lower at baseline in the lines without CTNND2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[COL22A1]] | C | COL22A1 activity raises PAK3's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 3.48× lower at baseline in the lines without COL22A1 | 0.029 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[LINC02742]] | C | LINC02742 activity raises PAK3's level | lines that do not express LINC02742 (34) vs lines expressing it (16) | 3.48× lower at baseline in the lines without LINC02742 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000255029, ENSG00000254526, ENSG00000255227; co-absent with the target |
| [[CDH11]] | C | CDH11 activity raises PAK3's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 3.31× lower at baseline in the lines without CDH11 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[IGFBP5]] | C | IGFBP5 activity raises PAK3's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 2.39× lower at baseline in the lines without IGFBP5 | 0.055 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC14A1]] | C | PAK3 activity raises SLC14A1's level | lines that do not express PAK3 (32) vs lines expressing it (18) | 2.70× lower at baseline in the lines without PAK3 | 0.005 | ⚠ within organs, on part of the lines; also absent: CRLF2, SLC14A1, ENTHD1; co-absent with the target |
| [[COL22A1]] | C | PAK3 activity raises COL22A1's level | lines that do not express PAK3 (32) vs lines expressing it (18) | 3.90× lower at baseline in the lines without PAK3 | 0.020 | ⚠ within organs, on part of the lines; also absent: CRLF2, SLC14A1, ENTHD1; co-absent with the target |
| [[SRPX2]] | C | PAK3 activity raises SRPX2's level | lines that do not express PAK3 (32) vs lines expressing it (18) | 3.45× lower at baseline in the lines without PAK3 | 0.033 | ⚠ within organs, on part of the lines; also absent: CRLF2, SLC14A1, ENTHD1; co-absent with the target |
| [[SYTL5]] | C | PAK3 activity raises SYTL5's level | lines that do not express PAK3 (32) vs lines expressing it (18) | 1.80× lower at baseline in the lines without PAK3 | 0.039 | ⚠ within organs, on part of the lines; also absent: CRLF2, SLC14A1, ENTHD1; co-absent with the target |
| [[LINC01967]] | C | PAK3 activity raises LINC01967's level | lines that do not express PAK3 (32) vs lines expressing it (18) | 2.30× lower at baseline in the lines without PAK3 | 0.052 | ⚠ within organs, on part of the lines; also absent: CRLF2, SLC14A1, ENTHD1; co-absent with the target |
| [[LINC02742]] | C | PAK3 activity raises LINC02742's level | lines that do not express PAK3 (32) vs lines expressing it (18) | 2.88× lower at baseline in the lines without PAK3 | 0.069 | ⚠ within organs, on part of the lines; also absent: CRLF2, SLC14A1, ENTHD1; co-absent with the target |
| [[SHC4]] | C | PAK3 activity raises SHC4's level | lines that do not express PAK3 (32) vs lines expressing it (18) | 2.71× lower at baseline in the lines without PAK3 | 0.071 | ⚠ within organs, on part of the lines; also absent: CRLF2, SLC14A1, ENTHD1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.3, 34.1); signed map (40.9, 45.1). **Vector** length 64.6, 23.9% of its response variance represented; |z| ≥ 3 in 457 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | -0.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +1.6 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +3.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -4.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | p21 (RAC1) activated kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:110,944,285-111,227,361 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hPAK3, bPAK; previously MRX30, MRX47 |
| Gene groups (HGNC) | p21 (RAC1) activated kinase family |
| Hallmark sets | PANCREAS_BETA_CELLS |
| Reactome | 32 pathways, smallest: CD28 dependent Vav1 pathway; Activation of RAC1; Generation of second messenger molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [O75914](https://www.uniprot.org/uniprotkb/O75914) (Serine/threonine-protein kinase PAK 3):

> Serine/threonine protein kinase that plays a role in a variety of different signaling pathways including cytoskeleton regulation, cell migration, or cell cycle regulation. Plays a role in dendrite spine morphogenesis as well as synapse formation and plasticity. Acts as a downstream effector of the small GTPases CDC42 and RAC1. Activation by the binding of active CDC42 and RAC1 results in a conformational change and a subsequent autophosphorylation on several serine and/or threonine residues. …

**Summary**, from NCBI Gene [5063](https://www.ncbi.nlm.nih.gov/gene/5063):

> The protein encoded by this gene is a serine-threonine kinase and forms an activated complex with GTP-bound RAS-like (P21), CDC2 and RAC1. This protein may be necessary for dendritic development and for the rapid cytoskeletal reorganization in dendritic spines associated with synaptic plasticity. Defects in this gene are the cause of a non-syndromic form of X-linked intellectual disability. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by …

**Accessions** — [HGNC:8592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8592) · Entrez [5063](https://www.ncbi.nlm.nih.gov/gene/5063) · UniProt [O75914](https://www.uniprot.org/uniprotkb/O75914) · Ensembl [ENSG00000077264](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077264)

## Data

Gene col 1182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1182); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1182]; `tensor/DDL_lfc|DDL_z.npy` [1182]; `embed/gene_vectors.npy` [1182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1182 or target_col == 1182). Every well: [[PAK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

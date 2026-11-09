---
symbol: "ARL10"
type: "gene"
col: 10607
ensembl_id: "ENSG00000175414"
name: "ARF like GTPase 10"
location: "5q35.2"
module: 13
arm: "+"
pooled_cpm: 9.48
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ARL10

*ARF like GTPase 10* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.99× (z +11.6, q 4e-28, up in 12 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.32× (z +6.6, q 6e-09, up in 18 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.513× (z -10.8, q 2e-24, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KC6]] (+0.63, fdr 7e-06), [[ZNF521]] (+0.60, fdr 7e-06), [[MDGA2]] (+0.60, fdr 1e-05); moves opposite to [[NT5C2]] (-0.48, fdr 5e-05), [[IL22RA1]] (-0.47, fdr 4e-05), [[SLC11A2]] (-0.47, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[HAS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10607.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +11.6 | 4e-28 | 12/29 (A498, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +7.4 | 5e-11 | 6/20 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.6 | 6e-09 | 18/42 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +6.5 | 1e-08 | 3/17 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +5.0 | 6e-05 | 11/36 (CHP-212, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +4.4 | 1e-03 | 11/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.21× | +3.2 | 0.11 | 9/46 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +3.0 | 0.16 | 10/33 (NCI-H2347, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.21× | +3.0 | 0.16 | 5/46 (C-33 A, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10607.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.513×** | -10.8 | 2e-24 | 26/45 (NCI-H23, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.638×** | -10.7 | 3e-24 | 22/42 (LOX-IMVI, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.615×** | -8.2 | 6e-14 | 21/39 (SK-MEL-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.617×** | -8.1 | 6e-14 | 19/47 (NCI-H1792, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.707×** | -5.8 | 6e-07 | 17/48 (NCI-H23, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.816×** | -4.8 | 1e-04 | 15/48 (Hs 766T, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.754×** | -4.7 | 2e-04 | 16/48 (Hs 766T, NCI-H23, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.777×** | -4.3 | 0.002 | 11/41 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.643×** | -3.9 | 0.006 | 8/47 (SK-MEL-2, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.6 | 0.016 | 3/48 (SNU-423, SW 1271, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.664×** | -3.6 | 0.016 | 6/39 (C32, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.812×** | -3.4 | 0.033 | 16/39 (C32, NCI-H23, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.812×** | -3.4 | 0.033 | 5/46 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.836× | -3.0 | 0.11 | 4/46 (SW 900, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 24.8 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0420× (z -19.5) |
| [[NCI-H1792 (line)]] | alt | 31.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.1) |
| [[C32 (line)]] | wt | 23.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -15.3) |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -20.1) |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0977× (z -13.1) |
| [[CHP-212 (line)]] | wt | 46.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -13.6) |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 22.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0907× (z -20.8) |
| [[NCI-H2347 (line)]] | alt | 14.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.5) |
| [[SW480 (line)]] | alt | 11.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -14.9) |
| [[A-427 (line)]] | wt | 3.70 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0760× (z -9.2) |
| [[C-33 A (line)]] | alt | 48.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -17.5) |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.7) |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -12.7) |
| [[J82 (line)]] | alt | 4.56 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.101× (z -8.6) |
| [[PANC-1 (line)]] | alt | 6.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -10.9) |
| [[A-172 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KC6]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ZNF521]] | +0.60 | +0.58 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[MDGA2]] | +0.60 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CSPG4]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[LINC02226]] | +0.57 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[AEBP1]] | +0.57 | +0.54 / +0.47 | both halves | 2e-05 | same gene group |
| [[SETBP1]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TMEM45A]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[RHOJ]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[MAGI2]] | +0.53 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[CTHRC1]] | +0.52 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[NAV1]] | +0.51 | +0.46 / +0.59 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NT5C2]] | -0.48 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[IL22RA1]] | -0.47 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[SLC11A2]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[TMEM125]] | -0.45 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[CHN2]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[POF1B]] | -0.43 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[GDA]] | -0.42 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[EXPH5]] | -0.42 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[MYO5C]] | -0.42 | -0.41 / -0.29 | both halves | 2e-04 | same gene group |
| [[RPH3AL]] | -0.42 | -0.41 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HAS2]] | B | HAS2 activity raises ARL10's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 2.08× lower at baseline in the lines without HAS2 | 0.018 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[CSPG4]] | B | CSPG4 activity raises ARL10's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.52× lower at baseline in the lines without CSPG4 | 0.042 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1 |
| [[SPOCD1]] | B | SPOCD1 activity raises ARL10's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 1.54× lower at baseline in the lines without SPOCD1 | 0.056 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[AIM2]] | B | AIM2 activity raises ARL10's level | lines that do not express AIM2 (26) vs lines expressing it (24) | 2.20× lower at baseline in the lines without AIM2 | 0.076 | ⚠ within organs, on part of the lines; also absent: PEX5L, PHACTR1, ARMCX2 |
| [[SPOCD1]] | B | SPOCD1 activity strengthens ARL10's drug response | lines that do not express SPOCD1 (25) vs lines expressing it (23) | the lines without SPOCD1 respond 0.75× as strongly (z diff +0.39); strongest at Homoharringtonine 5 µM: 0.74x vs 0.31x (z diff +3.9) | 0.076 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1; target measured in part of the lines; both ways; artifact flags |
| [[AEBP1]] | B | AEBP1 activity raises ARL10's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 2.90× lower at baseline in the lines without AEBP1 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[MME]] | B | MME activity raises ARL10's level | lines that do not express MME (30) vs lines expressing it (20) | 1.75× lower at baseline in the lines without MME | 0.087 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[ANKRD7]] | B | ANKRD7 activity raises ARL10's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 2.17× lower at baseline in the lines without ANKRD7 | 0.088 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.0, 26.3); signed map (30.4, 42.8). **Vector** length 64.7, 9.39% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.9 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +11.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +5.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | -0.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.1 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.2 | -8.2 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.2 | -0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.0 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:176,365,487-176,401,865 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARL10A |
| Gene groups (HGNC) | ARF GTPase family; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q8N8L6](https://www.uniprot.org/uniprotkb/Q8N8L6) carries no function annotation.

**Summary**, from NCBI Gene [285598](https://www.ncbi.nlm.nih.gov/gene/285598):

> Predicted to enable GTP binding activity; GTPase activity; and metal ion binding activity. Located in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22042) · Entrez [285598](https://www.ncbi.nlm.nih.gov/gene/285598) · UniProt [Q8N8L6](https://www.uniprot.org/uniprotkb/Q8N8L6) · Ensembl [ENSG00000175414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175414)

## Data

Gene col 10607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10607); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10607]; `tensor/DDL_lfc|DDL_z.npy` [10607]; `embed/gene_vectors.npy` [10607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10607 or target_col == 10607). Every well: [[ARL10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

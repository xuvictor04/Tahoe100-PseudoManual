---
symbol: "CEACAM22P-1"
type: "gene"
col: 16494
ensembl_id: "ENSG00000290603"
name: ""
location: ""
module: 191
arm: "+"
pooled_cpm: 4.49
n_lines_expressing: 43
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 22
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# CEACAM22P-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 11.4× (z +23.9, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.456× (z -7.7, q 7e-12, down in 22 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL26A1]] (+0.70, fdr 7e-06), [[HULC]] (+0.69, fdr 7e-06), [[TMPRSS9]] (+0.68, fdr 7e-06); moves opposite to [[ABCB10]] (-0.48, fdr 4e-05), [[ASH2L]] (-0.48, fdr 5e-05), [[ARMC10]] (-0.46, fdr 4e-05).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[VAV1]] → it (grade B ⚠); 3 go from it, the strongest it → [[CEACAM16-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **11.4×** | +23.9 | 0e+00 | 37/38 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **9.80×** | +22.4 | 0e+00 | 33/36 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.33×** | +20.4 | 0e+00 | 22/30 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.82×** | +18.7 | 0e+00 | 36/38 (HT-29, KATO III, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.73×** | +18.3 | 0e+00 | 26/29 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.80×** | +15.4 | 0e+00 | 24/33 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **4.29×** | +14.3 | 1e-44 | 30/36 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.65×** | +12.7 | 3e-35 | 31/34 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.11×** | +11.2 | 3e-27 | 29/37 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.16×** | +10.9 | 8e-26 | 22/35 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.95×** | +10.6 | 1e-24 | 13/28 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +10.4 | 1e-23 | 8/15 (RPMI-7951, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +9.9 | 1e-21 | 4/11 (HOP62, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +9.4 | 2e-19 | 3/8 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.82×** | +5.3 | 4e-06 | 15/33 (A498, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.74×** | +5.2 | 6e-06 | 12/31 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.39×** | +4.5 | 2e-04 | 7/37 (HEC-1-A, CFPAC-1, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.3 | 6e-04 | 8/27 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16494.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.456×** | -7.7 | 7e-12 | 22/36 (KATO III, A549, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.494×** | -6.9 | 1e-09 | 24/39 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.556×** | -5.8 | 2e-06 | 19/35 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -5.5 | 5e-06 | 18/26 (NCI-H2030, A549, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.612×** | -4.8 | 2e-04 | 14/38 (A498, J82, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.511×** | -3.4 | 0.054 | 12/27 (KATO III, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.694×** | -3.3 | 0.075 | 6/36 (BT-474, A549, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | 0.723× | -3.1 | 0.15 | 5/37 (RKO, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 16.7 | 5 | 8 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 13.0× (z +14.4) | [[Ixazomib citrate (drug)]] 0.5 µM 0.103× (z -12.8) |
| [[A498 (line)]] | wt | 22.6 | 2 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.72× (z +10.6) | [[Bortezomib (drug)]] 0.05 µM 0.177× (z -9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.184× (z -9.2) |
| [[HT-29 (line)]] | alt | 6.29 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 19.7× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 2.45 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 51.4× (z +9.9) | — |
| [[SW480 (line)]] | alt | 1.72 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 123× (z +14.9) | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0667× (z -12.9) |
| [[PANC-1 (line)]] | alt | 2.97 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 26.4× (z +13.3) | — |
| [[A549 (line)]] | wt | 10.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 14.0× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 2.49 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 161× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 7.47 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.39× (z +14.1) | — |
| [[NCI-H2030 (line)]] | alt | 6.83 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.28× (z +11.9) | [[Digitoxin (drug)]] 5 µM 0.0835× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 2.31 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 415× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 2.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +12.4) | — |
| [[LoVo (line)]] | wt | 2.05 | 1 | 0 | [[Auranofin (drug)]] 5 µM 17.9× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.30 | 1 | 0 | [[Auranofin (drug)]] 5 µM 15.3× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 7.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 4.75 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 17.4× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 1.72 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 29.5× (z +8.5) | — |
| [[A-172 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.742 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.933 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.993 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL26A1]] | +0.70 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[HULC]] | +0.69 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[TMPRSS9]] | +0.68 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[LINC00243]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[LINC00624]] | +0.61 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[HBG2]] | +0.61 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[KCNN3]] | +0.60 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[LINC01422]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TCN2]] | +0.60 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ZC3H12A-DT]] | +0.59 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[DNAH3]] | +0.58 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[IL3RA]] | +0.58 | +0.57 / +0.63 | both halves | 9e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB10]] | -0.48 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[ASH2L]] | -0.48 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[ARMC10]] | -0.46 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[MCM9]] | -0.46 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[CMTM4]] | -0.45 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[MTERF3]] | -0.45 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[GLMN]] | -0.45 | -0.46 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAV1]] | B | VAV1 activity raises CEACAM22P-1's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.58× lower at baseline in the lines without VAV1 | 0.061 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[TNFSF14]] | B | TNFSF14 activity raises CEACAM22P-1's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.40× lower at baseline in the lines without TNFSF14 | 0.062 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers CEACAM22P-1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEACAM16-AS1]] | B | CEACAM22P-1 activity raises CEACAM16-AS1's level | lines that do not express CEACAM22P-1 (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without CEACAM22P-1 | 0.085 | ⚠ within organs, on part of the lines; also absent: PPM1L, ENSG00000287400; maybe low, not absent |
| [[LINC00243]] | B | CEACAM22P-1 activity strengthens LINC00243's drug response | lines that do not express CEACAM22P-1 (7) vs lines expressing it (31) | the lines without CEACAM22P-1 respond 0.54× as strongly (z diff +1.54); strongest at Tucidinostat 0.5 µM: 2.79x vs 4.15x (z diff +2.8) | 0.085 | ⚠ within organs, on part of the lines; also absent: PPM1L, ENSG00000287400; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LINC02175]] | B | CEACAM22P-1 activity raises LINC02175's level | lines that do not express CEACAM22P-1 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without CEACAM22P-1 | 0.086 | ⚠ within organs, on part of the lines; also absent: PPM1L, ENSG00000287400; maybe low, not absent |

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.764). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.6, 34.2); signed map (26.3, 16.3). **Vector** length 69.4, 12.8% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +18.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +9.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +12.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +15.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +5.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +1.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -7.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -1.9 | -1.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -2.4 |

## What is on record

> [!warning] No registry record
> CEACAM22P-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16494); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16494]; `tensor/DDL_lfc|DDL_z.npy` [16494]; `embed/gene_vectors.npy` [16494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16494 or target_col == 16494). Every well: [[CEACAM22P-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEACAM22P-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

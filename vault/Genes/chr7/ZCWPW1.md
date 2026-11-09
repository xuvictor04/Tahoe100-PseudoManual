---
symbol: "ZCWPW1"
type: "gene"
col: 1224
ensembl_id: "ENSG00000078487"
name: "zinc finger CW-type and PWWP domain containing 1"
location: "7q22.1"
module: 35
arm: "+"
pooled_cpm: 8.39
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 21
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ZCWPW1

*zinc finger CW-type and PWWP domain containing 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.11× (z +12.1, q 4e-31, up in 37 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.324× (z -12.9, q 2e-35, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP3CB-AS1]] (+0.82, fdr 7e-06), [[PPP1R12A-AS2]] (+0.80, fdr 4e-05), [[ATE1OSP]] (+0.79, fdr 1e-05); moves opposite to [[YIF1B]] (-0.67, fdr 0.001, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[THNSL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +12.1 | 4e-31 | 37/43 (HOP62, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.24×** | +9.3 | 5e-18 | 26/30 (NCI-H2347, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +9.1 | 2e-17 | 19/21 (NCI-H2347, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +8.5 | 2e-15 | 11/14 (HT-29, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.015 | 9/41 (A-427, hTERT-HPNE, …) | two highest doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.6 | 0.029 | 3/47 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.32× | +3.2 | 0.12 | 4/47 (SW1417, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.33× | +3.0 | 0.18 | 9/41 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1224.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.324×** | -12.9 | 2e-35 | 36/46 (Panc 03.27, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.367×** | -11.5 | 5e-28 | 36/46 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.375×** | -11.2 | 6e-27 | 33/45 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.379×** | -11.1 | 2e-26 | 36/46 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.453×** | -9.1 | 1e-17 | 26/46 (A-427, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.455×** | -9.0 | 2e-17 | 31/45 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -8.4 | 5e-15 | 28/42 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.577×** | -6.3 | 2e-08 | 27/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.592×** | -6.0 | 1e-07 | 24/41 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.694×** | -5.9 | 2e-07 | 22/47 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.455×** | -4.7 | 1e-04 | 16/43 (A-427, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.456×** | -4.7 | 1e-04 | 16/45 (NCI-H1573, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.683×** | -4.4 | 6e-04 | 17/47 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -4.2 | 0.001 | 18/42 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.734×** | -3.5 | 0.015 | 10/44 (hTERT-HPNE, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.675×** | -3.2 | 0.042 | 5/47 (MIA PaCa-2, PANC-1, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0163× (z -22.8) |
| [[PANC-1 (line)]] | alt | 17.5 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.164× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0969× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -9.3) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0887× (z -13.3) |
| [[SW480 (line)]] | alt | 8.78 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.211× (z -9.5) |
| [[A-172 (line)]] | wt | 6.81 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0960× (z -9.6) |
| [[A549 (line)]] | wt | 6.21 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0618× (z -10.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 7.80 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.5 µM 0.0755× (z -9.7) |
| [[HCT15 (line)]] | alt | 7.29 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM 0.0524× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 6.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0938× (z -11.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 6.27 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0896× (z -8.9) |
| [[KATO III (line)]] | alt | 9.06 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.148× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 1 | — | [[Abemaciclib (drug)]] 5 µM 0.0263× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 7.48 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.115× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 4.50 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0359× (z -11.9) |
| [[A498 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 7 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CB-AS1]] | +0.82 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[PPP1R12A-AS2]] | +0.80 | +0.77 / +0.42 | both halves | 4e-05 |  |
| [[ATE1OSP]] | +0.79 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | +0.79 | +0.77 / +0.42 | both halves | 4e-05 |  |
| [[TMEM202-AS1]] | +0.78 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[CCT6B]] | +0.77 | +0.77 / +0.50 | both halves | 1e-05 |  |
| [[PJVK]] | +0.77 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[SUMO2P17]] | +0.76 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[NQO1-DT]] | +0.76 | +0.75 / +0.44 | both halves | 3e-05 |  |
| [[SEPTIN7-DT]] | +0.76 | +0.73 / +0.43 | both halves | 4e-05 |  |
| [[MZF1-AS1]] | +0.76 | +0.75 / +0.41 | both halves | 4e-05 |  |
| [[SMIM15-AS1]] | +0.75 | +0.78 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIF1B]] | -0.67 | -0.64 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THNSL2]] | B | THNSL2 activity raises ZCWPW1's level | lines that do not express THNSL2 (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without THNSL2 | 0.020 | ⚠ within organs, on part of the lines; also absent: CRABP2, NPTX2, SULT4A1 |
| [[AGA-DT]] | B | AGA-DT activity raises ZCWPW1's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 1.66× lower at baseline in the lines without AGA-DT | 0.054 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[FAM66C]] | B | FAM66C activity raises ZCWPW1's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.40× lower at baseline in the lines without FAM66C | 0.067 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[ZNF577]] | B | ZNF577 activity raises ZCWPW1's level | lines that do not express ZNF577 (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without ZNF577 | 0.088 | ⚠ within organs, on part of the lines; also absent: ZNF649, ZNF724, ENSG00000283201 |
| [[TMEM9B-AS1]] | B | TMEM9B-AS1 activity raises ZCWPW1's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.55× lower at baseline in the lines without TMEM9B-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[CDKL3]] | C | CDKL3's natural level strengthens ZCWPW1's drug response | CDKL3's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.70, reverse -0.14; direction not clear | 0.016 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.797). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.5, 13.5); signed map (25.2, -6.4). **Vector** length 81.6, 15.6% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +3.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.3 | -12.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -11.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.7 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.0 | -9.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CW-type and PWWP domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,400,826-100,428,992 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10057, DKFZp434N0510, ZCW1 |
| Gene groups (HGNC) | Zinc fingers CW-type; PWWP domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0M4](https://www.uniprot.org/uniprotkb/Q9H0M4) (Zinc finger CW-type PWWP domain protein 1):

> Dual histone methylation reader specific for PRDM9-catalyzed histone marks (H3K4me3 and H3K36me3). Facilitates the repair of PRDM9-induced meiotic double-strand breaks (DSBs) (By similarity). Essential for male fertility and spermatogenesis (By similarity). Required for meiosis prophase I progression in male but not in female germ cells (By similarity).

**Summary**, from NCBI Gene [55063](https://www.ncbi.nlm.nih.gov/gene/55063):

> Enables histone H3K4me3 reader activity. Involved in epigenetic regulation of gene expression. Located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23486](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23486) · Entrez [55063](https://www.ncbi.nlm.nih.gov/gene/55063) · UniProt [Q9H0M4](https://www.uniprot.org/uniprotkb/Q9H0M4) · Ensembl [ENSG00000078487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078487)

## Data

Gene col 1224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1224); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1224]; `tensor/DDL_lfc|DDL_z.npy` [1224]; `embed/gene_vectors.npy` [1224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1224 or target_col == 1224). Every well: [[ZCWPW1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCWPW1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

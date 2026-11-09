---
symbol: "SARNP"
type: "gene"
col: 12967
ensembl_id: "ENSG00000205323"
name: "SAP domain containing ribonucleoprotein"
location: "12q13.2"
module: 220
arm: "+"
pooled_cpm: 124.88
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/220"]
generated_by: "tahoemap"
---

# SARNP

*SAP domain containing ribonucleoprotein* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.25× (z +12.8, q 1e-34, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.702× (z -7.3, q 2e-10, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CWC15]] (+0.68, fdr 1e-05), [[CDADC1]] (+0.66, fdr 7e-06), [[MARCHF5]] (+0.64, fdr 7e-06); moves opposite to [[RSC1A1]] (-0.59, fdr 1e-05), [[TNFRSF12A]] (-0.58, fdr 1e-05), [[ZNF770]] (-0.55, fdr 1e-05).
> It is in [[Module 220]], a single-armed module (Respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCND1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12967.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.25×** | +12.8 | 1e-34 | 47/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +11.4 | 2e-27 | 41/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +9.6 | 2e-19 | 43/48 (SW480, LoVo, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +9.2 | 8e-18 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +7.3 | 4e-11 | 38/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +5.6 | 2e-06 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.4 | 6e-06 | 35/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 2e-04 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.6 | 3e-04 | 26/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.7 | 0.014 | 7/49 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.18× | +3.5 | 0.028 | 20/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 1.12× | +3.3 | 0.043 | 20/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.055 | 19/49 (PANC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.066 | 13/48 (Hs 766T, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12967.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.702×** | -7.3 | 2e-10 | 43/48 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.728×** | -6.6 | 2e-08 | 36/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.763×** | -5.6 | 4e-06 | 30/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.831×** | -5.4 | 1e-05 | 25/49 (H4, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.855× | -4.6 | 6e-04 | 17/48 (SW480, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.805×** | -4.5 | 7e-04 | 26/48 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.830×** | -3.8 | 0.010 | 21/48 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.838× | -3.7 | 0.018 | 16/48 (C32, AsPC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.849× | -3.4 | 0.046 | 20/48 (HOP62, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | 0.849× | -3.2 | 0.065 | 20/44 (HepG2/C3A, NCI-H2347, …) | top dose only | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | 0.856× | -3.2 | 0.072 | 14/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.860× | -3.1 | 0.092 | 14/48 (KATO III, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 124 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +16.2) | — |
| [[PANC-1 (line)]] | alt | 120 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +16.2) | — |
| [[SW480 (line)]] | alt | 167 | 6 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.12× (z +16.1) | — |
| [[LoVo (line)]] | wt | 126 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.62× (z +18.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +13.3) | — |
| [[AsPC-1 (line)]] | alt | 161 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.07× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[LS 180 (line)]] | wt | 115 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +11.5) | — |
| [[KATO III (line)]] | alt | 89.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +12.6) | — |
| [[NCI-H2347 (line)]] | alt | 171 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.432× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[COLO 205 (line)]] | alt | 110 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.30× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 123 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.64× (z +8.9) | [[Auranofin (drug)]] 5 µM 0.520× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 123 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[NCI-H1573 (line)]] | alt | 128 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.42× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 150 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.36× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 170 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.02× (z +10.3) | — |
| [[SK-MEL-2 (line)]] | alt | 87.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.02× (z +8.5) | — |
| [[A-172 (line)]] | wt | 112 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -27.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -8.5) ⚠ cell-cycle shift, explains ~17% of this change |
| [[H4 (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -9.1) ⚠ cell-cycle shift, explains ~17% of this change |
| [[HT-29 (line)]] | alt | 100 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.18× (z +8.9) | — |
| [[J82 (line)]] | alt | 129 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 147 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.98× (z +9.9) | — |
| [[RKO (line)]] | wt | 115 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.64× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 103 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.91× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 120 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.482× (z -8.7) |
| [[SW1417 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.450× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[SW48 (line)]] | wt | 122 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.16× (z +9.2) | — |
| [[A498 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 139 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 126 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 98.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 108 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 144 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWC15]] | +0.68 | +0.72 / +0.54 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 469 |
| [[CDADC1]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MARCHF5]] | +0.64 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[SNX1]] | +0.64 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SNX4]] | +0.64 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ZNF358]] | +0.63 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ALG9]] | +0.60 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TENT2]] | +0.59 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[MBD2]] | +0.59 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[PRMT9]] | +0.58 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[MED17]] | +0.58 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[NDUFS4]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSC1A1]] | -0.59 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | -0.58 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[ZNF770]] | -0.55 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[ZBTB33]] | -0.52 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[CCND1]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[BBS10]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[BZW1]] | -0.51 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[ENC1]] | -0.51 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SLC30A1]] | -0.51 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[PHLDA1]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[AGO2]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ELK4]] | -0.49 | -0.65 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCND1]] | B | CCND1 activity raises SARNP's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 1.14× lower at baseline in the lines without CCND1 | 0.037 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 220]] — Respiratory electron transport; 11 genes; every member is in the + arm (projection on the module's main direction 0.602). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-3.6, -12.7); signed map (-32.8, -10.0). **Vector** length 97.6, 29.6% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.1 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.9 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | +3.6 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.2 | +2.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +12.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.1 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.5 | -1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.3 | -7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.8 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | +11.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -1.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SAP domain containing ribonucleoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,752,463-55,817,724 (-) |
| Ensembl biotype | protein_coding |
| Also known as | THO1, Hcc-1, CIP29 |
| Gene groups (HGNC) | Transcription and export complex 1 subunits |
| Reactome | 5 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [P82979](https://www.uniprot.org/uniprotkb/P82979) (SAP domain-containing ribonucleoprotein):

> Binds both single-stranded and double-stranded DNA with higher affinity for the single-stranded form. Specifically binds to scaffold/matrix attachment region DNA. Also binds single-stranded RNA. Enhances RNA unwinding activity of DDX39A. May participate in important transcriptional or translational control of cell growth, metabolism and carcinogenesis. Component of the TREX complex which is thought to couple mRNA transcription, processing and nuclear export, and specifically associates with …

**Summary**, from NCBI Gene [84324](https://www.ncbi.nlm.nih.gov/gene/84324):

> This gene encodes a protein that is upregulated in response to various cytokines. The encoded protein may play a role in cell cycle progression. A translocation between this gene and the myeloid/lymphoid leukemia gene, resulting in expression of a chimeric protein, has been associated with acute myelomonocytic leukemia. Pseudogenes exist on chromosomes 7 and 8. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:24432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24432) · Entrez [84324](https://www.ncbi.nlm.nih.gov/gene/84324) · UniProt [P82979](https://www.uniprot.org/uniprotkb/P82979) · Ensembl [ENSG00000205323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205323)

## Data

Gene col 12967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12967); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12967]; `tensor/DDL_lfc|DDL_z.npy` [12967]; `embed/gene_vectors.npy` [12967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12967 or target_col == 12967). Every well: [[SARNP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SARNP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

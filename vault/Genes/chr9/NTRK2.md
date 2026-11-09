---
symbol: "NTRK2"
type: "gene"
col: 7238
ensembl_id: "ENSG00000148053"
name: "neurotrophic receptor tyrosine kinase 2"
location: "9q21.33"
module: 87
arm: "+"
pooled_cpm: 7.36
n_lines_expressing: 22
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# NTRK2

*neurotrophic receptor tyrosine kinase 2* — 9q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.97× (z +24.7, q 0e+00, up in 10 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Hydroxyurea (drug)]] 5 µM: 0.686× (z -4.0, q 0.025, down in 1 of 19 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VSNL1]] (+0.58, fdr 3e-05), [[LEF1-AS1]] (+0.56, fdr 3e-05), [[NYAP2]] (+0.53, fdr 2e-05); moves opposite to [[CLMP]] (-0.47, fdr 1e-04), [[CAPRIN2]] (-0.41, fdr 2e-04), [[ZNF699]] (-0.41, fdr 3e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[LEF1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.97×** | +24.7 | 0e+00 | 10/16 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.07×** | +17.7 | 0e+00 | 10/11 (AsPC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.72×** | +15.4 | 0e+00 | 17/19 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.28×** | +12.5 | 2e-33 | 3/5 (SW480, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +12.0 | 3e-31 | 5/8 (Hs 766T, SW480, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.29×** | +9.0 | 1e-17 | 15/18 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +6.1 | 8e-08 | 4/19 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.8 | 1e-04 | 2/15 (HS-578T, SW 900) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.7 | 2e-04 | 2/16 (HCT15, C-33 A) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +4.3 | 0.001 | 9/19 (NCI-H23, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.71×** | +4.2 | 0.002 | 2/8 (AsPC-1, LS 180) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.1 | 0.002 | 1/6 (SW1417) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.9 | 0.004 | 1/11 (AsPC-1) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.019 | 4/19 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.5 | 0.019 | 0/13 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.019 | 1/19 (PANC-1) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.019 | 5/19 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.027 | 4/18 (NCI-H23, SW480, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +3.3 | 0.031 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.046 | 6/19 (SW480, SW 900, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.058 | 1/19 (PANC-1) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.059 | 1/15 (SW480) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7238.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hydroxyurea (drug)]] 5 µM |  | **0.686×** | -4.0 | 0.025 | 1/19 (SK-MEL-2) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.703×** | -3.9 | 0.025 | 10/19 (SW480, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.706×** | -3.8 | 0.025 | 11/19 (SW480, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.727×** | -3.5 | 0.066 | 3/19 (HCT15, NCI-H1573, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.05 µM |  | 0.744× | -3.1 | 0.21 | 0/18 | inconsistent across doses |  |
| [[Isocorydine (drug)]] 5 µM |  | 0.821× | -3.1 | 0.21 | 0/19 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.8 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.5) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -11.7) |
| [[C32 (line)]] | wt | 24.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -10.7) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.104× (z -9.6) |
| [[SW1417 (line)]] | alt | 119 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 21.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.6) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.242× (z -8.6) |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.992 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.976 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VSNL1]] | +0.58 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[LEF1-AS1]] | +0.56 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[NYAP2]] | +0.53 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[PTPRZ1]] | +0.53 | +0.64 / +0.40 | both halves | 4e-05 | STRING 574 |
| [[LOXL4]] | +0.53 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[FKBP9P1-1]] | +0.52 | +0.49 / +0.34 | both halves | 1e-04 |  |
| [[PLEKHS1]] | +0.52 | +0.38 / +0.36 | both halves | 9e-05 |  |
| [[ABCG2]] | +0.52 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[KSR2]] | +0.51 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[SLC44A3-AS1]] | +0.51 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[CD200]] | +0.51 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[SLC44A3]] | +0.51 | +0.50 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLMP]] | -0.47 | -0.47 / -0.36 | both halves | 1e-04 | same gene group |
| [[CAPRIN2]] | -0.41 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[ZNF699]] | -0.41 | -0.35 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NTRK2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF704]] | B | ZNF704 activity raises NTRK2's level | lines that do not express ZNF704 (17) vs lines expressing it (33) | 1.72× lower at baseline in the lines without ZNF704 | 0.075 | ⚠ within organs, on part of the lines |
| [[PTPRZ1]] | C | PTPRZ1 activity raises NTRK2's level | lines that do not express PTPRZ1 (40) vs lines expressing it (10) | 3.10× lower at baseline in the lines without PTPRZ1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, KRT5, ENSG00000242029; co-absent with the target |
| [[CPVL]] | C | CPVL activity raises NTRK2's level | lines that do not express CPVL (21) vs lines expressing it (29) | 1.90× lower at baseline in the lines without CPVL | 0.098 | ⚠ within organs, on part of the lines; also absent: CHN2, PTPRR, BBOX1-AS1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LEF1-AS1]] | B | NTRK2 activity raises LEF1-AS1's level | lines that do not express NTRK2 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without NTRK2 | 0.053 | ⚠ within organs, on part of the lines; also absent: ANKRD20A9P, ONECUT3, LINC00408; maybe low, not absent |
| [[AMOT]] | B | NTRK2 activity raises AMOT's level | lines that do not express NTRK2 (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without NTRK2 | 0.061 | ⚠ within organs, on part of the lines; also absent: ANKRD20A9P, ONECUT3, LINC00408; maybe low, not absent |
| [[COL9A3]] | C | NTRK2 activity raises COL9A3's level | lines that do not express NTRK2 (28) vs lines expressing it (22) | 2.27× lower at baseline in the lines without NTRK2 | 0.016 | ⚠ within organs, on part of the lines; also absent: ANKRD20A9P, ONECUT3, LINC00408; maybe low, not absent; co-absent with the target |
| [[CPVL]] | C | NTRK2 activity raises CPVL's level | lines that do not express NTRK2 (28) vs lines expressing it (22) | 1.66× lower at baseline in the lines without NTRK2 | 0.052 | ⚠ within organs, on part of the lines; also absent: ANKRD20A9P, ONECUT3, LINC00408; maybe low, not absent; co-absent with the target |
| [[LEF1]] | C | NTRK2 activity raises LEF1's level | lines that do not express NTRK2 (28) vs lines expressing it (22) | 2.27× lower at baseline in the lines without NTRK2 | 0.054 | ⚠ within organs, on part of the lines; also absent: ANKRD20A9P, ONECUT3, LINC00408; maybe low, not absent; co-absent with the target |
| [[EYA1]] | C | NTRK2 activity raises EYA1's level | lines that do not express NTRK2 (28) vs lines expressing it (22) | 1.63× lower at baseline in the lines without NTRK2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ANKRD20A9P, ONECUT3, LINC00408; maybe low, not absent; co-absent with the target |
| [[APCDD1]] | C | NTRK2 activity raises APCDD1's level | lines that do not express NTRK2 (28) vs lines expressing it (22) | 1.72× lower at baseline in the lines without NTRK2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ANKRD20A9P, ONECUT3, LINC00408; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (53.9, 29.9); signed map (28.8, 37.4). **Vector** length 46.4, 10.4% of its response variance represented; |z| ≥ 3 in 500 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +17.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +12.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +24.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +3.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | neurotrophic receptor tyrosine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.33 — chr9:84,668,375-85,095,751 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRKB |
| Gene groups (HGNC) | I-set domain containing; Neurotrophic receptor tyrosine kinase family |
| Reactome | 20 pathways, smallest: Activated NTRK2 signals through PLCG1; NGF-independant TRKA activation; Activation of TRKA receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16620](https://www.uniprot.org/uniprotkb/Q16620) (BDNF/NT-3 growth factors receptor):

> Receptor tyrosine kinase involved in the development and the maturation of the central and the peripheral nervous systems through regulation of neuron survival, proliferation, migration, differentiation, and synapse formation and plasticity (By similarity). Receptor for BDNF/brain-derived neurotrophic factor and NTF4/neurotrophin-4. Alternatively can also bind NTF3/neurotrophin-3 which is less efficient in activating the receptor but regulates neuron survival through NTRK2. Upon ligand-binding, …

**Summary**, from NCBI Gene [4915](https://www.ncbi.nlm.nih.gov/gene/4915):

> This gene encodes a member of the neurotrophic tyrosine receptor kinase (NTRK) family. This kinase is a membrane-bound receptor that, upon neurotrophin binding, phosphorylates itself and members of the MAPK pathway. Signalling through this kinase leads to cell differentiation. Mutations in this gene have been associated with obesity and mood disorders. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:8032](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8032) · Entrez [4915](https://www.ncbi.nlm.nih.gov/gene/4915) · UniProt [Q16620](https://www.uniprot.org/uniprotkb/Q16620) · Ensembl [ENSG00000148053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148053)

## Data

Gene col 7238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7238); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7238]; `tensor/DDL_lfc|DDL_z.npy` [7238]; `embed/gene_vectors.npy` [7238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7238 or target_col == 7238). Every well: [[NTRK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTRK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

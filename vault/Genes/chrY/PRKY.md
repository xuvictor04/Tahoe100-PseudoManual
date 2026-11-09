---
symbol: "PRKY"
type: "gene"
col: 1807
ensembl_id: "ENSG00000099725"
name: "protein kinase Y-linked (pseudogene)"
location: "Yp11.2"
module: 13
arm: "+"
pooled_cpm: 35.95
n_lines_expressing: 20
n_dd_up: 14
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PRKY

*protein kinase Y-linked (pseudogene)* — Yp11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.04× (z +9.9, q 2e-20, up in 1 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 1.61× (z +6.6, q 5e-09, up in 0 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.455× (z -11.0, q 3e-25, down in 15 of 18 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND2A]] (+0.55, fdr 2e-05), [[LINC01411]] (+0.51, fdr 1e-05), [[WNT5B]] (+0.51, fdr 2e-05); moves opposite to [[PRKAR2B]] (-0.43, fdr 1e-04), [[CLCN3]] (-0.41, fdr 1e-04), [[PRSS16]] (-0.41, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PRKAR2B]] → it (grade B ⚠); 4 go from it, the strongest it → [[ZNF423]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1807.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +9.9 | 2e-20 | 1/17 (C32) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +9.7 | 1e-19 | 3/17 (NCI-H460, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +8.2 | 4e-14 | 0/17 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.61×** | +6.6 | 5e-09 | 0/17 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +6.0 | 2e-07 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +5.6 | 2e-06 | 6/16 (A549, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.2 | 2e-05 | 4/18 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.1 | 2e-05 | 4/18 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 2e-05 | 0/17 | two highest doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.9 | 7e-05 | 7/17 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.008 | 0/17 | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.8 | 0.008 | 3/17 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.016 | 0/17 | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.090 | 0/17 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, none with an alert; shown: the 15 strongest. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1807.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.455×** | -11.0 | 3e-25 | 15/18 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.590×** | -10.4 | 7e-23 | 16/18 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.519×** | -9.1 | 1e-17 | 15/18 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.530×** | -8.8 | 2e-16 | 13/17 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.538×** | -8.3 | 1e-14 | 16/18 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.658×** | -5.8 | 5e-07 | 11/18 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.688×** | -4.8 | 1e-04 | 1/17 (SK-MEL-2) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.739×** | -4.2 | 0.002 | 8/17 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.750×** | -4.0 | 0.004 | 0/17 | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.750×** | -4.0 | 0.004 | 1/17 (hTERT-HPNE) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.763×** | -3.8 | 0.009 | 0/18 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.765×** | -3.7 | 0.009 | 4/17 (J82, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.693×** | -3.6 | 0.012 | 0/18 | inconsistent across doses | noisy plate (z scaled) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.778×** | -3.5 | 0.020 | 0/17 | two highest doses |  |
| [[Tucatinib (drug)]] 0.5 µM |  | **0.719×** | -3.3 | 0.040 | 0/18 | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1807. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 278 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -31.3) |
| [[hTERT-HPNE (line)]] | wt | 209 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -17.9) |
| [[J82 (line)]] | alt | 122 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -18.9) |
| [[LoVo (line)]] | wt | 64.4 | 2 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.365× (z -11.1) |
| [[H4 (line)]] | wt | 216 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -13.4) |
| [[C32 (line)]] | wt | 58.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -15.5) |
| [[A-427 (line)]] | wt | 38.4 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.3) |
| [[A549 (line)]] | wt | 62.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -21.3) |
| [[NCI-H460 (line)]] | wt | 173 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -14.8) |
| [[SK-MEL-2 (line)]] | alt | 51.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -26.3) |
| [[SNU-423 (line)]] | alt | 54.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -18.8) |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.168× (z -11.7) |
| [[SNU-1 (line)]] | wt | 101 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.351× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 43.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.7) |
| [[CHP-212 (line)]] | wt | 77.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -11.6) |
| [[A498 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.62 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1807), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND2A]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[LINC01411]] | +0.51 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[WNT5B]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[SEMA5A]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[LINC01615]] | +0.50 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CEP85L]] | +0.49 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[ADAMTS2]] | +0.48 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[IPO9-AS1]] | +0.48 | +0.22 / +0.56 | both halves | 6e-04 |  |
| [[SYNC]] | +0.48 | +0.31 / +0.45 | both halves | 2e-04 |  |
| [[TSHZ3-AS1]] | +0.47 | +0.45 / +0.37 | both halves | 8e-05 |  |
| [[FLI1]] | +0.46 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[COL5A1]] | +0.46 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAR2B]] | -0.43 | -0.36 / -0.40 | both halves | 1e-04 | STRING 854 |
| [[CLCN3]] | -0.41 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[PRSS16]] | -0.41 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[MYO5C]] | -0.40 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[VWDE]] | -0.39 | -0.24 / -0.29 | both halves | 5e-04 |  |
| [[DLG3]] | -0.39 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[GTPBP8]] | -0.39 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[KIF13B]] | -0.38 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[DMXL2]] | -0.38 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[PIK3CB]] | -0.38 | -0.29 / -0.33 | both halves | 3e-04 |  |
| [[DLEU1]] | -0.38 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[ICA1]] | -0.37 | -0.38 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKAR2B]] | B | PRKAR2B activity raises PRKY's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 3.77× lower at baseline in the lines without PRKAR2B | 0.056 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[TOP2A]] | B | TOP2A activity lowers PRKY's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[UTY]] | C | UTY activity raises PRKY's level | lines that do not express UTY (31) vs lines expressing it (19) | 13.41× lower at baseline in the lines without UTY | 9e-06 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[GDNF-AS1]] | C | GDNF-AS1 activity raises PRKY's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 3.99× lower at baseline in the lines without GDNF-AS1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF423]] | B | PRKY activity raises ZNF423's level | lines that do not express PRKY (30) vs lines expressing it (20) | 1.51× lower at baseline in the lines without PRKY | 0.043 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1 |
| [[FDXR]] | B | PRKY activity raises FDXR's level | lines that do not express PRKY (30) vs lines expressing it (20) | 1.84× lower at baseline in the lines without PRKY | 0.057 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1 |
| [[UTY]] | C | PRKY, [[USP9Y]] activity raises UTY's level | lines that do not express PRKY, USP9Y (30) vs lines expressing them (20) | 17.21× lower at baseline in the lines without PRKY, USP9Y | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target; co-absent genes |
| [[EDA2R]] | C | PRKY activity raises EDA2R's level | lines that do not express PRKY (30) vs lines expressing it (20) | 2.77× lower at baseline in the lines without PRKY | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ZFY, KDM5D, RPS4Y1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.9, 15.9); signed map (25.0, 49.2). **Vector** length 64.2, 18.9% of its response variance represented; |z| ≥ 3 in 518 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +6.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +6.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -8.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -3.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase Y-linked (pseudogene) |
| Locus type | pseudogene |
| Location | Yp11.2 — chrY:7,274,313-7,371,868 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | PRKYP, PRKXP3 |
| Gene groups (HGNC) | Protein kinase A family |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [5616](https://www.ncbi.nlm.nih.gov/gene/5616):

> This gene is similar to the protein kinase, X-linked gene in the pseudoautosomal region of the X chromosome. The gene is classified as a transcribed pseudogene because it has lost a coding exon that results in all transcripts being candidates for nonsense-mediated decay (NMD) and unlikely to express a protein. Abnormal recombination between this gene and a related gene on chromosome X is a frequent cause of XX males and XY females. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:9444](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9444) · Entrez [5616](https://www.ncbi.nlm.nih.gov/gene/5616) · Ensembl [ENSG00000099725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099725)

## Data

Gene col 1807: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1807); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1807, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1807]; `tensor/DDL_lfc|DDL_z.npy` [1807]; `embed/gene_vectors.npy` [1807]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1807 or target_col == 1807). Every well: [[PRKY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

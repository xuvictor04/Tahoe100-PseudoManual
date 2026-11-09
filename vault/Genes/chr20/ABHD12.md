---
symbol: "ABHD12"
type: "gene"
col: 2056
ensembl_id: "ENSG00000100997"
name: "abhydrolase domain containing 12, lysophospholipase"
location: "20p11.21"
module: 163
arm: "+"
pooled_cpm: 81.24
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# ABHD12

*abhydrolase domain containing 12, lysophospholipase* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.66× (z +12.5, q 4e-33, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.576× (z -13.5, q 7e-39, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RANBP9]] (+0.70, fdr 7e-06), [[MFSD14B]] (+0.69, fdr 7e-06), [[RAP1A]] (+0.69, fdr 7e-06); moves opposite to [[CWC22]] (-0.67, fdr 7e-06), [[RPL7L1]] (-0.66, fdr 1e-05), [[ZNF24]] (-0.66, fdr 7e-06).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SMCO2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +12.5 | 4e-33 | 41/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +10.8 | 7e-25 | 31/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +9.4 | 1e-18 | 38/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.41×** | +8.4 | 5e-15 | 30/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.22×** | +6.9 | 5e-10 | 23/49 (NCI-H460, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +6.9 | 5e-10 | 31/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | **1.27×** | +5.6 | 1e-06 | 25/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +4.6 | 3e-04 | 19/49 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.19× | +4.2 | 0.002 | 21/48 (RKO, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.14× | +3.3 | 0.054 | 14/48 (SW480, PANC-1, …) | two highest doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.082 | 15/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2056.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.576×** | -13.5 | 7e-39 | 39/48 (A-427, SW 900, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.622×** | -11.6 | 9e-29 | 43/48 (SW 900, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.708×** | -8.4 | 6e-15 | 40/48 (HS-578T, A498, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.743×** | -7.3 | 6e-11 | 29/48 (HT-29, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.741×** | -6.8 | 2e-09 | 30/47 (AN3 CA, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.838× | -6.1 | 1e-07 | 22/48 (SW 900, HT-29, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -5.9 | 3e-07 | 20/48 (A-427, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.788×** | -5.6 | 2e-06 | 26/48 (A-427, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **0.813×** | -5.0 | 3e-05 | 24/48 (SW 1088, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.739×** | -3.9 | 0.006 | 20/47 (NCI-H1573, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.860× | -3.5 | 0.020 | 16/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.875× | -3.2 | 0.055 | 11/49 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.883× | -3.0 | 0.11 | 13/47 (A-427, LS 180, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 48.5 | 3 | 2 | [[Belinostat (drug)]] 5 µM 2.21× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -10.1) |
| [[SNU-1 (line)]] | wt | 242 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.394× (z -9.8) |
| [[SW 900 (line)]] | alt | 131 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -14.5) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 28.4 | 3 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.11× (z +9.8) | — |
| [[A-427 (line)]] | wt | 44.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -22.6) |
| [[HOP62 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 46.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +14.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.05× (z +8.8) | — |
| [[RKO (line)]] | wt | 87.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -11.8) |
| [[SW480 (line)]] | alt | 80.6 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 1.86× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 61.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 61.1 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.19× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 95.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 203 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -12.6) ⚠ cell-cycle shift, explains ~13% of this change |
| [[J82 (line)]] | alt | 79.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.530× (z -8.6) |
| [[LoVo (line)]] | wt | 45.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +11.8) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[LOX-IMVI (line)]] | wt | 37.5 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.97× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 56.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.2) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[NCI-H2030 (line)]] | alt | 48.8 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.39× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 84.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.486× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 81.2 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.155× (z -8.7) |
| [[SNU-423 (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -8.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[A-172 (line)]] | wt | 94.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 72.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 100 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP9]] | +0.70 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[MFSD14B]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[RAP1A]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation |
| [[CMC2]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[PACSIN2]] | +0.67 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[UBE2G1]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[SETD3]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[UBTD1]] | +0.66 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[RNF38]] | +0.66 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[MFSD14CP]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SAP130]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[RPA1]] | +0.65 | +0.65 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWC22]] | -0.67 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[RPL7L1]] | -0.66 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[ZNF24]] | -0.66 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[HDAC9]] | -0.66 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.65 | -0.73 / -0.56 | both halves | 1e-05 |  |
| [[SON]] | -0.65 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.65 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[FAM200A]] | -0.64 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[MYSM1]] | -0.63 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.63 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[ARL14EP]] | -0.62 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[OCIAD1]] | -0.62 | -0.61 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMCO2]] | B | SMCO2 activity lowers ABHD12's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.40× higher at baseline in the lines without SMCO2 | 0.012 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |
| [[CREB3L1]] | B | CREB3L1 activity raises ABHD12's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.48× lower at baseline in the lines without CREB3L1 | 0.032 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[CREB3L1]] | B | CREB3L1 activity weakens ABHD12's drug response | lines that do not express CREB3L1 (24) vs lines expressing it (25) | the lines without CREB3L1 respond 1.39× as strongly (z diff -0.89); strongest at Idarubicin (hydrochloride) 5 µM: 1.38x vs 1.05x (z diff -3.1) | 0.036 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1; target measured in part of the lines; artifact flags |
| [[LINC00944]] | B | LINC00944 activity raises ABHD12's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.34× lower at baseline in the lines without LINC00944 | 0.040 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[HDAC6]] | B | HDAC6 activity lowers ABHD12's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.0, -6.1); signed map (-40.6, -1.0). **Vector** length 121, 32.8% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +6.7 | +9.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.5 | +12.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.2 | +6.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | +3.9 | +5.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.2 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.0 | -13.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.1 | -11.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -9.0 | -8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -7.6 | -6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.2 | -5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.7 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 12, lysophospholipase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:25,294,742-25,390,835 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434P106, dJ965G21.2, BEM46L2, ABHD12A; previously C20orf22 |
| Gene groups (HGNC) | Abhydrolase domain containing; 2-arachidonoylglycerol hydrolases |
| Reactome | 7 pathways, smallest: Arachidonate production from DAG; Effects of PIP2 hydrolysis; G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2K0](https://www.uniprot.org/uniprotkb/Q8N2K0) (Lysophosphatidylserine lipase ABHD12):

> Lysophosphatidylserine (LPS) lipase that mediates the hydrolysis of lysophosphatidylserine, a class of signaling lipids that regulates immunological and neurological processes. Represents a major lysophosphatidylserine lipase in the brain, thereby playing a key role in the central nervous system (By similarity). Prefers as substrates lysophosphatidylserines having long and very long chain acyl chains. Also able to hydrolyze oxidized phosphatidylserine; oxidized phosphatidylserine is produced in …

**Summary**, from NCBI Gene [26090](https://www.ncbi.nlm.nih.gov/gene/26090):

> This gene encodes an enzyme that catalyzes the hydrolysis of 2-arachidonoyl glycerol (2-AG), the main endocannabinoid lipid transmitter that acts on cannabinoid receptors, CB1 and CB2. The endocannabinoid system is involved in a wide range of physiological processes, including neurotransmission, mood, appetite, pain appreciation, addiction behavior, and inflammation. Mutations in this gene are associated with the neurodegenerative disease, PHARC (polyneuropathy, hearing loss, ataxia, retinitis …

**Accessions** — [HGNC:15868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15868) · Entrez [26090](https://www.ncbi.nlm.nih.gov/gene/26090) · UniProt [Q8N2K0](https://www.uniprot.org/uniprotkb/Q8N2K0) · Ensembl [ENSG00000100997](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100997)

## Data

Gene col 2056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2056); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2056]; `tensor/DDL_lfc|DDL_z.npy` [2056]; `embed/gene_vectors.npy` [2056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2056 or target_col == 2056). Every well: [[ABHD12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

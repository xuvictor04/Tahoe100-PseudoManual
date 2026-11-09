---
symbol: "MRPL44"
type: "gene"
col: 5771
ensembl_id: "ENSG00000135900"
name: "mitochondrial ribosomal protein L44"
location: "2q36.1"
module: 119
arm: "+"
pooled_cpm: 24.84
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# MRPL44

*mitochondrial ribosomal protein L44* — 2q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.86× (z +16.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.413× (z -13.1, q 1e-36, down in 29 of 35 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (LS 180 0.0914×, HEC-1-A 0.0886×, A-172 0.0966×, C32 0.0784×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 0.129×, NCI-H2347 0.290×, LS 180 0.253×, NCI-H2030 0.214×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0922×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH4]] (+0.77, fdr 7e-06), [[COIL]] (+0.73, fdr 7e-06), [[PHAX]] (+0.69, fdr 1e-05); moves opposite to [[DIAPH1]] (-0.62, fdr 2e-05), [[SEPTIN10]] (-0.59, fdr 1e-05), [[ODF2]] (-0.57, fdr 1e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.86×** | +16.7 | 0e+00 | 48/48 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +10.6 | 5e-24 | 40/45 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.09×** | +9.1 | 1e-17 | 34/46 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.63×** | +7.6 | 4e-12 | 36/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.55×** | +6.8 | 2e-09 | 28/48 (SW480, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +6.6 | 4e-09 | 29/47 (A498, PANC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +6.3 | 3e-08 | 30/48 (C32, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.8 | 4e-07 | 29/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.42×** | +5.2 | 1e-05 | 30/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.8 | 8e-05 | 24/48 (A498, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.34×** | +4.6 | 2e-04 | 22/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +4.4 | 6e-04 | 23/47 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.32×** | +4.3 | 7e-04 | 23/46 (A-172, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.001 | 16/48 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +4.2 | 0.001 | 19/47 (A498, A-427, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.003 | 14/48 (Hs 766T, SW480, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +3.7 | 0.007 | 16/48 (CFPAC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.3 | 0.031 | 15/48 (AsPC-1, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.068 | 12/48 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5771.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (LS 180 0.0914×, HEC-1-A 0.0886×, A-172 0.0966×, C32 0.0784×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 0.129×, NCI-H2347 0.290×, LS 180 0.253×, NCI-H2030 0.214×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0922×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -13.1 | 1e-36 | 29/35 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.555×** | -8.3 | 2e-14 | 31/42 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 0.843× | -3.7 | 0.037 | 15/48 (CFPAC-1, SW 1271, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.822× | -3.0 | 0.36 | 8/48 (LoVo, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 35.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.61× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.0914× (z -19.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 21.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.81× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.94× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.328× (z -9.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 24.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0886× (z -17.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 22.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.2× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 26.4 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.52× (z +9.0) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 9.35× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.24× (z +10.2) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -10.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 24.9 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.0× (z +12.8) | — |
| [[A-172 (line)]] | wt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0966× (z -17.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0784× (z -13.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -12.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -11.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 19.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +8.8) | — |
| [[LoVo (line)]] | wt | 22.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.74× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 26.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.86× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0922× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -11.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH4]] | +0.77 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[COIL]] | +0.73 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[PHAX]] | +0.69 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[METTL14]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[RDH14]] | +0.68 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[NCBP2AS2]] | +0.67 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[TEFM]] | +0.66 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[ABT1]] | +0.65 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[TMEM11]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ZNF14]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[RCHY1]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ZNF576]] | +0.63 | +0.53 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | -0.62 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[SEPTIN10]] | -0.59 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ODF2]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[SLC4A7]] | -0.56 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[RELT]] | -0.55 | -0.58 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.0, 3.9); signed map (-10.8, -11.9). **Vector** length 94.3, 22.8% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.8 | +6.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +16.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.9 | +10.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +9.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.9 | -8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.6 | -13.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.8 | -1.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | -2.4 | +4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | +0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.1 — chr2:223,957,463-223,967,714 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12701, FLJ13990, mL44 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9J2](https://www.uniprot.org/uniprotkb/Q9H9J2) (Large ribosomal subunit protein mL44):

> Component of the 39S subunit of mitochondrial ribosome. May have a function in the assembly/stability of nascent mitochondrial polypeptides exiting the ribosome.

**Summary**, from NCBI Gene [65080](https://www.ncbi.nlm.nih.gov/gene/65080):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:16650](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16650) · Entrez [65080](https://www.ncbi.nlm.nih.gov/gene/65080) · UniProt [Q9H9J2](https://www.uniprot.org/uniprotkb/Q9H9J2) · Ensembl [ENSG00000135900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135900)

## Data

Gene col 5771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5771); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5771]; `tensor/DDL_lfc|DDL_z.npy` [5771]; `embed/gene_vectors.npy` [5771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5771 or target_col == 5771). Every well: [[MRPL44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

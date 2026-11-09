---
symbol: "CCNJL"
type: "gene"
col: 5649
ensembl_id: "ENSG00000135083"
name: "cyclin J like"
location: "5q33.3"
module: 135
arm: "-"
pooled_cpm: 16.81
n_lines_expressing: 41
n_dd_up: 6
n_dd_down: 28
n_dd_up_clean: 5
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# CCNJL

*cyclin J like* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.34× (z +7.1, q 5e-10, up in 23 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.368× (z -23.9, q 0e+00, down in 30 of 38 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGS14]] (+0.60, fdr 1e-05), [[ABHD6]] (+0.58, fdr 1e-04), [[ST3GAL5]] (+0.58, fdr 3e-05); moves opposite to [[VPS35L]] (-0.52, fdr 3e-05), [[CACNA2D1]] (-0.51, fdr 6e-05), [[RC3H2]] (-0.51, fdr 4e-05).
> It sits in the **-** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CARD11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +7.1 | 5e-10 | 23/38 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +4.7 | 7e-04 | 16/39 (LoVo, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 7e-04 | 14/37 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +4.5 | 1e-03 | 12/39 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +4.0 | 0.008 | 11/38 (H4, A498, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.3 | 0.078 | 10/37 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.078 | 0/39 | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5649.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.368×** | -23.9 | 0e+00 | 30/38 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.478×** | -17.7 | 0e+00 | 27/36 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.405×** | -14.7 | 0e+00 | 31/39 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.433×** | -13.6 | 5e-40 | 17/21 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.434×** | -13.6 | 6e-40 | 28/37 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.465×** | -13.0 | 2e-36 | 24/39 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.455×** | -12.8 | 1e-35 | 27/37 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.507×** | -11.5 | 1e-28 | 25/37 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.536×** | -10.5 | 4e-24 | 25/29 (SW 900, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.549×** | -10.1 | 3e-22 | 24/39 (RKO, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.585×** | -9.1 | 7e-18 | 20/38 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.577×** | -8.6 | 4e-16 | 18/28 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.604×** | -8.5 | 8e-16 | 21/35 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.672×** | -6.7 | 8e-10 | 20/38 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.705×** | -5.9 | 1e-07 | 20/37 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.726×** | -5.2 | 7e-06 | 15/37 (C32, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.749×** | -4.9 | 4e-05 | 14/39 (C32, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.752×** | -4.6 | 1e-04 | 12/37 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.770×** | -4.4 | 3e-04 | 13/38 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 37.4 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -23.1) |
| [[SW 900 (line)]] | alt | 86.9 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -19.5) |
| [[PANC-1 (line)]] | alt | 26.5 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -23.9) |
| [[A-172 (line)]] | wt | 23.6 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -19.2) |
| [[SW480 (line)]] | alt | 29.9 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -17.7) |
| [[C32 (line)]] | wt | 25.5 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0860× (z -16.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.207× (z -15.5) |
| [[HOP62 (line)]] | alt | 22.3 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -13.4) |
| [[SW1417 (line)]] | alt | 16.9 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -13.0) |
| [[A498 (line)]] | wt | 25.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 26.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -16.2) |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -12.1) |
| [[RKO (line)]] | wt | 12.8 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0442× (z -15.3) |
| [[SNU-423 (line)]] | alt | 22.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0453× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.190× (z -15.3) |
| [[HepG2_C3A (line)]] | wt | 20.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0865× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.216× (z -10.1) |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.277× (z -9.2) |
| [[J82 (line)]] | alt | 12.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -15.5) |
| [[A549 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -8.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0848× (z -9.7) |
| [[HT-29 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 4.91 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0825× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.174× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 4.56 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 7.18 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.169× (z -9.4) |
| [[SHP-77 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -14.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 11.1 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0781× (z -9.1) |
| [[A-427 (line)]] | wt | 3.62 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS14]] | +0.60 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ABHD6]] | +0.58 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[ST3GAL5]] | +0.58 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[CKLF]] | +0.57 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[ETV5]] | +0.57 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[EIF4EBP1]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MFSD9]] | +0.57 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[MAP3K9]] | +0.56 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[TOX2]] | +0.56 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[SLC27A1]] | +0.54 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[WASF3]] | +0.54 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[HPCAL1]] | +0.54 | +0.52 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS35L]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[CACNA2D1]] | -0.51 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[RC3H2]] | -0.51 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[DUSP16]] | -0.50 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[PBLD]] | -0.50 | -0.51 / -0.32 | both halves | 1e-04 |  |
| [[TAX1BP3]] | -0.50 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[DECR1]] | -0.50 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[CNTLN]] | -0.50 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[TAPBP]] | -0.50 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[UBE3B]] | -0.49 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[FSTL3]] | -0.49 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[LINC01004]] | -0.49 | -0.51 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD11]] | B | CARD11 activity strengthens CCNJL's drug response | lines that do not express CARD11 (27) vs lines expressing it (12) | the lines without CARD11 respond 0.47× as strongly (z diff +2.90); strongest at Idarubicin (hydrochloride) 5 µM: 0.66x vs 0.27x (z diff +5.7) | 0.012 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3; target measured in part of the lines; artifact flags |
| [[SHROOM2]] | B | SHROOM2 activity raises CCNJL's level | lines that do not express SHROOM2 (15) vs lines expressing it (35) | 1.95× lower at baseline in the lines without SHROOM2 | 0.012 | ⚠ within organs, on part of the lines; also absent: GPR143, RASGEF1C |
| [[SHROOM4]] | B | SHROOM4 activity raises CCNJL's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 1.95× lower at baseline in the lines without SHROOM4 | 0.036 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539 |
| [[VLDLR]] | B | VLDLR activity raises CCNJL's level | lines that do not express VLDLR (8) vs lines expressing it (42) | 2.21× lower at baseline in the lines without VLDLR | 0.072 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989 |
| [[MAP2K1]] | B | MAP2K1 activity raises CCNJL's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **-** arm (projection on the module's main direction -0.378). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (5.5, 5.4); signed map (-46.8, 20.7). **Vector** length 93.1, 20.6% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -0.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -14.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -13.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -8.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -10.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.6 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | cyclin J like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:160,249,083-160,345,396 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14166 |
| Gene groups (HGNC) | Cyclins |
| Matched by | ensembl_id |

UniProt [Q8IV13](https://www.uniprot.org/uniprotkb/Q8IV13) carries no function annotation.

**Summary**, from NCBI Gene [79616](https://www.ncbi.nlm.nih.gov/gene/79616):

> Predicted to enable cyclin-dependent protein serine/threonine kinase regulator activity. Predicted to be involved in G1/S transition of mitotic cell cycle. Predicted to be part of cyclin-dependent protein kinase holoenzyme complex. Predicted to be active in cytoplasm; microtubule organizing center; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25876) · Entrez [79616](https://www.ncbi.nlm.nih.gov/gene/79616) · UniProt [Q8IV13](https://www.uniprot.org/uniprotkb/Q8IV13) · Ensembl [ENSG00000135083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135083)

## Data

Gene col 5649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5649); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5649]; `tensor/DDL_lfc|DDL_z.npy` [5649]; `embed/gene_vectors.npy` [5649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5649 or target_col == 5649). Every well: [[CCNJL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNJL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

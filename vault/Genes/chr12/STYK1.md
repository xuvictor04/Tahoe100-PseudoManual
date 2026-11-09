---
symbol: "STYK1"
type: "gene"
col: 684
ensembl_id: "ENSG00000060140"
name: "STY kinase 1"
location: "12p13.2"
module: 8
arm: "+"
pooled_cpm: 25.66
n_lines_expressing: 30
n_dd_up: 28
n_dd_down: 17
n_dd_up_clean: 20
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 42
direction_downstream: 46
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# STYK1

*STY kinase 1* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.37× (z +20.4, q 0e+00, up in 15 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.532× (z -10.6, q 2e-23, down in 23 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.572× (z -9.4, q 1e-18, down in 20 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSH2D]] (+0.57, fdr 1e-05), [[LIPH]] (+0.56, fdr 1e-05), [[INAVA]] (+0.55, fdr 1e-05); moves opposite to [[CA5B]] (-0.53, fdr 2e-05), [[BCL7C]] (-0.48, fdr 2e-04), [[PACS2]] (-0.47, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 42 arrows point to it, the strongest [[SLC44A3-AS1]] → it (grade B ⚠); 46 go from it, the strongest it → [[JUP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 684.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.37×** | +20.4 | 0e+00 | 15/28 (NCI-H1792, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +13.5 | 7e-39 | 23/28 (NCI-H1792, LS 180, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +11.8 | 8e-30 | 12/27 (LOX-IMVI, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +11.0 | 6e-26 | 17/28 (LS 180, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +10.7 | 1e-24 | 22/27 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.77×** | +9.5 | 2e-19 | 18/28 (HOP62, NCI-H1573, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.77×** | +9.0 | 1e-17 | 16/27 (NCI-H23, SW 900, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.75×** | +8.8 | 8e-17 | 15/27 (HOP62, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +8.8 | 1e-16 | 15/28 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +8.2 | 1e-14 | 17/28 (HOP62, COLO 205, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +6.4 | 7e-09 | 15/27 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.9 | 2e-07 | 11/28 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.2 | 8e-06 | 5/27 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.36×** | +5.1 | 1e-05 | 11/28 (NCI-H2347, LS 180, …) | all doses, stronger at high dose |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.76×** | +4.9 | 3e-05 | 10/28 (LOX-IMVI, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 684.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.532×** | -10.6 | 2e-23 | 23/27 (COLO 205, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.572×** | -9.4 | 1e-18 | 20/28 (COLO 205, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.572×** | -9.0 | 3e-17 | 21/27 (HEC-1-A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -8.3 | 2e-14 | 18/23 (NCI-H2030, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.612×** | -8.3 | 2e-14 | 18/27 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.654×** | -7.1 | 9e-11 | 23/28 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.475×** | -6.6 | 5e-09 | 20/27 (HT-29, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -6.5 | 5e-09 | 18/27 (LS 180, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.481×** | -6.4 | 8e-09 | 16/27 (COLO 205, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.497×** | -6.2 | 4e-08 | 20/27 (AsPC-1, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.535×** | -5.5 | 2e-06 | 14/27 (SW480, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.745×** | -5.0 | 3e-05 | 13/27 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.752×** | -4.8 | 7e-05 | 16/28 (NCI-H23, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.758×** | -4.7 | 1e-04 | 11/28 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.796×** | -3.7 | 0.008 | 9/28 (HT-29, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.812×** | -3.5 | 0.016 | 15/28 (COLO 205, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.875× | -3.2 | 0.042 | 4/28 (HT-29, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 66.8 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.287× (z -10.4) |
| [[COLO 205 (line)]] | alt | 69.5 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 36.9 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0819× (z -18.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.259× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 122 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.257× (z -12.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.374× (z -9.4) |
| [[A-427 (line)]] | wt | 113 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.349× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 14.8 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 53.7× (z +28.6) | [[LJI308 (drug)]] 0.5 µM 0.0388× (z -11.8) |
| [[BT-474 (line)]] | alt | 30.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +17.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0617× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[CFPAC-1 (line)]] | alt | 86.4 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -10.7) |
| [[HOP62 (line)]] | alt | 7.03 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.35× (z +13.8) | — |
| [[LS 180 (line)]] | wt | 26.8 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.48× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.280× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 82.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0901× (z -15.0) ⚠ toxic |
| [[A498 (line)]] | wt | 22.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.9) | — |
| [[HT-29 (line)]] | alt | 59.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -14.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 43.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +15.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 6.74 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.54× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 53.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 15.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0651× (z -12.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.165× (z -8.6) |
| [[SW 900 (line)]] | alt | 14.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -9.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -16.1) ⚠ toxic |
| [[J82 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +11.6) | — |
| [[A-172 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.10 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.78 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSH2D]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[LIPH]] | +0.56 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[INAVA]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[CPNE4]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SLCO3A1]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PLEKHG6]] | +0.52 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[FRK]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[FUT2]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TTC22]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[IL22RA1]] | +0.51 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[CRACDL]] | +0.51 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[XDH]] | +0.51 | +0.44 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CA5B]] | -0.53 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[BCL7C]] | -0.48 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[PACS2]] | -0.47 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[THAP4]] | -0.46 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[NPRL3]] | -0.44 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[FAM228B]] | -0.43 | -0.34 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 13, C 29. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises STYK1's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.58× lower at baseline in the lines without SLC44A3-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[IKZF2]] | B | IKZF2 activity raises STYK1's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without IKZF2 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[LPAR5]] | B | LPAR5 activity raises STYK1's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.93× lower at baseline in the lines without LPAR5 | 0.009 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[VAV1]] | B | VAV1 activity raises STYK1's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 2.54× lower at baseline in the lines without VAV1 | 0.021 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[CRYBG2]] | B | CRYBG2 activity raises STYK1's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 3.11× lower at baseline in the lines without CRYBG2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[SLC44A3]] | B | SLC44A3 activity raises STYK1's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.54× lower at baseline in the lines without SLC44A3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[PLEKHG1]] | B | PLEKHG1 activity raises STYK1's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.47× lower at baseline in the lines without PLEKHG1 | 0.052 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[LINC01559]] | B | LINC01559 activity raises STYK1's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 3.03× lower at baseline in the lines without LINC01559 | 0.054 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17 |
| [[CYP4F3]] | B | CYP4F3 activity raises STYK1's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.72× lower at baseline in the lines without CYP4F3 | 0.057 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[MUC16]] | B | MUC16 activity raises STYK1's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 3.95× lower at baseline in the lines without MUC16 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4 |
| [[SPATA6L]] | B | SPATA6L activity raises STYK1's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.61× lower at baseline in the lines without SPATA6L | 0.084 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[JUP]] | B | JUP activity raises STYK1's level | lines that do not express JUP (16) vs lines expressing it (34) | 3.19× lower at baseline in the lines without JUP | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 17, C 29. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JUP]] | B | STYK1 activity raises JUP's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 3.84× lower at baseline in the lines without STYK1 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[ACOT11]] | B | STYK1 activity raises ACOT11's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without STYK1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[LPAR5]] | B | STYK1 activity raises LPAR5's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without STYK1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[AFF1]] | B | STYK1 activity raises AFF1's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 1.64× lower at baseline in the lines without STYK1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[SLC44A3]] | B | STYK1 activity raises SLC44A3's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.68× lower at baseline in the lines without STYK1 | 0.015 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[ELF3-AS1]] | B | STYK1 activity raises ELF3-AS1's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.58× lower at baseline in the lines without STYK1 | 0.016 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[CRYBG2]] | B | STYK1 activity raises CRYBG2's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.91× lower at baseline in the lines without STYK1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[LNX1]] | B | STYK1 activity raises LNX1's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.55× lower at baseline in the lines without STYK1 | 0.021 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[IKZF2]] | B | STYK1 activity raises IKZF2's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without STYK1 | 0.021 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[SLC44A3-AS1]] | B | STYK1 activity raises SLC44A3-AS1's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.69× lower at baseline in the lines without STYK1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[B3GALT5]] | B | STYK1 activity raises B3GALT5's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.01× lower at baseline in the lines without STYK1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[ITPKC]] | B | STYK1 activity raises ITPKC's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.16× lower at baseline in the lines without STYK1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.1, 56.1); signed map (55.1, 10.7). **Vector** length 90.5, 23.4% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +10.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.2 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +20.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +9.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -7.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -6.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -9.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -6.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -5.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | STY kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.2 — chr12:10,618,923-10,674,318 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SuRTK106, DKFZp761P1010, NOK |
| Gene groups (HGNC) | STY kinase 1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6J9G0](https://www.uniprot.org/uniprotkb/Q6J9G0) (Tyrosine-protein kinase STYK1):

> Probable tyrosine protein-kinase, which has strong transforming capabilities on a variety of cell lines. When overexpressed, it can also induce tumor cell invasion as well as metastasis in distant organs. May act by activating both MAP kinase and phosphatidylinositol 3'-kinases (PI3K) pathways (By similarity).

**Summary**, from NCBI Gene [55359](https://www.ncbi.nlm.nih.gov/gene/55359):

> Receptor protein tyrosine kinases, like STYK1, play important roles in diverse cellular and developmental processes, such as cell proliferation, differentiation, and survival (Liu et al., 2004 [PubMed 15150103]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18889](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18889) · Entrez [55359](https://www.ncbi.nlm.nih.gov/gene/55359) · UniProt [Q6J9G0](https://www.uniprot.org/uniprotkb/Q6J9G0) · Ensembl [ENSG00000060140](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060140)

## Data

Gene col 684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 684); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 684]; `tensor/DDL_lfc|DDL_z.npy` [684]; `embed/gene_vectors.npy` [684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 684 or target_col == 684). Every well: [[STYK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STYK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

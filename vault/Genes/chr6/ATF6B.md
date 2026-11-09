---
symbol: "ATF6B"
type: "gene"
col: 13126
ensembl_id: "ENSG00000213676"
name: "activating transcription factor 6 beta"
location: "6p21.3"
module: 76
arm: "+"
pooled_cpm: 27.0
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# ATF6B

*activating transcription factor 6 beta* — 6p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.67× (z +10.0, q 7e-21, up in 23 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.32× (z +5.6, q 4e-06, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.504× (z -13.9, q 2e-41, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSD]] (+0.71, fdr 7e-06), [[TMEM59]] (+0.68, fdr 7e-06), [[UBXN6]] (+0.65, fdr 7e-06); moves opposite to [[TNFRSF12A]] (-0.58, fdr 1e-05), [[TTPAL]] (-0.57, fdr 1e-05), [[CEP83]] (-0.57, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13126.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +10.0 | 7e-21 | 23/35 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +8.9 | 2e-16 | 32/44 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.6 | 4e-06 | 26/48 (PANC-1, SW480, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +5.2 | 2e-05 | 20/40 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +4.0 | 0.007 | 16/47 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~4% of this change | **1.20×** | +3.8 | 0.013 | 17/46 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.013 | 10/46 (C32, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.014 | 11/48 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.014 | 13/46 (A-427, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.025 | 8/45 (HEC-1-A, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.20× | +3.5 | 0.026 | 13/48 (RKO, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.043 | 14/47 (PANC-1, LS 180, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 1.36× | +3.0 | 0.12 | 10/48 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13126.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.504×** | -13.9 | 2e-41 | 40/47 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.642×** | -12.8 | 7e-35 | 33/47 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.570×** | -11.5 | 4e-28 | 41/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -9.4 | 5e-19 | 39/48 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.716×** | -6.8 | 1e-09 | 29/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.715×** | -6.6 | 5e-09 | 25/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.825×** | -5.5 | 2e-06 | 21/48 (NCI-H460, A-427, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.574×** | -5.3 | 6e-06 | 22/47 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.582×** | -5.2 | 1e-05 | 22/47 (SNU-1, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.775×** | -5.2 | 1e-05 | 22/48 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.584×** | -5.2 | 1e-05 | 24/47 (H4, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.584×** | -5.2 | 1e-05 | 21/48 (NCI-H460, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.777×** | -5.1 | 1e-05 | 22/47 (J82, CFPAC-1, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.744×** | -4.3 | 7e-04 | 19/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.807×** | -4.1 | 0.001 | 18/48 (Hs 766T, SW 900, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.797×** | -4.0 | 0.002 | 15/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.840× | -3.5 | 0.013 | 11/47 (SW480, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13126. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 36.0 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +15.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 35.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -14.8) |
| [[LoVo (line)]] | wt | 15.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -10.2) |
| [[SNU-423 (line)]] | alt | 40.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.6) |
| [[SW 900 (line)]] | alt | 27.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -16.3) |
| [[A549 (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +9.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.0) |
| [[COLO 205 (line)]] | alt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 26.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.8) |
| [[HS-578T (line)]] | alt | 31.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.121× (z -8.5) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.282× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.358× (z -9.4) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 37.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.353× (z -8.8) |
| [[A-172 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13126), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSD]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[TMEM59]] | +0.68 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[UBXN6]] | +0.65 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[DHPS]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ALDH6A1]] | +0.64 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[CALCOCO1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[OS9]] | +0.63 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[LAPTM4A]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[KLHDC3]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 | pathway: Unfolded Protein Response (UPR) |
| [[GNPTG]] | +0.62 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[DCAF11]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[PTOV1]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF12A]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[TTPAL]] | -0.57 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[CEP83]] | -0.57 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[NPL]] | -0.56 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[NIFK]] | -0.56 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[EPOP]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[C12orf29]] | -0.55 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[NIPAL1]] | -0.54 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[SOWAHC]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[NOC3L]] | -0.53 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[GNPNAT1]] | -0.52 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[HSF2BP]] | -0.52 | -0.58 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, -18.9); signed map (-20.2, 6.9). **Vector** length 96.7, 21.1% of its response variance represented; |z| ≥ 3 in 817 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | +1.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.6 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -13.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.5 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -5.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -5.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | activating transcription factor 6 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.3 — chr6:32,115,264-32,128,253 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G13, ATF6beta; previously CREBL1 |
| Gene groups (HGNC) | Activating transcription factor 6 family |
| Reactome | 4 pathways, smallest: ATF6B (ATF6-beta) activates chaperones; Unfolded Protein Response (UPR); Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99941](https://www.uniprot.org/uniprotkb/Q99941) (Cyclic AMP-dependent transcription factor ATF-6 beta):

> [Cyclic AMP-dependent transcription factor ATF-6 beta]: Precursor of the transcription factor form (Processed cyclic AMP-dependent transcription factor ATF-6 beta), which is embedded in the endoplasmic reticulum membrane. Endoplasmic reticulum stress promotes processing of this form, releasing the transcription factor form that translocates into the nucleus, where it activates transcription of genes involved in the unfolded protein response (UPR).; [Processed cyclic AMP-dependent transcription …

**Summary**, from NCBI Gene [1388](https://www.ncbi.nlm.nih.gov/gene/1388):

> The protein encoded by this gene is a transcription factor in the unfolded protein response (UPR) pathway during ER stress. Either as a homodimer or as a heterodimer with ATF6-alpha, the encoded protein binds to the ER stress response element, interacting with nuclear transcription factor Y to activate UPR target genes. The protein is normally found in the membrane of the endoplasmic reticulum; however, under ER stress, the N-terminal cytoplasmic domain is cleaved from the rest of the protein …

**Accessions** — [HGNC:2349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2349) · Entrez [1388](https://www.ncbi.nlm.nih.gov/gene/1388) · UniProt [Q99941](https://www.uniprot.org/uniprotkb/Q99941) · Ensembl [ENSG00000213676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213676)

## Data

Gene col 13126: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13126); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13126, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13126]; `tensor/DDL_lfc|DDL_z.npy` [13126]; `embed/gene_vectors.npy` [13126]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13126 or target_col == 13126). Every well: [[ATF6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATF6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

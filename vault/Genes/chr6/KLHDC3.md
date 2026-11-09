---
symbol: "KLHDC3"
type: "gene"
col: 4559
ensembl_id: "ENSG00000124702"
name: "kelch domain containing 3"
location: "6p21.1"
module: 76
arm: "+"
pooled_cpm: 20.79
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 27
n_dd_up_clean: 3
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# KLHDC3

*kelch domain containing 3* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.20× (z +5.0, q 3e-04, up in 17 of 48 measured lines) ⚠ cell-cycle shift, explains ~20% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.36× (z +4.3, q 0.003, up in 13 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.339× (z -30.0, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WIPI2]] (+0.80, fdr 7e-06), [[CCDC28A]] (+0.74, fdr 7e-06), [[MKRN1]] (+0.71, fdr 7e-06); moves opposite to [[ERCC6L2]] (-0.64, fdr 1e-05), [[EIF3J]] (-0.60, fdr 1e-05), [[ST7L]] (-0.59, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.20× | +5.0 | 3e-04 | 17/48 (NCI-H1573, PANC-1, …) | top dose only | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.6 | 0.002 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 0.003 | 13/48 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.074 | 13/46 (HEC-1-A, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.090 | 6/46 (KATO III, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.090 | 10/47 (RKO, NCI-H460, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.090 | 6/48 (HT-29, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.2 | 0.090 | 6/37 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.10 | 10/48 (HOP62, SW480, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4559.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.339×** | -30.0 | 0e+00 | 46/47 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.361×** | -19.2 | 0e+00 | 47/48 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.403×** | -17.8 | 0e+00 | 41/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.501×** | -13.5 | 1e-39 | 42/47 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -9.3 | 1e-18 | 39/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.663×** | -8.1 | 7e-14 | 31/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.459×** | -8.0 | 1e-13 | 31/46 (SNU-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.471×** | -7.7 | 9e-13 | 30/44 (H4, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.480×** | -7.5 | 3e-12 | 25/47 (NCI-H23, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.686×** | -7.4 | 9e-12 | 23/47 (AsPC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.692×** | -7.2 | 3e-11 | 26/46 (SW48, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.529×** | -6.5 | 3e-09 | 23/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.729×** | -6.2 | 3e-08 | 20/47 (SNU-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.550×** | -6.1 | 3e-08 | 25/47 (SW1417, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.733×** | -6.1 | 4e-08 | 25/48 (NCI-H2347, SNU-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.581×** | -5.6 | 9e-07 | 22/48 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.673×** | -5.5 | 1e-06 | 21/48 (SHP-77, NCI-H2030, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -17.8) |
| [[CFPAC-1 (line)]] | alt | 26.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -20.2) |
| [[NCI-H2347 (line)]] | alt | 22.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -15.1) |
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -20.8) |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.4) |
| [[Hs 766T (line)]] | wt | 15.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 29.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -14.5) |
| [[NCI-H23 (line)]] | alt | 28.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -12.9) |
| [[SW 900 (line)]] | alt | 18.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -13.3) |
| [[SW480 (line)]] | alt | 18.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -19.6) |
| [[A-172 (line)]] | wt | 17.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.9) |
| [[A-427 (line)]] | wt | 23.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -12.9) |
| [[C32 (line)]] | wt | 15.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -10.0) |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0410× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 25.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.9) |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -18.6) |
| [[KATO III (line)]] | alt | 24.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.366× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 25.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 35.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.150× (z -15.0) |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -12.7) |
| [[HS-578T (line)]] | alt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.310× (z -8.6) |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.8) |
| [[J82 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.6) |
| [[LoVo (line)]] | wt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 7.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0348× (z -17.1) |
| [[SK-MEL-2 (line)]] | alt | 26.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.8) |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 39.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -15.9) |
| [[SW48 (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WIPI2]] | +0.80 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[MKRN1]] | +0.71 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.70 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[SPSB3]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[LMBR1L]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[HINFP]] | +0.68 | +0.51 / +0.77 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[RETREG2]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PPT2]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[SNX1]] | +0.66 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[MARF1]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.64 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.60 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[ST7L]] | -0.59 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.59 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.57 | -0.66 / -0.39 | both halves | 5e-05 |  |
| [[LZIC]] | -0.56 | -0.66 / -0.39 | both halves | 5e-05 |  |
| [[WARS2-AS1]] | -0.56 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[COMMD10]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[NANOS3]] | -0.56 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[ANAPC7]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ZBTB38]] | -0.55 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.818). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.5, -45.3); signed map (-19.1, 9.8). **Vector** length 97.3, 21.5% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +3.3 | +5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +2.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.6 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.1 | -30.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -19.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -17.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.8 | -13.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -9.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.8 | -8.0 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -7.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.5 | -7.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.0 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | kelch domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:43,014,103-43,021,298 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEAS, hPeas, dJ20C7.3 |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 5 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ90](https://www.uniprot.org/uniprotkb/Q9BQ90) (Kelch domain-containing protein 3):

> Substrate-recognition component of a Cul2-RING (CRL2) E3 ubiquitin-protein ligase complex of the DesCEND (destruction via C-end degrons) pathway, which recognizes a C-degron located at the extreme C terminus of target proteins, leading to their ubiquitination and degradation. The C-degron recognized by the DesCEND pathway is usually a motif of less than ten residues and can be present in full-length proteins, truncated proteins or proteolytically cleaved forms. The CRL2(KLHDC3) complex …

**Summary**, from NCBI Gene [116138](https://www.ncbi.nlm.nih.gov/gene/116138):

> The protein encoded by this gene contains six repeated kelch motifs that are structurally similar to recombination activating gene 2, a protein involved in the activation of the V(D)J recombination. In mouse, this gene is found to be expressed specifically in testis. Its expression in pachytene spermatocytes is localized to cytoplasma and meiotic chromatin, suggesting that this gene may be involved in meiotic recombination. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:20704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20704) · Entrez [116138](https://www.ncbi.nlm.nih.gov/gene/116138) · UniProt [Q9BQ90](https://www.uniprot.org/uniprotkb/Q9BQ90) · Ensembl [ENSG00000124702](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124702)

## Data

Gene col 4559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4559); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4559]; `tensor/DDL_lfc|DDL_z.npy` [4559]; `embed/gene_vectors.npy` [4559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4559 or target_col == 4559). Every well: [[KLHDC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHDC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

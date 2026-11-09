---
symbol: "ADPRS"
type: "gene"
col: 3849
ensembl_id: "ENSG00000116863"
name: "ADP-ribosylserine hydrolase"
location: "1p34.3"
module: 119
arm: "+"
pooled_cpm: 27.29
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# ADPRS

*ADP-ribosylserine hydrolase* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.53× (z +5.3, q 7e-05, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.358× (z -12.2, q 1e-31, down in 27 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.822× (z -3.4, q 0.082, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A498 0.103×, SW1417 0.0992×, HT-29 0.0941×, A-172 0.154×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LoVo 0.0583×, Hs 766T 0.0796×, MIA PaCa-2 0.163×, A-172 0.177×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C16orf91]] (+0.75, fdr 7e-06), [[NCBP2AS2]] (+0.71, fdr 3e-05), [[N4BP1]] (+0.71, fdr 7e-06); moves opposite to [[DHFR]] (-0.68, fdr 4e-05), [[NONO]] (-0.66, fdr 1e-05), [[GNG12]] (-0.64, fdr 1e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +5.3 | 7e-05 | 28/47 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +5.2 | 7e-05 | 32/45 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.08×** | +4.7 | 4e-04 | 26/46 (HOP62, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +4.6 | 6e-04 | 29/48 (RKO, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.010 | 22/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.6 | 0.036 | 21/48 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3849.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A498 0.103×, SW1417 0.0992×, HT-29 0.0941×, A-172 0.154×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (LoVo 0.0583×, Hs 766T 0.0796×, MIA PaCa-2 0.163×, A-172 0.177×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.155×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.358×** | -12.2 | 1e-31 | 27/35 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.530×** | -7.9 | 1e-12 | 34/44 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.668×** | -4.8 | 3e-04 | 28/47 (C-33 A, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.082 | 19/48 (MIA PaCa-2, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | 0.629× | -3.0 | 0.31 | 13/48 (RPMI-7951, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 33.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -11.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -12.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 32.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -10.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 36.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -10.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 32.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 27.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 27.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[A-427 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -19.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.137× (z -10.5) ⚠ toxic |
| [[H4 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -8.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -10.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -9.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 29.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0796× (z -16.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -11.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0941× (z -13.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[LoVo (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0583× (z -22.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -11.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0992× (z -15.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0868× (z -11.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A549 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C16orf91]] | +0.75 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[NCBP2AS2]] | +0.71 | +0.45 / +0.80 | both halves | 3e-05 |  |
| [[N4BP1]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[TIMM29]] | +0.70 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | +0.69 | +0.49 / +0.75 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TTF1]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[IMP3]] | +0.69 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[C18orf21]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MED19]] | +0.68 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[ZNF766]] | +0.68 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[RNF113A]] | +0.68 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[ALKBH4]] | +0.68 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[ZNF593]] | +0.67 | +0.47 / +0.71 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHFR]] | -0.68 | -0.41 / -0.73 | both halves | 4e-05 |  |
| [[NONO]] | -0.66 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[GNG12]] | -0.64 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[STT3B]] | -0.63 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[HNRNPA3]] | -0.63 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[MMGT1]] | -0.63 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.63 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[IPO5]] | -0.63 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[FKBP9]] | -0.62 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[UBQLN4]] | -0.62 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[CRTAP]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ACADVL]] | -0.61 | -0.43 / -0.62 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.0, -10.1); signed map (-9.4, -10.8). **Vector** length 108, 29.4% of its response variance represented; |z| ≥ 3 in 595 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +3.6 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +0.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -11.2 | -7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.9 | -12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change | -8.6 | -0.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.4 | -4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.8 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ADP-ribosylserine hydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:36,088,892-36,093,932 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARH3, FLJ20446; previously ADPRHL2 |
| Reactome | 5 pathways, smallest: POLB-Dependent Long Patch Base Excision Repair; Resolution of AP sites via the multiple-nucleotide patch replacement pathway; Resolution of Abasic Sites (AP sites) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX46](https://www.uniprot.org/uniprotkb/Q9NX46) (ADP-ribosylhydrolase ARH3):

> ADP-ribosylhydrolase that preferentially hydrolyzes the scissile alpha-O-linkage attached to the anomeric C1'' position of ADP-ribose and acts on different substrates, such as proteins ADP-ribosylated on serine and threonine, free poly(ADP-ribose) and O-acetyl-ADP-D-ribose. Specifically acts as a serine mono-ADP-ribosylhydrolase by mediating the removal of mono-ADP-ribose attached to serine residues on proteins, thereby playing a key role in DNA damage response. Serine ADP-ribosylation of …

**Summary**, from NCBI Gene [54936](https://www.ncbi.nlm.nih.gov/gene/54936):

> This gene encodes a member of the ADP-ribosylglycohydrolase family. The encoded enzyme catalyzes the removal of ADP-ribose from ADP-ribosylated proteins. This enzyme localizes to the mitochondria, in addition to the nucleus and cytoplasm.[provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:21304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21304) · Entrez [54936](https://www.ncbi.nlm.nih.gov/gene/54936) · UniProt [Q9NX46](https://www.uniprot.org/uniprotkb/Q9NX46) · Ensembl [ENSG00000116863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116863)

## Data

Gene col 3849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3849); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3849]; `tensor/DDL_lfc|DDL_z.npy` [3849]; `embed/gene_vectors.npy` [3849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3849 or target_col == 3849). Every well: [[ADPRS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADPRS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "PHB2"
type: "gene"
col: 13240
ensembl_id: "ENSG00000215021"
name: "prohibitin 2"
location: "12p13.31"
module: 169
arm: "+"
pooled_cpm: 34.59
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# PHB2

*prohibitin 2* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.18× (z +14.2, q 9e-43, up in 43 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +6.5, q 9e-09, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.569× (z -9.7, q 1e-19, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF7]] (+0.72, fdr 9e-06), [[RNF4]] (+0.68, fdr 1e-05), [[RPL29]] (+0.67, fdr 1e-05); moves opposite to [[ZNF674]] (-0.60, fdr 1e-05), [[PIM3]] (-0.58, fdr 2e-05), [[SERTAD1]] (-0.58, fdr 1e-05).
> It is in [[Module 169]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +14.2 | 9e-43 | 43/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +11.3 | 4e-27 | 33/38 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +6.6 | 8e-09 | 36/43 (KATO III, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.5 | 9e-09 | 33/48 (NCI-H2347, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.66×** | +6.2 | 6e-08 | 34/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.67×** | +6.0 | 1e-07 | 37/47 (LoVo, BT-474, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.8 | 1e-04 | 26/46 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +4.6 | 3e-04 | 32/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +4.6 | 3e-04 | 25/47 (HOP62, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +4.4 | 5e-04 | 26/48 (NCI-H1792, SW 900, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.29×** | +3.6 | 0.014 | 19/48 (LoVo, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.020 | 20/48 (HT-29, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.31×** | +3.1 | 0.074 | 24/48 (NCI-H23, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13240.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.569×** | -9.7 | 1e-19 | 38/47 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -4.4 | 0.003 | 25/47 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.799×** | -3.9 | 0.020 | 18/48 (SW 900, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.3) |
| [[LoVo (line)]] | wt | 67.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 49.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -9.3) |
| [[SNU-1 (line)]] | wt | 29.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 7.34× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -12.0) |
| [[SW480 (line)]] | alt | 54.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -10.7) |
| [[A498 (line)]] | wt | 33.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +10.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 30.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 77.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.4) |
| [[A-172 (line)]] | wt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.65× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -14.1) |
| [[C-33 A (line)]] | alt | 38.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -17.8) |
| [[HT-29 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +9.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.2) |
| [[KATO III (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 36.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 46.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.20× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 46.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 31.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF7]] | +0.72 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[RNF4]] | +0.68 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[RPL29]] | +0.67 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[ADPGK]] | +0.65 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[APEX1]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[KATNB1]] | +0.63 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[QARS1]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CDC123]] | +0.62 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[DDX54]] | +0.62 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[IPO11]] | +0.62 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[EIF3L]] | +0.62 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ZDHHC7]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF674]] | -0.60 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[PIM3]] | -0.58 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[SERTAD1]] | -0.58 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[XIAP]] | -0.58 | -0.62 / -0.41 | both halves | 4e-05 | STRING 569 |
| [[IER5]] | -0.57 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[TUBB2A]] | -0.54 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[H3-3B]] | -0.54 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[MARCKS]] | -0.54 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[TMEM40]] | -0.54 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[GOLT1A]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[JUND]] | -0.53 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[PFN1]] | -0.53 | -0.54 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.3, -13.7); signed map (-42.0, -12.7). **Vector** length 64.7, 15.6% of its response variance represented; |z| ≥ 3 in 588 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +1.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.8 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +0.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | prohibitin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,965,327-6,970,780 (-) |
| Ensembl biotype | protein_coding |
| Also known as | REA, BCAP37, Bap37, p22 |
| Gene groups (HGNC) | Mitochondrial nucleoid associated proteins |
| Hallmark sets | MYC_TARGETS_V1, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Cellular response to mitochondrial stress; Processing of SMDT1; Mitochondrial calcium ion transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99623](https://www.uniprot.org/uniprotkb/Q99623) (Prohibitin-2):

> Protein with pleiotropic attributes mediated in a cell-compartment- and tissue-specific manner, which include the plasma membrane-associated cell signaling functions, mitochondrial chaperone, and transcriptional co-regulator of transcription factors and sex steroid hormones in the nucleus.; In the mitochondria, together with PHB1, forms large ring complexes (prohibitin complexes) in the inner mitochondrial membrane (IMM) and functions as a chaperone protein that stabilizes mitochondrial …

**Summary**, from NCBI Gene [11331](https://www.ncbi.nlm.nih.gov/gene/11331):

> Enables obsolete amide binding activity; protein dimerization activity; and sphingolipid binding activity. Involved in several processes, including RIG-I signaling pathway; antiviral innate immune response; and regulation of DNA-templated transcription. Located in several cellular components, including cell surface; mitochondrial membrane; and nuclear matrix. Part of mitochondrial prohibitin complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30306](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30306) · Entrez [11331](https://www.ncbi.nlm.nih.gov/gene/11331) · UniProt [Q99623](https://www.uniprot.org/uniprotkb/Q99623) · Ensembl [ENSG00000215021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215021)

## Data

Gene col 13240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13240); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13240]; `tensor/DDL_lfc|DDL_z.npy` [13240]; `embed/gene_vectors.npy` [13240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13240 or target_col == 13240). Every well: [[PHB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "STX10"
type: "gene"
col: 2524
ensembl_id: "ENSG00000104915"
name: "syntaxin 10"
location: "19p13.13"
module: 109
arm: "+"
pooled_cpm: 10.93
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# STX10

*syntaxin 10* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.42× (z +13.6, q 3e-39, up in 35 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.59× (z +5.1, q 3e-05, up in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (NCI-H460 7.43×, SNU-423 5.45×, A-172 4.60×, LoVo 3.47×, …; ⚠ cell-cycle shift, explains ~52% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 6.56×, A-427 5.23×, SW480 4.20×, A498 3.75×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 4.81×, LS 180 5.44×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.05 µM: 0.735× (z -4.6, q 0.002, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGL2]] (+0.66, fdr 7e-06), [[BCL2L12]] (+0.62, fdr 1e-05), [[PRX]] (+0.58, fdr 3e-05); moves opposite to [[SETMAR]] (-0.50, fdr 8e-05), [[MTERF3]] (-0.49, fdr 3e-05), [[POP1]] (-0.48, fdr 3e-05).
> It is in [[Module 109]], a single-armed module (immediate early).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2524.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (NCI-H460 7.43×, SNU-423 5.45×, A-172 4.60×, LoVo 3.47×, …; ⚠ cell-cycle shift, explains ~52% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (LoVo 6.56×, A-427 5.23×, SW480 4.20×, A498 3.75×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 4.81×, LS 180 5.44×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.42×** | +13.6 | 3e-39 | 35/39 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +12.3 | 4e-32 | 19/21 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.81×** | +9.3 | 2e-18 | 28/45 (NCI-H460, SNU-423, …) | top dose only | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +7.7 | 3e-12 | 23/27 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.63×** | +5.4 | 7e-06 | 28/42 (RPMI-7951, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +5.1 | 3e-05 | 22/46 (C-33 A, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.35×** | +3.4 | 0.065 | 16/46 (SNU-1, PANC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.71×** | +3.3 | 0.066 | 8/42 (J82, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2524.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | **0.735×** | -4.6 | 0.002 | 20/48 (NCI-H23, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.686×** | -3.8 | 0.034 | 12/47 (AsPC-1, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.696×** | -3.7 | 0.034 | 17/44 (NCI-H23, HCT15, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.703×** | -3.7 | 0.037 | 15/46 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.543×** | -3.4 | 0.081 | 12/46 (LoVo, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.732×** | -3.3 | 0.097 | 15/45 (NCI-H1573, C32, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.690× | -3.2 | 0.13 | 12/48 (NCI-H23, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 24.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 10.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +9.7) ⚠ cell-cycle shift, explains ~52% of this change | [[Temsirolimus (drug)]] 0.5 µM 0.0977× (z -11.0) |
| [[LoVo (line)]] | wt | 10.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.56× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 12.0 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +12.2) ⚠ cell-cycle shift, explains ~52% of this change | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.162× (z -8.5) |
| [[SW480 (line)]] | alt | 9.88 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 11.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +11.5) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[A498 (line)]] | wt | 12.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.81× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 6.66 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +8.7) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[LS 180 (line)]] | wt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.44× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +8.6) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[NCI-H460 (line)]] | wt | 8.75 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +16.7) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[Panc 03.27 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 9.33 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.7) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +10.1) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[A549 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGL2]] | +0.66 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[BCL2L12]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PRX]] | +0.58 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[EGR2]] | +0.57 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[SYT5]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ING1]] | +0.55 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[IER2]] | +0.53 | +0.54 / +0.44 | both halves | 3e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[GNL1]] | +0.53 | +0.58 / +0.38 | both halves | 6e-05 |  |
| [[DLG4]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[RGP1]] | +0.52 | +0.53 / +0.43 | both halves | 3e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[EGR1]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PLEKHO2]] | +0.52 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[TAF10]] | +0.52 | +0.63 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETMAR]] | -0.50 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[MTERF3]] | -0.49 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[POP1]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[ZNF142]] | -0.47 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[PA2G4]] | -0.47 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[TADA2A]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[NAA50]] | -0.47 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[PSMA1]] | -0.46 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[ADPGK]] | -0.45 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[DTD2]] | -0.45 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[STARD7]] | -0.45 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[ZBTB24]] | -0.44 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.6, -1.8); signed map (4.3, 29.3). **Vector** length 63.4, 11.0% of its response variance represented; |z| ≥ 3 in 690 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +6.5 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +7.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +0.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.5 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -0.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:13,144,058-13,150,383 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hsyn10, SYN10 |
| Gene groups (HGNC) | Syntaxins |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O60499](https://www.uniprot.org/uniprotkb/O60499) (Syntaxin-10):

> SNARE involved in vesicular transport from the late endosomes to the trans-Golgi network.

**Summary**, from NCBI Gene [8677](https://www.ncbi.nlm.nih.gov/gene/8677):

> This gene belongs to the syntaxin family and encodes a soluble N-ethylmaleimide sensitive factor attachment protein receptor (SNARE). The encoded protein is involved in docking and fusion events at the Golgi apparatus. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:11428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11428) · Entrez [8677](https://www.ncbi.nlm.nih.gov/gene/8677) · UniProt [O60499](https://www.uniprot.org/uniprotkb/O60499) · Ensembl [ENSG00000104915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104915)

## Data

Gene col 2524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2524); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2524]; `tensor/DDL_lfc|DDL_z.npy` [2524]; `embed/gene_vectors.npy` [2524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2524 or target_col == 2524). Every well: [[STX10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

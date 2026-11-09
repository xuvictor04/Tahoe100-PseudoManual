---
symbol: "STRIP1"
type: "gene"
col: 6676
ensembl_id: "ENSG00000143093"
name: "striatin interacting protein 1"
location: "1p13.3"
module: 46
arm: "+"
pooled_cpm: 25.82
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# STRIP1

*striatin interacting protein 1* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.06× (z +11.0, q 1e-25, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.443× (z -12.5, q 3e-33, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.764× (z -5.9, q 7e-07, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXW4]] (+0.59, fdr 4e-05), [[GGA3]] (+0.58, fdr 3e-05), [[DHX35]] (+0.56, fdr 3e-05); moves opposite to [[TNIK]] (-0.58, fdr 1e-05), [[HLTF]] (-0.55, fdr 3e-04), [[NDFIP2]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.06×** | +11.0 | 1e-25 | 46/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +10.6 | 9e-24 | 42/47 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +9.5 | 3e-19 | 36/46 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.77×** | +8.7 | 4e-16 | 37/47 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.55×** | +6.7 | 3e-09 | 38/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +6.4 | 1e-08 | 37/47 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +6.2 | 3e-08 | 34/48 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +5.8 | 6e-07 | 33/48 (PANC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +5.2 | 1e-05 | 28/48 (LS 180, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.6 | 2e-04 | 25/47 (A498, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.6 | 3e-04 | 23/48 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.8 | 0.007 | 18/47 (LoVo, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.021 | 16/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.085 | 17/47 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.095 | 13/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6676.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.443×** | -12.5 | 3e-33 | 36/44 (LoVo, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -9.8 | 3e-20 | 28/37 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.611×** | -7.0 | 5e-10 | 24/41 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.764×** | -5.9 | 7e-07 | 36/48 (A498, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.769×** | -4.0 | 0.006 | 22/48 (SW 1271, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **0.796×** | -3.4 | 0.067 | 12/47 (HEC-1-A, AN3 CA, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 29.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0976× (z -16.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 21.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.249× (z -9.6) |
| [[A498 (line)]] | wt | 23.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +20.3) | — |
| [[AN3 CA (line)]] | alt | 40.2 | 0 | 2 (1 ⚠) | — | [[Decitabine (drug)]] 0.05 µM 0.0972× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 24.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -10.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 29.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -12.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 20.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -11.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 27.2 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 68.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 22.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.7) | — |
| [[A549 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -11.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -11.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -13.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -13.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -9.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 28.7 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0565× (z -16.2) |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -12.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0775× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.376× (z -8.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 42.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0796× (z -14.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW4]] | +0.59 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[GGA3]] | +0.58 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[DHX35]] | +0.56 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[RNF146]] | +0.56 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[ZDHHC1]] | +0.55 | +0.50 / +0.36 | both halves | 1e-04 |  |
| [[STRN4]] | +0.55 | +0.62 / +0.35 | both halves | 1e-04 | same gene group; STRING 999 |
| [[SETD1B]] | +0.54 | +0.34 / +0.43 | both halves | 1e-04 |  |
| [[KMT2B]] | +0.53 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[IGHMBP2]] | +0.53 | +0.36 / +0.43 | both halves | 9e-05 |  |
| [[DDX59]] | +0.53 | +0.29 / +0.51 | both halves | 3e-04 |  |
| [[HOXD3]] | +0.52 | +0.32 / +0.43 | both halves | 2e-04 |  |
| [[ATF5]] | +0.52 | +0.34 / +0.43 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNIK]] | -0.58 | -0.50 / -0.49 | both halves | 1e-05 | STRING 486 |
| [[HLTF]] | -0.55 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[NDFIP2]] | -0.54 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[SYAP1]] | -0.53 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[ST3GAL5]] | -0.50 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[KHDRBS1]] | -0.48 | -0.28 / -0.32 | both halves | 3e-04 |  |
| [[NME7]] | -0.47 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[CALU]] | -0.47 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[OSBPL8]] | -0.47 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[TRA2B]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[RADX]] | -0.47 | -0.31 / -0.37 | both halves | 2e-04 |  |
| [[SMC5]] | -0.46 | -0.25 / -0.40 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.6, 16.1); signed map (0.8, -9.0). **Vector** length 63.1, 10.7% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.8 | +2.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | -0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.6 | +5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.7 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -5.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -2.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.1 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | striatin interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:110,031,577-110,074,641 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14743, KIAA1761, FAR11A; previously FAM40A |
| Gene groups (HGNC) | STRIPAK complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VSL9](https://www.uniprot.org/uniprotkb/Q5VSL9) (Striatin-interacting protein 1):

> Plays a role in the regulation of cell morphology and cytoskeletal organization. Required in the cortical actin filament dynamics and cell shape. Part of the striatin-interacting phosphatase and kinase (STRIPAK) complexes. STRIPAK complexes have critical roles in protein (de)phosphorylation and are regulators of multiple signaling pathways including Hippo, MAPK, nuclear receptor and cytoskeleton remodeling. Different types of STRIPAK complexes are involved in a variety of biological processes …

**Summary**, from NCBI Gene [85369](https://www.ncbi.nlm.nih.gov/gene/85369):

> This gene encodes a member of the striatin-interacting phosphatase and kinase complex, which is involved in localization of the Golgi body. The encoded protein participates in cytosketelal organization. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:25916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25916) · Entrez [85369](https://www.ncbi.nlm.nih.gov/gene/85369) · UniProt [Q5VSL9](https://www.uniprot.org/uniprotkb/Q5VSL9) · Ensembl [ENSG00000143093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143093)

## Data

Gene col 6676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6676); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6676]; `tensor/DDL_lfc|DDL_z.npy` [6676]; `embed/gene_vectors.npy` [6676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6676 or target_col == 6676). Every well: [[STRIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STRIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

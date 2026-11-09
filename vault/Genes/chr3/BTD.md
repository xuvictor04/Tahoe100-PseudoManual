---
symbol: "BTD"
type: "gene"
col: 9857
ensembl_id: "ENSG00000169814"
name: "biotinidase"
location: "3p25.1"
module: 93
arm: "+"
pooled_cpm: 22.5
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# BTD

*biotinidase* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.75× (z +16.9, q 0e+00, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.697× (z -7.6, q 1e-11, down in 28 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.709× (z -7.3, q 1e-10, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FSIP1]] (+0.60, fdr 1e-05), [[ARMH4]] (+0.56, fdr 1e-05), [[AVIL]] (+0.50, fdr 1e-05); moves opposite to [[ZNG1C]] (-0.53, fdr 2e-05), [[C8orf76]] (-0.48, fdr 6e-05), [[SVIL-AS1-1]] (-0.46, fdr 8e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLRC4-KLRK1]], [[KLRK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9857.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +16.9 | 0e+00 | 36/47 (NCI-H1792, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +15.5 | 0e+00 | 33/46 (Hs 766T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +11.8 | 6e-30 | 43/48 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +10.4 | 4e-23 | 40/48 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +10.2 | 2e-22 | 28/41 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +9.1 | 1e-17 | 31/48 (HEC-1-A, HS-578T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +8.8 | 9e-17 | 19/32 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.35×** | +6.4 | 1e-08 | 22/48 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +5.0 | 3e-05 | 17/48 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.7 | 2e-04 | 16/48 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +4.6 | 2e-04 | 17/48 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 2e-04 | 16/48 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.003 | 11/45 (SW48, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.20×** | +3.9 | 0.004 | 17/46 (LS 180, MIA PaCa-2, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.20× | +3.9 | 0.004 | 2/48 (LoVo, NCI-H1792) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9857.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.697×** | -7.6 | 1e-11 | 28/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.709×** | -7.3 | 1e-10 | 24/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.713×** | -7.1 | 2e-10 | 24/47 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.762×** | -5.7 | 1e-06 | 20/47 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.777×** | -5.3 | 1e-05 | 22/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Ritonavir (drug)]] 0.5 µM |  | **0.814×** | -4.3 | 0.001 | 11/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.751×** | -4.3 | 0.001 | 8/48 (HOP62, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.815×** | -4.3 | 0.001 | 16/48 (NCI-H23, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.816×** | -4.3 | 0.001 | 13/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.822×** | -4.1 | 0.002 | 17/47 (SW480, SW 1271, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.831×** | -3.9 | 0.005 | 16/47 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.706×** | -3.8 | 0.006 | 7/48 (RPMI-7951, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.839× | -3.4 | 0.025 | 13/46 (HCT15, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Cyclosporin A (drug)]] 5 µM |  | 0.850× | -3.4 | 0.025 | 5/48 (AsPC-1, A498, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.893× | -3.4 | 0.029 | 13/48 (NCI-H460, CHP-212, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.854× | -3.3 | 0.031 | 17/47 (A-427, SHP-77, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.763×** | -3.0 | 0.089 | 10/46 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | 0.869× | -3.0 | 0.089 | 12/47 (SK-MEL-2, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 15.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +17.1) | — |
| [[A-427 (line)]] | wt | 27.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -12.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 19.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 14.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +17.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +13.6) | — |
| [[A498 (line)]] | wt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.1) | — |
| [[A549 (line)]] | wt | 20.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.69× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +13.2) | — |
| [[H4 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0715× (z -13.5) ⚠ cell-cycle shift, explains ~13% of this change |
| [[HEC-1-A (line)]] | alt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +16.8) | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +12.9) | — |
| [[NCI-H1792 (line)]] | alt | 32.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +20.8) | — |
| [[NCI-H2030 (line)]] | alt | 28.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 31.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[SK-MEL-2 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0947× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[SW480 (line)]] | alt | 31.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.345× (z -11.0) |
| [[A-172 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FSIP1]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ARMH4]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[AVIL]] | +0.50 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[FAM222A]] | +0.50 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CSMD1]] | +0.49 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[CTNNB1]] | +0.49 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[ABCA10]] | +0.49 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[IQCN]] | +0.48 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[EFCAB10]] | +0.48 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[ACBD7]] | +0.48 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[CRIM1]] | +0.48 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[ASXL1]] | +0.48 | +0.50 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNG1C]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[C8orf76]] | -0.48 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[SVIL-AS1-1]] | -0.46 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[NCLN]] | -0.46 | -0.58 / -0.29 | both halves | 2e-04 |  |
| [[R3HCC1L]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[MTFMT]] | -0.45 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[BAK1]] | -0.44 | -0.56 / -0.26 | both halves | 3e-04 |  |
| [[ZNF133]] | -0.43 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[ZNF680]] | -0.43 | -0.25 / -0.35 | both halves | 4e-04 |  |
| [[MRPL52]] | -0.42 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[ZUP1]] | -0.42 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[ANKS6]] | -0.42 | -0.50 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRC4-KLRK1]], [[KLRK1]] | B | KLRC4-KLRK1, KLRK1 activity weakens BTD's drug response | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1 respond 1.25× as strongly (z diff -0.42); strongest at Idarubicin (hydrochloride) 5 µM: 1.78x vs 1.32x (z diff -2.6) | 0.081 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; target measured in part of the lines; artifact flags; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.449). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.0, -30.3); signed map (14.8, -1.2). **Vector** length 79.3, 14.6% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change | +3.6 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +4.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -7.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.4 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | biotinidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:15,601,341-15,722,311 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Vanin family |
| Reactome | 6 pathways, smallest: Defects in biotin (Btn) metabolism; Biotin transport and metabolism; Defects in vitamin and cofactor metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P43251](https://www.uniprot.org/uniprotkb/P43251) (Biotinidase):

> Catalytic release of biotin from biocytin, the product of biotin-dependent carboxylases degradation.

**Summary**, from NCBI Gene [686](https://www.ncbi.nlm.nih.gov/gene/686):

> The protein encoded by this gene functions to recycle protein-bound biotin by cleaving biocytin (biotin-epsilon-lysine), a normal product of carboxylase degradation, resulting in regeneration of free biotin. The encoded protein has also been shown to have biotinyl transferase activity. Mutations in this gene are associated with biotinidase deficiency. Multiple transcript variants encoding different isoforms have been described. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:1122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1122) · Entrez [686](https://www.ncbi.nlm.nih.gov/gene/686) · UniProt [P43251](https://www.uniprot.org/uniprotkb/P43251) · Ensembl [ENSG00000169814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169814)

## Data

Gene col 9857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9857); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9857]; `tensor/DDL_lfc|DDL_z.npy` [9857]; `embed/gene_vectors.npy` [9857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9857 or target_col == 9857). Every well: [[BTD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "PRMT5-DT"
type: "gene"
col: 15030
ensembl_id: "ENSG00000257285"
name: "PRMT5 divergent transcript"
location: "14q11.2"
module: 21
arm: "+"
pooled_cpm: 3.02
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 2
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PRMT5-DT

*PRMT5 divergent transcript* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 8.33× (z +21.8, q 0e+00, up in 14 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 7.92× (z +21.3, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.604× (z -5.2, q 1e-04, down in 16 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 5 µM in 1 line (BT-474 0.0468×); [[Harringtonine (drug)]] 5 µM in 1 line (COLO 205 0.0656×; ⚠ cell-cycle shift, explains ~0% of this change); [[Gemfibrozil (drug)]] 0.5 µM in 1 line (LS 180 0.0675×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB14-AS1]] (+0.61, fdr 3e-05), [[ABHD8]] (+0.59, fdr 2e-05), [[MARCHF6]] (+0.56, fdr 1e-04); moves opposite to [[CHAMP1]] (-0.54, fdr 1e-04), [[ADO]] (-0.53, fdr 2e-04), [[TRMT5]] (-0.51, fdr 1e-03, ⚠ one half only (not replicated)), [[RRP8]] (-0.51, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.33×** | +21.8 | 0e+00 | 14/15 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **7.92×** | +21.3 | 0e+00 | 46/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.26×** | +20.9 | 0e+00 | 3/3 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **6.20×** | +18.8 | 0e+00 | 43/45 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **7.08×** | +18.6 | 0e+00 | 3/4 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.05×** | +18.5 | 0e+00 | 43/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.30×** | +17.3 | 0e+00 | 31/33 (CFPAC-1, SW480, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.39×** | +9.0 | 2e-17 | 27/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.32×** | +8.7 | 3e-16 | 24/42 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +7.5 | 3e-12 | 14/33 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.82×** | +6.2 | 4e-08 | 17/41 (CFPAC-1, NCI-H2030, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.77×** | +5.9 | 2e-07 | 13/35 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +5.3 | 4e-06 | 15/43 (CFPAC-1, PANC-1, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.4 | 4e-04 | 5/18 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.4 | 4e-04 | 7/22 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +4.3 | 7e-04 | 9/41 (CFPAC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +4.2 | 1e-03 | 7/44 (HOP62, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.004 | 8/27 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.94×** | +3.6 | 0.010 | 5/41 (SW480, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.039 | 3/39 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15030.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 5 µM in 1 line (BT-474 0.0468×); [[Harringtonine (drug)]] 5 µM in 1 line (COLO 205 0.0656×; ⚠ cell-cycle shift, explains ~0% of this change); [[Gemfibrozil (drug)]] 0.5 µM in 1 line (LS 180 0.0675×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.604×** | -5.2 | 1e-04 | 16/45 (A-427, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.685×** | -3.6 | 0.091 | 12/30 (HEC-1-A, A-427, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.02 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.2× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 6.08× (z +8.5) | — |
| [[SW480 (line)]] | alt | 4.00 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.7× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 2.26 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 20.4× (z +9.9) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 13.8× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 4.70 | 0 | 1 | — | [[Pimozide (drug)]] 5 µM 0.0468× (z -9.3) |
| [[COLO 205 (line)]] | alt | 7.42 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0656× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 3.07 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.5 µM 0.0675× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 4.36 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.8× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB14-AS1]] | +0.61 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[ABHD8]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[MARCHF6]] | +0.56 | +0.35 / +0.41 | both halves | 1e-04 |  |
| [[KIZ-AS1]] ⚠ | +0.55 | +0.48 / +0.51 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GEMIN7-AS1]] | +0.55 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[CRELD1]] | +0.55 | +0.28 / +0.55 | both halves | 3e-04 |  |
| [[SLC16A13]] | +0.54 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CCDC183]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[HCG25]] | +0.54 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[MYO18B]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[LRRC75A]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[CCDC39]] | +0.53 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[SLIT1]] | +0.53 | +0.43 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHAMP1]] | -0.54 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[ADO]] | -0.53 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[TRMT5]] | -0.51 | -0.18 / -0.55 | ⚠ one half (not replicated) | 1e-03 |  |
| [[RRP8]] | -0.51 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[ZNF816]] | -0.51 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[ZNF564]] | -0.50 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[CMTR2]] | -0.49 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[RPL7L1]] | -0.49 | -0.18 / -0.45 | ⚠ not reproduced | 9e-04 |  |
| [[NOL11]] | -0.48 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[UTP3]] | -0.47 | -0.20 / -0.45 | both halves | 7e-04 |  |
| [[ZNF614]] | -0.47 | -0.14 / -0.51 | ⚠ one half (not replicated) | 0.002 |  |
| [[ZBTB33]] | -0.47 | -0.21 / -0.45 | both halves | 6e-04 |  |
| [[OBI1]] | -0.46 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[UTP15]] | -0.46 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[CCDC137]] | -0.46 | -0.21 / -0.44 | both halves | 6e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.7, -11.0); signed map (-31.2, -2.6). **Vector** length 53.1, 6.82% of its response variance represented; |z| ≥ 3 in 1,086 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +20.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +21.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +18.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +21.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +18.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +6.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -0.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | PRMT5 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q11.2 — chr14:22,929,607-22,956,436 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55482](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55482) · Entrez [101926933](https://www.ncbi.nlm.nih.gov/gene/101926933) · Ensembl [ENSG00000257285](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257285)

## Data

Gene col 15030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15030); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15030]; `tensor/DDL_lfc|DDL_z.npy` [15030]; `embed/gene_vectors.npy` [15030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15030 or target_col == 15030). Every well: [[PRMT5-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRMT5-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

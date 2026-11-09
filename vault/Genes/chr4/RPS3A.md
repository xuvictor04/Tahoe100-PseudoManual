---
symbol: "RPS3A"
type: "gene"
col: 6991
ensembl_id: "ENSG00000145425"
name: "ribosomal protein S3A"
location: "4q31.3"
module: 20
arm: "+"
pooled_cpm: 46.18
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RPS3A

*ribosomal protein S3A* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.39× (z +11.3, q 7e-27, up in 41 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.21× (z +9.7, q 3e-20, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.624× (z -6.1, q 7e-07, down in 43 of 48 measured lines) ⚠ unreliable plate only; position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.246×, C-33 A 0.346×, AN3 CA 0.279×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.354×; ⚠ cell-cycle shift, explains ~29% of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (Hs 766T 0.174×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL6]] (+0.89, fdr 7e-06), [[RPS18]] (+0.80, fdr 7e-06), [[RPL14]] (+0.78, fdr 7e-06); moves opposite to [[ZNF503]] (-0.62, fdr 1e-05), [[NUDT16L1]] (-0.61, fdr 1e-05), [[YIF1A]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6991.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.39×** | +11.3 | 7e-27 | 41/46 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +10.7 | 4e-24 | 36/41 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.30×** | +10.4 | 4e-23 | 44/47 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.21×** | +9.7 | 3e-20 | 47/49 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **4.11×** | +9.6 | 1e-19 | 42/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +9.0 | 2e-17 | 42/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +8.8 | 1e-16 | 39/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +7.1 | 8e-11 | 36/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +6.4 | 8e-09 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +6.1 | 4e-08 | 32/46 (RKO, KATO III, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +6.0 | 7e-08 | 35/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +6.0 | 1e-07 | 42/48 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +5.3 | 6e-06 | 25/35 (HT-29, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.9 | 4e-05 | 28/48 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.8 | 5e-05 | 26/50 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 7e-04 | 26/48 (KATO III, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +4.1 | 0.002 | 28/48 (Hs 766T, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.002 | 19/48 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.006 | 22/48 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.007 | 23/48 (NCI-H2347, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.037 | 15/48 (PANC-1, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.045 | 18/48 (MIA PaCa-2, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6991.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.246×, C-33 A 0.346×, AN3 CA 0.279×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.354×; ⚠ cell-cycle shift, explains ~29% of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (Hs 766T 0.174×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.624×** | -6.1 | 7e-07 | 43/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.728×** | -4.1 | 0.013 | 30/48 (A-427, AN3 CA, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.783× | -3.1 | 0.28 | 15/48 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[Sacubitril_Valsartan (drug)]] 5 µM |  | 0.778× | -3.1 | 0.28 | 19/48 (A498, NCI-H23, …) | top dose only | position effect removed |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.789× | -3.0 | 0.28 | 11/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6991. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 60.1 | 10 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 48.6 | 9 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.02× (z +11.1) | — |
| [[LoVo (line)]] | wt | 62.1 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 44.4 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 56.6 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 45.2 | 4 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.45× (z +10.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +9.1) | — |
| [[KATO III (line)]] | alt | 39.8 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.85× (z +12.0) | — |
| [[A-427 (line)]] | wt | 53.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -16.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 43.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +10.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 26.6 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.15× (z +9.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.73× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 33.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +8.5) | — |
| [[RKO (line)]] | wt | 65.3 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.62× (z +10.9) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 7.69× (z +9.4) | — |
| [[A498 (line)]] | wt | 43.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 61.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 67.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 46.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +8.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 31.1 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.174× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 34.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 66.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +9.6) | — |
| [[A-172 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 81.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6991), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL6]] | +0.89 | +0.84 / +0.91 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS18]] | +0.80 | +0.80 / +0.79 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL14]] | +0.78 | +0.78 / +0.74 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS7]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL10]] | +0.76 | +0.70 / +0.76 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPSA]] | +0.76 | +0.68 / +0.80 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL3]] | +0.74 | +0.77 / +0.76 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL4]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL18A]] | +0.73 | +0.65 / +0.75 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[EEF1A1]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 997 |
| [[EEF1A1P5]] | +0.70 | +0.63 / +0.73 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation |
| [[SMG1P1]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF503]] | -0.62 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[NUDT16L1]] | -0.61 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[YIF1A]] | -0.61 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[ERVK3-1]] | -0.60 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[H3-3B]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[C14orf119]] | -0.59 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[TIMM17B]] ⚠ | -0.59 | -0.52 / -0.59 | both halves | 1e-05 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[TOPORS]] | -0.59 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[TUBB4B]] | -0.58 | -0.51 / -0.59 | both halves | 1e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[CDKN2AIP]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[INAFM1]] | -0.56 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[LRRC8E]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.689). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.8, -25.6); signed map (-22.2, -34.3). **Vector** length 91.0, 25.3% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +11.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +9.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | -1.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -6.0 | +1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +1.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.3 | -1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[DT-061 (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:151,099,624-151,104,642 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S3A, eS1; previously MFTL |
| Gene groups (HGNC) | S ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P61247](https://www.uniprot.org/uniprotkb/P61247) (Small ribosomal subunit protein eS1):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [6189](https://www.ncbi.nlm.nih.gov/gene/6189):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S3AE family of ribosomal proteins. It is located in the cytoplasm. Disruption of the gene encoding rat ribosomal protein S3a, also named v-fos transformation effector …

**Accessions** — [HGNC:10421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10421) · Entrez [6189](https://www.ncbi.nlm.nih.gov/gene/6189) · UniProt [P61247](https://www.uniprot.org/uniprotkb/P61247) · Ensembl [ENSG00000145425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145425)

## Data

Gene col 6991: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6991); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6991, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6991]; `tensor/DDL_lfc|DDL_z.npy` [6991]; `embed/gene_vectors.npy` [6991]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6991 or target_col == 6991). Every well: [[RPS3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

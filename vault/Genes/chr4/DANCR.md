---
symbol: "DANCR"
type: "gene"
col: 13562
ensembl_id: "ENSG00000226950"
name: "differentiation antagonizing non-protein coding RNA"
location: "4q12"
module: 25
arm: "+"
pooled_cpm: 18.01
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# DANCR

*differentiation antagonizing non-protein coding RNA* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.02× (z +18.0, q 0e+00, up in 41 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.95× (z +10.6, q 5e-24, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.315×; ⚠ cell-cycle shift, explains ~52% of this change); [[Cabozantinib (S-malate) (drug)]] 0.05 µM in 1 line (NCI-H661 0.0552×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS10-NUDT3]] (+0.57, fdr 4e-05), [[ARL5A]] (+0.56, fdr 8e-05), [[ZNF117]] (+0.54, fdr 2e-04); moves opposite to [[LENG1]] (-0.62, fdr 4e-05), [[CDKN2AIP]] (-0.58, fdr 3e-05), [[H3-3B]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.02×** | +18.0 | 0e+00 | 41/41 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.96×** | +14.8 | 0e+00 | 28/31 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.39×** | +13.1 | 4e-37 | 44/45 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.35×** | +12.2 | 2e-32 | 35/36 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.95×** | +10.6 | 5e-24 | 40/48 (NCI-H460, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +8.8 | 1e-16 | 40/45 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.12×** | +8.4 | 5e-15 | 42/46 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.80×** | +6.6 | 3e-09 | 33/48 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.71×** | +6.0 | 1e-07 | 31/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.75×** | +5.9 | 2e-07 | 16/25 (C32, NCI-H1573, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.63×** | +5.7 | 8e-07 | 35/46 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.42×** | +5.6 | 1e-06 | 26/47 (A498, HOP62, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.62×** | +5.4 | 3e-06 | 30/46 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +4.5 | 3e-04 | 26/46 (SK-MEL-2, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +4.5 | 3e-04 | 23/47 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 7e-04 | 20/47 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.70×** | +4.2 | 8e-04 | 23/47 (NCI-H23, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.00×** | +4.0 | 0.002 | 21/47 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.90×** | +3.7 | 0.006 | 14/46 (A498, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.006 | 15/46 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.010 | 20/47 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.011 | 14/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.77×** | +3.3 | 0.019 | 14/46 (NCI-H1792, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.71×** | +3.1 | 0.037 | 14/45 (NCI-H460, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.046 | 8/46 (Panc 03.27, SW 900, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.053 | 15/46 (AN3 CA, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.66×** | +3.0 | 0.058 | 9/44 (NCI-H23, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13562.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.315×; ⚠ cell-cycle shift, explains ~52% of this change); [[Cabozantinib (S-malate) (drug)]] 0.05 µM in 1 line (NCI-H661 0.0552×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.731× | -3.4 | 0.41 | 14/47 (BT-474, SW1417, …) | top dose only | plate-row cell shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.759× | -3.1 | 0.52 | 10/47 (KATO III, HS-578T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 28.3 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.87× (z +14.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 25.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.72× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 39.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 9.90 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.49× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 21.7 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.48× (z +10.9) ⚠ toxic | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 6.37× (z +12.1) ⚠ toxic | — |
| [[C32 (line)]] | wt | 39.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.88× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 28.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.01× (z +11.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.57× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 12.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.13× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 8.60 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +8.7) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[A498 (line)]] | wt | 12.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +11.4) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[C-33 A (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.05× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.30× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 34.6 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.05 µM 0.0552× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 11.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.88× (z +9.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 6.20 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.21× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SHP-77 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.60× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.66× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS10-NUDT3]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[ARL5A]] | +0.56 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[ZNF117]] | +0.54 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[MRPS25]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ECI1]] | +0.53 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[RCC1]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[TMEM64]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[CTTN-DT]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[CPSF6]] | +0.50 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[ABHD14B]] | +0.49 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[SMG1P1]] | +0.49 | +0.32 / +0.47 | both halves | 2e-04 |  |
| [[PABPC4]] | +0.49 | +0.44 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LENG1]] | -0.62 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[CDKN2AIP]] | -0.58 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[H3-3B]] | -0.54 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[FADD]] | -0.53 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[SETX]] | -0.52 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[POLD4]] | -0.48 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[ZNF184]] | -0.48 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[ADRM1]] | -0.46 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[DDX24]] | -0.46 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[TINF2]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[STYXL1]] | -0.45 | -0.24 / -0.54 | both halves | 4e-04 |  |
| [[MEA1]] | -0.45 | -0.39 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.162). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.7, 21.2); signed map (-0.8, -59.0). **Vector** length 74.8, 15.8% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +8.1 | +10.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.9 | +13.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +4.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.4 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +12.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +3.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.1 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | +1.0 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | differentiation antagonizing non-protein coding RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q12 — chr4:52,712,325-52,723,623 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ANCR, AGU2, lncRNA-ANCR; previously KIAA0114, SNHG13 |
| Gene groups (HGNC) | MicroRNA non-coding host genes; Small nucleolar RNA non-coding host genes; Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

UniProt [P0C864](https://www.uniprot.org/uniprotkb/P0C864) carries no function annotation.

**Summary**, from NCBI Gene [57291](https://www.ncbi.nlm.nih.gov/gene/57291):

> This gene produces a long non-coding RNA that functions as a negative regulator of cell differentiation. This transcript associates with enhancer of zeste homolog 2 to repress expression of the runt related transcription factor 2 gene. Increased expression of this transcript may be associated with cancer. Alternatively spliced transcript variants have been observed. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:28964](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28964) · Entrez [57291](https://www.ncbi.nlm.nih.gov/gene/57291) · UniProt [P0C864](https://www.uniprot.org/uniprotkb/P0C864) · Ensembl [ENSG00000226950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226950)

## Data

Gene col 13562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13562); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13562]; `tensor/DDL_lfc|DDL_z.npy` [13562]; `embed/gene_vectors.npy` [13562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13562 or target_col == 13562). Every well: [[DANCR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DANCR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "SIAH2"
type: "gene"
col: 11211
ensembl_id: "ENSG00000181788"
name: "siah E3 ubiquitin protein ligase 2"
location: "3q25.1"
module: 56
arm: "+"
pooled_cpm: 33.98
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SIAH2

*siah E3 ubiquitin protein ligase 2* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.54× (z +16.7, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.402× (z -17.8, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPT2]] (+0.68, fdr 7e-06), [[ALKBH5]] (+0.68, fdr 7e-06), [[GORASP2]] (+0.65, fdr 2e-05); moves opposite to [[TIA1]] (-0.60, fdr 2e-05), [[VPS35L]] (-0.60, fdr 1e-05), [[ATRX]] (-0.57, fdr 2e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11211.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.54×** | +16.7 | 0e+00 | 47/49 (NCI-H460, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +6.2 | 2e-07 | 26/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +4.5 | 0.001 | 20/47 (NCI-H2347, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.62×** | +4.0 | 0.009 | 20/47 (HT-29, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +3.7 | 0.020 | 18/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +3.3 | 0.082 | 14/48 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | 1.46× | +3.1 | 0.14 | 10/48 (CFPAC-1, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11211.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.402×** | -17.8 | 0e+00 | 43/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.474×** | -11.3 | 2e-27 | 28/37 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.506×** | -10.1 | 1e-21 | 29/44 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.530×** | -10.0 | 2e-21 | 33/47 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.532×** | -9.6 | 9e-20 | 32/47 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.699×** | -5.7 | 1e-06 | 23/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.701×** | -5.6 | 2e-06 | 25/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.768×** | -5.5 | 3e-06 | 31/48 (SW1417, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.719×** | -5.2 | 1e-05 | 29/48 (A498, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.726×** | -5.1 | 2e-05 | 21/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.723×** | -4.9 | 4e-05 | 23/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.755×** | -4.5 | 4e-04 | 22/48 (NCI-H23, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.747×** | -4.3 | 7e-04 | 21/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.773×** | -3.8 | 0.005 | 14/47 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.787×** | -3.5 | 0.017 | 19/47 (SW1417, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.802×** | -3.5 | 0.017 | 16/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.802×** | -3.3 | 0.032 | 20/47 (A-427, LoVo, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 40.4 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -17.9) |
| [[HT-29 (line)]] | alt | 89.2 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -18.0) |
| [[LoVo (line)]] | wt | 37.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -13.8) |
| [[PANC-1 (line)]] | alt | 35.5 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.52× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -18.8) |
| [[KATO III (line)]] | alt | 40.5 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.259× (z -14.3) |
| [[NCI-H2347 (line)]] | alt | 42.4 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.01× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -16.2) |
| [[SW480 (line)]] | alt | 26.1 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.76× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.6) |
| [[A-427 (line)]] | wt | 60.5 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.72× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0922× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.258× (z -15.4) |
| [[HepG2_C3A (line)]] | wt | 48.1 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.2× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.247× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.338× (z -8.8) |
| [[HS-578T (line)]] | alt | 50.1 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.54× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.317× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -11.0) |
| [[RKO (line)]] | wt | 26.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0498× (z -18.3) |
| [[C32 (line)]] | wt | 17.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 23.8× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -9.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 36.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -9.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 37.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.305× (z -8.8) |
| [[Hs 766T (line)]] | wt | 23.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[OTS514 (drug)]] 5 µM 0.0600× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 22.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 38.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 27.4 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 12.8× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 17.1 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 19.4× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 24.6 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 17.8× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -13.5) |
| [[SNU-1 (line)]] | wt | 38.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -14.2) |
| [[SW48 (line)]] | wt | 43.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.335× (z -8.5) |
| [[A549 (line)]] | wt | 23.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.8× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.2) |
| [[BT-474 (line)]] | alt | 25.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 31.9× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 49.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.50× (z +8.5) | — |
| [[H4 (line)]] | wt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -13.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.7) |
| [[HOP62 (line)]] | alt | 29.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.99× (z +8.7) | — |
| [[J82 (line)]] | alt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.5) |
| [[LS 180 (line)]] | wt | 42.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 41.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.248× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 22.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.1× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0879× (z -11.0) ⚠ toxic |
| [[SW1417 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPT2]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[ALKBH5]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[GORASP2]] | +0.65 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[GARS1]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[TXNDC11]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[SLC31A1]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MED26]] | +0.62 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[EIF4EBP1]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[TRIB3]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[IER3IP1]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[CSNK2A1]] | +0.61 | +0.68 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.60 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[VPS35L]] | -0.60 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[ATRX]] | -0.57 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[BAZ2B]] | -0.57 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[YTHDC2]] | -0.56 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ATXN10]] | -0.56 | -0.64 / -0.31 | both halves | 2e-04 |  |
| [[ERCC6L2]] | -0.55 | -0.64 / -0.34 | both halves | 1e-04 |  |
| [[ZNF280D]] | -0.54 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[C11orf58]] | -0.54 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[EIF2B5]] | -0.54 | -0.62 / -0.36 | both halves | 9e-05 |  |
| [[CACNA2D1]] | -0.53 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[CPLANE1]] | -0.53 | -0.55 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.1, -30.5); signed map (-43.3, 16.0). **Vector** length 120, 32.8% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.6 | +16.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.9 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -17.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -9.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.6 | -5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -10.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.4 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -3.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.3 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | siah E3 ubiquitin protein ligase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:150,741,125-150,763,477 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, HYPOXIA, ESTROGEN_RESPONSE_EARLY |
| Reactome | 9 pathways, smallest: Netrin-1 signaling; Amyloid fiber formation; Ub-specific processing proteases |
| Matched by | ensembl_id |

**Function**, from UniProt [O43255](https://www.uniprot.org/uniprotkb/O43255) (E3 ubiquitin-protein ligase SIAH2):

> E3 ubiquitin-protein ligase that mediates ubiquitination and subsequent proteasomal degradation of target proteins. E3 ubiquitin ligases accept ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Mediates E3 ubiquitin ligase activity either through direct binding to substrates or by functioning as the essential RING domain subunit of larger E3 complexes. Triggers the ubiquitin-mediated degradation of many …

**Summary**, from NCBI Gene [6478](https://www.ncbi.nlm.nih.gov/gene/6478):

> This gene encodes a protein that is a member of the seven in absentia homolog (SIAH) family. The protein is an E3 ligase and is involved in ubiquitination and proteasome-mediated degradation of specific proteins. The activity of this ubiquitin ligase has been implicated in regulating cellular response to hypoxia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10858) · Entrez [6478](https://www.ncbi.nlm.nih.gov/gene/6478) · UniProt [O43255](https://www.uniprot.org/uniprotkb/O43255) · Ensembl [ENSG00000181788](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181788)

## Data

Gene col 11211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11211); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11211]; `tensor/DDL_lfc|DDL_z.npy` [11211]; `embed/gene_vectors.npy` [11211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11211 or target_col == 11211). Every well: [[SIAH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIAH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

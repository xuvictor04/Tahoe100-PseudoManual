---
symbol: "LMBR1L"
type: "gene"
col: 6326
ensembl_id: "ENSG00000139636"
name: "limb development membrane protein 1 like"
location: "12q13.12"
module: 76
arm: "+"
pooled_cpm: 21.45
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# LMBR1L

*limb development membrane protein 1 like* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.26× (z +5.4, q 4e-05, up in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.30× (z +4.6, q 0.001, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.345× (z -18.8, q 0e+00, down in 40 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.487× (z -12.7, q 9e-35, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCD4]] (+0.77, fdr 7e-06), [[TSC22D4]] (+0.75, fdr 7e-06), [[HINFP]] (+0.74, fdr 7e-06); moves opposite to [[TRIM44]] (-0.74, fdr 7e-06), [[ANAPC7]] (-0.71, fdr 7e-06), [[ABCE1]] (-0.71, fdr 7e-06).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6326.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.26×** | +5.4 | 4e-05 | 25/48 (J82, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 0.001 | 19/47 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.25×** | +3.9 | 0.022 | 12/48 (RKO, J82, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | 1.41× | +3.2 | 0.23 | 8/46 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6326.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.345×** | -18.8 | 0e+00 | 40/42 (hTERT-HPNE, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.449×** | -13.6 | 1e-39 | 32/34 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.487×** | -12.7 | 9e-35 | 32/47 (NCI-H1573, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.519×** | -10.7 | 9e-25 | 28/39 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.557×** | -10.4 | 4e-23 | 36/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.638×** | -8.0 | 2e-13 | 34/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.679×** | -6.9 | 5e-10 | 24/48 (NCI-H460, C32, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.775×** | -6.2 | 5e-08 | 25/48 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.520×** | -6.0 | 9e-08 | 28/47 (LoVo, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.717×** | -5.7 | 8e-07 | 22/48 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.553×** | -5.5 | 2e-06 | 20/47 (SNU-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.798×** | -5.5 | 2e-06 | 25/48 (SNU-423, HCT15, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.728×** | -5.4 | 3e-06 | 24/48 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.591×** | -4.9 | 5e-05 | 20/47 (LoVo, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.833×** | -4.4 | 4e-04 | 19/48 (CFPAC-1, SW1417, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.635×** | -4.2 | 9e-04 | 19/47 (CFPAC-1, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.645×** | -4.1 | 0.002 | 16/48 (SNU-423, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.650×** | -4.0 | 0.002 | 13/48 (NCI-H1792, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.754×** | -3.6 | 0.009 | 9/48 (NCI-H2347, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.818×** | -3.6 | 0.009 | 14/48 (CHP-212, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.819×** | -3.6 | 0.009 | 13/48 (RPMI-7951, HCT15, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.866× | -3.4 | 0.015 | 9/48 (MIA PaCa-2, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6326. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 28.2 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 28.7 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0993× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -9.5) |
| [[SNU-423 (line)]] | alt | 41.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0844× (z -25.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -10.2) |
| [[HCT15 (line)]] | alt | 34.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -11.9) |
| [[HOP62 (line)]] | alt | 24.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -9.0) |
| [[LoVo (line)]] | wt | 25.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -8.5) |
| [[A498 (line)]] | wt | 15.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 44.3 | 0 | 2 (1 ⚠) | — | [[Roxadustat (drug)]] 0.05 µM 0.0735× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 16.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 15.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 18.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.375× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 30.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0388× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 18.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 27.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0709× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 24.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0724× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 29.3 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.106× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -13.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -8.5) |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.131× (z -8.7) |
| [[SW480 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6326), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCD4]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[TSC22D4]] | +0.75 | +0.73 / +0.84 | both halves | 7e-06 |  |
| [[HINFP]] | +0.74 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[KLHL7]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[VPS37D]] | +0.74 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[AAMDC]] | +0.72 | +0.51 / +0.78 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.72 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[LINC00674]] | +0.71 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.70 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.68 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[KLHDC3]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM44]] | -0.74 | -0.71 / -0.69 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.71 | -0.66 / -0.72 | both halves | 7e-06 |  |
| [[ABCE1]] | -0.71 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.68 | -0.63 / -0.66 | both halves | 7e-06 |  |
| [[CPSF2]] | -0.68 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[NAA15]] | -0.67 | -0.57 / -0.75 | both halves | 1e-05 |  |
| [[UTP20]] | -0.66 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.66 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[TASOR]] | -0.66 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[SNX19]] | -0.66 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[COMMD10]] | -0.66 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[SRCAP]] | -0.65 | -0.63 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.9, -15.6); signed map (-33.8, 13.4). **Vector** length 101, 23.6% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.0 | +5.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +2.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +3.5 | +3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +1.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -12.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.6 | -10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -5.0 | -10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -4.8 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -6.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.1 | -6.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -5.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | limb development membrane protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,097,136-49,110,900 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIMR, FLJ10494, KIAA1174 |
| Gene groups (HGNC) | LMBR family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UX01](https://www.uniprot.org/uniprotkb/Q6UX01) (Protein LMBR1L):

> Plays an essential role in lymphocyte development by negatively regulating the canonical Wnt signaling pathway (By similarity). In association with UBAC2 and E3 ubiquitin-protein ligase AMFR, promotes the ubiquitin-mediated degradation of CTNNB1 and Wnt receptors FZD6 and LRP6 (By similarity). LMBR1L stabilizes the beta-catenin destruction complex that is required for regulating CTNNB1 levels (By similarity). Acts as a LCN1 receptor and can mediate its endocytosis.

**Summary**, from NCBI Gene [55716](https://www.ncbi.nlm.nih.gov/gene/55716):

> Enables transmembrane signaling receptor activity. Involved in receptor-mediated endocytosis and signal transduction. Located in endoplasmic reticulum membrane and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18268](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18268) · Entrez [55716](https://www.ncbi.nlm.nih.gov/gene/55716) · UniProt [Q6UX01](https://www.uniprot.org/uniprotkb/Q6UX01) · Ensembl [ENSG00000139636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139636)

## Data

Gene col 6326: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6326); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6326, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6326]; `tensor/DDL_lfc|DDL_z.npy` [6326]; `embed/gene_vectors.npy` [6326]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6326 or target_col == 6326). Every well: [[LMBR1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMBR1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "EZH1"
type: "gene"
col: 2996
ensembl_id: "ENSG00000108799"
name: "enhancer of zeste 1 polycomb repressive complex 2 subunit"
location: "17q21.2"
module: 187
arm: "+"
pooled_cpm: 59.93
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 29
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# EZH1

*enhancer of zeste 1 polycomb repressive complex 2 subunit* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 1.27× (z +4.5, q 0.004, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.477× (z -13.8, q 7e-41, down in 44 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.665× (z -7.6, q 4e-12, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATXN3]] (+0.77, fdr 7e-06), [[OGA]] (+0.72, fdr 7e-06), [[RUFY2]] (+0.66, fdr 7e-06); moves opposite to [[FAT1]] (-0.57, fdr 1e-05), [[HNRNPAB]] (-0.55, fdr 2e-05), [[EIF4G1]] (-0.54, fdr 2e-05).
> It is in [[Module 187]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2996.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 0.004 | 30/48 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.098 | 19/49 (LOX-IMVI, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.20×** | +3.5 | 0.098 | 21/48 (RKO, LS 180, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.098 | 13/49 (A549, CFPAC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.15 | 14/48 (BT-474, A-427, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 1.12× | +3.1 | 0.16 | 9/48 (SNU-1, SHP-77, …) | top dose only |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.16 | 16/49 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2996.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.477×** | -13.8 | 7e-41 | 44/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.629×** | -8.0 | 3e-13 | 34/45 (A549, SW48, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.665×** | -7.6 | 4e-12 | 33/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.474×** | -7.3 | 4e-11 | 35/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.679×** | -7.0 | 4e-10 | 28/48 (LOX-IMVI, CFPAC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.702×** | -6.6 | 4e-09 | 30/48 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.515×** | -6.5 | 7e-09 | 30/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.520×** | -6.4 | 1e-08 | 35/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.710×** | -6.4 | 1e-08 | 31/48 (LOX-IMVI, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.705×** | -6.3 | 2e-08 | 28/47 (SNU-423, HS-578T, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.530×** | -6.2 | 3e-08 | 31/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -6.1 | 7e-08 | 27/48 (SNU-423, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.800×** | -5.9 | 2e-07 | 25/48 (LOX-IMVI, CFPAC-1, …) | two highest doses | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.726×** | -5.8 | 3e-07 | 32/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.735×** | -5.8 | 3e-07 | 27/48 (A549, SNU-423, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.626×** | -4.6 | 1e-04 | 27/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.792×** | -4.2 | 9e-04 | 23/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **0.752×** | -3.8 | 0.003 | 24/49 (MIA PaCa-2, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.806×** | -3.8 | 0.003 | 20/47 (Panc 03.27, Hs 766T, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.820×** | -3.7 | 0.004 | 22/48 (Panc 03.27, KATO III, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.768×** | -3.5 | 0.008 | 15/48 (MIA PaCa-2, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.772×** | -3.4 | 0.010 | 15/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | 0.836× | -3.3 | 0.015 | 21/48 (Hs 766T, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 133 | 0 | 11 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.268× (z -14.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 89.3 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -19.2) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -12.6) |
| [[SNU-423 (line)]] | alt | 109 | 0 | 6 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.255× (z -14.5) ⚠ toxic; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.406× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 88.1 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.5) ⚠ cell-cycle shift, explains ~76% of this change |
| [[NCI-H460 (line)]] | wt | 66.2 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.295× (z -14.6) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.387× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 79.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SW48 (line)]] | wt | 67.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0946× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[A549 (line)]] | wt | 90.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[AsPC-1 (line)]] | alt | 44.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -10.2) ⚠ cell-cycle shift, explains ~76% of this change |
| [[HEC-1-A (line)]] | alt | 59.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.374× (z -9.8) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.418× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 45.8 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.450× (z -8.5) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.104× (z -12.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 89.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[A498 (line)]] | wt | 47.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.5) ⚠ cell-cycle shift, explains ~76% of this change | — |
| [[AN3 CA (line)]] | alt | 57.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[CHP-212 (line)]] | wt | 122 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[COLO 205 (line)]] | alt | 43.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.7) ⚠ cell-cycle shift, explains ~76% of this change |
| [[H4 (line)]] | wt | 39.4 | 0 | 1 | — | [[TAK-733 (drug)]] 5 µM 0.0413× (z -8.9) |
| [[HOP62 (line)]] | alt | 59.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.294× (z -11.6) |
| [[Hs 766T (line)]] | wt | 65.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[J82 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 65.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.294× (z -11.8) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 45.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.325× (z -8.5) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SW1417 (line)]] | alt | 58.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.369× (z -11.5) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.427× (z -9.6) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 74.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 97.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN3]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[OGA]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[RUFY2]] | +0.66 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.65 | +0.62 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[FBXL20]] | +0.65 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[CRBN]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[AGO4]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.62 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[ZCRB1]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 | same gene group |
| [[GARRE1]] | +0.61 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[LMBR1L]] | +0.61 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[WDR48]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAT1]] | -0.57 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.55 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[EIF4G1]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SNRPB]] | -0.54 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[FUT4]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[EIF5A]] | -0.53 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[MYH15]] | -0.52 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[XRCC5]] | -0.52 | -0.38 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.776). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.4, -44.7); signed map (-15.5, 7.2). **Vector** length 113, 31.3% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +3.7 | -4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.6 | -13.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.0 | -7.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.9 | -6.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.9 | -6.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.3 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | enhancer of zeste 1 polycomb repressive complex 2 subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,700,275-42,745,049 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0388, KMT6B |
| Gene groups (HGNC) | Histone lysine methyltransferases; Myb/SANT domain containing; Polycomb repressive complex 2; SET domain containing; MicroRNA protein coding host genes |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 2 pathways, smallest: PRC2 methylates histones and DNA; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92800](https://www.uniprot.org/uniprotkb/Q92800) (Histone-lysine N-methyltransferase EZH1):

> Polycomb group (PcG) protein. Catalytic subunit of the PRC2/EED-EZH1 complex, which methylates 'Lys-27' of histone H3, leading to transcriptional repression of the affected target gene. Able to mono-, di- and trimethylate 'Lys-27' of histone H3 to form H3K27me1, H3K27me2 and H3K27me3, respectively. Required for embryonic stem cell derivation and self-renewal, suggesting that it is involved in safeguarding embryonic stem cell identity. Compared to EZH2-containing complexes, it is less abundant …

**Summary**, from NCBI Gene [2145](https://www.ncbi.nlm.nih.gov/gene/2145):

> EZH1 is a component of a noncanonical Polycomb repressive complex-2 (PRC2) that mediates methylation of histone H3 (see MIM 602812) lys27 (H3K27) and functions in the maintenance of embryonic stem cell pluripotency and plasticity (Shen et al., 2008 [PubMed 19026780]).[supplied by OMIM, Mar 2009]

**Accessions** — [HGNC:3526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3526) · Entrez [2145](https://www.ncbi.nlm.nih.gov/gene/2145) · UniProt [Q92800](https://www.uniprot.org/uniprotkb/Q92800) · Ensembl [ENSG00000108799](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108799)

## Data

Gene col 2996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2996); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2996]; `tensor/DDL_lfc|DDL_z.npy` [2996]; `embed/gene_vectors.npy` [2996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2996 or target_col == 2996). Every well: [[EZH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EZH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

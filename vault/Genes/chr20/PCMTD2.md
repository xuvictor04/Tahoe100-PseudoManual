---
symbol: "PCMTD2"
type: "gene"
col: 12799
ensembl_id: "ENSG00000203880"
name: "protein-L-isoaspartate (D-aspartate) O-methyltransferase domain containing 2"
location: "20q13.33"
module: 76
arm: "+"
pooled_cpm: 45.82
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 34
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# PCMTD2

*protein-L-isoaspartate (D-aspartate) O-methyltransferase domain containing 2* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.41× (z +4.5, q 0.002, up in 27 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[BAY1125976 (drug)]] 5 µM: 1.64× (z +3.5, q 0.061, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (16 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.347× (z -14.4, q 2e-44, down in 45 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.463× (z -10.5, q 7e-24, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CREBL2]] (+0.62, fdr 1e-04), [[FUNDC2]] (+0.61, fdr 6e-05), [[CTC1]] (+0.57, fdr 4e-05); moves opposite to [[MEIS2]] (-0.49, fdr 7e-05), [[CKAP4]] (-0.49, fdr 4e-05), [[DLG1]] (-0.48, fdr 7e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12799.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.5 | 0.002 | 27/47 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.5 | 0.002 | 23/42 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +4.2 | 0.004 | 23/47 (C32, A498, …) | top dose only | low cells (technical?) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.061 | 23/47 (NCI-H1573, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.40× | +3.3 | 0.12 | 16/47 (PANC-1, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 1.55× | +3.1 | 0.16 | 17/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.25× | +3.1 | 0.16 | 14/47 (KATO III, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12799.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.347×** | -14.4 | 2e-44 | 45/46 (SW480, SHP-77, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.477×** | -14.3 | 1e-43 | 40/46 (SK-MEL-2, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.406×** | -12.3 | 1e-32 | 43/47 (SW480, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.430×** | -11.5 | 1e-28 | 44/47 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.431×** | -11.0 | 3e-26 | 39/47 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.463×** | -10.5 | 7e-24 | 42/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.495×** | -9.6 | 6e-20 | 38/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.495×** | -9.6 | 7e-20 | 42/47 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.518×** | -9.0 | 2e-17 | 39/46 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -7.9 | 1e-13 | 36/47 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.562×** | -7.9 | 2e-13 | 39/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.595×** | -7.1 | 7e-11 | 35/46 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.378×** | -6.9 | 2e-10 | 40/46 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.379×** | -6.9 | 2e-10 | 39/47 (LoVo, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.379×** | -6.9 | 2e-10 | 33/41 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.595×** | -6.7 | 8e-10 | 39/47 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.410×** | -6.4 | 7e-09 | 41/46 (LoVo, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.531×** | -6.2 | 2e-08 | 42/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.436×** | -5.9 | 8e-08 | 34/47 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.477×** | -5.3 | 3e-06 | 34/47 (LoVo, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.666×** | -5.2 | 4e-06 | 35/47 (LoVo, Hs 766T, …) | all doses, flat | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.612×** | -4.8 | 4e-05 | 32/47 (NCI-H460, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.526×** | -4.6 | 1e-04 | 27/47 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.656×** | -4.1 | 8e-04 | 31/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 107 | 0 | 15 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.294× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 34.3 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -16.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[PANC-1 (line)]] | alt | 41.3 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -18.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.350× (z -9.8) |
| [[LoVo (line)]] | wt | 35.3 | 0 | 7 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.251× (z -13.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.409× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 66.4 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 38.1 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -16.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[MIA PaCa-2 (line)]] | alt | 48.6 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -14.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[Hs 766T (line)]] | wt | 63.1 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 55.1 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.358× (z -8.8) |
| [[SNU-423 (line)]] | alt | 49.0 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 69.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -17.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 28.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -15.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[AsPC-1 (line)]] | alt | 30.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -14.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[COLO 205 (line)]] | alt | 55.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -13.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H1792 (line)]] | alt | 82.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 59.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0989× (z -24.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.174× (z -13.2) |
| [[C-33 A (line)]] | alt | 80.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -13.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 35.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HOP62 (line)]] | alt | 26.6 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -9.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 39.5 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.270× (z -10.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2030 (line)]] | alt | 60.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -9.0) |
| [[SHP-77 (line)]] | alt | 66.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 52.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -15.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW 900 (line)]] | alt | 35.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -15.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HEC-1-A (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.285× (z -10.4) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -8.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -9.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[Panc 03.27 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -9.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[RKO (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW1417 (line)]] | alt | 68.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.411× (z -8.7) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREBL2]] | +0.62 | +0.33 / +0.67 | both halves | 1e-04 |  |
| [[FUNDC2]] | +0.61 | +0.38 / +0.68 | both halves | 6e-05 |  |
| [[CTC1]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[ZBTB44]] | +0.56 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[RNF44]] | +0.56 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[CALCOCO1]] | +0.54 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[CCDC28A]] | +0.53 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ZNF37BP]] | +0.53 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[RBL2]] | +0.53 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[SF1]] | +0.52 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[AUH]] | +0.51 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[RAD51-AS1]] | +0.51 | +0.45 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEIS2]] | -0.49 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[CKAP4]] | -0.49 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[DLG1]] | -0.48 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[GSTP1]] | -0.46 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[RRBP1]] | -0.45 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[KIF21A]] | -0.44 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[F12]] | -0.44 | -0.19 / -0.47 | ⚠ not reproduced | 8e-04 |  |
| [[RIC8B]] | -0.43 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[SIX1]] | -0.43 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[DEGS1]] | -0.43 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[FNIP2]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ABCB6]] | -0.42 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[TUBA4A]] | -0.42 | -0.34 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.478). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-27.7, -26.4); signed map (-25.0, -34.1). **Vector** length 95.4, 28.3% of its response variance represented; |z| ≥ 3 in 1,335 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +4.5 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +2.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | -0.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.5 | +2.7 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.3 | +1.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.8 | -11.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.2 | -6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -7.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.0 | -6.9 |
|  | [[EX229 (drug)]] 5 µM |  | -5.4 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.0 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.9 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | protein-L-isoaspartate (D-aspartate) O-methyltransferase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:64,255,695-64,304,820 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10883; previously C20orf36 |
| Gene groups (HGNC) | 7BS protein methyltransferases; Isoaspartate methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NV79](https://www.uniprot.org/uniprotkb/Q9NV79) (Protein-L-isoaspartate O-methyltransferase domain-containing protein 2):

> May act as a substrate recognition component of an ECS (Elongin BC-CUL5-SOCS-box protein) E3 ubiquitin ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. May bind to the methyltransferase cofactor S-adenosylmethionine (AdoMet) via the N-terminal AdoMet binding motif, but probably does not display methyltransferase activity.

**Summary**, from NCBI Gene [55251](https://www.ncbi.nlm.nih.gov/gene/55251):

> Predicted to enable protein-L-isoaspartate (D-aspartate) O-methyltransferase activity. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15882) · Entrez [55251](https://www.ncbi.nlm.nih.gov/gene/55251) · UniProt [Q9NV79](https://www.uniprot.org/uniprotkb/Q9NV79) · Ensembl [ENSG00000203880](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203880)

## Data

Gene col 12799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12799); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12799]; `tensor/DDL_lfc|DDL_z.npy` [12799]; `embed/gene_vectors.npy` [12799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12799 or target_col == 12799). Every well: [[PCMTD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCMTD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

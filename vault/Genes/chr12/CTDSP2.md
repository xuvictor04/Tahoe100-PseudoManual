---
symbol: "CTDSP2"
type: "gene"
col: 10582
ensembl_id: "ENSG00000175215"
name: "CTD small phosphatase 2"
location: "12q14.1"
module: 69
arm: "+"
pooled_cpm: 50.45
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 32
n_dd_up_clean: 1
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# CTDSP2

*CTD small phosphatase 2* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.10× (z +5.5, q 2e-05, up in 1 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Bimiralisib (drug)]] 5 µM: 1.61× (z +4.1, q 0.010, up in 24 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.43×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.412× (z -14.8, q 0e+00, down in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.523× (z -10.2, q 3e-22, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL24]] (+0.69, fdr 7e-06), [[UBXN7]] (+0.68, fdr 9e-06), [[CREBRF]] (+0.67, fdr 2e-05); moves opposite to [[EIPR1]] (-0.58, fdr 1e-05), [[EIF2B3]] (-0.56, fdr 2e-05), [[POP1]] (-0.54, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10582.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.43×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.5 | 2e-05 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.61×** | +4.1 | 0.010 | 24/49 (LoVo, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10582.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.412×** | -14.8 | 0e+00 | 48/48 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.515×** | -11.1 | 5e-26 | 44/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.521×** | -10.8 | 4e-25 | 43/48 (NCI-H23, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.523×** | -10.2 | 3e-22 | 43/48 (SW 1271, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.557×** | -9.7 | 2e-20 | 42/48 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.572×** | -9.3 | 1e-18 | 40/48 (SNU-423, A-427, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **0.616×** | -8.1 | 5e-14 | 36/49 (NCI-H1792, NCI-H1573, …) | all doses, flat | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.428×** | -7.4 | 1e-11 | 40/48 (SW48, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.432×** | -7.3 | 2e-11 | 40/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.433×** | -7.3 | 2e-11 | 41/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.597×** | -7.2 | 4e-11 | 35/47 (SW48, AN3 CA, …) | rises with dose | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.439×** | -7.2 | 4e-11 | 39/48 (NCI-H23, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.448×** | -7.0 | 1e-10 | 39/48 (NCI-H23, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.661×** | -6.9 | 2e-10 | 33/48 (NCI-H1573, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.643×** | -6.8 | 4e-10 | 30/45 (NCI-H460, CFPAC-1, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.674×** | -6.6 | 2e-09 | 36/48 (NCI-H1573, CFPAC-1, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.729×** | -5.3 | 4e-06 | 26/48 (NCI-H1792, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.658×** | -5.0 | 2e-05 | 26/48 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.749×** | -4.8 | 4e-05 | 27/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.681×** | -4.6 | 1e-04 | 29/48 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.772×** | -4.3 | 4e-04 | 27/48 (NCI-H23, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.702×** | -4.2 | 6e-04 | 27/49 (HOP62, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 152 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -18.5) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 57.6 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.299× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -9.8) |
| [[SNU-423 (line)]] | alt | 65.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -18.0) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.391× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 80.4 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -16.2) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[venetoclax (drug)]] 5 µM 0.163× (z -9.3) |
| [[HT-29 (line)]] | alt | 59.3 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0947× (z -11.1) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 42.8 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.231× (z -11.1) |
| [[A-427 (line)]] | wt | 70.0 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -13.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[AN3 CA (line)]] | alt | 73.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.185× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 56.7 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.233× (z -11.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.337× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 71.7 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.350× (z -9.6) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.376× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 37.4 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.187× (z -12.9) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.113× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 66.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -9.8) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SW480 (line)]] | alt | 48.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 63.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -13.7) ⚠ cell-cycle shift, explains ~44% of this change |
| [[COLO 205 (line)]] | alt | 41.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.185× (z -11.0) |
| [[HOP62 (line)]] | alt | 39.7 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.331× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 25.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[SNU-1 (line)]] | wt | 75.4 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.302× (z -12.2) |
| [[SW 900 (line)]] | alt | 53.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0852× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 39.9 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.147× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.0605× (z -8.9) |
| [[A-172 (line)]] | wt | 37.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.355× (z -8.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A549 (line)]] | wt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[CHP-212 (line)]] | wt | 42.2 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0799× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.356× (z -10.3) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.362× (z -8.8) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 59.8 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.345× (z -9.3) |
| [[LS 180 (line)]] | wt | 43.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.388× (z -9.6) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SK-MEL-2 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.335× (z -9.3) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW 1271 (line)]] | alt | 66.7 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0661× (z -10.1) |
| [[SW1417 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.328× (z -9.7) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL24]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.68 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[CREBRF]] | +0.67 | +0.48 / +0.73 | both halves | 2e-05 | pathway: Unfolded Protein Response (UPR) |
| [[TSC22D4]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[RNF103]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[UBXN6]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[FOXO4]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[TXNDC16]] | +0.62 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TCP11L2]] | +0.61 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[NATD1]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ATOSA]] | +0.61 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[PIK3IP1]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIPR1]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[EIF2B3]] | -0.56 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[POP1]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[NOL10]] | -0.54 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[NAA15]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[METTL2B]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[CCT6A]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[PSMD14]] | -0.53 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[PDSS1]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[PSMD1]] | -0.52 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[CCT3]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[TCERG1]] | -0.52 | -0.46 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.7, -44.3); signed map (-13.3, 9.4). **Vector** length 111, 31.8% of its response variance represented; |z| ≥ 3 in 1,247 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.9 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.8 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.5 | +0.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +3.1 | +2.1 |
|  | [[DTP3 (drug)]] 5 µM |  | +2.7 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.2 | -11.1 |
|  | [[EX229 (drug)]] 5 µM |  | -7.1 | -7.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.0 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.0 | -9.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.9 | -7.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.0 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | CTD small phosphatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:57,819,927-57,846,729 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OS4, SCP2, PSR2 |
| Gene groups (HGNC) | CTD family phosphatases; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [O14595](https://www.uniprot.org/uniprotkb/O14595) (Carboxy-terminal domain RNA polymerase II polypeptide A small phosphatase 2):

> Preferentially catalyzes the dephosphorylation of 'Ser-5' within the tandem 7 residue repeats in the C-terminal domain (CTD) of the largest RNA polymerase II subunit POLR2A. Negatively regulates RNA polymerase II transcription, possibly by controlling the transition from initiation/capping to processive transcript elongation. Recruited by REST to neuronal genes that contain RE-1 elements, leading to neuronal gene silencing in non-neuronal cells. May contribute to the development of sarcomas.

**Summary**, from NCBI Gene [10106](https://www.ncbi.nlm.nih.gov/gene/10106):

> Enables RNA polymerase II CTD heptapeptide repeat phosphatase activity. Involved in protein dephosphorylation. Predicted to be located in nucleoplasm. Predicted to be part of TIM23 mitochondrial import inner membrane translocase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17077) · Entrez [10106](https://www.ncbi.nlm.nih.gov/gene/10106) · UniProt [O14595](https://www.uniprot.org/uniprotkb/O14595) · Ensembl [ENSG00000175215](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175215)

## Data

Gene col 10582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10582); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10582]; `tensor/DDL_lfc|DDL_z.npy` [10582]; `embed/gene_vectors.npy` [10582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10582 or target_col == 10582). Every well: [[CTDSP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTDSP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

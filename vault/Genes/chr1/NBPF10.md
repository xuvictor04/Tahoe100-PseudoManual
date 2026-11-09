---
symbol: "NBPF10"
type: "gene"
col: 15683
ensembl_id: "ENSG00000271425"
name: "NBPF member 10"
location: "1q21.1"
module: 226
arm: "+"
pooled_cpm: 16.16
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/226"]
generated_by: "tahoemap"
---

# NBPF10

*NBPF member 10* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.98× (z +33.0, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.540× (z -10.5, q 5e-23, down in 25 of 34 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 0.0951×, A498 0.226×, LOX-IMVI 0.260×, LoVo 0.202×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW 900 0.126×, A498 0.209×, NCI-H1792 0.121×, PANC-1 0.311×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (Hs 766T 0.0832×, SNU-423 0.197×, CFPAC-1 0.250×; ⚠ toxic; transcription drop); [[Pralsetinib (drug)]] 5 µM in 1 line (A549 0.0528×); [[Saquinavir (drug)]] 0.5 µM in 1 line (HCT15 0.123×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (HCT15 0.130×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBPF14]] (+0.91, fdr 7e-06), [[NBPF19]] (+0.90, fdr 7e-06), [[NOTCH2NLB]] (+0.76, fdr 7e-06); moves opposite to [[COPS7B]] (-0.67, fdr 7e-06), [[ADPGK]] (-0.66, fdr 7e-06), [[CIPC]] (-0.65, fdr 7e-06).
> It is in [[Module 226]], a single-armed module (NOTCH2 Activation and Transmission of Signal to the Nucleus).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HMGN2P46]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15683.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.98×** | +33.0 | 0e+00 | 46/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.17×** | +18.8 | 0e+00 | 44/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +10.9 | 2e-25 | 29/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +6.5 | 1e-08 | 26/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.3 | 1e-05 | 19/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +5.0 | 4e-05 | 17/45 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.34×** | +4.9 | 1e-04 | 17/46 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 3e-04 | 14/43 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.6 | 3e-04 | 14/47 (SW1417, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 3e-04 | 20/46 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.006 | 18/45 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.7 | 0.012 | 3/47 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.051 | 8/47 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.43×** | +3.1 | 0.065 | 3/43 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.065 | 5/46 (HOP62, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.077 | 7/42 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.097 | 5/45 (J82, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15683.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 0.0951×, A498 0.226×, LOX-IMVI 0.260×, LoVo 0.202×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (SW 900 0.126×, A498 0.209×, NCI-H1792 0.121×, PANC-1 0.311×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (Hs 766T 0.0832×, SNU-423 0.197×, CFPAC-1 0.250×; ⚠ toxic; transcription drop); [[Pralsetinib (drug)]] 5 µM in 1 line (A549 0.0528×); [[Saquinavir (drug)]] 0.5 µM in 1 line (HCT15 0.123×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (HCT15 0.130×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.540×** | -10.5 | 5e-23 | 25/34 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.630×** | -7.6 | 1e-11 | 27/41 (J82, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.635×** | -7.1 | 2e-10 | 23/31 (Hs 766T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.776×** | -4.4 | 0.002 | 15/47 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.796×** | -3.9 | 0.010 | 15/46 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.830× | -3.2 | 0.13 | 6/47 (COLO 205, Panc 03.27, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.838× | -3.1 | 0.18 | 6/46 (SNU-423, HOP62, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +24.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0951× (z -20.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 17.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[PANC-1 (line)]] | alt | 19.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.35× (z +29.6) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 21.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +15.1) | — |
| [[A549 (line)]] | wt | 14.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.99× (z +19.3) | [[Pralsetinib (drug)]] 5 µM 0.0528× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 26.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[HEC-1-A (line)]] | alt | 20.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +19.7) | — |
| [[NCI-H1573 (line)]] | alt | 10.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -9.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 12.6 | 0 | 2 | — | [[Saquinavir (drug)]] 0.5 µM 0.123× (z -8.7) |
| [[HOP62 (line)]] | alt | 22.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.298× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 15.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0832× (z -12.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 29.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +16.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.242× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 7.52 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -9.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 23.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -10.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 20.8 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 8.07× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SNU-423 (line)]] | alt | 29.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -10.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 30.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +8.8) | — |
| [[H4 (line)]] | wt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 7.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +10.2) | — |
| [[KATO III (line)]] | alt | 8.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.93× (z +15.6) | — |
| [[NCI-H23 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +13.1) | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +11.0) | — |
| [[SNU-1 (line)]] | wt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +12.0) | — |
| [[SW1417 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +11.0) | — |
| [[SW48 (line)]] | wt | 13.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +10.2) | — |
| [[SW480 (line)]] | alt | 5.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.93 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF14]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | same gene group |
| [[NBPF19]] | +0.90 | +0.89 / +0.88 | both halves | 7e-06 | same gene group |
| [[NOTCH2NLB]] | +0.76 | +0.75 / +0.73 | both halves | 7e-06 | STRING 543 |
| [[NOTCH2NLA]] | +0.74 | +0.69 / +0.73 | both halves | 7e-06 | STRING 431; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NBPF26]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 | same gene group; STRING 456 |
| [[METTL23]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[GATAD1]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[LRCH3]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD12]] | +0.62 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[OFD1]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[AK6]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[WASHC1]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ATF4]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS7B]] | -0.67 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[ADPGK]] | -0.66 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[CIPC]] | -0.65 | -0.69 / -0.59 | both halves | 7e-06 |  |
| [[PPT1]] | -0.64 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[RPE]] | -0.64 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[CPSF4]] | -0.62 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[TMEM248]] | -0.62 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[ARHGEF7]] | -0.62 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[CUL2]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[CNPY3]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[ALG6]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[PSMB2]] | -0.60 | -0.63 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGN2P46]] | B | HMGN2P46 activity raises NBPF10's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 1.44× lower at baseline in the lines without HMGN2P46 | 0.062 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 226]] — NOTCH2 Activation and Transmission of Signal to the Nucleus; 9 genes; every member is in the + arm (projection on the module's main direction 0.920). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.4, -29.4); signed map (44.5, -15.5). **Vector** length 87.1, 17.2% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NOTCH2 Activation and Transmission of Signal to the Nucleus* (reactome, mean cos +0.64 to 4); *Signaling by NOTCH2* (reactome, mean cos +0.64 to 4); *Pre-NOTCH Transcription and Translation* (reactome, mean cos +0.64 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +33.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +18.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.1 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -4.6 | -7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | -10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -3.7 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | +0.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | NBPF member 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.1 — chr1:146,064,711-146,229,000 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AG1 |
| Gene groups (HGNC) | NBPF members |
| Matched by | ensembl_id |

UniProt [Q6P3W6](https://www.uniprot.org/uniprotkb/Q6P3W6) carries no function annotation.

**Summary**, from NCBI Gene [100132406](https://www.ncbi.nlm.nih.gov/gene/100132406):

> This gene is a member of the neuroblastoma breakpoint family (NBPF) which consists of dozens of recently duplicated genes primarily located in segmental duplications on human chromosome 1. This gene family has experienced its greatest expansion within the human lineage and has expanded, to a lesser extent, among primates in general. Members of this gene family are characterized by tandemly repeated copies of DUF1220 protein domains. Gene copy number variations in the human chromosomal region …

**Accessions** — [HGNC:31992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31992) · Entrez [100132406](https://www.ncbi.nlm.nih.gov/gene/100132406) · UniProt [Q6P3W6](https://www.uniprot.org/uniprotkb/Q6P3W6) · Ensembl [ENSG00000271425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271425)

## Data

Gene col 15683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15683); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15683]; `tensor/DDL_lfc|DDL_z.npy` [15683]; `embed/gene_vectors.npy` [15683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15683 or target_col == 15683). Every well: [[NBPF10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBPF10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "FAH"
type: "gene"
col: 2399
ensembl_id: "ENSG00000103876"
name: "fumarylacetoacetate hydrolase"
location: "15q25.1"
module: 104
arm: "+"
pooled_cpm: 9.69
n_lines_expressing: 49
n_dd_up: 34
n_dd_down: 4
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# FAH

*fumarylacetoacetate hydrolase* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.06× (z +16.9, q 0e+00, up in 30 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.49× (z +6.1, q 1e-07, up in 18 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.677× (z -5.9, q 2e-06, down in 19 of 41 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Temsirolimus (drug)]] 0.5 µM: 0.754× (z -4.3, q 0.005, down in 14 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.226×, RPMI-7951 0.373×; ⚠ cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.212×, NCI-H1573 0.175×; ⚠ cell-cycle shift, explains ~26% of this change); [[Orlistat (drug)]] 0.05 µM in 1 line (RKO 0.0691×); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW1417 0.0572×); [[GSK1059615 (drug)]] 0.05 µM in 1 line (Hs 766T 0.0772×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EML3]] (+0.65, fdr 1e-05), [[ATP1A1]] (+0.64, fdr 7e-06), [[PLBD2]] (+0.63, fdr 1e-05); moves opposite to [[MYPN]] (-0.54, fdr 2e-05), [[TOPORS]] (-0.52, fdr 2e-05), [[RBBP6]] (-0.51, fdr 3e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MYO1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 16 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2399.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.06×** | +16.9 | 0e+00 | 30/32 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.89×** | +15.5 | 0e+00 | 12/14 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.31×** | +11.7 | 2e-29 | 16/23 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.84×** | +9.2 | 6e-18 | 31/46 (NCI-H2030, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.60×** | +7.1 | 1e-10 | 27/45 (NCI-H2347, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.60×** | +7.1 | 1e-10 | 22/46 (C32, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.56×** | +6.7 | 1e-09 | 27/46 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +6.1 | 1e-07 | 18/41 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.46×** | +5.8 | 5e-07 | 17/46 (NCI-H2030, SW1417, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.42×** | +5.0 | 3e-05 | 13/40 (RKO, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +4.7 | 1e-04 | 13/43 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.4 | 4e-04 | 14/46 (SW480, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 8e-04 | 8/44 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 14/47 (NCI-H1573, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.20×** | +3.9 | 0.004 | 18/44 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.5 | 0.015 | 11/46 (A498, NCI-H2347, …) | rises with dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.016 | 10/43 (NCI-H1792, RPMI-7951, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.023 | 12/46 (HOP62, A498, …) | rises with dose | position effect removed |
| [[Radotinib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.033 | 6/44 (PANC-1, LS 180, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.037 | 4/46 (NCI-H2347, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.040 | 8/44 (LS 180, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.058 | 5/46 (SHP-77, HOP62, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.058 | 6/44 (NCI-H1792, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.058 | 12/44 (RPMI-7951, SW 900, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.062 | 11/47 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.45×** | +2.9 | 0.066 | 6/43 (A498, RPMI-7951, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2399.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.226×, RPMI-7951 0.373×; ⚠ cell-cycle shift, explains ~26% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.212×, NCI-H1573 0.175×; ⚠ cell-cycle shift, explains ~26% of this change); [[Orlistat (drug)]] 0.05 µM in 1 line (RKO 0.0691×); [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW1417 0.0572×); [[GSK1059615 (drug)]] 0.05 µM in 1 line (Hs 766T 0.0772×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.677×** | -5.9 | 2e-06 | 19/41 (RPMI-7951, NCI-H1573, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.754×** | -4.3 | 0.005 | 14/43 (A498, COLO 205, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.830×** | -4.0 | 0.011 | 19/44 (NCI-H1573, RPMI-7951, …) | two highest doses | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.771×** | -4.0 | 0.011 | 13/44 (HOP62, KATO III, …) | two highest doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.814× | -3.1 | 0.20 | 11/41 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.05 µM |  | 0.810× | -3.0 | 0.20 | 6/46 (A-172, A-427, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 34.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -10.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 19.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 5.36 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.05 µM 0.0772× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.10× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 7.13 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 10.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0691× (z -11.8) |
| [[SW1417 (line)]] | alt | 6.30 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0572× (z -11.5) |
| [[A-172 (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EML3]] | +0.65 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ATP1A1]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PLBD2]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ANXA6]] | +0.61 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[COPS8]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ANPEP]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[COLGALT1]] | +0.58 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SRPX]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[COL18A1]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[APMAP]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[CRTAP]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[ABCA2]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYPN]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[TOPORS]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[RBBP6]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CKMT2-AS1]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[GTF2IRD2B]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[TMEM217]] | -0.49 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[C15orf48]] | -0.48 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[NME6]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ZNF140]] | -0.48 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[TRIP11]] | -0.48 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[MFAP1]] | -0.48 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[EID2]] | -0.48 | -0.45 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1B]] | B | MYO1B activity raises FAH's level | lines that do not express MYO1B (7) vs lines expressing it (43) | 1.67× lower at baseline in the lines without MYO1B | 0.035 | ⚠ within organs, on part of the lines; also absent: TBC1D8B, AHR, FAM241A |
| [[TBXAS1]] | B | TBXAS1 activity raises FAH's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 1.38× lower at baseline in the lines without TBXAS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.497). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.2, 13.1); signed map (15.7, 34.4). **Vector** length 78.6, 13.7% of its response variance represented; |z| ≥ 3 in 1,116 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.5 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.4 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.3 | +11.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.5 | +2.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.4 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.3 | -5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.6 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -2.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | fumarylacetoacetate hydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:80,152,490-80,186,946 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | XENOBIOTIC_METABOLISM, IL2_STAT5_SIGNALING, ADIPOGENESIS |
| Reactome | 3 pathways, smallest: Tyrosine catabolism; Phenylalanine and tyrosine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P16930](https://www.uniprot.org/uniprotkb/P16930) (Fumarylacetoacetase):

> Catalyzes the final step in the breakdown of the amino acid tyrosine, converting fumarylacetoacetate into fumarate and acetoacetate.

**Summary**, from NCBI Gene [2184](https://www.ncbi.nlm.nih.gov/gene/2184):

> Predicted to enable fumarylacetoacetase activity. Predicted to be involved in L-phenylalanine catabolic process; L-tyrosine catabolic process; and homogentisate catabolic process. Predicted to act upstream of or within L-arginine catabolic process. Located in extracellular exosome. Implicated in tyrosinemia type I. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3579) · Entrez [2184](https://www.ncbi.nlm.nih.gov/gene/2184) · UniProt [P16930](https://www.uniprot.org/uniprotkb/P16930) · Ensembl [ENSG00000103876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103876)

## Data

Gene col 2399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2399); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2399]; `tensor/DDL_lfc|DDL_z.npy` [2399]; `embed/gene_vectors.npy` [2399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2399 or target_col == 2399). Every well: [[FAH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

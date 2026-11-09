---
symbol: "RPS7"
type: "gene"
col: 10178
ensembl_id: "ENSG00000171863"
name: "ribosomal protein S7"
location: "2p25.3"
module: 43
arm: "+"
pooled_cpm: 67.61
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# RPS7

*ribosomal protein S7* — 2p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.42× (z +7.5, q 3e-11, up in 41 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.73× (z +4.5, q 1e-03, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 3.42×, LoVo 3.58×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 5.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.623× (z -13.6, q 3e-39, down in 48 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Medroxyprogesterone acetate (drug)]] 0.5 µM: 0.648× (z -3.6, q 0.055, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 15 lines (KATO III 0.584×, LoVo 0.571×, AsPC-1 0.603×, NCI-H23 0.562×, …; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.286×, C-33 A 0.331×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SNU-1 0.162×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL14]] (+0.80, fdr 7e-06), [[RPS2]] (+0.79, fdr 7e-06), [[RPS3A]] (+0.77, fdr 7e-06); moves opposite to [[RBM42]] (-0.54, fdr 5e-05), [[APOBEC3A]] (-0.50, fdr 3e-05), [[SLC35A4]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10178.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 3.42×, LoVo 3.58×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 5.75×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.42×** | +7.5 | 3e-11 | 41/48 (COLO 205, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.15×** | +6.2 | 1e-07 | 31/43 (SW480, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +5.8 | 2e-06 | 35/45 (A-172, KATO III, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.0 | 8e-05 | 41/47 (COLO 205, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.73×** | +4.5 | 1e-03 | 30/48 (KATO III, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.68×** | +4.4 | 1e-03 | 35/47 (LS 180, NCI-H2030, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +3.6 | 0.023 | 36/49 (KATO III, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.47× | +3.1 | 0.12 | 27/47 (KATO III, SW1417, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 1.43× | +3.1 | 0.14 | 33/48 (LoVo, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.28× | +3.0 | 0.14 | 26/49 (HOP62, NCI-H2030, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10178.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 15 lines (KATO III 0.584×, LoVo 0.571×, AsPC-1 0.603×, NCI-H23 0.562×, …; ⚠ position not correctable); [[Homoharringtonine (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.286×, C-33 A 0.331×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SNU-1 0.162×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.623×** | -13.6 | 3e-39 | 48/50 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.563×** | -4.8 | 4e-04 | 42/49 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.648×** | -3.6 | 0.055 | 34/48 (SNU-1, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 0.760× | -3.2 | 0.18 | 32/48 (AsPC-1, SW1417, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 88.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.58× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Adagrasib (drug)]] 0.05 µM 0.571× (z -13.3) ⚠ position not correctable |
| [[MIA PaCa-2 (line)]] | alt | 80.6 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.594× (z -10.4) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.286× (z -10.4) |
| [[SW480 (line)]] | alt | 83.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.42× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Adagrasib (drug)]] 0.05 µM 0.637× (z -11.5) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.632× (z -9.4) ⚠ position not correctable |
| [[A-427 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.590× (z -11.9) ⚠ position not correctable |
| [[A498 (line)]] | wt | 77.1 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.646× (z -9.7) ⚠ position not correctable |
| [[A549 (line)]] | wt | 89.1 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.578× (z -11.7) ⚠ position not correctable |
| [[AN3 CA (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 73.3 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.603× (z -12.5) ⚠ position not correctable |
| [[C-33 A (line)]] | alt | 65.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 53.0 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.574× (z -11.6) ⚠ position not correctable |
| [[COLO 205 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HCT15 (line)]] | alt | 59.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.633× (z -9.5) ⚠ position not correctable |
| [[HEC-1-A (line)]] | alt | 71.2 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.626× (z -10.7) ⚠ position not correctable |
| [[HepG2_C3A (line)]] | wt | 93.2 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.588× (z -11.6) ⚠ position not correctable |
| [[HOP62 (line)]] | alt | 55.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.595× (z -11.6) ⚠ position not correctable |
| [[Hs 766T (line)]] | wt | 45.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.599× (z -10.4) ⚠ position not correctable |
| [[HS-578T (line)]] | alt | 46.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.631× (z -9.5) ⚠ position not correctable |
| [[HT-29 (line)]] | alt | 67.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.599× (z -11.7) ⚠ position not correctable |
| [[hTERT-HPNE (line)]] | wt | 55.5 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.607× (z -11.3) ⚠ position not correctable |
| [[J82 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.647× (z -9.6) ⚠ position not correctable |
| [[KATO III (line)]] | alt | 79.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.584× (z -13.5) ⚠ position not correctable |
| [[LOX-IMVI (line)]] | wt | 90.3 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.634× (z -10.5) ⚠ position not correctable |
| [[LS 180 (line)]] | wt | 67.7 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.580× (z -11.7) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 53.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.552× (z -12.1) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.562× (z -12.3) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.589× (z -12.0) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 76.7 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.605× (z -11.1) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 67.4 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.602× (z -11.3) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 65.5 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.598× (z -12.0) ⚠ position not correctable |
| [[RKO (line)]] | wt | 82.2 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.666× (z -8.7) ⚠ position not correctable |
| [[RPMI-7951 (line)]] | alt | 48.3 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.609× (z -9.1) ⚠ position not correctable |
| [[SNU-1 (line)]] | wt | 59.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.162× (z -9.8) |
| [[SNU-423 (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.582× (z -11.3) ⚠ position not correctable |
| [[SW 900 (line)]] | alt | 50.0 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.618× (z -10.4) ⚠ position not correctable |
| [[SW1417 (line)]] | alt | 73.4 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.664× (z -10.4) ⚠ position not correctable |
| [[BT-474 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 95.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 13 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL14]] | +0.80 | +0.75 / +0.75 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS2]] | +0.79 | +0.77 / +0.69 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS3A]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL39]] | +0.73 | +0.68 / +0.68 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 994 |
| [[RPLP0]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL7]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL5]] | +0.68 | +0.60 / +0.64 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.67 | +0.68 / +0.57 | both halves | 1e-05 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS4X]] | +0.67 | +0.66 / +0.55 | both halves | 1e-05 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RACK1]] | +0.66 | +0.68 / +0.55 | both halves | 1e-05 | STRING 999 |
| [[RPL3]] | +0.66 | +0.68 / +0.56 | both halves | 1e-05 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL4]] | +0.66 | +0.71 / +0.61 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM42]] | -0.54 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[APOBEC3A]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[SLC35A4]] | -0.49 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[KPTN]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 | pathway: Cellular response to starvation |
| [[PHKG2]] | -0.47 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[MEPCE]] | -0.47 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[RGL2]] | -0.47 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[NUP62]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[SIX5]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-45.8, -30.2); signed map (-61.0, -6.8). **Vector** length 75.4, 19.5% of its response variance represented; |z| ≥ 3 in 644 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.59 to 34); *MYC targets v1* (hallmark, mean cos +0.56 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.9 | +0.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.9 | +1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.8 | -0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.8 | -2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.3 — chr2:3,575,260-3,580,920 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S7, eS7 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 52 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62081](https://www.uniprot.org/uniprotkb/P62081) (Small ribosomal subunit protein eS7):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. Required for rRNA maturation. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, …

**Summary**, from NCBI Gene [6201](https://www.ncbi.nlm.nih.gov/gene/6201):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S7E family of ribosomal proteins. It is located in the cytoplasm. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this gene …

**Accessions** — [HGNC:10440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10440) · Entrez [6201](https://www.ncbi.nlm.nih.gov/gene/6201) · UniProt [P62081](https://www.uniprot.org/uniprotkb/P62081) · Ensembl [ENSG00000171863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171863)

## Data

Gene col 10178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10178); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10178]; `tensor/DDL_lfc|DDL_z.npy` [10178]; `embed/gene_vectors.npy` [10178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10178 or target_col == 10178). Every well: [[RPS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

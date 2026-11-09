---
symbol: "TMEM109"
type: "gene"
col: 3118
ensembl_id: "ENSG00000110108"
name: "transmembrane protein 109"
location: "11q12.2"
module: 6
arm: "+"
pooled_cpm: 16.42
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TMEM109

*transmembrane protein 109* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.41× (z +16.3, q 0e+00, up in 27 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.36× (z +3.5, q 0.025, up in 10 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (HOP62 8.58×, PANC-1 5.14×, NCI-H2030 4.52×, NCI-H1792 12.8×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-423 8.60×, LOX-IMVI 7.55×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 2 lines (A498 1.49×, NCI-H2030 1.49×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.229× (z -23.8, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIGMAR1]] (+0.79, fdr 7e-06), [[ICMT]] (+0.77, fdr 7e-06), [[CDCA7]] (+0.75, fdr 7e-06); moves opposite to [[OFD1]] (-0.66, fdr 1e-05), [[CCDC174]] (-0.66, fdr 1e-05), [[NSRP1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3118.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (HOP62 8.58×, PANC-1 5.14×, NCI-H2030 4.52×, NCI-H1792 12.8×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-423 8.60×, LOX-IMVI 7.55×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 2 lines (A498 1.49×, NCI-H2030 1.49×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.41×** | +16.3 | 0e+00 | 27/28 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.90×** | +15.6 | 0e+00 | 35/37 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.44×** | +14.6 | 0e+00 | 44/46 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.98×** | +11.5 | 1e-28 | 31/32 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.70×** | +5.8 | 6e-07 | 28/45 (C32, LoVo, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +5.1 | 2e-05 | 27/41 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.58×** | +5.0 | 4e-05 | 25/42 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **1.41×** | +3.9 | 0.006 | 19/46 (SNU-423, NCI-H2030, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.38×** | +3.7 | 0.016 | 13/46 (NCI-H2030, HS-578T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.37×** | +3.6 | 0.016 | 15/45 (HOP62, J82, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.025 | 10/46 (A-172, A549, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +3.4 | 0.030 | 16/46 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Olanzapine (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.092 | 5/46 (LS 180, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3118.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.229×** | -23.8 | 0e+00 | 43/45 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.323×** | -12.9 | 1e-35 | 38/45 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.656×** | -4.6 | 7e-04 | 24/45 (MIA PaCa-2, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.660×** | -4.6 | 7e-04 | 25/45 (A498, J82, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.703×** | -3.8 | 0.016 | 18/46 (KATO III, A-172, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.598× | -3.1 | 0.18 | 18/46 (HT-29, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.686× | -3.1 | 0.18 | 5/46 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 23.7 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -16.1) |
| [[HOP62 (line)]] | alt | 12.3 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 8.58× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.2) |
| [[J82 (line)]] | alt | 30.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -19.0) |
| [[LOX-IMVI (line)]] | wt | 16.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 7.55× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0280× (z -19.5) |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -13.4) |
| [[PANC-1 (line)]] | alt | 17.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -15.1) |
| [[H4 (line)]] | wt | 20.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0713× (z -11.2) |
| [[Hs 766T (line)]] | wt | 21.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.90× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.0629× (z -20.8) |
| [[HS-578T (line)]] | alt | 42.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.4) |
| [[RKO (line)]] | wt | 17.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.1) |
| [[SNU-423 (line)]] | alt | 17.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.60× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 15.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 8.76× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.0980× (z -16.1) |
| [[SW480 (line)]] | alt | 16.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -19.1) |
| [[A-172 (line)]] | wt | 32.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -13.8) |
| [[A-427 (line)]] | wt | 20.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -11.3) |
| [[C32 (line)]] | wt | 17.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.34× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 15.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -14.7) |
| [[KATO III (line)]] | alt | 14.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.54× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 9.49 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.8× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 26.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -19.1) |
| [[NCI-H460 (line)]] | wt | 8.62 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -13.2) |
| [[SW48 (line)]] | wt | 20.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.2) |
| [[AN3 CA (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0844× (z -8.8) |
| [[BT-474 (line)]] | alt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -12.1) |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -8.6) |
| [[LoVo (line)]] | wt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -16.6) |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.2) |
| [[RPMI-7951 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 8.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -10.1) |
| [[SW1417 (line)]] | alt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.3) |
| [[A549 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIGMAR1]] | +0.79 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[ICMT]] | +0.77 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[CDCA7]] | +0.75 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[TFDP1]] | +0.72 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[COLGALT1]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[MCM3]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[PARP1]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[RANBP1]] | +0.68 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PPT1]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[GOT2]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OFD1]] | -0.66 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.66 | -0.72 / -0.51 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.65 | -0.72 / -0.53 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.63 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[ZKSCAN1]] | -0.63 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.61 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[ANKRD49]] | -0.61 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[ZNF791]] | -0.60 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[NKAP]] | -0.60 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[NBPF10]] | -0.59 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[AK6]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[ATF4]] | -0.58 | -0.60 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises TMEM109's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.44× lower at baseline in the lines without TCF19 | 0.036 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CRTAP]] | C | CRTAP activity raises TMEM109's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.83× lower at baseline in the lines without CRTAP | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |
| [[MCM3]] | C | MCM3 activity raises TMEM109's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 2.60× lower at baseline in the lines without MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |
| [[MYBL2]] | C | MYBL2 activity raises TMEM109's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.45× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[PFN2]] | C | PFN2 activity raises TMEM109's level | lines that do not express PFN2 (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without PFN2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: ASAP3, CCDC102A, TPST1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-29.3, -33.2); signed map (-28.4, -42.8). **Vector** length 91.9, 21.4% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Unwinding of DNA* (reactome, mean cos +0.50 to 12); *G0 and Early G1* (reactome, mean cos +0.50 to 10); *MYC targets v1* (hallmark, mean cos +0.54 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.8 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.7 | +15.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +4.3 | +5.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -23.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -12.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.3 | -2.1 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 109 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:60,914,158-60,923,443 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5508, SND3, hSND3, Mg23 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVC6](https://www.uniprot.org/uniprotkb/Q9BVC6) (Voltage-gated monoatomic cation channel TMEM109):

> Functions as a voltage-gated monoatomic cation channel permeable to both potassium and calcium (By similarity). Plays a role in the cellular response to DNA damage.

**Summary**, from NCBI Gene [79073](https://www.ncbi.nlm.nih.gov/gene/79073):

> Predicted to enable voltage-gated monoatomic cation channel activity. Acts upstream of or within cellular response to gamma radiation and negative regulation of programmed cell death. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28771](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28771) · Entrez [79073](https://www.ncbi.nlm.nih.gov/gene/79073) · UniProt [Q9BVC6](https://www.uniprot.org/uniprotkb/Q9BVC6) · Ensembl [ENSG00000110108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110108)

## Data

Gene col 3118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3118); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3118]; `tensor/DDL_lfc|DDL_z.npy` [3118]; `embed/gene_vectors.npy` [3118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3118 or target_col == 3118). Every well: [[TMEM109 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM109.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

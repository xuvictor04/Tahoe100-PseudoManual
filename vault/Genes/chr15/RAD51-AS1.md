---
symbol: "RAD51-AS1"
type: "gene"
col: 14446
ensembl_id: "ENSG00000245849"
name: "RAD51 antisense RNA 1"
location: "15q15.1"
module: 15
arm: "+"
pooled_cpm: 11.4
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# RAD51-AS1

*RAD51 antisense RNA 1* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.34× (z +9.4, q 3e-18, up in 18 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.42× (z +4.1, q 0.007, up in 16 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 10.8×, SW1417 12.2×, KATO III 5.22×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 7.40×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 7.68×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.375× (z -11.3, q 9e-27, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BICRAL]] (+0.67, fdr 7e-06), [[C8orf44-SGK3]] (+0.66, fdr 3e-05), [[DYNLT2]] (+0.63, fdr 3e-05); moves opposite to [[MRPL17]] (-0.60, fdr 3e-05), [[YIF1A]] (-0.49, fdr 5e-05), [[ZNF184]] (-0.49, fdr 8e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14446.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 10.8×, SW1417 12.2×, KATO III 5.22×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 7.40×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 7.68×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +9.4 | 3e-18 | 18/21 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.5 | 2e-08 | 20/34 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +5.0 | 1e-04 | 15/28 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.007 | 16/47 (LoVo, KATO III, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +3.5 | 0.052 | 14/48 (LoVo, NCI-H2030, …) | top dose only | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.076 | 7/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.32× | +3.2 | 0.11 | 12/47 (SW48, A-172, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.31× | +3.1 | 0.13 | 8/47 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14446.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.375×** | -11.3 | 9e-27 | 35/46 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.362×** | -11.2 | 9e-27 | 39/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.527×** | -10.4 | 4e-23 | 34/45 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.449×** | -9.2 | 5e-18 | 33/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.489×** | -8.2 | 3e-14 | 34/47 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.526×** | -6.5 | 6e-09 | 27/46 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.567×** | -6.5 | 6e-09 | 29/44 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.573×** | -6.4 | 1e-08 | 27/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.354×** | -6.2 | 3e-08 | 27/43 (SNU-423, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.565×** | -6.2 | 3e-08 | 28/43 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.590×** | -6.1 | 7e-08 | 29/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.599×** | -5.9 | 2e-07 | 25/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.382×** | -5.8 | 3e-07 | 24/46 (HT-29, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.632×** | -5.3 | 5e-06 | 21/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.630×** | -4.7 | 9e-05 | 17/47 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.510×** | -4.0 | 0.002 | 15/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.788×** | -3.9 | 0.003 | 18/48 (RPMI-7951, NCI-H1792, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.720×** | -3.8 | 0.005 | 14/47 (SW 900, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.745×** | -3.4 | 0.019 | 17/46 (HT-29, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.742×** | -3.2 | 0.035 | 10/46 (C-33 A, SNU-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.754×** | -3.1 | 0.040 | 16/47 (J82, NCI-H23, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **0.764×** | -3.1 | 0.042 | 15/46 (hTERT-HPNE, C-33 A, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.781×** | -2.8 | 0.087 | 9/46 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.623×** | -2.8 | 0.087 | 8/44 (MIA PaCa-2, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 26.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -13.9) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.155× (z -11.2) |
| [[LoVo (line)]] | wt | 21.8 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 10.8× (z +16.5) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.264× (z -9.6) |
| [[PANC-1 (line)]] | alt | 13.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -18.1) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.178× (z -10.4) |
| [[SW480 (line)]] | alt | 17.6 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.172× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.119× (z -10.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.198× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 9.32 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -8.8) |
| [[A549 (line)]] | wt | 7.71 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -9.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[C-33 A (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0943× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[COLO 205 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[H4 (line)]] | wt | 9.65 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0672× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.246× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 7.67 | 0 | 1 | — | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM 0.0773× (z -8.8) |
| [[Hs 766T (line)]] | wt | 8.55 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.114× (z -8.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 5.81 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0486× (z -11.0) |
| [[KATO III (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -11.0) ⚠ cell-cycle shift, explains ~57% of this change |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -8.9) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SW1417 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.2× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BICRAL]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[C8orf44-SGK3]] | +0.66 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[DYNLT2]] | +0.63 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[ZNF789]] | +0.62 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[MSTO1]] | +0.62 | +0.27 / +0.68 | both halves | 3e-04 |  |
| [[CYB5D2]] | +0.61 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[ANKRD10]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[LINC03006-1]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ZC3H3]] | +0.60 | +0.31 / +0.66 | both halves | 2e-04 |  |
| [[GTF3C2-AS2]] | +0.59 | +0.44 / +0.61 | both halves | 3e-05 | same gene group |
| [[ZBTB26]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[H3-3A-DT]] | +0.58 | +0.61 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL17]] | -0.60 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[YIF1A]] | -0.49 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ZNF184]] | -0.49 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[FADD]] | -0.49 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[SIX1]] | -0.49 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[LEO1]] | -0.48 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[CYC1]] | -0.48 | -0.24 / -0.52 | both halves | 5e-04 |  |
| [[FIBP]] | -0.47 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ARF6]] | -0.46 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[USP28]] | -0.46 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[CRYBG3]] | -0.46 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[JMJD6]] | -0.46 | -0.51 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-5.8, 23.3); signed map (31.4, -16.5). **Vector** length 72.0, 13.2% of its response variance represented; |z| ≥ 3 in 934 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.9 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | -0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.1 | -3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.9 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -9.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.7 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | RAD51 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q15.1 — chr15:40,686,183-40,695,107 (-) |
| Ensembl biotype | lncRNA |
| Also known as | TODRA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48621) · Entrez [100505648](https://www.ncbi.nlm.nih.gov/gene/100505648) · Ensembl [ENSG00000245849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245849)

## Data

Gene col 14446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14446); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14446]; `tensor/DDL_lfc|DDL_z.npy` [14446]; `embed/gene_vectors.npy` [14446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14446 or target_col == 14446). Every well: [[RAD51-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD51-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

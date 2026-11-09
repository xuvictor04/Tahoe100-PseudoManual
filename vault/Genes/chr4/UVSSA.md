---
symbol: "UVSSA"
type: "gene"
col: 8818
ensembl_id: "ENSG00000163945"
name: "UV stimulated scaffold protein A"
location: "4p16.3"
module: 52
arm: "+"
pooled_cpm: 29.21
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# UVSSA

*UV stimulated scaffold protein A* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.42× (z +4.7, q 0.001, up in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 4.23×, AsPC-1 2.86×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.434× (z -11.3, q 9e-27, down in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.624× (z -6.4, q 3e-08, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SZT2]] (+0.73, fdr 7e-06), [[GOLGA3]] (+0.72, fdr 7e-06), [[RER1]] (+0.67, fdr 1e-05); moves opposite to [[SPPL3]] (-0.53, fdr 4e-05), [[DENND4C]] (-0.53, fdr 5e-05), [[PIAS1]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8818.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 4.23×, AsPC-1 2.86×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +4.7 | 0.001 | 25/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +4.2 | 0.007 | 22/48 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8818.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.434×** | -11.3 | 9e-27 | 40/47 (KATO III, H4, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.542×** | -8.3 | 3e-14 | 36/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.584×** | -7.3 | 7e-11 | 31/47 (H4, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.624×** | -6.4 | 3e-08 | 31/47 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.640×** | -5.8 | 8e-07 | 32/48 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.671×** | -5.2 | 2e-05 | 27/47 (RPMI-7951, SK-MEL-2, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.683×** | -5.0 | 6e-05 | 26/47 (A498, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.702×** | -4.8 | 1e-04 | 28/47 (BT-474, SW 900, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.705×** | -4.7 | 2e-04 | 26/47 (RPMI-7951, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.786×** | -4.6 | 2e-04 | 23/48 (RPMI-7951, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -4.6 | 2e-04 | 23/45 (KATO III, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.780×** | -3.3 | 0.039 | 21/48 (A549, AN3 CA, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.789×** | -3.2 | 0.060 | 16/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -3.2 | 0.060 | 2/48 (NCI-H2030, BT-474) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 43.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 29.7 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -10.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Thymol (drug)]] 0.5 µM 0.202× (z -8.7) |
| [[LoVo (line)]] | wt | 53.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -10.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 28.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -11.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 38.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.4) ⚠ cell-cycle shift, explains ~6% of this change |
| [[A-427 (line)]] | wt | 69.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.122× (z -11.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[C-33 A (line)]] | alt | 48.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 29.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.264× (z -10.3) |
| [[KATO III (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -13.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.296× (z -8.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.110× (z -9.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 36.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +16.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -12.9) ⚠ cell-cycle shift, explains ~14% of this change |
| [[SW 900 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.182× (z -9.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -10.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SZT2]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[GOLGA3]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[RER1]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[SART1]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[LRRC59]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SRPRA]] | +0.61 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[YKT6]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SEC16A]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[TMEM214]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CHFR]] | +0.59 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[ARFIP2]] | +0.59 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[FOXRED1]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPPL3]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[DENND4C]] | -0.53 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[PIAS1]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 | pathway: Nucleotide Excision Repair |
| [[ARL15]] | -0.50 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[CDC14A]] | -0.50 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[ZNF148]] | -0.49 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[FRS2]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PUM1]] | -0.48 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[ATP6V0E1]] | -0.48 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[PARP8]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[HOXA7]] | -0.47 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[WDFY3]] | -0.47 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.7, -28.4); signed map (-50.9, 3.6). **Vector** length 82.2, 17.0% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.8 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.3 | -0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | -1.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.1 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.9 | -4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -11.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -3.5 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -0.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | UV stimulated scaffold protein A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,345,691-1,395,989 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1530 |
| Reactome | 6 pathways, smallest: Formation of TC-NER Pre-Incision Complex; Gap-filling DNA repair synthesis and ligation in TC-NER; Dual incision in TC-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2YD98](https://www.uniprot.org/uniprotkb/Q2YD98) (UV-stimulated scaffold protein A):

> Factor involved in transcription-coupled nucleotide excision repair (TC-NER), a mechanism that rapidly removes RNA polymerase II-blocking lesions from the transcribed strand of active genes. Acts as a key adapter that promotes recruitment of factors involved in TC-NER. Facilitates the ubiquitination of the elongating form of RNA polymerase II (RNA pol IIo) at DNA damage sites, thereby promoting RNA pol IIo backtracking and access by the TC-NER machinery to lesion sites. Also promotes …

**Summary**, from NCBI Gene [57654](https://www.ncbi.nlm.nih.gov/gene/57654):

> The protein encoded by this gene appears to be involved in ubiquitination and dephosphorylation of RNA polymerase II subunits that stall after UV irradiation. The encoded protein interacts with several members of the nucleotide excision repair complex, and is thought to be involved in the transcription-coupled nucleotide excision repair (TC-NER) pathway to help remove lesions in the DNA that block transcription. Defects in this gene can cause UV-sensitive syndrome 3. Alternative splicing …

**Accessions** — [HGNC:29304](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29304) · Entrez [57654](https://www.ncbi.nlm.nih.gov/gene/57654) · UniProt [Q2YD98](https://www.uniprot.org/uniprotkb/Q2YD98) · Ensembl [ENSG00000163945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163945)

## Data

Gene col 8818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8818); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8818]; `tensor/DDL_lfc|DDL_z.npy` [8818]; `embed/gene_vectors.npy` [8818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8818 or target_col == 8818). Every well: [[UVSSA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UVSSA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

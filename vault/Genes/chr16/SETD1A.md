---
symbol: "SETD1A"
type: "gene"
col: 1801
ensembl_id: "ENSG00000099381"
name: "SET domain containing 1A, histone lysine methyltransferase"
location: "16p11.2"
module: 36
arm: "+"
pooled_cpm: 27.75
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SETD1A

*SET domain containing 1A, histone lysine methyltransferase* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.07× (z +13.7, q 5e-40, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.579× (z -8.5, q 9e-15, down in 37 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 0.105×, LoVo 0.161×, AsPC-1 0.121×, A549 0.170×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.299×, PANC-1 0.280×, A498 0.283×, SW48 0.126×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LS 180 0.114×, HEC-1-A 0.237×, SNU-423 0.178×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.151×, HOP62 0.297×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.340×, SK-MEL-2 0.299×); [[DT-061 (drug)]] 5 µM in 1 line (NCI-H1792 0.0641×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHERP]] (+0.78, fdr 7e-06), [[UPF1]] (+0.73, fdr 7e-06), [[MLLT1]] (+0.67, fdr 7e-06); moves opposite to [[SDCBP]] (-0.53, fdr 1e-05), [[ABI1]] (-0.51, fdr 3e-05), [[SCOC]] (-0.49, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1801.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.07×** | +13.7 | 5e-40 | 44/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.99×** | +11.7 | 4e-29 | 42/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +7.9 | 4e-13 | 40/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +7.4 | 2e-11 | 32/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +6.9 | 5e-10 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.6 | 2e-06 | 28/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +4.0 | 0.006 | 20/48 (NCI-H460, J82, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.015 | 19/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.015 | 13/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +3.5 | 0.026 | 16/47 (J82, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.1 | 0.099 | 13/48 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1801.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 0.105×, LoVo 0.161×, AsPC-1 0.121×, A549 0.170×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.299×, PANC-1 0.280×, A498 0.283×, SW48 0.126×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LS 180 0.114×, HEC-1-A 0.237×, SNU-423 0.178×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.151×, HOP62 0.297×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.340×, SK-MEL-2 0.299×); [[DT-061 (drug)]] 5 µM in 1 line (NCI-H1792 0.0641×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.579×** | -8.5 | 9e-15 | 37/47 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -8.0 | 3e-13 | 24/36 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.631×** | -7.5 | 2e-11 | 31/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.649×** | -6.8 | 2e-09 | 33/48 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.772×** | -3.9 | 0.012 | 18/42 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -3.8 | 0.014 | 15/48 (A498, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -3.6 | 0.025 | 20/48 (AsPC-1, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.810×** | -3.3 | 0.066 | 20/48 (NCI-H2030, A-427, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.819×** | -3.3 | 0.069 | 16/48 (NCI-H2030, SNU-1, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 26.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -15.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 29.6 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.42× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 23.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.12× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.105× (z -19.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 29.5 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.93× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -13.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 35.7 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -14.7) |
| [[A549 (line)]] | wt | 23.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -13.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 25.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -11.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 24.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.77× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -15.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 21.4 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 10.0× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 33.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 29.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -8.9) |
| [[A498 (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -12.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -11.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -10.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 19.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -9.0) |
| [[KATO III (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -13.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -9.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 44.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 1 | — | [[DT-061 (drug)]] 5 µM 0.0641× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -11.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0684× (z -12.4) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 35.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -8.6) |
| [[SNU-423 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -11.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -11.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHERP]] | +0.78 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[UPF1]] | +0.73 | +0.70 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[MLLT1]] | +0.67 | +0.77 / +0.58 | both halves | 7e-06 | STRING 441 |
| [[TBC1D10B]] | +0.66 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[L3MBTL2]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[DDX23]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ZNF384]] | +0.64 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[PRCC]] | +0.63 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[KMT2B]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 | same gene group; pathway: Chromatin modifying enzymes; STRING 821 |
| [[ZNF787]] | +0.62 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ZDHHC5]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[DNAAF5]] | +0.59 | +0.64 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP]] | -0.53 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[ABI1]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[SCOC]] | -0.49 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ATP11B]] | -0.49 | -0.31 / -0.58 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-31.2, -10.2); signed map (-10.7, -28.4). **Vector** length 91.3, 19.6% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +7.2 | +11.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.1 | +13.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.7 | +0.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.3 | +1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.8 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +0.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +1.1 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -8.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.2 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -3.3 | -3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -1.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | SET domain containing 1A, histone lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,957,294-30,984,664 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0339, Set1, KMT2F, SET1A |
| Gene groups (HGNC) | Histone lysine methyltransferases; RNA binding motif containing; SET domain containing |
| Reactome | 8 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; PKMTs methylate histone lysines; RUNX1 regulates genes involved in megakaryocyte differentiation and platelet function |
| Matched by | ensembl_id |

**Function**, from UniProt [O15047](https://www.uniprot.org/uniprotkb/O15047) (Histone-lysine N-methyltransferase SETD1A):

> Histone methyltransferase that catalyzes methyl group transfer from S-adenosyl-L-methionine to the epsilon-amino group of 'Lys-4' of histone H3 (H3K4) via a non-processive mechanism. Part of chromatin remodeling machinery, forms H3K4me1, H3K4me2 and H3K4me3 methylation marks at active chromatin sites where transcription and DNA repair take place. Responsible for H3K4me3 enriched promoters and transcriptional programming of inner mass stem cells and neuron progenitors during embryogenesis (By …

**Summary**, from NCBI Gene [9739](https://www.ncbi.nlm.nih.gov/gene/9739):

> The protein encoded by this gene is a component of a histone methyltransferase (HMT) complex that produces mono-, di-, and trimethylated histone H3 at Lys4. Trimethylation of histone H3 at lysine 4 (H3K4me3) is a chromatin modification known to generally mark the transcription start sites of active genes. The protein contains SET domains, a RNA recognition motif domain and is a member of the class V-like SAM-binding methyltransferase superfamily. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:29010](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29010) · Entrez [9739](https://www.ncbi.nlm.nih.gov/gene/9739) · UniProt [O15047](https://www.uniprot.org/uniprotkb/O15047) · Ensembl [ENSG00000099381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099381)

## Data

Gene col 1801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1801); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1801]; `tensor/DDL_lfc|DDL_z.npy` [1801]; `embed/gene_vectors.npy` [1801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1801 or target_col == 1801). Every well: [[SETD1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETD1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

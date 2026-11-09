---
symbol: "LARS2"
type: "gene"
col: 237
ensembl_id: "ENSG00000011376"
name: "leucyl-tRNA synthetase 2, mitochondrial"
location: "3p21.31"
module: 4
arm: "+"
pooled_cpm: 50.82
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# LARS2

*leucyl-tRNA synthetase 2, mitochondrial* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.79× (z +13.2, q 8e-37, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.563× (z -12.1, q 9e-31, down in 33 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.810× (z -6.8, q 2e-09, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 0.107×, RKO 0.137×, KATO III 0.185×, NCI-H2030 0.231×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.164×, SW48 0.115×, NCI-H460 0.397×, SHP-77 0.314×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.349×, KATO III 0.269×, PANC-1 0.454×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.102×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (SW 1271 0.0712×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYRM4]] (+0.76, fdr 7e-06), [[ATR]] (+0.76, fdr 7e-06), [[COX10]] (+0.75, fdr 7e-06); moves opposite to [[RAB33B]] (-0.60, fdr 1e-05), [[PJA2]] (-0.57, fdr 1e-05), [[FAM161B]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CAMK2N1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.79×** | +13.2 | 8e-37 | 40/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +13.0 | 2e-36 | 40/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +10.9 | 2e-25 | 42/48 (HOP62, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +9.9 | 6e-21 | 38/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +9.2 | 6e-18 | 36/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +8.9 | 8e-17 | 38/48 (HOP62, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.7 | 4e-16 | 35/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +8.0 | 1e-13 | 35/48 (NCI-H2347, NCI-H460, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +7.8 | 5e-13 | 34/43 (SW480, RKO, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +5.8 | 5e-07 | 19/48 (HS-578T, SNU-423, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.28×** | +5.4 | 3e-06 | 23/48 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.18× | +5.3 | 5e-06 | 19/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.52×** | +4.7 | 1e-04 | 25/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +4.6 | 1e-04 | 21/47 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 2e-04 | 19/47 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.004 | 13/48 (SK-MEL-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.004 | 17/48 (HOP62, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.011 | 15/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.026 | 8/48 (C32, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.038 | 5/48 (Panc 03.27, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 237.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H23 0.107×, RKO 0.137×, KATO III 0.185×, NCI-H2030 0.231×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (A-427 0.164×, SW48 0.115×, NCI-H460 0.397×, SHP-77 0.314×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.349×, KATO III 0.269×, PANC-1 0.454×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.102×); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (SW 1271 0.0712×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.563×** | -12.1 | 9e-31 | 33/45 (A-427, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.611×** | -11.2 | 1e-26 | 34/46 (NCI-H23, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -8.1 | 8e-14 | 28/44 (HEC-1-A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -6.8 | 2e-09 | 29/48 (A498, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.769×** | -6.0 | 3e-07 | 29/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.821×** | -4.5 | 6e-04 | 23/47 (NCI-H2030, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.846× | -3.8 | 0.011 | 21/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.858× | -3.5 | 0.034 | 14/47 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.866× | -3.3 | 0.062 | 13/48 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.908× | -3.1 | 0.098 | 10/48 (RPMI-7951, HCT15, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.827× | -3.1 | 0.10 | 16/48 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.1 | 0.11 | 12/48 (SW480, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 42.7 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.11× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.429× (z -8.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 73.3 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.550× (z -9.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 44.5 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -16.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 62.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -18.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 53.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.102× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 93.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -13.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 59.5 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 33.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 44.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.454× (z -10.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 58.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 66.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -9.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 56.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 80.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -24.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 56.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -11.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 80.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -20.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 62.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -10.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 73.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 78.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 51.4 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0712× (z -9.0) |
| [[SW48 (line)]] | wt | 58.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -14.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 59.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYRM4]] | +0.76 | +0.81 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ATR]] | +0.76 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[COX10]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[ANAPC1]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.72 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[TANGO6]] | +0.71 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[EIPR1]] | +0.70 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.66 | +0.68 / +0.68 | both halves | 7e-06 | STRING 484 |
| [[NAA25]] | +0.66 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[RPTOR]] | +0.66 | +0.57 / +0.69 | both halves | 1e-05 | STRING 630 |
| [[QRSL1]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[PRMT3]] | +0.64 | +0.66 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB33B]] | -0.60 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[PJA2]] | -0.57 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[FAM161B]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[HDAC5]] | -0.56 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[RAB11A]] | -0.55 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[RIOK3]] | -0.54 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[BMF]] | -0.54 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ING1]] | -0.54 | -0.66 / -0.48 | both halves | 2e-05 |  |
| [[KDM5B]] | -0.54 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[FOXO6]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[RAP1GAP]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMK2N1]] | B | CAMK2N1 activity lowers LARS2's level | lines that do not express CAMK2N1 (8) vs lines expressing it (42) | 1.35× higher at baseline in the lines without CAMK2N1 | 0.066 | ⚠ within organs, on part of the lines; also absent: RPLP0P2; maybe low, not absent |
| [[TSEN2]] | C | TSEN2 activity raises LARS2's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.25× lower at baseline in the lines without TSEN2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.3, -33.1); signed map (-0.3, -49.9). **Vector** length 112, 29.6% of its response variance represented; |z| ≥ 3 in 1,110 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.7 | +13.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.4 | +10.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.7 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.4 | +9.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.1 | -6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.7 | -11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | leucyl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:45,388,561-45,554,726 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0028, LEURS, MGC26121, mtLeuRS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15031](https://www.uniprot.org/uniprotkb/Q15031) (Leucine--tRNA ligase, mitochondrial):

> Catalyzes the attachment of leucine to its cognate tRNA.

**Summary**, from NCBI Gene [23395](https://www.ncbi.nlm.nih.gov/gene/23395):

> This gene encodes a class 1 aminoacyl-tRNA synthetase, mitochondrial leucyl-tRNA synthetase. Each of the twenty aminoacyl-tRNA synthetases catalyzes the aminoacylation of a specific tRNA or tRNA isoaccepting family with the cognate amino acid. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17095) · Entrez [23395](https://www.ncbi.nlm.nih.gov/gene/23395) · UniProt [Q15031](https://www.uniprot.org/uniprotkb/Q15031) · Ensembl [ENSG00000011376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011376)

## Data

Gene col 237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 237); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 237]; `tensor/DDL_lfc|DDL_z.npy` [237]; `embed/gene_vectors.npy` [237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 237 or target_col == 237). Every well: [[LARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "PIP5K1C"
type: "gene"
col: 11779
ensembl_id: "ENSG00000186111"
name: "phosphatidylinositol-4-phosphate 5-kinase type 1 gamma"
location: "19p13.3"
module: 3
arm: "+"
pooled_cpm: 23.43
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PIP5K1C

*phosphatidylinositol-4-phosphate 5-kinase type 1 gamma* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 3.56× (z +29.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.578× (z -11.7, q 6e-29, down in 27 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.533× (z -7.6, q 9e-12, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (SW480 0.165×, NCI-H460 0.138×, NCI-H2030 0.104×, LoVo 0.231×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H460 0.196×, SW480 0.297×, NCI-H23 0.254×, LoVo 0.308×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.150×, KATO III 0.212×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Naproxen (drug)]] 5 µM in 1 line (AN3 CA 0.0896×); [[TAK-901 (drug)]] 5 µM in 1 line (NCI-H23 0.129×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (AN3 CA 0.114×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC34]] (+0.73, fdr 7e-06), [[GAS2L1]] (+0.68, fdr 4e-05), [[DVL1]] (+0.64, fdr 3e-05); moves opposite to [[MTMR2]] (-0.56, fdr 3e-05), [[YARS2]] (-0.55, fdr 5e-05), [[SELENOF]] (-0.53, fdr 7e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11779.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.56×** | +29.2 | 0e+00 | 47/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.78×** | +23.6 | 0e+00 | 47/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.59×** | +21.9 | 0e+00 | 48/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +8.1 | 1e-13 | 28/47 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +7.8 | 7e-13 | 31/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +7.7 | 1e-12 | 34/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +6.6 | 3e-09 | 20/47 (NCI-H1792, SW480, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +6.2 | 5e-08 | 18/48 (SW480, LS 180, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +5.1 | 2e-05 | 19/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.8 | 9e-05 | 16/47 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +4.5 | 4e-04 | 16/48 (HEC-1-A, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 0.001 | 7/48 (HT-29, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.13× | +4.0 | 0.003 | 15/47 (A498, NCI-H23, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.005 | 8/46 (NCI-H23, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | 1.16× | +3.3 | 0.035 | 16/47 (KATO III, SW480, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.11× | +3.3 | 0.040 | 3/48 (SHP-77, A549, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.15× | +3.1 | 0.061 | 15/47 (A-172, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11779.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (SW480 0.165×, NCI-H460 0.138×, NCI-H2030 0.104×, LoVo 0.231×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H460 0.196×, SW480 0.297×, NCI-H23 0.254×, LoVo 0.308×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.150×, KATO III 0.212×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Naproxen (drug)]] 5 µM in 1 line (AN3 CA 0.0896×); [[TAK-901 (drug)]] 5 µM in 1 line (NCI-H23 0.129×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (AN3 CA 0.114×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.578×** | -11.7 | 6e-29 | 27/40 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.533×** | -7.6 | 9e-12 | 25/48 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **0.823×** | -6.4 | 4e-08 | 21/48 (A-427, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.791×** | -5.4 | 8e-06 | 20/43 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.845× | -3.8 | 0.020 | 6/47 (A-427, NCI-H1792, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.738×** | -3.7 | 0.023 | 13/31 (HS-578T, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.906× | -3.2 | 0.095 | 3/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.866× | -3.1 | 0.15 | 14/47 (H4, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.1 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.26× (z +15.4) | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -17.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 29.0 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.61× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 34.7 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +8.5) ⚠ cell-cycle shift, explains ~5% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.129× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 25.3 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.28× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -15.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 42.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +10.7) | — |
| [[A498 (line)]] | wt | 15.0 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +11.1) | — |
| [[A549 (line)]] | wt | 14.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.83× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -10.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 34.4 | 0 | 3 | — | [[Naproxen (drug)]] 5 µM 0.0896× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 28.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +13.0) | — |
| [[KATO III (line)]] | alt | 19.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.80× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 33.1 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.29× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 28.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.43× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.4) ⚠ cell-cycle shift, explains ~5% of this change |
| [[PANC-1 (line)]] | alt | 15.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.69× (z +12.8) | — |
| [[A-427 (line)]] | wt | 26.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 21.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.61× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 19.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 26.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.60× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 24.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.45× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 27.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.66× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 18.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -15.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 20.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.81× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 25.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 18.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.66× (z +8.6) | — |
| [[H4 (line)]] | wt | 14.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.07× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 29.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.05× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.203× (z -9.4) ⚠ toxic |
| [[J82 (line)]] | alt | 22.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.82× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +8.7) | — |
| [[RKO (line)]] | wt | 30.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -12.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC34]] | +0.73 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[GAS2L1]] | +0.68 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[DVL1]] | +0.64 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MEX3D]] | +0.64 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[LLGL2]] | +0.63 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[PGAP6]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[GNA11]] | +0.62 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[CAMSAP3]] | +0.62 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CCNQ]] | +0.61 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[TRIM11]] | +0.60 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[TMEM184B]] | +0.60 | +0.33 / +0.63 | both halves | 1e-04 |  |
| [[RBM38]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR2]] | -0.56 | -0.45 / -0.52 | both halves | 3e-05 | pathway: PI Metabolism |
| [[YARS2]] | -0.55 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[SELENOF]] | -0.53 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[ATP5PB]] | -0.52 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[SNX5]] | -0.51 | -0.18 / -0.47 | ⚠ not reproduced | 0.001 | STRING 619 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.4, -0.4); signed map (-26.8, 18.2). **Vector** length 84.5, 16.9% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +29.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +23.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +21.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +3.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +8.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.8 | +3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.6 | +1.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.3 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -4.7 | -6.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -7.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.8 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -1.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.8 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-4-phosphate 5-kinase type 1 gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,630,183-3,700,468 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIP5Kgamma, KIAA0589, LCCS3 |
| Gene groups (HGNC) | Phosphatidylinositol-4-phosphate 5-kinase type 1 family |
| Reactome | 23 pathways, smallest: SEMA3A-Plexin repulsion signaling by inhibiting Integrin adhesion; Regulation of CDH1 posttranslational processing and trafficking to plasma membrane; Synthesis of PIPs at the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [O60331](https://www.uniprot.org/uniprotkb/O60331) (Phosphatidylinositol 4-phosphate 5-kinase type-1 gamma):

> Catalyzes the phosphorylation of phosphatidylinositol 4-phosphate (PtdIns(4)P/PI4P) to form phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2/PIP2), a lipid second messenger that regulates several cellular processes such as signal transduction, vesicle trafficking, actin cytoskeleton dynamics, cell adhesion, and cell motility. PtdIns(4,5)P2 can directly act as a second messenger or can be utilized as a precursor to generate other second messengers: inositol 1,4,5-trisphosphate (IP3), …

**Summary**, from NCBI Gene [23396](https://www.ncbi.nlm.nih.gov/gene/23396):

> This locus encodes a type I phosphatidylinositol 4-phosphate 5-kinase. The encoded protein catalyzes phosphorylation of phosphatidylinositol 4-phosphate, producing phosphatidylinositol 4,5-bisphosphate. This enzyme is found at synapses and has been found to play roles in endocytosis and cell migration. Mutations at this locus have been associated with lethal congenital contractural syndrome. Alternatively spliced transcript variants encoding different isoforms have been described.[provided by …

**Accessions** — [HGNC:8996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8996) · Entrez [23396](https://www.ncbi.nlm.nih.gov/gene/23396) · UniProt [O60331](https://www.uniprot.org/uniprotkb/O60331) · Ensembl [ENSG00000186111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186111)

## Data

Gene col 11779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11779); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11779]; `tensor/DDL_lfc|DDL_z.npy` [11779]; `embed/gene_vectors.npy` [11779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11779 or target_col == 11779). Every well: [[PIP5K1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIP5K1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

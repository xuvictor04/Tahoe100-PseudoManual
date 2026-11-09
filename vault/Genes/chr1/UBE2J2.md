---
symbol: "UBE2J2"
type: "gene"
col: 8298
ensembl_id: "ENSG00000160087"
name: "ubiquitin conjugating enzyme E2 J2"
location: "1p36.33"
module: 156
arm: "+"
pooled_cpm: 38.86
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# UBE2J2

*ubiquitin conjugating enzyme E2 J2* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.48× (z +12.3, q 3e-32, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.658× (z -9.3, q 8e-18, down in 31 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tetracycline (hydrochloride) (drug)]] 5 µM: 0.807× (z -4.6, q 4e-04, down in 13 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LoVo 0.104×, NCI-H1792 0.0853×, SW480 0.300×, A549 0.163×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 6 lines (A-427 0.194×, C-33 A 0.182×, SW480 0.376×, MIA PaCa-2 0.309×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.219×, AsPC-1 0.268×; ⚠ toxic; transcription drop); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (AN3 CA 0.134×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SW48 0.211×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF3]] (+0.71, fdr 7e-06), [[RPP14]] (+0.70, fdr 7e-06), [[MAU2]] (+0.70, fdr 7e-06); moves opposite to [[CREG1]] (-0.65, fdr 7e-06), [[PGRMC1]] (-0.60, fdr 1e-05), [[ERMP1]] (-0.58, fdr 1e-05).
> It is in [[Module 156]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +12.3 | 3e-32 | 37/48 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.5 | 2e-08 | 26/47 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +6.1 | 1e-07 | 29/48 (A-172, HCT15, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +5.9 | 4e-07 | 24/45 (HOP62, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | **1.25×** | +5.0 | 6e-05 | 24/47 (HCT15, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.9 | 8e-05 | 24/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 1e-04 | 23/47 (SW480, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.8 | 1e-04 | 18/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +4.8 | 1e-04 | 23/48 (KATO III, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.8 | 1e-04 | 23/48 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.49×** | +4.6 | 2e-04 | 20/49 (LoVo, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.24×** | +4.6 | 2e-04 | 22/48 (HOP62, A498, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 3e-04 | 18/47 (RKO, HOP62, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.22×** | +4.5 | 3e-04 | 22/48 (HCT15, SNU-423, …) | two highest doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 0.001 | 18/48 (HOP62, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.8 | 0.005 | 5/48 (NCI-H23, SHP-77, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.007 | 14/47 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.021 | 8/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.17× | +3.3 | 0.026 | 12/47 (A-172, CFPAC-1, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.034 | 16/47 (A-172, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8298.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (LoVo 0.104×, NCI-H1792 0.0853×, SW480 0.300×, A549 0.163×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 6 lines (A-427 0.194×, C-33 A 0.182×, SW480 0.376×, MIA PaCa-2 0.309×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.219×, AsPC-1 0.268×; ⚠ toxic; transcription drop); [[5-Azacytidine (drug)]] 0.5 µM in 1 line (AN3 CA 0.134×); [[Roxadustat (drug)]] 0.05 µM in 1 line (SW48 0.211×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.658×** | -9.3 | 8e-18 | 31/47 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.643×** | -9.1 | 4e-17 | 28/43 (A-427, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.734×** | -6.6 | 7e-09 | 21/40 (LoVo, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.816×** | -6.3 | 3e-08 | 22/47 (HT-29, A-427, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.775×** | -5.6 | 2e-06 | 25/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.847× | -5.2 | 2e-05 | 21/48 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | **0.807×** | -4.6 | 4e-04 | 13/48 (PANC-1, NCI-H2347, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.871× | -4.3 | 0.001 | 12/48 (NCI-H460, SW480, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.822×** | -4.2 | 0.002 | 20/47 (HepG2/C3A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.880× | -4.0 | 0.004 | 11/48 (A549, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.858× | -3.2 | 0.060 | 19/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 5 µM |  | 0.865× | -3.2 | 0.063 | 8/48 (SK-MEL-2, C-33 A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 26.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +16.3) | — |
| [[C-33 A (line)]] | alt | 56.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -12.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 46.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.1) | [[Lonafarnib (drug)]] 5 µM 0.0941× (z -12.1) ⚠ toxic |
| [[LoVo (line)]] | wt | 44.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -24.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 58.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -9.4) ⚠ cell-cycle shift, explains ~15% of this change |
| [[A-427 (line)]] | wt | 51.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -16.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 30.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -15.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 44.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +17.1) | — |
| [[NCI-H460 (line)]] | wt | 36.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -9.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 45.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -15.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 27.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 46.0 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.134× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -10.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 59.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +13.0) | — |
| [[HCT15 (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -9.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -9.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -8.9) ⚠ cell-cycle shift, explains ~9% of this change |
| [[J82 (line)]] | alt | 45.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 32.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0853× (z -20.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.499× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -10.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 51.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.3) | — |
| [[RPMI-7951 (line)]] | alt | 46.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 33.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +15.0) | — |
| [[SW48 (line)]] | wt | 36.9 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.211× (z -9.3) |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF3]] | +0.71 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[RPP14]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[MAU2]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[FAF2]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 | STRING 444 |
| [[SDHAF2]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PIAS4]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[SFSWAP]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[DOHH]] | +0.65 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[MTG2]] | +0.65 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[HMGXB4]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PPP6R2]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[IP6K1]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREG1]] | -0.65 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[PGRMC1]] | -0.60 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[ERMP1]] | -0.58 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[SCARB2]] | -0.58 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[H3-3A]] | -0.58 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.56 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[LANCL1]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[VAMP1]] | -0.55 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[TMEM106C]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[TMEM123]] | -0.55 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[KDM1A]] | -0.54 | -0.63 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.724). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.5, 3.1); signed map (-4.5, -15.2). **Vector** length 103, 23.1% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +12.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +6.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.6 | +4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +4.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.9 | +2.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.7 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.5 | -9.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.7 | -5.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.4 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.7 | -9.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.0 | -0.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 J2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,253,909-1,273,864 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ubc6p, NCUBE2 |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 7 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; E3 ubiquitin ligases ubiquitinate target proteins; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2K1](https://www.uniprot.org/uniprotkb/Q8N2K1) (Ubiquitin-conjugating enzyme E2 J2):

> Catalyzes the covalent attachment of ubiquitin to other proteins. Seems to function in the selective degradation of misfolded membrane proteins from the endoplasmic reticulum (ERAD) (By similarity). In cooperation with the GATOR2 complex, catalyzes 'Lys-6'-linked ubiquitination of NPRL2.

**Summary**, from NCBI Gene [118424](https://www.ncbi.nlm.nih.gov/gene/118424):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. This enzyme is located in the membrane of the endoplasmic reticulum. Multiple alternatively spliced …

**Accessions** — [HGNC:19268](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19268) · Entrez [118424](https://www.ncbi.nlm.nih.gov/gene/118424) · UniProt [Q8N2K1](https://www.uniprot.org/uniprotkb/Q8N2K1) · Ensembl [ENSG00000160087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160087)

## Data

Gene col 8298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8298); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8298]; `tensor/DDL_lfc|DDL_z.npy` [8298]; `embed/gene_vectors.npy` [8298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8298 or target_col == 8298). Every well: [[UBE2J2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2J2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

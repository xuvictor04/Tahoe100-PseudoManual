---
symbol: "MROH1"
type: "gene"
col: 11058
ensembl_id: "ENSG00000179832"
name: "maestro heat like repeat family member 1"
location: "8q24.3"
module: 17
arm: "-"
pooled_cpm: 77.86
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 18
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MROH1

*maestro heat like repeat family member 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +9.7, q 1e-19, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.458× (z -11.6, q 2e-28, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.721× (z -7.2, q 2e-10, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS53]] (+0.70, fdr 7e-06), [[TANGO2]] (+0.63, fdr 7e-06), [[CDR2]] (+0.62, fdr 1e-05); moves opposite to [[PRKAA1]] (-0.63, fdr 4e-05), [[NBN]] (-0.60, fdr 1e-05), [[C2CD5]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11058.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +9.7 | 1e-19 | 39/49 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.78×** | +7.4 | 4e-11 | 39/48 (PANC-1, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.54×** | +6.7 | 5e-09 | 36/48 (COLO 205, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +5.1 | 5e-05 | 27/48 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.35×** | +4.5 | 8e-04 | 27/47 (NCI-H2030, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 0.002 | 27/48 (COLO 205, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.30×** | +4.1 | 0.003 | 27/48 (NCI-H1573, A498, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.003 | 22/49 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.012 | 23/49 (HOP62, J82, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | 1.18× | +3.6 | 0.015 | 15/49 (NCI-H1573, Hs 766T, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.021 | 29/47 (NCI-H2030, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.030 | 18/48 (HEC-1-A, A498, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.17× | +3.3 | 0.038 | 13/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.1 | 0.087 | 13/48 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.089 | 23/48 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.100 | 22/48 (CFPAC-1, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.49×** | +3.0 | 0.100 | 20/49 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11058.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.458×** | -11.6 | 2e-28 | 41/48 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.599×** | -7.3 | 6e-11 | 31/43 (NCI-H23, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.721×** | -7.2 | 2e-10 | 37/48 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.744×** | -6.5 | 1e-08 | 28/48 (BT-474, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **0.673×** | -6.1 | 1e-07 | 34/48 (RKO, SW48, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.760×** | -6.0 | 2e-07 | 31/48 (RKO, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.683×** | -5.9 | 3e-07 | 33/48 (HS-578T, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.678×** | -5.8 | 5e-07 | 27/40 (A-172, A-427, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.680×** | -5.7 | 6e-07 | 35/47 (RKO, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.694×** | -5.7 | 8e-07 | 30/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.732×** | -4.8 | 7e-05 | 32/49 (NCI-H2347, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~97% of this change | **0.761×** | -4.2 | 0.001 | 26/47 (HT-29, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.619×** | -3.6 | 0.017 | 23/47 (HOP62, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.806×** | -3.3 | 0.033 | 21/48 (LS 180, SW48, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.813×** | -3.2 | 0.049 | 19/47 (NCI-H1792, hTERT-HPNE, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **0.809×** | -3.2 | 0.055 | 20/48 (A498, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.805×** | -3.1 | 0.063 | 20/47 (C-33 A, A549, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11058. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 91.6 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +11.6) | [[Harringtonine (drug)]] 0.5 µM 0.254× (z -11.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 94.5 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -15.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[MIA PaCa-2 (line)]] | alt | 94.8 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 64.3 | 1 (1 ⚠) | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.23× (z +9.6) ⚠ cell-cycle shift, explains ~33% of this change | [[Harringtonine (drug)]] 5 µM 0.306× (z -13.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 68.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[HT-29 (line)]] | alt | 131 | 2 (2 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +9.3) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[LOX-IMVI (line)]] | wt | 55.1 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.168× (z -15.4) ⚠ cell-cycle shift, explains ~43% of this change |
| [[Panc 03.27 (line)]] | alt | 102 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.538× (z -9.2) |
| [[RKO (line)]] | wt | 224 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.474× (z -9.9) |
| [[A-172 (line)]] | wt | 66.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0584× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[A549 (line)]] | wt | 57.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 92.4 | 0 | 3 | — | [[Tucidinostat (drug)]] 0.5 µM 0.416× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 58.7 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.461× (z -9.4) |
| [[SW1417 (line)]] | alt | 129 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -16.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 93.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.325× (z -11.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[BT-474 (line)]] | alt | 150 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -17.4) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 87.2 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.42× (z +10.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 95.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.13× (z +8.6) ⚠ cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 59.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 49.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[AsPC-1 (line)]] | alt | 120 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 44.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.7) | — |
| [[H4 (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 79.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[HepG2_C3A (line)]] | wt | 59.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.250× (z -9.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 82.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 92.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 61.0 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.91× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.284× (z -10.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SNU-423 (line)]] | alt | 87.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[SW 900 (line)]] | alt | 64.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 109 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 84.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11058), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS53]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[TANGO2]] | +0.63 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[CDR2]] | +0.62 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[VAC14]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PITPNA]] | +0.60 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[UFD1]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[DRD4]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[CTNS]] | +0.58 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[NPIPB11]] | +0.58 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[TPD52L2]] | +0.57 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[PTDSS2]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[SENP5]] | +0.57 | +0.47 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAA1]] | -0.63 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[NBN]] | -0.60 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[C2CD5]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[CDC73]] | -0.59 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[VAPA]] | -0.59 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[COMMD8]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[TBL1XR1]] | -0.57 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[NDUFA5]] | -0.56 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[EID1]] | -0.56 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[SUGT1P3]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ZNF608]] | -0.55 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[DUSP19]] | -0.55 | -0.46 / -0.63 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-16.7, -0.1); signed map (-21.5, 0.6). **Vector** length 128, 40.3% of its response variance represented; |z| ≥ 3 in 1,164 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +9.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | +8.8 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +8.3 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.0 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.2 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.4 | +4.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +4.1 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.0 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.4 | -7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -7.3 | -11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.1 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.2 | -5.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.8 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | maestro heat like repeat family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,148,016-144,261,927 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1833; previously HEATR7A |
| Gene groups (HGNC) | Maestro heat like repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDA8](https://www.uniprot.org/uniprotkb/Q8NDA8) (Maestro heat-like repeat-containing protein family member 1):

> Lysosome fission factor. Recruited to lysosomes by RAB7 (RAB7A or RAB7B) at scission sites and homooligomerizes to mediate the constriction and scission of lysosomal tubules. May sever membranes by inserting amphipathic helices into one bilayer leaflet. Lysosome fission is required to maintain their steady-state number, shape, size, composition and function, and to accomplish regeneration.

**Summary**, from NCBI Gene [727957](https://www.ncbi.nlm.nih.gov/gene/727957):

> Enables membrane destabilizing activity. Involved in lysosome fission. Is active in lysosomal membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26958](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26958) · Entrez [727957](https://www.ncbi.nlm.nih.gov/gene/727957) · UniProt [Q8NDA8](https://www.uniprot.org/uniprotkb/Q8NDA8) · Ensembl [ENSG00000179832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179832)

## Data

Gene col 11058: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11058); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11058, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11058]; `tensor/DDL_lfc|DDL_z.npy` [11058]; `embed/gene_vectors.npy` [11058]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11058 or target_col == 11058). Every well: [[MROH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MROH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

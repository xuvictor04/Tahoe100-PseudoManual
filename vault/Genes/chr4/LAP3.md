---
symbol: "LAP3"
type: "gene"
col: 20
ensembl_id: "ENSG00000002549"
name: "leucine aminopeptidase 3"
location: "4p15.32"
module: 32
arm: "+"
pooled_cpm: 66.9
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 38
direction_downstream: 10
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# LAP3

*leucine aminopeptidase 3* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.23× (z +10.9, q 8e-25, up in 38 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +8.6, q 1e-15, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.586× (z -10.3, q 5e-22, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MX1]] (+0.89, fdr 7e-06), [[CMPK2]] (+0.89, fdr 7e-06), [[OAS2]] (+0.89, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[TRIM22]] → it (grade B ⚠); 10 go from it, the strongest it → [[IRF9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 20.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.23×** | +10.9 | 8e-25 | 38/47 (J82, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.97×** | +8.8 | 3e-16 | 32/43 (J82, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +8.6 | 1e-15 | 34/48 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.72×** | +6.8 | 2e-09 | 30/45 (J82, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +4.7 | 3e-04 | 27/47 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +4.6 | 5e-04 | 33/47 (SW480, CFPAC-1, …) | two highest doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.38×** | +4.1 | 0.004 | 26/48 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.012 | 25/47 (C32, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.31×** | +3.5 | 0.029 | 23/49 (C32, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.19× | +3.2 | 0.069 | 12/48 (SK-MEL-2, NCI-H2347, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.087 | 21/48 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.10 | 20/48 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.11 | 15/48 (SNU-423, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 20.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.586×** | -10.3 | 5e-22 | 33/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -9.6 | 2e-19 | 37/47 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.498×** | -9.5 | 6e-19 | 38/48 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.548×** | -8.2 | 4e-14 | 37/48 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.563×** | -7.8 | 6e-13 | 35/48 (HepG2/C3A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.697×** | -6.9 | 4e-10 | 34/48 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.703×** | -6.8 | 1e-09 | 31/49 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.612×** | -6.7 | 2e-09 | 31/48 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.627×** | -6.3 | 1e-08 | 30/48 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.645×** | -6.0 | 1e-07 | 29/48 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.747×** | -5.6 | 1e-06 | 32/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.666×** | -5.5 | 2e-06 | 33/48 (SW 900, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.678×** | -5.3 | 5e-06 | 30/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.783×** | -4.7 | 1e-04 | 26/48 (A498, COLO 205, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.710×** | -4.7 | 1e-04 | 29/48 (BT-474, COLO 205, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.529×** | -4.5 | 2e-04 | 30/49 (A498, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.724×** | -4.4 | 4e-04 | 29/47 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 20. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 105 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.350× (z -12.8) |
| [[A549 (line)]] | wt | 77.9 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.366× (z -11.1) |
| [[BT-474 (line)]] | alt | 62.8 | 0 | 6 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0565× (z -18.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 90.3 | 0 | 6 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.334× (z -14.2) |
| [[RKO (line)]] | wt | 112 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 131 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -18.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -14.8) |
| [[SW480 (line)]] | alt | 33.4 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.32× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -10.0) |
| [[A498 (line)]] | wt | 123 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.377× (z -13.4) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.439× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 146 | 1 | 3 | [[Binimetinib (drug)]] 5 µM 2.47× (z +8.5) | [[Tofacitinib (drug)]] 5 µM 0.327× (z -14.2) |
| [[COLO 205 (line)]] | alt | 198 | 0 | 4 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.283× (z -13.5) |
| [[A-172 (line)]] | wt | 78.6 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.393× (z -9.8) |
| [[A-427 (line)]] | wt | 38.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -9.6) |
| [[C-33 A (line)]] | alt | 87.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -9.0) |
| [[HCT15 (line)]] | alt | 38.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.25× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 42.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +11.7) | — |
| [[J82 (line)]] | alt | 70.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.21× (z +17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[LS 180 (line)]] | wt | 44.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 26.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.81× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 77.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.292× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 62.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.217× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.416× (z -9.6) |
| [[C32 (line)]] | wt | 58.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.78× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 33.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +12.5) | — |
| [[HOP62 (line)]] | alt | 26.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[KATO III (line)]] | alt | 84.2 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.474× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 85.8 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.339× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 61.1 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.396× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 127 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.404× (z -13.3) |
| [[SW 900 (line)]] | alt | 108 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.320× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -8.5) |
| [[Hs 766T (line)]] | wt | 49.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 29.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 26.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H23 (line)]] | alt | 68.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.334× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 59.3 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.431× (z -8.8) |
| [[PANC-1 (line)]] | alt | 52.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[RPMI-7951 (line)]] | alt | 91.1 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.479× (z -8.5) |
| [[SHP-77 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.71× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 98.4 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.419× (z -9.0) |
| [[SW1417 (line)]] | alt | 43.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.354× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 20), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MX1]] | +0.89 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[CMPK2]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[OAS2]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 478 |
| [[OAS3]] | +0.87 | +0.83 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 623 |
| [[PLSCR1]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT; STRING 426 |
| [[USP18]] | +0.85 | +0.81 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 439 |
| [[STAT1]] | +0.85 | +0.85 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 779 |
| [[PARP14]] | +0.85 | +0.86 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 434 |
| [[EIF2AK2]] | +0.84 | +0.77 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[MX2]] | +0.84 | +0.78 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[IFIT1]] | +0.84 | +0.83 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 448 |
| [[PARP9]] | +0.84 | +0.79 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 537 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 38, C 0. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM22]] | B | TRIM22 activity raises LAP3's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.88× lower at baseline in the lines without TRIM22 | 0.001 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[OAS2]] | B | OAS2 activity raises LAP3's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without OAS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[RASGRP3]] | B | RASGRP3 activity raises LAP3's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 1.79× lower at baseline in the lines without RASGRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[CCDC194]] | B | CCDC194 activity raises LAP3's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without CCDC194 | 0.003 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[OAS1]] | B | OAS1 activity raises LAP3's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.93× lower at baseline in the lines without OAS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises LAP3's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.80× lower at baseline in the lines without MX1 | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[IFI6]] | B | IFI6 activity raises LAP3's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.97× lower at baseline in the lines without IFI6 | 0.006 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity strengthens LAP3's drug response | lines that do not express TRIM22 (18) vs lines expressing it (30) | the lines without TRIM22 respond 0.83× as strongly (z diff +0.30); strongest at Tucidinostat 5 µM: 0.82x vs 0.66x (z diff +2.4) | 0.006 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1; target measured in part of the lines; both ways; artifact flags |
| [[SAMD9L]] | B | SAMD9L activity raises LAP3's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.54× lower at baseline in the lines without SAMD9L | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[GBP4]] | B | GBP4 activity raises LAP3's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.57× lower at baseline in the lines without GBP4 | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[IFI27]] | B | IFI27 activity raises LAP3's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.68× lower at baseline in the lines without IFI27 | 0.007 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[SLC15A3]] | B | SLC15A3 activity raises LAP3's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 1.63× lower at baseline in the lines without SLC15A3 | 0.010 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF9]] | C | LAP3's natural level strengthens IRF9's drug response | LAP3's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.79, reverse -0.06; direction clear | 3e-04 | ⚠ tissue can mimic it; precision caveat |
| [[CMTR1]] | C | LAP3's natural level strengthens CMTR1's drug response | LAP3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse -0.14; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM25]] | C | LAP3's natural level strengthens TRIM25's drug response | LAP3's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.69, reverse -0.04; direction clear | 0.013 | ⚠ tissue can mimic it; precision caveat |
| [[REC8]] | C | LAP3's natural level strengthens REC8's drug response | LAP3's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.70, reverse -0.02; direction clear | 0.017 | ⚠ tissue can mimic it; precision caveat |
| [[PML]] | C | LAP3's natural level strengthens PML's drug response | LAP3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68, reverse -0.04; direction clear | 0.024 | ⚠ tissue can mimic it; precision caveat |
| [[ADAR]] | C | LAP3's natural level strengthens ADAR's drug response | LAP3's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.67, reverse -0.20; direction not clear | 0.025 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | LAP3's natural level strengthens HELZ2's drug response | LAP3's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.14; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | LAP3's natural level strengthens IFIT5's drug response | LAP3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.19; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SAMHD1]] | C | LAP3's natural level strengthens SAMHD1's drug response | LAP3's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.06; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PNPT1]] | C | LAP3's natural level strengthens PNPT1's drug response | LAP3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.21; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.862). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.9, 54.7); signed map (65.3, 32.6). **Vector** length 147, 53.4% of its response variance represented; |z| ≥ 3 in 1,437 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.80 to 23); *Interferon Signaling* (reactome, mean cos +0.75 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.78 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.6 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +4.7 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +3.3 | +4.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.1 | -6.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -9.6 | -10.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -9.1 | -6.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.9 | -6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.5 | -5.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -8.2 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | leucine aminopeptidase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32 — chr4:17,577,198-17,607,972 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LAPEP, LAP; previously PEPS |
| Gene groups (HGNC) | Aminopeptidases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, COMPLEMENT, INTERFERON_GAMMA_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [P28838](https://www.uniprot.org/uniprotkb/P28838) (Cytosol aminopeptidase):

> Cytosolic metallopeptidase that catalyzes the removal of unsubstituted N-terminal hydrophobic amino acids from various peptides. The presence of Zn(2+) ions is essential for the peptidase activity, and the association with other cofactors can modulate the substrate spectificity of the enzyme. For instance, in the presence of Mn(2+), it displays a specific Cys-Gly hydrolyzing activity of Cys-Gly-S-conjugates. Involved in the metabolism of glutathione and in the degradation of glutathione …

**Summary**, from NCBI Gene [51056](https://www.ncbi.nlm.nih.gov/gene/51056):

> Predicted to enable peptidase activity. Predicted to be involved in proteolysis. Located in several cellular components, including extracellular exosome; focal adhesion; and mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18449) · Entrez [51056](https://www.ncbi.nlm.nih.gov/gene/51056) · UniProt [P28838](https://www.uniprot.org/uniprotkb/P28838) · Ensembl [ENSG00000002549](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000002549)

## Data

Gene col 20: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 20); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 20, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 20]; `tensor/DDL_lfc|DDL_z.npy` [20]; `embed/gene_vectors.npy` [20]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 20 or target_col == 20). Every well: [[LAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

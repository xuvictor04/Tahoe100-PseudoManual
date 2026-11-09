---
symbol: "SPOP"
type: "gene"
col: 4251
ensembl_id: "ENSG00000121067"
name: "speckle type BTB/POZ protein"
location: "17q21.33"
module: 12
arm: "+"
pooled_cpm: 95.29
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SPOP

*speckle type BTB/POZ protein* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.14× (z +10.3, q 2e-22, up in 38 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 4 lines (SW480 3.63×, COLO 205 5.08×, A-427 3.58×, LoVo 3.45×); [[PH-797804 (drug)]] 5 µM in 2 lines (SW480 3.23×, HEC-1-A 3.12×); [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 1.66×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.450× (z -29.2, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM4]] (+0.73, fdr 7e-06), [[CCDC174]] (+0.70, fdr 7e-06), [[VIRMA]] (+0.69, fdr 7e-06); moves opposite to [[TTL]] (-0.62, fdr 1e-05), [[HPRT1]] (-0.62, fdr 7e-06), [[SMG1P3]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4251.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 4 lines (SW480 3.63×, COLO 205 5.08×, A-427 3.58×, LoVo 3.45×); [[PH-797804 (drug)]] 5 µM in 2 lines (SW480 3.23×, HEC-1-A 3.12×); [[Homoharringtonine (drug)]] 5 µM in 1 line (LoVo 1.66×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +10.3 | 2e-22 | 38/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +6.1 | 4e-07 | 27/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.15× | +3.7 | 0.034 | 10/48 (SW1417, SNU-423, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.15× | +3.7 | 0.034 | 16/49 (PANC-1, SW480, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.036 | 11/47 (HS-578T, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.10× | +3.5 | 0.051 | 2/48 (BT-474, Hs 766T) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.26× | +3.1 | 0.12 | 17/47 (HOP62, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.12 | 10/48 (Panc 03.27, HOP62, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.14 | 2/49 (Hs 766T, LOX-IMVI) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4251.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.450×** | -29.2 | 0e+00 | 47/49 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.468×** | -18.9 | 0e+00 | 43/48 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.535×** | -16.2 | 0e+00 | 44/48 (A498, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.531×** | -15.7 | 0e+00 | 38/44 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.548×** | -15.6 | 0e+00 | 41/49 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.552×** | -14.8 | 0e+00 | 39/50 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.599×** | -13.3 | 3e-38 | 44/48 (A498, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.603×** | -13.1 | 3e-37 | 41/48 (A498, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.593×** | -12.5 | 5e-34 | 38/45 (SK-MEL-2, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.623×** | -11.8 | 3e-30 | 42/47 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.638×** | -11.6 | 2e-29 | 46/48 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.679×** | -10.0 | 7e-22 | 39/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.717×** | -8.6 | 4e-16 | 32/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.724×** | -8.4 | 3e-15 | 33/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.729×** | -8.2 | 1e-14 | 38/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.728×** | -7.5 | 2e-12 | 34/48 (KATO III, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.761×** | -7.0 | 6e-11 | 27/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.622×** | -6.4 | 4e-09 | 33/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.690×** | -5.0 | 1e-05 | 30/49 (A498, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.820×** | -4.9 | 2e-05 | 23/48 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.827×** | -4.9 | 2e-05 | 23/48 (MIA PaCa-2, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.828×** | -4.9 | 2e-05 | 25/48 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.701×** | -4.8 | 3e-05 | 27/48 (CFPAC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.853× | -3.9 | 0.002 | 16/48 (SW 1271, NCI-H1792, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.766×** | -3.6 | 0.006 | 20/48 (CFPAC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 84.1 | 0 | 15 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -22.6) |
| [[A498 (line)]] | wt | 115 | 0 | 11 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.301× (z -19.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -18.4) |
| [[KATO III (line)]] | alt | 141 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -15.3) |
| [[NCI-H1792 (line)]] | alt | 115 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -17.8) |
| [[HEC-1-A (line)]] | alt | 126 | 1 | 8 (6 ⚠) | [[PH-797804 (drug)]] 5 µM 3.12× (z +9.3) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -15.0) |
| [[C32 (line)]] | wt | 117 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0992× (z -25.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -21.6) |
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -21.1) |
| [[COLO 205 (line)]] | alt | 142 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.08× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -15.2) |
| [[H4 (line)]] | wt | 102 | 0 | 6 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -13.1) |
| [[HOP62 (line)]] | alt | 109 | 0 | 6 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -22.7) |
| [[HT-29 (line)]] | alt | 101 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -13.6) |
| [[LoVo (line)]] | wt | 83.0 | 2 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.45× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 85.0 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -20.3) |
| [[PANC-1 (line)]] | alt | 109 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -23.7) |
| [[SW480 (line)]] | alt | 116 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.63× (z +10.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -14.4) |
| [[A-427 (line)]] | wt | 123 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.58× (z +9.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -24.1) |
| [[HS-578T (line)]] | alt | 84.7 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 104 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -18.8) |
| [[A-172 (line)]] | wt | 80.2 | 0 | 4 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -14.6) |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.416× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -9.4) |
| [[LS 180 (line)]] | wt | 90.3 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 59.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 74.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 110 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -16.1) |
| [[RKO (line)]] | wt | 75.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 87.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0602× (z -29.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.2) |
| [[SNU-423 (line)]] | alt | 90.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -16.1) |
| [[SW 900 (line)]] | alt | 109 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -20.0) |
| [[C-33 A (line)]] | alt | 87.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -14.7) |
| [[RPMI-7951 (line)]] | alt | 79.7 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -12.1) |
| [[A549 (line)]] | wt | 87.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -13.7) |
| [[AN3 CA (line)]] | alt | 59.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 54.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -17.0) |
| [[CHP-212 (line)]] | wt | 193 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.310× (z -8.9) |
| [[HCT15 (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -10.8) |
| [[Hs 766T (line)]] | wt | 60.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 63.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -13.8) |
| [[SNU-1 (line)]] | wt | 116 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -11.1) |
| [[SW1417 (line)]] | alt | 77.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -15.7) |
| [[BT-474 (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.464× (z -8.5) ⚠ cell-cycle shift, explains ~18% of this change |
| [[J82 (line)]] | alt | 67.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 64.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.375× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 86.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -17.5) |
| [[NCI-H661 (line)]] | alt | 74.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -8.5) |
| [[SHP-77 (line)]] | alt | 71.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -12.3) |
| [[SW 1271 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW48 (line)]] | wt | 50.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -9.9) |
| [[NCI-H2122 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM4]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[KLHL20]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 | same gene group; STRING 924 |
| [[SNRPB2]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[CIR1]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[COIL]] | +0.66 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[MED19]] | +0.66 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[SCAND1]] | +0.65 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[TCEAL8]] | +0.65 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[MFAP1]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[PIGBOS1]] | +0.65 | +0.44 / +0.70 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTL]] | -0.62 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[HPRT1]] | -0.62 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[SMG1P3]] | -0.62 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[ITPR3]] | -0.61 | -0.46 / -0.67 | both halves | 3e-05 |  |
| [[IPO5]] | -0.59 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[SRPK1]] | -0.57 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[CERS2]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.708). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.0, -5.9); signed map (-9.6, -10.0). **Vector** length 117, 36.7% of its response variance represented; |z| ≥ 3 in 1,327 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +11.4 | +10.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.7 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.1 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | -6.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.7 | +3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.4 | +2.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.0 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +2.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -18.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -5.7 | -15.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -5.6 | -12.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -14.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -8.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -4.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.5 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | speckle type BTB/POZ protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:49,598,884-49,678,163 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TEF2, BTBD32 |
| Gene groups (HGNC) | BTB domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 8 pathways, smallest: SPOP-mediated proteasomal degradation of PD-L1(CD274); Hedgehog 'on' state; Regulation of PD-L1(CD274) Post-translational modification |
| Matched by | ensembl_id |

**Function**, from UniProt [O43791](https://www.uniprot.org/uniprotkb/O43791) (Speckle-type POZ protein):

> Component of a cullin-RING-based BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex that mediates the ubiquitination of target proteins, leading most often to their proteasomal degradation. In complex with CUL3, involved in ubiquitination and proteasomal degradation of BRMS1, DAXX, PDX1/IPF1, GLI2 and GLI3. In complex with CUL3, involved in ubiquitination of MACROH2A1 and BMI1; this does not lead to their proteasomal degradation. Inhibits transcriptional activation of PDX1/IPF1 targets, …

**Summary**, from NCBI Gene [8405](https://www.ncbi.nlm.nih.gov/gene/8405):

> This gene encodes a protein that may modulate the transcriptional repression activities of death-associated protein 6 (DAXX), which interacts with histone deacetylase, core histones, and other histone-associated proteins. In mouse, the encoded protein binds to the putative leucine zipper domain of macroH2A1.2, a variant H2A histone that is enriched on inactivated X chromosomes. The BTB/POZ domain of this protein has been shown in other proteins to mediate transcriptional repression and to …

**Accessions** — [HGNC:11254](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11254) · Entrez [8405](https://www.ncbi.nlm.nih.gov/gene/8405) · UniProt [O43791](https://www.uniprot.org/uniprotkb/O43791) · Ensembl [ENSG00000121067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121067)

## Data

Gene col 4251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4251); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4251]; `tensor/DDL_lfc|DDL_z.npy` [4251]; `embed/gene_vectors.npy` [4251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4251 or target_col == 4251). Every well: [[SPOP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPOP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "LEMD3"
type: "gene"
col: 10460
ensembl_id: "ENSG00000174106"
name: "LEM domain containing 3"
location: "12q14.3"
module: 15
arm: "+"
pooled_cpm: 96.55
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# LEMD3

*LEM domain containing 3* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.57× (z +16.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.399× (z -15.3, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SW48 0.0714×, SW480 0.227×, HEC-1-A 0.204×, NCI-H2347 0.251×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H2347 0.244×, A-427 0.239×, NCI-H2030 0.203×, A498 0.255×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.203×, NCI-H2347 0.315×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPBP1L1]] (+0.68, fdr 1e-05), [[KIAA2026]] (+0.67, fdr 1e-05), [[WDR20]] (+0.66, fdr 1e-05); moves opposite to [[RPAP3]] (-0.62, fdr 4e-05), [[CYB5R1]] (-0.61, fdr 3e-05), [[MOCS2]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10460.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.57×** | +16.3 | 0e+00 | 48/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +12.7 | 2e-34 | 45/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.02×** | +12.2 | 1e-31 | 48/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.90×** | +11.1 | 2e-26 | 48/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +10.9 | 8e-26 | 43/49 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.15×** | +10.3 | 1e-22 | 44/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.73×** | +9.0 | 2e-17 | 44/48 (SW480, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +8.9 | 5e-17 | 40/48 (SK-MEL-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +8.7 | 1e-16 | 34/48 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +8.4 | 2e-15 | 44/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +7.7 | 9e-13 | 38/48 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.9 | 2e-07 | 35/50 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +5.5 | 2e-06 | 35/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +4.9 | 4e-05 | 34/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.008 | 26/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.049 | 20/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10460.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (SW48 0.0714×, SW480 0.227×, HEC-1-A 0.204×, NCI-H2347 0.251×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H2347 0.244×, A-427 0.239×, NCI-H2030 0.203×, A498 0.255×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SHP-77 0.203×, NCI-H2347 0.315×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -15.3 | 0e+00 | 43/44 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.465×** | -13.3 | 1e-37 | 46/49 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.629×** | -7.4 | 2e-11 | 35/45 (SHP-77, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.881× | -3.1 | 0.26 | 11/48 (LOX-IMVI, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 74.6 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 77.6 | 8 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -11.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 92.0 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -13.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 101 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -14.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 93.9 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -20.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 102 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 137 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.65× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -12.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 70.8 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +16.6) | — |
| [[NCI-H1573 (line)]] | alt | 117 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 136 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 103 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -18.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 152 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.07× (z +16.6) | — |
| [[NCI-H1792 (line)]] | alt | 89.9 | 4 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 76.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +14.5) | — |
| [[SW48 (line)]] | wt | 119 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.56× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.0714× (z -22.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 104 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -15.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 82.6 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -11.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 78.4 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -14.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 108 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -15.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 76.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -9.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 109 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -11.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 106 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -17.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 101 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -11.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 54.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -16.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 114 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 142 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -12.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 54.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 112 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -15.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 131 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.4) | — |
| [[SNU-1 (line)]] | wt | 87.4 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.164× (z -13.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 94.5 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -13.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 160 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -16.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 90.8 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 118 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -16.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 76.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -14.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 110 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.96× (z +15.8) | — |
| [[Panc 03.27 (line)]] | alt | 59.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 80.8 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -13.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 46.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +10.1) | — |
| [[C32 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -10.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 97.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 75.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -11.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 154 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPBP1L1]] | +0.68 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[KIAA2026]] | +0.67 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[WDR20]] | +0.66 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[PHC2-AS1]] | +0.65 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[POC1B-AS1]] | +0.64 | +0.43 / +0.38 | both halves | 6e-05 |  |
| [[NR2C2]] | +0.63 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[PTGR3]] | +0.62 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[ENDOG]] | +0.61 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[PRDM10]] | +0.61 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[C2orf42]] | +0.61 | +0.37 / +0.44 | both halves | 8e-05 |  |
| [[TRIM7]] | +0.60 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[HERPUD2]] | +0.60 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP3]] | -0.62 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CYB5R1]] | -0.61 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[MOCS2]] | -0.57 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[ALAS1]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[DRG2]] | -0.55 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[STAM2]] | -0.54 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[FLNC]] | -0.54 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[SOGA3]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[SH3PXD2B]] | -0.54 | -0.23 / -0.45 | both halves | 6e-04 |  |
| [[HUS1]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[COMMD2]] | -0.53 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[TBC1D19]] | -0.52 | -0.42 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LEMD3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TRIM7]] | B | TRIM7 activity lowers LEMD3's level | lines that do not express TRIM7 (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without TRIM7 | 0.089 | ⚠ within organs, on part of the lines; also absent: IRAK2, A4GALT, PAPSS2; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.634). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.9, 19.9); signed map (17.6, -5.4). **Vector** length 75.7, 21.5% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.4 | +10.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +8.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.9 | +8.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.8 | -0.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | -1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.0 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | LEM domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.3 — chr12:65,169,583-65,248,355 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAN1 |
| Gene groups (HGNC) | LEM domain containing |
| Reactome | 21 pathways, smallest: Depolymerization of the Nuclear Lamina; Initiation of Nuclear Envelope (NE) Reformation; RND1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2U8](https://www.uniprot.org/uniprotkb/Q9Y2U8) (Inner nuclear membrane protein Man1):

> Can function as a specific repressor of TGF-beta, activin, and BMP signaling through its interaction with the R-SMAD proteins. Antagonizes TGF-beta-induced cell proliferation arrest.

**Summary**, from NCBI Gene [23592](https://www.ncbi.nlm.nih.gov/gene/23592):

> This locus encodes a LEM domain-containing protein. The encoded protein functions to antagonize transforming growth factor-beta signaling at the inner nuclear membrane. Two transcript variants encoding different isoforms have been found for this gene. Mutations in this gene have been associated with osteopoikilosis, Buschke-Ollendorff syndrome and melorheostosis.[provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:28887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28887) · Entrez [23592](https://www.ncbi.nlm.nih.gov/gene/23592) · UniProt [Q9Y2U8](https://www.uniprot.org/uniprotkb/Q9Y2U8) · Ensembl [ENSG00000174106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174106)

## Data

Gene col 10460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10460); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10460]; `tensor/DDL_lfc|DDL_z.npy` [10460]; `embed/gene_vectors.npy` [10460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10460 or target_col == 10460). Every well: [[LEMD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LEMD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

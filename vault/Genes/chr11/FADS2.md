---
symbol: "FADS2"
type: "gene"
col: 5609
ensembl_id: "ENSG00000134824"
name: "fatty acid desaturase 2"
location: "11q12.2"
module: 86
arm: "+"
pooled_cpm: 37.86
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 18
n_dd_up_clean: 14
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# FADS2

*fatty acid desaturase 2* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.04× (z +18.9, q 0e+00, up in 38 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +15.5, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.513× (z -16.0, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FADS1]] (+0.78, fdr 7e-06, ⚠ same locus), [[FASN]] (+0.70, fdr 7e-06), [[ACAT2]] (+0.66, fdr 7e-06), [[DHCR24]] (+0.65, fdr 7e-06); moves opposite to [[PDRG1]] (-0.53, fdr 4e-05), [[SEC62]] (-0.50, fdr 4e-05), [[RBMX2]] (-0.50, fdr 4e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5609.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +18.9 | 0e+00 | 38/42 (A549, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +15.5 | 0e+00 | 40/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +15.3 | 0e+00 | 34/37 (Panc 03.27, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.76×** | +13.6 | 8e-40 | 35/48 (A549, HOP62, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | **1.68×** | +12.5 | 8e-34 | 34/48 (A549, Panc 03.27, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +10.9 | 1e-25 | 28/38 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.59×** | +7.6 | 3e-12 | 27/47 (HOP62, A549, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.40×** | +5.7 | 1e-06 | 24/47 (A549, SW 900, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.35×** | +4.9 | 6e-05 | 21/45 (SW480, HT-29, …) | top dose only |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.9 | 6e-05 | 24/47 (HOP62, A549, …) | top dose only | plate-row cell shift |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.34×** | +4.8 | 9e-05 | 18/48 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift |
| [[Berbamine (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 2e-04 | 21/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.32×** | +4.6 | 2e-04 | 18/47 (SW480, NCI-H23, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.31×** | +4.5 | 3e-04 | 18/48 (A-172, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +4.3 | 6e-04 | 14/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.19× | +4.2 | 9e-04 | 20/48 (A549, SNU-423, …) | rises with dose |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.005 | 19/48 (A549, HOP62, …) | rises with dose | plate-row cell shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.007 | 16/48 (A549, A-172, …) | top dose only |  |
| [[Ritonavir (drug)]] 5 µM |  | 1.16× | +3.6 | 0.008 | 17/48 (PANC-1, LS 180, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.010 | 18/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.021 | 18/47 (HOP62, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5609.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.513×** | -16.0 | 0e+00 | 39/48 (A-427, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.461×** | -13.1 | 7e-37 | 35/48 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.568×** | -9.2 | 5e-18 | 33/48 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.778×** | -6.0 | 3e-07 | 23/48 (A-427, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.710×** | -5.8 | 7e-07 | 23/48 (KATO III, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.806×** | -5.2 | 2e-05 | 23/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.758×** | -4.4 | 8e-04 | 20/48 (BT-474, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.776×** | -4.3 | 0.001 | 14/47 (SW 1271, SNU-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.778×** | -4.2 | 0.001 | 20/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.789×** | -4.0 | 0.003 | 20/47 (PANC-1, BT-474, …) | rises with dose |  |
| [[Salicylic acid (drug)]] 5 µM |  | 0.850× | -3.9 | 0.005 | 15/48 (CHP-212, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.797×** | -3.9 | 0.005 | 17/48 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.802×** | -3.7 | 0.008 | 15/47 (LS 180, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.817×** | -3.4 | 0.025 | 18/48 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.755×** | -3.4 | 0.026 | 9/48 (A-427, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.684×** | -3.4 | 0.026 | 9/48 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 25.7 | 7 (2 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 4.33× (z +15.3) | — |
| [[NCI-H460 (line)]] | wt | 30.8 | 4 (1 ⚠) | 3 | [[Cepharanthine (drug)]] 5 µM 2.58× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.8) |
| [[A549 (line)]] | wt | 29.4 | 6 (2 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 6.33× (z +17.5) | — |
| [[A-172 (line)]] | wt | 128 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.9) | — |
| [[A-427 (line)]] | wt | 107 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -19.2) |
| [[C-33 A (line)]] | alt | 92.8 | 3 | 2 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 3.08× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 46.9 | 4 (2 ⚠) | 1 | [[Berbamine (drug)]] 5 µM 2.80× (z +10.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -8.5) |
| [[LS 180 (line)]] | wt | 33.8 | 3 (1 ⚠) | 2 | [[Berbamine (drug)]] 5 µM 3.61× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 41.0 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.40× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Berbamine (drug)]] 5 µM 3.51× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.2) |
| [[PANC-1 (line)]] | alt | 56.7 | 4 (2 ⚠) | 1 | [[Cepharanthine (drug)]] 5 µM 2.48× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.7) |
| [[SW 900 (line)]] | alt | 34.9 | 3 | 2 | [[Cepharanthine (drug)]] 5 µM 5.19× (z +13.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -10.1) |
| [[BT-474 (line)]] | alt | 177 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 27.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -15.2) |
| [[NCI-H2030 (line)]] | alt | 92.7 | 2 | 2 | [[Cepharanthine (drug)]] 5 µM 2.75× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 13.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.35× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.4) |
| [[SNU-423 (line)]] | alt | 18.0 | 3 | 0 | [[Cepharanthine (drug)]] 5 µM 4.68× (z +11.7) | — |
| [[A498 (line)]] | wt | 48.9 | 2 | 0 | [[Berbamine (drug)]] 5 µM 2.30× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 24.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 46.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 56.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -8.6) |
| [[SW480 (line)]] | alt | 21.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +13.5) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -10.9) |
| [[AN3 CA (line)]] | alt | 118 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -16.6) |
| [[H4 (line)]] | wt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -11.2) |
| [[HS-578T (line)]] | alt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 36.5 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 3.75× (z +8.5) | — |
| [[LoVo (line)]] | wt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +14.2) | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.62× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +8.5) | — |
| [[RKO (line)]] | wt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -8.5) |
| [[SW1417 (line)]] | alt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +8.9) | — |
| [[C32 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FADS1]] | +0.78 | +0.80 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_BILE_ACID_METABOLISM; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[FASN]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 712 |
| [[ACAT2]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 438 |
| [[DHCR24]] | +0.65 | +0.74 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_BILE_ACID_METABOLISM |
| [[DHCR7]] | +0.64 | +0.71 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 516 |
| [[SCD]] | +0.64 | +0.68 / +0.57 | both halves | 1e-05 | same gene group; pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 971 |
| [[FDPS]] | +0.63 | +0.66 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[ACLY]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 514 |
| [[PCSK9]] | +0.60 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[PPIA]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[HMGCR]] | +0.59 | +0.68 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 467 |
| [[IDI1]] | +0.58 | +0.59 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_BILE_ACID_METABOLISM |
| [[MSMO1]] | +0.57 | +0.63 / +0.61 | both halves | 7e-06 | STRING 631 |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDRG1]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[SEC62]] | -0.50 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[RBMX2]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[C18orf21]] | -0.48 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[PUS3]] | -0.48 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[SURF2]] | -0.47 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[H3-3B]] | -0.47 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[CEP290]] | -0.47 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[MRPS31]] | -0.47 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[NEMF]] | -0.46 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[CROCCP2-1]] | -0.45 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[MRPL46]] | -0.45 | -0.32 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.4, -50.0); signed map (-51.8, 31.7). **Vector** length 115, 30.1% of its response variance represented; |z| ≥ 3 in 1,253 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metabolism of steroids* (reactome, mean cos +0.50 to 25); *Activation of gene expression by SREBF (SREBP)* (reactome, mean cos +0.51 to 16); *Cholesterol biosynthesis via desmosterol (Bloch pathway)* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +15.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +7.4 | +13.6 |
|  | [[Berbamine (drug)]] 5 µM |  | +6.5 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +15.3 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +4.1 | +7.6 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -13.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -16.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -3.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.8 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -2.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.5 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | fatty acid desaturase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,792,980-61,867,354 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FADSD6, D6D, TU13, DES6, SLL0262; previously LLCDL2 |
| Gene groups (HGNC) | Fatty acid desaturases; Cytochrome b5 domain containing |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, BILE_ACID_METABOLISM, MTORC1_SIGNALING |
| Reactome | 5 pathways, smallest: Linoleic acid (LA) metabolism; alpha-linolenic (omega3) and linoleic (omega6) acid metabolism; alpha-linolenic acid (ALA) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O95864](https://www.uniprot.org/uniprotkb/O95864) (Acyl-CoA 6-desaturase):

> Involved in the biosynthesis of highly unsaturated fatty acids (HUFA) from the essential polyunsaturated fatty acids (PUFA) linoleic acid (LA) (18:2n-6) and alpha-linolenic acid (ALA) (18:3n-3) precursors, acting as a fatty acyl-coenzyme A (CoA) desaturase that introduces a cis double bond at carbon 6 of the fatty acyl chain. Catalyzes the first and rate limiting step in this pathway which is the desaturation of LA (18:2n-6) and ALA (18:3n-3) into gamma-linoleate (GLA) (18:3n-6) and …

**Summary**, from NCBI Gene [9415](https://www.ncbi.nlm.nih.gov/gene/9415):

> The protein encoded by this gene is a member of the fatty acid desaturase (FADS) gene family. Desaturase enzymes regulate unsaturation of fatty acids through the introduction of double bonds between defined carbons of the fatty acyl chain. FADS family members are considered fusion products composed of an N-terminal cytochrome b5-like domain and a C-terminal multiple membrane-spanning desaturase portion, both of which are characterized by conserved histidine motifs. This gene is clustered with …

**Accessions** — [HGNC:3575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3575) · Entrez [9415](https://www.ncbi.nlm.nih.gov/gene/9415) · UniProt [O95864](https://www.uniprot.org/uniprotkb/O95864) · Ensembl [ENSG00000134824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134824)

## Data

Gene col 5609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5609); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5609]; `tensor/DDL_lfc|DDL_z.npy` [5609]; `embed/gene_vectors.npy` [5609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5609 or target_col == 5609). Every well: [[FADS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FADS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

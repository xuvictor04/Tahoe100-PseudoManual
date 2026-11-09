---
symbol: "ASF1B"
type: "gene"
col: 2540
ensembl_id: "ENSG00000105011"
name: "anti-silencing function 1B histone chaperone"
location: "19p13.12"
module: 71
arm: "+"
pooled_cpm: 15.52
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# ASF1B

*anti-silencing function 1B histone chaperone* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (22 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.18× (z +29.2, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.517× (z -6.9, q 3e-09, down in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~64% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.709× (z -5.1, q 1e-04, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C21orf58]] (+0.81, fdr 7e-06), [[RFWD3]] (+0.79, fdr 7e-06), [[CDCA5]] (+0.79, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[FAM111B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 22 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2540.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.18×** | +29.2 | 0e+00 | 44/46 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **3.91×** | +13.7 | 2e-40 | 43/47 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **3.43×** | +12.4 | 5e-33 | 39/45 (J82, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **3.19×** | +12.1 | 1e-31 | 43/47 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **2.90×** | +11.1 | 1e-26 | 41/46 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **2.84×** | +10.9 | 1e-25 | 40/46 (A498, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.83×** | +8.9 | 3e-17 | 33/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **2.31×** | +8.4 | 2e-15 | 29/41 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.79×** | +6.1 | 7e-08 | 29/47 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.75×** | +5.6 | 1e-06 | 10/20 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.61×** | +5.0 | 3e-05 | 24/46 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.39×** | +4.9 | 5e-05 | 26/47 (LoVo, RKO, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.59×** | +4.8 | 6e-05 | 22/47 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.37×** | +4.7 | 1e-04 | 22/45 (AsPC-1, NCI-H2030, …) | top dose only | composition shift |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.36×** | +4.6 | 2e-04 | 22/47 (HCT15, SW480, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.16×** | +4.2 | 8e-04 | 15/45 (PANC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.005 | 18/43 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.046 | 12/46 (SW480, A-427, …) | top dose only | plate-row cell shift |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.31×** | +2.8 | 0.095 | 6/46 (SW480, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2540.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.517×** | -6.9 | 3e-09 | 33/47 (A498, H4, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.709×** | -5.1 | 1e-04 | 28/47 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.609×** | -4.9 | 2e-04 | 25/47 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.741×** | -4.4 | 0.001 | 21/47 (A498, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.661×** | -4.3 | 0.002 | 17/46 (NCI-H2030, HEC-1-A, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.750×** | -4.2 | 0.002 | 22/47 (COLO 205, A-172, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.659×** | -4.2 | 0.002 | 21/43 (SW 900, SW48, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.672×** | -4.0 | 0.004 | 15/46 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.662×** | -3.9 | 0.006 | 19/47 (A-427, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.702×** | -3.7 | 0.012 | 18/46 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.704×** | -3.7 | 0.013 | 17/46 (HepG2/C3A, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.709×** | -3.6 | 0.015 | 15/47 (COLO 205, A498, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.578×** | -3.4 | 0.027 | 15/47 (SW480, A-172, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.715×** | -3.4 | 0.031 | 17/46 (HOP62, A498, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **0.798×** | -3.3 | 0.032 | 11/47 (NCI-H2030, hTERT-HPNE, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.733×** | -3.2 | 0.042 | 13/46 (SK-MEL-2, SW 1271, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.779×** | -3.1 | 0.073 | 12/47 (A-427, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.736×** | -3.0 | 0.095 | 8/46 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.754×** | -2.9 | 0.095 | 11/47 (A-172, A-427, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.818×** | -2.9 | 0.095 | 16/47 (HOP62, A549, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.34 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 26.2 | 7 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +18.0) | — |
| [[A498 (line)]] | wt | 13.9 | 3 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.54× (z +9.4) ⚠ cell-cycle shift, explains ~77% of this change | [[Selinexor (drug)]] 5 µM 0.196× (z -12.6) ⚠ cell-cycle shift, explains ~96% of this change |
| [[PANC-1 (line)]] | alt | 15.5 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.84× (z +17.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.07× (z +15.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.0977× (z -11.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 7.46 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +13.3) | [[Selinexor (drug)]] 0.5 µM 0.132× (z -9.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[A-172 (line)]] | wt | 20.4 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.137× (z -9.5) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.5 µM 0.156× (z -8.8) |
| [[A-427 (line)]] | wt | 27.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -9.7) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.208× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 38.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.9) ⚠ cell-cycle shift, explains ~84% of this change |
| [[J82 (line)]] | alt | 32.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +14.8) | — |
| [[HOP62 (line)]] | alt | 14.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 5.71 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +9.6) | [[Selinexor (drug)]] 5 µM 0.180× (z -9.1) ⚠ cell-cycle shift, explains ~96% of this change |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0799× (z -10.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SW1417 (line)]] | alt | 28.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +12.6) | — |
| [[A549 (line)]] | wt | 5.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +14.1) | — |
| [[AsPC-1 (line)]] | alt | 4.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.1× (z +16.5) | — |
| [[BT-474 (line)]] | alt | 17.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +14.6) | — |
| [[C-33 A (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +10.7) | — |
| [[C32 (line)]] | wt | 8.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 8.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +14.6) | — |
| [[COLO 205 (line)]] | alt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.14× (z +9.6) | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0441× (z -10.5) ⚠ cell-cycle shift, explains ~64% of this change |
| [[HCT15 (line)]] | alt | 24.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.37× (z +11.3) | — |
| [[HepG2_C3A (line)]] | wt | 4.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.2× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.15× (z +13.0) | — |
| [[HS-578T (line)]] | alt | 6.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.3× (z +15.0) | — |
| [[HT-29 (line)]] | alt | 17.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.66× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 4.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.7× (z +11.3) | — |
| [[KATO III (line)]] | alt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +12.3) | — |
| [[LoVo (line)]] | wt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +17.7) | — |
| [[NCI-H1573 (line)]] | alt | 4.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +12.6) | — |
| [[NCI-H1792 (line)]] | alt | 4.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.9× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 16.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +14.0) | — |
| [[Panc 03.27 (line)]] | alt | 37.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +19.8) | — |
| [[RKO (line)]] | wt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.45× (z +15.7) | — |
| [[RPMI-7951 (line)]] | alt | 9.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.2× (z +13.1) | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.67× (z +14.6) | — |
| [[SW 900 (line)]] | alt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.28× (z +12.4) | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C21orf58]] | +0.81 | +0.79 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[RFWD3]] | +0.79 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[CDCA5]] | +0.79 | +0.71 / +0.81 | both halves | 7e-06 | STRING 603 |
| [[ATAD5]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 | STRING 425 |
| [[GINS4]] | +0.78 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[SPC25]] | +0.78 | +0.75 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 444 |
| [[ESCO2]] | +0.78 | +0.76 / +0.80 | both halves | 7e-06 |  |
| [[TK1]] | +0.78 | +0.74 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 648 |
| [[ZNF367]] | +0.77 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[DBF4B]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[HAUS8]] | +0.76 | +0.64 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM111B]] | B | FAM111B activity raises ASF1B's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 2.15× lower at baseline in the lines without FAM111B | 0.005 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises ASF1B's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.77× lower at baseline in the lines without E2F8 | 0.011 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ASF1B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers ASF1B's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[E2F2]] | B | E2F2 activity raises ASF1B's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.04× lower at baseline in the lines without E2F2 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises ASF1B's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.71× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[MCM10]] | C | MCM10 activity raises ASF1B's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.44× lower at baseline in the lines without MCM10 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises ASF1B's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.74× lower at baseline in the lines without AURKB | 0.072 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PKMYT1]] | C | PKMYT1 activity raises ASF1B's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.75× lower at baseline in the lines without PKMYT1 | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent |
| [[E2F1]] | C | E2F1 activity raises ASF1B's level | lines that do not express E2F1 (3) vs lines expressing it (47) | 2.63× lower at baseline in the lines without E2F1 | 0.095 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent |
| [[TP53]] | C | TP53 activity weakens ASF1B's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 16 not recorded | the TP53-altered lines respond 1.14× as strongly (z diff -0.97); strongest at Idarubicin (hydrochloride) 0.5 µM: 2.20x vs 0.82x (z diff -5.3) | 0.396 over the table, 0.017 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; the reference differs; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.809). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.4, -47.7); signed map (-41.4, -45.7). **Vector** length 119, 36.9% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.56 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +7.3 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +29.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.8 | +13.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.8 | +5.0 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +3.8 | +4.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.3 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +2.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | -6.0 | -4.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -5.8 | -6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | -5.6 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.7 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.8 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | anti-silencing function 1B histone chaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,119,512-14,136,613 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10604 |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVP2](https://www.uniprot.org/uniprotkb/Q9NVP2) (Histone chaperone ASF1B):

> Histone chaperone that facilitates histone deposition and histone exchange and removal during nucleosome assembly and disassembly. Cooperates with chromatin assembly factor 1 (CAF-1) to promote replication-dependent chromatin assembly. Also involved in the nuclear import of the histone H3-H4 dimer together with importin-4 (IPO4): specifically recognizes and binds newly synthesized histones with the monomethylation of H3 'Lys-9' (H3K9me1) and diacetylation at 'Lys-5' and 'Lys-12' of H4 …

**Summary**, from NCBI Gene [55723](https://www.ncbi.nlm.nih.gov/gene/55723):

> This gene encodes a member of the H3/H4 family of histone chaperone proteins and is similar to the anti-silencing function-1 gene in yeast. The encoded protein is the substrate of the tousled-like kinase family of cell cycle-regulated kinases, and may play a key role in modulating the nucleosome structure of chromatin by ensuring a constant supply of histones at sites of nucleosome assembly. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20996) · Entrez [55723](https://www.ncbi.nlm.nih.gov/gene/55723) · UniProt [Q9NVP2](https://www.uniprot.org/uniprotkb/Q9NVP2) · Ensembl [ENSG00000105011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105011)

## Data

Gene col 2540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2540); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2540]; `tensor/DDL_lfc|DDL_z.npy` [2540]; `embed/gene_vectors.npy` [2540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2540 or target_col == 2540). Every well: [[ASF1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASF1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

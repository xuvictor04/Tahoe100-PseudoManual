---
symbol: "WDR76"
type: "gene"
col: 1701
ensembl_id: "ENSG00000092470"
name: "WD repeat domain 76"
location: "15q15.3"
module: 6
arm: "+"
pooled_cpm: 19.07
n_lines_expressing: 48
n_dd_up: 42
n_dd_down: 37
n_dd_up_clean: 11
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# WDR76

*WD repeat domain 76* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (31 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.76× (z +14.9, q 0e+00, up in 35 of 45 measured lines) ⚠ cell-cycle shift, explains ~84% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.39× (z +4.8, q 4e-05, up in 19 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (13 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.630× (z -9.6, q 4e-19, down in 30 of 46 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Temsirolimus (drug)]] 0.5 µM: 0.726× (z -4.7, q 2e-04, down in 18 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC45]] (+0.95, fdr 7e-06), [[EXO1]] (+0.94, fdr 7e-06), [[MYBL2]] (+0.93, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); 1 goes from it, the strongest it → [[WDHD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 33 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 31 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **2.76×** | +14.9 | 0e+00 | 35/45 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **2.75×** | +14.2 | 2e-43 | 23/27 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.59×** | +13.9 | 8e-42 | 30/39 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.29×** | +12.1 | 1e-31 | 35/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.10×** | +10.9 | 2e-25 | 33/46 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **2.19×** | +10.6 | 4e-24 | 25/36 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.95×** | +9.7 | 2e-20 | 28/46 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.84×** | +8.9 | 3e-17 | 28/43 (PANC-1, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~87% of this change | **1.73×** | +7.7 | 8e-13 | 27/42 (SW480, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.68×** | +7.6 | 2e-12 | 25/46 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.65×** | +7.3 | 2e-11 | 25/45 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.64×** | +7.3 | 2e-11 | 26/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.60×** | +6.9 | 2e-10 | 26/45 (PANC-1, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.61×** | +6.7 | 8e-10 | 25/43 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.47×** | +5.7 | 6e-07 | 23/45 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.8 | 4e-05 | 19/45 (HT-29, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 8e-04 | 21/45 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.001 | 10/46 (HEC-1-A, A498, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.003 | 12/46 (SW 900, COLO 205, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +3.4 | 0.010 | 3/46 (NCI-H2347, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.014 | 11/46 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.015 | 9/46 (SW480, HT-29, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.043 | 6/46 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.21×** | +2.8 | 0.071 | 4/46 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.31×** | +2.8 | 0.074 | 7/46 (NCI-H2030, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +2.8 | 0.074 | 8/45 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.20×** | +2.7 | 0.096 | 6/43 (SW480, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1701.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.630×** | -9.6 | 4e-19 | 30/46 (LS 180, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.554×** | -8.7 | 1e-15 | 26/45 (H4, SNU-1, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.536×** | -6.5 | 1e-08 | 25/46 (SW480, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.741×** | -6.2 | 6e-08 | 22/46 (COLO 205, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.665×** | -6.0 | 2e-07 | 23/46 (COLO 205, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.692×** | -5.4 | 6e-06 | 23/45 (NCI-H23, HEC-1-A, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.726×** | -4.7 | 2e-04 | 18/43 (C32, Panc 03.27, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.692×** | -4.5 | 4e-04 | 14/46 (A-427, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.740×** | -4.4 | 5e-04 | 19/45 (HCT15, A498, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.692×** | -4.4 | 5e-04 | 16/46 (RKO, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.763×** | -4.4 | 5e-04 | 17/46 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.738×** | -4.3 | 8e-04 | 13/44 (RKO, A-427, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.816×** | -4.2 | 9e-04 | 15/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.668×** | -4.2 | 9e-04 | 9/46 (SW480, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.826×** | -4.0 | 0.003 | 22/44 (A-427, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.768×** | -3.9 | 0.003 | 10/45 (A-172, HOP62, …) | top dose only |  |
| [[palbociclib (drug)]] 5 µM |  | **0.574×** | -3.8 | 0.004 | 13/43 (SW480, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.780×** | -3.7 | 0.008 | 14/45 (SK-MEL-2, RKO, …) | rises with dose | low cells (technical?) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.790×** | -3.5 | 0.013 | 16/45 (KATO III, SW 1271, …) | top dose only |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.749×** | -3.5 | 0.013 | 13/46 (PANC-1, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.851× | -3.4 | 0.017 | 17/46 (KATO III, RKO, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.851× | -3.4 | 0.017 | 15/46 (RKO, HCT15, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.852× | -3.4 | 0.017 | 9/46 (NCI-H2030, HOP62, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.804×** | -3.2 | 0.026 | 11/46 (A-172, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.50 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 49.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -18.5) |
| [[PANC-1 (line)]] | alt | 24.5 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +11.4) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[SW480 (line)]] | alt | 17.1 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.59× (z +11.5) ⚠ toxic; cell-cycle shift, explains ~87% of this change | — |
| [[A-172 (line)]] | wt | 21.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.158× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 46.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -14.6) |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -8.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 8.12 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.173× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0539× (z -9.5) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HT-29 (line)]] | alt | 9.90 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.81× (z +9.5) | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.344× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0657× (z -16.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.310× (z -9.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW48 (line)]] | wt | 26.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.134× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC45]] | +0.95 | +0.95 / +0.94 | both halves | 7e-06 | STRING 462 |
| [[EXO1]] | +0.94 | +0.95 / +0.92 | both halves | 7e-06 | STRING 527 |
| [[MYBL2]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[DTL]] | +0.92 | +0.94 / +0.91 | both halves | 7e-06 | same gene group |
| [[MCM10]] | +0.91 | +0.92 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[FANCA]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[CLSPN]] | +0.90 | +0.90 / +0.87 | both halves | 7e-06 | STRING 513 |
| [[CENPK]] | +0.89 | +0.87 / +0.89 | both halves | 7e-06 |  |
| [[MCM3]] | +0.89 | +0.88 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[E2F1]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[MCM4]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | STRING 611 |
| [[CHAF1A]] | +0.88 | +0.89 / +0.84 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises WDR76's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.72× lower at baseline in the lines without E2F8 | 0.040 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises WDR76's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without E2F2 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises WDR76's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 8.1% of all compounds | 0.070 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TLCD3B]] | B | TLCD3B activity raises WDR76's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.23× lower at baseline in the lines without TLCD3B | 0.074 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[XRCC3]] | C | XRCC3's natural level weakens WDR76's drug response | XRCC3's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.19; direction not clear | 0.014 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CDC25A]] | C | CDC25A's natural level weakens WDR76's drug response | CDC25A's natural level across 42 lines (lineage-adjusted; a glimpse) | r -0.74, reverse -0.17; direction not clear | 0.016 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[DSCC1]] | C | DSCC1 activity raises WDR76's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.75× lower at baseline in the lines without DSCC1 | 0.041 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[MCM10]] | C | MCM10's natural level weakens WDR76's drug response | MCM10's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.69, reverse -0.28; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[E2F1]] | C | E2F1's natural level weakens WDR76's drug response | E2F1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.27; direction not clear | 0.068 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDHD1]] | C | WDR76's natural level weakens WDHD1's drug response | WDR76's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.45; direction not clear | 0.091 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.950). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.8, -45.0); signed map (-38.0, -44.6). **Vector** length 134, 41.6% of its response variance represented; |z| ≥ 3 in 1,258 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.71 to 65); *DNA strand elongation* (reactome, mean cos +0.76 to 28); *DNA Replication* (reactome, mean cos +0.76 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | +5.3 | +10.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | +5.1 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | +5.0 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.8 | +13.9 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +4.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +2.5 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.6 | +2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.5 | +3.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.5 | +1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +4.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -7.0 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -7.0 | -5.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -5.8 | -8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -4.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -3.9 | -6.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.7 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 76 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,826,980-43,868,412 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12973, Cmr1 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H967](https://www.uniprot.org/uniprotkb/Q9H967) (WD repeat-containing protein 76):

> Specifically binds 5-hydroxymethylcytosine (5hmC), suggesting that it acts as a specific reader of 5hmC.

**Summary**, from NCBI Gene [79968](https://www.ncbi.nlm.nih.gov/gene/79968):

> Enables enzyme binding activity. Involved in DNA damage response. Located in heterochromatin; nucleus; and site of DNA damage. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25773) · Entrez [79968](https://www.ncbi.nlm.nih.gov/gene/79968) · UniProt [Q9H967](https://www.uniprot.org/uniprotkb/Q9H967) · Ensembl [ENSG00000092470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092470)

## Data

Gene col 1701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1701); `tables/drug_effects.parquet` (88 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1701]; `tensor/DDL_lfc|DDL_z.npy` [1701]; `embed/gene_vectors.npy` [1701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1701 or target_col == 1701). Every well: [[WDR76 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR76.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

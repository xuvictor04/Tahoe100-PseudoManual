---
symbol: "ITPR1"
type: "gene"
col: 7474
ensembl_id: "ENSG00000150995"
name: "inositol 1,4,5-trisphosphate receptor type 1"
location: "3p26.1"
module: 13
arm: "+"
pooled_cpm: 118.67
n_lines_expressing: 35
n_dd_up: 16
n_dd_down: 31
n_dd_up_clean: 12
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 22
direction_downstream: 4
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ITPR1

*inositol 1,4,5-trisphosphate receptor type 1* — 3p26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.64× (z +17.9, q 0e+00, up in 25 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.275× (z -12.4, q 2e-32, down in 32 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LOXL2]] (+0.61, fdr 1e-05), [[TSHZ3]] (+0.59, fdr 1e-05), [[KHDRBS3]] (+0.59, fdr 1e-05); moves opposite to [[LINC01836]] (-0.51, fdr 5e-05), [[LATS2]] (-0.49, fdr 4e-05), [[ERBB2]] (-0.49, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[AFF3]] → it (grade B ⚠); 4 go from it, the strongest it → [[EFL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.64×** | +17.9 | 0e+00 | 25/33 (LOX-IMVI, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +13.8 | 4e-41 | 23/33 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +13.1 | 5e-37 | 20/33 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +9.7 | 4e-20 | 23/33 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +9.6 | 1e-19 | 24/33 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +8.5 | 2e-15 | 17/33 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +8.0 | 1e-13 | 20/34 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.55×** | +7.8 | 6e-13 | 15/33 (NCI-H460, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.0 | 2e-10 | 16/35 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.29×** | +6.6 | 2e-09 | 11/34 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.4 | 4e-06 | 10/33 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +5.0 | 2e-05 | 16/33 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.62×** | +4.6 | 2e-04 | 17/33 (A-172, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.003 | 12/34 (NCI-H23, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | 1.16× | +3.9 | 0.004 | 10/33 (NCI-H23, A-427, …) | top dose only | low cells (technical?) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.015 | 5/33 (NCI-H460, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.020 | 11/33 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.048 | 4/33 (C32, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.058 | 9/33 (PANC-1, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7474.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.275×** | -12.4 | 2e-32 | 32/34 (RPMI-7951, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.552×** | -10.1 | 2e-21 | 25/30 (A-427, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.421×** | -8.3 | 2e-14 | 26/33 (C32, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.635×** | -8.0 | 2e-13 | 24/33 (RPMI-7951, C32, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.664×** | -7.5 | 7e-12 | 24/34 (C32, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.667×** | -7.4 | 1e-11 | 26/33 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.789×** | -6.1 | 7e-08 | 22/34 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.730×** | -5.8 | 6e-07 | 25/33 (PANC-1, SW 1088, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.558×** | -5.6 | 1e-06 | 19/29 (C32, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.784×** | -5.2 | 1e-05 | 22/33 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.679×** | -5.1 | 2e-05 | 19/33 (A-172, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -5.0 | 3e-05 | 23/33 (C32, RPMI-7951, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.773×** | -4.7 | 1e-04 | 23/33 (NCI-H1792, A-427, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.620×** | -4.6 | 2e-04 | 18/31 (HOP62, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.782×** | -4.5 | 3e-04 | 20/33 (PANC-1, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.781×** | -4.3 | 5e-04 | 16/32 (A-172, RKO, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.783×** | -4.3 | 5e-04 | 15/33 (SK-MEL-2, SW 1088, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.791×** | -4.3 | 6e-04 | 17/33 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.793×** | -4.0 | 0.002 | 16/33 (SK-MEL-2, BT-474, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.807×** | -3.9 | 0.002 | 13/32 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.814×** | -3.8 | 0.004 | 16/34 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.815×** | -3.7 | 0.004 | 14/34 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 919 | 0 | 21 (15 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.238× (z -14.3) |
| [[PANC-1 (line)]] | alt | 100 | 2 (1 ⚠) | 11 (10 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.86× (z +12.0) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 2.13× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.257× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.193× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 537 | 0 | 13 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -22.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0838× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 1,015 | 0 | 11 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -21.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.159× (z -9.3) |
| [[HS-578T (line)]] | alt | 232 | 0 | 10 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -13.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 147 | 1 | 9 (9 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.88× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0754× (z -18.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 417 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0898× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 74.3 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.78× (z +15.0) | — |
| [[NCI-H2347 (line)]] | alt | 36.4 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +18.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.21× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 50.4 | 7 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +12.9) | — |
| [[SK-MEL-2 (line)]] | alt | 232 | 1 | 4 | [[Panobinostat (drug)]] 5 µM 2.72× (z +8.8) | [[Cobimetinib (drug)]] 5 µM 0.305× (z -10.1) |
| [[A-427 (line)]] | wt | 74.3 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.64× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -18.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 216 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -12.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 55.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +11.7) | — |
| [[H4 (line)]] | wt | 166 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -11.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 65.6 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 8.85× (z +13.7) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.226× (z -8.6) |
| [[HOP62 (line)]] | alt | 200 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 62.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.19× (z +13.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 118 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.480× (z -9.7) |
| [[C-33 A (line)]] | alt | 104 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 38.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.50× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.170× (z -9.4) ⚠ cell-cycle shift, explains ~18% of this change |
| [[NCI-H2030 (line)]] | alt | 52.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +11.5) | — |
| [[SW 1088 (line)]] | alt | 368 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0388× (z -15.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -9.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 28.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 28.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.96 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 28.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.7 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LOXL2]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[TSHZ3]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[KHDRBS3]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ZCCHC24]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ALK]] | +0.57 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[MTSS1]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TMEM255B]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[TRIM9]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.55 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[EPHB1]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[RGS17]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 | pathway: G alpha (i) signalling events |
| [[ITGB3]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 | pathway: Platelet activation, signaling and aggregation |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01836]] | -0.51 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[LATS2]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ERBB2]] | -0.49 | -0.36 / -0.52 | both halves | 1e-04 | pathway: Intracellular signaling by second messengers |
| [[MARK2]] | -0.48 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[RPRD2]] | -0.48 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[RNF115]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SORBS2]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[NFIB]] | -0.46 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 20, C 2. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFF3]] | B | AFF3 activity raises ITPR1's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 4.64× lower at baseline in the lines without AFF3 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[ITGB3]] | B | ITGB3 activity raises ITPR1's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.75× lower at baseline in the lines without ITGB3 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[INSYN2B]] | B | INSYN2B activity raises ITPR1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 4.53× lower at baseline in the lines without INSYN2B | 0.005 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5 |
| [[SGIP1]] | B | SGIP1 activity raises ITPR1's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.82× lower at baseline in the lines without SGIP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG |
| [[LINC02813]] | B | LINC02813 activity raises ITPR1's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without LINC02813 | 0.013 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[FAM20C]] | B | FAM20C activity raises ITPR1's level | lines that do not express FAM20C (19) vs lines expressing it (31) | 3.39× lower at baseline in the lines without FAM20C | 0.013 | ⚠ within organs, on part of the lines; also absent: TUB, S1PR3, FHL1 |
| [[TOP2A]] | B | TOP2A activity lowers ITPR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GDNF]] | B | GDNF activity raises ITPR1's level | lines that do not express GDNF (38) vs lines expressing it (12) | 4.49× lower at baseline in the lines without GDNF | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[LINC01705]] | B | LINC01705 activity raises ITPR1's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 2.99× lower at baseline in the lines without LINC01705 | 0.035 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[ZMAT4]] | B | ZMAT4 activity raises ITPR1's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 3.20× lower at baseline in the lines without ZMAT4 | 0.039 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11 |
| [[ITGB3]] | B | ITGB3 activity weakens ITPR1's drug response | lines that do not express ITGB3 (13) vs lines expressing it (21) | the lines without ITGB3 respond 1.27× as strongly (z diff -0.70); strongest at Panobinostat 0.5 µM: 2.32x vs 1.42x (z diff -3.6) | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; target measured in part of the lines; both ways; artifact flags |
| [[LINC03047]] | B | LINC03047 activity raises ITPR1's level | lines that do not express LINC03047 (28) vs lines expressing it (22) | 4.04× lower at baseline in the lines without LINC03047 | 0.048 | ⚠ within organs, on part of the lines; also absent: CNRIP1, ITGA4, INSYN2B |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFL1]] | B | ITPR1 activity raises EFL1's level | lines that do not express ITPR1 (15) vs lines expressing it (35) | 1.34× lower at baseline in the lines without ITPR1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, CCDC169, SPART; maybe low, not absent |
| [[CHD1L]] | B | ITPR1 activity raises CHD1L's level | lines that do not express ITPR1 (15) vs lines expressing it (35) | 2.11× lower at baseline in the lines without ITPR1 | 0.043 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, CCDC169, SPART; maybe low, not absent |
| [[SGIP1]] | B | ITPR1 activity raises SGIP1's level | lines that do not express ITPR1 (15) vs lines expressing it (35) | 3.29× lower at baseline in the lines without ITPR1 | 0.090 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, CCDC169, SPART; maybe low, not absent |
| [[ARHGAP22]] | C | ITPR1 activity raises ARHGAP22's level | lines that do not express ITPR1 (15) vs lines expressing it (35) | 5.28× lower at baseline in the lines without ITPR1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SPART-AS1, CCDC169, SPART; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.519). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.5, 10.2); signed map (-2.0, 49.4). **Vector** length 128, 38.4% of its response variance represented; |z| ≥ 3 in 1,329 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +17.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +13.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +8.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +3.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[EX229 (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +1.9 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -4.9 | -3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -12.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -5.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.3 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.0 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | inositol 1,4,5-trisphosphate receptor type 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p26.1 — chr3:4,493,345-4,847,506 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Insp3r1, IP3R1, ACV, PPP1R94; previously SCA15, SCA16, SCA29 |
| Gene groups (HGNC) | Inositol 1,4,5-triphosphate receptors; Protein phosphatase 1 regulatory subunits |
| Reactome | 47 pathways, smallest: Elevation of cytosolic Ca2+ levels; Rituximab:MS4A1 (rituximab:CD20) targets B cells for antibody-dependent cellular cytotoxicity by NK cells; CLEC7A (Dectin-1) induces NFAT activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14643](https://www.uniprot.org/uniprotkb/Q14643) (Inositol 1,4,5-trisphosphate-gated calcium channel ITPR1):

> Inositol 1,4,5-trisphosphate-gated calcium channel that, upon inositol 1,4,5-trisphosphate binding, mediates calcium release from the endoplasmic reticulum (ER). Undergoes conformational changes upon ligand binding, suggesting structural flexibility that allows the channel to switch from a closed state, capable of interacting with its ligands such as 1,4,5-trisphosphate and calcium, to an open state, capable of transferring calcium ions across the ER membrane (By similarity). Cytoplasmic …

**Summary**, from NCBI Gene [3708](https://www.ncbi.nlm.nih.gov/gene/3708):

> This gene encodes an intracellular receptor for inositol 1,4,5-trisphosphate. Upon stimulation by inositol 1,4,5-trisphosphate, this receptor mediates calcium release from the endoplasmic reticulum. Mutations in this gene cause spinocerebellar ataxia type 15, a disease associated with an heterogeneous group of cerebellar disorders. Multiple transcript variants have been identified for this gene. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:6180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6180) · Entrez [3708](https://www.ncbi.nlm.nih.gov/gene/3708) · UniProt [Q14643](https://www.uniprot.org/uniprotkb/Q14643) · Ensembl [ENSG00000150995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150995)

## Data

Gene col 7474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7474); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7474]; `tensor/DDL_lfc|DDL_z.npy` [7474]; `embed/gene_vectors.npy` [7474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7474 or target_col == 7474). Every well: [[ITPR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITPR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

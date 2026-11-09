---
symbol: "CRACD"
type: "gene"
col: 3040
ensembl_id: "ENSG00000109265"
name: "capping protein inhibiting regulator of actin dynamics"
location: "4q12"
module: 115
arm: "+"
pooled_cpm: 60.19
n_lines_expressing: 38
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 13
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# CRACD

*capping protein inhibiting regulator of actin dynamics* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.40× (z +10.8, q 1e-24, up in 22 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.439× (z -26.3, q 0e+00, down in 34 of 36 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.454× (z -17.9, q 0e+00, down in 29 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STRBP]] (+0.64, fdr 1e-05), [[KIAA1549]] (+0.64, fdr 7e-06), [[CDYL]] (+0.63, fdr 1e-05); moves opposite to [[MIR583HG]] (-0.51, fdr 2e-05), [[MTERF1]] (-0.50, fdr 5e-05), [[LINC01252]] (-0.50, fdr 3e-05).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TTPA]] → it (grade B ⚠); 13 go from it, the strongest it → [[LRRC8D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +10.8 | 1e-24 | 22/36 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +10.2 | 5e-22 | 20/36 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +10.1 | 1e-21 | 24/36 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +7.1 | 2e-10 | 19/36 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +6.9 | 8e-10 | 21/36 (SW 900, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.78×** | +6.8 | 1e-09 | 15/37 (NCI-H1573, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.25×** | +5.0 | 4e-05 | 13/36 (SW1417, A498, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.23×** | +4.6 | 3e-04 | 13/36 (A-172, NCI-H460, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +4.3 | 9e-04 | 10/36 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.20× | +4.1 | 0.002 | 10/36 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.007 | 14/36 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.034 | 9/38 (SK-MEL-2, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.034 | 7/37 (NCI-H460, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.034 | 8/37 (BT-474, J82, …) | top dose only | noisy plate (z scaled) |
| [[Penfluridol (drug)]] 5 µM |  | 1.17× | +3.3 | 0.034 | 9/36 (A498, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.439×** | -26.3 | 0e+00 | 34/36 (LoVo, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.454×** | -17.9 | 0e+00 | 29/35 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.562×** | -12.5 | 1e-33 | 27/36 (NCI-H2030, LoVo, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.411×** | -10.5 | 1e-23 | 30/37 (RKO, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.647×** | -9.8 | 9e-21 | 24/36 (LoVo, SW48, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.469×** | -9.0 | 3e-17 | 22/36 (LoVo, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.685×** | -8.6 | 1e-15 | 21/36 (SW48, A-427, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.678×** | -8.1 | 3e-14 | 21/35 (RKO, SW48, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.724×** | -7.3 | 2e-11 | 23/35 (SW48, SNU-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -7.1 | 6e-11 | 23/36 (RKO, SW48, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.751×** | -6.2 | 3e-08 | 19/36 (SNU-1, SW48, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.599×** | -6.1 | 7e-08 | 18/25 (HEC-1-A, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.835× | -5.8 | 3e-07 | 16/36 (NCI-H2030, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.776×** | -5.7 | 4e-07 | 19/36 (SW48, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.790×** | -5.3 | 4e-06 | 22/36 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.808×** | -4.8 | 5e-05 | 21/37 (KATO III, RKO, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.711×** | -4.0 | 0.002 | 18/35 (KATO III, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.856× | -3.5 | 0.011 | 19/36 (RKO, C-33 A, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.856× | -3.4 | 0.016 | 8/37 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.911× | -3.0 | 0.057 | 8/36 (AsPC-1, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 109 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -23.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -16.2) |
| [[RKO (line)]] | wt | 227 | 0 | 13 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -19.9) |
| [[LoVo (line)]] | wt | 98.9 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -39.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -26.6) |
| [[SW48 (line)]] | wt | 165 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -34.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0507× (z -29.5) |
| [[A-427 (line)]] | wt | 124 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.437× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 99.5 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -18.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.375× (z -10.2) |
| [[C-33 A (line)]] | alt | 217 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -16.8) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -10.9) |
| [[LS 180 (line)]] | wt | 217 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -25.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -18.7) |
| [[NCI-H2030 (line)]] | alt | 97.4 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -24.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -15.4) |
| [[SHP-77 (line)]] | alt | 210 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -18.5) ⚠ cell-cycle shift, explains ~55% of this change |
| [[SNU-1 (line)]] | wt | 78.3 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 90.5 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 109 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -24.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.209× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 72.2 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.10× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0811× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -14.0) |
| [[C32 (line)]] | wt | 91.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 57.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -21.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -14.1) |
| [[PANC-1 (line)]] | alt | 23.8 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.78× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -12.1) |
| [[A-172 (line)]] | wt | 36.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -9.3) |
| [[A549 (line)]] | wt | 33.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -14.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 16.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.07× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 32.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -12.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 35.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.1) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[AN3 CA (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[CHP-212 (line)]] | wt | 69.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 17.6 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0680× (z -10.8) |
| [[Hs 766T (line)]] | wt | 44.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.119× (z -8.5) ⚠ toxic |
| [[J82 (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H596 (line)]] | alt | 68.1 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.181× (z -8.7) |
| [[SW 900 (line)]] | alt | 56.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.204× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~7% of this change |
| [[BT-474 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.97 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.47 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.83 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.17 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 26.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRBP]] | +0.64 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[KIAA1549]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[CDYL]] | +0.63 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[DOCK9]] | +0.57 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[SCD5]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[RNF125]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[GAB2]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ARHGAP44]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PALS2]] | +0.53 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ZNF704]] | +0.53 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PRKCQ]] | +0.53 | +0.46 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR583HG]] | -0.51 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[MTERF1]] | -0.50 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[LINC01252]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[NR2F2-AS1]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ZNF429]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[METTL25B]] | -0.48 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[GALK2]] | -0.46 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[LMLN]] | -0.46 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[EFCAB6]] | -0.45 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[BBOF1]] | -0.45 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[METTL6]] | -0.45 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[COG4]] | -0.45 | -0.47 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTPA]] | B | TTPA activity raises CRACD's level | lines that do not express TTPA (24) vs lines expressing it (26) | 2.60× lower at baseline in the lines without TTPA | 0.056 | ⚠ within organs, on part of the lines; also absent: MKX, FGF20, ENSG00000238178 |
| [[SLC16A10]] | B | SLC16A10 activity raises CRACD's level | lines that do not express SLC16A10 (15) vs lines expressing it (35) | 2.30× lower at baseline in the lines without SLC16A10 | 0.091 | ⚠ within organs, on part of the lines; also absent: SH3GL2, FZD3, TTYH2 |
| [[BTNL9]] | B | BTNL9 activity raises CRACD's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.31× lower at baseline in the lines without BTNL9 | 0.099 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC8D]] | B | CRACD activity raises LRRC8D's level | lines that do not express CRACD (12) vs lines expressing it (38) | 2.44× lower at baseline in the lines without CRACD | 0.004 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[PACC1]] | B | CRACD activity raises PACC1's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.82× lower at baseline in the lines without CRACD | 0.007 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[KIAA1549]] | B | CRACD activity raises KIAA1549's level | lines that do not express CRACD (12) vs lines expressing it (38) | 2.24× lower at baseline in the lines without CRACD | 0.018 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[DTNB]] | B | CRACD activity raises DTNB's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without CRACD | 0.019 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[PARD6G]] | B | CRACD activity raises PARD6G's level | lines that do not express CRACD (12) vs lines expressing it (38) | 2.27× lower at baseline in the lines without CRACD | 0.029 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[BBOF1]] | B | CRACD activity lowers BBOF1's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.45× higher at baseline in the lines without CRACD | 0.046 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[AHCYL2]] | B | CRACD activity raises AHCYL2's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without CRACD | 0.052 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[LHX2]] | B | CRACD activity raises LHX2's level | lines that do not express CRACD (12) vs lines expressing it (38) | 2.47× lower at baseline in the lines without CRACD | 0.059 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[CMTM8]] | B | CRACD activity raises CMTM8's level | lines that do not express CRACD (12) vs lines expressing it (38) | 2.53× lower at baseline in the lines without CRACD | 0.062 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[TMTC4]] | B | CRACD activity raises TMTC4's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.87× lower at baseline in the lines without CRACD | 0.066 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[NIPA1]] | B | CRACD activity raises NIPA1's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without CRACD | 0.072 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[TTPA]] | B | CRACD activity raises TTPA's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.74× lower at baseline in the lines without CRACD | 0.092 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.2, 44.3); signed map (-23.3, 39.1). **Vector** length 109, 28.3% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.5 | +10.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.4 | +6.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.2 | +10.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.1 | +3.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.7 | -10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -17.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -7.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.5 | -12.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -9.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | capping protein inhibiting regulator of actin dynamics |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:56,049,098-56,330,609 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRAD; previously KIAA1211 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZU35](https://www.uniprot.org/uniprotkb/Q6ZU35) (Capping protein-inhibiting regulator of actin dynamics):

> Involved in epithelial cell integrity by acting on the maintenance of the actin cytoskeleton. Positively regulates the actin polymerization, by inhibiting the interaction of actin-capping proteins with actin.

**Summary**, from NCBI Gene [57482](https://www.ncbi.nlm.nih.gov/gene/57482):

> Involved in negative regulation of barbed-end actin filament capping. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29219) · Entrez [57482](https://www.ncbi.nlm.nih.gov/gene/57482) · UniProt [Q6ZU35](https://www.uniprot.org/uniprotkb/Q6ZU35) · Ensembl [ENSG00000109265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109265)

## Data

Gene col 3040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3040); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3040]; `tensor/DDL_lfc|DDL_z.npy` [3040]; `embed/gene_vectors.npy` [3040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3040 or target_col == 3040). Every well: [[CRACD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRACD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

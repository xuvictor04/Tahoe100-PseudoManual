---
symbol: "ABCG1"
type: "gene"
col: 8305
ensembl_id: "ENSG00000160179"
name: "ATP binding cassette subfamily G member 1"
location: "21q22.3"
module: 59
arm: "+"
pooled_cpm: 22.79
n_lines_expressing: 35
n_dd_up: 17
n_dd_down: 30
n_dd_up_clean: 16
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# ABCG1

*ATP binding cassette subfamily G member 1* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Retinoic acid (drug)]] 5 µM: 2.56× (z +14.3, q 1e-43, up in 29 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (14 with an alert ⚠); the strongest is [[Clotrimazole (drug)]] 5 µM: 0.335× (z -16.5, q 0e+00, down in 30 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YPEL2]] (+0.61, fdr 1e-05), [[ARL4D]] (+0.57, fdr 5e-05), [[RGS9]] (+0.56, fdr 5e-05); moves opposite to [[PRDM5]] (-0.53, fdr 5e-05), [[SNX5]] (-0.52, fdr 3e-05), [[ALG8]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00482]] → it (grade B ⚠); 3 go from it, the strongest it → [[SLC22A23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 5 µM |  | **2.56×** | +14.3 | 1e-43 | 29/34 (SW480, LoVo, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **3.14×** | +12.3 | 2e-32 | 31/32 (SW480, LoVo, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **2.92×** | +11.5 | 2e-28 | 28/33 (SW480, LoVo, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **2.80×** | +11.1 | 2e-26 | 32/33 (SW480, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +10.3 | 7e-23 | 28/33 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **2.08×** | +7.9 | 3e-13 | 27/33 (SW480, LoVo, …) | rises with dose |  |
| [[Bexarotene (drug)]] 5 µM |  | **2.01×** | +7.5 | 4e-12 | 25/33 (SW480, SW1417, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +7.5 | 5e-12 | 26/34 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.74×** | +5.7 | 7e-07 | 19/30 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.46×** | +5.1 | 2e-05 | 17/32 (BT-474, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +4.3 | 8e-04 | 17/33 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.002 | 14/34 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.006 | 17/31 (NCI-H460, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.26×** | +3.6 | 0.012 | 13/33 (BT-474, SHP-77, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.033 | 15/31 (LS 180, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.049 | 9/32 (SW480, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8305.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clotrimazole (drug)]] 5 µM |  | **0.335×** | -16.5 | 0e+00 | 30/34 (SW480, SW1417, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.333×** | -11.7 | 3e-29 | 28/32 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.349×** | -11.2 | 7e-27 | 30/33 (SW480, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.372×** | -10.5 | 9e-24 | 30/33 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.563×** | -8.6 | 8e-16 | 21/32 (COLO 205, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.475×** | -7.9 | 2e-13 | 20/30 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.484×** | -7.7 | 9e-13 | 26/33 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.512×** | -7.1 | 8e-11 | 25/33 (HT-29, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.519×** | -6.7 | 1e-09 | 20/32 (SW480, NCI-H1792, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.539×** | -6.3 | 2e-08 | 24/29 (LoVo, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **0.562×** | -6.1 | 5e-08 | 18/29 (COLO 205, HT-29, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -6.1 | 5e-08 | 20/31 (HT-29, SW1417, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.570×** | -6.0 | 1e-07 | 21/33 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.574×** | -5.9 | 2e-07 | 20/32 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.355×** | -5.8 | 3e-07 | 26/32 (Panc 03.27, A549, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.408×** | -5.0 | 2e-05 | 18/32 (KATO III, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.410×** | -5.0 | 2e-05 | 20/31 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.415×** | -4.9 | 3e-05 | 20/32 (NCI-H1792, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **0.739×** | -4.5 | 2e-04 | 16/33 (LS 180, SNU-1, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.485×** | -4.0 | 0.001 | 18/30 (A549, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.789×** | -3.5 | 0.010 | 11/33 (CHP-212, SW480, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.638×** | -3.4 | 0.015 | 16/33 (AN3 CA, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.556×** | -3.3 | 0.024 | 16/31 (NCI-H23, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.743×** | -3.1 | 0.035 | 12/33 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 27.4 | 6 | 8 (6 ⚠) | [[Retinoic acid (drug)]] 5 µM 3.89× (z +16.3) | [[Clotrimazole (drug)]] 5 µM 0.288× (z -14.8) |
| [[HT-29 (line)]] | alt | 84.8 | 1 | 10 (6 ⚠) | [[Retinoic acid (drug)]] 5 µM 3.19× (z +9.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0485× (z -15.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -11.0) |
| [[COLO 205 (line)]] | alt | 96.1 | 2 | 8 (6 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.72× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -17.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Clotrimazole (drug)]] 5 µM 0.310× (z -10.3) |
| [[LoVo (line)]] | wt | 15.3 | 4 | 5 (2 ⚠) | [[Retinoic acid (drug)]] 5 µM 5.01× (z +13.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -11.1) |
| [[LS 180 (line)]] | wt | 18.0 | 5 | 4 (2 ⚠) | [[Retinoic acid (drug)]] 5 µM 5.70× (z +12.9) | [[Clotrimazole (drug)]] 5 µM 0.190× (z -12.2) |
| [[KATO III (line)]] | alt | 44.5 | 3 | 5 (4 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.63× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.0719× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Clotrimazole (drug)]] 5 µM 0.414× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 55.1 | 1 | 7 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.90× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -16.3) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 40.9 | 0 | 7 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -11.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Clotrimazole (drug)]] 5 µM 0.295× (z -9.6) |
| [[SW1417 (line)]] | alt | 49.2 | 2 | 5 (3 ⚠) | [[Retinoic acid (drug)]] 5 µM 2.22× (z +9.1) | [[Clotrimazole (drug)]] 5 µM 0.311× (z -13.3) |
| [[HCT15 (line)]] | alt | 19.8 | 4 | 1 (1 ⚠) | [[Retinoic acid (drug)]] 5 µM 6.27× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -9.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HOP62 (line)]] | alt | 18.0 | 4 | 1 | [[Bexarotene (drug)]] 0.5 µM 8.70× (z +10.0) | [[Clotrimazole (drug)]] 5 µM 0.198× (z -10.5) |
| [[Hs 766T (line)]] | wt | 87.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Clotrimazole (drug)]] 5 µM 0.348× (z -11.8) |
| [[A549 (line)]] | wt | 31.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Clotrimazole (drug)]] 5 µM 0.218× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 73.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -13.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Clotrimazole (drug)]] 5 µM 0.334× (z -12.4) |
| [[H4 (line)]] | wt | 23.8 | 2 | 2 (1 ⚠) | [[Retinoic acid (drug)]] 5 µM 5.74× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.0721× (z -9.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Clotrimazole (drug)]] 5 µM 0.209× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 22.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 14.8 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.67× (z +10.4) | [[Clotrimazole (drug)]] 5 µM 0.280× (z -8.6) |
| [[SHP-77 (line)]] | alt | 40.1 | 2 | 0 | [[Bexarotene (drug)]] 0.5 µM 4.05× (z +9.3) | — |
| [[A-172 (line)]] | wt | 40.3 | 0 | 1 | — | [[Clotrimazole (drug)]] 5 µM 0.322× (z -8.7) |
| [[BT-474 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.182× (z -8.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -9.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SNU-1 (line)]] | wt | 29.3 | 1 | 0 | [[Retinoic acid (drug)]] 5 µM 4.03× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 22.9 | 0 | 1 | — | [[Clotrimazole (drug)]] 5 µM 0.292× (z -9.3) |
| [[A-427 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.58 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL2]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[ARL4D]] | +0.57 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[RGS9]] | +0.56 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[ATP2A3]] | +0.56 | +0.43 / +0.55 | both halves | 4e-05 |  |
| [[HDAC11]] | +0.55 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[FOXO4]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[PLEKHG6]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[RNF19B]] | +0.53 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[CASP9]] | +0.53 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[ASAP3]] | +0.52 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[PELI1]] | +0.52 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[LINC00482]] | +0.52 | +0.39 / +0.47 | both halves | 6e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM5]] | -0.53 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[SNX5]] | -0.52 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ALG8]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[AVEN]] | -0.51 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[DNAAF10]] | -0.51 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[UTP20]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ZRANB3]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ANAPC1]] | -0.50 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ZNF577]] | -0.50 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[MCPH1]] | -0.50 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[CSTF3]] | -0.50 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[ARMC6]] | -0.50 | -0.38 / -0.48 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00482]] | B | LINC00482 activity raises ABCG1's level | lines that do not express LINC00482 (8) vs lines expressing it (42) | 2.78× lower at baseline in the lines without LINC00482 | 0.029 | ⚠ within organs, on part of the lines; also absent: SOX13, SEPTIN9-DT |
| [[TMCC2]] | B | TMCC2 activity lowers ABCG1's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 4.61× higher at baseline in the lines without TMCC2 | 0.057 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[FA2H]] | B | FA2H activity raises ABCG1's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.81× lower at baseline in the lines without FA2H | 0.085 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC22A23]] | B | ABCG1 activity raises SLC22A23's level | lines that do not express ABCG1 (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without ABCG1 | 0.061 | ⚠ within organs, on part of the lines; also absent: RSPH1, OLFM1, PDK4 |
| [[FOXO4]] | B | ABCG1 activity raises FOXO4's level | lines that do not express ABCG1 (15) vs lines expressing it (35) | 1.11× lower at baseline in the lines without ABCG1 | 0.088 | ⚠ within organs, on part of the lines; also absent: RSPH1, OLFM1, PDK4 |
| [[ATP2A3]] | B | ABCG1 activity raises ATP2A3's level | lines that do not express ABCG1 (15) vs lines expressing it (35) | 2.22× lower at baseline in the lines without ABCG1 | 0.098 | ⚠ within organs, on part of the lines; also absent: RSPH1, OLFM1, PDK4 |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.358). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (11.4, 1.5); signed map (-20.2, 28.2). **Vector** length 88.7, 18.9% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -10.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -5.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily G member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:42,199,689-42,297,244 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ABC8 |
| Gene groups (HGNC) | ATP binding cassette subfamily G |
| Reactome | 9 pathways, smallest: HDL remodeling; ABC transporters in lipid homeostasis; Plasma lipoprotein remodeling |
| Matched by | ensembl_id |

**Function**, from UniProt [P45844](https://www.uniprot.org/uniprotkb/P45844) (ATP-binding cassette sub-family G member 1):

> Catalyzes the efflux of phospholipids such as sphingomyelin, cholesterol and its oxygenated derivatives like 7beta-hydroxycholesterol and this transport is coupled to hydrolysis of ATP. The lipid efflux is ALB-dependent. Is an active component of the macrophage lipid export complex. Could also be involved in intracellular lipid transport processes. The role in cellular lipid homeostasis may not be limited to macrophages. Prevents cell death by transporting cytotoxic 7beta-hydroxycholesterol.

**Summary**, from NCBI Gene [9619](https://www.ncbi.nlm.nih.gov/gene/9619):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the White subfamily. It is involved in macrophage cholesterol and phospholipids transport, and may regulate cellular lipid homeostasis in other cell types. Six alternative …

**Accessions** — [HGNC:73](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:73) · Entrez [9619](https://www.ncbi.nlm.nih.gov/gene/9619) · UniProt [P45844](https://www.uniprot.org/uniprotkb/P45844) · Ensembl [ENSG00000160179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160179)

## Data

Gene col 8305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8305); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8305]; `tensor/DDL_lfc|DDL_z.npy` [8305]; `embed/gene_vectors.npy` [8305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8305 or target_col == 8305). Every well: [[ABCG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

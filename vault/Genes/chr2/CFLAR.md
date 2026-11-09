---
symbol: "CFLAR"
type: "gene"
col: 34
ensembl_id: "ENSG00000003402"
name: "CASP8 and FADD like apoptosis regulator"
location: "2q33.1"
module: 10
arm: "+"
pooled_cpm: 148.76
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 22
n_dd_up_clean: 11
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CFLAR

*CASP8 and FADD like apoptosis regulator* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +13.6, q 2e-39, up in 35 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.184× (z -35.8, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKN2-AS1]] (+0.72, fdr 6e-05), [[MMADHC-DT]] (+0.71, fdr 1e-04), [[PBLD]] (+0.70, fdr 5e-05); moves opposite to [[CDON]] (-0.73, fdr 7e-06), [[YIF1B]] (-0.67, fdr 8e-05), [[ARL6]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 34.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +13.6 | 2e-39 | 35/49 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +10.2 | 8e-22 | 30/48 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +7.4 | 2e-11 | 34/48 (HOP62, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +6.9 | 1e-09 | 29/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +5.9 | 5e-07 | 25/48 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.65×** | +5.5 | 3e-06 | 32/49 (Hs 766T, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.3 | 9e-06 | 25/48 (HS-578T, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.28×** | +4.9 | 9e-05 | 24/45 (LoVo, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.002 | 25/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.004 | 19/48 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.21×** | +3.9 | 0.004 | 23/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.006 | 22/50 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.012 | 22/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.012 | 19/48 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.18× | +3.5 | 0.018 | 20/48 (HOP62, A-172, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.031 | 16/47 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.10× | +2.9 | 0.088 | 12/48 (HOP62, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 34.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.184×** | -35.8 | 0e+00 | 47/48 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.216×** | -32.4 | 0e+00 | 47/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.224×** | -31.6 | 0e+00 | 48/48 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.433×** | -17.6 | 0e+00 | 47/48 (COLO 205, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.577×** | -11.6 | 4e-29 | 42/48 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.449×** | -8.8 | 8e-17 | 41/49 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.660×** | -8.8 | 1e-16 | 36/48 (J82, NCI-H23, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.739×** | -6.1 | 6e-08 | 29/47 (SW 1271, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.819×** | -6.0 | 2e-07 | 27/48 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.766×** | -5.6 | 1e-06 | 30/49 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.643×** | -4.9 | 5e-05 | 33/48 (NCI-H23, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.807×** | -4.5 | 3e-04 | 26/48 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.686×** | -4.2 | 0.001 | 23/48 (SW1417, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.697×** | -4.0 | 0.003 | 24/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.707×** | -3.8 | 0.005 | 22/48 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.708×** | -3.8 | 0.005 | 20/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.846× | -3.5 | 0.013 | 15/48 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 34. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 186 | 6 | 6 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +27.0) | [[Panobinostat (drug)]] 5 µM 0.123× (z -30.3) |
| [[HOP62 (line)]] | alt | 69.9 | 8 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.5) | [[Belinostat (drug)]] 5 µM 0.243× (z -14.0) |
| [[LoVo (line)]] | wt | 101 | 6 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.01× (z +13.2) | [[Belinostat (drug)]] 5 µM 0.154× (z -23.2) |
| [[HS-578T (line)]] | alt | 76.8 | 6 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.177× (z -17.5) |
| [[A498 (line)]] | wt | 231 | 4 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.257× (z -19.4) |
| [[hTERT-HPNE (line)]] | wt | 87.1 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +20.8) | [[Panobinostat (drug)]] 5 µM 0.267× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 180 | 2 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +17.3) | [[Panobinostat (drug)]] 5 µM 0.178× (z -23.7) |
| [[SK-MEL-2 (line)]] | alt | 49.2 | 2 (1 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.3) | [[Belinostat (drug)]] 5 µM 0.285× (z -10.2) |
| [[SNU-423 (line)]] | alt | 88.3 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.180× (z -17.7) |
| [[C-33 A (line)]] | alt | 59.7 | 3 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.2) | [[Belinostat (drug)]] 5 µM 0.190× (z -13.6) |
| [[C32 (line)]] | wt | 99.3 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +14.3) | [[Panobinostat (drug)]] 5 µM 0.156× (z -18.8) |
| [[COLO 205 (line)]] | alt | 181 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.0589× (z -29.0) |
| [[HepG2_C3A (line)]] | wt | 140 | 2 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -19.0) |
| [[HT-29 (line)]] | alt | 97.2 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -22.7) |
| [[NCI-H23 (line)]] | alt | 102 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.188× (z -18.0) |
| [[NCI-H2347 (line)]] | alt | 182 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -21.6) |
| [[RKO (line)]] | wt | 65.8 | 2 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.178× (z -15.2) |
| [[SW1417 (line)]] | alt | 137 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -20.8) |
| [[A-427 (line)]] | wt | 46.7 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.259× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 135 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -26.7) |
| [[J82 (line)]] | alt | 160 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +17.1) | [[Panobinostat (drug)]] 5 µM 0.216× (z -18.3) |
| [[LOX-IMVI (line)]] | wt | 160 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0988× (z -24.4) |
| [[Panc 03.27 (line)]] | alt | 171 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -23.2) |
| [[PANC-1 (line)]] | alt | 65.0 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.191× (z -21.1) |
| [[RPMI-7951 (line)]] | alt | 98.7 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +13.1) | [[Belinostat (drug)]] 5 µM 0.206× (z -15.5) |
| [[SW 900 (line)]] | alt | 108 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.223× (z -15.2) |
| [[SW480 (line)]] | alt | 55.8 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +13.7) | [[Belinostat (drug)]] 5 µM 0.183× (z -21.3) |
| [[AsPC-1 (line)]] | alt | 384 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -21.3) |
| [[BT-474 (line)]] | alt | 75.6 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 354 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -23.4) |
| [[KATO III (line)]] | alt | 75.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -21.5) |
| [[LS 180 (line)]] | wt | 116 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -25.7) |
| [[SNU-1 (line)]] | wt | 50.3 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.150× (z -13.7) |
| [[SW 1271 (line)]] | alt | 218 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -11.9) |
| [[A549 (line)]] | wt | 186 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -23.3) |
| [[H4 (line)]] | wt | 80.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -14.3) |
| [[HCT15 (line)]] | alt | 112 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -17.9) |
| [[Hs 766T (line)]] | wt | 216 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -19.0) |
| [[MIA PaCa-2 (line)]] | alt | 220 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -17.7) |
| [[NCI-H1792 (line)]] | alt | 132 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -17.3) |
| [[NCI-H2030 (line)]] | alt | 550 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 229 | 2 (1 ⚠) | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.21× (z +10.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 2.11× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.547× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 39.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.187× (z -13.1) |
| [[AN3 CA (line)]] | alt | 66.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -8.6) |
| [[SW 1088 (line)]] | alt | 85.7 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.05 µM 0.0763× (z -9.2) |
| [[CHP-212 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 34), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKN2-AS1]] | +0.72 | +0.66 / +0.38 | both halves | 6e-05 |  |
| [[MMADHC-DT]] | +0.71 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[PBLD]] | +0.70 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[PPP3CB-AS1]] | +0.68 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[PPP1R12A-AS2]] | +0.68 | +0.66 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[SPRY3]] | +0.67 | +0.62 / +0.35 | both halves | 1e-04 |  |
| [[WAC-AS1]] | +0.66 | +0.55 / +0.28 | both halves | 3e-04 |  |
| [[TMEM202-AS1]] | +0.66 | +0.59 / +0.21 | both halves | 7e-04 |  |
| [[WAKMAR2]] | +0.65 | +0.60 / +0.36 | both halves | 9e-05 |  |
| [[PCNX4-DT]] | +0.65 | +0.59 / +0.22 | both halves | 6e-04 |  |
| [[ARRDC3-AS1]] | +0.65 | +0.59 / +0.26 | both halves | 4e-04 |  |
| [[IL6ST]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IQCH-AS1]] | +0.64 | +0.57 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDON]] | -0.73 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[YIF1B]] | -0.67 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ARL6]] | -0.66 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.65 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[NXPH4]] | -0.65 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SLC27A1]] | -0.65 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[HACE1]] | -0.64 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[SMYD3]] | -0.63 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[L2HGDH]] | -0.63 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[MAST3]] | -0.63 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[CSNK2A1]] | -0.62 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[WASF3]] | -0.62 | -0.51 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CFLAR's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ALDOC]] | B | ALDOC activity raises CFLAR's level | lines that do not express ALDOC (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without ALDOC | 0.095 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.4, 11.7); signed map (23.9, -7.6). **Vector** length 140, 45.3% of its response variance represented; |z| ≥ 3 in 1,579 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.7 | +13.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +10.1 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +10.1 | +10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.5 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.6 | +2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +4.7 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.5 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.4 | +3.6 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.6 | -31.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.6 | -17.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.2 | -32.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -8.0 | -11.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.5 | -35.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.4 | -8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | CASP8 and FADD like apoptosis regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:201,116,154-201,176,687 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CASH, Casper, CLARP, FLAME, FLIP, I-FLICE, MRIT, c-FLIP; previously CASP8AP1 |
| Gene groups (HGNC) | Receptor ligands; Death effector domain containing; Ripoptosome; Death inducing signaling complex |
| Hallmark sets | APOPTOSIS, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 14 pathways, smallest: TRAIL  signaling; CASP8 activity is inhibited; Dimerization of procaspase-8 |
| Matched by | ensembl_id |

**Function**, from UniProt [O15519](https://www.uniprot.org/uniprotkb/O15519) (CASP8 and FADD-like apoptosis regulator):

> Regulator of programmed cell death, which acts as master cellular switch, determining whether a cell survives or undergoes death receptor-mediated cell death. Lacks enzymatic (caspase) activity. Full length (isoform 1) and short isoform (isoform 2) either induce or reduce TNFRSF-triggered apoptosis. Acts as an inhibitor of TNFRSF6 mediated apoptosis. A proteolytic fragment (p43) is likely retained in the death-inducing signaling complex (DISC) thereby blocking further recruitment and processing …

**Summary**, from NCBI Gene [8837](https://www.ncbi.nlm.nih.gov/gene/8837):

> The protein encoded by this gene is a regulator of apoptosis and is structurally similar to caspase-8. However, the encoded protein lacks caspase activity and appears to be itself cleaved into two peptides by caspase-8. Several transcript variants encoding different isoforms have been found for this gene, and partial evidence for several more variants exists. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:1876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1876) · Entrez [8837](https://www.ncbi.nlm.nih.gov/gene/8837) · UniProt [O15519](https://www.uniprot.org/uniprotkb/O15519) · Ensembl [ENSG00000003402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003402)

## Data

Gene col 34: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 34); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 34, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 34]; `tensor/DDL_lfc|DDL_z.npy` [34]; `embed/gene_vectors.npy` [34]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 34 or target_col == 34). Every well: [[CFLAR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFLAR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

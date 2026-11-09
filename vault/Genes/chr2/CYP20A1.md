---
symbol: "CYP20A1"
type: "gene"
col: 4035
ensembl_id: "ENSG00000119004"
name: "cytochrome P450 family 20 subfamily A member 1"
location: "2q33.2"
module: 170
arm: "+"
pooled_cpm: 62.58
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# CYP20A1

*cytochrome P450 family 20 subfamily A member 1* — 2q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.25× (z +21.9, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.531× (z -12.1, q 1e-30, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOSR1]] (+0.68, fdr 2e-05), [[NDUFAF1]] (+0.67, fdr 7e-06), [[TSG101]] (+0.66, fdr 1e-05); moves opposite to [[ARHGEF7]] (-0.67, fdr 7e-06), [[LDHB]] (-0.62, fdr 3e-05), [[HACD3]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EMP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4035.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.25×** | +21.9 | 0e+00 | 45/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +13.7 | 3e-40 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +8.8 | 2e-16 | 32/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +6.7 | 3e-09 | 32/48 (NCI-H1573, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +4.9 | 1e-04 | 33/49 (LoVo, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 6e-04 | 24/48 (NCI-H2347, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.55×** | +4.4 | 9e-04 | 27/49 (A498, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.54×** | +4.3 | 0.001 | 23/48 (CFPAC-1, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.040 | 15/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.19× | +3.3 | 0.052 | 17/48 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.058 | 20/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.18× | +3.1 | 0.086 | 17/47 (HOP62, A-427, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.10 | 14/48 (SW 900, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4035.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.531×** | -12.1 | 1e-30 | 45/48 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -8.9 | 1e-16 | 40/49 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.632×** | -8.7 | 4e-16 | 32/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.633×** | -8.7 | 4e-16 | 38/48 (SW480, NCI-H460, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.445×** | -8.1 | 9e-14 | 36/48 (LOX-IMVI, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.657×** | -8.0 | 1e-13 | 35/48 (NCI-H2030, J82, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.669×** | -7.6 | 2e-12 | 33/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.691×** | -7.0 | 2e-10 | 34/48 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.709×** | -6.5 | 4e-09 | 30/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.733×** | -5.9 | 2e-07 | 32/48 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.735×** | -5.6 | 1e-06 | 28/47 (NCI-H1792, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.777×** | -4.8 | 9e-05 | 24/48 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.626×** | -4.7 | 1e-04 | 19/36 (NCI-H1573, C32, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.630×** | -4.6 | 2e-04 | 26/45 (C32, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -4.4 | 5e-04 | 1/49 (RKO) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.666×** | -4.0 | 0.002 | 21/49 (NCI-H460, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.668×** | -4.0 | 0.002 | 24/47 (NCI-H2030, AN3 CA, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.811×** | -4.0 | 0.002 | 22/48 (NCI-H2030, J82, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.807×** | -3.8 | 0.003 | 19/48 (SW480, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.868× | -3.8 | 0.004 | 13/48 (NCI-H2030, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.841× | -3.3 | 0.025 | 16/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.850× | -3.0 | 0.072 | 15/47 (NCI-H23, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4035. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 96.7 | 2 | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +27.7) | [[Digitoxin (drug)]] 0.05 µM 0.316× (z -15.3) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.422× (z -11.4) |
| [[SW480 (line)]] | alt | 70.4 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +22.0) | [[Ixazomib citrate (drug)]] 0.5 µM 0.434× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 60.9 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +22.1) | [[Digitoxin (drug)]] 5 µM 0.274× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.396× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 88.3 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.6) | [[Belinostat (drug)]] 0.5 µM 0.360× (z -11.6) |
| [[J82 (line)]] | alt | 77.9 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.292× (z -14.2) |
| [[LS 180 (line)]] | wt | 61.4 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +16.8) | [[Digitoxin (drug)]] 5 µM 0.248× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 72.4 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +20.0) | [[Belinostat (drug)]] 0.5 µM 0.417× (z -12.0) |
| [[H4 (line)]] | wt | 78.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 65.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.0) | [[Belinostat (drug)]] 0.5 µM 0.380× (z -10.1) |
| [[A-427 (line)]] | wt | 49.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 49.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 43.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.0) | [[Belinostat (drug)]] 0.5 µM 0.318× (z -11.6) |
| [[HOP62 (line)]] | alt | 70.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.390× (z -10.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 48.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.1) | [[Belinostat (drug)]] 0.5 µM 0.389× (z -9.5) |
| [[LoVo (line)]] | wt | 47.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +19.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 78.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +15.0) | — |
| [[NCI-H2030 (line)]] | alt | 117 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +11.6) | [[Belinostat (drug)]] 0.5 µM 0.280× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 54.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.7) | — |
| [[BT-474 (line)]] | alt | 43.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +14.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.297× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[HCT15 (line)]] | alt | 76.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 66.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.0) | [[Belinostat (drug)]] 0.5 µM 0.399× (z -8.6) |
| [[HS-578T (line)]] | alt | 70.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.362× (z -10.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.398× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 48.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.8) | [[PH-797804 (drug)]] 5 µM 0.146× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 41.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 48.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +8.6) | [[Belinostat (drug)]] 0.5 µM 0.284× (z -10.0) |
| [[AN3 CA (line)]] | alt | 48.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +9.7) | — |
| [[C32 (line)]] | wt | 74.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.1) | — |
| [[CFPAC-1 (line)]] | alt | 51.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.7) | — |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0724× (z -11.8) |
| [[COLO 205 (line)]] | alt | 39.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +17.5) | — |
| [[Hs 766T (line)]] | wt | 41.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +14.2) | — |
| [[hTERT-HPNE (line)]] | wt | 61.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 68.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 36.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0779× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 65.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.6) | — |
| [[A498 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4035), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOSR1]] | +0.68 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[NDUFAF1]] | +0.67 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[TSG101]] | +0.66 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[GPAT4-AS1]] | +0.65 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[XIAP]] | +0.65 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[HELQ]] | +0.65 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[ZNF181]] | +0.65 | +0.75 / +0.35 | both halves | 1e-04 |  |
| [[FKRP]] | +0.65 | +0.72 / +0.37 | both halves | 8e-05 |  |
| [[CIRBP]] | +0.65 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[CHMP4A]] | +0.64 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[LRCH3]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[NDUFA6-DT]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF7]] | -0.67 | -0.72 / -0.67 | both halves | 7e-06 |  |
| [[LDHB]] | -0.62 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[HACD3]] | -0.62 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[PGAM1]] | -0.62 | -0.73 / -0.58 | both halves | 7e-06 |  |
| [[SKP2]] | -0.60 | -0.63 / -0.46 | both halves | 2e-05 |  |
| [[METAP1]] | -0.60 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[TUFM]] | -0.58 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[PARP1]] | -0.58 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[TMEM97]] | -0.57 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[PLXND1]] | -0.56 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[KATNB1]] | -0.56 | -0.63 / -0.21 | both halves | 7e-04 |  |
| [[EXT2]] | -0.56 | -0.63 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EMP3]] | B | EMP3 activity raises CYP20A1's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 1.56× lower at baseline in the lines without EMP3 | 0.099 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-28.4, 8.3); signed map (3.0, -13.2). **Vector** length 130, 38.9% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +16.5 | +21.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +13.6 | +13.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.0 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.8 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.5 | +4.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.1 | +2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +4.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -11.6 | -12.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.2 | -5.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.1 | -8.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.8 | -8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.5 | -8.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.4 | -8.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.0 | -4.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -3.5 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 20 subfamily A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.2 — chr2:203,238,977-203,306,026 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CYP-M |
| Gene groups (HGNC) | Cytochrome P450 family 20 |
| Matched by | ensembl_id |

UniProt [Q6UW02](https://www.uniprot.org/uniprotkb/Q6UW02) carries no function annotation.

**Summary**, from NCBI Gene [57404](https://www.ncbi.nlm.nih.gov/gene/57404):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases that catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This protein lacks one amino acid of the conserved heme binding site. It also lacks the conserved I-helix motif AGX(D,E)T, suggesting that its substrate may carry its own oxygen. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20576) · Entrez [57404](https://www.ncbi.nlm.nih.gov/gene/57404) · UniProt [Q6UW02](https://www.uniprot.org/uniprotkb/Q6UW02) · Ensembl [ENSG00000119004](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119004)

## Data

Gene col 4035: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4035); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4035, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4035]; `tensor/DDL_lfc|DDL_z.npy` [4035]; `embed/gene_vectors.npy` [4035]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4035 or target_col == 4035). Every well: [[CYP20A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP20A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

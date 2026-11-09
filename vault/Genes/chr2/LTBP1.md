---
symbol: "LTBP1"
type: "gene"
col: 550
ensembl_id: "ENSG00000049323"
name: "latent transforming growth factor beta binding protein 1"
location: "2p22.3"
module: 104
arm: "+"
pooled_cpm: 76.16
n_lines_expressing: 35
n_dd_up: 19
n_dd_down: 17
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 18
direction_downstream: 4
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# LTBP1

*latent transforming growth factor beta binding protein 1* — 2p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.25× (z +21.6, q 0e+00, up in 22 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.513× (z -12.5, q 4e-33, down in 24 of 33 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3RF3]] (+0.54, fdr 3e-05), [[CACNA1C]] (+0.52, fdr 2e-04), [[PLXNA2]] (+0.52, fdr 2e-05); moves opposite to [[TESMIN]] (-0.48, fdr 3e-05), [[LRRC27]] (-0.42, fdr 1e-04), [[CYB561D1]] (-0.40, fdr 1e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[ATP2B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 550.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +21.6 | 0e+00 | 22/34 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +15.8 | 0e+00 | 22/33 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +12.6 | 5e-34 | 24/34 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.94×** | +12.0 | 4e-31 | 19/33 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +9.0 | 3e-17 | 14/32 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.9 | 6e-10 | 15/35 (LS 180, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.6 | 4e-09 | 10/27 (C32, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.4 | 8e-09 | 16/33 (NCI-H460, A549, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.0 | 1e-07 | 13/31 (SW48, BT-474, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 1e-05 | 13/33 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.31×** | +5.1 | 2e-05 | 11/33 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +4.7 | 1e-04 | 10/34 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.23×** | +3.9 | 0.004 | 10/33 (NCI-H1573, PANC-1, …) | two highest doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.007 | 10/33 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.007 | 9/33 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.019 | 12/33 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.026 | 4/34 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.026 | 7/33 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.039 | 5/33 (LS 180, A549, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 550.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.513×** | -12.5 | 4e-33 | 24/33 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.601×** | -9.2 | 1e-17 | 25/33 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.658×** | -7.8 | 9e-13 | 23/33 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.684×** | -7.1 | 2e-10 | 22/33 (C-33 A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -6.6 | 5e-09 | 19/31 (RKO, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.705×** | -6.6 | 5e-09 | 19/33 (hTERT-HPNE, RPMI-7951, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.710×** | -6.4 | 1e-08 | 17/33 (A-427, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.710×** | -6.4 | 1e-08 | 21/31 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.799×** | -5.9 | 2e-07 | 21/33 (A549, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.738×** | -5.7 | 8e-07 | 19/33 (A-427, hTERT-HPNE, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.754×** | -5.3 | 7e-06 | 17/33 (A-172, RKO, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.768×** | -4.7 | 2e-04 | 15/33 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.798×** | -4.2 | 0.001 | 15/31 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.804×** | -4.1 | 0.002 | 15/33 (hTERT-HPNE, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.663×** | -4.0 | 0.002 | 15/32 (RPMI-7951, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.863× | -3.9 | 0.004 | 7/34 (NCI-H2347, C32, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.678×** | -3.8 | 0.005 | 8/32 (RKO, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 0.889× | -3.1 | 0.060 | 6/33 (HS-578T, C32, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.798×** | -3.0 | 0.077 | 3/33 (NCI-H1792, RPMI-7951, …) | two highest doses | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.893× | -3.0 | 0.081 | 9/34 (RPMI-7951, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 86.7 | 16 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 5.61× (z +13.4) | — |
| [[hTERT-HPNE (line)]] | wt | 642 | 2 | 12 (6 ⚠) | [[Budesonide (drug)]] 0.5 µM 3.06× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -14.3) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.169× (z -14.2) |
| [[HS-578T (line)]] | alt | 800 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -14.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -12.0) |
| [[SHP-77 (line)]] | alt | 67.9 | 0 | 9 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.216× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.290× (z -10.5) |
| [[A-427 (line)]] | wt | 62.8 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.139× (z -18.5) |
| [[NCI-H1573 (line)]] | alt | 26.3 | 7 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.05 µM 6.49× (z +11.7) | — |
| [[LoVo (line)]] | wt | 93.9 | 2 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +19.9) | [[Digitoxin (drug)]] 5 µM 0.417× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.418× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 336 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -11.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -11.2) |
| [[C-33 A (line)]] | alt | 91.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -13.1) |
| [[LS 180 (line)]] | wt | 68.4 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +12.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -9.7) |
| [[PANC-1 (line)]] | alt | 33.8 | 2 | 2 | [[Tucidinostat (drug)]] 5 µM 2.48× (z +12.4) | [[Ixazomib citrate (drug)]] 5 µM 0.367× (z -9.8) |
| [[RKO (line)]] | wt | 36.1 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.119× (z -15.0) |
| [[A498 (line)]] | wt | 26.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.1) ⚠ cell-cycle shift, explains ~75% of this change |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 336 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -11.4) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -10.2) |
| [[A549 (line)]] | wt | 48.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -16.2) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.186× (z -10.9) |
| [[HCT15 (line)]] | alt | 23.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.55× (z +12.7) | — |
| [[NCI-H460 (line)]] | wt | 41.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +14.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.343× (z -9.4) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 282 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.335× (z -11.2) |
| [[SW48 (line)]] | wt | 95.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.290× (z -8.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 90.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.350× (z -8.7) |
| [[BT-474 (line)]] | alt | 40.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +9.6) | — |
| [[C32 (line)]] | wt | 31.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.08× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 89.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.3) ⚠ cell-cycle shift, explains ~75% of this change |
| [[HT-29 (line)]] | alt | 19.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +11.7) | — |
| [[KATO III (line)]] | alt | 69.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.9) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H2347 (line)]] | alt | 26.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.04× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 81.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.309× (z -8.8) |
| [[AN3 CA (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.05 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.53 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.53 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3RF3]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[CACNA1C]] | +0.52 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[PLXNA2]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[KITLG]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ANPEP]] | +0.49 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[ITGA8]] | +0.48 | +0.37 / +0.46 | both halves | 8e-05 | pathway: Elastic fibre formation; STRING 590 |
| [[NPTX2]] | +0.48 | +0.45 / +0.36 | both halves | 1e-04 |  |
| [[DCN]] | +0.47 | +0.39 / +0.42 | both halves | 6e-05 | pathway: Extracellular matrix organization; STRING 600 |
| [[JAK2]] | +0.47 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[ONECUT2]] | +0.47 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[HIP1R]] | +0.46 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[PDGFRA]] | +0.46 | +0.35 / +0.52 | both halves | 1e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TESMIN]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[LRRC27]] | -0.42 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[CYB561D1]] | -0.40 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[DYNC2LI1]] | -0.39 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[TAB1]] | -0.38 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[MAFIP]] | -0.38 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[FPGT]] | -0.38 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[ATP6V0D1-DT]] | -0.38 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[AP3S2]] | -0.37 | -0.35 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LTBP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LOX]] | B | LOX activity raises LTBP1's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.60× lower at baseline in the lines without LOX | 0.024 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[DKK3]] | B | DKK3 activity raises LTBP1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 2.86× lower at baseline in the lines without DKK3 | 0.028 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1 |
| [[HTR1F]] | B | HTR1F activity raises LTBP1's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 2.56× lower at baseline in the lines without HTR1F | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent |
| [[PLAT]] | B | PLAT activity raises LTBP1's level | lines that do not express PLAT (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without PLAT | 0.035 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[ADAMTS2]] | B | ADAMTS2 activity raises LTBP1's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 2.13× lower at baseline in the lines without ADAMTS2 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1 |
| [[PTGFR]] | B | PTGFR activity raises LTBP1's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 2.30× lower at baseline in the lines without PTGFR | 0.041 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |
| [[LOX]] | B | LOX activity weakens LTBP1's drug response | lines that do not express LOX (20) vs lines expressing it (15) | the lines without LOX respond 3.22× as strongly (z diff -2.86); strongest at Idarubicin (hydrochloride) 5 µM: 2.10x vs 1.03x (z diff -6.6) | 0.046 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; target measured in part of the lines; artifact flags |
| [[FN1]] | B | FN1 activity raises LTBP1's level | lines that do not express FN1 (29) vs lines expressing it (21) | 2.43× lower at baseline in the lines without FN1 | 0.048 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[HTRA1]] | B | HTRA1 activity raises LTBP1's level | lines that do not express HTRA1 (19) vs lines expressing it (31) | 2.32× lower at baseline in the lines without HTRA1 | 0.048 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[NECTIN3]] | B | NECTIN3 activity raises LTBP1's level | lines that do not express NECTIN3 (11) vs lines expressing it (39) | 2.13× lower at baseline in the lines without NECTIN3 | 0.052 | ⚠ within organs, on part of the lines; also absent: CD96, NECTIN3-AS1, GPR176 |
| [[PXDN]] | B | PXDN activity raises LTBP1's level | lines that do not express PXDN (29) vs lines expressing it (21) | 2.74× lower at baseline in the lines without PXDN | 0.062 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP2B1]] | B | LTBP1 activity raises ATP2B1's level | lines that do not express LTBP1 (15) vs lines expressing it (35) | 1.92× lower at baseline in the lines without LTBP1 | 0.029 | ⚠ within organs, on part of the lines |
| [[TMTC1]] | B | LTBP1 activity raises TMTC1's level | lines that do not express LTBP1 (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without LTBP1 | 0.056 | ⚠ within organs, on part of the lines |
| [[GRB10]] | B | LTBP1 activity raises GRB10's level | lines that do not express LTBP1 (15) vs lines expressing it (35) | 2.88× lower at baseline in the lines without LTBP1 | 0.078 | ⚠ within organs, on part of the lines |
| [[KITLG]] | B | LTBP1 activity raises KITLG's level | lines that do not express LTBP1 (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without LTBP1 | 0.097 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.495). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.4, 17.0); signed map (21.2, 36.3). **Vector** length 97.0, 22.1% of its response variance represented; |z| ≥ 3 in 1,178 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +15.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +21.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.5 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -7.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.9 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | latent transforming growth factor beta binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.3 — chr2:32,946,953-33,399,509 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Latent transforming growth factor beta binding proteins |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 8 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; TGF-beta receptor signaling activates SMADs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14766](https://www.uniprot.org/uniprotkb/Q14766) (Latent-transforming growth factor beta-binding protein 1):

> Key regulator of transforming growth factor beta (TGFB1, TGFB2 and TGFB3) that controls TGF-beta activation by maintaining it in a latent state during storage in extracellular space. Associates specifically via disulfide bonds with the Latency-associated peptide (LAP), which is the regulatory chain of TGF-beta, and regulates integrin-dependent activation of TGF-beta. Outcompeted by LRRC32/GARP for binding to LAP regulatory chain of TGF-beta.

**Summary**, from NCBI Gene [4052](https://www.ncbi.nlm.nih.gov/gene/4052):

> The protein encoded by this gene belongs to the family of latent TGF-beta binding proteins (LTBPs). The secretion and activation of TGF-betas is regulated by their association with latency-associated proteins and with latent TGF-beta binding proteins. The product of this gene targets latent complexes of transforming growth factor beta to the extracellular matrix, where the latent cytokine is subsequently activated by several different mechanisms. Alternatively spliced transcript variants …

**Accessions** — [HGNC:6714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6714) · Entrez [4052](https://www.ncbi.nlm.nih.gov/gene/4052) · UniProt [Q14766](https://www.uniprot.org/uniprotkb/Q14766) · Ensembl [ENSG00000049323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049323)

## Data

Gene col 550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 550); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 550]; `tensor/DDL_lfc|DDL_z.npy` [550]; `embed/gene_vectors.npy` [550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 550 or target_col == 550). Every well: [[LTBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LTBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

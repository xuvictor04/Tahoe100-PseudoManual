---
symbol: "MRPL3"
type: "gene"
col: 3575
ensembl_id: "ENSG00000114686"
name: "mitochondrial ribosomal protein L3"
location: "3q22.1"
module: 4
arm: "+"
pooled_cpm: 82.4
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MRPL3

*mitochondrial ribosomal protein L3* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.39× (z +13.7, q 5e-40, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.499× (z -21.1, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR36]] (+0.79, fdr 7e-06), [[RIOX2]] (+0.77, fdr 7e-06), [[AGK]] (+0.76, fdr 7e-06); moves opposite to [[MICU1]] (-0.63, fdr 1e-05), [[AAMDC]] (-0.62, fdr 7e-06), [[EIF1B]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MVB12B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.39×** | +13.7 | 5e-40 | 45/49 (HOP62, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.55×** | +10.5 | 3e-23 | 37/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +9.9 | 5e-21 | 37/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +9.9 | 5e-21 | 44/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +9.0 | 3e-17 | 28/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +7.7 | 1e-12 | 36/45 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +7.3 | 3e-11 | 31/47 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +7.1 | 1e-10 | 34/47 (NCI-H1573, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.82×** | +6.7 | 1e-09 | 37/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +6.4 | 7e-09 | 26/38 (HOP62, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +5.5 | 2e-06 | 37/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.58×** | +5.1 | 2e-05 | 25/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.8 | 6e-05 | 0/50 | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.53×** | +4.8 | 8e-05 | 32/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.51×** | +4.6 | 2e-04 | 26/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.001 | 22/48 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.002 | 21/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +4.0 | 0.002 | 12/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.005 | 21/48 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.026 | 17/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.036 | 15/48 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.16× | +3.1 | 0.039 | 9/48 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.039 | 13/48 (RPMI-7951, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.499×** | -21.1 | 0e+00 | 44/49 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.745×** | -6.3 | 6e-08 | 31/48 (A498, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.817×** | -6.2 | 1e-07 | 21/48 (LoVo, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.755×** | -6.0 | 2e-07 | 25/48 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.835× | -5.5 | 4e-06 | 28/48 (LS 180, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.782×** | -5.3 | 1e-05 | 29/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -5.2 | 1e-05 | 22/48 (A-427, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.782×** | -5.1 | 2e-05 | 27/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.813×** | -4.5 | 5e-04 | 22/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.818×** | -4.3 | 8e-04 | 23/47 (SW48, LS 180, …) | two highest doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.836× | -3.9 | 0.005 | 19/48 (RKO, BT-474, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.838× | -3.7 | 0.011 | 19/47 (LoVo, HS-578T, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.6 | 0.012 | 22/48 (RKO, HOP62, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.846× | -3.6 | 0.013 | 17/48 (KATO III, SW48, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.905× | -3.0 | 0.084 | 12/48 (hTERT-HPNE, MIA PaCa-2, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.764×** | -3.0 | 0.084 | 9/49 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 65.2 | 3 (1 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.99× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -19.3) |
| [[PANC-1 (line)]] | alt | 109 | 4 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.79× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.01× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -15.0) |
| [[SW480 (line)]] | alt | 94.5 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.47× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -14.2) |
| [[HT-29 (line)]] | alt | 50.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +10.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -8.8) |
| [[LoVo (line)]] | wt | 82.7 | 2 (1 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 2.14× (z +9.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 3.75× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 111 | 3 (3 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.35× (z +10.0) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -14.1) |
| [[A498 (line)]] | wt | 103 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 128 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 4.13× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 68.4 | 2 (2 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.05× (z +11.8) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 64.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +11.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 100 | 2 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 4.91× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -12.6) |
| [[RKO (line)]] | wt | 109 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.84× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -23.6) |
| [[SNU-1 (line)]] | wt | 140 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -13.0) |
| [[SNU-423 (line)]] | alt | 44.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 45.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +10.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -11.0) |
| [[BT-474 (line)]] | alt | 92.3 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.74× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -13.4) |
| [[J82 (line)]] | alt | 71.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -12.4) |
| [[KATO III (line)]] | alt | 60.6 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.81× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -11.0) |
| [[LS 180 (line)]] | wt | 76.2 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 4.79× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 120 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.60× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -15.8) |
| [[SW1417 (line)]] | alt | 103 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -14.6) |
| [[A-427 (line)]] | wt | 138 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.501× (z -12.4) |
| [[A549 (line)]] | wt | 53.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 43.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -13.1) |
| [[C-33 A (line)]] | alt | 93.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -8.5) |
| [[C32 (line)]] | wt | 54.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -16.6) |
| [[CFPAC-1 (line)]] | alt | 50.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.61× (z +11.7) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[Hs 766T (line)]] | wt | 46.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 52.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 75.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 88.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -18.3) |
| [[SW48 (line)]] | wt | 135 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -15.6) |
| [[AN3 CA (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 86.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR36]] | +0.79 | +0.82 / +0.79 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.77 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[AGK]] | +0.76 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[ATIC]] | +0.74 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[PRPF19]] | +0.74 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[CAD]] | +0.73 | +0.61 / +0.81 | both halves | 7e-06 |  |
| [[MRPL42]] | +0.73 | +0.67 / +0.77 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 952 |
| [[FARSB]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 | STRING 581 |
| [[POLR1B]] | +0.72 | +0.81 / +0.67 | both halves | 7e-06 | STRING 783 |
| [[PFAS]] | +0.72 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[DLAT]] | +0.71 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.71 | +0.69 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICU1]] | -0.63 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.62 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[EIF1B]] | -0.62 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[SHOC2]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MVB12B]] | B | MVB12B activity raises MRPL3's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without MVB12B | 0.086 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises MRPL3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.782). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.5, -38.0); signed map (-8.2, -48.3). **Vector** length 122, 39.4% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA Aminoacylation* (reactome, mean cos +0.50 to 7); *tRNA processing in the nucleus* (reactome, mean cos +0.55 to 8); *tRNA processing* (reactome, mean cos +0.55 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.5 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +9.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.3 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +10.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.8 | +6.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.8 | +5.1 |
|  | [[EX229 (drug)]] 5 µM |  | +4.6 | +5.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.1 | +4.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -21.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.0 | +4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.3 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.8 | -4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.6 | -1.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.9 | -3.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:131,462,212-131,502,983 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRL3, uL3m; previously RPML3 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small nucleolar RNA protein coding host genes; Large subunit mitochondrial ribosomal proteins |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [P09001](https://www.uniprot.org/uniprotkb/P09001) carries no function annotation.

**Summary**, from NCBI Gene [11222](https://www.ncbi.nlm.nih.gov/gene/11222):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:10379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10379) · Entrez [11222](https://www.ncbi.nlm.nih.gov/gene/11222) · UniProt [P09001](https://www.uniprot.org/uniprotkb/P09001) · Ensembl [ENSG00000114686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114686)

## Data

Gene col 3575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3575); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3575]; `tensor/DDL_lfc|DDL_z.npy` [3575]; `embed/gene_vectors.npy` [3575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3575 or target_col == 3575). Every well: [[MRPL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

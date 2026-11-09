---
symbol: "GMCL1"
type: "gene"
col: 1502
ensembl_id: "ENSG00000087338"
name: "germ cell-less 1, spermatogenesis associated"
location: "2p13.3"
module: 40
arm: "+"
pooled_cpm: 81.55
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 28
n_dd_up_clean: 7
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# GMCL1

*germ cell-less 1, spermatogenesis associated* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 3.21× (z +18.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.492× (z -11.0, q 3e-25, down in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.495× (z -10.8, q 8e-25, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOSPD3]] (+0.80, fdr 7e-06), [[SDHAP1]] (+0.79, fdr 7e-06), [[HSPB11]] (+0.77, fdr 7e-06); moves opposite to [[ST7L]] (-0.80, fdr 7e-06), [[FKRP]] (-0.76, fdr 1e-05), [[ZC3H4]] (-0.76, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.21×** | +18.8 | 0e+00 | 48/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.02×** | +17.7 | 0e+00 | 47/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.93×** | +17.3 | 0e+00 | 47/48 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +9.1 | 1e-17 | 46/48 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +7.0 | 4e-10 | 40/48 (HT-29, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.5 | 7e-09 | 29/49 (A-172, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +6.0 | 1e-07 | 40/49 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.17× | +3.4 | 0.040 | 15/48 (HT-29, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1502.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -11.0 | 3e-25 | 38/44 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.495×** | -10.8 | 8e-25 | 44/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.498×** | -10.8 | 9e-25 | 39/48 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.653×** | -9.5 | 3e-19 | 33/48 (NCI-H2347, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.557×** | -9.4 | 5e-19 | 37/48 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.540×** | -9.2 | 4e-18 | 35/45 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.561×** | -8.9 | 5e-17 | 38/49 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.581×** | -8.7 | 2e-16 | 44/48 (A498, NCI-H2347, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.741×** | -6.7 | 1e-09 | 38/48 (SW 900, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.653×** | -6.6 | 2e-09 | 34/47 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.733×** | -4.6 | 2e-04 | 30/47 (A549, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.752×** | -4.4 | 5e-04 | 31/48 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.761×** | -4.4 | 5e-04 | 29/49 (COLO 205, RPMI-7951, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.780×** | -4.0 | 0.003 | 24/48 (A549, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.790×** | -3.8 | 0.006 | 25/49 (SW 900, HS-578T, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.651×** | -3.6 | 0.011 | 24/47 (AsPC-1, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.804×** | -3.5 | 0.015 | 22/48 (NCI-H1792, LS 180, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.854× | -3.5 | 0.015 | 12/48 (SHP-77, SW 1088, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.805×** | -3.5 | 0.015 | 22/48 (HS-578T, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 98.6 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -15.9) |
| [[A498 (line)]] | wt | 118 | 4 | 6 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.315× (z -13.4) |
| [[SW480 (line)]] | alt | 118 | 9 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +15.6) | — |
| [[A549 (line)]] | wt | 91.7 | 3 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.31× (z +11.9) | [[Harringtonine (drug)]] 0.5 µM 0.328× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 111 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.311× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 87.4 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.15× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.408× (z -9.2) |
| [[SW 900 (line)]] | alt | 138 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.390× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 113 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.72× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.406× (z -8.5) |
| [[A-172 (line)]] | wt | 69.8 | 4 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.92× (z +13.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -11.8) |
| [[A-427 (line)]] | wt | 95.4 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0750× (z -26.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 60.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.26× (z +13.6) | — |
| [[LOX-IMVI (line)]] | wt | 43.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.01× (z +17.6) | — |
| [[NCI-H1573 (line)]] | alt | 60.5 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 2.91× (z +11.0) | [[Harringtonine (drug)]] 5 µM 0.372× (z -9.7) |
| [[SNU-423 (line)]] | alt | 61.8 | 3 | 2 | [[Belinostat (drug)]] 5 µM 2.92× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 75.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.79× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -12.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 82.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.34× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.0898× (z -19.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 49.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.10× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.210× (z -10.5) ⚠ toxic |
| [[HOP62 (line)]] | alt | 85.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -10.3) |
| [[HS-578T (line)]] | alt | 77.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -10.6) |
| [[KATO III (line)]] | alt | 88.0 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.27× (z +11.6) | [[Harringtonine (drug)]] 5 µM 0.326× (z -10.6) |
| [[LoVo (line)]] | wt | 69.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.48× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 82.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.85× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 57.3 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.90× (z +14.9) | [[Harringtonine (drug)]] 5 µM 0.393× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 74.7 | 2 | 2 | [[Panobinostat (drug)]] 0.5 µM 2.67× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -12.3) |
| [[SNU-1 (line)]] | wt | 77.6 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.91× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -8.9) |
| [[C32 (line)]] | wt | 52.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.52× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 107 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -11.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 74.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +13.7) | — |
| [[Hs 766T (line)]] | wt | 74.0 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.01× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -9.3) |
| [[J82 (line)]] | alt | 40.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.68× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 73.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 91.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 69.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.60× (z +13.5) | — |
| [[Panc 03.27 (line)]] | alt | 72.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.78× (z +12.3) | — |
| [[RKO (line)]] | wt | 76.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 102 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +12.8) | — |
| [[BT-474 (line)]] | alt | 41.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 48.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +10.4) | — |
| [[SW48 (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -11.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 83.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -10.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 64.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 77.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.229× (z -8.7) |
| [[SHP-77 (line)]] | alt | 63.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +8.6) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SW 1088 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0635× (z -9.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSPD3]] | +0.80 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.79 | +0.85 / +0.59 | both halves | 7e-06 |  |
| [[HSPB11]] | +0.77 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[ARL3]] | +0.77 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.76 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.76 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.76 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[PLEKHH3]] | +0.76 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[ELP2]] | +0.74 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.74 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[SLC31A1]] | +0.74 | +0.75 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7L]] | -0.80 | -0.78 / -0.65 | both halves | 7e-06 |  |
| [[FKRP]] | -0.76 | -0.79 / -0.56 | both halves | 1e-05 |  |
| [[ZC3H4]] | -0.76 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[RAB30-DT]] | -0.75 | -0.78 / -0.56 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.75 | -0.79 / -0.67 | both halves | 7e-06 |  |
| [[ZSCAN29]] | -0.75 | -0.75 / -0.60 | both halves | 7e-06 |  |
| [[ZNF655]] | -0.72 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[WARS2-AS1]] | -0.72 | -0.74 / -0.44 | both halves | 3e-05 |  |
| [[UTP20]] | -0.72 | -0.71 / -0.62 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.72 | -0.73 / -0.59 | both halves | 7e-06 |  |
| [[SLC9A8]] | -0.71 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[PPP3CB-AS1]] | -0.71 | -0.68 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers GMCL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[P3H1]] | C | P3H1 activity raises GMCL1's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without P3H1 | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.848). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (3.5, -14.1); signed map (-35.1, 15.4). **Vector** length 151, 53.2% of its response variance represented; |z| ≥ 3 in 1,283 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +10.0 | +17.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +9.0 | +17.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +8.5 | +18.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +7.0 | +7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.7 | +9.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +6.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | +2.9 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +2.6 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -13.2 | -9.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -12.2 | -10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -11.5 | -10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -11.5 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -9.6 | -8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.6 | -6.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.5 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | germ cell-less 1, spermatogenesis associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:69,829,660-69,881,384 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13057, BTBD13, GCL1, SPATA29 |
| Gene groups (HGNC) | BTB domain containing |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IK5](https://www.uniprot.org/uniprotkb/Q96IK5) (Germ cell-less protein-like 1):

> Possible function in spermatogenesis. Enhances the degradation of MDM2 and increases the amount of p53 probably by modulating the nucleocytoplasmic transport (By similarity).

**Summary**, from NCBI Gene [64395](https://www.ncbi.nlm.nih.gov/gene/64395):

> This gene encodes a nuclear envelope protein that appears to be involved in spermatogenesis, either directly or by influencing genes that play a more direct role in the process. This multi-exon locus is the homolog of the mouse and drosophila germ cell-less gene but the human genome also contains a single-exon locus on chromosome 5 that contains an open reading frame capable of encoding a highly-related protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23843](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23843) · Entrez [64395](https://www.ncbi.nlm.nih.gov/gene/64395) · UniProt [Q96IK5](https://www.uniprot.org/uniprotkb/Q96IK5) · Ensembl [ENSG00000087338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087338)

## Data

Gene col 1502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1502); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1502]; `tensor/DDL_lfc|DDL_z.npy` [1502]; `embed/gene_vectors.npy` [1502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1502 or target_col == 1502). Every well: [[GMCL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMCL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

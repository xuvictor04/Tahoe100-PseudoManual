---
symbol: "TCP10L"
type: "gene"
col: 14306
ensembl_id: "ENSG00000242220"
name: "t-complex 10 like"
location: "21q22.11"
module: 139
arm: "+"
pooled_cpm: 20.09
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 34
n_dd_up_clean: 12
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# TCP10L

*t-complex 10 like* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.62× (z +8.7, q 1e-15, up in 30 of 46 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.42× (z +6.3, q 6e-08, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.331× (z -14.1, q 1e-42, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP298-TCP10L]] (+0.90, fdr 7e-06, ⚠ same locus), [[MMP1]] (+0.57, fdr 1e-05), [[SERPIND1]] (+0.52, fdr 1e-05), [[EPHB6]] (+0.49, fdr 2e-04); moves opposite to [[ACSL1]] (-0.53, fdr 3e-05), [[FKBP5]] (-0.53, fdr 2e-05), [[NNMT]] (-0.52, fdr 1e-04).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.62×** | +8.7 | 1e-15 | 30/46 (RKO, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +6.3 | 6e-08 | 25/46 (A498, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +5.5 | 6e-06 | 21/46 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +5.4 | 1e-05 | 24/45 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 6e-04 | 15/46 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +4.5 | 6e-04 | 19/46 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.002 | 17/46 (PANC-1, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.002 | 17/45 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.22×** | +3.7 | 0.014 | 19/44 (HEC-1-A, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.6 | 0.021 | 6/27 (HEC-1-A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +3.4 | 0.031 | 11/45 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.031 | 17/46 (NCI-H1573, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.031 | 12/46 (LoVo, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.29×** | +3.3 | 0.035 | 11/45 (NCI-H1573, MIA PaCa-2, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +3.2 | 0.052 | 7/45 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.052 | 14/46 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.054 | 11/45 (PANC-1, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.071 | 10/46 (SW48, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14306.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.331×** | -14.1 | 1e-42 | 39/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.352×** | -13.3 | 4e-38 | 31/42 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.419×** | -10.7 | 2e-24 | 32/45 (PANC-1, A-427, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.471×** | -9.6 | 1e-19 | 32/45 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.489×** | -9.1 | 8e-18 | 28/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.650×** | -7.7 | 9e-13 | 25/44 (HepG2/C3A, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.563×** | -7.3 | 2e-11 | 24/44 (PANC-1, HepG2/C3A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.569×** | -6.9 | 3e-10 | 25/40 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.627×** | -5.9 | 2e-07 | 24/46 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.447×** | -5.4 | 4e-06 | 26/44 (SW480, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.656×** | -5.4 | 4e-06 | 25/45 (NCI-H460, A549, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.671×** | -5.0 | 3e-05 | 22/46 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.476×** | -5.0 | 3e-05 | 20/42 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.675×** | -4.9 | 4e-05 | 19/46 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.777×** | -4.5 | 2e-04 | 21/46 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.695×** | -4.4 | 3e-04 | 20/44 (SK-MEL-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.701×** | -4.3 | 5e-04 | 18/45 (HOP62, AsPC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.707×** | -4.2 | 7e-04 | 21/45 (LS 180, C-33 A, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.539×** | -4.1 | 0.001 | 18/40 (SW480, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.549×** | -4.0 | 0.002 | 15/42 (PANC-1, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.731×** | -4.0 | 0.002 | 17/45 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.730×** | -3.9 | 0.002 | 15/45 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.737×** | -3.9 | 0.003 | 17/45 (NCI-H460, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 50.1 | 0 | 13 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -19.4) |
| [[PANC-1 (line)]] | alt | 22.2 | 0 | 11 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0849× (z -20.9) |
| [[AsPC-1 (line)]] | alt | 36.6 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -15.2) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.223× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 70.4 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0423× (z -26.5) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 23.8 | 0 | 8 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.105× (z -14.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -10.2) |
| [[A-427 (line)]] | wt | 36.6 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.155× (z -13.3) |
| [[HOP62 (line)]] | alt | 29.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -14.5) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -10.4) |
| [[A-172 (line)]] | wt | 42.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.5) ⚠ cell-cycle shift, explains ~93% of this change |
| [[A549 (line)]] | wt | 17.5 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.101× (z -13.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 34.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 45.5 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.144× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~72% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.271× (z -9.1) |
| [[SW1417 (line)]] | alt | 37.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.5) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -8.8) |
| [[A498 (line)]] | wt | 7.19 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +8.9) ⚠ cell-cycle shift, explains ~23% of this change | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -9.1) ⚠ cell-cycle shift, explains ~93% of this change |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 2 | — | [[Talc (drug)]] 0.05 µM 0.0505× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -14.5) ⚠ cell-cycle shift, explains ~93% of this change |
| [[COLO 205 (line)]] | alt | 8.31 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0771× (z -8.5) |
| [[H4 (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0650× (z -10.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 10.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +10.0) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[LoVo (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.236× (z -9.8) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 5.16 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +9.9) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[LS 180 (line)]] | wt | 24.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.189× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0410× (z -12.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -11.0) |
| [[RKO (line)]] | wt | 7.18 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 5.43× (z +9.2) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SW48 (line)]] | wt | 17.9 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0807× (z -9.0) |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP298-TCP10L]] | +0.90 | +0.91 / +0.89 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[MMP1]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SERPIND1]] | +0.52 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[EPHB6]] | +0.49 | +0.32 / +0.59 | both halves | 2e-04 |  |
| [[MANCR]] | +0.49 | +0.40 / +0.45 | both halves | 4e-05 |  |
| [[FST]] | +0.48 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[TRBC2]] | +0.47 | +0.35 / +0.34 | both halves | 1e-04 |  |
| [[IGDCC4]] | +0.47 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[SYNJ2]] | +0.46 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[SH2D2A]] | +0.46 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[PRDM8]] | +0.46 | +0.27 / +0.47 | both halves | 3e-04 |  |
| [[LINC03042]] | +0.45 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[ADAM19]] | +0.45 | +0.33 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACSL1]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[FKBP5]] | -0.53 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[NNMT]] | -0.52 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[TSC22D3]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[FSTL3]] | -0.49 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[DCN]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[SAA1]] | -0.46 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[SLC16A7]] | -0.46 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[MGP]] | -0.45 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[KLF9]] | -0.45 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[MT1E]] | -0.45 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[ADPRHL1]] | -0.45 | -0.35 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers TCP10L's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction -0.449). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.5, 16.3); signed map (12.3, 52.6). **Vector** length 86.5, 19.6% of its response variance represented; |z| ≥ 3 in 1,444 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.6 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +4.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.2 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.1 | -10.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.5 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.5 | -3.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -3.3 | -2.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.2 | -5.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -3.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | t-complex 10 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:32,497,967-32,587,373 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRED77 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDR4](https://www.uniprot.org/uniprotkb/Q8TDR4) (T-complex protein 10A homolog 1):

> May be involved in transcriptional regulation. Has in vitro transcription inhibition activity. Acts as a tumor suppressor in hepatocellular carcinoma (HCC) cells.

**Summary**, from NCBI Gene [140290](https://www.ncbi.nlm.nih.gov/gene/140290):

> Enables DNA-binding transcription factor binding activity; identical protein binding activity; and transcription corepressor activity. Involved in negative regulation of transcription by RNA polymerase II. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11657](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11657) · Entrez [140290](https://www.ncbi.nlm.nih.gov/gene/140290) · UniProt [Q8TDR4](https://www.uniprot.org/uniprotkb/Q8TDR4) · Ensembl [ENSG00000242220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242220)

## Data

Gene col 14306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14306); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14306]; `tensor/DDL_lfc|DDL_z.npy` [14306]; `embed/gene_vectors.npy` [14306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14306 or target_col == 14306). Every well: [[TCP10L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCP10L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

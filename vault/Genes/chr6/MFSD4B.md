---
symbol: "MFSD4B"
type: "gene"
col: 10355
ensembl_id: "ENSG00000173214"
name: "solute carrier family 60 member 2"
location: "6q21"
module: 112
arm: "+"
pooled_cpm: 63.91
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# MFSD4B

*solute carrier family 60 member 2* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.64× (z +18.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.597× (z -9.9, q 2e-20, down in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.688× (z -7.2, q 1e-10, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEM]] (+0.53, fdr 5e-05), [[CALN1]] (+0.50, fdr 1e-05), [[ATP6AP1L]] (+0.49, fdr 4e-05); moves opposite to [[JAK2]] (-0.58, fdr 2e-05), [[NOD1]] (-0.53, fdr 1e-04), [[RHOBTB1]] (-0.51, fdr 5e-04).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.64×** | +18.7 | 0e+00 | 48/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.37×** | +16.6 | 0e+00 | 48/48 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +14.6 | 0e+00 | 46/48 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +9.4 | 8e-19 | 38/48 (A498, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +9.0 | 3e-17 | 42/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.35×** | +8.2 | 2e-14 | 35/48 (A498, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +8.2 | 2e-14 | 30/48 (HCT15, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +6.7 | 2e-09 | 36/49 (KATO III, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +6.6 | 3e-09 | 34/49 (PANC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +5.8 | 4e-07 | 32/48 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.28×** | +4.7 | 1e-04 | 27/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +4.5 | 3e-04 | 23/48 (MIA PaCa-2, HT-29, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.002 | 20/49 (NCI-H23, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.002 | 24/48 (PANC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.003 | 22/48 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.029 | 17/48 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.031 | 16/48 (A-427, HCT15, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10355.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.597×** | -9.9 | 2e-20 | 37/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.646×** | -8.4 | 1e-14 | 36/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.669×** | -7.4 | 2e-11 | 29/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.688×** | -7.2 | 1e-10 | 30/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -6.5 | 8e-09 | 33/48 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.743×** | -5.7 | 1e-06 | 27/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.588×** | -5.3 | 8e-06 | 28/48 (SNU-1, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.593×** | -5.2 | 1e-05 | 29/49 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.773×** | -4.9 | 5e-05 | 28/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.841× | -4.7 | 2e-04 | 18/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.837× | -3.4 | 0.032 | 18/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.842× | -3.3 | 0.048 | 13/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.839× | -3.2 | 0.051 | 16/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.845× | -3.2 | 0.051 | 19/47 (COLO 205, LOX-IMVI, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.888× | -3.2 | 0.052 | 10/49 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.848× | -3.0 | 0.080 | 15/48 (CFPAC-1, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 119 | 3 | 7 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +14.1) | [[Digitoxin (drug)]] 5 µM 0.328× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.471× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 142 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -26.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.541× (z -10.9) |
| [[A498 (line)]] | wt | 35.6 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.19× (z +12.4) | — |
| [[KATO III (line)]] | alt | 97.6 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.84× (z +11.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.434× (z -9.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 80.3 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.59× (z +11.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.435× (z -10.1) ⚠ toxic |
| [[A-172 (line)]] | wt | 49.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.97× (z +15.9) | — |
| [[HOP62 (line)]] | alt | 47.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.82× (z +12.9) | — |
| [[SNU-423 (line)]] | alt | 121 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.67× (z +12.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.321× (z -10.5) ⚠ toxic |
| [[SW480 (line)]] | alt | 77.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.417× (z -10.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 17.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.92× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 60.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 40.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.42× (z +13.7) | — |
| [[J82 (line)]] | alt | 45.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.01× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 65.5 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.0) | [[Digitoxin (drug)]] 0.5 µM 0.399× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 41.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.50× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 52.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 65.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +10.3) | — |
| [[A-427 (line)]] | wt | 45.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +10.5) | — |
| [[A549 (line)]] | wt | 36.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.88× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 126 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[HS-578T (line)]] | alt | 63.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.56× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 47.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +9.8) | — |
| [[NCI-H661 (line)]] | alt | 40.5 | 0 | 2 | — | [[Budesonide (drug)]] 0.05 µM 0.0675× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0864× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Canagliflozin (drug)]] 0.05 µM 0.105× (z -9.1) |
| [[AN3 CA (line)]] | alt | 86.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -9.9) ⚠ toxic |
| [[C-33 A (line)]] | alt | 72.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 68.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.22× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 86.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.421× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 53.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.89× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 79.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.373× (z -9.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 54.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 42.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +8.5) | — |
| [[SW48 (line)]] | wt | 45.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.6) | — |
| [[C32 (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 95.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 85.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEM]] | +0.53 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[CALN1]] | +0.50 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ATP6AP1L]] | +0.49 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[GMDS-DT]] | +0.49 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[ATP7A]] | +0.47 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[IER3]] | +0.47 | +0.36 / +0.40 | both halves | 1e-04 |  |
| [[ZFPM2-AS1]] | +0.47 | +0.33 / +0.43 | both halves | 1e-04 |  |
| [[HIF1A-AS3]] | +0.47 | +0.33 / +0.44 | both halves | 1e-04 |  |
| [[UBA6-DT]] | +0.46 | +0.66 / +0.39 | both halves | 5e-05 |  |
| [[XKR6]] | +0.45 | +0.38 / +0.50 | both halves | 6e-05 |  |
| [[XRRA1]] | +0.45 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[TMEM14B]] | +0.44 | +0.32 / +0.50 | both halves | 2e-04 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAK2]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[NOD1]] | -0.53 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[RHOBTB1]] | -0.51 | -0.42 / -0.24 | both halves | 5e-04 |  |
| [[ZYG11A]] | -0.50 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[MAP3K6]] | -0.48 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[NUP85]] | -0.47 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[DSCC1]] | -0.46 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[MFSD14B]] | -0.46 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[SLC38A9]] | -0.46 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[STIM1]] | -0.46 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[AUNIP]] | -0.45 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[ZNF142]] | -0.45 | -0.37 / -0.38 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises MFSD4B's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without FSIP2-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[EPIC1]] | B | EPIC1 activity raises MFSD4B's level | lines that do not express EPIC1 (23) vs lines expressing it (27) | 1.54× lower at baseline in the lines without EPIC1 | 0.067 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000243620, POTEE, FAR2P1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.381). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.9, 31.2); signed map (35.0, -12.8). **Vector** length 68.3, 15.0% of its response variance represented; |z| ≥ 3 in 1,279 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.9 | +6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.5 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.7 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -6.5 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.9 | +1.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.9 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.7 | -7.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | +0.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.6 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 60 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:111,259,327-111,445,354 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33953; previously KIAA1919, MFSD4B |
| Gene groups (HGNC) | Solute carrier family 60 |
| Reactome | 3 pathways, smallest: Cellular hexose transport; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TF39](https://www.uniprot.org/uniprotkb/Q5TF39) (Solute carrier family 60 member 2):

> Low-affinity Na(+)-dependent glucose symporter with a Na(+) to glucose coupling ratio of 1:1. Potential channels for urea in the inner medulla of kidney.

**Summary**, from NCBI Gene [91749](https://www.ncbi.nlm.nih.gov/gene/91749):

> Predicted to enable D-glucose:sodium symporter activity. Predicted to be involved in D-glucose import across plasma membrane. Predicted to be located in brush border membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21053) · Entrez [91749](https://www.ncbi.nlm.nih.gov/gene/91749) · UniProt [Q5TF39](https://www.uniprot.org/uniprotkb/Q5TF39) · Ensembl [ENSG00000173214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173214)

## Data

Gene col 10355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10355); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10355]; `tensor/DDL_lfc|DDL_z.npy` [10355]; `embed/gene_vectors.npy` [10355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10355 or target_col == 10355). Every well: [[MFSD4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "OXNAD1"
type: "gene"
col: 7842
ensembl_id: "ENSG00000154814"
name: "oxidoreductase NAD binding domain containing 1"
location: "3p25.1-p24.3"
module: 40
arm: "+"
pooled_cpm: 39.35
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# OXNAD1

*oxidoreductase NAD binding domain containing 1* — 3p25.1-p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.98× (z +24.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.623× (z -10.6, q 2e-23, down in 32 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.633× (z -10.3, q 3e-22, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRC1]] (+0.76, fdr 7e-06), [[THOC3]] (+0.73, fdr 7e-06), [[NPRL2]] (+0.72, fdr 7e-06); moves opposite to [[SKIL]] (-0.64, fdr 1e-05), [[PNRC2]] (-0.64, fdr 1e-05), [[ZNF702P]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SEC13]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.98×** | +24.3 | 0e+00 | 48/48 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.67×** | +21.9 | 0e+00 | 48/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.43×** | +19.8 | 0e+00 | 47/48 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +9.6 | 1e-19 | 39/48 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +7.3 | 4e-11 | 34/48 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +6.4 | 2e-08 | 25/48 (SK-MEL-2, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.32×** | +5.9 | 2e-07 | 23/48 (SW480, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.21×** | +5.9 | 3e-07 | 23/48 (SHP-77, SW480, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +5.0 | 3e-05 | 2/48 (NCI-H23, CHP-212) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.23×** | +4.4 | 5e-04 | 19/48 (SW480, Panc 03.27, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +4.4 | 5e-04 | 17/48 (NCI-H460, CFPAC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.15× | +4.3 | 1e-03 | 17/48 (NCI-H460, C32, …) | rises with dose | low cells (technical?) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.13× | +3.9 | 0.005 | 12/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.18× | +3.6 | 0.013 | 15/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7842.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -10.6 | 2e-23 | 32/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.633×** | -10.3 | 3e-22 | 33/48 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.704×** | -7.3 | 6e-11 | 26/43 (SNU-423, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.747×** | -6.6 | 8e-09 | 28/48 (SHP-77, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.829×** | -6.0 | 3e-07 | 24/47 (A498, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.769×** | -5.9 | 3e-07 | 21/48 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.770×** | -5.9 | 3e-07 | 20/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.763×** | -5.9 | 3e-07 | 21/39 (SHP-77, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.786×** | -5.4 | 4e-06 | 23/46 (NCI-H23, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.805×** | -4.9 | 6e-05 | 22/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.809×** | -4.8 | 9e-05 | 17/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.865× | -4.6 | 2e-04 | 19/48 (KATO III, HEC-1-A, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.834× | -4.1 | 0.002 | 12/48 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.822×** | -4.1 | 0.002 | 16/47 (H4, HS-578T, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 0.856× | -3.5 | 0.017 | 20/47 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.752×** | -3.4 | 0.027 | 12/48 (C32, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.863× | -3.3 | 0.028 | 14/48 (KATO III, A498, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.869× | -3.2 | 0.044 | 12/48 (Hs 766T, SW48, …) | inconsistent across doses |  |
| [[Cyclosporin A (drug)]] 5 µM |  | 0.871× | -3.1 | 0.047 | 11/48 (AsPC-1, J82, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.876× | -3.0 | 0.072 | 12/48 (SW 1088, NCI-H1573, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.880× | -2.9 | 0.098 | 5/48 (HCT15, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 57.2 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -15.8) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.398× (z -10.0) |
| [[HS-578T (line)]] | alt | 50.1 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.45× (z +10.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -11.6) ⚠ cell-cycle shift, explains ~76% of this change |
| [[SW480 (line)]] | alt | 40.2 | 5 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +15.0) | [[Digitoxin (drug)]] 5 µM 0.512× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 37.9 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.91× (z +15.3) | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 43.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.82× (z +13.6) | [[Dinaciclib (drug)]] 0.05 µM 0.399× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 39.4 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.97× (z +10.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.406× (z -9.0) ⚠ cell-cycle shift, explains ~76% of this change |
| [[NCI-H460 (line)]] | wt | 25.3 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.11× (z +14.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.417× (z -8.8) |
| [[SHP-77 (line)]] | alt | 87.5 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.42× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.390× (z -10.3) |
| [[SNU-423 (line)]] | alt | 28.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.96× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 25.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 29.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -14.5) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -10.4) |
| [[C32 (line)]] | wt | 26.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.90× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 62.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +10.6) | — |
| [[J82 (line)]] | alt | 36.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.80× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -9.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 19.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.46× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.68× (z +13.2) | — |
| [[NCI-H1792 (line)]] | alt | 38.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.73× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 32.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 47.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.48× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -16.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 26.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 57.6 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.93× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -10.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 56.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +12.2) | — |
| [[SW1417 (line)]] | alt | 54.9 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.45× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.358× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.404× (z -9.6) |
| [[A-427 (line)]] | wt | 53.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 25.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.58× (z +9.9) | — |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 2 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.104× (z -9.0) |
| [[RKO (line)]] | wt | 37.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.40× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.354× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 50.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.240× (z -8.5) |
| [[HCT15 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -12.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 28.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 27.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.03× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC1]] | +0.76 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[THOC3]] | +0.73 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[NPRL2]] | +0.72 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.71 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.71 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[COG5]] | +0.70 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[RARS2]] | +0.70 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.70 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[IER3IP1]] | +0.70 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[GPR107]] | +0.69 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.69 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[RINT1]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKIL]] | -0.64 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.64 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[ZNF702P]] | -0.61 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[FKRP]] | -0.61 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[BMPR1B]] | -0.59 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[PPP1R1C]] | -0.58 | -0.48 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers OXNAD1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers OXNAD1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEC13]] | C | OXNAD1's natural level strengthens SEC13's drug response | OXNAD1's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.08; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.770). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (0.5, -17.5); signed map (-47.1, 7.3). **Vector** length 107, 28.2% of its response variance represented; |z| ≥ 3 in 1,160 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.0 | +19.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +24.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +21.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.4 | +7.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.4 | +1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.2 | +3.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.2 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -8.6 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.9 | -6.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -5.5 | -3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.0 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | oxidoreductase NAD binding domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1-p24.3 — chr3:16,265,160-16,350,299 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15763; previously RFTN1-AS1 |
| Gene groups (HGNC) | Oxidoreductases |
| Matched by | ensembl_id |

UniProt [Q96HP4](https://www.uniprot.org/uniprotkb/Q96HP4) carries no function annotation.

**Summary**, from NCBI Gene [92106](https://www.ncbi.nlm.nih.gov/gene/92106):

> Predicted to enable oxidoreductase activity. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25128) · Entrez [92106](https://www.ncbi.nlm.nih.gov/gene/92106) · UniProt [Q96HP4](https://www.uniprot.org/uniprotkb/Q96HP4) · Ensembl [ENSG00000154814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154814)

## Data

Gene col 7842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7842); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7842]; `tensor/DDL_lfc|DDL_z.npy` [7842]; `embed/gene_vectors.npy` [7842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7842 or target_col == 7842). Every well: [[OXNAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OXNAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "SMAD1"
type: "gene"
col: 9941
ensembl_id: "ENSG00000170365"
name: "SMAD family member 1"
location: "4q31.21"
module: 11
arm: "+"
pooled_cpm: 25.91
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 17
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SMAD1

*SMAD family member 1* — 4q31.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +15.6, q 0e+00, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.282× (z -20.8, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UQCRFS1]] (+0.70, fdr 1e-05), [[KLHL42]] (+0.69, fdr 1e-05), [[POLR3C]] (+0.68, fdr 1e-05); moves opposite to [[GNAI2]] (-0.67, fdr 2e-04), [[SPAG9]] (-0.63, fdr 2e-05), [[F11R]] (-0.61, fdr 1e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CGAS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +15.6 | 0e+00 | 38/46 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.50×** | +7.9 | 1e-12 | 29/47 (LoVo, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.33×** | +6.7 | 5e-09 | 26/47 (PANC-1, C-33 A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +5.6 | 2e-06 | 25/46 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +5.0 | 6e-05 | 26/46 (AsPC-1, A498, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 4e-04 | 21/47 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +4.5 | 5e-04 | 18/46 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +4.5 | 6e-04 | 20/47 (AsPC-1, A498, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.30×** | +4.3 | 0.001 | 23/47 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.002 | 16/46 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.003 | 16/46 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.005 | 15/46 (CFPAC-1, LS 180, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.5 | 0.020 | 12/41 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.020 | 16/47 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.046 | 10/46 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.049 | 15/47 (CFPAC-1, CHP-212, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.050 | 12/47 (AsPC-1, HCT15, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.053 | 15/46 (NCI-H2347, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9941.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.282×** | -20.8 | 0e+00 | 44/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.315×** | -18.9 | 0e+00 | 44/47 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.415×** | -14.4 | 6e-45 | 44/46 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.498×** | -11.5 | 3e-28 | 38/46 (LoVo, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.522×** | -10.7 | 2e-24 | 37/47 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.535×** | -10.3 | 9e-23 | 31/41 (LoVo, SHP-77, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.568×** | -9.3 | 1e-18 | 34/45 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.567×** | -8.6 | 5e-16 | 24/39 (NCI-H2030, SHP-77, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.604×** | -7.9 | 1e-13 | 21/37 (SW480, PANC-1, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.664×** | -6.7 | 1e-09 | 28/46 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.667×** | -6.6 | 2e-09 | 25/46 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.702×** | -5.6 | 1e-06 | 26/45 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.718×** | -5.4 | 2e-06 | 23/47 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -4.9 | 4e-05 | 20/46 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -3.9 | 0.004 | 19/47 (A498, KATO III, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.802×** | -3.5 | 0.017 | 14/47 (A498, A549, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.684×** | -3.3 | 0.034 | 18/44 (RKO, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 37.2 | 2 | 8 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0968× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.123× (z -19.8) |
| [[SW480 (line)]] | alt | 45.4 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -20.3) |
| [[LS 180 (line)]] | wt | 40.9 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.213× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 18.1 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.153× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -12.2) |
| [[SHP-77 (line)]] | alt | 40.9 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0745× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.171× (z -14.3) |
| [[A498 (line)]] | wt | 40.9 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -20.1) |
| [[KATO III (line)]] | alt | 33.2 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -17.6) |
| [[NCI-H2030 (line)]] | alt | 28.9 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.82× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0631× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.301× (z -10.7) |
| [[C-33 A (line)]] | alt | 60.6 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0965× (z -19.1) |
| [[SW1417 (line)]] | alt | 29.6 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.208× (z -13.0) |
| [[SW48 (line)]] | wt | 41.3 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -10.1) |
| [[A-427 (line)]] | wt | 32.8 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -10.0) |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0873× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 27.9 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.371× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 35.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.160× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.195× (z -8.8) |
| [[PANC-1 (line)]] | alt | 24.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -12.5) |
| [[SNU-1 (line)]] | wt | 50.0 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -10.1) |
| [[BT-474 (line)]] | alt | 40.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -10.5) |
| [[HT-29 (line)]] | alt | 18.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 25.1 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.143× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 28.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -16.2) |
| [[A-172 (line)]] | wt | 22.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -10.9) |
| [[A549 (line)]] | wt | 17.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 20.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -11.9) |
| [[RKO (line)]] | wt | 31.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.247× (z -9.1) |
| [[AN3 CA (line)]] | alt | 63.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -8.6) |
| [[C32 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 43.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -9.0) |
| [[H4 (line)]] | wt | 17.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0261× (z -15.1) |
| [[HepG2_C3A (line)]] | wt | 23.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 9.45 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 26.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.3× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRFS1]] | +0.70 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[KLHL42]] | +0.69 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[POLR3C]] | +0.68 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZNF777]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[ZNF689]] | +0.66 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[RPP38]] | +0.65 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[SLC16A14]] | +0.65 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[DICER1]] | +0.64 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[NSUN3]] | +0.63 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[MIER3]] | +0.63 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[GABPB1]] | +0.63 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[SIAH1]] | +0.62 | +0.43 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI2]] | -0.67 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[SPAG9]] | -0.63 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[F11R]] | -0.61 | -0.56 / -0.36 | both halves | 1e-04 | pathway: Signaling by TGFB family members |
| [[PCMT1]] | -0.60 | -0.53 / -0.25 | both halves | 4e-04 |  |
| [[NBEAL1]] | -0.60 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[MYADM]] | -0.60 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[OSBPL8]] | -0.59 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[PLXNA3]] | -0.58 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[SUN1]] | -0.57 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[TUBGCP2]] | -0.57 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[STXBP1]] | -0.57 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[FCHSD1]] | -0.57 | -0.50 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CGAS]] | B | CGAS activity lowers SMAD1's level | lines that do not express CGAS (17) vs lines expressing it (33) | 1.69× higher at baseline in the lines without CGAS | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[SLC16A9]] | B | SLC16A9 activity raises SMAD1's level | lines that do not express SLC16A9 (18) vs lines expressing it (32) | 1.48× lower at baseline in the lines without SLC16A9 | 0.080 | ⚠ within organs, on part of the lines; also absent: BOC, TLCD4, KIF26A; maybe low, not absent |
| [[ZBED3]] | C | ZBED3 activity raises SMAD1's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 2.50× lower at baseline in the lines without ZBED3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.482). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-6.3, 10.0); signed map (25.4, -26.7). **Vector** length 113, 29.8% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.7 | +15.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.0 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.7 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.3 | +4.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -8.5 | -20.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.0 | -18.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.5 | -14.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -3.6 | -10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | SMAD family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.21 — chr4:145,481,194-145,559,176 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MADR1, JV4-1; previously MADH1 |
| Gene groups (HGNC) | SMAD family |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 10 pathways, smallest: Cardiogenesis; RUNX2 regulates bone development; Signaling by BMP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15797](https://www.uniprot.org/uniprotkb/Q15797) (SMAD family member 1):

> Transcriptional modulator that plays a role in various cellular processes, including embryonic development, cell differentiation, and tissue homeostasis. Upon BMP ligand binding to their receptors at the cell surface, is phosphorylated by activated type I BMP receptors (BMPRIs) and associates with SMAD4 to form a heteromeric complex which translocates into the nucleus acting as transcription factor. In turn, the hetero-trimeric complex recognizes cis-regulatory elements containing Smad Binding …

**Summary**, from NCBI Gene [4086](https://www.ncbi.nlm.nih.gov/gene/4086):

> The protein encoded by this gene belongs to the SMAD, a family of proteins similar to the gene products of the Drosophila gene 'mothers against decapentaplegic' (Mad) and the C. elegans gene Sma. SMAD proteins are signal transducers and transcriptional modulators that mediate multiple signaling pathways. This protein mediates the signals of the bone morphogenetic proteins (BMPs), which are involved in a range of biological activities including cell growth, apoptosis, morphogenesis, development …

**Accessions** — [HGNC:6767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6767) · Entrez [4086](https://www.ncbi.nlm.nih.gov/gene/4086) · UniProt [Q15797](https://www.uniprot.org/uniprotkb/Q15797) · Ensembl [ENSG00000170365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170365)

## Data

Gene col 9941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9941); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9941]; `tensor/DDL_lfc|DDL_z.npy` [9941]; `embed/gene_vectors.npy` [9941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9941 or target_col == 9941). Every well: [[SMAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

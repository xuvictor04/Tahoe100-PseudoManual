---
symbol: "PYGB"
type: "gene"
col: 2055
ensembl_id: "ENSG00000100994"
name: "glycogen phosphorylase B"
location: "20p11.21"
module: 97
arm: "+"
pooled_cpm: 96.02
n_lines_expressing: 47
n_dd_up: 30
n_dd_down: 26
n_dd_up_clean: 25
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 15
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# PYGB

*glycogen phosphorylase B* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.05× (z +11.3, q 1e-26, up in 31 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.60× (z +7.6, q 5e-12, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.577× (z -9.0, q 1e-16, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENTPD6]] (+0.73, fdr 7e-06, ⚠ same locus), [[RPS6KA2]] (+0.63, fdr 7e-06), [[SH3RF3]] (+0.61, fdr 1e-05), [[ERGIC1]] (+0.60, fdr 1e-05); moves opposite to [[KMO]] (-0.62, fdr 1e-05), [[C15orf48]] (-0.57, fdr 1e-05), [[MARCKS]] (-0.56, fdr 1e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 15 go from it, the strongest it → cells under [[Idarubicin (hydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2055.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +11.3 | 1e-26 | 31/39 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +10.0 | 3e-21 | 39/46 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +7.6 | 5e-12 | 26/45 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.58×** | +7.5 | 1e-11 | 31/45 (NCI-H2347, NCI-H460, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.54×** | +7.0 | 3e-10 | 27/45 (NCI-H2347, NCI-H460, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +5.9 | 4e-07 | 24/45 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Budesonide (drug)]] 5 µM |  | **1.43×** | +5.8 | 7e-07 | 28/45 (NCI-H2347, A498, …) | all doses, flat | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.7 | 7e-07 | 25/44 (COLO 205, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +5.6 | 2e-06 | 22/45 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.41×** | +5.5 | 2e-06 | 25/45 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +5.2 | 9e-06 | 28/42 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.41×** | +5.2 | 9e-06 | 25/44 (NCI-H460, NCI-H2347, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.37×** | +5.1 | 2e-05 | 26/45 (NCI-H1573, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.37×** | +5.1 | 2e-05 | 25/45 (NCI-H2347, NCI-H1573, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.36×** | +5.0 | 2e-05 | 26/45 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **1.36×** | +5.0 | 2e-05 | 24/45 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +4.8 | 6e-05 | 25/45 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.22×** | +4.6 | 2e-04 | 21/45 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.32×** | +4.6 | 2e-04 | 22/45 (A498, NCI-H2347, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2055.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.577×** | -9.0 | 1e-16 | 34/45 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -8.4 | 2e-14 | 32/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.604×** | -8.3 | 3e-14 | 34/45 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.722×** | -7.6 | 6e-12 | 29/44 (SNU-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -7.5 | 7e-12 | 30/46 (SNU-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.775×** | -5.9 | 3e-07 | 25/45 (A-172, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.743×** | -5.8 | 6e-07 | 29/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.702×** | -5.6 | 2e-06 | 27/45 (LoVo, C32, …) | all doses, stronger at high dose | composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **0.728×** | -5.5 | 2e-06 | 27/46 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.725×** | -5.3 | 7e-06 | 28/45 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.727×** | -5.0 | 3e-05 | 26/44 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.780×** | -5.0 | 3e-05 | 22/45 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.743×** | -4.9 | 5e-05 | 26/46 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.772×** | -4.8 | 7e-05 | 23/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.748×** | -4.8 | 7e-05 | 24/45 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.751×** | -4.5 | 2e-04 | 24/45 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.616×** | -4.1 | 0.001 | 24/46 (RKO, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.765×** | -4.1 | 0.002 | 24/44 (LoVo, SW48, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 268 | 0 | 21 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.428× (z -26.8) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -17.4) |
| [[LoVo (line)]] | wt | 196 | 0 | 20 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -22.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.142× (z -20.1) |
| [[NCI-H460 (line)]] | wt | 99.9 | 10 | 10 (3 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 2.99× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -14.2) |
| [[C32 (line)]] | wt | 270 | 0 | 15 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -20.0) |
| [[NCI-H2347 (line)]] | alt | 69.3 | 15 | 0 | [[Dexamethasone (drug)]] 0.5 µM 3.64× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 51.5 | 13 | 0 | [[Dexamethasone (drug)]] 5 µM 4.13× (z +10.7) | — |
| [[A498 (line)]] | wt | 85.1 | 11 | 0 | [[Budesonide (drug)]] 5 µM 2.48× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 736 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -22.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -21.2) |
| [[A-172 (line)]] | wt | 79.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -11.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.317× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 70.3 | 5 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Dexamethasone (drug)]] 0.5 µM 2.90× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -10.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HT-29 (line)]] | alt | 227 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 139 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -12.3) |
| [[SW48 (line)]] | wt | 112 | 2 | 3 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.35× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.272× (z -8.9) |
| [[LS 180 (line)]] | wt | 134 | 1 (1 ⚠) | 3 (2 ⚠) | [[Artesunate (drug)]] 5 µM 2.00× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -9.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.371× (z -8.7) |
| [[PANC-1 (line)]] | alt | 150 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -12.8) |
| [[A549 (line)]] | wt | 59.1 | 3 (2 ⚠) | 0 | [[Dexamethasone (drug)]] 0.5 µM 2.89× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 57.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +12.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 31.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +9.3) ⚠ toxic; transcription drop | [[AZD2858 (drug)]] 0.5 µM 0.121× (z -9.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 120 | 1 | 1 | [[Dexamethasone (drug)]] 0.5 µM 2.65× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.8) |
| [[Hs 766T (line)]] | wt | 132 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +9.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -8.5) |
| [[SNU-423 (line)]] | alt | 54.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 78.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +9.5) | — |
| [[SW480 (line)]] | alt | 54.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.42× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 36.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0950× (z -8.9) |
| [[HS-578T (line)]] | alt | 92.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -9.6) |
| [[KATO III (line)]] | alt | 154 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.21× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -8.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SHP-77 (line)]] | alt | 38.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 42.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 18.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTPD6]] | +0.73 | +0.72 / +0.65 | both halves | 7e-06 | STRING 425; ⚠ same locus (20.0 kb, same strand: neighbours can correlate without regulation) |
| [[RPS6KA2]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[SH3RF3]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ERGIC1]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[NIBAN2]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ACOT7]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ITPK1]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ZDHHC3]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[COPS8]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[HPCAL1]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[SLC20A1]] | +0.55 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[TBC1D16]] | +0.55 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMO]] | -0.62 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[C15orf48]] | -0.57 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[MARCKS]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[GPR158]] | -0.55 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[DSE]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[DUSP16]] | -0.54 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[PSME2]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[MAF]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[NMB]] | -0.53 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[HLA-B]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[LINC02100]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[LINC00944]] | -0.52 | -0.46 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises PYGB's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[MAP2K1]] | B | MAP2K1 activity raises PYGB's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[MAOA]] | B | MAOA activity raises PYGB's level | lines that do not express MAOA (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without MAOA | 0.099 | ⚠ within organs, on part of the lines; also absent: OAS1, CKB; maybe low, not absent |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | C | PYGB activity raises the cells' numbers under Idarubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 0.49× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| cells under [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM | C | PYGB activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 5 µM (protects the cells) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 0.57× the cells of the other lines | 0.013 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| cells under [[Everolimus (drug)]] 5 µM | C | PYGB activity lowers the cells' numbers under Everolimus 5 µM (makes them more sensitive) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 1.32× the cells of the other lines | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | PYGB activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 0.68× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| cells under [[Erythromycin (drug)]] 5 µM | C | PYGB activity lowers the cells' numbers under Erythromycin 5 µM (makes them more sensitive) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 1.37× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 5 µM | C | PYGB activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 0.27× the cells of the other lines | 0.025 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| cells under [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM | C | PYGB activity raises the cells' numbers under Fedratinib (hydrochloride hydrate) 5 µM (protects the cells) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 0.65× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| cells under [[GSK1059615 (drug)]] 5 µM | C | PYGB activity raises the cells' numbers under GSK1059615 5 µM (protects the cells) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 0.30× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| cells under [[RMC-6236 (drug)]] 5 µM | C | PYGB activity raises the cells' numbers under RMC-6236 5 µM (protects the cells) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 0.50× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| [[PACSIN2]] | C | PYGB activity raises PACSIN2's level | lines that do not express PYGB (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without PYGB | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| cells under [[XRK3F2 (drug)]] 5 µM | C | PYGB activity raises the cells' numbers under XRK3F2 5 µM (protects the cells) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 0.65× the cells of the other lines | 0.076 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| [[ENTPD6]] | C | PYGB's natural level strengthens ENTPD6's drug response | PYGB's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.08; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.7, 10.9); signed map (13.1, 34.7). **Vector** length 150, 49.7% of its response variance represented; |z| ≥ 3 in 1,795 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dexamethasone (drug)]] 0.5 µM |  | +7.2 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +10.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +6.6 | +5.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +6.3 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +11.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +6.2 | +4.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | +5.9 | +5.1 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -9.0 | -5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.6 | -5.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -7.2 | -4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.0 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -7.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -6.4 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | glycogen phosphorylase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:25,248,085-25,298,012 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycogen phosphorylases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 5 pathways, smallest: Glycogen breakdown (glycogenolysis); Glycogen metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P11216](https://www.uniprot.org/uniprotkb/P11216) (Glycogen phosphorylase, brain form):

> Glycogen phosphorylase that regulates glycogen mobilization. Phosphorylase is an important allosteric enzyme in carbohydrate metabolism. Enzymes from different sources differ in their regulatory mechanisms and in their natural substrates. However, all known phosphorylases share catalytic and structural properties.

**Summary**, from NCBI Gene [5834](https://www.ncbi.nlm.nih.gov/gene/5834):

> The protein encoded by this gene is a glycogen phosphorylase found predominantly in the brain. The encoded protein forms homodimers which can associate into homotetramers, the enzymatically active form of glycogen phosphorylase. The activity of this enzyme is positively regulated by AMP and negatively regulated by ATP, ADP, and glucose-6-phosphate. This enzyme catalyzes the rate-determining step in glycogen degradation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9723) · Entrez [5834](https://www.ncbi.nlm.nih.gov/gene/5834) · UniProt [P11216](https://www.uniprot.org/uniprotkb/P11216) · Ensembl [ENSG00000100994](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100994)

## Data

Gene col 2055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2055); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2055]; `tensor/DDL_lfc|DDL_z.npy` [2055]; `embed/gene_vectors.npy` [2055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2055 or target_col == 2055). Every well: [[PYGB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYGB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

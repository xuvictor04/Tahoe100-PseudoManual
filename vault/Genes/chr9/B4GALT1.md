---
symbol: "B4GALT1"
type: "gene"
col: 1452
ensembl_id: "ENSG00000086062"
name: "beta-1,4-galactosyltransferase 1"
location: "9p21.1"
module: 106
arm: "+"
pooled_cpm: 108.79
n_lines_expressing: 47
n_dd_up: 23
n_dd_down: 16
n_dd_up_clean: 19
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 23
direction_downstream: 4
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# B4GALT1

*beta-1,4-galactosyltransferase 1* — 9p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Budesonide (drug)]] 0.05 µM: 1.38× (z +8.3, q 6e-14, up in 22 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.498× (z -17.9, q 0e+00, down in 37 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPD]] (+0.68, fdr 7e-06), [[PDLIM1]] (+0.67, fdr 7e-06), [[SLC16A7]] (+0.65, fdr 7e-06); moves opposite to [[TMEM158]] (-0.51, fdr 1e-04), [[LINC00973]] (-0.51, fdr 3e-05), [[MARCHF4]] (-0.51, fdr 2e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[TLR2]] → it (grade B ⚠); 4 go from it, the strongest it → [[STOM]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 0.05 µM |  | **1.38×** | +8.3 | 6e-14 | 22/45 (NCI-H2347, RPMI-7951, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +6.9 | 2e-09 | 27/45 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +6.2 | 8e-08 | 26/45 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +6.2 | 9e-08 | 23/45 (CFPAC-1, RPMI-7951, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.25×** | +5.9 | 4e-07 | 25/47 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +5.8 | 7e-07 | 23/45 (CFPAC-1, PANC-1, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +5.7 | 1e-06 | 25/46 (HepG2/C3A, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.24×** | +5.5 | 3e-06 | 23/45 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.24×** | +5.4 | 3e-06 | 21/46 (Panc 03.27, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +5.4 | 3e-06 | 17/45 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.23×** | +5.4 | 3e-06 | 23/47 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +5.3 | 6e-06 | 19/45 (LOX-IMVI, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.16× | +5.3 | 6e-06 | 17/45 (Panc 03.27, SNU-423, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.23×** | +5.2 | 7e-06 | 23/45 (A549, NCI-H2347, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.23×** | +5.1 | 1e-05 | 22/46 (NCI-H2347, PANC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +5.0 | 2e-05 | 19/45 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.22×** | +5.0 | 2e-05 | 23/45 (NCI-H2347, Panc 03.27, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +4.9 | 2e-05 | 23/44 (LOX-IMVI, HS-578T, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.21×** | +4.9 | 2e-05 | 21/46 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1452.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -17.9 | 0e+00 | 37/44 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.737×** | -11.0 | 7e-26 | 28/45 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -8.8 | 2e-16 | 34/45 (NCI-H460, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.712×** | -8.8 | 3e-16 | 29/45 (LoVo, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.726×** | -8.2 | 2e-14 | 28/45 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.717×** | -8.2 | 2e-14 | 24/44 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.733×** | -8.0 | 1e-13 | 25/45 (LoVo, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.748×** | -7.5 | 5e-12 | 25/45 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.764×** | -6.6 | 3e-09 | 26/45 (A498, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.778×** | -6.5 | 5e-09 | 25/45 (BT-474, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.778×** | -6.5 | 5e-09 | 23/45 (LoVo, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -6.4 | 9e-09 | 24/45 (A498, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.648×** | -5.8 | 2e-07 | 26/42 (A498, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.827×** | -4.5 | 2e-04 | 20/44 (C-33 A, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.853× | -4.1 | 0.002 | 21/45 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.746×** | -3.9 | 0.003 | 20/45 (NCI-H460, A549, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.748×** | -3.9 | 0.003 | 17/45 (NCI-H460, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.874× | -3.5 | 0.015 | 16/46 (J82, SNU-423, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.874× | -3.3 | 0.023 | 11/46 (A498, HepG2/C3A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.912× | -3.3 | 0.024 | 12/46 (NCI-H1573, A549, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.789×** | -3.2 | 0.033 | 15/44 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 79.3 | 8 | 1 | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 2.67× (z +12.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.463× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 179 | 2 (1 ⚠) | 6 (2 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.07× (z +12.4) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.88× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -26.5) |
| [[A549 (line)]] | wt | 259 | 2 | 4 (1 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 2.39× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -14.4) |
| [[A498 (line)]] | wt | 303 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.490× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 81.4 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 80.1 | 2 | 2 | [[Clobetasol propionate (drug)]] 0.05 µM 2.52× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -10.6) |
| [[Hs 766T (line)]] | wt | 197 | 1 | 3 (1 ⚠) | [[Budesonide (drug)]] 5 µM 2.50× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -22.3) |
| [[LoVo (line)]] | wt | 153 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -16.4) |
| [[PANC-1 (line)]] | alt | 60.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 117 | 3 | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 2.50× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -11.1) |
| [[A-172 (line)]] | wt | 120 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -15.3) |
| [[HOP62 (line)]] | alt | 102 | 3 (1 ⚠) | 0 | [[Dexamethasone (drug)]] 0.5 µM 2.26× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 53.2 | 3 (1 ⚠) | 0 | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 2.75× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 121 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 157 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 70.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 143 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -13.3) |
| [[BT-474 (line)]] | alt | 162 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 89.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.9) |
| [[HT-29 (line)]] | alt | 98.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 183 | 2 | 0 | [[Budesonide (drug)]] 5 µM 2.77× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 47.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 41.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -13.2) |
| [[H4 (line)]] | wt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 82.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.11× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.496× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.540× (z -8.6) |
| [[KATO III (line)]] | alt | 110 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.485× (z -8.8) |
| [[SW 900 (line)]] | alt | 132 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -8.5) |
| [[A-427 (line)]] | wt | 25.1 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 85.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 148 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPD]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[PDLIM1]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SLC16A7]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[IFNGR1]] | +0.64 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[STOM]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ACSL1]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[TSC22D3]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[SLC39A8]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[KLF9]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CCND3]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[SAA2]] | +0.59 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[IGFBP4]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM158]] | -0.51 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[LINC00973]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[MARCHF4]] | -0.51 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[EFL1]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MYH16]] | -0.48 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ANTXR2]] | -0.48 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[MANCR]] | -0.47 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[MSANTD3]] | -0.47 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[RABGEF1P3]] | -0.46 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[BCL2A1]] | -0.46 | -0.38 / -0.45 | both halves | 7e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[AFF3]] | -0.46 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[SLC7A11-AS1]] | -0.45 | -0.48 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 20, C 3. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLR2]] | B | TLR2 activity raises B4GALT1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.80× lower at baseline in the lines without TLR2 | 0.006 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |
| [[PDLIM1]] | B | PDLIM1 activity raises B4GALT1's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.33× lower at baseline in the lines without PDLIM1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[ALDH3B1]] | B | ALDH3B1 activity raises B4GALT1's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 2.14× lower at baseline in the lines without ALDH3B1 | 0.013 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[A4GALT]] | B | A4GALT activity raises B4GALT1's level | lines that do not express A4GALT (14) vs lines expressing it (36) | 1.65× lower at baseline in the lines without A4GALT | 0.019 | ⚠ within organs, on part of the lines; also absent: HTR1D, PAPSS2, NT5E |
| [[PAPSS2]] | B | PAPSS2 activity raises B4GALT1's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 1.65× lower at baseline in the lines without PAPSS2 | 0.025 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E |
| [[DENND3]] | B | DENND3 activity raises B4GALT1's level | lines that do not express DENND3 (7) vs lines expressing it (43) | 2.27× lower at baseline in the lines without DENND3 | 0.032 | ⚠ within organs, on part of the lines; also absent: JAG1, DUSP1, AMIGO2; maybe low, not absent |
| [[LINC00511]] | B | LINC00511 activity raises B4GALT1's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 1.86× lower at baseline in the lines without LINC00511 | 0.042 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[ANTXR2]] | B | ANTXR2 activity raises B4GALT1's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without ANTXR2 | 0.043 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[CCBE1]] | B | CCBE1 activity raises B4GALT1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without CCBE1 | 0.047 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[TSC22D3]] | B | TSC22D3 activity raises B4GALT1's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 1.92× lower at baseline in the lines without TSC22D3 | 0.048 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[SLPI]] | B | SLPI activity raises B4GALT1's level | lines that do not express SLPI (25) vs lines expressing it (25) | 1.80× lower at baseline in the lines without SLPI | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[NR3C1]] | B | NR3C1 activity raises B4GALT1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STOM]] | C | B4GALT1 activity raises STOM's level | lines that do not express B4GALT1 (3) vs lines expressing it (47) | 4.12× lower at baseline in the lines without B4GALT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TIMP1, UGDH, ATXN1; maybe low, not absent; its own permutation p |
| [[JAK1]] | C | B4GALT1 activity raises JAK1's level | lines that do not express B4GALT1 (3) vs lines expressing it (47) | 1.49× lower at baseline in the lines without B4GALT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TIMP1, UGDH, ATXN1; maybe low, not absent; its own permutation p |
| [[PACSIN2]] | C | B4GALT1 activity raises PACSIN2's level | lines that do not express B4GALT1 (3) vs lines expressing it (47) | 1.63× lower at baseline in the lines without B4GALT1 | 0.099 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TIMP1, UGDH, ATXN1; maybe low, not absent |
| cells under [[Naproxen (drug)]] 5 µM | C | B4GALT1's natural level raises the cells' numbers under Naproxen 5 µM (protects the cells) | B4GALT1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.339 over the table, 0.086 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.3, 18.4); signed map (18.4, 28.6). **Vector** length 143, 46.1% of its response variance represented; |z| ≥ 3 in 1,642 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +6.6 | +6.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +6.1 | +8.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +6.1 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +4.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.9 | +5.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -17.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.5 | -8.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -8.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.8 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -4.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,4-galactosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.1 — chr9:33,104,082-33,167,356 (-) |
| Ensembl biotype | protein_coding |
| Also known as | beta4Gal-T1; previously GGTB2 |
| Gene groups (HGNC) | Beta 4-glycosyltransferases |
| Hallmark sets | APICAL_SURFACE, ANDROGEN_RESPONSE, APICAL_JUNCTION, GLYCOLYSIS, ESTROGEN_RESPONSE_EARLY, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 20 pathways, smallest: Interaction With Cumulus Cells And The Zona Pellucida; Fertilization; N-Glycan antennae elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [P15291](https://www.uniprot.org/uniprotkb/P15291) (Beta-1,4-galactosyltransferase 1):

> Galactosyltransferase acting in the Golgi stacks. Catalyzes the transfer of galactose (Gal) from UDP-alpha-D-galactose in beta(1->4) linkage to the non-reducing terminal N-acetylglucosamine (GlcNAc) moieties of glycolipids and complex-type N-linked glycans. Adds one Gal residue to both GlcNAc beta(1->2)-linked to the alpha(1->3) and alpha(1->6) mannose antennae of complex-type N-glycans, enabling the formation of mono- and di-galactosylated glycoforms. Galactosylates complex-type N-glycans …

**Summary**, from NCBI Gene [2683](https://www.ncbi.nlm.nih.gov/gene/2683):

> This gene is one of seven beta-1,4-galactosyltransferase (beta4GalT) genes. They encode type II membrane-bound glycoproteins that appear to have exclusive specificity for the donor substrate UDP-galactose; all transfer galactose in a beta1,4 linkage to similar acceptor sugars: GlcNAc, Glc, and Xyl. Each beta4GalT has a distinct function in the biosynthesis of different glycoconjugates and saccharide structures. As type II membrane proteins, they have an N-terminal hydrophobic signal sequence …

**Accessions** — [HGNC:924](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:924) · Entrez [2683](https://www.ncbi.nlm.nih.gov/gene/2683) · UniProt [P15291](https://www.uniprot.org/uniprotkb/P15291) · Ensembl [ENSG00000086062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086062)

## Data

Gene col 1452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1452); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1452]; `tensor/DDL_lfc|DDL_z.npy` [1452]; `embed/gene_vectors.npy` [1452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1452 or target_col == 1452). Every well: [[B4GALT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B4GALT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

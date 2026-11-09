---
symbol: "CLOCK"
type: "gene"
col: 5613
ensembl_id: "ENSG00000134852"
name: "clock circadian regulator"
location: "4q12"
module: 194
arm: "+"
pooled_cpm: 123.93
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# CLOCK

*clock circadian regulator* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +15.4, q 0e+00, up in 34 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (MIA PaCa-2 3.53×, NCI-H460 2.11×, HT-29 2.42×, RPMI-7951 2.91×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (A498 2.73×, PANC-1 2.06×, NCI-H460 2.02×, NCI-H2347 2.14×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 2.27×, A498 2.33×; ⚠ cell-cycle shift, explains ~16% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.414× (z -25.6, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPSF2]] (+0.62, fdr 1e-05), [[HIVEP1]] (+0.61, fdr 1e-05), [[GALNT7-DT]] (+0.61, fdr 1e-04); moves opposite to [[FCHSD1]] (-0.62, fdr 3e-05), [[DPY30]] (-0.62, fdr 3e-05), [[MKRN2]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CAMK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5613.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (MIA PaCa-2 3.53×, NCI-H460 2.11×, HT-29 2.42×, RPMI-7951 2.91×, …); [[Homoharringtonine (drug)]] 5 µM in 5 lines (A498 2.73×, PANC-1 2.06×, NCI-H460 2.02×, NCI-H2347 2.14×, …; ⚠ cell-cycle shift, explains ~30% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 2.27×, A498 2.33×; ⚠ cell-cycle shift, explains ~16% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +15.4 | 0e+00 | 34/49 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +9.3 | 3e-18 | 32/48 (SNU-423, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.18× | +6.8 | 1e-09 | 24/48 (A498, PANC-1, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.26×** | +6.5 | 1e-08 | 27/48 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | 1.15× | +3.9 | 0.011 | 15/49 (J82, SHP-77, …) | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | 1.24× | +3.2 | 0.11 | 12/48 (LOX-IMVI, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.0 | 0.21 | 12/49 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5613.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.414×** | -25.6 | 0e+00 | 46/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.421×** | -25.2 | 0e+00 | 46/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.489×** | -20.8 | 0e+00 | 47/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.750×** | -11.8 | 5e-30 | 32/48 (LS 180, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.713×** | -9.9 | 7e-21 | 37/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.758×** | -8.0 | 8e-14 | 36/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.739×** | -6.3 | 3e-08 | 23/45 (LoVo, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.811×** | -6.1 | 9e-08 | 28/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.824×** | -5.6 | 1e-06 | 23/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.835× | -5.2 | 1e-05 | 24/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.787×** | -5.0 | 3e-05 | 24/48 (LoVo, LS 180, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.819×** | -4.6 | 2e-04 | 21/48 (LoVo, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.865× | -4.2 | 0.001 | 18/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.762×** | -4.1 | 0.001 | 18/49 (LS 180, LoVo, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | 0.866× | -4.0 | 0.002 | 19/47 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.832×** | -3.8 | 0.004 | 14/47 (CHP-212, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.833×** | -3.8 | 0.005 | 19/48 (HCT15, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.881× | -3.7 | 0.006 | 10/48 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.793×** | -3.5 | 0.011 | 20/49 (LOX-IMVI, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.793×** | -3.5 | 0.011 | 15/47 (RKO, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 350 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -24.7) |
| [[PANC-1 (line)]] | alt | 132 | 2 (2 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +19.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Panobinostat (drug)]] 5 µM 0.321× (z -21.9) |
| [[A-427 (line)]] | wt | 151 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.303× (z -19.2) |
| [[LS 180 (line)]] | wt | 310 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.155× (z -20.5) |
| [[NCI-H1573 (line)]] | alt | 171 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -15.9) |
| [[SHP-77 (line)]] | alt | 155 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.410× (z -12.8) |
| [[A498 (line)]] | wt | 96.3 | 4 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +23.5) ⚠ cell-cycle shift, explains ~30% of this change | [[Panobinostat (drug)]] 5 µM 0.496× (z -11.5) |
| [[C32 (line)]] | wt | 143 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 78.1 | 3 (2 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +23.2) | [[Panobinostat (drug)]] 0.5 µM 0.293× (z -16.1) |
| [[NCI-H23 (line)]] | alt | 246 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.403× (z -16.8) |
| [[SK-MEL-2 (line)]] | alt | 110 | 2 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +9.3) | [[Belinostat (drug)]] 5 µM 0.351× (z -14.1) |
| [[A549 (line)]] | wt | 67.5 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +16.4) ⚠ cell-cycle shift, explains ~30% of this change | [[Panobinostat (drug)]] 5 µM 0.334× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 84.2 | 2 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.415× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 107 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +17.5) ⚠ cell-cycle shift, explains ~30% of this change | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 84.8 | 2 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +19.3) | [[Panobinostat (drug)]] 5 µM 0.414× (z -16.0) |
| [[HOP62 (line)]] | alt | 124 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.418× (z -11.8) |
| [[Hs 766T (line)]] | wt | 91.8 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.392× (z -11.3) |
| [[HT-29 (line)]] | alt | 88.1 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +16.3) | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -10.8) |
| [[J82 (line)]] | alt | 84.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.421× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 91.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -14.5) |
| [[NCI-H2030 (line)]] | alt | 87.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.335× (z -14.6) |
| [[RKO (line)]] | wt | 114 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -13.8) |
| [[SNU-423 (line)]] | alt | 88.6 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +12.3) | [[Selinexor (drug)]] 5 µM 0.568× (z -10.2) |
| [[SW48 (line)]] | wt | 165 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.275× (z -13.2) |
| [[SW480 (line)]] | alt | 97.8 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.420× (z -14.6) |
| [[BT-474 (line)]] | alt | 115 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -13.2) |
| [[C-33 A (line)]] | alt | 175 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 122 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 84.9 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.403× (z -10.4) |
| [[SNU-1 (line)]] | wt | 138 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.361× (z -10.3) |
| [[SW 900 (line)]] | alt | 196 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -10.8) |
| [[SW1417 (line)]] | alt | 117 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -13.6) |
| [[A-172 (line)]] | wt | 87.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 73.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +12.7) | — |
| [[HS-578T (line)]] | alt | 98.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.462× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 106 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.416× (z -9.0) |
| [[KATO III (line)]] | alt | 64.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 170 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.333× (z -8.9) |
| [[H4 (line)]] | wt | 137 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.379× (z -9.0) |
| [[HCT15 (line)]] | alt | 217 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.409× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 79.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +15.6) | — |
| [[AN3 CA (line)]] | alt | 121 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF2]] | +0.62 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[HIVEP1]] | +0.61 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[GALNT7-DT]] | +0.61 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[MED13]] | +0.59 | +0.37 / +0.51 | both halves | 7e-05 | pathway: PPARA activates gene expression |
| [[MYLK-AS1]] | +0.59 | +0.44 / +0.22 | both halves | 6e-04 |  |
| [[LINC01135]] | +0.58 | +0.36 / +0.42 | both halves | 9e-05 |  |
| [[USP13]] | +0.58 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[ICA1L]] | +0.58 | +0.41 / +0.29 | both halves | 3e-04 |  |
| [[TENM3-AS1]] | +0.57 | +0.36 / +0.40 | both halves | 1e-04 |  |
| [[DGKH]] | +0.57 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[ZBED5]] | +0.56 | +0.34 / +0.41 | both halves | 1e-04 |  |
| [[TAOK1]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHSD1]] | -0.62 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[DPY30]] | -0.62 | -0.43 / -0.52 | both halves | 3e-05 | pathway: Chromatin modifying enzymes |
| [[MKRN2]] | -0.61 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[SLC27A1]] | -0.61 | -0.48 / -0.36 | both halves | 1e-04 | pathway: PPARA activates gene expression |
| [[TBC1D13]] | -0.60 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[ESS2]] | -0.59 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[PHKA2]] | -0.58 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[HDAC11]] | -0.58 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[MAST3]] | -0.58 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[PIGH]] | -0.58 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[UNC45A]] | -0.57 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[OSBPL7]] | -0.57 | -0.36 / -0.47 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMK1]] | B | CAMK1 activity lowers CLOCK's level | lines that do not express CAMK1 (8) vs lines expressing it (42) | 1.44× higher at baseline in the lines without CAMK1 | 0.059 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-0.2, -5.3); signed map (16.3, -7.8). **Vector** length 120, 33.1% of its response variance represented; |z| ≥ 3 in 1,246 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.5 | +15.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +8.7 | +2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +8.1 | +6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.9 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.0 | +9.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.4 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.9 | -11.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.4 | -25.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.4 | -25.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.0 | -20.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -5.2 | -5.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -4.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.8 | -5.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.3 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | clock circadian regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:55,427,903-55,546,909 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0334, KAT13D, bHLHe8 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; Lysine acetyltransferases; PAS domain containing |
| Reactome | 18 pathways, smallest: Phosphorylation and nuclear translocation of BMAL1 (ARNTL) and CLOCK; Phosphorylation of CLOCK, acetylation of BMAL1 (ARNTL) at target gene promoters; The CRY:PER:kinase complex represses transactivation by the BMAL:CLOCK (ARNTL:CLOCK) complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O15516](https://www.uniprot.org/uniprotkb/O15516) (Circadian locomoter output cycles protein kaput):

> Transcriptional activator which forms a core component of the circadian clock. The circadian clock, an internal time-keeping system, regulates various physiological processes through the generation of approximately 24 hour circadian rhythms in gene expression, which are translated into rhythms in metabolism and behavior. It is derived from the Latin roots 'circa' (about) and 'diem' (day) and acts as an important regulator of a wide array of physiological functions including metabolism, sleep, …

**Summary**, from NCBI Gene [9575](https://www.ncbi.nlm.nih.gov/gene/9575):

> The protein encoded by this gene plays a central role in the regulation of circadian rhythms. The protein encodes a transcription factor of the basic helix-loop-helix (bHLH) family and contains DNA binding histone acetyltransferase activity. The encoded protein forms a heterodimer with ARNTL (BMAL1) that binds E-box enhancer elements upstream of Period (PER1, PER2, PER3) and Cryptochrome (CRY1, CRY2) genes and activates transcription of these genes. PER and CRY proteins heterodimerize and …

**Accessions** — [HGNC:2082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2082) · Entrez [9575](https://www.ncbi.nlm.nih.gov/gene/9575) · UniProt [O15516](https://www.uniprot.org/uniprotkb/O15516) · Ensembl [ENSG00000134852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134852)

## Data

Gene col 5613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5613); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5613]; `tensor/DDL_lfc|DDL_z.npy` [5613]; `embed/gene_vectors.npy` [5613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5613 or target_col == 5613). Every well: [[CLOCK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLOCK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

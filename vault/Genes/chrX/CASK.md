---
symbol: "CASK"
type: "gene"
col: 7142
ensembl_id: "ENSG00000147044"
name: "calcium/calmodulin dependent serine protein kinase"
location: "Xp11.4"
module: 1
arm: "-"
pooled_cpm: 187.44
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CASK

*calcium/calmodulin dependent serine protein kinase* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.19× (z +7.3, q 2e-10, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.625× (z -13.3, q 1e-37, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LARGE1]] (+0.50, fdr 2e-05), [[MAGI3]] (+0.48, fdr 1e-04), [[DLG1]] (+0.48, fdr 3e-05); moves opposite to [[DPH1]] (-0.45, fdr 4e-05), [[TUT1]] (-0.44, fdr 5e-05), [[TAF1A]] (-0.44, fdr 4e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KITLG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7142.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +7.3 | 2e-10 | 25/47 (BT-474, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +5.8 | 2e-06 | 25/46 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.20×** | +5.4 | 2e-05 | 21/46 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.16× | +4.3 | 0.002 | 16/46 (J82, HS-578T, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +4.2 | 0.003 | 15/46 (NCI-H1573, SW480, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | 1.15× | +4.0 | 0.005 | 16/48 (LS 180, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.16× | +4.0 | 0.005 | 17/47 (LS 180, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.11× | +4.0 | 0.005 | 11/47 (LS 180, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.15× | +3.9 | 0.005 | 16/49 (LS 180, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.14× | +3.8 | 0.008 | 14/48 (SW480, BT-474, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.10× | +3.7 | 0.010 | 7/47 (LS 180, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.11× | +3.7 | 0.011 | 10/47 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.016 | 12/47 (LoVo, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.13× | +3.5 | 0.017 | 12/48 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.029 | 14/47 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.088 | 8/47 (CFPAC-1, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7142.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.625×** | -13.3 | 1e-37 | 38/47 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.719×** | -13.3 | 1e-37 | 31/47 (A-172, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.644×** | -12.9 | 6e-36 | 35/47 (A-172, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.652×** | -12.1 | 2e-31 | 39/46 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.693×** | -10.8 | 6e-25 | 39/47 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.713×** | -9.9 | 3e-21 | 32/47 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.762×** | -8.0 | 1e-13 | 27/47 (J82, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.766×** | -7.8 | 3e-13 | 31/47 (KATO III, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.776×** | -7.4 | 7e-12 | 28/47 (LS 180, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.788×** | -7.0 | 1e-10 | 27/47 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.792×** | -6.8 | 4e-10 | 27/47 (HOP62, Panc 03.27, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.802×** | -6.5 | 4e-09 | 25/47 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.806×** | -6.3 | 1e-08 | 26/47 (RPMI-7951, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.702×** | -5.4 | 2e-06 | 24/48 (NCI-H23, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.834× | -5.3 | 4e-06 | 21/47 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.880× | -3.5 | 0.014 | 16/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.923× | -3.3 | 0.027 | 8/48 (NCI-H1573, A549, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.899× | -3.1 | 0.039 | 7/47 (NCI-H1573, C-33 A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.893× | -3.1 | 0.042 | 9/46 (NCI-H2030, J82, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.906× | -2.9 | 0.069 | 7/47 (SHP-77, Hs 766T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.930× | -2.9 | 0.069 | 9/47 (HOP62, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 545 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -18.9) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.357× (z -12.2) |
| [[HOP62 (line)]] | alt | 236 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -19.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.265× (z -14.4) |
| [[A549 (line)]] | wt | 275 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -14.3) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.477× (z -10.4) |
| [[J82 (line)]] | alt | 261 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -18.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.312× (z -13.6) |
| [[KATO III (line)]] | alt | 446 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -14.7) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.520× (z -11.6) |
| [[A-172 (line)]] | wt | 182 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -25.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.389× (z -16.5) |
| [[HS-578T (line)]] | alt | 247 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -17.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -14.3) |
| [[LS 180 (line)]] | wt | 414 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -14.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.581× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 174 | 4 (4 ⚠) | 2 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +17.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 0.05 µM 0.582× (z -9.2) |
| [[SNU-423 (line)]] | alt | 396 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -19.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.247× (z -15.0) |
| [[A-427 (line)]] | wt | 179 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -19.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.488× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 301 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -15.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.416× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 232 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.295× (z -14.2) |
| [[C-33 A (line)]] | alt | 410 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -11.9) ⚠ cell-cycle shift, explains ~84% of this change |
| [[HEC-1-A (line)]] | alt | 149 | 1 (1 ⚠) | 3 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.63× (z +9.5) ⚠ unreliable plate only | [[Panobinostat (drug)]] 0.5 µM 0.643× (z -8.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 140 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.501× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.525× (z -9.9) |
| [[PANC-1 (line)]] | alt | 105 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -14.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.540× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 88.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.09× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -11.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 180 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.434× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 187 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -12.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.534× (z -8.5) |
| [[Hs 766T (line)]] | wt | 216 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.416× (z -11.0) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0988× (z -15.7) |
| [[C32 (line)]] | wt | 128 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.466× (z -10.2) |
| [[COLO 205 (line)]] | alt | 241 | 1 | 0 | [[Peretinoin (drug)]] 5 µM 2.09× (z +8.9) | — |
| [[H4 (line)]] | wt | 173 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.410× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[hTERT-HPNE (line)]] | wt | 131 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.410× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.338× (z -13.4) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.545× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[RKO (line)]] | wt | 81.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.0) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[SHP-77 (line)]] | alt | 135 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.473× (z -10.8) |
| [[A498 (line)]] | wt | 40.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 154 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 237 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 173 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7142), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARGE1]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[MAGI3]] | +0.48 | +0.59 / +0.36 | both halves | 1e-04 | same gene group; STRING 401 |
| [[DLG1]] | +0.48 | +0.47 / +0.45 | both halves | 3e-05 | same gene group; pathway: Activation of NMDA receptors and postsynaptic events; STRING 980 |
| [[PDE5A]] | +0.48 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[COP1]] | +0.46 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[STK3]] | +0.46 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[GNAQ]] | +0.45 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[PCSK5]] | +0.45 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[SNTB2]] | +0.45 | +0.46 / +0.45 | both halves | 3e-05 | same gene group; pathway: Extracellular matrix organization; STRING 471 |
| [[CEP85L]] | +0.44 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[VOPP1]] | +0.43 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[NECTIN3]] | +0.43 | +0.51 / +0.37 | both halves | 8e-05 | pathway: Cell-Cell communication |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH1]] | -0.45 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[TUT1]] | -0.44 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[TAF1A]] | -0.44 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZNF283]] | -0.43 | -0.29 / -0.45 | both halves | 3e-04 |  |
| [[UTP25]] | -0.43 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[ZNF23]] | -0.42 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[ZNF408]] | -0.42 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[PYM1]] | -0.41 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[EXOSC7]] | -0.41 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[ZSCAN12]] | -0.41 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[SEPSECS]] | -0.40 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[ZNF225]] | -0.40 | -0.31 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KITLG]] | B | KITLG activity raises CASK's level | lines that do not express KITLG (10) vs lines expressing it (40) | 1.40× lower at baseline in the lines without KITLG | 0.093 | ⚠ within organs, on part of the lines; also absent: ETS2, CDA, LMO7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.288). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-52.4, 9.5); signed map (-16.2, 29.7). **Vector** length 98.4, 26.5% of its response variance represented; |z| ≥ 3 in 1,468 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | -0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +2.8 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +2.8 | +3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +4.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.3 | -12.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -10.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | -4.6 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.7 | -3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | calcium/calmodulin dependent serine protein kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:41,514,934-41,923,554 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LIN2, CAGH39, FGS4; previously TNRC8 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing; CASK family; SH3 domain containing |
| Reactome | 18 pathways, smallest: Nephrin family interactions; Dopamine Neurotransmitter Release Cycle; Syndecan interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [O14936](https://www.uniprot.org/uniprotkb/O14936) (Peripheral plasma membrane protein CASK):

> Multidomain scaffolding Mg(2+)-independent protein kinase that catalyzes the phosphotransfer from ATP to proteins such as NRXN1, and plays a role in synaptic transmembrane protein anchoring and ion channel trafficking. Contributes to neural development and regulation of gene expression via interaction with the transcription factor TBR1. Binds to cell-surface proteins, including amyloid precursor protein, neurexins and syndecans. May mediate a link between the extracellular matrix and the actin …

**Summary**, from NCBI Gene [8573](https://www.ncbi.nlm.nih.gov/gene/8573):

> This gene encodes a calcium/calmodulin-dependent serine protein kinase. The encoded protein is a MAGUK (membrane-associated guanylate kinase) protein family member. These proteins are scaffold proteins and the encoded protein is located at synapses in the brain. Mutations in this gene are associated with FG syndrome 4, intellectual disability and microcephaly with pontine and cerebellar hypoplasia, and a form of X-linked intellectual disability. Multiple transcript variants encoding different …

**Accessions** — [HGNC:1497](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1497) · Entrez [8573](https://www.ncbi.nlm.nih.gov/gene/8573) · UniProt [O14936](https://www.uniprot.org/uniprotkb/O14936) · Ensembl [ENSG00000147044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147044)

## Data

Gene col 7142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7142); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7142, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7142]; `tensor/DDL_lfc|DDL_z.npy` [7142]; `embed/gene_vectors.npy` [7142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7142 or target_col == 7142). Every well: [[CASK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

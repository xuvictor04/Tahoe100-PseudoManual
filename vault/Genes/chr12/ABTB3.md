---
symbol: "ABTB3"
type: "gene"
col: 7489
ensembl_id: "ENSG00000151136"
name: "ankyrin repeat and BTB domain containing 3"
location: "12q23.3"
module: 84
arm: "+"
pooled_cpm: 69.1
n_lines_expressing: 27
n_dd_up: 24
n_dd_down: 40
n_dd_up_clean: 18
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 5
direction_downstream: 19
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# ABTB3

*ankyrin repeat and BTB domain containing 3* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.87× (z +23.6, q 0e+00, up in 23 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.561× (z -14.3, q 2e-43, down in 20 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[S100A16]] (+0.71, fdr 1e-05), [[MMP1]] (+0.71, fdr 7e-06), [[FXYD5]] (+0.71, fdr 1e-05); moves opposite to [[HDGF]] (-0.61, fdr 3e-05), [[MR1]] (-0.60, fdr 1e-04), [[NEXN]] (-0.60, fdr 1e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[BCAR3]] → it (grade B ⚠); 19 go from it, the strongest it → [[ITGA5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7489.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.87×** | +23.6 | 0e+00 | 23/25 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.49×** | +21.8 | 0e+00 | 23/25 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.07×** | +19.6 | 0e+00 | 22/25 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +17.8 | 0e+00 | 16/25 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.50×** | +16.0 | 0e+00 | 19/25 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.63×** | +12.1 | 1e-31 | 6/26 (LoVo, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.65×** | +8.8 | 1e-16 | 16/25 (A498, COLO 205, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.49×** | +6.9 | 3e-10 | 16/25 (A498, SW48, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +6.7 | 1e-09 | 7/26 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +6.5 | 4e-09 | 13/25 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +5.3 | 6e-06 | 12/25 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +4.8 | 6e-05 | 8/23 (Panc 03.27, BT-474, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +4.6 | 2e-04 | 10/25 (COLO 205, H4, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.28×** | +4.4 | 5e-04 | 10/25 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.28×** | +4.2 | 0.001 | 5/25 (LoVo, H4, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +4.1 | 0.001 | 6/26 (LoVo, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.003 | 11/24 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.82×** | +3.9 | 0.003 | 12/25 (RKO, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.005 | 8/26 (LoVo, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.009 | 12/25 (J82, A-172, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7489.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.561×** | -14.3 | 2e-43 | 20/25 (A549, SNU-423, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.514×** | -11.6 | 1e-28 | 20/25 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.570×** | -9.4 | 8e-19 | 17/25 (A549, SW48, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.641×** | -9.2 | 5e-18 | 20/25 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.567×** | -8.6 | 1e-15 | 21/26 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.605×** | -8.4 | 4e-15 | 18/25 (AsPC-1, A-172, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.624×** | -8.2 | 2e-14 | 21/25 (SW1417, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.684×** | -7.9 | 2e-13 | 18/25 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.736×** | -7.5 | 3e-12 | 17/25 (CFPAC-1, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.650×** | -7.5 | 3e-12 | 19/26 (A-172, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.630×** | -7.5 | 5e-12 | 17/25 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.661×** | -6.8 | 5e-10 | 17/25 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.714×** | -6.5 | 4e-09 | 18/26 (A-172, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.768×** | -6.4 | 6e-09 | 16/26 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.689×** | -6.2 | 2e-08 | 18/24 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.707×** | -6.0 | 5e-08 | 13/24 (NCI-H1573, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.792×** | -5.7 | 5e-07 | 10/25 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 313 | 2 | 14 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.65× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.0440× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.4) |
| [[A-172 (line)]] | wt | 139 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -24.4) |
| [[LoVo (line)]] | wt | 25.2 | 8 (3 ⚠) | 3 | [[Panobinostat (drug)]] 5 µM 7.63× (z +15.4) | [[Harringtonine (drug)]] 5 µM 0.256× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 52.8 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -12.5) |
| [[SNU-423 (line)]] | alt | 238 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0733× (z -27.5) |
| [[RKO (line)]] | wt | 71.3 | 4 | 5 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.50× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.210× (z -10.4) |
| [[SW1417 (line)]] | alt | 138 | 5 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 4.44× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -23.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 363 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0437× (z -34.8) |
| [[HOP62 (line)]] | alt | 87.4 | 0 | 8 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.558× (z -12.9) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.243× (z -12.5) |
| [[A498 (line)]] | wt | 314 | 2 (1 ⚠) | 5 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.71× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.387× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 142 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.320× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 414 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -18.3) |
| [[SW48 (line)]] | wt | 157 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -16.6) |
| [[SW480 (line)]] | alt | 46.5 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.75× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 19.0 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 14.2× (z +9.2) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0475× (z -10.6) |
| [[HCT15 (line)]] | alt | 23.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.82× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 121 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.5) |
| [[COLO 205 (line)]] | alt | 22.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.46× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 46.8 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.87× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.6) |
| [[HS-578T (line)]] | alt | 23.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.4) |
| [[J82 (line)]] | alt | 50.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 46.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 18.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.23× (z +9.1) | — |
| [[A-427 (line)]] | wt | 4.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.95 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.48 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.11 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.39 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.22 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.33 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.43 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.06 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[S100A16]] | +0.71 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[MMP1]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[FXYD5]] | +0.71 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[WDFY2]] | +0.71 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[HPCAL1]] | +0.70 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[KIF21B]] | +0.70 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[THBD]] | +0.69 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[PPARD]] | +0.69 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[RAC2]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.68 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[MYO9B]] | +0.68 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDGF]] | -0.61 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[MR1]] | -0.60 | -0.61 / -0.32 | both halves | 1e-04 |  |
| [[NEXN]] | -0.60 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[STAT5A]] | -0.59 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[TAPBPL]] | -0.58 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[RARRES1]] | -0.57 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[PAXIP1-AS2]] | -0.56 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[CILK1]] | -0.56 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[AJUBA]] | -0.56 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[SLC39A1]] | -0.56 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[C1orf43]] | -0.56 | -0.52 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAR3]] | B | BCAR3 activity raises ABTB3's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 3.46× lower at baseline in the lines without BCAR3 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[PLEK2]] | B | PLEK2 activity raises ABTB3's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.76× lower at baseline in the lines without PLEK2 | 0.090 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[STC1]] | B | STC1 activity raises ABTB3's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.32× lower at baseline in the lines without STC1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[CDYL2]] | C | CDYL2 activity raises ABTB3's level | lines that do not express CDYL2 (19) vs lines expressing it (31) | 3.03× lower at baseline in the lines without CDYL2 | 0.055 | ⚠ within organs, on part of the lines; also absent: B3GALT5, BCL11B, ENSG00000225330; co-absent with the target |
| [[CREG2]] | C | CREG2 activity raises ABTB3's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 1.94× lower at baseline in the lines without CREG2 | 0.083 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 17, C 2. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA5]] | B | ABTB3 activity raises ITGA5's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 2.79× lower at baseline in the lines without ABTB3 | 0.014 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[S100A16]] | B | ABTB3 activity raises S100A16's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 2.68× lower at baseline in the lines without ABTB3 | 0.035 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[CDCP1]] | B | ABTB3 activity raises CDCP1's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without ABTB3 | 0.041 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[PTPRE]] | B | ABTB3 activity raises PTPRE's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 2.24× lower at baseline in the lines without ABTB3 | 0.044 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[BACE2]] | B | ABTB3 activity raises BACE2's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 2.32× lower at baseline in the lines without ABTB3 | 0.050 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[TGFA]] | B | ABTB3 activity raises TGFA's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 2.43× lower at baseline in the lines without ABTB3 | 0.060 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[CELSR1]] | B | ABTB3 activity raises CELSR1's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 1.58× lower at baseline in the lines without ABTB3 | 0.062 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[SHB]] | B | ABTB3 activity raises SHB's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 2.05× lower at baseline in the lines without ABTB3 | 0.063 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[PI4K2A]] | B | ABTB3 activity raises PI4K2A's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 1.23× lower at baseline in the lines without ABTB3 | 0.065 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[THBD]] | B | ABTB3 activity raises THBD's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without ABTB3 | 0.068 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[MAP4K4]] | B | ABTB3 activity raises MAP4K4's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without ABTB3 | 0.069 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |
| [[SLC25A51]] | B | ABTB3 activity raises SLC25A51's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without ABTB3 | 0.079 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.0, 3.2); signed map (2.3, 48.7). **Vector** length 115, 33.5% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.9 | +19.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +23.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +21.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +17.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +16.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +8.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.0 | +2.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.8 | -7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.4 | -14.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -11.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.3 | -7.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.7 | -9.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.7 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.6 | -8.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.6 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and BTB domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:107,318,421-107,659,642 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33957, ABTB2B; previously BTBD11 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A6QL63](https://www.uniprot.org/uniprotkb/A6QL63) (Ankyrin repeat- and BTB/POZ domain-containing protein 3):

> Cortical and hippocampal inhibitory interneuron-specific protein localized at glutamatergic (excitatory) synapses, where it supports cell type-specific synaptic function.

**Summary**, from NCBI Gene [121551](https://www.ncbi.nlm.nih.gov/gene/121551):

> Predicted to enable PDZ domain binding activity and protein heterodimerization activity. Predicted to act upstream of or within exploration behavior; glutamatergic synaptic transmission; and protein stabilization. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23844) · Entrez [121551](https://www.ncbi.nlm.nih.gov/gene/121551) · UniProt [A6QL63](https://www.uniprot.org/uniprotkb/A6QL63) · Ensembl [ENSG00000151136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151136)

## Data

Gene col 7489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7489); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7489]; `tensor/DDL_lfc|DDL_z.npy` [7489]; `embed/gene_vectors.npy` [7489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7489 or target_col == 7489). Every well: [[ABTB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABTB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

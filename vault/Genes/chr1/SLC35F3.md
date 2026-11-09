---
symbol: "SLC35F3"
type: "gene"
col: 11456
ensembl_id: "ENSG00000183780"
name: "solute carrier family 35 member F3"
location: "1q42.2"
module: 193
arm: "+"
pooled_cpm: 165.98
n_lines_expressing: 23
n_dd_up: 15
n_dd_down: 26
n_dd_up_clean: 11
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 11
direction_downstream: 8
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# SLC35F3

*solute carrier family 35 member F3* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.98× (z +11.5, q 9e-28, up in 12 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.617× (z -7.8, q 3e-12, down in 17 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCHF4]] (+0.68, fdr 7e-06), [[BMP6]] (+0.64, fdr 1e-05), [[CDH4]] (+0.64, fdr 7e-06).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CDCP1]] → it (grade B ⚠); 8 go from it, the strongest it → [[GPR39]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +11.5 | 9e-28 | 12/21 (RPMI-7951, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +10.7 | 2e-24 | 11/21 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +8.3 | 2e-14 | 1/22 (A-427) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +6.9 | 1e-09 | 1/20 (A-427) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +6.2 | 6e-08 | 1/20 (RPMI-7951) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +6.2 | 7e-08 | 8/22 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.5 | 3e-06 | 1/22 (RPMI-7951) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +5.1 | 3e-05 | 17/21 (SW 900, NCI-H1573, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.47×** | +4.6 | 3e-04 | 10/21 (SW 900, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +4.4 | 7e-04 | 18/21 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.2 | 0.001 | 10/22 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.001 | 12/21 (SW 900, NCI-H1573, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.009 | 1/21 (RPMI-7951) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.027 | 9/20 (SW 900, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.027 | 0/22 | rises with dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.064 | 0/22 | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.083 | 3/21 (Panc 03.27, SNU-423, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.085 | 3/21 (A549, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.19× | +2.9 | 0.096 | 13/21 (SW 900, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11456.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.617×** | -7.8 | 3e-12 | 17/21 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.672×** | -6.2 | 2e-07 | 10/21 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.716×** | -5.6 | 2e-06 | 11/21 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.736×** | -5.6 | 2e-06 | 12/23 (NCI-H596, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.717×** | -5.6 | 2e-06 | 12/21 (Hs 766T, A498, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.795×** | -5.4 | 7e-06 | 8/21 (CFPAC-1, HEC-1-A, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.732×** | -5.3 | 1e-05 | 12/21 (A549, AsPC-1, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.736×** | -5.2 | 2e-05 | 6/21 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.732×** | -5.1 | 3e-05 | 17/21 (Hs 766T, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.756×** | -4.7 | 1e-04 | 16/21 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.774×** | -4.6 | 2e-04 | 16/22 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.754×** | -4.4 | 5e-04 | 9/21 (A498, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.817×** | -4.3 | 7e-04 | 13/21 (CFPAC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.839× | -4.2 | 0.001 | 10/21 (Hs 766T, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.783×** | -4.1 | 0.001 | 15/22 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.827×** | -3.8 | 0.005 | 12/21 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.799×** | -3.8 | 0.005 | 10/21 (NCI-H1573, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~3% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 803 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 610 | 1 (1 ⚠) | 8 (5 ⚠) | [[Selinexor (drug)]] 5 µM 2.20× (z +8.8) ⚠ cell-cycle shift, explains ~14% of this change | [[Harringtonine (drug)]] 5 µM 0.0729× (z -19.9) |
| [[Hs 766T (line)]] | wt | 660 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -20.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 135 | 2 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.47× (z +11.4) | [[Ixazomib citrate (drug)]] 5 µM 0.258× (z -12.1) |
| [[LS 180 (line)]] | wt | 296 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 172 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -18.3) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -11.2) |
| [[A549 (line)]] | wt | 758 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -17.6) |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.221× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -9.4) |
| [[BT-474 (line)]] | alt | 91.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -13.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.204× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 77.4 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.265× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.272× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 64.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +18.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.71× (z +10.1) | — |
| [[A-427 (line)]] | wt | 66.1 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.16× (z +9.0) | [[Ixazomib citrate (drug)]] 0.5 µM 0.334× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 279 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -14.5) |
| [[A498 (line)]] | wt | 277 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +14.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 359 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +18.7) ⚠ cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -8.7) |
| [[SW 1271 (line)]] | alt | 146 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0477× (z -12.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 67.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.86× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 224 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -12.2) |
| [[A-172 (line)]] | wt | 21.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 21.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 21.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.1 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.6 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 31.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.9 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 31.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 28.6 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 14.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCHF4]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[BMP6]] | +0.64 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[CDH4]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[FAM107B]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ITGA2]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[NR2E3]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[THSD4]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[CDCP1]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[IL31RA]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ANTXR2]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[AADACP1]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[CAPN2]] | +0.61 | +0.62 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCP1]] | B | CDCP1 activity raises SLC35F3's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 3.08× lower at baseline in the lines without CDCP1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[GPR39]] | B | GPR39 activity raises SLC35F3's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.87× lower at baseline in the lines without GPR39 | 0.030 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[ITGA2]] | B | ITGA2 activity raises SLC35F3's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 3.69× lower at baseline in the lines without ITGA2 | 0.046 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[PLEK2]] | B | PLEK2 activity raises SLC35F3's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.91× lower at baseline in the lines without PLEK2 | 0.050 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[AMOTL1]] | B | AMOTL1 activity raises SLC35F3's level | lines that do not express AMOTL1 (16) vs lines expressing it (34) | 3.23× lower at baseline in the lines without AMOTL1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, RNF150, NALCN |
| [[ZNF185]] | B | ZNF185 activity raises SLC35F3's level | lines that do not express ZNF185 (15) vs lines expressing it (35) | 2.25× lower at baseline in the lines without ZNF185 | 0.093 | ⚠ within organs, on part of the lines; also absent: HTR1D, KLF5, IL18 |
| [[MAP2K1]] | B | MAP2K1 activity raises SLC35F3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[NR2E3]] | C | NR2E3 activity raises SLC35F3's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 4.23× lower at baseline in the lines without NR2E3 | 0.008 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L; co-absent with the target |
| [[LINP1]] | C | LINP1 activity raises SLC35F3's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.70× lower at baseline in the lines without LINP1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1; co-absent with the target |
| [[EYA2]] | C | EYA2 activity raises SLC35F3's level | lines that do not express EYA2 (34) vs lines expressing it (16) | 3.23× lower at baseline in the lines without EYA2 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL22A1, LGSN, EPGN; co-absent with the target |
| [[THSD4]] | C | THSD4 activity raises SLC35F3's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 3.02× lower at baseline in the lines without THSD4 | 0.099 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR39]] | B | SLC35F3 activity raises GPR39's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 2.43× lower at baseline in the lines without SLC35F3 | 0.011 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3 |
| [[CDCP1]] | B | SLC35F3 activity raises CDCP1's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 3.46× lower at baseline in the lines without SLC35F3 | 0.021 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3 |
| [[ITGA6]] | B | SLC35F3 activity raises ITGA6's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 1.17× lower at baseline in the lines without SLC35F3 | 0.056 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3 |
| [[SHANK2]] | B | SLC35F3 activity raises SHANK2's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 2.67× lower at baseline in the lines without SLC35F3 | 0.073 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3 |
| [[PCED1B]] | B | SLC35F3 activity raises PCED1B's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 2.19× lower at baseline in the lines without SLC35F3 | 0.080 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3 |
| [[THSD4]] | C | SLC35F3 activity raises THSD4's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 3.36× lower at baseline in the lines without SLC35F3 | 0.025 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3; co-absent with the target |
| [[NR2E3]] | C | SLC35F3 activity raises NR2E3's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 2.62× lower at baseline in the lines without SLC35F3 | 0.045 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3; co-absent with the target |
| [[LINP1]] | C | SLC35F3 activity raises LINP1's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 1.80× lower at baseline in the lines without SLC35F3 | 0.082 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3; co-absent with the target |

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.0, 8.8); signed map (8.5, 43.9). **Vector** length 99.5, 32.9% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.5 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.3 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +4.2 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.6 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +4.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.0 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -6.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -4.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.2 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member F3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:233,904,676-234,324,511 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37712 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY50](https://www.uniprot.org/uniprotkb/Q8IY50) (Solute carrier family 35 member F3):

> Mediates thiamine transport. Also mediates choline transport, although the underlying transport mechanism remains to be elucidated.

**Summary**, from NCBI Gene [148641](https://www.ncbi.nlm.nih.gov/gene/148641):

> Enables choline transmembrane transporter activity. Involved in choline transport and thiamine transport. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23616) · Entrez [148641](https://www.ncbi.nlm.nih.gov/gene/148641) · UniProt [Q8IY50](https://www.uniprot.org/uniprotkb/Q8IY50) · Ensembl [ENSG00000183780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183780)

## Data

Gene col 11456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11456); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11456]; `tensor/DDL_lfc|DDL_z.npy` [11456]; `embed/gene_vectors.npy` [11456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11456 or target_col == 11456). Every well: [[SLC35F3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35F3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

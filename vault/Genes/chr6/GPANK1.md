---
symbol: "GPANK1"
type: "gene"
col: 12873
ensembl_id: "ENSG00000204438"
name: "G-patch domain and ankyrin repeats 1"
location: "6p21.33"
module: 11
arm: "+"
pooled_cpm: 8.98
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# GPANK1

*G-patch domain and ankyrin repeats 1* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +10.9, q 7e-25, up in 36 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.528× (z -8.0, q 5e-13, down in 36 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.419× (z -5.7, q 3e-06, down in 23 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM32A]] (+0.73, fdr 7e-06), [[ZNF646]] (+0.72, fdr 7e-06), [[TBCC]] (+0.69, fdr 7e-06); moves opposite to [[NDRG3]] (-0.66, fdr 1e-05), [[SLC23A2]] (-0.65, fdr 1e-05), [[CS]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12873.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +10.9 | 7e-25 | 36/44 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.7 | 5e-09 | 26/43 (J82, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.6 | 8e-09 | 24/47 (J82, HOP62, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.009 | 15/42 (J82, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +3.7 | 0.020 | 17/40 (NCI-H2030, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.031 | 10/46 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.043 | 13/46 (J82, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.062 | 9/46 (J82, RKO, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.19× | +3.1 | 0.11 | 6/48 (PANC-1, NCI-H1573, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.13 | 11/46 (RKO, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12873.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.528×** | -8.0 | 5e-13 | 36/47 (PANC-1, C-33 A, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.419×** | -5.7 | 3e-06 | 23/41 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.637×** | -5.7 | 3e-06 | 21/47 (A-172, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -4.9 | 2e-04 | 21/44 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.693×** | -4.6 | 4e-04 | 16/47 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.547×** | -4.0 | 0.007 | 18/44 (CFPAC-1, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.745×** | -3.7 | 0.017 | 17/47 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.819×** | -3.6 | 0.025 | 13/47 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.600×** | -3.4 | 0.048 | 9/40 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.671×** | -3.2 | 0.082 | 5/48 (NCI-H460, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.776× | -3.1 | 0.11 | 14/39 (COLO 205, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 16.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.31× (z +19.3) ⚠ cell-cycle shift, explains ~74% of this change | [[Dinaciclib (drug)]] 5 µM 0.148× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 8.47 | 0 | 2 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0885× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 10.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +9.9) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0871× (z -9.5) |
| [[HOP62 (line)]] | alt | 5.83 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +11.5) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[Hs 766T (line)]] | wt | 5.99 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0963× (z -8.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[hTERT-HPNE (line)]] | wt | 7.43 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.0981× (z -8.5) |
| [[J82 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +15.0) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[LOX-IMVI (line)]] | wt | 9.69 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +10.9) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[SNU-423 (line)]] | alt | 9.37 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +8.6) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[A-172 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM32A]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[ZNF646]] | +0.72 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[TBCC]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[CPT2]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ZNF791]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[C14orf119]] | +0.67 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[SLU7]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[KDM5A]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MAD2L1BP]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[ZNF830]] | +0.64 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[TOPORS]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[RBM8A]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | -0.66 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[SLC23A2]] | -0.65 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[CS]] | -0.64 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[OPA1]] | -0.60 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[TBCD]] | -0.59 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[CPSF6]] | -0.59 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[MEST]] | -0.57 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[SOAT1]] | -0.57 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[MRPL42]] | -0.57 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[FAR1]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[C20orf27]] | -0.55 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[STX2]] | -0.55 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GPANK1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers GPANK1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.7, 5.3); signed map (2.6, -17.2). **Vector** length 76.0, 13.9% of its response variance represented; |z| ≥ 3 in 783 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +6.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +2.7 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -8.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.6 | -5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.6 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | G-patch domain and ankyrin repeats 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,661,228-31,666,283 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G5, D6S54E, GPATCH10, ANKRD59; previously BAT4 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; G-patch domain containing |
| Matched by | ensembl_id |

UniProt [O95872](https://www.uniprot.org/uniprotkb/O95872) carries no function annotation.

**Summary**, from NCBI Gene [7918](https://www.ncbi.nlm.nih.gov/gene/7918):

> This gene is located in a cluster of HLA-B-associated transcripts, which is included in the human major histocompatability complex III region. This gene encodes a protein which is thought to play a role in immunity. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:13920](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13920) · Entrez [7918](https://www.ncbi.nlm.nih.gov/gene/7918) · UniProt [O95872](https://www.uniprot.org/uniprotkb/O95872) · Ensembl [ENSG00000204438](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204438)

## Data

Gene col 12873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12873); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12873]; `tensor/DDL_lfc|DDL_z.npy` [12873]; `embed/gene_vectors.npy` [12873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12873 or target_col == 12873). Every well: [[GPANK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPANK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

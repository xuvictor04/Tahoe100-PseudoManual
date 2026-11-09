---
symbol: "HIKESHI"
type: "gene"
col: 7349
ensembl_id: "ENSG00000149196"
name: "heat shock protein nuclear import factor hikeshi"
location: "11q14.2"
module: 148
arm: "+"
pooled_cpm: 21.62
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 8
n_dd_up_clean: 26
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# HIKESHI

*heat shock protein nuclear import factor hikeshi* — 11q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.62× (z +16.0, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.562× (z -9.6, q 4e-19, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TACO1]] (+0.72, fdr 4e-05), [[ZNF407-AS1]] (+0.70, fdr 1e-04), [[PSMC2]] (+0.70, fdr 1e-05); moves opposite to [[NPHP4]] (-0.67, fdr 2e-04), [[GRK6]] (-0.66, fdr 1e-04), [[FAM118A]] (-0.65, fdr 0.003, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.62×** | +16.0 | 0e+00 | 45/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +11.7 | 3e-29 | 38/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +11.1 | 3e-26 | 36/43 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +10.9 | 2e-25 | 38/47 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.13×** | +9.9 | 4e-21 | 38/48 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +9.5 | 1e-19 | 36/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +9.3 | 1e-18 | 36/47 (LS 180, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +8.4 | 3e-15 | 28/40 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.5 | 5e-12 | 30/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.1 | 7e-11 | 29/48 (C32, NCI-H23, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.9 | 3e-10 | 30/48 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.8 | 4e-10 | 23/47 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +6.5 | 4e-09 | 26/48 (NCI-H2347, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +6.3 | 9e-09 | 22/34 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +5.3 | 3e-06 | 22/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.3 | 6e-04 | 17/48 (LoVo, J82, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.002 | 18/46 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.005 | 20/48 (LoVo, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.562×** | -9.6 | 4e-19 | 32/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.565×** | -9.5 | 5e-19 | 28/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.570×** | -9.4 | 2e-18 | 38/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.573×** | -9.3 | 3e-18 | 35/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.792×** | -3.9 | 0.011 | 15/47 (HOP62, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.816×** | -3.4 | 0.065 | 17/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.821×** | -3.3 | 0.079 | 14/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.823×** | -3.3 | 0.079 | 11/47 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 44.1 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.0) | [[Digitoxin (drug)]] 0.5 µM 0.339× (z -13.7) |
| [[A-172 (line)]] | wt | 16.5 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.86× (z +12.8) | — |
| [[SW480 (line)]] | alt | 30.3 | 1 | 3 | [[Auranofin (drug)]] 5 µM 3.25× (z +12.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -15.3) |
| [[BT-474 (line)]] | alt | 15.3 | 1 | 2 | [[Auranofin (drug)]] 5 µM 7.16× (z +9.8) | [[Digitoxin (drug)]] 0.5 µM 0.158× (z -9.1) |
| [[C32 (line)]] | wt | 19.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.19× (z +11.5) | — |
| [[LoVo (line)]] | wt | 15.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.08× (z +10.8) | — |
| [[RKO (line)]] | wt | 20.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +9.4) | — |
| [[A498 (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +11.2) | — |
| [[A549 (line)]] | wt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.35× (z +11.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 22.6 | 0 | 1 | — | [[Bestatin (drug)]] 5 µM 0.0657× (z -9.0) |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.132× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 23.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.22× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 14.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.99× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 25.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -10.4) |
| [[KATO III (line)]] | alt | 31.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.344× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.305× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 25.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.42× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 17.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.72× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 24.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.99× (z +9.7) | — |
| [[A-427 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TACO1]] | +0.72 | +0.78 / +0.42 | both halves | 4e-05 |  |
| [[ZNF407-AS1]] | +0.70 | +0.77 / +0.36 | both halves | 1e-04 |  |
| [[PSMC2]] | +0.70 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[PEF1]] | +0.70 | +0.70 / +0.34 | both halves | 1e-04 |  |
| [[C3orf38]] | +0.69 | +0.74 / +0.36 | both halves | 1e-04 |  |
| [[FAM200A]] | +0.67 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[GIN1]] | +0.67 | +0.72 / +0.36 | both halves | 1e-04 |  |
| [[MOB4]] | +0.67 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[METTL6]] | +0.67 | +0.71 / +0.32 | both halves | 2e-04 |  |
| [[FIZ1]] | +0.67 | +0.73 / +0.23 | both halves | 5e-04 |  |
| [[AEBP2]] | +0.66 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[CCDC59]] | +0.66 | +0.64 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP4]] | -0.67 | -0.66 / -0.30 | both halves | 2e-04 |  |
| [[GRK6]] | -0.66 | -0.71 / -0.33 | both halves | 1e-04 |  |
| [[FAM118A]] | -0.65 | -0.73 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[NHP2]] | -0.59 | -0.52 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HIKESHI's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-15.8, 8.7); signed map (14.2, -24.3). **Vector** length 97.1, 22.7% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.4 | +16.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.0 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +9.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +7.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.6 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.5 | -9.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.3 | -3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -9.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein nuclear import factor hikeshi |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.2 — chr11:86,302,211-86,345,943 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC138, HSPC179, OPI10; previously C11orf73 |
| Reactome | 4 pathways, smallest: Regulation of HSF1-mediated heat shock response; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53FT3](https://www.uniprot.org/uniprotkb/Q53FT3) (Protein Hikeshi):

> Acts as a specific nuclear import carrier for HSP70 proteins following heat-shock stress: acts by mediating the nucleoporin-dependent translocation of ATP-bound HSP70 proteins into the nucleus. HSP70 proteins import is required to protect cells from heat shock damages. Does not translocate ADP-bound HSP70 proteins into the nucleus.

**Summary**, from NCBI Gene [51501](https://www.ncbi.nlm.nih.gov/gene/51501):

> This gene encodes an evolutionarily conserved nuclear transport receptor that mediates heat-shock-induced nuclear import of 70 kDa heat-shock proteins (Hsp70s) through interactions with FG-nucleoporins. The protein mediates transport of the ATP form but not the ADP form of Hsp70 proteins under conditions of heat shock stress. Structural analyses demonstrate that the protein forms an asymmetric homodimer and that the N-terminal domain consists of a jelly-roll/beta-sandwich fold structure that …

**Accessions** — [HGNC:26938](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26938) · Entrez [51501](https://www.ncbi.nlm.nih.gov/gene/51501) · UniProt [Q53FT3](https://www.uniprot.org/uniprotkb/Q53FT3) · Ensembl [ENSG00000149196](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149196)

## Data

Gene col 7349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7349); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7349]; `tensor/DDL_lfc|DDL_z.npy` [7349]; `embed/gene_vectors.npy` [7349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7349 or target_col == 7349). Every well: [[HIKESHI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIKESHI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "MICALL2"
type: "gene"
col: 9017
ensembl_id: "ENSG00000164877"
name: "MICAL like 2"
location: "7p22.3"
module: 33
arm: "-"
pooled_cpm: 23.06
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 23
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# MICALL2

*MICAL like 2* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.77× (z +19.2, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.893× (z -5.4, q 4e-05, down in 7 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.779× (z -4.7, q 6e-04, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGRN]] (+0.57, fdr 1e-05), [[CCDC200]] (+0.57, fdr 1e-05), [[RELT]] (+0.54, fdr 2e-05); moves opposite to [[ORC5]] (-0.61, fdr 1e-05), [[WDR3]] (-0.58, fdr 1e-05), [[RMND1]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9017.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.77×** | +19.2 | 0e+00 | 41/45 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.72×** | +17.4 | 0e+00 | 48/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +16.4 | 0e+00 | 40/45 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.83×** | +13.8 | 3e-41 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.44×** | +11.8 | 4e-30 | 44/47 (SW480, KATO III, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +11.0 | 5e-26 | 38/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +10.9 | 7e-26 | 36/45 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +8.8 | 1e-16 | 31/48 (A-172, J82, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.90×** | +8.5 | 1e-15 | 30/48 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +8.5 | 1e-15 | 36/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +8.3 | 7e-15 | 30/47 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.78×** | +7.6 | 1e-12 | 29/47 (LoVo, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +6.2 | 2e-08 | 27/48 (SW480, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +5.7 | 5e-07 | 26/47 (KATO III, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +5.7 | 5e-07 | 23/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +5.3 | 4e-06 | 26/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 3e-04 | 22/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9017.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -5.4 | 4e-05 | 7/49 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.779×** | -4.7 | 6e-04 | 22/48 (NCI-H1792, RPMI-7951, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.727×** | -4.3 | 0.003 | 20/48 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.580×** | -3.8 | 0.020 | 17/44 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 0.633× | -3.2 | 0.15 | 16/49 (HT-29, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | 0.848× | -3.2 | 0.15 | 14/48 (SNU-1, NCI-H661, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.850× | -3.1 | 0.16 | 5/48 (SNU-1, RKO, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9017. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.9 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.7) | — |
| [[LoVo (line)]] | wt | 12.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +14.3) | — |
| [[AsPC-1 (line)]] | alt | 14.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +14.6) | — |
| [[KATO III (line)]] | alt | 33.2 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.40× (z +12.0) | — |
| [[SW480 (line)]] | alt | 22.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.30× (z +14.6) | — |
| [[A-172 (line)]] | wt | 36.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.9) | — |
| [[A498 (line)]] | wt | 37.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +16.8) | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 8.16 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 38.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.81× (z +15.0) | — |
| [[SW1417 (line)]] | alt | 20.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.27× (z +10.5) | — |
| [[SW48 (line)]] | wt | 23.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 23.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +11.7) | — |
| [[Hs 766T (line)]] | wt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +11.3) | — |
| [[J82 (line)]] | alt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +13.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.49× (z +10.8) | — |
| [[A-427 (line)]] | wt | 7.62 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.72× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 29.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.50× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HCT15 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +11.8) | — |
| [[HT-29 (line)]] | alt | 38.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.61× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.158× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 37.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 14.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.38× (z +9.6) | — |
| [[A549 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9017), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGRN]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[CCDC200]] | +0.57 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[RELT]] | +0.54 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[BAIAP2]] | +0.54 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[ISYNA1]] | +0.54 | +0.43 / +0.50 | both halves | 4e-05 |  |
| [[NOTCH1]] | +0.54 | +0.59 / +0.49 | both halves | 2e-05 |  |
| [[ACADVL]] | +0.53 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[DMWD]] | +0.52 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[ZMIZ1]] | +0.51 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[MC1R]] | +0.50 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[PITRM1]] | +0.49 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[TNFSF9]] | +0.49 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORC5]] | -0.61 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[WDR3]] | -0.58 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[RMND1]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[MRPL15]] | -0.57 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[ZNHIT6]] | -0.57 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[NARS2]] | -0.57 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TAMM41]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[MRPS35]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[GEMIN5]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[KAT14]] | -0.55 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[SMARCAD1]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[NUFIP1]] | -0.54 | -0.28 / -0.56 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MICALL2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **-** arm (projection on the module's main direction -0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.3, -43.7); signed map (1.8, 20.3). **Vector** length 89.8, 21.3% of its response variance represented; |z| ≥ 3 in 1,240 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.4 | +2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +16.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +6.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +4.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +4.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.8 | -3.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.8 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.3 | -3.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.9 | -4.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | MICAL like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:1,428,465-1,459,470 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC46023, FLJ23471, MICAL-L2, JRAB |
| Gene groups (HGNC) | LIM domain containing; Bivalent Mical/EHBP Rab binding domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY33](https://www.uniprot.org/uniprotkb/Q8IY33) (MICAL-like protein 2):

> Effector of small Rab GTPases which is involved in junctional complexes assembly through the regulation of cell adhesion molecules transport to the plasma membrane and actin cytoskeleton reorganization. Regulates the endocytic recycling of occludins, claudins and E-cadherin to the plasma membrane and may thereby regulate the establishment of tight junctions and adherens junctions. In parallel, may regulate actin cytoskeleton reorganization directly through interaction with F-actin or indirectly …

**Summary**, from NCBI Gene [79778](https://www.ncbi.nlm.nih.gov/gene/79778):

> Enables filamin binding activity. Involved in obsolete positive regulation of protein targeting to mitochondrion. Predicted to be located in several cellular components, including bicellular tight junction; recycling endosome; and stress fiber. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29672) · Entrez [79778](https://www.ncbi.nlm.nih.gov/gene/79778) · UniProt [Q8IY33](https://www.uniprot.org/uniprotkb/Q8IY33) · Ensembl [ENSG00000164877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164877)

## Data

Gene col 9017: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9017); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9017, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9017]; `tensor/DDL_lfc|DDL_z.npy` [9017]; `embed/gene_vectors.npy` [9017]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9017 or target_col == 9017). Every well: [[MICALL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MICALL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

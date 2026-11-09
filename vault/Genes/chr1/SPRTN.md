---
symbol: "SPRTN"
type: "gene"
col: 198
ensembl_id: "ENSG00000010072"
name: "SprT-like N-terminal domain"
location: "1q42.2"
module: 7
arm: "+"
pooled_cpm: 13.31
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SPRTN

*SprT-like N-terminal domain* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.79× (z +20.1, q 0e+00, up in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.80× (z +20.0, q 0e+00, up in 45 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Hydroxyurea (drug)]] 0.05 µM in 1 line (RKO 0.0703×); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (BT-474 0.0780×); [[Pemetrexed (drug)]] 0.5 µM in 1 line (SNU-423 0.162×).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHUK]] (+0.52, fdr 4e-05), [[TIMM22]] (+0.49, fdr 1e-04), [[AREL1]] (+0.48, fdr 6e-04); moves opposite to [[PER1]] (-0.44, fdr 3e-04), [[TFRC]] (-0.43, fdr 2e-04), [[AP1AR]] (-0.42, fdr 4e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.79×** | +20.1 | 0e+00 | 45/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.80×** | +20.0 | 0e+00 | 45/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.74×** | +19.7 | 0e+00 | 46/47 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +17.8 | 0e+00 | 38/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +17.5 | 0e+00 | 37/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +14.3 | 4e-44 | 40/46 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +13.1 | 2e-37 | 32/42 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.88×** | +12.2 | 2e-32 | 34/46 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.85×** | +12.0 | 2e-31 | 38/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.75×** | +10.9 | 1e-25 | 35/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +10.5 | 3e-24 | 33/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.77×** | +10.5 | 3e-24 | 31/46 (SNU-423, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.60×** | +9.8 | 6e-21 | 30/47 (LS 180, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +9.6 | 3e-20 | 28/47 (HT-29, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.65×** | +9.5 | 1e-19 | 27/46 (RKO, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +9.4 | 2e-19 | 25/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +8.5 | 5e-16 | 27/45 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +7.7 | 5e-13 | 23/45 (PANC-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 198.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Hydroxyurea (drug)]] 0.05 µM in 1 line (RKO 0.0703×); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (BT-474 0.0780×); [[Pemetrexed (drug)]] 0.5 µM in 1 line (SNU-423 0.162×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.843× | -3.4 | 0.39 | 11/47 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.854× | -3.1 | 0.47 | 7/48 (RPMI-7951, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 9.30 | 3 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 5.72× (z +9.0) | — |
| [[SW480 (line)]] | alt | 14.5 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 8.64 | 0 | 2 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0780× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 13.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.15 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.44× (z +9.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 15.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.7) | — |
| [[RKO (line)]] | wt | 12.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +9.4) | [[Hydroxyurea (drug)]] 0.05 µM 0.0703× (z -12.7) |
| [[H4 (line)]] | wt | 8.95 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0648× (z -8.8) |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.101× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 1 | — | [[Pemetrexed (drug)]] 0.5 µM 0.162× (z -9.6) |
| [[A-172 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHUK]] | +0.52 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[TIMM22]] | +0.49 | +0.55 / +0.32 | both halves | 1e-04 |  |
| [[AREL1]] | +0.48 | +0.21 / +0.43 | both halves | 6e-04 |  |
| [[PSMD7]] | +0.48 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[ZNF346]] | +0.46 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ACTR1A]] | +0.46 | +0.36 / +0.38 | both halves | 1e-04 |  |
| [[FASTKD5]] | +0.46 | +0.44 / +0.32 | both halves | 2e-04 |  |
| [[PSMD1]] | +0.46 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[SMIM10L1]] | +0.45 | +0.52 / +0.33 | both halves | 1e-04 |  |
| [[GPATCH8]] | +0.45 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[PHF23]] | +0.45 | +0.52 / +0.23 | both halves | 5e-04 |  |
| [[PLAA]] | +0.45 | +0.33 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PER1]] | -0.44 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[TFRC]] | -0.43 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[AP1AR]] | -0.42 | -0.25 / -0.32 | both halves | 4e-04 |  |
| [[NDUFV2]] | -0.42 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[TUBE1]] | -0.41 | -0.47 / -0.22 | both halves | 6e-04 |  |
| [[MTX2]] | -0.41 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[IMPDH2]] | -0.40 | -0.43 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[DESI2]] | -0.40 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[FIG4]] | -0.39 | -0.43 / -0.26 | both halves | 3e-04 |  |
| [[CD83]] | -0.38 | -0.40 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[SLC35A5]] | -0.38 | -0.25 / -0.26 | both halves | 4e-04 |  |
| [[SNHG1]] | -0.38 | -0.28 / -0.31 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPRTN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.377). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-45.9, 2.2); signed map (-7.1, -26.0). **Vector** length 50.1, 6.85% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.1 | +10.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +10.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +13.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.6 | +9.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.5 | +10.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +9.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +5.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.3 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.0 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.6 | +20.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.6 | +8.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.2 | +0.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | SprT-like N-terminal domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:231,337,104-231,355,023 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP547N043, Spartan, DVC1; previously C1orf124 |
| Gene groups (HGNC) | Zinc fingers UBZ4 CCHC-type |
| Reactome | 4 pathways, smallest: Translesion Synthesis by POLH; Translesion synthesis by Y family DNA polymerases bypasses lesions on DNA template; DNA Damage Bypass |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H040](https://www.uniprot.org/uniprotkb/Q9H040) (DNA-dependent metalloprotease SPRTN):

> DNA-dependent metalloendopeptidase that mediates the proteolytic cleavage of covalent DNA-protein cross-links (DPCs) during DNA synthesis and mitosis, thereby playing a key role in maintaining genomic integrity. DPCs are highly toxic DNA lesions that interfere with essential chromatin transactions, such as replication and transcription, and which are induced by reactive agents, such as UV light or formaldehyde. Associates with the DNA replication machinery and specifically removes DPCs during …

**Summary**, from NCBI Gene [83932](https://www.ncbi.nlm.nih.gov/gene/83932):

> The protein encoded by this gene may play a role in DNA repair during replication of damaged DNA. This protein recruits valosin containing protein (p97) to stalled DNA replication forks where it may prevent excessive translesional DNA synthesis and limit the number of DNA-damage induced mutations. It may also be involved in replication-related G2/M-checkpoint regulation. Deficiency of a similar protein in mouse causes chromosomal instability and progeroid phenotypes. Mutations in this gene have …

**Accessions** — [HGNC:25356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25356) · Entrez [83932](https://www.ncbi.nlm.nih.gov/gene/83932) · UniProt [Q9H040](https://www.uniprot.org/uniprotkb/Q9H040) · Ensembl [ENSG00000010072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010072)

## Data

Gene col 198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 198); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 198]; `tensor/DDL_lfc|DDL_z.npy` [198]; `embed/gene_vectors.npy` [198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 198 or target_col == 198). Every well: [[SPRTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

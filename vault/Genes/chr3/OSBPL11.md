---
symbol: "OSBPL11"
type: "gene"
col: 6946
ensembl_id: "ENSG00000144909"
name: "oxysterol binding protein like 11"
location: "3q21.2"
module: 129
arm: "+"
pooled_cpm: 32.42
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# OSBPL11

*oxysterol binding protein like 11* — 3q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.56× (z +11.0, q 1e-25, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.735× (z -5.2, q 1e-04, down in 20 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 0.790× (z -4.2, q 0.007, down in 14 of 48 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK38L]] (+0.56, fdr 1e-05), [[AKIRIN1]] (+0.54, fdr 3e-05), [[RBBP8]] (+0.49, fdr 2e-04); moves opposite to [[PIK3C3]] (-0.51, fdr 4e-05), [[ELOA-AS1]] (-0.49, fdr 2e-04), [[LINC00159]] (-0.49, fdr 1e-04).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +11.0 | 1e-25 | 32/47 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +11.0 | 1e-25 | 31/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +9.1 | 2e-17 | 33/48 (J82, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.40×** | +8.3 | 1e-14 | 30/48 (CFPAC-1, J82, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +7.3 | 4e-11 | 27/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +6.8 | 1e-09 | 27/47 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +6.7 | 2e-09 | 24/47 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.31×** | +6.7 | 2e-09 | 25/48 (J82, RKO, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +6.6 | 2e-09 | 23/48 (J82, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.21×** | +4.7 | 1e-04 | 16/47 (SW480, CFPAC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.20× | +4.4 | 5e-04 | 14/48 (SNU-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.20×** | +4.4 | 5e-04 | 17/37 (HEC-1-A, HS-578T, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.19× | +4.2 | 1e-03 | 14/48 (SNU-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +4.0 | 0.002 | 9/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.17× | +3.9 | 0.004 | 18/47 (LoVo, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.089 | 11/48 (HOP62, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.735×** | -5.2 | 1e-04 | 20/42 (NCI-H460, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.790×** | -4.2 | 0.007 | 14/48 (PANC-1, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.732×** | -4.1 | 0.009 | 12/38 (HT-29, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.801×** | -4.0 | 0.011 | 16/46 (BT-474, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.851× | -3.9 | 0.012 | 17/47 (HepG2/C3A, COLO 205, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.869× | -3.5 | 0.044 | 12/47 (SW 1271, A-172, …) | inconsistent across doses |  |
| [[Vandetanib (drug)]] 0.5 µM |  | 0.872× | -3.4 | 0.053 | 8/47 (CHP-212, PANC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.828×** | -3.4 | 0.055 | 8/48 (HEC-1-A, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.910× | -3.3 | 0.055 | 9/48 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.831×** | -3.3 | 0.055 | 6/48 (HEC-1-A, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.881× | -3.2 | 0.079 | 11/47 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.885× | -3.1 | 0.10 | 10/47 (NCI-H23, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 38.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +13.4) | — |
| [[A-427 (line)]] | wt | 70.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.598× (z -8.9) |
| [[A498 (line)]] | wt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.2) | — |
| [[KATO III (line)]] | alt | 41.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[MIA PaCa-2 (line)]] | alt | 29.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.164× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.247× (z -9.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 45.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.158× (z -10.7) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK38L]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[AKIRIN1]] | +0.54 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[RBBP8]] | +0.49 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[BCAP29]] | +0.49 | +0.22 / +0.53 | both halves | 6e-04 |  |
| [[SCYL2]] | +0.49 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[SMARCB1]] | +0.47 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[MTMR9]] | +0.47 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[TEX2]] | +0.46 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[VPS4A]] | +0.46 | +0.23 / +0.46 | both halves | 5e-04 |  |
| [[FAM118B]] | +0.46 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[SSX2IP]] | +0.45 | +0.24 / +0.55 | both halves | 5e-04 |  |
| [[IPO9]] | +0.45 | +0.24 / +0.59 | both halves | 5e-04 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3C3]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ELOA-AS1]] | -0.49 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[LINC00159]] | -0.49 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[GGA2]] | -0.45 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ALG1L9P]] | -0.45 | -0.24 / -0.50 | both halves | 4e-04 |  |
| [[LINC02680]] | -0.44 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[ACP6]] | -0.44 | -0.17 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[ELP2]] | -0.44 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[RPL34-DT]] | -0.44 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[LINC01482]] | -0.44 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[TAGAP-AS1]] | -0.44 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[CD27-AS1]] | -0.44 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[TBX19]] | -0.43 | -0.27 / -0.49 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers OSBPL11's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.117). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.8, 28.2); signed map (-5.8, 38.7). **Vector** length 68.2, 11.4% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.5 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.4 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | +2.9 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.1 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.0 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.4 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.6 | -3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -3.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +0.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.8 | -3.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | oxysterol binding protein like 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.2 — chr3:125,528,858-125,595,497 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ORP-11, ORP11, FLJ13012, FLJ13164 |
| Gene groups (HGNC) | Oxysterol binding proteins; Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: RHOH GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXB4](https://www.uniprot.org/uniprotkb/Q9BXB4) (Oxysterol-binding protein-related protein 11):

> Plays a role in regulating ADIPOQ and FABP4 levels in differentiating adipocytes and is also involved in regulation of adipocyte triglyceride storage. Weakly binds 25-hydroxycholesterol. Interacts with OSBPL9 to function as lipid transfer proteins. Together they form a heterodimer that localizes at the ER-trans-Golgi membrane contact sites, and exchanges phosphatidylserine (1,2-diacyl-sn-glycero-3-phospho-L-serine, PS) for phosphatidylinositol-4-phosphate …

**Summary**, from NCBI Gene [114885](https://www.ncbi.nlm.nih.gov/gene/114885):

> This gene encodes a member of the oxysterol-binding protein (OSBP) family, a group of intracellular lipid receptors. Like most members, the encoded protein contains an N-terminal pleckstrin homology domain and a highly conserved C-terminal OSBP-like sterol-binding domain. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16397) · Entrez [114885](https://www.ncbi.nlm.nih.gov/gene/114885) · UniProt [Q9BXB4](https://www.uniprot.org/uniprotkb/Q9BXB4) · Ensembl [ENSG00000144909](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144909)

## Data

Gene col 6946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6946); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6946]; `tensor/DDL_lfc|DDL_z.npy` [6946]; `embed/gene_vectors.npy` [6946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6946 or target_col == 6946). Every well: [[OSBPL11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSBPL11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

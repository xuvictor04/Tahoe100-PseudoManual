---
symbol: "SPATA32"
type: "gene"
col: 11524
ensembl_id: "ENSG00000184361"
name: "spermatogenesis associated 32"
location: "17q21.31"
module: 47
arm: "+"
pooled_cpm: 2.47
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SPATA32

*spermatogenesis associated 32* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.49× (z +14.1, q 4e-42, up in 17 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.308× (z -9.4, q 2e-18, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM41]] (+0.81, fdr 7e-06), [[CPT1C]] (+0.69, fdr 7e-06), [[CHADL]] (+0.69, fdr 7e-06); moves opposite to [[RNPC3]] (-0.57, fdr 4e-05), [[CIAO2A]] (-0.54, fdr 2e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ASGR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.49×** | +14.1 | 4e-42 | 17/30 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.51×** | +7.3 | 8e-11 | 30/40 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.49×** | +7.2 | 9e-11 | 24/41 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.31×** | +6.7 | 4e-09 | 19/39 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.13×** | +5.8 | 9e-07 | 0/3 | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +5.2 | 2e-05 | 12/29 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.0 | 4e-05 | 12/31 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.86×** | +4.9 | 6e-05 | 11/25 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.84×** | +4.8 | 8e-05 | 11/44 (A498, C-33 A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +4.6 | 3e-04 | 11/42 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.58×** | +3.4 | 0.041 | 0/4 | all doses, stronger at high dose | composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.056 | 6/22 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.48×** | +3.1 | 0.077 | 0/10 | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.0 | 0.10 | 2/42 (A-427, C-33 A) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11524.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.308×** | -9.4 | 2e-18 | 34/43 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.406×** | -7.2 | 2e-10 | 25/38 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.440×** | -6.6 | 1e-08 | 15/21 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.453×** | -6.3 | 3e-08 | 22/36 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.559×** | -4.7 | 4e-04 | 16/40 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.581×** | -4.3 | 0.001 | 14/33 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.591×** | -4.2 | 0.002 | 16/42 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.591×** | -4.2 | 0.002 | 10/40 (C32, SW48, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.606×** | -4.0 | 0.004 | 7/42 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.620×** | -3.8 | 0.007 | 7/36 (A-427, A549, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.635×** | -3.5 | 0.024 | 13/18 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **0.638×** | -3.5 | 0.024 | 6/34 (J82, HT-29, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.633×** | -3.4 | 0.030 | 8/41 (SW48, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.751×** | -3.3 | 0.045 | 14/42 (SW1417, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.669×** | -3.2 | 0.047 | 10/41 (NCI-H2030, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 9.23 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0495× (z -14.2) ⚠ toxic |
| [[J82 (line)]] | alt | 5.18 | 0 | 2 | — | [[Thymol (drug)]] 0.05 µM 0.0505× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 1.95 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +12.1) | — |
| [[SW480 (line)]] | alt | 2.37 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0528× (z -10.2) |
| [[HOP62 (line)]] | alt | 2.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.71× (z +10.3) | — |
| [[LoVo (line)]] | wt | 1.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 4.59 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.0605× (z -8.7) |
| [[A-172 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.855 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.999 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.754 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.836 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.913 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.812 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM41]] | +0.81 | +0.82 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[CPT1C]] | +0.69 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[CHADL]] | +0.69 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[MYLK2]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[TMEM25]] | +0.67 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[A3GALT2]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MMP25]] | +0.65 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[LINC02236]] | +0.65 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.64 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[ASTL]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MYO15A]] | +0.64 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[TINCR]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNPC3]] | -0.57 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[CIAO2A]] | -0.54 | -0.61 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASGR1]] | B | ASGR1 activity raises SPATA32's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without ASGR1 | 0.025 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers SPATA32's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MPP4]] | C | MPP4 activity raises SPATA32's level | lines that do not express MPP4 (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without MPP4 | 0.074 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, LINC01762, ENSG00000286162; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.6, -15.0); signed map (17.3, 13.3). **Vector** length 64.7, 10.9% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.3 | +5.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.7 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | -0.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +0.9 | +0.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -9.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.3 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.3 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.1 | -6.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:45,254,393-45,262,094 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25414, AEP2, VAD1.2; previously C17orf46, TEX34 |
| Matched by | ensembl_id |

UniProt [Q96LK8](https://www.uniprot.org/uniprotkb/Q96LK8) carries no function annotation.

**Summary**, from NCBI Gene [124783](https://www.ncbi.nlm.nih.gov/gene/124783):

> Predicted to enable actin binding activity. Predicted to be involved in spermatogenesis. Predicted to be active in perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26349) · Entrez [124783](https://www.ncbi.nlm.nih.gov/gene/124783) · UniProt [Q96LK8](https://www.uniprot.org/uniprotkb/Q96LK8) · Ensembl [ENSG00000184361](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184361)

## Data

Gene col 11524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11524); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11524]; `tensor/DDL_lfc|DDL_z.npy` [11524]; `embed/gene_vectors.npy` [11524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11524 or target_col == 11524). Every well: [[SPATA32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

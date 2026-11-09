---
symbol: "PRR7-AS1"
type: "gene"
col: 14462
ensembl_id: "ENSG00000246334"
name: "PRR7 antisense RNA 1"
location: "5q35.3"
module: 5
arm: "+"
pooled_cpm: 8.39
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PRR7-AS1

*PRR7 antisense RNA 1* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.60× (z +6.0, q 1e-06, up in 23 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.312× (z -10.4, q 1e-22, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PALD1]] (+0.67, fdr 7e-06), [[MRTO4]] (+0.60, fdr 1e-05), [[P2RY11]] (+0.59, fdr 1e-05); moves opposite to [[LAPTM4A]] (-0.56, fdr 4e-05), [[MAPK3]] (-0.54, fdr 9e-05), [[LANCL1]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CMTM7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14462.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.0 | 1e-06 | 23/43 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.44×** | +4.6 | 1e-03 | 19/42 (NCI-H1573, NCI-H460, …) | top dose only | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.049 | 8/45 (HS-578T, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +3.5 | 0.049 | 13/44 (NCI-H2347, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.52×** | +3.5 | 0.049 | 4/18 (HOP62, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **2.03×** | +3.3 | 0.085 | 8/34 (HS-578T, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14462.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.312×** | -10.4 | 1e-22 | 31/45 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.390×** | -8.4 | 1e-14 | 35/44 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.423×** | -7.7 | 3e-12 | 30/44 (HEC-1-A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.487×** | -6.5 | 1e-08 | 30/46 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.647×** | -5.5 | 5e-06 | 22/46 (J82, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.330×** | -5.2 | 2e-05 | 25/44 (SK-MEL-2, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.568×** | -4.7 | 3e-04 | 20/44 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.674×** | -4.3 | 0.001 | 20/45 (SW480, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.620×** | -4.3 | 0.001 | 22/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.633×** | -4.1 | 0.003 | 18/44 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.623×** | -4.0 | 0.003 | 20/44 (RKO, A-427, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.646×** | -3.9 | 0.005 | 16/44 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.689×** | -3.8 | 0.005 | 20/46 (COLO 205, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.647×** | -3.7 | 0.008 | 19/43 (SW480, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **0.469×** | -3.5 | 0.016 | 15/42 (H4, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0744× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 13.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0728× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 10.7 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +9.8) ⚠ cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -10.8) |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -11.3) |
| [[J82 (line)]] | alt | 13.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0533× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.271× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 27.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.157× (z -11.1) |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0486× (z -11.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.0822× (z -8.8) |
| [[A498 (line)]] | wt | 5.44 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0721× (z -9.3) |
| [[C32 (line)]] | wt | 9.75 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0685× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 4.46 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0747× (z -8.5) |
| [[LoVo (line)]] | wt | 6.06 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +8.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[LOX-IMVI (line)]] | wt | 3.78 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +8.6) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1573 (line)]] | alt | 2.58 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +10.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 5.18 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0765× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 4.04 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0477× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 9.87 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0514× (z -11.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 4.26 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0277× (z -10.5) |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 1 | — | [[Neratinib (drug)]] 5 µM 0.109× (z -9.7) |
| [[SW48 (line)]] | wt | 17.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0938× (z -8.9) |
| [[SW480 (line)]] | alt | 11.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.139× (z -9.9) |
| [[A-172 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALD1]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[P2RY11]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[KCNJ14]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[POLR1C]] | +0.58 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PRR7]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CDK5R1]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[NOP2]] | +0.57 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[IL19]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[NOP56]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[EEF1AKMT1]] | +0.56 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[DUS2]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[E2F3]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAPTM4A]] | -0.56 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[MAPK3]] | -0.54 | -0.37 / -0.53 | both halves | 9e-05 |  |
| [[LANCL1]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[VAMP7]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ARHGAP17]] | -0.52 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[KRAS]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[CCDC28A]] | -0.51 | -0.57 / -0.43 | both halves | 4e-05 |  |
| [[ARNT]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[LAMP2]] | -0.50 | -0.43 / -0.54 | both halves | 4e-05 |  |
| [[YPEL2]] | -0.50 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[PGM2L1]] | -0.50 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[OSBPL9]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CMTM7]] | B | CMTM7 activity raises PRR7-AS1's level | lines that do not express CMTM7 (5) vs lines expressing it (45) | 1.95× lower at baseline in the lines without CMTM7 | 0.082 | ⚠ within organs, on part of the lines; also absent: EPB41L2, FAM3C2P, P3H1 |
| [[MAP2K1]] | B | MAP2K1 activity raises PRR7-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.570). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (28.4, -6.8); signed map (10.9, 19.5). **Vector** length 92.1, 20.0% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.4 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +0.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +2.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.7 | -6.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.8 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.4 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | PRR7 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q35.3 — chr5:177,438,503-177,447,982 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27961) · Entrez [340037](https://www.ncbi.nlm.nih.gov/gene/340037) · Ensembl [ENSG00000246334](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246334)

## Data

Gene col 14462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14462); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14462]; `tensor/DDL_lfc|DDL_z.npy` [14462]; `embed/gene_vectors.npy` [14462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14462 or target_col == 14462). Every well: [[PRR7-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR7-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

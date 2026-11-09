---
symbol: "MFSD14CP-1"
type: "gene"
col: 16504
ensembl_id: "ENSG00000290770"
name: ""
location: ""
module: 5
arm: "+"
pooled_cpm: 45.58
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MFSD14CP-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +4.9, q 5e-04, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.402× (z -7.8, q 3e-12, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUTM2A-AS1]] (+0.74, fdr 7e-06), [[C1orf159]] (+0.70, fdr 7e-06), [[NUTM2B-AS1]] (+0.70, fdr 7e-06); moves opposite to [[DBP]] (-0.61, fdr 1e-05), [[ZNF14]] (-0.61, fdr 1e-05), [[FAM229B]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.9 | 5e-04 | 25/47 (PANC-1, H4, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.4 | 0.004 | 21/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.23× | +3.5 | 0.10 | 17/48 (CFPAC-1, LS 180, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.2 | 0.23 | 10/48 (SNU-423, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16504.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.402×** | -7.8 | 3e-12 | 39/49 (HT-29, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.614×** | -7.7 | 3e-12 | 33/48 (RKO, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.741×** | -7.0 | 6e-10 | 27/47 (RKO, A549, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.483×** | -6.3 | 6e-08 | 32/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.721×** | -5.4 | 8e-06 | 31/47 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.724×** | -5.3 | 1e-05 | 25/48 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.579×** | -4.7 | 2e-04 | 28/47 (HT-29, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.766×** | -4.4 | 8e-04 | 25/48 (SW480, NCI-H460, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.779×** | -4.1 | 0.003 | 22/48 (BT-474, HEC-1-A, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.783×** | -3.9 | 0.006 | 22/48 (SW 1088, SNU-423, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.793×** | -3.8 | 0.007 | 22/48 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.811×** | -3.4 | 0.027 | 21/48 (BT-474, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.4 | 0.032 | 20/48 (CHP-212, AN3 CA, …) | top dose only | low cells (technical?) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.810×** | -3.3 | 0.034 | 11/48 (PANC-1, H4, …) | top dose only | plate-row cell shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.806×** | -3.3 | 0.039 | 18/47 (A549, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Fumaric acid (drug)]] 5 µM |  | **0.825×** | -3.1 | 0.080 | 7/48 (NCI-H2030, SW1417, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 47.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -14.0) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.339× (z -9.7) |
| [[A-427 (line)]] | wt | 33.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -18.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.249× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 57.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.330× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 59.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -11.5) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.371× (z -10.2) |
| [[RKO (line)]] | wt | 90.0 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0815× (z -23.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 68.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 60.3 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.378× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.178× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 38.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.6) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A-172 (line)]] | wt | 85.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.9) ⚠ cell-cycle shift, explains ~84% of this change |
| [[AN3 CA (line)]] | alt | 39.3 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0750× (z -9.4) ⚠ cell-cycle shift, explains ~4% of this change |
| [[C32 (line)]] | wt | 57.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.313× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 76.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -8.9) ⚠ cell-cycle shift, explains ~84% of this change |
| [[HS-578T (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.2) ⚠ cell-cycle shift, explains ~84% of this change |
| [[LOX-IMVI (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -13.2) ⚠ cell-cycle shift, explains ~84% of this change |
| [[PANC-1 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.2) ⚠ cell-cycle shift, explains ~84% of this change |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.5) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A498 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 59.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUTM2A-AS1]] | +0.74 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[C1orf159]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[NUTM2B-AS1]] | +0.70 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[UGGT2]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[DOCK1]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[HNRNPAB]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[RANBP17]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[RNF32-AS1]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ENOX2]] | +0.62 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[EHMT1]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TTL]] | +0.60 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[LMF1]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBP]] | -0.61 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ZNF14]] | -0.61 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[FAM229B]] | -0.61 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[FRRS1]] | -0.59 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[KBTBD3]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[SNX2]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ATP23]] | -0.56 | -0.31 / -0.62 | both halves | 2e-04 |  |
| [[ORC4]] | -0.55 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[ARRDC3]] | -0.55 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[THAP8]] | -0.54 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[PPDPF]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[KLHL32]] | -0.54 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2B]] | B | TOP2B activity lowers MFSD14CP-1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers MFSD14CP-1's level | compounds that target TOP2A: 2 of 5 raise it (Doxorubicin, Mitoxantrone) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (7.0, -11.4); signed map (10.0, -6.9). **Vector** length 93.8, 22.3% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +0.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.0 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.6 | -7.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.1 | -4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -2.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.3 | -3.9 |

## What is on record

> [!warning] No registry record
> MFSD14CP-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16504); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16504]; `tensor/DDL_lfc|DDL_z.npy` [16504]; `embed/gene_vectors.npy` [16504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16504 or target_col == 16504). Every well: [[MFSD14CP-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD14CP-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

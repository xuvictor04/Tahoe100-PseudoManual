---
symbol: "DHRS11"
type: "gene"
col: 15915
ensembl_id: "ENSG00000278535"
name: "dehydrogenase/reductase 11"
location: "17q12"
module: 6
arm: "+"
pooled_cpm: 4.34
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# DHRS11

*dehydrogenase/reductase 11* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.15× (z +20.6, q 0e+00, up in 37 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Fusidic acid (drug)]] 0.5 µM: 0.762× (z -3.5, q 0.089, down in 6 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDOR1]] (+0.65, fdr 1e-05), [[AKT1]] (+0.64, fdr 7e-06), [[SUV39H2]] (+0.61, fdr 1e-05); moves opposite to [[SEC62]] (-0.63, fdr 7e-06), [[SMIM30]] (-0.61, fdr 4e-05), [[UBE2B]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15915.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.15×** | +20.6 | 0e+00 | 37/39 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.43×** | +10.9 | 5e-25 | 23/34 (NCI-H460, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.09×** | +9.4 | 9e-19 | 15/22 (SW480, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.22×** | +9.4 | 9e-19 | 9/12 (HEC-1-A, A498, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **2.00×** | +8.4 | 4e-15 | 15/26 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.94×** | +8.1 | 5e-14 | 3/6 (NCI-H2030, PANC-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.88×** | +8.0 | 1e-13 | 23/46 (HEC-1-A, A498, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.20× | +7.6 | 3e-12 | 12/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.78×** | +7.3 | 2e-11 | 21/46 (HT-29, LOX-IMVI, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.80×** | +7.2 | 3e-11 | 20/38 (RKO, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.62×** | +6.1 | 5e-08 | 23/46 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +5.0 | 3e-05 | 17/45 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.47×** | +4.9 | 4e-05 | 10/37 (A-172, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.5 | 3e-04 | 10/45 (A-172, HOP62, …) | rises with dose | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.002 | 5/32 (Panc 03.27, RKO, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.007 | 4/45 (NCI-H1573, HEC-1-A, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.63×** | +3.2 | 0.036 | 2/34 (MIA PaCa-2, NCI-H460) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.045 | 4/35 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15915.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fusidic acid (drug)]] 0.5 µM |  | **0.762×** | -3.5 | 0.089 | 6/45 (AN3 CA, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.825×** | -3.5 | 0.089 | 11/45 (KATO III, SNU-1, …) | all doses, stronger at high dose |  |
| [[Bicalutamide (drug)]] 0.5 µM |  | **0.765×** | -3.4 | 0.089 | 10/43 (A-427, Panc 03.27, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.765×** | -3.4 | 0.089 | 9/34 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.776× | -3.2 | 0.14 | 8/42 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15915. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.03 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +8.6) | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.105× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 7.18 | 0 | 2 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0603× (z -11.3) |
| [[A498 (line)]] | wt | 4.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +10.4) | — |
| [[A549 (line)]] | wt | 3.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.99× (z +10.0) | — |
| [[BT-474 (line)]] | alt | 5.85 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.0565× (z -9.7) |
| [[LoVo (line)]] | wt | 2.29 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0737× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 5.53 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0880× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 9.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 3.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +9.9) | — |
| [[A-427 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15915), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDOR1]] | +0.65 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[AKT1]] | +0.64 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[SUV39H2]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PIGW]] | +0.60 | +0.46 / +0.61 | both halves | 2e-05 | STRING 591 |
| [[XRCC3]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PASK]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SLC25A15]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CERS2]] | +0.59 | +0.62 / +0.39 | both halves | 6e-05 |  |
| [[LY6G5B]] | +0.57 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[TOR3A]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[DPAGT1]] | +0.57 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[PCGF2]] | +0.56 | +0.44 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC62]] | -0.63 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[SMIM30]] | -0.61 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[UBE2B]] | -0.58 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[IK]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TTBK2]] | -0.54 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[CTR9]] | -0.54 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[MAP9]] | -0.53 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[AKAP9]] | -0.53 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[PHF3]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[KLF2]] | -0.52 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[TTC3P1]] | -0.52 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[TCAF1]] | -0.52 | -0.36 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DHRS11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.409). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-25.4, -6.4); signed map (-25.3, -42.9). **Vector** length 50.3, 6.05% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +20.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +5.2 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +4.8 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.6 | +9.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.9 | +10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +1.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase/reductase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:36,591,879-36,600,804 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4172, SDR24C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UWP2](https://www.uniprot.org/uniprotkb/Q6UWP2) (Dehydrogenase/reductase SDR family member 11):

> Catalyzes the conversion of the 17-keto group of estrone, 4- and 5-androstenes and 5-alpha-androstanes into their 17-beta-hydroxyl metabolites and the conversion of the 3-keto group of 3-, 3,17- and 3,20- diketosteroids into their 3beta-hydroxyl metabolites. Exhibits reductive 3-beta-hydroxysteroid dehydrogenase activity toward 5-beta-androstanes, 5-beta-pregnanes, 4-pregnenes and bile acids. May contribute to the metabolism of adrenal-derived androgen precursors. Reduces …

**Summary**, from NCBI Gene [79154](https://www.ncbi.nlm.nih.gov/gene/79154):

> Enables 17-beta-hydroxysteroid dehydrogenase (NADP+) activity; 3-beta-hydroxysteroid 3-dehydrogenase (NADP+) activity; and estradiol 17-beta-dehydrogenase [NAD(P)+] activity. Involved in steroid biosynthetic process. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28639](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28639) · Entrez [79154](https://www.ncbi.nlm.nih.gov/gene/79154) · UniProt [Q6UWP2](https://www.uniprot.org/uniprotkb/Q6UWP2) · Ensembl [ENSG00000278535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000278535)

## Data

Gene col 15915: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15915); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15915, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15915]; `tensor/DDL_lfc|DDL_z.npy` [15915]; `embed/gene_vectors.npy` [15915]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15915 or target_col == 15915). Every well: [[DHRS11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRS11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

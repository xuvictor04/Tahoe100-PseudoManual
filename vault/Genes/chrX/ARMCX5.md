---
symbol: "ARMCX5"
type: "gene"
col: 4697
ensembl_id: "ENSG00000125962"
name: "armadillo repeat containing X-linked 5"
location: "Xq22.1"
module: 28
arm: "+"
pooled_cpm: 8.12
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ARMCX5

*armadillo repeat containing X-linked 5* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.43× (z +7.9, q 1e-12, up in 24 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.488× (z -15.9, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNC]] (+0.68, fdr 7e-06), [[ZNF780A]] (+0.68, fdr 7e-06), [[THUMPD2]] (+0.65, fdr 1e-05); moves opposite to [[KIAA2026]] (-0.54, fdr 2e-05), [[CD9]] (-0.54, fdr 3e-05), [[CORO7]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4697.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +7.9 | 1e-12 | 24/43 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +7.9 | 1e-12 | 19/42 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +5.6 | 4e-06 | 18/45 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +5.5 | 4e-06 | 10/48 (Panc 03.27, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.1 | 0.006 | 7/47 (A-427, NCI-H2347, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.008 | 4/40 (AsPC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.030 | 12/46 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.031 | 8/40 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.031 | 4/39 (SK-MEL-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.032 | 7/47 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.4 | 0.032 | 2/48 (MIA PaCa-2, AsPC-1) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.24×** | +3.3 | 0.043 | 10/38 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.23×** | +3.2 | 0.063 | 5/45 (SW480, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4697.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.488×** | -15.9 | 0e+00 | 42/44 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.585×** | -8.4 | 1e-14 | 24/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.636×** | -7.1 | 2e-10 | 22/46 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.712×** | -5.3 | 1e-05 | 16/47 (COLO 205, SW480, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.576×** | -4.5 | 7e-04 | 12/46 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.777×** | -3.8 | 0.012 | 14/44 (NCI-H23, RKO, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.779×** | -3.8 | 0.012 | 14/45 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.779×** | -3.8 | 0.012 | 14/45 (SW48, HOP62, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.849× | -3.6 | 0.017 | 13/48 (H4, BT-474, …) | rises with dose |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **0.799×** | -3.3 | 0.060 | 10/40 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.813×** | -3.2 | 0.060 | 3/47 (SW48, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 9.67 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0664× (z -13.4) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0837× (z -10.5) |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 16.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 9.55 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -10.2) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H460 (line)]] | wt | 9.65 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 7.52 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -9.9) |
| [[SHP-77 (line)]] | alt | 7.84 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.126× (z -8.7) |
| [[A-172 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNC]] | +0.68 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ZNF780A]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[THUMPD2]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[ZSCAN12]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ZNF182]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[FUNDC1]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MMADHC]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ZFP37]] | +0.63 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[RNFT1]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ZNF317]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[NUDT12]] | +0.62 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[CCDC43]] | +0.62 | +0.57 / +0.59 | both halves | 9e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA2026]] | -0.54 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[CD9]] | -0.54 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[CORO7]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[SMG1P5]] | -0.53 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[KPNB1-DT]] | -0.53 | -0.27 / -0.58 | both halves | 3e-04 |  |
| [[MAPKAPK2]] | -0.53 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[CD81]] | -0.52 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[CTBP2]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[FOXK2]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[CASTOR3P]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TMBIM6]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[SRGAP2C]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARMCX5's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-31.4, 8.8); signed map (2.2, -25.8). **Vector** length 63.3, 9.06% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.5 | +3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -15.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.8 | -3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -2.5 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing X-linked 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:102,599,168-102,604,159 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12969, GASP5 |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

UniProt [Q6P1M9](https://www.uniprot.org/uniprotkb/Q6P1M9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25772) · Entrez [64860](https://www.ncbi.nlm.nih.gov/gene/64860) · UniProt [Q6P1M9](https://www.uniprot.org/uniprotkb/Q6P1M9) · Ensembl [ENSG00000125962](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125962)

## Data

Gene col 4697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4697); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4697]; `tensor/DDL_lfc|DDL_z.npy` [4697]; `embed/gene_vectors.npy` [4697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4697 or target_col == 4697). Every well: [[ARMCX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMCX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

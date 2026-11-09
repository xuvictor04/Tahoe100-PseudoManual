---
symbol: "CSAD"
type: "gene"
col: 6325
ensembl_id: "ENSG00000139631"
name: "cysteine sulfinic acid decarboxylase"
location: "12q13.13"
module: 21
arm: "+"
pooled_cpm: 22.06
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CSAD

*cysteine sulfinic acid decarboxylase* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.20× (z +17.0, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.484× (z -5.8, q 4e-06, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM229A]] (+0.56, fdr 3e-05), [[FAM219B]] (+0.55, fdr 3e-05), [[CCNL2]] (+0.54, fdr 3e-05); moves opposite to [[ZKSCAN2]] (-0.49, fdr 5e-05), [[HMBS]] (-0.48, fdr 6e-05), [[PCBP1]] (-0.47, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6325.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +17.0 | 0e+00 | 42/47 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +6.4 | 5e-08 | 20/34 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +5.5 | 6e-06 | 25/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 2e-04 | 19/48 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.6 | 4e-04 | 20/46 (Panc 03.27, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.5 | 8e-04 | 17/42 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.22×** | +4.2 | 0.002 | 19/48 (A498, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.004 | 12/43 (LS 180, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.048 | 6/46 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.24×** | +3.3 | 0.052 | 14/48 (RKO, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.24×** | +3.2 | 0.084 | 14/41 (KATO III, LS 180, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.094 | 9/46 (SW48, HepG2/C3A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.095 | 14/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6325.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -5.8 | 4e-06 | 33/49 (LoVo, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.581×** | -4.3 | 0.003 | 22/46 (HS-578T, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.754×** | -4.3 | 0.003 | 19/46 (NCI-H2030, AN3 CA, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.774×** | -3.7 | 0.030 | 19/47 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.794×** | -3.4 | 0.074 | 20/47 (RPMI-7951, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.817× | -3.1 | 0.15 | 15/48 (hTERT-HPNE, SW480, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.811× | -3.1 | 0.15 | 9/47 (NCI-H23, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.821× | -3.0 | 0.15 | 14/48 (SW480, SW1417, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.821× | -3.0 | 0.15 | 15/47 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.687× | -3.0 | 0.15 | 8/45 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.4) | [[Belinostat (drug)]] 0.5 µM 0.304× (z -9.1) ⚠ cell-cycle shift, explains ~23% of this change |
| [[LS 180 (line)]] | wt | 29.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.0) | — |
| [[A498 (line)]] | wt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +10.8) | — |
| [[A549 (line)]] | wt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 31.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 40.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.305× (z -8.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0524× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 9.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +11.1) | — |
| [[KATO III (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.235× (z -10.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.231× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 8.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 23.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +11.4) | — |
| [[SW48 (line)]] | wt | 18.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +8.9) | — |
| [[A-427 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM229A]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[FAM219B]] | +0.55 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[CCNL2]] | +0.54 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[TMEM219]] | +0.53 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[TMEM134]] | +0.52 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[EOGT-DT]] | +0.52 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[STXBP2]] | +0.52 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[ATP6AP2]] | +0.51 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[URM1]] | +0.51 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[WDR20]] | +0.50 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[ENY2]] | +0.50 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[NDUFV1]] | +0.50 | +0.55 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN2]] | -0.49 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[HMBS]] | -0.48 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[PCBP1]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CCT2]] | -0.46 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[FIBP]] | -0.46 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[SERBP1]] | -0.46 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[WDR7]] | -0.46 | -0.32 / -0.33 | both halves | 1e-04 |  |
| [[CBR1]] | -0.46 | -0.32 / -0.45 | both halves | 2e-04 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[RGS19]] | -0.46 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[POP4]] | -0.46 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[THUMPD3]] | -0.45 | -0.36 / -0.57 | both halves | 1e-04 |  |
| [[TRMT10C]] | -0.45 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CSAD's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.404). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.6, -20.4); signed map (3.9, -4.9). **Vector** length 80.9, 15.4% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +6.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +4.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.5 | +1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +1.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.2 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.5 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -2.8 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.6 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cysteine sulfinic acid decarboxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,157,663-53,180,925 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSADC, PCAP, CSD |
| Gene groups (HGNC) | Decarboxylases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 3 pathways, smallest: Degradation of cysteine and homocysteine; Sulfur amino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y600](https://www.uniprot.org/uniprotkb/Q9Y600) (Cysteine sulfinic acid decarboxylase):

> Catalyzes the decarboxylation of L-aspartate, 3-sulfino-L-alanine (cysteine sulfinic acid), and L-cysteate to beta-alanine, hypotaurine and taurine, respectively. The preferred substrate is 3-sulfino-L-alanine. Does not exhibit any decarboxylation activity toward glutamate.

**Summary**, from NCBI Gene [51380](https://www.ncbi.nlm.nih.gov/gene/51380):

> This gene encodes a member of the group 2 decarboxylase family. A similar protein in rodents plays a role in multiple biological processes as the rate-limiting enzyme in taurine biosynthesis, catalyzing the decarboxylation of cysteinesulfinate to hypotaurine. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:18966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18966) · Entrez [51380](https://www.ncbi.nlm.nih.gov/gene/51380) · UniProt [Q9Y600](https://www.uniprot.org/uniprotkb/Q9Y600) · Ensembl [ENSG00000139631](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139631)

## Data

Gene col 6325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6325); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6325]; `tensor/DDL_lfc|DDL_z.npy` [6325]; `embed/gene_vectors.npy` [6325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6325 or target_col == 6325). Every well: [[CSAD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSAD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

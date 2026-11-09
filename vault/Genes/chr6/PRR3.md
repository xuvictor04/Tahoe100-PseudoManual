---
symbol: "PRR3"
type: "gene"
col: 12893
ensembl_id: "ENSG00000204576"
name: "proline rich 3"
location: "6p21.33"
module: 10
arm: "+"
pooled_cpm: 10.01
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# PRR3

*proline rich 3* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.71× (z +20.9, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.504× (z -10.3, q 2e-22, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (70 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 30 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNISR-AS1]] (+0.68, fdr 1e-05), [[VPS52]] (+0.67, fdr 4e-04), [[DUS2]] (+0.67, fdr 1e-05); moves opposite to [[UNC13B]] (-0.63, fdr 6e-05), [[LLGL2]] (-0.62, fdr 2e-04), [[CABLES2]] (-0.56, fdr 0.005, ⚠ one half only (not replicated)), [[MAPK8]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12893.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +20.9 | 0e+00 | 41/46 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +8.9 | 1e-16 | 31/46 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.2 | 1e-10 | 24/48 (HOP62, Hs 766T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.28×** | +6.5 | 9e-09 | 18/47 (J82, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +6.2 | 7e-08 | 24/47 (SHP-77, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +5.3 | 1e-05 | 21/47 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.8 | 1e-04 | 10/28 (A498, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +4.6 | 3e-04 | 11/43 (HOP62, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.24×** | +4.5 | 5e-04 | 17/48 (AsPC-1, J82, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +4.4 | 7e-04 | 10/47 (NCI-H1792, PANC-1, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.3 | 9e-04 | 15/46 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.001 | 10/47 (HOP62, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.011 | 13/47 (BT-474, LoVo, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.23×** | +3.2 | 0.057 | 10/46 (A-172, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12893.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.504×** | -10.3 | 2e-22 | 38/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -10.1 | 1e-21 | 34/46 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -5.1 | 6e-05 | 19/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.718×** | -5.0 | 9e-05 | 17/46 (SW48, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.694×** | -4.8 | 1e-04 | 17/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.740×** | -4.5 | 5e-04 | 11/45 (NCI-H23, Hs 766T, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.741×** | -4.5 | 5e-04 | 8/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.780×** | -3.6 | 0.023 | 12/47 (COLO 205, SW 1271, …) | all doses, stronger at high dose |  |
| [[Simotinib (drug)]] 0.05 µM |  | **0.794×** | -3.2 | 0.082 | 11/46 (NCI-H661, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.812×** | -3.1 | 0.099 | 6/47 (COLO 205, J82, …) | two highest doses |  |
| [[Rifaximin (drug)]] 0.05 µM |  | 0.802× | -3.1 | 0.11 | 11/46 (AN3 CA, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.1 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.192× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 7.93 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.0) | [[Docetaxel (drug)]] 0.05 µM 0.175× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~78% of this change |
| [[SNU-423 (line)]] | alt | 9.22 | 0 | 2 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0840× (z -11.3) |
| [[SW480 (line)]] | alt | 10.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~3% of this change |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.108× (z -9.8) |
| [[HCT15 (line)]] | alt | 16.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0868× (z -11.2) |
| [[HOP62 (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 8.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 5.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +8.6) | — |
| [[LoVo (line)]] | wt | 8.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 8.13 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0581× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 7.34 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -8.8) |
| [[SW48 (line)]] | wt | 12.6 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0841× (z -9.0) |
| [[A-172 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 27 of them with an alert (⚠; 27 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR-AS1]] | +0.68 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[VPS52]] | +0.67 | +0.70 / +0.25 | both halves | 4e-04 |  |
| [[DUS2]] | +0.67 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[GTF3C4]] | +0.67 | +0.72 / +0.34 | both halves | 1e-04 |  |
| [[HIKESHI]] | +0.65 | +0.68 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[THBS4]] | +0.65 | +0.61 / +0.37 | both halves | 9e-05 |  |
| [[ZBTB2]] | +0.65 | +0.59 / +0.37 | both halves | 7e-05 |  |
| [[MAIP1]] | +0.65 | +0.57 / +0.37 | both halves | 9e-05 |  |
| [[TIMM8B]] | +0.64 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[PSMC2]] | +0.62 | +0.57 / +0.29 | both halves | 3e-04 |  |
| [[CTBP1-DT]] | +0.62 | +0.57 / +0.28 | both halves | 3e-04 |  |
| [[ZNF189]] | +0.62 | +0.62 / +0.27 | both halves | 3e-04 |  |
| [[ZNF407-AS1]] | +0.62 | +0.68 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC13B]] | -0.63 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[LLGL2]] | -0.62 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[CABLES2]] | -0.56 | -0.52 / -0.05 | ⚠ one half (not replicated) | 0.005 |  |
| [[MAPK8]] | -0.56 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[GNAI2]] | -0.56 | -0.49 / -0.12 | ⚠ not reproduced | 0.002 |  |
| [[ACTG1]] | -0.55 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[USP2]] | -0.54 | -0.30 / -0.29 | both halves | 3e-04 |  |
| [[PPP1CC]] | -0.53 | -0.40 / -0.19 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRR3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-3.6, 10.6); signed map (21.2, -23.2). **Vector** length 69.9, 11.3% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +20.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +4.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +2.8 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -10.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.1 | -10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | +1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,557,280-30,563,723 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAT56, Em:AB014077.1, Em:AB023052.2 |
| Gene groups (HGNC) | Zinc fingers CCCH-type |
| Matched by | ensembl_id |

UniProt [P79522](https://www.uniprot.org/uniprotkb/P79522) carries no function annotation.

**Summary**, from NCBI Gene [80742](https://www.ncbi.nlm.nih.gov/gene/80742):

> Enables RNA binding activity. Predicted to be involved in positive regulation of termination of RNA polymerase II transcription, poly(A)-coupled. Predicted to be part of PTW/PP1 phosphatase complex. Predicted to be active in chromatin. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21149) · Entrez [80742](https://www.ncbi.nlm.nih.gov/gene/80742) · UniProt [P79522](https://www.uniprot.org/uniprotkb/P79522) · Ensembl [ENSG00000204576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204576)

## Data

Gene col 12893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12893); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12893]; `tensor/DDL_lfc|DDL_z.npy` [12893]; `embed/gene_vectors.npy` [12893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12893 or target_col == 12893). Every well: [[PRR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

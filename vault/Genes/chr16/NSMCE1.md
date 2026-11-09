---
symbol: "NSMCE1"
type: "gene"
col: 9769
ensembl_id: "ENSG00000169189"
name: "NSE1 component of SMC5/6 complex"
location: "16p12.1"
module: 28
arm: "+"
pooled_cpm: 20.37
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# NSMCE1

*NSE1 component of SMC5/6 complex* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.42× (z +11.7, q 9e-29, up in 38 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.37× (z +4.0, q 0.009, up in 17 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.431× (z -11.1, q 5e-26, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS33]] (+0.67, fdr 7e-06), [[EBAG9]] (+0.66, fdr 8e-06), [[COQ5]] (+0.66, fdr 7e-06); moves opposite to [[SMG1P5]] (-0.54, fdr 1e-05), [[RAD9A]] (-0.53, fdr 5e-05), [[ASB16-AS1]] (-0.52, fdr 5e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +11.7 | 9e-29 | 38/42 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +10.3 | 2e-22 | 28/31 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +4.7 | 5e-04 | 19/33 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.009 | 17/48 (NCI-H1792, NCI-H1573, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.012 | 19/45 (RPMI-7951, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.33×** | +3.8 | 0.014 | 19/44 (SW480, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.32×** | +3.7 | 0.017 | 21/47 (A-172, NCI-H1573, …) | all doses, flat |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.040 | 12/47 (NCI-H460, J82, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.20×** | +3.4 | 0.040 | 13/48 (A498, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.088 | 11/48 (HEC-1-A, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9769.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.431×** | -11.1 | 5e-26 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.471×** | -10.0 | 7e-21 | 44/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.479×** | -9.7 | 5e-20 | 38/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.563×** | -7.6 | 5e-12 | 35/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.593×** | -6.9 | 6e-10 | 32/46 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.640×** | -5.6 | 2e-06 | 26/47 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.778×** | -4.7 | 2e-04 | 27/47 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.731×** | -4.1 | 0.003 | 20/46 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.554×** | -4.0 | 0.003 | 19/39 (J82, SW 900, …) | all doses, flat | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.739×** | -4.0 | 0.004 | 16/48 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.772×** | -3.4 | 0.033 | 20/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.707×** | -3.1 | 0.099 | 9/48 (PANC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.8 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -11.9) |
| [[A-427 (line)]] | wt | 23.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -12.4) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.278× (z -9.1) |
| [[A498 (line)]] | wt | 27.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 2 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0684× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Silodosin (drug)]] 5 µM 0.0809× (z -9.2) |
| [[J82 (line)]] | alt | 18.9 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0769× (z -9.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 17.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +9.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.05 µM 0.188× (z -9.4) |
| [[A-172 (line)]] | wt | 21.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -8.5) |
| [[H4 (line)]] | wt | 13.7 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0729× (z -9.5) |
| [[KATO III (line)]] | alt | 5.96 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.118× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 14.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +8.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 21.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.340× (z -8.9) |
| [[SHP-77 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 20.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -10.6) |
| [[A549 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS33]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.66 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[COQ5]] | +0.66 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[CEP63]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[CCDC25]] | +0.63 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[CETN3]] | +0.63 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[FAM114A2]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SLX4IP]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[DARS1]] | +0.61 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[POLI]] | +0.60 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[HMG20A]] | +0.60 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[UROS]] | +0.60 | +0.65 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P5]] | -0.54 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[RAD9A]] | -0.53 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[ASB16-AS1]] | -0.52 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[DIP2A]] | -0.49 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[SANBR]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[RNF38]] | -0.48 | -0.59 / -0.38 | both halves | 7e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises NSMCE1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.3, 3.8); signed map (6.4, -24.8). **Vector** length 63.7, 11.4% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +4.6 | +3.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.0 | -7.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.9 | -10.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -9.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.7 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | -0.9 | +0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | NSE1 component of SMC5/6 complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:27,224,994-27,268,772 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NSE1 |
| Gene groups (HGNC) | Ring finger proteins; SMC5/6 complex; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: SUMOylation of DNA damage response and repair proteins; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WV22](https://www.uniprot.org/uniprotkb/Q8WV22) (Non-structural maintenance of chromosomes element 1 homolog):

> RING-type zinc finger-containing E3 ubiquitin ligase that assembles with melanoma antigen protein (MAGE) to catalyze the direct transfer of ubiquitin from E2 ubiquitin-conjugating enzyme to a specific substrate. Within MAGE-RING ubiquitin ligase complex, MAGE stimulates and specifies ubiquitin ligase activity likely through recruitment and/or stabilization of the E2 ubiquitin-conjugating enzyme at the E3:substrate complex. Involved in maintenance of genome integrity, DNA damage response and DNA …

**Summary**, from NCBI Gene [197370](https://www.ncbi.nlm.nih.gov/gene/197370):

> Enables protein dimerization activity and ubiquitin protein ligase activity. Involved in DNA damage response. Located in nucleoplasm. Part of Smc5-Smc6 complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29897) · Entrez [197370](https://www.ncbi.nlm.nih.gov/gene/197370) · UniProt [Q8WV22](https://www.uniprot.org/uniprotkb/Q8WV22) · Ensembl [ENSG00000169189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169189)

## Data

Gene col 9769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9769); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9769]; `tensor/DDL_lfc|DDL_z.npy` [9769]; `embed/gene_vectors.npy` [9769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9769 or target_col == 9769). Every well: [[NSMCE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSMCE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

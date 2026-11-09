---
symbol: "FCSK"
type: "gene"
col: 8063
ensembl_id: "ENSG00000157353"
name: "fucose kinase"
location: "16q22.1"
module: 17
arm: "+"
pooled_cpm: 5.87
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# FCSK

*fucose kinase* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.43× (z +5.3, q 5e-05, up in 6 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.32× (z +4.1, q 0.006, up in 9 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.469× (z -11.2, q 2e-26, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAB1]] (+0.63, fdr 1e-05), [[FAM133B]] (+0.62, fdr 1e-05), [[COG2]] (+0.61, fdr 3e-05); moves opposite to [[CCNT2-AS1]] (-0.54, fdr 3e-04), [[CCDC168]] (-0.53, fdr 8e-05), [[LINC02798]] (-0.53, fdr 9e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8063.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +5.3 | 5e-05 | 6/27 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.7 | 6e-04 | 7/14 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +4.1 | 0.006 | 9/47 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +4.1 | 0.006 | 12/47 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.0 | 0.006 | 4/10 (CFPAC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.026 | 6/31 (SHP-77, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.026 | 10/40 (HEC-1-A, BT-474, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.026 | 11/46 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.5 | 0.028 | 2/14 (PANC-1, LoVo) | top dose only | noisy plate (z scaled) |
| [[Menadione (drug)]] 0.05 µM |  | 1.25× | +3.1 | 0.12 | 5/39 (C-33 A, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8063.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.469×** | -11.2 | 2e-26 | 29/47 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.589×** | -7.9 | 1e-12 | 18/39 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.594×** | -7.7 | 2e-12 | 25/45 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -6.4 | 2e-08 | 18/40 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -5.9 | 3e-07 | 20/41 (A-172, RKO, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.767×** | -5.6 | 2e-06 | 15/47 (A-172, COLO 205, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.706×** | -5.2 | 2e-05 | 9/46 (A549, SW 1271, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -5.1 | 2e-05 | 15/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.732×** | -4.6 | 2e-04 | 17/45 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -4.4 | 5e-04 | 13/36 (Panc 03.27, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.576×** | -4.3 | 9e-04 | 12/43 (SHP-77, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.782×** | -3.7 | 0.012 | 7/44 (NCI-H661, HS-578T, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.786×** | -3.6 | 0.016 | 7/43 (LoVo, NCI-H2030, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.635×** | -3.5 | 0.017 | 5/36 (SW 900, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.797×** | -3.4 | 0.028 | 12/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.668×** | -3.1 | 0.061 | 7/40 (Panc 03.27, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.19 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0641× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -10.2) |
| [[A-172 (line)]] | wt | 16.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0756× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -11.4) |
| [[C-33 A (line)]] | alt | 8.24 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0753× (z -9.8) |
| [[BT-474 (line)]] | alt | 9.44 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0922× (z -10.4) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 5.64 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 3.60 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0481× (z -11.8) |
| [[LoVo (line)]] | wt | 5.54 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.161× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 4.52 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 4.15 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0919× (z -8.6) |
| [[PANC-1 (line)]] | alt | 5.32 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.301× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 6.51 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -10.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 6.01 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0540× (z -8.5) |
| [[A-427 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAB1]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[FAM133B]] | +0.62 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[COG2]] | +0.61 | +0.57 / +0.45 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[TTC38]] | +0.60 | +0.37 / +0.59 | both halves | 9e-05 |  |
| [[MRPS31P4]] | +0.59 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ZNF30]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[WDR11]] | +0.59 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[IRAK1BP1]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[QDPR]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SLC25A12]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[EHMT2]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[TAFAZZIN]] | +0.57 | +0.46 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNT2-AS1]] | -0.54 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[CCDC168]] | -0.53 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[LINC02798]] | -0.53 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[TICAM2]] | -0.52 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[HCG18]] | -0.52 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[MCF2]] | -0.52 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[RAB22A]] | -0.51 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[SLC25A53]] | -0.51 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[PXDNL]] | -0.50 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[PDK1-AS1]] | -0.50 | -0.37 / -0.42 | both halves | 7e-05 |  |
| [[TEX21P]] | -0.49 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[LINC01588]] | -0.49 | -0.35 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FCSK's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers FCSK's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.1, -3.4); signed map (-24.1, -14.4). **Vector** length 50.3, 5.88% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.8 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.2 | +4.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.0 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | fucose kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:70,454,595-70,480,274 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39408; previously FUK |
| Gene groups (HGNC) | Carbohydrate kinases |
| Reactome | 4 pathways, smallest: GDP-fucose biosynthesis; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N0W3](https://www.uniprot.org/uniprotkb/Q8N0W3) (L-fucose kinase):

> Takes part in the salvage pathway for reutilization of fucose from the degradation of oligosaccharides.

**Summary**, from NCBI Gene [197258](https://www.ncbi.nlm.nih.gov/gene/197258):

> The protein encoded by this gene belongs to the GHMP (galacto-, homoserine, mevalonate and phosphomevalonate) kinase family and catalyzes the phosphorylation of L-fucose to form beta-L-fucose 1-phosphate. This enzyme catalyzes the first step in the utilization of free L-fucose in glycoprotein and glycolipid synthesis. L-fucose may be important in mediating a number of cell-cell interactions such as blood group antigen recognition, inflammation, and metastatis. While several transcript variants …

**Accessions** — [HGNC:29500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29500) · Entrez [197258](https://www.ncbi.nlm.nih.gov/gene/197258) · UniProt [Q8N0W3](https://www.uniprot.org/uniprotkb/Q8N0W3) · Ensembl [ENSG00000157353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157353)

## Data

Gene col 8063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8063); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8063]; `tensor/DDL_lfc|DDL_z.npy` [8063]; `embed/gene_vectors.npy` [8063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8063 or target_col == 8063). Every well: [[FCSK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FCSK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "TMEM79"
type: "gene"
col: 8696
ensembl_id: "ENSG00000163472"
name: "transmembrane protein 79"
location: "1q22"
module: 89
arm: "+"
pooled_cpm: 4.19
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# TMEM79

*transmembrane protein 79* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.77× (z +17.8, q 0e+00, up in 30 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-172 0.140×, PANC-1 0.214×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0984×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Naproxen (drug)]] 0.05 µM in 1 line (J82 0.0738×); [[Aprepitant (drug)]] 0.05 µM in 1 line (NCI-H2030 0.127×); [[Acetazolamide (drug)]] 0.5 µM in 1 line (LoVo 0.0772×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC4A1AP]] (+0.70, fdr 7e-06), [[ALKBH4]] (+0.69, fdr 8e-06), [[MTRFR]] (+0.67, fdr 7e-06); moves opposite to [[MAPK8]] (-0.58, fdr 3e-05), [[RSU1]] (-0.55, fdr 1e-04), [[UNC13B]] (-0.55, fdr 5e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.77×** | +17.8 | 0e+00 | 30/36 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +14.3 | 6e-44 | 33/37 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.66×** | +12.1 | 2e-31 | 34/43 (NCI-H460, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +8.8 | 1e-16 | 16/26 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +7.4 | 2e-11 | 20/35 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.82×** | +7.0 | 2e-10 | 20/42 (A498, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.71×** | +6.4 | 1e-08 | 19/34 (PANC-1, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.67×** | +6.3 | 2e-08 | 15/35 (A-172, Panc 03.27, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +6.1 | 6e-08 | 17/41 (NCI-H23, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.1 | 6e-08 | 12/47 (NCI-H2030, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.61×** | +5.9 | 2e-07 | 17/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +5.5 | 2e-06 | 19/42 (KATO III, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.57×** | +5.4 | 3e-06 | 12/39 (HEC-1-A, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.53×** | +5.2 | 7e-06 | 10/46 (LoVo, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.49×** | +4.9 | 3e-05 | 16/47 (NCI-H23, Hs 766T, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +4.2 | 7e-04 | 13/37 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.005 | 7/42 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.017 | 5/44 (NCI-H23, J82, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.020 | 1/32 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.023 | 1/45 (NCI-H460) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.030 | 6/45 (NCI-H1573, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8696.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A-172 0.140×, PANC-1 0.214×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0984×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Naproxen (drug)]] 0.05 µM in 1 line (J82 0.0738×); [[Aprepitant (drug)]] 0.05 µM in 1 line (NCI-H2030 0.127×); [[Acetazolamide (drug)]] 0.5 µM in 1 line (LoVo 0.0772×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.5 | 0.25 | 12/48 (A549, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.21 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.139× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[C32 (line)]] | wt | 5.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 97.9× (z +20.6) | — |
| [[LoVo (line)]] | wt | 2.18 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +10.1) | [[Acetazolamide (drug)]] 0.5 µM 0.0772× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 4.73 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +9.1) | [[Aprepitant (drug)]] 0.05 µM 0.127× (z -8.7) |
| [[A-172 (line)]] | wt | 9.07 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 5.62 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0984× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 3.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 2.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +11.2) | — |
| [[hTERT-HPNE (line)]] | wt | 2.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +9.1) | — |
| [[J82 (line)]] | alt | 4.34 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0738× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 2.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 4.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 8.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 5.45 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 3.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +10.9) | — |
| [[A-427 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC4A1AP]] | +0.70 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ALKBH4]] | +0.69 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[MTRFR]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TTF1]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ZNF653]] | +0.65 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[COA6]] | +0.64 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[TIRAP]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SLC25A17]] | +0.63 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SART3]] | +0.62 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[TBP]] | +0.62 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.62 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[RPAP1]] | +0.61 | +0.60 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK8]] | -0.58 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[RSU1]] | -0.55 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[UNC13B]] | -0.55 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[TTLL12]] | -0.55 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[MED14]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[APEH]] | -0.50 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM79's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF675]] | B | ZNF675 activity raises TMEM79's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.38× lower at baseline in the lines without ZNF675 | 0.082 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.5, 6.6); signed map (-7.5, -11.3). **Vector** length 53.0, 6.80% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.8 | +12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +17.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +14.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.9 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +4.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.4 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.2 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -1.8 | +5.2 |
|  | [[Folic acid (drug)]] 5 µM |  | -0.8 | -0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.8 | -0.7 |
|  | [[Pimozide (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[8-Hydroxyquinoline (drug)]] 5 µM |  | -0.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 79 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,282,935-156,293,185 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13102, FLJ16057, FLJ32254, MATT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSE2](https://www.uniprot.org/uniprotkb/Q9BSE2) (Transmembrane protein 79):

> Contributes to the epidermal integrity and skin barrier function. Plays a role in the lamellar granule (LG) secretory system and in the stratum corneum (SC) epithelial cell formation (By similarity).

**Summary**, from NCBI Gene [84283](https://www.ncbi.nlm.nih.gov/gene/84283):

> Enables identical protein binding activity. Predicted to be involved in several processes, including epithelial cell maturation; establishment of skin barrier; and positive regulation of epidermis development. Predicted to act upstream of or within cornification; cuticle development; and hair follicle morphogenesis. Predicted to be located in Golgi apparatus; lysosome; and membrane. Predicted to be active in lysosomal membrane and trans-Golgi network membrane. [provided by Alliance of Genome …

**Accessions** — [HGNC:28196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28196) · Entrez [84283](https://www.ncbi.nlm.nih.gov/gene/84283) · UniProt [Q9BSE2](https://www.uniprot.org/uniprotkb/Q9BSE2) · Ensembl [ENSG00000163472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163472)

## Data

Gene col 8696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8696); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8696]; `tensor/DDL_lfc|DDL_z.npy` [8696]; `embed/gene_vectors.npy` [8696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8696 or target_col == 8696). Every well: [[TMEM79 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM79.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

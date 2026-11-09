---
symbol: "SLC2A8"
type: "gene"
col: 5919
ensembl_id: "ENSG00000136856"
name: "solute carrier family 2 member 8"
location: "9q33.3"
module: 2
arm: "+"
pooled_cpm: 4.34
n_lines_expressing: 49
n_dd_up: 38
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SLC2A8

*solute carrier family 2 member 8* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.64× (z +16.9, q 0e+00, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.519× (z -4.5, q 0.004, down in 11 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Furosemide (drug)]] 0.05 µM in 1 line (SHP-77 0.0715×); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H460 0.0710×); [[Peretinoin (drug)]] 5 µM in 1 line (Panc 03.27 0.0610×).
> Its strongest partners by |cos| (69 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 31 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFYVE21]] (+0.62, fdr 3e-04), [[TP53I13]] (+0.62, fdr 1e-04), [[FAM3A]] (+0.60, fdr 3e-05); moves opposite to [[ZNF780B]] (-0.46, fdr 0.004, ⚠ not reproduced), [[TRIM44]] (-0.42, fdr 0.002, ⚠ not reproduced), [[NAB1]] (-0.42, fdr 7e-04), [[CDK6]] (-0.42, fdr 4e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.64×** | +16.9 | 0e+00 | 40/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.37×** | +15.8 | 0e+00 | 36/45 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +15.6 | 0e+00 | 29/34 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.63×** | +12.6 | 2e-34 | 37/46 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +12.2 | 3e-32 | 21/36 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +7.3 | 2e-11 | 16/35 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **2.80×** | +7.0 | 2e-10 | 10/25 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +6.8 | 6e-10 | 19/46 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.71×** | +6.7 | 1e-09 | 19/37 (NCI-H460, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +6.0 | 1e-07 | 17/46 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **1.61×** | +6.0 | 1e-07 | 1/9 (SNU-423) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.57×** | +5.7 | 6e-07 | 13/33 (NCI-H460, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.53×** | +5.4 | 3e-06 | 10/24 (A498, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +5.1 | 1e-05 | 10/37 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +4.9 | 4e-05 | 5/45 (LoVo, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 5e-04 | 10/43 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.3 | 5e-04 | 11/46 (A549, NCI-H460, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.001 | 7/38 (J82, HOP62, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.76×** | +3.8 | 0.003 | 5/34 (PANC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.029 | 1/21 (KATO III) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.036 | 9/35 (A-172, NCI-H1573, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5919.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Furosemide (drug)]] 0.05 µM in 1 line (SHP-77 0.0715×); [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H460 0.0710×); [[Peretinoin (drug)]] 5 µM in 1 line (Panc 03.27 0.0610×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.519×** | -4.5 | 0.004 | 11/40 (Panc 03.27, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.527×** | -4.3 | 0.004 | 15/34 (SNU-423, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -3.3 | 0.21 | 6/45 (LoVo, BT-474, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.790× | -3.0 | 0.33 | 6/34 (SHP-77, Panc 03.27, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.42 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 2.40 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.33× (z +11.7) | [[Verteporfin (drug)]] 5 µM 0.0710× (z -9.8) |
| [[SW1417 (line)]] | alt | 15.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[A498 (line)]] | wt | 5.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 4.15 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0610× (z -9.4) |
| [[SHP-77 (line)]] | alt | 6.09 | 0 | 1 | — | [[Furosemide (drug)]] 0.05 µM 0.0715× (z -10.5) |
| [[A-427 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 28 of them with an alert (⚠; 28 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE21]] | +0.62 | +0.28 / +0.68 | both halves | 3e-04 |  |
| [[TP53I13]] | +0.62 | +0.33 / +0.67 | both halves | 1e-04 |  |
| [[FAM3A]] | +0.60 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[GSK3A]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[GIT1]] | +0.58 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[RPS6KB2]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ADCK5]] | +0.56 | +0.31 / +0.56 | both halves | 2e-04 |  |
| [[RFNG]] | +0.56 | +0.30 / +0.60 | both halves | 2e-04 |  |
| [[RUSC1]] | +0.55 | +0.14 / +0.65 | ⚠ one half (not replicated) | 0.002 |  |
| [[RCE1]] | +0.53 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[PKD1]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[DGAT1]] | +0.52 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[MIIP]] | +0.51 | +0.26 / +0.58 | both halves | 3e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF780B]] | -0.46 | -0.06 / -0.42 | ⚠ not reproduced | 0.004 |  |
| [[TRIM44]] | -0.42 | -0.13 / -0.49 | ⚠ not reproduced | 0.002 |  |
| [[NAB1]] | -0.42 | -0.21 / -0.48 | both halves | 7e-04 |  |
| [[CDK6]] | -0.42 | -0.26 / -0.50 | both halves | 4e-04 |  |
| [[ZNF221]] | -0.41 | -0.17 / -0.40 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC2A8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.433). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.2, -20.3); signed map (-24.4, 1.7). **Vector** length 46.7, 5.40% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +15.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.3 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.0 | +16.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.7 | +15.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.6 | +7.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.8 | -4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 2 member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:127,397,138-127,408,424 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GLUTX1, GLUT8 |
| Gene groups (HGNC) | Solute carrier family 2 |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 7 pathways, smallest: Cellular hexose transport; Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NY64](https://www.uniprot.org/uniprotkb/Q9NY64) (Solute carrier family 2, facilitated glucose transporter member 8):

> Insulin-regulated facilitative hexose transporter that mediates the transport of glucose and fructose (By similarity). Facilitates hepatic influx of dietary trehalose, which in turn inhibits glucose and fructose influx triggering a starvation signal and hepatic autophagy through activation of AMPK and ULK1. Also able to mediate the transport of dehydroascorbate.

**Summary**, from NCBI Gene [29988](https://www.ncbi.nlm.nih.gov/gene/29988):

> This gene belongs to the solute carrier 2A family, which includes intracellular glucose transporters. Based on sequence comparison, the glucose transporters are grouped into three classes and this gene is a member of class II. The encoded protein, like other members of the family, contains several conserved residues and motifs and 12 transmembrane domains with both amino and carboxyl ends being on the cytosolic side of the membrane. Alternatively spliced transcript variants have been described …

**Accessions** — [HGNC:13812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13812) · Entrez [29988](https://www.ncbi.nlm.nih.gov/gene/29988) · UniProt [Q9NY64](https://www.uniprot.org/uniprotkb/Q9NY64) · Ensembl [ENSG00000136856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136856)

## Data

Gene col 5919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5919); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5919]; `tensor/DDL_lfc|DDL_z.npy` [5919]; `embed/gene_vectors.npy` [5919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5919 or target_col == 5919). Every well: [[SLC2A8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC2A8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "CDC23"
type: "gene"
col: 1728
ensembl_id: "ENSG00000094880"
name: "cell division cycle 23"
location: "5q31.2"
module: 171
arm: "+"
pooled_cpm: 25.99
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# CDC23

*cell division cycle 23* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.81× (z +11.1, q 5e-26, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.712× (z -9.1, q 6e-17, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED24]] (+0.63, fdr 7e-06), [[SASS6]] (+0.63, fdr 7e-06), [[COPS7B]] (+0.62, fdr 8e-06); moves opposite to [[ZSWIM6]] (-0.66, fdr 7e-06), [[DUSP5]] (-0.56, fdr 4e-05), [[LINC01619]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +11.1 | 5e-26 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +9.7 | 1e-19 | 37/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +8.2 | 5e-14 | 37/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +6.9 | 7e-10 | 32/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.93×** | +6.5 | 1e-08 | 24/48 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +6.4 | 1e-08 | 24/47 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +6.3 | 2e-08 | 26/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.26×** | +6.0 | 1e-07 | 23/47 (LOX-IMVI, A549, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +5.8 | 4e-07 | 22/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +5.7 | 9e-07 | 22/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 9e-06 | 21/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **1.33×** | +5.2 | 1e-05 | 21/47 (LoVo, A-427, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.8 | 6e-05 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.25×** | +4.2 | 0.001 | 14/48 (NCI-H460, A-427, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +4.1 | 0.001 | 14/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.096 | 5/47 (SNU-1, HCT15, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.712×** | -9.1 | 6e-17 | 39/48 (A498, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.750×** | -5.4 | 1e-05 | 25/48 (HepG2/C3A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.785×** | -4.6 | 9e-04 | 18/48 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.844× | -3.2 | 0.14 | 14/47 (AN3 CA, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.844× | -3.2 | 0.14 | 9/48 (HT-29, HS-578T, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.840× | -3.2 | 0.14 | 11/48 (NCI-H1573, NCI-H661, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.15 | 15/47 (H4, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 30.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -17.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 21.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +11.0) | — |
| [[AN3 CA (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0864× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.93× (z +10.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 28.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW1417 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 29.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +11.1) | — |
| [[A-172 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED24]] | +0.63 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SASS6]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[COPS7B]] | +0.62 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[EIF2B1]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[TCTN2]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[CWF19L1]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[MBIP]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[HAUS5]] | +0.58 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[SNX4]] | +0.58 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[MTBP]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ZNF138]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ZCCHC4]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM6]] | -0.66 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[DUSP5]] | -0.56 | -0.40 / -0.58 | both halves | 4e-05 |  |
| [[LINC01619]] | -0.54 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[ATP2B1]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[RPS6KA3]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 | pathway: Cellular Senescence |
| [[NABP1]] | -0.52 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TRIB1]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[MIDN]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[EZR]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[LONRF3]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[C11orf96]] | -0.50 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[DELEC1]] | -0.50 | -0.38 / -0.56 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CDC23's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-22.1, -8.2); signed map (-35.2, -30.2). **Vector** length 66.4, 11.2% of its response variance represented; |z| ≥ 3 in 893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~7% of this change | +3.8 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.1 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +5.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.7 | +1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.8 | -5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | -1.7 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:138,187,650-138,213,343 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APC8, ANAPC8, CUT23 |
| Gene groups (HGNC) | Anaphase promoting complex; Tetratricopeptide repeat domain containing |
| Reactome | 42 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJX2](https://www.uniprot.org/uniprotkb/Q9UJX2) (Cell division cycle protein 23 homolog):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains. APC/C catalyzes assembly of branched 'Lys-11'-/'Lys-48'-linked branched ubiquitin chains on …

**Summary**, from NCBI Gene [8697](https://www.ncbi.nlm.nih.gov/gene/8697):

> The protein encoded by this gene shares strong similarity with Saccharomyces cerevisiae Cdc23, a protein essential for cell cycle progression through the G2/M transition. This protein is a component of anaphase-promoting complex (APC), which is composed of eight protein subunits and highly conserved in eukaryotic cells. APC catalyzes the formation of cyclin B-ubiquitin conjugate that is responsible for the ubiquitin-mediated proteolysis of B-type cyclins. This protein and 3 other members of the …

**Accessions** — [HGNC:1724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1724) · Entrez [8697](https://www.ncbi.nlm.nih.gov/gene/8697) · UniProt [Q9UJX2](https://www.uniprot.org/uniprotkb/Q9UJX2) · Ensembl [ENSG00000094880](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000094880)

## Data

Gene col 1728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1728); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1728]; `tensor/DDL_lfc|DDL_z.npy` [1728]; `embed/gene_vectors.npy` [1728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1728 or target_col == 1728). Every well: [[CDC23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

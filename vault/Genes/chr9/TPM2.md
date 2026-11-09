---
symbol: "TPM2"
type: "gene"
col: 12597
ensembl_id: "ENSG00000198467"
name: "tropomyosin 2"
location: "9p13.3"
module: 4
arm: "-"
pooled_cpm: 65.96
n_lines_expressing: 38
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TPM2

*tropomyosin 2* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.81× (z +14.8, q 0e+00, up in 34 of 35 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 5.29×, NCI-H23 4.80×, NCI-H1792 6.69×, A549 6.36×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.39×, A-427 4.95×, NCI-H23 3.78×, Panc 03.27 3.90×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.479× (z -8.1, q 2e-13, down in 30 of 36 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM117A]] (+0.49, fdr 8e-05), [[HOXB-AS3]] (+0.49, fdr 2e-04), [[NFKBID]] (+0.49, fdr 2e-04); moves opposite to [[CPTP]] (-0.50, fdr 9e-05), [[EXOC2]] (-0.49, fdr 5e-05), [[UBL4A]] (-0.45, fdr 2e-04).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[ICAM5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12597.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (PANC-1 5.29×, NCI-H23 4.80×, NCI-H1792 6.69×, A549 6.36×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 4.39×, A-427 4.95×, NCI-H23 3.78×, Panc 03.27 3.90×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.81×** | +14.8 | 0e+00 | 34/35 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.20×** | +12.3 | 2e-32 | 29/31 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +9.3 | 2e-18 | 30/31 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.62×** | +5.3 | 2e-05 | 27/35 (AsPC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.6 | 0.040 | 17/35 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.35×** | +3.3 | 0.094 | 17/35 (J82, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | 1.23× | +3.0 | 0.19 | 14/36 (NCI-H1573, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12597.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.479×** | -8.1 | 2e-13 | 30/36 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.485×** | -8.0 | 4e-13 | 27/36 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.577×** | -6.1 | 2e-07 | 28/36 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.651×** | -4.8 | 3e-04 | 21/36 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.747×** | -4.4 | 0.001 | 16/35 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.661×** | -4.3 | 0.001 | 25/35 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.704×** | -3.7 | 0.015 | 19/35 (H4, C-33 A, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.507×** | -3.4 | 0.056 | 17/35 (A-427, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.536× | -3.1 | 0.13 | 16/36 (AsPC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 129 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -9.2) |
| [[HS-578T (line)]] | alt | 257 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +11.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 42.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.224× (z -9.9) |
| [[PANC-1 (line)]] | alt | 195 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +14.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 64.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -12.1) |
| [[A-427 (line)]] | wt | 38.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +11.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 106 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +12.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 29.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +9.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 72.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 72.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.69× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 445 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +13.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 84.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 94.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 24.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 36.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -9.7) |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.230× (z -8.7) |
| [[Hs 766T (line)]] | wt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +10.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 228 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 31.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +10.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.58 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.26 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 134 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.63 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 280 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM117A]] | +0.49 | +0.37 / +0.39 | both halves | 8e-05 |  |
| [[HOXB-AS3]] | +0.49 | +0.30 / +0.42 | both halves | 2e-04 |  |
| [[NFKBID]] | +0.49 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[ZNF490]] | +0.48 | +0.28 / +0.45 | both halves | 3e-04 |  |
| [[HOXB3]] | +0.48 | +0.26 / +0.45 | both halves | 4e-04 |  |
| [[LASP1]] | +0.47 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[TMA7]] | +0.47 | +0.42 / +0.38 | both halves | 6e-05 |  |
| [[SUPT5H]] | +0.46 | +0.35 / +0.41 | both halves | 1e-04 |  |
| [[ACADSB]] | +0.45 | +0.28 / +0.32 | both halves | 3e-04 |  |
| [[ICAM5]] | +0.45 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[CLCN2]] | +0.45 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[C12orf57]] | +0.45 | +0.34 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPTP]] | -0.50 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[EXOC2]] | -0.49 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[UBL4A]] | -0.45 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[PSMD1]] | -0.44 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[ICE1]] | -0.44 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[HERC2P9-1]] | -0.44 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PIP4K2A]] | -0.43 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[ZC3H10]] | -0.43 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[EXOC6B]] | -0.43 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[EIF6]] | -0.43 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[GCLM]] | -0.42 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[SLC39A3]] | -0.42 | -0.32 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TPM2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ICAM5]] | B | TPM2 activity raises ICAM5's level | lines that do not express TPM2 (12) vs lines expressing it (38) | 2.36× lower at baseline in the lines without TPM2 | 0.082 | ⚠ within organs, on part of the lines; also absent: GAB3, CYBRD1, CACNG6; maybe low, not absent |
| [[FAM151B-DT]] | B | TPM2 activity raises FAM151B-DT's level | lines that do not express TPM2 (12) vs lines expressing it (38) | 1.15× lower at baseline in the lines without TPM2 | 0.082 | ⚠ within organs, on part of the lines; also absent: GAB3, CYBRD1, CACNG6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.294). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.5, -39.2); signed map (4.3, 8.8). **Vector** length 54.4, 12.0% of its response variance represented; |z| ≥ 3 in 515 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.6 | -4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +1.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +0.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.1 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | tropomyosin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,681,992-35,690,056 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DA1, NEM4; previously AMCD1 |
| Gene groups (HGNC) | Tropomyosins |
| Hallmark sets | MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Striated Muscle Contraction; Smooth Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P07951](https://www.uniprot.org/uniprotkb/P07951) (Tropomyosin beta chain):

> Binds to actin filaments in muscle and non-muscle cells. Plays a central role, in association with the troponin complex, in the calcium dependent regulation of vertebrate striated muscle contraction. Smooth muscle contraction is regulated by interaction with caldesmon. In non-muscle cells is implicated in stabilizing cytoskeleton actin filaments. The non-muscle isoform may have a role in agonist-mediated receptor internalization.

**Summary**, from NCBI Gene [7169](https://www.ncbi.nlm.nih.gov/gene/7169):

> This gene encodes beta-tropomyosin, a member of the actin filament binding protein family, and mainly expressed in slow, type 1 muscle fibers. Mutations in this gene can alter the expression of other sarcomeric tropomyosin proteins, and cause cap disease, nemaline myopathy and distal arthrogryposis syndromes. Alternatively spliced transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:12011](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12011) · Entrez [7169](https://www.ncbi.nlm.nih.gov/gene/7169) · UniProt [P07951](https://www.uniprot.org/uniprotkb/P07951) · Ensembl [ENSG00000198467](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198467)

## Data

Gene col 12597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12597); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12597]; `tensor/DDL_lfc|DDL_z.npy` [12597]; `embed/gene_vectors.npy` [12597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12597 or target_col == 12597). Every well: [[TPM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

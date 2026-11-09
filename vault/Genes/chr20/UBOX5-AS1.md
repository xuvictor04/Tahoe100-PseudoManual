---
symbol: "UBOX5-AS1"
type: "gene"
col: 14051
ensembl_id: "ENSG00000235958"
name: "UBOX5 antisense RNA 1"
location: "20p13"
module: 21
arm: "+"
pooled_cpm: 2.38
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# UBOX5-AS1

*UBOX5 antisense RNA 1* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.17× (z +10.8, q 2e-24, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.06× (z +10.0, q 7e-21, up in 24 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.814× (z -7.2, q 5e-10, down in 23 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Futibatinib (drug)]] 0.05 µM: 0.658× (z -3.9, q 0.031, down in 8 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Methotrexate (drug)]] 0.05 µM in 1 line (A498 0.0696×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0873×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCNT7]] (+0.84, fdr 7e-06), [[C2CD5-AS1]] (+0.83, fdr 7e-06), [[HRG-AS1]] (+0.82, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.17×** | +10.8 | 2e-24 | 2/4 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +10.0 | 7e-21 | 24/34 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +8.0 | 3e-13 | 9/13 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +7.5 | 7e-12 | 4/5 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.08×** | +7.2 | 1e-10 | 4/11 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +5.6 | 3e-06 | 11/37 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.2 | 0.002 | 12/28 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.005 | 4/34 (RPMI-7951, HS-578T, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.005 | 4/28 (A498, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +3.7 | 0.015 | 0/3 | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +3.5 | 0.020 | 4/40 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +3.5 | 0.020 | 1/4 (SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +3.5 | 0.020 | 4/31 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.020 | 8/43 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.023 | 3/41 (SW480, J82, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.031 | 4/34 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.046 | 5/44 (SW480, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.055 | 5/41 (SNU-1, HT-29, …) | top dose only |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.40×** | +3.1 | 0.055 | 3/38 (HT-29, C32, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.055 | 4/33 (BT-474, SHP-77, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.064 | 3/42 (NCI-H23, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.085 | 4/46 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14051.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Methotrexate (drug)]] 0.05 µM in 1 line (A498 0.0696×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0873×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.814×** | -7.2 | 5e-10 | 23/47 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.658×** | -3.9 | 0.031 | 8/42 (KATO III, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.804× | -3.0 | 0.46 | 4/45 (Hs 766T, MIA PaCa-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.99 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0696× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 2.43 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0873× (z -8.7) |
| [[A-172 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCNT7]] | +0.84 | +0.71 / +0.82 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.83 | +0.63 / +0.80 | both halves | 7e-06 | same gene group |
| [[HRG-AS1]] | +0.82 | +0.67 / +0.82 | both halves | 7e-06 | same gene group |
| [[BIRC6-AS2-1]] | +0.82 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.82 | +0.60 / +0.84 | both halves | 7e-06 | same gene group |
| [[FAM217A]] | +0.81 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.81 | +0.67 / +0.76 | both halves | 7e-06 | same gene group |
| [[ZRANB2-AS1]] | +0.80 | +0.73 / +0.73 | both halves | 7e-06 | same gene group |
| [[EOGT-DT]] | +0.79 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[VPS39-DT]] | +0.79 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.79 | +0.56 / +0.83 | both halves | 1e-05 | same gene group |
| [[CTDSPL2-DT]] | +0.79 | +0.57 / +0.77 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM | C | UBOX5-AS1's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | UBOX5-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.015 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Ipatasertib (drug)]] 0.5 µM | C | UBOX5-AS1's natural level lowers the cells' numbers under Ipatasertib 0.5 µM (makes them more sensitive) | UBOX5-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.083 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | UBOX5-AS1's natural level raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | UBOX5-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.57 | 0.499 over the table, 0.085 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.873). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.6, 28.0); signed map (34.2, 5.0). **Vector** length 32.1, 2.61% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +7.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +1.9 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.1 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.7 | -1.9 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.7 | -2.0 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | UBOX5 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20p13 — chr20:3,106,913-3,150,867 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44111) · Entrez [100134015](https://www.ncbi.nlm.nih.gov/gene/100134015) · Ensembl [ENSG00000235958](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235958)

## Data

Gene col 14051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14051); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14051]; `tensor/DDL_lfc|DDL_z.npy` [14051]; `embed/gene_vectors.npy` [14051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14051 or target_col == 14051). Every well: [[UBOX5-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBOX5-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

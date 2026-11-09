---
symbol: "AGBL1"
type: "gene"
col: 15789
ensembl_id: "ENSG00000273540"
name: "AGBL carboxypeptidase 1"
location: "15q25.3"
module: 140
arm: "+"
pooled_cpm: 5.81
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# AGBL1

*AGBL carboxypeptidase 1* — 15q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.57× (z +24.7, q 0e+00, up in 27 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.658× (z -4.8, q 8e-04, down in 14 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[TAK-901 (drug)]] 5 µM in 1 line (SHP-77 0.00836×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.0824×; ⚠ toxic; cell-cycle shift, explains ~14% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.153×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNTL6]] (+0.78, fdr 7e-06), [[CNTNAP4]] (+0.77, fdr 7e-06), [[LINC02755]] (+0.75, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CGA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15789.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.57×** | +24.7 | 0e+00 | 27/36 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.51×** | +20.7 | 0e+00 | 4/6 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.54×** | +17.4 | 0e+00 | 15/19 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.57×** | +13.5 | 2e-39 | 4/10 (C-33 A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.07×** | +11.8 | 4e-30 | 18/38 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +10.1 | 4e-22 | 25/46 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.31×** | +9.4 | 5e-19 | 22/43 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +5.9 | 2e-07 | 15/41 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +5.9 | 2e-07 | 14/41 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +5.7 | 8e-07 | 9/44 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +5.5 | 2e-06 | 10/38 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +4.7 | 1e-04 | 5/19 (SNU-423, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.67×** | +4.2 | 0.001 | 3/41 (HOP62, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.001 | 10/44 (AsPC-1, H4, …) | top dose only | position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.0 | 0.003 | 4/29 (C32, SHP-77, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +3.9 | 0.003 | 1/32 (LOX-IMVI) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.013 | 10/43 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.020 | 8/33 (A549, A498, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[EX229 (drug)]] 5 µM |  | **1.75×** | +3.4 | 0.023 | 7/31 (HOP62, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.025 | 1/41 (HS-578T) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15789.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[TAK-901 (drug)]] 5 µM in 1 line (SHP-77 0.00836×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.0824×; ⚠ toxic; cell-cycle shift, explains ~14% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.153×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.658×** | -4.8 | 8e-04 | 14/45 (SHP-77, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -3.4 | 0.14 | 8/47 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM |  | 0.746× | -3.3 | 0.14 | 6/42 (MIA PaCa-2, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Busulfan (drug)]] 5 µM |  | 0.822× | -3.2 | 0.14 | 8/45 (A-427, SNU-1, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.822× | -3.2 | 0.14 | 8/46 (SNU-423, LS 180, …) | rises with dose | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.754× | -3.0 | 0.24 | 5/44 (HS-578T, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15789. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 51.1 | 0 | 3 (3 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.00836× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 3.05 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.0× (z +12.3) | — |
| [[A498 (line)]] | wt | 1.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.01× (z +8.8) | — |
| [[A549 (line)]] | wt | 5.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.78× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 2.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.84× (z +8.6) | — |
| [[KATO III (line)]] | alt | 2.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 3.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.95× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 1.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 91.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0960× (z -8.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 2.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.21× (z +11.7) | — |
| [[A-172 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15789), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNTL6]] | +0.78 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[CNTNAP4]] | +0.77 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[LINC02755]] | +0.75 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.75 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.74 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.73 | +0.61 / +0.76 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.73 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.73 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[GALNT17]] | +0.71 | +0.60 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ANO3]] | +0.71 | +0.57 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[PCDH15]] | +0.71 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.71 | +0.57 / +0.79 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CGA]] | B | CGA activity raises AGBL1's level | lines that do not express CGA (44) vs lines expressing it (6) | 2.76× lower at baseline in the lines without CGA | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[LSAMP]] | B | LSAMP activity raises AGBL1's level | lines that do not express LSAMP (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without LSAMP | 0.037 | ⚠ within organs, on part of the lines; also absent: FRG1JP, ENSG00000289153, CA9; maybe low, not absent |
| [[FRMPD4]] | B | FRMPD4 activity raises AGBL1's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 1.80× lower at baseline in the lines without FRMPD4 | 0.060 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[ADARB2]] | B | ADARB2 activity raises AGBL1's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 1.82× lower at baseline in the lines without ADARB2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.4, 28.8); signed map (33.5, 14.5). **Vector** length 63.7, 9.66% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.5 | +24.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.4 | +17.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.2 | +20.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.7 | +13.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.1 | +1.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.1 | -3.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.4 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -4.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -1.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -2.0 | -2.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | AGBL carboxypeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.3 — chr15:86,079,871-87,049,169 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32310, CCP4 |
| Gene groups (HGNC) | M14 carboxypeptidases; Armadillo like helical domain containing |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MI9](https://www.uniprot.org/uniprotkb/Q96MI9) (Cytosolic carboxypeptidase 4):

> Metallocarboxypeptidase that mediates deglutamylation of tubulin and non-tubulin target proteins. Catalyzes the removal of polyglutamate side chains present on the gamma-carboxyl group of glutamate residues within the C-terminal tail of tubulin protein. Specifically cleaves tubulin long-side-chains, while it is not able to remove the branching point glutamate. Also catalyzes the removal of polyglutamate residues from the carboxy-terminus of non-tubulin proteins such as MYLK.

**Summary**, from NCBI Gene [123624](https://www.ncbi.nlm.nih.gov/gene/123624):

> Polyglutamylation is a reversible posttranslational modification catalyzed by polyglutamylases that results in the addition of glutamate side chains on the modified protein. This gene encodes a glutamate decarboxylase that catalyzes the deglutamylation of polyglutamylated proteins. Mutations in this gene result in dominant late-onset Fuchs corneal dystrophy. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:26504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26504) · Entrez [123624](https://www.ncbi.nlm.nih.gov/gene/123624) · UniProt [Q96MI9](https://www.uniprot.org/uniprotkb/Q96MI9) · Ensembl [ENSG00000273540](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273540)

## Data

Gene col 15789: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15789); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15789, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15789]; `tensor/DDL_lfc|DDL_z.npy` [15789]; `embed/gene_vectors.npy` [15789]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15789 or target_col == 15789). Every well: [[AGBL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGBL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

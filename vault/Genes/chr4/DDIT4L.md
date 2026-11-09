---
symbol: "DDIT4L"
type: "gene"
col: 6981
ensembl_id: "ENSG00000145358"
name: "DNA damage inducible transcript 4 like"
location: "4q24"
module: 19
arm: "+"
pooled_cpm: 2.09
n_lines_expressing: 21
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# DDIT4L

*DNA damage inducible transcript 4 like* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.35× (z +11.8, q 3e-29, up in 16 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.469× (z -4.0, q 0.034, down in 1 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0682×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0656×; ⚠ cell-cycle shift, explains ~33% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0512×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0804×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.170×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAX7]] (+0.77, fdr 7e-06), [[SCARA5]] (+0.75, fdr 7e-06), [[LINC03000]] (+0.73, fdr 7e-06); moves opposite to [[ITGA9-AS1]] (-0.47, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SCARA5]] → it (grade C ⚠); 2 go from it, the strongest it → [[CACNA2D3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.35×** | +11.8 | 3e-29 | 16/16 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.62×** | +9.7 | 1e-19 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.12×** | +9.3 | 4e-18 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.48×** | +7.9 | 5e-13 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.01×** | +6.2 | 5e-08 | 10/11 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +5.5 | 3e-06 | 2/9 (LoVo, A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.72×** | +5.3 | 9e-06 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.49×** | +5.2 | 2e-05 | 0/8 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.22×** | +4.5 | 4e-04 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.69×** | +4.2 | 0.002 | 1/17 (LoVo) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +4.1 | 0.002 | 1/7 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.95×** | +3.8 | 0.008 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +3.7 | 0.008 | 7/16 (NCI-H2347, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +3.7 | 0.009 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.009 | 2/10 (A549, HOP62) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.26×** | +3.3 | 0.032 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.81×** | +3.0 | 0.070 | 0/8 | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.070 | 0/9 | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.69×** | +2.9 | 0.081 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +2.9 | 0.098 | 7/16 (LS 180, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6981.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0682×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0656×; ⚠ cell-cycle shift, explains ~33% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0512×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0804×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.170×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.469×** | -4.0 | 0.034 | 1/15 (LS 180) | inconsistent across doses |  |
| [[Orlistat (drug)]] 5 µM |  | 0.545× | -3.1 | 0.34 | 0/14 | top dose only |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.581× | -3.1 | 0.34 | 2/13 (CFPAC-1, A549) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.592× | -3.0 | 0.36 | 8/15 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.8 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0682× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 7.76 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.32× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 5.22 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.33× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 4.02 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0449× (z -9.3) ⚠ cell-cycle shift, explains ~7% of this change |
| [[A-172 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.121 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.152 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.865 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.162 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.163 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.206 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.153 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.708 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.137 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.160 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.145 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.150 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.165 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.533 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.127 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.549 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.632 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.130 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.209 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.660 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.139 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.153 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.735 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.115 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.152 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.232 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.185 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.298 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAX7]] | +0.77 | +0.81 / +0.72 | both halves | 7e-06 |  |
| [[SCARA5]] | +0.75 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[LINC03000]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[DPP10]] | +0.72 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[SLC15A5]] | +0.71 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[CHL1]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.68 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[SPDYE10]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[SERPINB11]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[GTF2I-AS1]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA9-AS1]] | -0.47 | -0.34 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCARA5]] | C | SCARA5 activity raises DDIT4L's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.19× lower at baseline in the lines without SCARA5 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[PRICKLE1]] | C | PRICKLE1 activity raises DDIT4L's level | lines that do not express PRICKLE1 (26) vs lines expressing it (24) | 1.71× lower at baseline in the lines without PRICKLE1 | 0.029 | ⚠ within organs, on part of the lines; also absent: COL4A2, NR0B1, THBD; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises DDIT4L's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 1.95× lower at baseline in the lines without GTF2I-AS1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[SERPINB11]] | C | SERPINB11 activity raises DDIT4L's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 2.57× lower at baseline in the lines without SERPINB11 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises DDIT4L's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 2.42× lower at baseline in the lines without GSG1L2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises DDIT4L's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 2.10× lower at baseline in the lines without LINC03000 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA2D3]] | C | DDIT4L activity raises CACNA2D3's level | lines that do not express DDIT4L (29) vs lines expressing it (21) | 2.11× lower at baseline in the lines without DDIT4L | 0.077 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL1B, ARMCX2; co-absent with the target |
| [[EFEMP1]] | C | DDIT4L activity raises EFEMP1's level | lines that do not express DDIT4L (29) vs lines expressing it (21) | 2.94× lower at baseline in the lines without DDIT4L | 0.088 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL1B, ARMCX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.3, 36.5); signed map (43.0, 44.5). **Vector** length 37.4, 9.68% of its response variance represented; |z| ≥ 3 in 380 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.1 | +5.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.1 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.8 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.8 | +1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.6 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.1 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -0.8 | -0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -0.8 | -0.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -1.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.6 | -1.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.6 | -4.0 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -0.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | DNA damage inducible transcript 4 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:100,185,870-100,190,782 (-) |
| Ensembl biotype | protein_coding |
| Also known as | REDD2, Rtp801L |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96D03](https://www.uniprot.org/uniprotkb/Q96D03) (DNA damage-inducible transcript 4-like protein):

> Inhibits cell growth by regulating the TOR signaling pathway upstream of the TSC1-TSC2 complex and downstream of AKT1.

**Summary**, from NCBI Gene [115265](https://www.ncbi.nlm.nih.gov/gene/115265):

> Predicted to be involved in negative regulation of signal transduction. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30555) · Entrez [115265](https://www.ncbi.nlm.nih.gov/gene/115265) · UniProt [Q96D03](https://www.uniprot.org/uniprotkb/Q96D03) · Ensembl [ENSG00000145358](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145358)

## Data

Gene col 6981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6981); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6981]; `tensor/DDL_lfc|DDL_z.npy` [6981]; `embed/gene_vectors.npy` [6981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6981 or target_col == 6981). Every well: [[DDIT4L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDIT4L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

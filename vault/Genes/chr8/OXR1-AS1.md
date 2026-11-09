---
symbol: "OXR1-AS1"
type: "gene"
col: 14817
ensembl_id: "ENSG00000253582"
name: "OXR1 antisense RNA 1"
location: "8q23.1"
module: 21
arm: "+"
pooled_cpm: 4.76
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# OXR1-AS1

*OXR1 antisense RNA 1* — 8q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.66× (z +23.6, q 0e+00, up in 36 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.634× (z -4.9, q 4e-04, down in 17 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (A-427 0.102×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C32 0.0879×; ⚠ toxic; cell-cycle shift, explains ~10% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (C32 0.0973×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0993×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2CD5-AS1]] (+0.75, fdr 7e-06), [[ZBTB20-AS5]] (+0.73, fdr 7e-06), [[EHBP1-AS1]] (+0.72, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.66×** | +23.6 | 0e+00 | 36/37 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.86×** | +11.0 | 2e-25 | 24/34 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +10.1 | 2e-21 | 28/36 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +9.1 | 9e-18 | 6/7 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +8.0 | 1e-13 | 11/25 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +8.0 | 2e-13 | 26/46 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.02×** | +7.6 | 2e-12 | 25/44 (NCI-H2030, SW48, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +6.9 | 3e-10 | 7/13 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +5.8 | 5e-07 | 17/46 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +5.0 | 3e-05 | 11/43 (SW48, A498, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +5.0 | 3e-05 | 12/45 (KATO III, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.8 | 7e-05 | 11/46 (SW1417, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.5 | 3e-04 | 14/44 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +4.3 | 6e-04 | 9/44 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +3.2 | 0.047 | 3/23 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14817.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (A-427 0.102×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (C32 0.0879×; ⚠ toxic; cell-cycle shift, explains ~10% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (C32 0.0973×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0993×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.634×** | -4.9 | 4e-04 | 17/46 (SW480, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.727× | -3.5 | 0.11 | 14/36 (NCI-H1792, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.659× | -3.4 | 0.11 | 12/41 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.738× | -3.3 | 0.14 | 10/45 (SW480, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 8.15 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0879× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~10% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0973× (z -8.8) |
| [[HOP62 (line)]] | alt | 3.64 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 4.83 | 0 | 2 | — | [[Celecoxib (drug)]] 0.05 µM 0.0634× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 2.39 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +8.5) | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0993× (z -8.7) |
| [[A-172 (line)]] | wt | 2.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.51× (z +9.3) | — |
| [[A-427 (line)]] | wt | 12.1 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.102× (z -10.3) |
| [[A549 (line)]] | wt | 2.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.15× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 3.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.67× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 3.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.2× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 6.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 4.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +10.1) | — |
| [[J82 (line)]] | alt | 3.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 5.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 3.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.20× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 3.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.45× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 4.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +12.3) | — |
| [[A498 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2CD5-AS1]] | +0.75 | +0.60 / +0.73 | both halves | 7e-06 | same gene group |
| [[ZBTB20-AS5]] | +0.73 | +0.63 / +0.71 | both halves | 7e-06 | same gene group |
| [[EHBP1-AS1]] | +0.72 | +0.56 / +0.67 | both halves | 1e-05 | same gene group |
| [[CTDSPL2-DT]] | +0.71 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[C12orf40]] | +0.70 | +0.47 / +0.75 | both halves | 2e-05 |  |
| [[HRG-AS1]] | +0.70 | +0.55 / +0.66 | both halves | 1e-05 | same gene group |
| [[ZNF451-AS1]] | +0.70 | +0.60 / +0.66 | both halves | 7e-06 | same gene group |
| [[CCNO-DT]] | +0.70 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[UBOX5-AS1]] | +0.70 | +0.43 / +0.70 | both halves | 3e-05 | same gene group |
| [[GEMIN7-AS1]] | +0.69 | +0.52 / +0.70 | both halves | 1e-05 | same gene group |
| [[CHMP3-AS1]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 | same gene group |
| [[LANCL1-AS1]] | +0.68 | +0.59 / +0.62 | both halves | 7e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers OXR1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GRID2]] | C | GRID2 activity lowers OXR1-AS1's level | lines that do not express GRID2 (4) vs lines expressing it (46) | 1.81× higher at baseline in the lines without GRID2 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC01811, IQCM; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, 26.7); signed map (33.9, 3.3). **Vector** length 45.7, 5.35% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +23.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +11.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +0.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -3.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.8 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | OXR1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q23.1 — chr8:106,520,474-106,657,548 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55533](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55533) · Entrez [105375700](https://www.ncbi.nlm.nih.gov/gene/105375700) · Ensembl [ENSG00000253582](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253582)

## Data

Gene col 14817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14817); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14817]; `tensor/DDL_lfc|DDL_z.npy` [14817]; `embed/gene_vectors.npy` [14817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14817 or target_col == 14817). Every well: [[OXR1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OXR1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

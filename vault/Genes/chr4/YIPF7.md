---
symbol: "YIPF7"
type: "gene"
col: 10864
ensembl_id: "ENSG00000177752"
name: "Yip1 domain family member 7"
location: "4p12"
module: 39
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# YIPF7

*Yip1 domain family member 7* — 4p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.00× (z +14.1, q 3e-42, up in 22 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (NCI-H1573 0.0682×); [[Idoxuridine (drug)]] 0.05 µM in 1 line (SW 900 0.0602×); [[Erythromycin (drug)]] 0.5 µM in 1 line (SW 900 0.0688×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF546]] (+0.78, fdr 7e-06), [[MCF2]] (+0.77, fdr 7e-06), [[CFAP70]] (+0.77, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[C12orf50]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.00×** | +14.1 | 3e-42 | 22/25 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.51×** | +11.8 | 1e-29 | 21/31 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.64×** | +11.7 | 2e-29 | 26/35 (A-427, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.66×** | +10.9 | 2e-25 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.30×** | +10.8 | 3e-25 | 35/41 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +9.9 | 3e-21 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.98×** | +9.3 | 7e-19 | 24/35 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.52×** | +8.4 | 4e-15 | 27/38 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +8.2 | 1e-14 | 13/22 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.33×** | +7.7 | 1e-12 | 18/30 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +7.2 | 3e-11 | 14/42 (HEC-1-A, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +6.8 | 7e-10 | 9/41 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +6.2 | 2e-08 | 4/10 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.32×** | +5.7 | 5e-07 | 3/5 (NCI-H2347, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +5.1 | 1e-05 | 13/36 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.4 | 4e-04 | 7/30 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +4.2 | 8e-04 | 14/43 (SW 900, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.83×** | +3.9 | 0.003 | 7/39 (A-172, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.006 | 6/42 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10864.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Bendamustine (drug)]] 5 µM in 1 line (NCI-H1573 0.0682×); [[Idoxuridine (drug)]] 0.05 µM in 1 line (SW 900 0.0602×); [[Erythromycin (drug)]] 0.5 µM in 1 line (SW 900 0.0688×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sinomenine (drug)]] 0.5 µM |  | 0.683× | -3.5 | 0.20 | 9/40 (SNU-1, NCI-H460, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.497× | -3.3 | 0.20 | 3/18 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 0.702× | -3.2 | 0.20 | 11/42 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.696× | -3.1 | 0.20 | 2/37 (LS 180, H4) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.711× | -3.1 | 0.20 | 5/42 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 5.51 | 0 | 2 | — | [[Idoxuridine (drug)]] 0.05 µM 0.0602× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 4.71 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0824× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 4.35 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0682× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 2.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +9.3) | — |
| [[A-172 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.744 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.759 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.842 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.569 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.560 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF546]] | +0.78 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[MCF2]] | +0.77 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[CFAP70]] | +0.77 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[GRK7]] | +0.77 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[BAAT]] | +0.75 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PARD6G-AS1]] | +0.75 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.75 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.75 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[NEK11]] | +0.75 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MSH4]] | +0.75 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[FRZB]] | +0.75 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[PTOV1-AS1]] | +0.74 | +0.71 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf50]] | B | C12orf50 activity raises YIPF7's level | lines that do not express C12orf50 (8) vs lines expressing it (42) | 1.74× lower at baseline in the lines without C12orf50 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195, LYPLAL1-AS1, ENSG00000237153; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers YIPF7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ST8SIA5]] | B | ST8SIA5 activity raises YIPF7's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.71× lower at baseline in the lines without ST8SIA5 | 0.050 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[ZNF382]] | B | ZNF382 activity raises YIPF7's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.43× lower at baseline in the lines without ZNF382 | 0.060 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[LY96]] | B | LY96 activity raises YIPF7's level | lines that do not express LY96 (18) vs lines expressing it (32) | 1.45× lower at baseline in the lines without LY96 | 0.070 | ⚠ within organs, on part of the lines; also absent: SOX5, ENSG00000287100, ENSG00000287622; maybe low, not absent |
| [[IMPG2]] | C | IMPG2 activity raises YIPF7's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 1.96× lower at baseline in the lines without IMPG2 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.5, -12.5); signed map (18.9, 3.5). **Vector** length 58.0, 7.95% of its response variance represented; |z| ≥ 3 in 1,243 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +14.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.4 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.3 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +6.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | Yip1 domain family member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12 — chr4:44,622,088-44,678,556 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ39576, FinGER9, Yip1b, YIPFalpha1b |
| Gene groups (HGNC) | Yip1 domain containing |
| Matched by | ensembl_id |

UniProt [Q8N8F6](https://www.uniprot.org/uniprotkb/Q8N8F6) carries no function annotation.

**Summary**, from NCBI Gene [285525](https://www.ncbi.nlm.nih.gov/gene/285525):

> Predicted to be involved in endoplasmic reticulum to Golgi vesicle-mediated transport and vesicle fusion with Golgi apparatus. Predicted to act upstream of or within Golgi organization. Predicted to be located in cis-Golgi network; endoplasmic reticulum membrane; and endoplasmic reticulum-Golgi intermediate compartment. Predicted to be active in trans-Golgi network. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26825) · Entrez [285525](https://www.ncbi.nlm.nih.gov/gene/285525) · UniProt [Q8N8F6](https://www.uniprot.org/uniprotkb/Q8N8F6) · Ensembl [ENSG00000177752](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177752)

## Data

Gene col 10864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10864); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10864]; `tensor/DDL_lfc|DDL_z.npy` [10864]; `embed/gene_vectors.npy` [10864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10864 or target_col == 10864). Every well: [[YIPF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YIPF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "SEMA6A-AS1"
type: "gene"
col: 14539
ensembl_id: "ENSG00000248445"
name: "SEMA6A antisense RNA 1"
location: "5q23.1"
module: 26
arm: "+"
pooled_cpm: 5.17
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SEMA6A-AS1

*SEMA6A antisense RNA 1* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.03× (z +8.3, q 9e-14, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.269× (z -9.8, q 4e-20, down in 36 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (A-427 0.0797×, NCI-H460 0.0468×, LS 180 0.0934×; ⚠ toxic); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 2 lines (HCT15 0.0565×, A-427 0.190×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0960×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ponatinib (drug)]] 5 µM in 1 line (C32 0.0716×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00907]] (+0.78, fdr 7e-06), [[COMMD10]] (+0.77, fdr 7e-06, ⚠ same locus), [[RGS5]] (+0.76, fdr 7e-06), [[PRH1]] (+0.75, fdr 7e-06); moves opposite to [[SLC35A1]] (-0.65, fdr 2e-05), [[IDH2]] (-0.64, fdr 1e-05), [[POGLUT2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14539.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.03×** | +8.3 | 9e-14 | 35/44 (HEC-1-A, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.19×** | +8.0 | 4e-13 | 8/11 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +7.1 | 2e-10 | 25/41 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +7.0 | 3e-10 | 4/4 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +6.9 | 4e-10 | 14/23 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.43×** | +6.6 | 4e-09 | 24/39 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.97×** | +4.8 | 1e-04 | 20/44 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.69×** | +3.9 | 0.006 | 15/46 (SW480, NCI-H460, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.71×** | +3.8 | 0.008 | 16/41 (SW480, PANC-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.64×** | +3.7 | 0.013 | 16/45 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.013 | 13/46 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +3.4 | 0.036 | 13/45 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.59×** | +3.3 | 0.041 | 12/43 (NCI-H2347, SNU-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 2.16× | +3.0 | 0.11 | 5/42 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14539.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (A-427 0.0797×, NCI-H460 0.0468×, LS 180 0.0934×; ⚠ toxic); [[Topotecan (hydrochloride) (drug)]] 0.5 µM in 2 lines (HCT15 0.0565×, A-427 0.190×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0960×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ponatinib (drug)]] 5 µM in 1 line (C32 0.0716×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.269×** | -9.8 | 4e-20 | 36/45 (HCT15, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.561×** | -4.2 | 0.009 | 19/27 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -3.6 | 0.051 | 16/45 (SNU-423, SW480, …) | top dose only | plate-row cell shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.637× | -3.4 | 0.10 | 19/45 (SNU-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.642× | -3.3 | 0.10 | 13/46 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | 0.743× | -3.2 | 0.15 | 8/45 (SHP-77, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 21.5 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0797× (z -13.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.190× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 4.54 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +13.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0789× (z -8.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 4.83 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.79× (z +12.8) | — |
| [[C32 (line)]] | wt | 10.0 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.0716× (z -9.3) |
| [[COLO 205 (line)]] | alt | 6.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.5× (z +14.4) | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0565× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 4.88 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.3× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 9.05 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0934× (z -9.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 6.53 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0468× (z -12.3) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 4.33 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[A-172 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00907]] | +0.78 | +0.74 / +0.79 | both halves | 7e-06 |  |
| [[COMMD10]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 | ⚠ same locus (34.8 kb, same strand: neighbours can correlate without regulation) |
| [[RGS5]] | +0.76 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[PRH1]] | +0.75 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[RNF32-AS1]] | +0.74 | +0.76 / +0.71 | both halves | 7e-06 | same gene group |
| [[LINC02516]] | +0.72 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[PRR4]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[WARS2-AS1]] | +0.71 | +0.85 / +0.55 | both halves | 1e-05 | same gene group |
| [[DPH5-DT]] | +0.71 | +0.80 / +0.56 | both halves | 1e-05 |  |
| [[ITPR2-AS1]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 | same gene group |
| [[TIAM2]] | +0.69 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[LINC00486]] | +0.69 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[ACYP2]] | +0.68 | +0.81 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A1]] | -0.65 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[IDH2]] | -0.64 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[POGLUT2]] | -0.62 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[APAF1]] | -0.61 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[KLHL7]] | -0.59 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.59 | -0.77 / -0.34 | both halves | 1e-04 |  |
| [[ARL3]] | -0.58 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[L2HGDH]] | -0.58 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[FLYWCH2]] | -0.58 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[CRY2]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[SMAP2]] | -0.57 | -0.59 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity raises SEMA6A-AS1's level | compounds that target TOP1: 2 of 3 lower it (Irinotecan, Topotecan) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KLRG1]] | B | KLRG1 activity raises SEMA6A-AS1's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without KLRG1 | 0.084 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |
| [[ST8SIA5]] | B | ST8SIA5 activity raises SEMA6A-AS1's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.87× lower at baseline in the lines without ST8SIA5 | 0.097 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (14.3, 15.0); signed map (22.1, 3.0). **Vector** length 86.9, 16.9% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.7 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +4.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.9 | -9.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.9 | -4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.5 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.3 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | SEMA6A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q23.1 — chr5:116,447,547-116,508,276 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51110) · Entrez [101927233](https://www.ncbi.nlm.nih.gov/gene/101927233) · Ensembl [ENSG00000248445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248445)

## Data

Gene col 14539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14539); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14539]; `tensor/DDL_lfc|DDL_z.npy` [14539]; `embed/gene_vectors.npy` [14539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14539 or target_col == 14539). Every well: [[SEMA6A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA6A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

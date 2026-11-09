---
symbol: "ICAM5"
type: "gene"
col: 2592
ensembl_id: "ENSG00000105376"
name: "intercellular adhesion molecule 5"
location: "19p13.2"
module: 103
arm: "+"
pooled_cpm: 8.27
n_lines_expressing: 36
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# ICAM5

*intercellular adhesion molecule 5* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.36× (z +14.8, q 0e+00, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.598× (z -4.4, q 0.005, down in 19 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0647×, SK-MEL-2 0.163×; ⚠ toxic; cell-cycle shift, explains ~73% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.188×); [[Docetaxel (drug)]] 0.05 µM in 1 line (Hs 766T 0.116×; ⚠ transcription drop; cell-cycle shift, explains ~95% of this change); [[Brimonidine (drug)]] 0.05 µM in 1 line (HCT15 0.0428×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KREMEN2]] (+0.58, fdr 1e-05), [[NFKBID]] (+0.56, fdr 1e-05), [[NTF3]] (+0.56, fdr 3e-05); moves opposite to [[HECTD1]] (-0.60, fdr 7e-06), [[BNIP2]] (-0.56, fdr 3e-05), [[HERC2P9-1]] (-0.54, fdr 3e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MME]] → it (grade B ⚠); 2 go from it, the strongest it → [[TMEM39B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2592.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.36×** | +14.8 | 0e+00 | 26/31 (A498, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.17×** | +9.5 | 7e-19 | 20/32 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.35×** | +7.1 | 2e-10 | 19/32 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +5.8 | 7e-07 | 8/18 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +4.6 | 6e-04 | 15/34 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.3 | 0.002 | 14/29 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +4.2 | 0.002 | 16/33 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.020 | 9/32 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.50×** | +3.5 | 0.025 | 15/31 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.036 | 9/32 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2592.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (hTERT-HPNE 0.0647×, SK-MEL-2 0.163×; ⚠ toxic; cell-cycle shift, explains ~73% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.188×); [[Docetaxel (drug)]] 0.05 µM in 1 line (Hs 766T 0.116×; ⚠ transcription drop; cell-cycle shift, explains ~95% of this change); [[Brimonidine (drug)]] 0.05 µM in 1 line (HCT15 0.0428×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.598×** | -4.4 | 0.005 | 19/32 (HOP62, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.680× | -3.3 | 0.16 | 12/31 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.682× | -3.3 | 0.16 | 6/33 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.689× | -3.2 | 0.16 | 13/33 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.680× | -3.2 | 0.16 | 10/31 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.700× | -3.1 | 0.20 | 11/33 (H4, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.703× | -3.0 | 0.20 | 10/31 (HOP62, hTERT-HPNE, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2592. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.84 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 11.1× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.66× (z +10.1) | — |
| [[A498 (line)]] | wt | 12.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.60× (z +13.1) | — |
| [[C32 (line)]] | wt | 11.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 14.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +9.7) | [[Docetaxel (drug)]] 0.05 µM 0.116× (z -9.7) ⚠ transcription drop; cell-cycle shift, explains ~95% of this change |
| [[NCI-H2347 (line)]] | alt | 7.31 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 4.58 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +11.0) | — |
| [[A-172 (line)]] | wt | 4.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +11.3) | — |
| [[A549 (line)]] | wt | 3.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 5.07 | 0 | 1 | — | [[Brimonidine (drug)]] 0.05 µM 0.0428× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0647× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~73% of this change |
| [[LOX-IMVI (line)]] | wt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 2.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.163× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~73% of this change |
| [[SW 900 (line)]] | alt | 7.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +8.9) | — |
| [[SW480 (line)]] | alt | 4.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +8.7) | — |
| [[A-427 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2592), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KREMEN2]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[NFKBID]] | +0.56 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NTF3]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MME-AS1]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[FAM110A]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[RBPJ]] | +0.55 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[CD40]] | +0.55 | +0.41 / +0.55 | both halves | 4e-05 | pathway: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell |
| [[LFNG]] | +0.54 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[FGFR1]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[SNAI1]] | +0.54 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[ATP23]] | +0.54 | +0.37 / +0.55 | both halves | 7e-05 |  |
| [[ADCY10]] | +0.53 | +0.42 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HECTD1]] | -0.60 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[BNIP2]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[HERC2P9-1]] | -0.54 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[PSMD1]] | -0.53 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[GTF3C3]] | -0.53 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[UTP11]] | -0.52 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[CCT2]] | -0.51 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[VPS50]] | -0.50 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[PSMD12]] | -0.50 | -0.43 / -0.53 | both halves | 4e-05 |  |
| [[SNX19]] | -0.49 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PTPN11]] | -0.49 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[LSG1]] | -0.49 | -0.44 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MME]] | B | MME activity raises ICAM5's level | lines that do not express MME (30) vs lines expressing it (20) | 2.32× lower at baseline in the lines without MME | 0.004 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[JAM2]] | B | JAM2 activity raises ICAM5's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without JAM2 | 0.038 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[TPM2]] | B | TPM2 activity raises ICAM5's level | lines that do not express TPM2 (12) vs lines expressing it (38) | 2.36× lower at baseline in the lines without TPM2 | 0.082 | ⚠ within organs, on part of the lines; also absent: GAB3, CYBRD1, CACNG6; maybe low, not absent |
| [[ACHE]] | B | ACHE activity strengthens ICAM5's drug response | lines that do not express ACHE (10) vs lines expressing it (24) | the lines without ACHE respond 0.36× as strongly (z diff +1.85); strongest at Niclosamide (olamine) 5 µM: 0.74x vs 2.00x (z diff +4.0) | 0.091 | ⚠ within organs, on part of the lines; also absent: DKK1, KREMEN2; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM39B]] | B | ICAM5 activity raises TMEM39B's level | lines that do not express ICAM5 (14) vs lines expressing it (36) | 1.39× lower at baseline in the lines without ICAM5 | 0.092 | ⚠ within organs, on part of the lines; also absent: MDFIC, VIM, CAV1; maybe low, not absent |
| [[ATP23]] | B | ICAM5 activity raises ATP23's level | lines that do not express ICAM5 (14) vs lines expressing it (36) | 1.36× lower at baseline in the lines without ICAM5 | 0.096 | ⚠ within organs, on part of the lines; also absent: MDFIC, VIM, CAV1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.383). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.8, -4.3); signed map (-3.9, 28.9). **Vector** length 77.0, 19.0% of its response variance represented; |z| ≥ 3 in 627 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +14.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.7 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +0.7 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +2.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -0.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.1 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | intercellular adhesion molecule 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,289,952-10,296,778 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TLN; previously TLCN |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 4 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Integrin cell surface interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMF0](https://www.uniprot.org/uniprotkb/Q9UMF0) (Intercellular adhesion molecule 5):

> Cell adhesion molecule that functions as a receptor ligand of the signaling receptor ITGAL:ITGB2/LFA-1 (lymphocyte-function associated (LFA) molecule 1) ensuring neuron cell-leukocyte adhesion. Creates homophilic cell adhesion promoting dendritogenesis and arborization of hippocampal neurons.

**Summary**, from NCBI Gene [7087](https://www.ncbi.nlm.nih.gov/gene/7087):

> The protein encoded by this gene is a member of the intercellular adhesion molecule (ICAM) family. All ICAM proteins are type I transmembrane glycoproteins, contain 2-9 immunoglobulin-like C2-type domains, and bind to the leukocyte adhesion LFA-1 protein. This protein is expressed on the surface of telencephalic neurons and displays two types of adhesion activity, homophilic binding between neurons and heterophilic binding between neurons and leukocytes. It may be a critical component in …

**Accessions** — [HGNC:5348](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5348) · Entrez [7087](https://www.ncbi.nlm.nih.gov/gene/7087) · UniProt [Q9UMF0](https://www.uniprot.org/uniprotkb/Q9UMF0) · Ensembl [ENSG00000105376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105376)

## Data

Gene col 2592: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2592); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2592, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2592]; `tensor/DDL_lfc|DDL_z.npy` [2592]; `embed/gene_vectors.npy` [2592]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2592 or target_col == 2592). Every well: [[ICAM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ICAM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

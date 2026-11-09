---
symbol: "TPRN"
type: "gene"
col: 10677
ensembl_id: "ENSG00000176058"
name: "taperin"
location: "9q34.3"
module: 119
arm: "+"
pooled_cpm: 11.65
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# TPRN

*taperin* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +9.6, q 4e-19, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.582× (z -5.0, q 4e-04, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDCD7]] (+0.75, fdr 7e-06), [[ZNF324]] (+0.74, fdr 7e-06), [[ZNF200]] (+0.68, fdr 7e-06); moves opposite to [[RAD23B]] (-0.67, fdr 7e-06), [[MRPL42]] (-0.63, fdr 6e-05), [[UBQLN1]] (-0.62, fdr 2e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10677.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +9.6 | 4e-19 | 42/44 (A549, AsPC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.39×** | +7.6 | 6e-12 | 29/39 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.21×** | +7.2 | 1e-10 | 43/47 (RKO, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.96×** | +6.1 | 1e-07 | 36/47 (RKO, A549, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.80×** | +5.3 | 1e-05 | 29/47 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.8 | 1e-04 | 24/45 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.3 | 0.002 | 20/48 (RKO, HS-578T, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.58×** | +4.2 | 0.002 | 18/34 (C32, J82, …) | two highest doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.54×** | +3.8 | 0.011 | 21/45 (NCI-H460, LS 180, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.33×** | +3.6 | 0.019 | 16/44 (NCI-H1573, PANC-1, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | 1.41× | +3.0 | 0.13 | 6/23 (Hs 766T, HT-29, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10677.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.582×** | -5.0 | 4e-04 | 26/47 (NCI-H23, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.655×** | -3.9 | 0.025 | 22/47 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.664×** | -3.8 | 0.025 | 25/47 (BT-474, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.649×** | -3.7 | 0.025 | 20/45 (HT-29, HEC-1-A, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.677×** | -3.4 | 0.064 | 20/47 (NCI-H1573, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.720× | -3.0 | 0.19 | 15/47 (C32, HT-29, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.720× | -3.0 | 0.19 | 9/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.702× | -3.0 | 0.19 | 9/47 (RKO, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 6.30 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +9.4) | [[Roxadustat (drug)]] 5 µM 0.0549× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 5.28 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +10.5) ⚠ cell-cycle shift, explains ~55% of this change | [[Verteporfin (drug)]] 5 µM 0.0693× (z -10.0) |
| [[RKO (line)]] | wt | 19.2 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 5.77× (z +8.6) ⚠ cell-cycle shift, explains ~29% of this change | [[Verteporfin (drug)]] 5 µM 0.136× (z -9.4) |
| [[A-172 (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[A549 (line)]] | wt | 7.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0586× (z -10.1) |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.169× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 7.35 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0822× (z -9.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 13.7 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0667× (z -9.1) |
| [[A-427 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD7]] | +0.75 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[ZNF324]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[ZNF200]] | +0.68 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[NCBP2AS2]] | +0.66 | +0.43 / +0.74 | both halves | 3e-05 |  |
| [[MED19]] | +0.65 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ADPRS]] | +0.64 | +0.37 / +0.73 | both halves | 7e-05 |  |
| [[BRPF1]] | +0.64 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[ARMC5]] | +0.64 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[C16orf91]] | +0.64 | +0.37 / +0.73 | both halves | 8e-05 |  |
| [[OXLD1]] | +0.63 | +0.36 / +0.75 | both halves | 9e-05 |  |
| [[ZNF593]] | +0.63 | +0.43 / +0.72 | both halves | 3e-05 |  |
| [[IRX5]] | +0.63 | +0.50 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD23B]] | -0.67 | -0.59 / -0.73 | both halves | 7e-06 |  |
| [[MRPL42]] | -0.63 | -0.38 / -0.66 | both halves | 6e-05 |  |
| [[UBQLN1]] | -0.62 | -0.46 / -0.76 | both halves | 2e-05 |  |
| [[LIN7C]] | -0.61 | -0.13 / -0.78 | ⚠ one half (not replicated) | 0.002 |  |
| [[GLO1]] | -0.60 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[PFKM]] | -0.60 | -0.34 / -0.66 | both halves | 1e-04 |  |
| [[NONO]] | -0.60 | -0.34 / -0.70 | both halves | 1e-04 |  |
| [[MAPK9]] | -0.59 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[DHFR]] | -0.58 | -0.38 / -0.68 | both halves | 6e-05 |  |
| [[EMB]] | -0.58 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SRP9]] | -0.58 | -0.33 / -0.67 | both halves | 1e-04 |  |
| [[SYNJ2BP]] | -0.58 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[GSR]] | -0.58 | -0.43 / -0.63 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TPRN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises TPRN's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SRPX2]] | B | SRPX2 activity lowers TPRN's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 1.36× higher at baseline in the lines without SRPX2 | 0.092 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.1, -13.6); signed map (-8.5, -3.9). **Vector** length 64.5, 12.5% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.8 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +9.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.2 | +1.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.1 | +1.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | -5.3 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | -5.1 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | taperin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,191,617-137,204,193 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90254; previously C9orf75, DFNB79 |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4KMQ1](https://www.uniprot.org/uniprotkb/Q4KMQ1) (Taperin):

> Essential for hearing (By similarity). Required for maintenance of stereocilia on both inner and outer hair cells (By similarity). Necessary for the integrity of the stereociliary rootlet (By similarity). May act as an actin cytoskeleton regulator involved in the regulation of actin dynamics at the pointed end in hair cells (By similarity). Forms rings at the base of stereocilia and binds actin filaments in the stereocilia which may stabilize the stereocilia (By similarity). Acts as a strong …

**Summary**, from NCBI Gene [286262](https://www.ncbi.nlm.nih.gov/gene/286262):

> This locus encodes a sensory epithelial protein. It was defined by linkage analysis in three Pakistani families to lie between D9S1818 (centromeric) and D9SH6 (telomeric). Mutations at this locus have been associated with autosomal recessive deafness. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:26894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26894) · Entrez [286262](https://www.ncbi.nlm.nih.gov/gene/286262) · UniProt [Q4KMQ1](https://www.uniprot.org/uniprotkb/Q4KMQ1) · Ensembl [ENSG00000176058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176058)

## Data

Gene col 10677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10677); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10677]; `tensor/DDL_lfc|DDL_z.npy` [10677]; `embed/gene_vectors.npy` [10677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10677 or target_col == 10677). Every well: [[TPRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

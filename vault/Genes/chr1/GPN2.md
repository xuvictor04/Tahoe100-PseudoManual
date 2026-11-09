---
symbol: "GPN2"
type: "gene"
col: 6653
ensembl_id: "ENSG00000142751"
name: "GPN-loop GTPase 2"
location: "1p36.11"
module: 114
arm: "+"
pooled_cpm: 16.78
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 2
n_dd_up_clean: 27
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# GPN2

*GPN-loop GTPase 2* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.85× (z +20.4, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.809× (z -5.9, q 2e-06, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.139×, NCI-H2030 0.202×, SK-MEL-2 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (AN3 CA 0.0937×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF586]] (+0.70, fdr 7e-06), [[ZNF529-AS1]] (+0.70, fdr 2e-05), [[GRK7]] (+0.68, fdr 1e-05); moves opposite to [[TMEM106C]] (-0.59, fdr 1e-05), [[SSX2IP]] (-0.59, fdr 3e-05), [[PSIP1]] (-0.57, fdr 3e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF790]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6653.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.85×** | +20.4 | 0e+00 | 45/47 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +16.0 | 0e+00 | 39/46 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.13×** | +14.5 | 4e-45 | 40/48 (SW480, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +14.4 | 6e-45 | 41/47 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +14.0 | 2e-42 | 35/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +13.2 | 2e-37 | 34/43 (NCI-H1573, HT-29, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +12.2 | 2e-32 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +10.6 | 2e-24 | 37/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +10.4 | 2e-23 | 37/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +10.1 | 2e-22 | 31/48 (A498, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.50×** | +9.3 | 5e-19 | 29/44 (SW480, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +7.8 | 2e-13 | 28/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +7.4 | 6e-12 | 24/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +7.3 | 8e-12 | 27/48 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +6.8 | 5e-10 | 27/47 (SW480, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +6.7 | 1e-09 | 23/47 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +6.3 | 1e-08 | 23/47 (A498, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6653.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.139×, NCI-H2030 0.202×, SK-MEL-2 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (AN3 CA 0.0937×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -5.9 | 2e-06 | 20/48 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.811×** | -4.1 | 0.011 | 12/47 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6653. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.1 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.84× (z +15.5) | — |
| [[LoVo (line)]] | wt | 19.3 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.40× (z +12.3) | — |
| [[NCI-H460 (line)]] | wt | 14.0 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.91× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 35.8 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.21× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 20.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 17.7 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.21× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 7.20× (z +12.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.52× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 15.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 23.1 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0937× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 14.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.40× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 13.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.69× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 20.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.71× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6653), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF586]] | +0.70 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ZNF529-AS1]] | +0.70 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[GRK7]] | +0.68 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[CDKL3]] | +0.67 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ZNF778]] | +0.67 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[ZNF721]] | +0.67 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[ZNF547]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZBTB8OS]] | +0.67 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TMEM222]] | +0.67 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[LRRC41]] | +0.66 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[ZNF506]] | +0.66 | +0.57 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM106C]] | -0.59 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SSX2IP]] | -0.59 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[PSIP1]] | -0.57 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ARL2]] | -0.55 | -0.34 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF790]] | B | ZNF790 activity raises GPN2's level | lines that do not express ZNF790 (14) vs lines expressing it (36) | 1.10× lower at baseline in the lines without ZNF790 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZNF345, ZNF606, ZNF569 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.778). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.8, 9.0); signed map (1.5, -2.9). **Vector** length 76.2, 14.3% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.1 | +20.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +10.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +14.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +14.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +9.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -5.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.7 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -0.0 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.4 | -0.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | GPN-loop GTPase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,876,132-26,890,283 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10349; previously ATPBD1B |
| Gene groups (HGNC) | GPN-loop GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9Y4](https://www.uniprot.org/uniprotkb/Q9H9Y4) (GPN-loop GTPase 2):

> Small GTPase involved in the correct assembly of RNA polymerase RNA polymerase II and III (RNAPII and RNAPIII) complexes, ensuring their proper nuclear import.

**Summary**, from NCBI Gene [54707](https://www.ncbi.nlm.nih.gov/gene/54707):

> Predicted to enable GTPase activity. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25513) · Entrez [54707](https://www.ncbi.nlm.nih.gov/gene/54707) · UniProt [Q9H9Y4](https://www.uniprot.org/uniprotkb/Q9H9Y4) · Ensembl [ENSG00000142751](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142751)

## Data

Gene col 6653: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6653); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6653, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6653]; `tensor/DDL_lfc|DDL_z.npy` [6653]; `embed/gene_vectors.npy` [6653]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6653 or target_col == 6653). Every well: [[GPN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "OSCP1"
type: "gene"
col: 3852
ensembl_id: "ENSG00000116885"
name: "organic solute carrier partner 1"
location: "1p34.3"
module: 12
arm: "+"
pooled_cpm: 4.71
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# OSCP1

*organic solute carrier partner 1* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.88× (z +18.7, q 0e+00, up in 32 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.594× (z -9.1, q 4e-17, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MORN2]] (+0.78, fdr 7e-06), [[DRC3]] (+0.75, fdr 7e-06), [[BBOF1]] (+0.68, fdr 7e-06); moves opposite to [[USB1]] (-0.59, fdr 1e-05), [[ARHGAP8]] (-0.59, fdr 2e-05), [[GART]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EFCAB6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3852.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.88×** | +18.7 | 0e+00 | 32/37 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +15.2 | 0e+00 | 35/39 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.30×** | +10.0 | 3e-21 | 22/42 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +7.4 | 2e-11 | 18/36 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.81×** | +7.4 | 2e-11 | 20/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +6.8 | 8e-10 | 19/45 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +6.4 | 1e-08 | 19/46 (CFPAC-1, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +6.3 | 2e-08 | 12/29 (NCI-H2030, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +6.1 | 6e-08 | 16/44 (LS 180, HOP62, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.49×** | +6.0 | 2e-07 | 15/41 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +4.9 | 4e-05 | 18/45 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.48×** | +4.9 | 4e-05 | 16/42 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +4.6 | 2e-04 | 4/11 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Sulfatinib (drug)]] 5 µM |  | **1.45×** | +4.5 | 3e-04 | 8/42 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.003 | 8/45 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.028 | 6/44 (HOP62, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +3.3 | 0.034 | 7/36 (LoVo, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3852.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.594×** | -9.1 | 4e-17 | 27/45 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.603×** | -6.3 | 1e-07 | 18/43 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.673×** | -4.9 | 2e-04 | 16/35 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.698×** | -4.4 | 1e-03 | 7/45 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.699×** | -4.4 | 1e-03 | 17/46 (RPMI-7951, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.700×** | -4.4 | 1e-03 | 13/43 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.737×** | -3.8 | 0.013 | 11/43 (SW480, H4, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.747×** | -3.6 | 0.021 | 9/43 (NCI-H23, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.739×** | -3.6 | 0.021 | 13/30 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.772×** | -3.2 | 0.078 | 13/42 (COLO 205, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Peretinoin (drug)]] 5 µM |  | 0.772× | -3.1 | 0.11 | 9/44 (NCI-H1792, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3852. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 5.87 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +12.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0978× (z -9.7) ⚠ cell-cycle shift, explains ~88% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.107× (z -9.4) |
| [[SW1417 (line)]] | alt | 2.68 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.05 µM 0.0578× (z -9.2) |
| [[A-427 (line)]] | wt | 4.06 | 0 | 1 | — | [[Malotilate (drug)]] 0.5 µM 0.0650× (z -9.8) |
| [[A498 (line)]] | wt | 3.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 8.03 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM 0.0526× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 4.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 3.19 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0646× (z -8.5) |
| [[KATO III (line)]] | alt | 3.12 | 0 | 1 | — | [[Nafamostat (mesylate) (drug)]] 0.05 µM 0.0684× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 5.82 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0743× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 4.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 4.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +11.7) | — |
| [[SW480 (line)]] | alt | 4.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +11.0) | — |
| [[A-172 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3852), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MORN2]] | +0.78 | +0.78 / +0.72 | both halves | 7e-06 | STRING 420 |
| [[DRC3]] | +0.75 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[BBOF1]] | +0.68 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[CLUAP1]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[DNAJC27]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ANKRD49]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ZNF446]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PI4KB]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CWC25]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[LRRC27]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[TOGARAM1]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[DNAL4]] | +0.63 | +0.68 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USB1]] | -0.59 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[ARHGAP8]] | -0.59 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[GART]] | -0.58 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[LYPLA1]] | -0.57 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[SRPK1]] | -0.57 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[IPO7]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 | same gene group |
| [[METAP1]] | -0.55 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[MCOLN2]] | -0.55 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[TMEM241]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[PRRG1]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[SEH1L]] | -0.54 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[DIAPH1]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFCAB6]] | B | EFCAB6 activity raises OSCP1's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without EFCAB6 | 0.025 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[ODAD4]] | C | ODAD4 activity raises OSCP1's level | lines that do not express ODAD4 (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without ODAD4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: GGT7, NAT14, SOGA1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-41.8, 19.9); signed map (-7.3, -3.4). **Vector** length 69.4, 11.4% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +18.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +15.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.2 | +6.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.4 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.1 | -6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.8 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | +0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | organic solute carrier partner 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:36,415,827-36,450,451 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOR1; previously C1orf102 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVF1](https://www.uniprot.org/uniprotkb/Q8WVF1) (Protein OSCP1):

> May be involved in drug clearance in the placenta.

**Summary**, from NCBI Gene [127700](https://www.ncbi.nlm.nih.gov/gene/127700):

> Enables transmembrane transporter activity. Involved in xenobiotic detoxification by transmembrane export across the plasma membrane. Located in basal plasma membrane and cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29971) · Entrez [127700](https://www.ncbi.nlm.nih.gov/gene/127700) · UniProt [Q8WVF1](https://www.uniprot.org/uniprotkb/Q8WVF1) · Ensembl [ENSG00000116885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116885)

## Data

Gene col 3852: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3852); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3852, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3852]; `tensor/DDL_lfc|DDL_z.npy` [3852]; `embed/gene_vectors.npy` [3852]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3852 or target_col == 3852). Every well: [[OSCP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSCP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "KEAP1"
type: "gene"
col: 1271
ensembl_id: "ENSG00000079999"
name: "kelch like ECH associated protein 1"
location: "19p13.2"
module: 7
arm: "+"
pooled_cpm: 16.92
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# KEAP1

*kelch like ECH associated protein 1* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.74× (z +7.4, q 6e-11, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.300× (z -17.0, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SART3]] (+0.70, fdr 7e-06), [[MCRS1]] (+0.69, fdr 7e-06), [[PSMD7]] (+0.68, fdr 1e-05); moves opposite to [[NPTN]] (-0.59, fdr 1e-05), [[AP1S2]] (-0.56, fdr 3e-05), [[EPB41L2]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1271.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +7.4 | 6e-11 | 31/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +6.9 | 2e-09 | 31/47 (COLO 205, SW480, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +6.6 | 8e-09 | 30/47 (COLO 205, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +5.0 | 9e-05 | 21/43 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.015 | 10/48 (HT-29, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.070 | 8/46 (RPMI-7951, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.089 | 7/48 (H4, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1271.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.300×** | -17.0 | 0e+00 | 46/48 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.313×** | -16.4 | 0e+00 | 47/47 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.317×** | -16.2 | 0e+00 | 46/48 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.467×** | -15.2 | 0e+00 | 38/47 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.427×** | -12.0 | 3e-31 | 43/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -9.8 | 1e-20 | 34/47 (A-172, SHP-77, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.362×** | -7.5 | 5e-12 | 36/48 (SHP-77, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.688×** | -7.5 | 6e-12 | 37/48 (SW480, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.605×** | -7.1 | 8e-11 | 28/47 (SK-MEL-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.614×** | -6.9 | 3e-10 | 32/47 (SW 900, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.631×** | -6.5 | 4e-09 | 32/48 (SW 1271, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -6.4 | 8e-09 | 28/48 (SNU-1, BT-474, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.631×** | -6.3 | 2e-08 | 27/47 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.650×** | -6.1 | 5e-08 | 26/41 (SNU-1, HS-578T, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.676×** | -5.5 | 1e-06 | 25/46 (PANC-1, LS 180, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -4.8 | 5e-05 | 24/46 (A-172, SW48, …) | top dose only | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1271. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 26.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -14.2) |
| [[LS 180 (line)]] | wt | 25.5 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 17.4 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.256× (z -10.0) |
| [[SW480 (line)]] | alt | 17.2 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -11.6) |
| [[A-427 (line)]] | wt | 28.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -22.4) |
| [[A498 (line)]] | wt | 26.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -14.9) |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 4 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0820× (z -13.7) |
| [[HT-29 (line)]] | alt | 15.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0834× (z -16.0) |
| [[KATO III (line)]] | alt | 17.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -13.1) |
| [[PANC-1 (line)]] | alt | 15.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -12.3) |
| [[SNU-1 (line)]] | wt | 38.2 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0672× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 17.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -10.9) |
| [[SHP-77 (line)]] | alt | 21.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.220× (z -9.7) |
| [[SNU-423 (line)]] | alt | 14.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -12.1) |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -11.9) |
| [[LoVo (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[NCI-H1573 (line)]] | alt | 9.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.9) |
| [[RKO (line)]] | wt | 21.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.148× (z -9.8) |
| [[SW48 (line)]] | wt | 19.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0950× (z -10.4) |
| [[A549 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1271), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SART3]] | +0.70 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[MCRS1]] | +0.69 | +0.59 / +0.67 | both halves | 7e-06 | pathway: Deubiquitination |
| [[PSMD7]] | +0.68 | +0.56 / +0.66 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 543 |
| [[PSMB5]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 647 |
| [[RHBDD3]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CUL1]] | +0.66 | +0.61 / +0.57 | both halves | 9e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 918 |
| [[GPATCH3]] | +0.65 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[YTHDF2]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[PHYKPL]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[TSSC4]] | +0.64 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[PEX14]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[AKAP8]] | +0.63 | +0.49 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPTN]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[AP1S2]] | -0.56 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[EPB41L2]] | -0.56 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[SEPTIN2]] | -0.56 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PPFIBP1]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[C12orf75]] | -0.55 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[APLP2]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[COTL1]] | -0.54 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[IL1RAP]] | -0.53 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers KEAP1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-42.9, 11.3); signed map (-7.3, -19.3). **Vector** length 93.2, 21.8% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.9 | +6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.5 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.0 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.7 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +2.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -4.5 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.9 | -4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -3.8 | -4.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -12.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -7.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | kelch like ECH associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,486,125-10,503,558 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0132, MGC10630, MGC1114, MGC20887, MGC4407, MGC9454, INrf2, KLHL19 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Reactome | 14 pathways, smallest: Potential therapeutics for SARS; Nuclear events mediated by NFE2L2; KEAP1-NFE2L2 pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14145](https://www.uniprot.org/uniprotkb/Q14145) (Kelch-like ECH-associated protein 1):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex that regulates the response to oxidative stress by targeting NFE2L2/NRF2 for ubiquitination. KEAP1 acts as a key sensor of oxidative and electrophilic stress: in normal conditions, the BCR(KEAP1) complex mediates ubiquitination and degradation of NFE2L2/NRF2, a transcription factor regulating expression of many cytoprotective genes. In response to oxidative stress, different electrophile metabolites trigger …

**Summary**, from NCBI Gene [9817](https://www.ncbi.nlm.nih.gov/gene/9817):

> This gene encodes a cytoplasmic regulatory protein that plays a role in the cellular response to oxidative and electrophilic stress. The encoded protein regulates NRF2, a transcription factor that controls the expression of antioxidant and cytoprotective genes. Under non-stress conditions, KEAP1 binds NRF2 and promotes its ubiquitination and proteasomal degradation, thereby maintaining low NRF2 levels. During oxidative or electrophilic stress, conformational changes in KEAP1 impair its ability …

**Accessions** — [HGNC:23177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23177) · Entrez [9817](https://www.ncbi.nlm.nih.gov/gene/9817) · UniProt [Q14145](https://www.uniprot.org/uniprotkb/Q14145) · Ensembl [ENSG00000079999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079999)

## Data

Gene col 1271: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1271); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1271, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1271]; `tensor/DDL_lfc|DDL_z.npy` [1271]; `embed/gene_vectors.npy` [1271]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1271 or target_col == 1271). Every well: [[KEAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KEAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

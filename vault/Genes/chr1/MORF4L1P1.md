---
symbol: "MORF4L1P1"
type: "gene"
col: 13290
ensembl_id: "ENSG00000218283"
name: "mortality factor 4 like 1 pseudogene 1"
location: "1q41"
module: 42
arm: "+"
pooled_cpm: 6.14
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# MORF4L1P1

*mortality factor 4 like 1 pseudogene 1* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.58× (z +15.5, q 0e+00, up in 30 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.51× (z +4.2, q 0.003, up in 12 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 5.54×, HOP62 8.05×, A-172 7.70×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 6.87×, HT-29 5.94×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.618× (z -4.9, q 5e-04, down in 22 of 42 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SF3B1]] (+0.61, fdr 1e-05), [[ZC3H11A]] (+0.54, fdr 2e-05), [[ARCN1]] (+0.54, fdr 2e-05); moves opposite to [[SDHAF1]] (-0.55, fdr 1e-04), [[MFSD14CP]] (-0.51, fdr 4e-05), [[TSEN54]] (-0.49, fdr 5e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DSP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13290.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 5.54×, HOP62 8.05×, A-172 7.70×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 6.87×, HT-29 5.94×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.58×** | +15.5 | 0e+00 | 30/30 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.66×** | +15.1 | 0e+00 | 10/10 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +9.6 | 1e-19 | 17/21 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +4.5 | 8e-04 | 2/13 (NCI-H2347, NCI-H23) | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.003 | 12/44 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.49×** | +4.1 | 0.004 | 12/35 (A549, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.8 | 0.014 | 11/35 (HEC-1-A, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.44×** | +3.7 | 0.014 | 10/47 (PANC-1, LOX-IMVI, …) | rises with dose | composition shift |
| [[Flutamide (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.041 | 14/44 (NCI-H2030, CFPAC-1, …) | two highest doses | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.81×** | +3.2 | 0.084 | 5/38 (PANC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13290.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.618×** | -4.9 | 5e-04 | 22/42 (C32, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Decitabine (drug)]] 0.05 µM |  | **0.623×** | -4.5 | 0.002 | 17/41 (hTERT-HPNE, KATO III, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.438×** | -4.4 | 0.002 | 20/42 (NCI-H1573, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.651×** | -4.4 | 0.002 | 16/47 (NCI-H1573, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.671×** | -4.1 | 0.006 | 14/47 (HT-29, KATO III, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.681×** | -3.9 | 0.009 | 15/47 (KATO III, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Allantoin (drug)]] 0.5 µM |  | **0.714×** | -3.4 | 0.050 | 6/42 (COLO 205, HCT15, …) | two highest doses | position effect removed |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **0.723×** | -3.3 | 0.069 | 16/42 (KATO III, HCT15, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -3.2 | 0.084 | 13/47 (NCI-H1573, LOX-IMVI, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.27 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.05× (z +9.3) ⚠ toxic; transcription drop | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.106× (z -10.0) |
| [[PANC-1 (line)]] | alt | 7.90 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.87× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 6.48 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.70× (z +9.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 3.72 | 0 | 1 | — | [[PH-797804 (drug)]] 0.05 µM 0.0474× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 7.74 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0760× (z -8.8) |
| [[HT-29 (line)]] | alt | 9.30 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.94× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 4.03 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.134× (z -8.9) |
| [[SNU-423 (line)]] | alt | 4.94 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0945× (z -8.6) |
| [[A-427 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B1]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ZC3H11A]] | +0.54 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[ARCN1]] | +0.54 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[SF3A1]] | +0.53 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[USO1]] | +0.52 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[LIN7C]] | +0.51 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[SRRM2]] | +0.51 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[HUWE1]] | +0.51 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[HDLBP]] | +0.51 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[EIF4H]] | +0.50 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[DYNC1LI2]] | +0.50 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[ACIN1]] | +0.50 | +0.42 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF1]] | -0.55 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[MFSD14CP]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[TSEN54]] | -0.49 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[PHAF1]] | -0.49 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[SMPD4BP]] | -0.48 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[NXT1]] | -0.47 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[FAM222B]] | -0.47 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[DEXI]] | -0.47 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[TMEM11]] | -0.47 | -0.26 / -0.53 | both halves | 4e-04 |  |
| [[GFOD2]] | -0.46 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[NCBP2AS2]] | -0.46 | -0.28 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSP]] | B | DSP activity raises MORF4L1P1's level | lines that do not express DSP (17) vs lines expressing it (33) | 1.11× lower at baseline in the lines without DSP | 0.057 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, GRB7, SFN; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises MORF4L1P1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.147). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.9, -17.1); signed map (13.3, -28.0). **Vector** length 44.6, 4.80% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +15.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +9.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.4 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +1.1 | +1.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -1.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.1 | -4.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.0 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | mortality factor 4 like 1 pseudogene 1 |
| Locus type | pseudogene |
| Location | 1q41 — chr1:220,253,570-220,254,536 (+) |
| Ensembl biotype | processed_pseudogene |
| Also known as | MRG1; previously MORF4LP1 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:20400](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20400) · Entrez [326591](https://www.ncbi.nlm.nih.gov/gene/326591) · Ensembl [ENSG00000218283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000218283)

## Data

Gene col 13290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13290); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13290]; `tensor/DDL_lfc|DDL_z.npy` [13290]; `embed/gene_vectors.npy` [13290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13290 or target_col == 13290). Every well: [[MORF4L1P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MORF4L1P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

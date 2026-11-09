---
symbol: "RAB29"
type: "gene"
col: 3891
ensembl_id: "ENSG00000117280"
name: "RAB29, member RAS oncogene family"
location: "1q32.1"
module: 14
arm: "+"
pooled_cpm: 14.73
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# RAB29

*RAB29, member RAS oncogene family* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.37× (z +8.6, q 3e-15, up in 26 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.55× (z +6.2, q 9e-08, up in 25 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.486× (z -7.2, q 4e-10, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTN2A2]] (+0.64, fdr 7e-06), [[ARMCX1]] (+0.57, fdr 1e-05), [[PLD6]] (+0.57, fdr 1e-05); moves opposite to [[FBH1]] (-0.57, fdr 3e-05), [[PDCD6]] (-0.53, fdr 6e-05), [[DGCR8]] (-0.50, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MCOLN3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +8.6 | 3e-15 | 26/37 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +7.3 | 7e-11 | 18/23 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +6.2 | 9e-08 | 25/45 (NCI-H1792, HS-578T, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.1 | 5e-05 | 25/46 (A-427, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.57×** | +4.6 | 5e-04 | 26/45 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.6 | 5e-04 | 26/46 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.4 | 8e-04 | 28/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.5 | 0.032 | 16/41 (C32, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.16 | 13/45 (J82, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3891.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.486×** | -7.2 | 4e-10 | 30/45 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -6.1 | 4e-07 | 27/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.333×** | -5.7 | 2e-06 | 35/42 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.622×** | -4.7 | 3e-04 | 23/45 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.436×** | -4.3 | 0.002 | 25/46 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.663×** | -4.1 | 0.004 | 24/44 (HCT15, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.687×** | -3.6 | 0.023 | 18/44 (NCI-H2030, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.539×** | -3.2 | 0.090 | 17/43 (SNU-1, C32, …) | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.738× | -3.0 | 0.16 | 15/45 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.83 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0792× (z -9.9) |
| [[PANC-1 (line)]] | alt | 12.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.186× (z -11.1) |
| [[A-172 (line)]] | wt | 34.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.5) | — |
| [[A-427 (line)]] | wt | 21.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0676× (z -9.2) |
| [[A549 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -8.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -9.4) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -8.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 18.4 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.143× (z -10.0) |
| [[SW480 (line)]] | alt | 11.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -9.4) |
| [[A498 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN2A2]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ARMCX1]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[PLD6]] | +0.57 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[GNPDA1]] | +0.56 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[LITAF]] | +0.55 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[DUSP15]] | +0.55 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SNX2]] | +0.54 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[RAB32]] | +0.54 | +0.55 / +0.46 | both halves | 3e-05 | same gene group; pathway: RAB geranylgeranylation |
| [[FLCN]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CHMP2B]] | +0.53 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[LINC02428]] | +0.52 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[HSBP1L1]] | +0.52 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBH1]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PDCD6]] | -0.53 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[DGCR8]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[ILF2]] | -0.50 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[NOMO2]] | -0.50 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[CHID1]] | -0.49 | -0.51 / -0.45 | both halves | 3e-05 | STRING 417 |
| [[ODF2]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[NDOR1]] | -0.49 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[ABHD17A]] | -0.48 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[RECQL]] | -0.48 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[SPCS3]] | -0.47 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[DTYMK]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN3]] | B | MCOLN3 activity raises RAB29's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without MCOLN3 | 0.015 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |
| [[PPM1H]] | B | PPM1H activity raises RAB29's level | lines that do not express PPM1H (11) vs lines expressing it (39) | 1.17× lower at baseline in the lines without PPM1H | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, MGST2, CXCL16; maybe low, not absent |
| [[RRAGD]] | B | RRAGD activity raises RAB29's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.72× lower at baseline in the lines without RRAGD | 0.089 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.505). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.5, 16.8); signed map (15.6, -14.4). **Vector** length 78.3, 17.2% of its response variance represented; |z| ≥ 3 in 772 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +6.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +4.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.4 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +4.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | -0.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -7.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -5.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | RAB29, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:205,767,986-205,775,482 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RAB7L, RAB7L1 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [O14966](https://www.uniprot.org/uniprotkb/O14966) (Ras-related protein Rab-29):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (By similarity). RAB29 is essential for maintaining the integrity of the endosome-trans-Golgi network structure (By …

**Summary**, from NCBI Gene [8934](https://www.ncbi.nlm.nih.gov/gene/8934):

> Enables several functions, including G protein activity; dynein complex binding activity; and guanyl ribonucleotide binding activity. Involved in several processes, including positive regulation of T cell receptor signaling pathway; positive regulation of receptor recycling; and regulation of plasma membrane bounded cell projection organization. Located in several cellular components, including Golgi apparatus; endosome; and vacuole. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9789](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9789) · Entrez [8934](https://www.ncbi.nlm.nih.gov/gene/8934) · UniProt [O14966](https://www.uniprot.org/uniprotkb/O14966) · Ensembl [ENSG00000117280](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117280)

## Data

Gene col 3891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3891); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3891]; `tensor/DDL_lfc|DDL_z.npy` [3891]; `embed/gene_vectors.npy` [3891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3891 or target_col == 3891). Every well: [[RAB29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "HLA-F"
type: "gene"
col: 12909
ensembl_id: "ENSG00000204642"
name: "major histocompatibility complex, class I, F"
location: "6p22.1"
module: 70
arm: "+"
pooled_cpm: 22.35
n_lines_expressing: 40
n_dd_up: 15
n_dd_down: 32
n_dd_up_clean: 14
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 53
direction_downstream: 33
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# HLA-F

*major histocompatibility complex, class I, F* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +8.1, q 3e-13, up in 24 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.492× (z -8.8, q 5e-16, down in 25 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B2M]] (+0.84, fdr 7e-06), [[HLA-B]] (+0.83, fdr 7e-06), [[PLEKHA4]] (+0.80, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[MX1]] → it (grade B ⚠); 33 go from it, the strongest it → [[HLA-E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12909.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +8.1 | 3e-13 | 24/38 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +7.9 | 8e-13 | 20/36 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +6.6 | 8e-09 | 25/38 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.7 | 5e-04 | 19/38 (HT-29, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.36×** | +3.9 | 0.011 | 17/38 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.9 | 0.011 | 15/35 (Hs 766T, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.55×** | +3.7 | 0.015 | 16/37 (A498, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.021 | 12/37 (HS-578T, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.021 | 17/38 (AsPC-1, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.023 | 20/36 (AsPC-1, RKO, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.037 | 17/37 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.037 | 12/36 (SK-MEL-2, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.056 | 10/38 (AsPC-1, J82, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.064 | 16/38 (J82, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.097 | 10/38 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 3 with an alert ⚠; shown: the 15 strongest. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12909.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.492×** | -8.8 | 5e-16 | 25/38 (COLO 205, SNU-423, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.621×** | -8.4 | 1e-14 | 25/38 (A549, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.559×** | -7.2 | 9e-11 | 23/38 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.634×** | -5.7 | 2e-06 | 22/38 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.649×** | -5.4 | 9e-06 | 23/38 (LoVo, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.614×** | -5.3 | 9e-06 | 23/37 (COLO 205, A549, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[EX229 (drug)]] 5 µM |  | **0.436×** | -5.1 | 3e-05 | 22/38 (SW 900, J82, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.670×** | -5.0 | 4e-05 | 18/38 (COLO 205, A498, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.691×** | -4.6 | 3e-04 | 22/38 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.667×** | -4.4 | 5e-04 | 18/38 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.701×** | -4.4 | 5e-04 | 18/38 (CFPAC-1, BT-474, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.705×** | -4.4 | 6e-04 | 18/38 (AsPC-1, A498, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.501×** | -4.2 | 0.001 | 19/36 (SK-MEL-2, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.728×** | -3.9 | 0.003 | 13/38 (A549, A498, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.799×** | -3.9 | 0.003 | 20/38 (SW 1088, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 83.7 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0858× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.255× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 17.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +15.1) | — |
| [[A498 (line)]] | wt | 30.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.277× (z -11.5) |
| [[A549 (line)]] | wt | 19.8 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.249× (z -10.7) |
| [[A-172 (line)]] | wt | 34.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.129× (z -8.6) |
| [[C32 (line)]] | wt | 7.31 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0447× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 65.3 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.456× (z -8.9) |
| [[J82 (line)]] | alt | 73.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 28.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 44.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 46.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.289× (z -8.7) |
| [[SNU-423 (line)]] | alt | 59.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.278× (z -9.6) |
| [[A-427 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.97 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.37 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.44 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B2M]] | +0.84 | +0.76 / +0.88 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 999 |
| [[HLA-B]] | +0.83 | +0.78 / +0.85 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 982 |
| [[PLEKHA4]] | +0.80 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[IFIH1]] | +0.79 | +0.73 / +0.79 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[GBP4]] | +0.79 | +0.70 / +0.81 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[PSMB9]] | +0.79 | +0.69 / +0.82 | both halves | 7e-06 | pathway: Antigen processing-Cross presentation; STRING 723 |
| [[TAP1]] | +0.79 | +0.70 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_UP; STRING 832 |
| [[ISG15]] | +0.78 | +0.75 / +0.80 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 417 |
| [[HLA-E]] | +0.78 | +0.70 / +0.80 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; STRING 997 |
| [[CFB]] | +0.77 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[IFI27]] | +0.77 | +0.69 / +0.78 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[PSME2]] | +0.77 | +0.61 / +0.77 | both halves | 7e-06 | pathway: Antigen processing-Cross presentation; STRING 452 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 49, C 4. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MX1]] | B | MX1 activity strengthens HLA-F's drug response | lines that do not express MX1 (13) vs lines expressing it (25) | the lines without MX1 respond 0.58× as strongly (z diff +1.19); strongest at Auranofin 5 µM: 0.86x vs 0.44x (z diff +4.6) | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1; target measured in part of the lines; artifact flags |
| [[MX1]] | B | MX1 activity raises HLA-F's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.31× lower at baseline in the lines without MX1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[IFI44L]] | B | IFI44L activity raises HLA-F's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without IFI44L | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[KMO]] | B | KMO activity raises HLA-F's level | lines that do not express KMO (18) vs lines expressing it (32) | 2.45× lower at baseline in the lines without KMO | 0.006 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[CTSS]] | B | CTSS activity raises HLA-F's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without CTSS | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity strengthens HLA-F's drug response | lines that do not express OAS2 (10) vs lines expressing it (28) | the lines without OAS2 respond 0.48× as strongly (z diff +1.31); strongest at Auranofin 5 µM: 0.84x vs 0.47x (z diff +4.3) | 0.006 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[GBP4]] | B | GBP4 activity raises HLA-F's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without GBP4 | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[GBP1]] | B | GBP1 activity raises HLA-F's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.42× lower at baseline in the lines without GBP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[EPSTI1]] | B | EPSTI1 activity raises HLA-F's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.78× lower at baseline in the lines without EPSTI1 | 0.009 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[HCP5]] | B | HCP5 activity raises HLA-F's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 2.39× lower at baseline in the lines without HCP5 | 0.010 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[RARRES1]] | B | RARRES1 activity raises HLA-F's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 2.65× lower at baseline in the lines without RARRES1 | 0.011 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |
| [[TYMP]] | B | TYMP activity raises HLA-F's level | lines that do not express TYMP (20) vs lines expressing it (30) | 2.30× lower at baseline in the lines without TYMP | 0.012 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 32, C 1. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-E]] | B | HLA-F activity raises HLA-E's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 2.38× lower at baseline in the lines without HLA-F | 0.002 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[HLA-A]] | B | HLA-F activity raises HLA-A's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 3.01× lower at baseline in the lines without HLA-F | 0.002 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[MOB3C]] | B | HLA-F activity raises MOB3C's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.68× lower at baseline in the lines without HLA-F | 0.008 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[PSMB8]] | B | HLA-F activity raises PSMB8's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 2.21× lower at baseline in the lines without HLA-F | 0.011 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[NFKB2]] | B | HLA-F activity raises NFKB2's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.45× lower at baseline in the lines without HLA-F | 0.019 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[HLA-H]] | B | HLA-F activity raises HLA-H's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 2.24× lower at baseline in the lines without HLA-F | 0.025 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[IFITM3]] | B | HLA-F activity raises IFITM3's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 2.41× lower at baseline in the lines without HLA-F | 0.026 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[GSDMD]] | B | HLA-F activity raises GSDMD's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.77× lower at baseline in the lines without HLA-F | 0.032 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[ALPK1]] | B | HLA-F activity raises ALPK1's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without HLA-F | 0.034 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[GBP4]] | B | HLA-F activity raises GBP4's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 3.19× lower at baseline in the lines without HLA-F | 0.051 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[SLC41A2]] | B | HLA-F activity raises SLC41A2's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.51× lower at baseline in the lines without HLA-F | 0.052 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[HCP5]] | B | HLA-F activity raises HCP5's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.89× lower at baseline in the lines without HLA-F | 0.054 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.875). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.3, 50.6); signed map (64.1, 28.2). **Vector** length 114, 33.1% of its response variance represented; |z| ≥ 3 in 856 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.65 to 25); *interferon alpha response* (hallmark, mean cos +0.65 to 19); *allograft rejection* (hallmark, mean cos +0.69 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +1.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.9 | -8.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.5 | -5.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.5 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -8.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.1 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | major histocompatibility complex, class I, F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:29,722,775-29,738,528 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Histocompatibility complex; C1-set domain containing |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 16 pathways, smallest: Endosomal/Vacuolar pathway; Antigen Presentation: Folding, assembly and peptide loading of class I MHC; Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell |
| Matched by | ensembl_id |

**Function**, from UniProt [P30511](https://www.uniprot.org/uniprotkb/P30511) (HLA class I histocompatibility antigen, alpha chain F):

> Non-classical major histocompatibility class Ib molecule postulated to play a role in immune surveillance, immune tolerance and inflammation. Functions in two forms, as a heterotrimeric complex with B2M/beta-2 microglobulin and a peptide (peptide-bound HLA-F-B2M) and as an open conformer (OC) devoid of peptide and B2M (peptide-free OC). In complex with B2M, presents non-canonical self-peptides carrying post-translational modifications, particularly phosphorylated self-peptides. Peptide-bound …

**Summary**, from NCBI Gene [3134](https://www.ncbi.nlm.nih.gov/gene/3134):

> This gene belongs to the HLA class I heavy chain paralogues. It encodes a non-classical heavy chain that forms a heterodimer with a beta-2 microglobulin light chain, with the heavy chain anchored in the membrane. Unlike most other HLA heavy chains, this molecule is localized in the endoplasmic reticulum and Golgi apparatus, with a small amount present at the cell surface in some cell types. It contains a divergent peptide-binding groove, and is thought to bind a restricted subset of peptides …

**Accessions** — [HGNC:4963](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4963) · Entrez [3134](https://www.ncbi.nlm.nih.gov/gene/3134) · UniProt [P30511](https://www.uniprot.org/uniprotkb/P30511) · Ensembl [ENSG00000204642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204642)

## Data

Gene col 12909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12909); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12909]; `tensor/DDL_lfc|DDL_z.npy` [12909]; `embed/gene_vectors.npy` [12909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12909 or target_col == 12909). Every well: [[HLA-F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

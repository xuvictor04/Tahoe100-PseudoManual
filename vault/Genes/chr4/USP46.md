---
symbol: "USP46"
type: "gene"
col: 3037
ensembl_id: "ENSG00000109189"
name: "ubiquitin specific peptidase 46"
location: "4q12"
module: 18
arm: "+"
pooled_cpm: 20.6
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# USP46

*ubiquitin specific peptidase 46* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.79× (z +11.8, q 1e-29, up in 28 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.21× (z +5.7, q 1e-06, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.478× (z -15.5, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPHS1]] (+0.73, fdr 7e-06), [[NAE1]] (+0.71, fdr 7e-06), [[RAB11FIP2]] (+0.70, fdr 7e-06); moves opposite to [[NBEAL1]] (-0.55, fdr 1e-04), [[GALE]] (-0.54, fdr 3e-05), [[ING1]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MYO1E]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3037.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +11.8 | 1e-29 | 28/34 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +10.0 | 5e-21 | 26/44 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.27×** | +7.1 | 2e-10 | 23/48 (A-427, A-172, …) | top dose only | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.90×** | +7.1 | 2e-10 | 24/39 (A498, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.7 | 1e-06 | 21/48 (A498, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +4.9 | 9e-05 | 14/48 (C32, LS 180, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +4.6 | 4e-04 | 21/41 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +4.2 | 0.002 | 14/47 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.063 | 13/47 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.067 | 10/48 (SW480, A549, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | 1.11× | +3.2 | 0.077 | 5/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.0 | 0.11 | 3/48 (A-427, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3037.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.478×** | -15.5 | 0e+00 | 38/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.486×** | -15.2 | 0e+00 | 38/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.677×** | -8.2 | 5e-14 | 28/47 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.895× | -7.7 | 2e-12 | 4/48 (HOP62, SW 1271, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.796×** | -6.8 | 1e-09 | 23/47 (NCI-H23, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.716×** | -6.7 | 1e-09 | 21/48 (NCI-H23, A-172, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.576×** | -6.1 | 1e-07 | 19/48 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.794×** | -4.7 | 2e-04 | 17/45 (A498, HEC-1-A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.812×** | -4.4 | 7e-04 | 19/46 (NCI-H460, BT-474, …) | rises with dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.689×** | -4.1 | 0.002 | 11/46 (PANC-1, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.831×** | -3.9 | 0.005 | 14/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.728×** | -3.5 | 0.022 | 14/46 (NCI-H1573, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Monocrotaline (drug)]] 0.05 µM |  | 0.842× | -3.3 | 0.036 | 11/46 (SK-MEL-2, Hs 766T, …) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.5 µM |  | 0.859× | -3.2 | 0.057 | 9/48 (CHP-212, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.3 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.260× (z -12.6) |
| [[SW480 (line)]] | alt | 20.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.278× (z -12.3) |
| [[A549 (line)]] | wt | 15.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -9.1) |
| [[C-33 A (line)]] | alt | 56.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.332× (z -9.2) |
| [[HOP62 (line)]] | alt | 13.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 18.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.296× (z -8.9) |
| [[RKO (line)]] | wt | 34.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.266× (z -10.4) |
| [[A-427 (line)]] | wt | 41.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.115× (z -9.2) ⚠ cell-cycle shift, explains ~63% of this change |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 33.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.402× (z -10.2) |
| [[LoVo (line)]] | wt | 21.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H23 (line)]] | alt | 56.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -20.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2347 (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -13.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPHS1]] | +0.73 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[NAE1]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[RAB11FIP2]] | +0.70 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[NSMAF]] | +0.68 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SLC35G1]] | +0.67 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[HDGFL3]] | +0.65 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[MVB12B]] | +0.65 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[MACROH2A2]] | +0.65 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[AK3]] | +0.64 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[RNASEH2B]] | +0.64 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[MARK1]] | +0.64 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[PYGO1]] | +0.63 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBEAL1]] | -0.55 | -0.54 / -0.32 | both halves | 1e-04 |  |
| [[GALE]] | -0.54 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ING1]] | -0.54 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[LGALS1]] | -0.52 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CASP9]] | -0.52 | -0.34 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1E]] | B | MYO1E activity lowers USP46's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 2.06× higher at baseline in the lines without MYO1E | 0.006 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[ADAM8]] | B | ADAM8 activity lowers USP46's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.38× higher at baseline in the lines without ADAM8 | 0.022 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[FAXC]] | B | FAXC activity raises USP46's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without FAXC | 0.029 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[ADAM8]] | B | ADAM8 activity weakens USP46's drug response | lines that do not express ADAM8 (28) vs lines expressing it (20) | the lines without ADAM8 respond 1.31× as strongly (z diff -0.85); strongest at Panobinostat 0.5 µM: 0.44x vs 0.60x (z diff -2.8) | 0.054 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MFAP3L]] | B | MFAP3L activity raises USP46's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without MFAP3L | 0.054 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[ADCY3]] | B | ADCY3 activity raises USP46's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.22× lower at baseline in the lines without ADCY3 | 0.063 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[MSI1]] | B | MSI1 activity raises USP46's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.43× lower at baseline in the lines without MSI1 | 0.065 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[SOBP]] | B | SOBP activity raises USP46's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.49× lower at baseline in the lines without SOBP | 0.091 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[LRRN2]] | B | LRRN2 activity raises USP46's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.21× lower at baseline in the lines without LRRN2 | 0.092 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[DCAF17]] | C | DCAF17's natural level strengthens USP46's drug response | DCAF17's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.15; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.6, 12.5); signed map (-12.8, -41.1). **Vector** length 90.5, 18.1% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +10.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.4 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +4.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +3.0 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.7 | -15.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -15.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | -8.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -2.6 | -6.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -7.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -3.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 46 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:52,590,960-52,659,301 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12552 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [P62068](https://www.uniprot.org/uniprotkb/P62068) (Ubiquitin carboxyl-terminal hydrolase 46):

> Deubiquitinating enzyme that plays a role in behavior, possibly by regulating GABA action. May act by mediating the deubiquitination of GAD1/GAD67 (By similarity). Has almost no deubiquitinating activity by itself and requires the interaction with WDR48 to have a high activity. Not involved in deubiquitination of monoubiquitinated FANCD2.

**Summary**, from NCBI Gene [64854](https://www.ncbi.nlm.nih.gov/gene/64854):

> Modification of cellular proteins by ubiquitin is an essential regulatory mechanism controlled by the coordinated action of multiple ubiquitin-conjugating and deubiquitinating enzymes. USP46 belongs to a large family of cysteine proteases that function as deubiquitinating enzymes (Quesada et al., 2004 [PubMed 14715245]).[supplied by OMIM, Jun 2009]

**Accessions** — [HGNC:20075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20075) · Entrez [64854](https://www.ncbi.nlm.nih.gov/gene/64854) · UniProt [P62068](https://www.uniprot.org/uniprotkb/P62068) · Ensembl [ENSG00000109189](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109189)

## Data

Gene col 3037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3037); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3037]; `tensor/DDL_lfc|DDL_z.npy` [3037]; `embed/gene_vectors.npy` [3037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3037 or target_col == 3037). Every well: [[USP46 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP46.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

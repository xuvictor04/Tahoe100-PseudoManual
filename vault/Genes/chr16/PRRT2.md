---
symbol: "PRRT2"
type: "gene"
col: 9457
ensembl_id: "ENSG00000167371"
name: "proline rich transmembrane protein 2"
location: "16p11.2"
module: 35
arm: "+"
pooled_cpm: 2.64
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PRRT2

*proline rich transmembrane protein 2* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.14× (z +10.4, q 2e-22, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +6.9, q 7e-10, up in 13 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.600× (z -4.8, q 5e-04, down in 15 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CA11]] (+0.63, fdr 1e-05), [[SAMD11]] (+0.62, fdr 7e-06), [[UPK2]] (+0.62, fdr 1e-05); moves opposite to [[PKP2]] (-0.51, fdr 4e-05), [[BMP6]] (-0.50, fdr 4e-05), [[FAM110C]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[COL3A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +10.4 | 2e-22 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +7.0 | 6e-10 | 2/4 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +7.0 | 6e-10 | 3/11 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +6.9 | 7e-10 | 13/26 (A498, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +5.9 | 5e-07 | 8/33 (SHP-77, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.79×** | +5.3 | 1e-05 | 8/24 (HS-578T, CFPAC-1, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.50×** | +4.6 | 4e-04 | 6/39 (C-33 A, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.002 | 2/22 (A-172, A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.008 | 8/36 (C-33 A, A-427, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.008 | 6/43 (PANC-1, C-33 A, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.011 | 3/36 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.50×** | +3.6 | 0.015 | 2/36 (PANC-1, HOP62) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.37×** | +3.4 | 0.031 | 5/44 (C-33 A, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.044 | 5/44 (PANC-1, SK-MEL-2, …) | all doses, flat |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.62×** | +3.2 | 0.044 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.082 | 1/39 (NCI-H1573) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.099 | 5/44 (A-427, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.099 | 4/44 (A-427, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9457.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.600×** | -4.8 | 5e-04 | 15/44 (C-33 A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.600×** | -4.8 | 5e-04 | 11/44 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.611×** | -4.6 | 7e-04 | 11/43 (RPMI-7951, PANC-1, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.616×** | -4.4 | 0.002 | 4/43 (H4, hTERT-HPNE, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.653×** | -4.0 | 0.007 | 13/41 (C32, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.660×** | -3.9 | 0.007 | 14/39 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.05 µM |  | **0.639×** | -3.9 | 0.007 | 7/27 (HEC-1-A, CHP-212, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.645×** | -3.9 | 0.007 | 12/32 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.655×** | -3.8 | 0.009 | 8/37 (SNU-423, AN3 CA, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.669×** | -3.8 | 0.009 | 12/42 (LOX-IMVI, J82, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.671×** | -3.7 | 0.009 | 11/37 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.712×** | -3.2 | 0.066 | 9/35 (SW1417, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.717×** | -3.1 | 0.080 | 10/44 (A549, hTERT-HPNE, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 2.86 | 0 | 1 | — | [[Aspirin (drug)]] 0.5 µM 0.0492× (z -8.9) |
| [[A-172 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.683 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.940 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.952 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.867 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.671 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.979 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.840 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.753 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.746 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.739 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.713 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CA11]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SAMD11]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[UPK2]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[TGFB3]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[GNAS]] | +0.58 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[HOXC6]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SOCS5]] | +0.58 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[CHASERR]] | +0.57 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[DLL1]] | +0.57 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[THBS2-AS1]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[CCDC3]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CERCAM]] | +0.56 | +0.40 / +0.56 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKP2]] | -0.51 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[BMP6]] | -0.50 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[FAM110C]] | -0.49 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[EIPR1]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[CAP1]] | -0.48 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[RRP1B]] | -0.48 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[BCL2L1]] | -0.47 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[POLR3B]] | -0.47 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[DFFA]] | -0.47 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[APPL2]] | -0.47 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[NEIL2]] | -0.47 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[PTPN3]] | -0.47 | -0.45 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL3A1]] | B | COL3A1 activity raises PRRT2's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 2.32× lower at baseline in the lines without COL3A1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[SSC5D]] | B | SSC5D activity raises PRRT2's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.80× lower at baseline in the lines without SSC5D | 0.017 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[ELFN1]] | B | ELFN1 activity raises PRRT2's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without ELFN1 | 0.019 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[LINC02384]] | B | LINC02384 activity raises PRRT2's level | lines that do not express LINC02384 (26) vs lines expressing it (24) | 1.89× lower at baseline in the lines without LINC02384 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, ENSG00000277693, FAM230C; maybe low, not absent |
| [[ID2-AS1]] | B | ID2-AS1 activity raises PRRT2's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 1.86× lower at baseline in the lines without ID2-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[CDK15]] | B | CDK15 activity raises PRRT2's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 1.40× lower at baseline in the lines without CDK15 | 0.034 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers PRRT2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[ADAMTS10]] | B | ADAMTS10 activity raises PRRT2's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 1.86× lower at baseline in the lines without ADAMTS10 | 0.057 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.468). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (6.2, 26.0); signed map (37.1, -3.0). **Vector** length 40.6, 4.39% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +7.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +3.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.2 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.2 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.3 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | proline rich transmembrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,811,382-29,815,892 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25513, DKFZp547J199, IFITMD1, FICCA, DSPB3, PKC, EKD1; previously ICCA, DYT10 |
| Gene groups (HGNC) | Dispanins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6L0](https://www.uniprot.org/uniprotkb/Q7Z6L0) (Proline-rich transmembrane protein 2):

> As a component of the outer core of AMPAR complex, may be involved in synaptic transmission in the central nervous system. In hippocampal neurons, in presynaptic terminals, plays an important role in the final steps of neurotransmitter release, possibly by regulating Ca(2+)-sensing. In the cerebellum, may inhibit SNARE complex formation and down-regulate short-term facilitation.

**Summary**, from NCBI Gene [112476](https://www.ncbi.nlm.nih.gov/gene/112476):

> This gene encodes a transmembrane protein containing a proline-rich domain in its N-terminal half. Studies in mice suggest that it is predominantly expressed in brain and spinal cord in embryonic and postnatal stages. Mutations in this gene are associated with episodic kinesigenic dyskinesia-1. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:30500](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30500) · Entrez [112476](https://www.ncbi.nlm.nih.gov/gene/112476) · UniProt [Q7Z6L0](https://www.uniprot.org/uniprotkb/Q7Z6L0) · Ensembl [ENSG00000167371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167371)

## Data

Gene col 9457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9457); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9457]; `tensor/DDL_lfc|DDL_z.npy` [9457]; `embed/gene_vectors.npy` [9457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9457 or target_col == 9457). Every well: [[PRRT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRRT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

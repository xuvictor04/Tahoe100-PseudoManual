---
symbol: "MVP-DT"
type: "gene"
col: 14164
ensembl_id: "ENSG00000238045"
name: "MVP divergent transcript"
location: "16p11.2"
module: 70
arm: "+"
pooled_cpm: 13.24
n_lines_expressing: 50
n_dd_up: 46
n_dd_down: 10
n_dd_up_clean: 36
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 23
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# MVP-DT

*MVP divergent transcript* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.12× (z +11.4, q 4e-27, up in 27 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.524× (z -6.9, q 2e-09, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-F]] (+0.75, fdr 7e-06), [[CFB]] (+0.71, fdr 7e-06), [[ELF3-AS1]] (+0.69, fdr 7e-06); moves opposite to [[SMYD2]] (-0.56, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[TRIM31]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14164.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +11.4 | 4e-27 | 27/43 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +8.8 | 6e-16 | 25/43 (LOX-IMVI, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **2.16×** | +7.9 | 5e-13 | 34/44 (AsPC-1, CFPAC-1, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.80×** | +7.6 | 5e-12 | 30/46 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +6.7 | 2e-09 | 12/23 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.90×** | +6.6 | 3e-09 | 31/45 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.4 | 1e-08 | 20/39 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.77×** | +6.3 | 2e-08 | 30/48 (AsPC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.2 | 3e-08 | 24/47 (A498, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.50×** | +6.0 | 1e-07 | 25/46 (AsPC-1, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.60×** | +5.3 | 7e-06 | 25/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.64×** | +5.3 | 7e-06 | 23/46 (MIA PaCa-2, A498, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +4.9 | 4e-05 | 24/47 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.56×** | +4.7 | 8e-05 | 22/47 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.42×** | +4.7 | 9e-05 | 20/46 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +4.7 | 9e-05 | 21/46 (Hs 766T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14164.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.524×** | -6.9 | 2e-09 | 31/47 (A549, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.534×** | -6.8 | 4e-09 | 24/41 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.630×** | -5.0 | 1e-04 | 24/46 (A549, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.672×** | -4.1 | 0.006 | 12/46 (A549, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.695×** | -3.9 | 0.010 | 14/48 (H4, A549, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.699×** | -3.8 | 0.011 | 20/47 (COLO 205, KATO III, …) | all doses, flat | composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.781×** | -3.8 | 0.012 | 22/46 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.691×** | -3.8 | 0.012 | 18/45 (HT-29, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.509×** | -3.7 | 0.015 | 16/41 (COLO 205, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.814×** | -3.1 | 0.097 | 10/46 (CFPAC-1, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.574× | -3.0 | 0.14 | 12/31 (KATO III, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14164. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 96.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0807× (z -21.6) |
| [[A-172 (line)]] | wt | 22.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +20.9) | — |
| [[SNU-423 (line)]] | alt | 21.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +14.3) | [[Digitoxin (drug)]] 0.05 µM 0.0886× (z -13.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.176× (z -9.8) |
| [[Hs 766T (line)]] | wt | 16.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +14.1) | [[Digitoxin (drug)]] 5 µM 0.163× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[hTERT-HPNE (line)]] | wt | 6.51 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +9.7) | [[Dexamethasone (drug)]] 5 µM 0.0637× (z -8.5) |
| [[A498 (line)]] | wt | 16.0 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.83× (z +8.8) | — |
| [[A549 (line)]] | wt | 29.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.140× (z -10.1) |
| [[HS-578T (line)]] | alt | 8.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 34.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.217× (z -9.0) |
| [[J82 (line)]] | alt | 6.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.6× (z +21.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.89× (z +10.6) ⚠ position not correctable | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0410× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +14.8) | — |
| [[NCI-H460 (line)]] | wt | 4.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 7.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +13.7) | — |
| [[SK-MEL-2 (line)]] | alt | 8.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +8.8) | — |
| [[A-427 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14164), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-F]] | +0.75 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[CFB]] | +0.71 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[ELF3-AS1]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[B2M]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[GBP2]] | +0.68 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[CEACAM16-AS1]] | +0.67 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[CASP10]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CTSS]] | +0.66 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[KMO]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TMEM140]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[APOL1]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMYD2]] | -0.56 | -0.60 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 22, C 1. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM31]] | B | TRIM31 activity raises MVP-DT's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 2.53× lower at baseline in the lines without TRIM31 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises MVP-DT's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 2.09× lower at baseline in the lines without PDZK1IP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[CFB]] | B | CFB activity raises MVP-DT's level | lines that do not express CFB (20) vs lines expressing it (30) | 1.99× lower at baseline in the lines without CFB | 0.012 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[GBP1]] | B | GBP1 activity raises MVP-DT's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without GBP1 | 0.014 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[GBP2]] | B | GBP2 activity raises MVP-DT's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without GBP2 | 0.017 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[PLAAT4]] | B | PLAAT4 activity raises MVP-DT's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.82× lower at baseline in the lines without PLAAT4 | 0.020 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[RSAD2]] | B | RSAD2 activity raises MVP-DT's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.04× lower at baseline in the lines without RSAD2 | 0.032 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[SPINK1]] | B | SPINK1 activity raises MVP-DT's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 2.02× lower at baseline in the lines without SPINK1 | 0.034 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |
| [[APOL1]] | B | APOL1 activity raises MVP-DT's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 1.85× lower at baseline in the lines without APOL1 | 0.040 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[RHOV]] | B | RHOV activity raises MVP-DT's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without RHOV | 0.043 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[IFIT2]] | B | IFIT2 activity raises MVP-DT's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without IFIT2 | 0.043 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[VNN1]] | B | VNN1 activity raises MVP-DT's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without VNN1 | 0.046 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.1, 49.8); signed map (48.6, 7.7). **Vector** length 102, 25.2% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.51 to 25); *Antigen processing-Cross presentation* (reactome, mean cos +0.58 to 14); *Interferon gamma signaling* (reactome, mean cos +0.57 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +11.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.2 | +7.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.0 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +4.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.7 | +5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.4 | +6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.9 | +4.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -3.4 | -3.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.2 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | +3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -1.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.5 | +4.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | MVP divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p11.2 — chr16:29,808,636-29,821,252 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AC009133.12 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56029](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56029) · Entrez [112268170](https://www.ncbi.nlm.nih.gov/gene/112268170) · Ensembl [ENSG00000238045](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000238045)

## Data

Gene col 14164: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14164); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14164, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14164]; `tensor/DDL_lfc|DDL_z.npy` [14164]; `embed/gene_vectors.npy` [14164]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14164 or target_col == 14164). Every well: [[MVP-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MVP-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "CSPG4"
type: "gene"
col: 10402
ensembl_id: "ENSG00000173546"
name: "chondroitin sulfate proteoglycan 4"
location: "15q24.2"
module: 13
arm: "+"
pooled_cpm: 8.82
n_lines_expressing: 19
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 35
direction_downstream: 43
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CSPG4

*chondroitin sulfate proteoglycan 4* — 15q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.92× (z +11.8, q 2e-29, up in 3 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.66× (z +4.4, q 0.002, up in 11 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.507× (z -6.1, q 6e-07, down in 13 of 15 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.534× (z -5.6, q 5e-06, down in 12 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL6A3]] (+0.71, fdr 7e-06), [[APCDD1L]] (+0.69, fdr 7e-06), [[NAV1]] (+0.68, fdr 7e-06); moves opposite to [[PATJ]] (-0.45, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 35 arrows point to it, the strongest [[MTSS1]] → it (grade B ⚠); 43 go from it, the strongest it → [[PLXNA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10402.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.92×** | +11.8 | 2e-29 | 3/10 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +9.3 | 4e-18 | 5/12 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +5.2 | 4e-05 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.66×** | +4.4 | 0.002 | 11/14 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.022 | 9/15 (RPMI-7951, SHP-77, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10402.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.507×** | -6.1 | 6e-07 | 13/15 (A-172, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.534×** | -5.6 | 5e-06 | 12/15 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.537×** | -5.6 | 5e-06 | 12/14 (A-172, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.575×** | -4.8 | 3e-04 | 7/14 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.600×** | -4.6 | 5e-04 | 12/15 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.615×** | -4.3 | 0.001 | 12/15 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.631×** | -4.0 | 0.006 | 11/14 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.670×** | -3.6 | 0.024 | 7/15 (HOP62, Hs 766T, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.899× | -3.4 | 0.037 | 3/17 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.684×** | -3.4 | 0.037 | 6/15 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.670×** | -3.4 | 0.037 | 0/16 | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.689×** | -3.3 | 0.042 | 9/15 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.702×** | -3.2 | 0.067 | 1/17 (PANC-1) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.780×** | -3.1 | 0.071 | 13/15 (HOP62, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.711×** | -3.1 | 0.086 | 5/14 (A-172, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10402. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 23.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0848× (z -18.3) |
| [[A-172 (line)]] | wt | 103 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -14.3) |
| [[Hs 766T (line)]] | wt | 17.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0676× (z -16.4) |
| [[C32 (line)]] | wt | 58.1 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -8.8) ⚠ cell-cycle shift, explains ~51% of this change |
| [[PANC-1 (line)]] | alt | 6.21 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 0 | 2 | — | [[Binimetinib (drug)]] 5 µM 0.136× (z -9.5) |
| [[HS-578T (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 82.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 29.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -9.6) |
| [[A-427 (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.881 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.701 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.637 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.787 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.899 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10402), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL6A3]] | +0.71 | +0.69 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.69 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[NAV1]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[AEBP1]] | +0.66 | +0.68 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[THBS2]] | +0.66 | +0.69 / +0.57 | both halves | 1e-05 | pathway: Diseases of glycosylation |
| [[LINC01615]] | +0.65 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[COL5A1]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[COL6A2]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 | STRING 409 |
| [[DENND2A]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[COL6A1]] | +0.63 | +0.64 / +0.58 | both halves | 7e-06 | STRING 435 |
| [[SARDH]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SCUBE3]] | +0.59 | +0.63 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATJ]] | -0.45 | -0.49 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 3, C 32. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTSS1]] | B | MTSS1 activity raises CSPG4's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.20× lower at baseline in the lines without MTSS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[PATJ]] | B | PATJ activity lowers CSPG4's level | lines that do not express PATJ (9) vs lines expressing it (41) | 6.23× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[TMEM255B]] | B | TMEM255B activity raises CSPG4's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 2.78× lower at baseline in the lines without TMEM255B | 0.086 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[TIMP3]] | C | TIMP3 activity raises CSPG4's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 6.58× lower at baseline in the lines without TIMP3 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises CSPG4's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 10.66× lower at baseline in the lines without FCRLA | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises CSPG4's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 3.72× lower at baseline in the lines without PDGFRB | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises CSPG4's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.29× lower at baseline in the lines without COL5A1 | 0.008 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises CSPG4's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 6.94× lower at baseline in the lines without AEBP1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises CSPG4's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 3.42× lower at baseline in the lines without ITGA11 | 0.010 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[LAMA4]] | C | LAMA4 activity raises CSPG4's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 3.12× lower at baseline in the lines without LAMA4 | 0.013 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[PTPRN]] | C | PTPRN activity raises CSPG4's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 3.55× lower at baseline in the lines without PTPRN | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises CSPG4's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 4.49× lower at baseline in the lines without APCDD1L | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 9, C 34. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNA2]] | B | CSPG4 activity weakens PLXNA2's drug response | lines that do not express CSPG4 (20) vs lines expressing it (13) | the lines without CSPG4 respond 0.97× as strongly (z diff +0.16); strongest at Tucidinostat 5 µM: 1.47x vs 1.02x (z diff -2.6) | 0.012 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; target measured in part of the lines; both ways; artifact flags |
| [[MTSS1]] | B | CSPG4 activity raises MTSS1's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.86× lower at baseline in the lines without CSPG4 | 0.018 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1 |
| [[PGF]] | B | CSPG4 activity raises PGF's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without CSPG4 | 0.025 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1 |
| [[PLXNA2]] | B | CSPG4 activity raises PLXNA2's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 1.91× lower at baseline in the lines without CSPG4 | 0.034 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1 |
| [[ARL10]] | B | CSPG4 activity raises ARL10's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.52× lower at baseline in the lines without CSPG4 | 0.042 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1 |
| [[PATJ]] | B | CSPG4 activity lowers PATJ's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.75× higher at baseline in the lines without CSPG4 | 0.051 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1 |
| [[PHLDB1]] | B | CSPG4 activity raises PHLDB1's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.22× lower at baseline in the lines without CSPG4 | 0.054 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1 |
| [[PHLDB1]] | B | CSPG4 activity strengthens PHLDB1's drug response | lines that do not express CSPG4 (27) vs lines expressing it (17) | the lines without CSPG4 respond 0.76× as strongly (z diff +1.05); strongest at Idarubicin (hydrochloride) 5 µM: 0.83x vs 0.53x (z diff +3.7) | 0.091 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; target measured in part of the lines; artifact flags |
| [[FAM167A]] | B | CSPG4 activity raises FAM167A's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.35× lower at baseline in the lines without CSPG4 | 0.092 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1 |
| [[DENND2A]] | C | CSPG4 activity raises DENND2A's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 3.14× lower at baseline in the lines without CSPG4 | 0.002 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |
| [[LAMA4]] | C | CSPG4 activity raises LAMA4's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 4.61× lower at baseline in the lines without CSPG4 | 0.003 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |
| [[GPR173]] | C | CSPG4 activity raises GPR173's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 4.95× lower at baseline in the lines without CSPG4 | 0.005 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.6, 17.8); signed map (24.7, 46.0). **Vector** length 59.4, 20.4% of its response variance represented; |z| ≥ 3 in 495 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen formation* (reactome, mean cos +0.50 to 12); *Assembly of collagen fibrils and other multimeric structures* (reactome, mean cos +0.52 to 10); *Collagen biosynthesis and modifying enzymes* (reactome, mean cos +0.53 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -5.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.3 | -3.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -3.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | chondroitin sulfate proteoglycan 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:75,674,322-75,712,848 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCSPG, MEL-CSPG, MSK16, NG2, MCSP, HMW-MAA, CSPG4A |
| Gene groups (HGNC) | Proteoglycans |
| Reactome | 16 pathways, smallest: Defective CHST14 causes EDS, musculocontractural type; Defective CHST3 causes SEDCJD; Defective CHSY1 causes TPBS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UVK1](https://www.uniprot.org/uniprotkb/Q6UVK1) (Chondroitin sulfate proteoglycan 4):

> Proteoglycan playing a role in cell proliferation and migration which stimulates endothelial cells motility during microvascular morphogenesis. May also inhibit neurite outgrowth and growth cone collapse during axon regeneration. Cell surface receptor for collagen alpha 2(VI) which may confer cells ability to migrate on that substrate. Binds through its extracellular N-terminus growth factors, extracellular matrix proteases modulating their activity. May regulate MPP16-dependent degradation and …

**Summary**, from NCBI Gene [1464](https://www.ncbi.nlm.nih.gov/gene/1464):

> A human melanoma-associated chondroitin sulfate proteoglycan plays a role in stabilizing cell-substratum interactions during early events of melanoma cell spreading on endothelial basement membranes. CSPG4 represents an integral membrane chondroitin sulfate proteoglycan expressed by human malignant melanoma cells. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2466) · Entrez [1464](https://www.ncbi.nlm.nih.gov/gene/1464) · UniProt [Q6UVK1](https://www.uniprot.org/uniprotkb/Q6UVK1) · Ensembl [ENSG00000173546](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173546)

## Data

Gene col 10402: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10402); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10402, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10402]; `tensor/DDL_lfc|DDL_z.npy` [10402]; `embed/gene_vectors.npy` [10402]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10402 or target_col == 10402). Every well: [[CSPG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSPG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

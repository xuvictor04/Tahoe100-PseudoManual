---
symbol: "ITGA4"
type: "gene"
col: 3637
ensembl_id: "ENSG00000115232"
name: "integrin subunit alpha 4"
location: "2q31.3"
module: 66
arm: "+"
pooled_cpm: 9.64
n_lines_expressing: 17
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 31
direction_downstream: 42
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# ITGA4

*integrin subunit alpha 4* — 2q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.73× (z +15.9, q 0e+00, up in 11 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +10.1, q 1e-21, up in 1 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.652× (z -4.5, q 0.003, down in 8 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (HOP62 0.0788×, LOX-IMVI 0.173×, RPMI-7951 0.221×, CHP-212 0.163×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.210×); [[Digitoxin (drug)]] 5 µM in 1 line (A498 0.350×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DKK3]] (+0.63, fdr 7e-06), [[COL3A1]] (+0.63, fdr 1e-05), [[COL4A1]] (+0.62, fdr 1e-05); moves opposite to [[STARD10]] (-0.45, fdr 5e-05), [[LIME1]] (-0.42, fdr 2e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[MMP2]] → it (grade C ⚠); 42 go from it, the strongest it → [[HEG1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.73×** | +15.9 | 0e+00 | 11/12 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.83×** | +14.3 | 8e-44 | 14/14 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.26×** | +11.6 | 7e-29 | 12/13 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +10.1 | 1e-21 | 1/15 (RPMI-7951) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +6.4 | 2e-08 | 9/15 (C32, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.8 | 2e-04 | 2/15 (RPMI-7951, SNU-423) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.7 | 2e-04 | 7/15 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.82×** | +4.5 | 4e-04 | 1/13 (CHP-212) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.4 | 6e-04 | 3/13 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.5 | 0.024 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.045 | 1/14 (SNU-423) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.36×** | +3.3 | 0.045 | 0/14 | inconsistent across doses | low cells (technical?) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.060 | 1/13 (LOX-IMVI) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.2 | 0.065 | 1/11 (HS-578T) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3637.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (HOP62 0.0788×, LOX-IMVI 0.173×, RPMI-7951 0.221×, CHP-212 0.163×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.210×); [[Digitoxin (drug)]] 5 µM in 1 line (A498 0.350×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -4.5 | 0.003 | 8/15 (A498, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.700× | -3.5 | 0.12 | 0/14 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.726× | -3.4 | 0.12 | 8/14 (A498, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.730× | -3.3 | 0.12 | 1/14 (C32) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | 0.727× | -3.3 | 0.12 | 9/15 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.735× | -3.1 | 0.18 | 0/15 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -3.0 | 0.20 | 1/15 (HOP62) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 73.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +14.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 45.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 58.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -10.7) |
| [[C32 (line)]] | wt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.48× (z +9.4) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 90.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0788× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 69.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 8.29 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.888 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.748 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.635 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.636 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.747 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.822 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.798 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.841 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.638 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DKK3]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[COL3A1]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[COL4A1]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 | pathway: Extracellular matrix organization; STRING 750 |
| [[PDGFRB]] | +0.62 | +0.64 / +0.48 | both halves | 2e-05 | same gene group |
| [[SPARC]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[COL4A2]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 | pathway: Extracellular matrix organization; STRING 744 |
| [[TGFBI]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[COL1A2]] | +0.58 | +0.58 / +0.46 | both halves | 3e-05 | pathway: Cell surface interactions at the vascular wall; STRING 730 |
| [[SUSD5]] | +0.57 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[FBN1]] | +0.57 | +0.60 / +0.47 | both halves | 2e-05 | pathway: Extracellular matrix organization |
| [[ITGA8]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 | same gene group; pathway: Extracellular matrix organization; STRING 778 |
| [[ARHGEF6]] | +0.56 | +0.66 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD10]] | -0.45 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[LIME1]] | -0.42 | -0.36 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 0, C 31. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP2]] | C | MMP2 activity raises ITGA4's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 10.22× lower at baseline in the lines without MMP2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises ITGA4's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 8.15× lower at baseline in the lines without APCDD1L | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises ITGA4's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 4.73× lower at baseline in the lines without COL5A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[HTR1F]] | C | HTR1F activity raises ITGA4's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 5.42× lower at baseline in the lines without HTR1F | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises ITGA4's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 4.33× lower at baseline in the lines without COL1A1 | 0.009 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises ITGA4's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 3.62× lower at baseline in the lines without FBN1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[POSTN]] | C | POSTN activity raises ITGA4's level | lines that do not express POSTN (38) vs lines expressing it (12) | 6.92× lower at baseline in the lines without POSTN | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[SRPX]] | C | SRPX activity raises ITGA4's level | lines that do not express SRPX (22) vs lines expressing it (28) | 5.01× lower at baseline in the lines without SRPX | 0.015 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises ITGA4's level | lines that do not express SPARC (34) vs lines expressing it (16) | 9.98× lower at baseline in the lines without SPARC | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises ITGA4's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 4.46× lower at baseline in the lines without DKK3 | 0.016 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[LAYN]] | C | LAYN activity raises ITGA4's level | lines that do not express LAYN (31) vs lines expressing it (19) | 3.85× lower at baseline in the lines without LAYN | 0.019 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[NID2]] | C | NID2 activity raises ITGA4's level | lines that do not express NID2 (32) vs lines expressing it (18) | 4.14× lower at baseline in the lines without NID2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 5, C 37. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEG1]] | B | ITGA4 activity raises HEG1's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.96× lower at baseline in the lines without ITGA4 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411 |
| [[SYTL3]] | B | ITGA4 activity raises SYTL3's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.60× lower at baseline in the lines without ITGA4 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411 |
| [[LOXL1]] | B | ITGA4 activity raises LOXL1's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without ITGA4 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411 |
| [[FKBP7]] | B | ITGA4 activity raises FKBP7's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.05× lower at baseline in the lines without ITGA4 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411 |
| [[DZIP1L]] | B | ITGA4 activity raises DZIP1L's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 2.27× lower at baseline in the lines without ITGA4 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411 |
| [[SPARC]] | C | ITGA4 activity raises SPARC's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 22.21× lower at baseline in the lines without ITGA4 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[MMP2]] | C | ITGA4 activity raises MMP2's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 13.19× lower at baseline in the lines without ITGA4 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[PDGFRB]] | C | ITGA4 activity raises PDGFRB's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 7.39× lower at baseline in the lines without ITGA4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[ARHGEF6]] | C | ITGA4 activity raises ARHGEF6's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 4.48× lower at baseline in the lines without ITGA4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[FBN1]] | C | ITGA4 activity raises FBN1's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 6.91× lower at baseline in the lines without ITGA4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[AK5]] | C | ITGA4 activity raises AK5's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 3.81× lower at baseline in the lines without ITGA4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[ZNF883]] | C | ITGA4 activity raises ZNF883's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 3.13× lower at baseline in the lines without ITGA4 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.530). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (55.4, 22.1); signed map (25.3, 42.3). **Vector** length 52.7, 17.4% of its response variance represented; |z| ≥ 3 in 370 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Assembly of collagen fibrils and other multimeric structures* (reactome, mean cos +0.53 to 8); *Fibronectin matrix formation* (reactome, mean cos +0.57 to 6); *Collagen chain trimerization* (reactome, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +15.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +10.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +3.0 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -0.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.6 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.3 — chr2:181,457,202-181,538,940 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD49d; previously CD49D |
| Gene groups (HGNC) | CD molecules; Integrin alpha subunits |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING |
| Reactome | 13 pathways, smallest: RUNX3 Regulates Immune Response and Cell Migration; Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Integrin cell surface interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P13612](https://www.uniprot.org/uniprotkb/P13612) (Integrin alpha-4):

> Integrins alpha-4/beta-1 (VLA-4) and alpha-4/beta-7 are receptors for fibronectin. They recognize one or more domains within the alternatively spliced CS-1 and CS-5 regions of fibronectin. They are also receptors for VCAM1. Integrin alpha-4/beta-1 recognizes the sequence Q-I-D-S in VCAM1. Integrin alpha-4/beta-7 is also a receptor for MADCAM1. It recognizes the sequence L-D-T in MADCAM1. On activated endothelial cells integrin VLA-4 triggers homotypic aggregation for most VLA-4-positive …

**Summary**, from NCBI Gene [3676](https://www.ncbi.nlm.nih.gov/gene/3676):

> The gene encodes a member of the integrin alpha chain family of proteins. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha 4 subunit. This subunit associates with a beta 1 or beta 7 subunit to form an integrin that may play a role in cell motility and migration. This integrin is a …

**Accessions** — [HGNC:6140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6140) · Entrez [3676](https://www.ncbi.nlm.nih.gov/gene/3676) · UniProt [P13612](https://www.uniprot.org/uniprotkb/P13612) · Ensembl [ENSG00000115232](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115232)

## Data

Gene col 3637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3637); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3637]; `tensor/DDL_lfc|DDL_z.npy` [3637]; `embed/gene_vectors.npy` [3637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3637 or target_col == 3637). Every well: [[ITGA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

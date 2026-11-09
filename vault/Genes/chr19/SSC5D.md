---
symbol: "SSC5D"
type: "gene"
col: 11070
ensembl_id: "ENSG00000179954"
name: "scavenger receptor cysteine rich family member with 5 domains"
location: "19q13.42"
module: 53
arm: "+"
pooled_cpm: 5.26
n_lines_expressing: 39
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 13
direction_downstream: 20
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# SSC5D

*scavenger receptor cysteine rich family member with 5 domains* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.58× (z +9.7, q 1e-19, up in 4 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +8.2, q 5e-14, up in 14 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.556× (z -6.5, q 5e-08, down in 17 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASGR1]] (+0.62, fdr 1e-05), [[SCUBE3]] (+0.61, fdr 1e-05), [[DLG4]] (+0.59, fdr 1e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[DENND2A]] → it (grade B ⚠); 20 go from it, the strongest it → [[LINC03048]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +9.7 | 1e-19 | 4/8 (RPMI-7951, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +9.6 | 1e-19 | 4/9 (A498, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +8.2 | 5e-14 | 14/30 (A549, NCI-H23, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.71×** | +5.9 | 5e-07 | 15/37 (RPMI-7951, LoVo, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +5.2 | 2e-05 | 4/13 (SNU-423, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.034 | 4/36 (HEC-1-A, SW 900, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.35× | +3.1 | 0.16 | 1/19 (NCI-H23) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.69× | +3.0 | 0.16 | 1/7 (A-172) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11070.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.556×** | -6.5 | 5e-08 | 17/34 (RPMI-7951, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.563×** | -6.4 | 6e-08 | 16/34 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.568×** | -6.2 | 8e-08 | 16/32 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.573×** | -6.1 | 1e-07 | 19/37 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.581×** | -6.0 | 2e-07 | 18/34 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -4.7 | 3e-04 | 14/36 (H4, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.660×** | -4.6 | 4e-04 | 14/29 (PANC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -4.4 | 6e-04 | 16/25 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -3.4 | 0.036 | 11/33 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.720×** | -3.3 | 0.046 | 7/32 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.732×** | -3.3 | 0.056 | 10/32 (SK-MEL-2, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **0.812×** | -3.2 | 0.056 | 10/36 (PANC-1, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.063 | 10/34 (PANC-1, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.753×** | -3.1 | 0.070 | 7/37 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.756×** | -3.1 | 0.073 | 12/37 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.739×** | -3.1 | 0.073 | 10/35 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -12.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 1.95 | 0 | 2 | — | [[Simotinib (drug)]] 0.5 µM 0.0642× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 5.80 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.136× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 2.16 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 35.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.191× (z -9.9) |
| [[SHP-77 (line)]] | alt | 4.75 | 0 | 1 | — | [[Triclosan (drug)]] 0.5 µM 0.0790× (z -8.6) |
| [[A-172 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.802 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASGR1]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SCUBE3]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[DLG4]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[AZU1]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[LAG3]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[MEI1]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[MRC2]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[SAMD14]] | +0.56 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[HPX]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 | pathway: Binding and Uptake of Ligands by Scavenger Receptors |
| [[LINC01119]] | +0.53 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[XG]] | +0.53 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[MIR9-1HG]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DENND2A]] | B | DENND2A activity raises SSC5D's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 2.41× lower at baseline in the lines without DENND2A | 0.002 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[MIR493HG]] | B | MIR493HG activity raises SSC5D's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 1.76× lower at baseline in the lines without MIR493HG | 0.011 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| [[ADAMTS10]] | B | ADAMTS10 activity raises SSC5D's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 2.30× lower at baseline in the lines without ADAMTS10 | 0.012 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| [[ELFN1]] | B | ELFN1 activity raises SSC5D's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.27× lower at baseline in the lines without ELFN1 | 0.026 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[PDGFRB]] | B | PDGFRB activity raises SSC5D's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.06× lower at baseline in the lines without PDGFRB | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[LAG3]] | B | LAG3 activity raises SSC5D's level | lines that do not express LAG3 (8) vs lines expressing it (42) | 2.42× lower at baseline in the lines without LAG3 | 0.042 | ⚠ within organs, on part of the lines; also absent: SCML2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[ASGR1]] | B | ASGR1 activity raises SSC5D's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 2.07× lower at baseline in the lines without ASGR1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[SARDH]] | B | SARDH activity raises SSC5D's level | lines that do not express SARDH (21) vs lines expressing it (29) | 1.66× lower at baseline in the lines without SARDH | 0.059 | ⚠ within organs, on part of the lines; also absent: PKD1L1-AS1, ZNF90, ENSG00000222032; maybe low, not absent |
| [[PLEKHG4B]] | B | PLEKHG4B activity raises SSC5D's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 1.67× lower at baseline in the lines without PLEKHG4B | 0.064 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1 |
| [[NTM]] | B | NTM activity raises SSC5D's level | lines that do not express NTM (33) vs lines expressing it (17) | 2.28× lower at baseline in the lines without NTM | 0.076 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1 |
| [[HHIPL2]] | B | HHIPL2 activity raises SSC5D's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without HHIPL2 | 0.083 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent |
| [[LOXL1]] | B | LOXL1 activity raises SSC5D's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.32× lower at baseline in the lines without LOXL1 | 0.096 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03048]] | B | SSC5D activity raises LINC03048's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without SSC5D | 0.003 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[PLCD4]] | B | SSC5D activity raises PLCD4's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without SSC5D | 0.015 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[ADAMTS10]] | B | SSC5D activity raises ADAMTS10's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 2.13× lower at baseline in the lines without SSC5D | 0.017 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[PRRT2]] | B | SSC5D activity raises PRRT2's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.80× lower at baseline in the lines without SSC5D | 0.017 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[AZU1]] | B | SSC5D activity raises AZU1's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without SSC5D | 0.026 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[NTRK1]] | B | SSC5D activity raises NTRK1's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without SSC5D | 0.026 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[ELFN1]] | B | SSC5D activity raises ELFN1's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 3.12× lower at baseline in the lines without SSC5D | 0.030 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[LAG3]] | B | SSC5D activity raises LAG3's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.93× lower at baseline in the lines without SSC5D | 0.032 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[SAMD14]] | B | SSC5D activity raises SAMD14's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.65× lower at baseline in the lines without SSC5D | 0.046 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[KIAA1614]] | B | SSC5D activity raises KIAA1614's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.55× lower at baseline in the lines without SSC5D | 0.053 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[APC2]] | B | SSC5D activity raises APC2's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.56× lower at baseline in the lines without SSC5D | 0.057 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[PTCH2]] | B | SSC5D activity raises PTCH2's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.43× lower at baseline in the lines without SSC5D | 0.061 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.3, -17.0); signed map (17.8, 17.6). **Vector** length 51.7, 7.70% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +5.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.3 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -6.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.1 | -3.3 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | scavenger receptor cysteine rich family member with 5 domains |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,488,404-55,519,099 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35258, S5D-SRCRB |
| Gene groups (HGNC) | Scavenger receptors; Scavenger receptor cysteine rich domain containing |
| Reactome | 3 pathways, smallest: Scavenging by Class B Receptors; Binding and Uptake of Ligands by Scavenger Receptors; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [A1L4H1](https://www.uniprot.org/uniprotkb/A1L4H1) (Soluble scavenger receptor cysteine-rich domain-containing protein SSC5D):

> Binds to extracellular matrix proteins. Binds to pathogen-associated molecular patterns (PAMPs) present on the cell walls of Gram-positive and Gram-negative bacteria and fungi, behaving as a pattern recognition receptor (PRR). Induces bacterial and fungal aggregation and subsequent inhibition of PAMP-induced cytokine release. Does not possess intrinsic bactericidal activity. May play a role in the innate defense and homeostasis of certain epithelial surfaces (By similarity).

**Summary**, from NCBI Gene [284297](https://www.ncbi.nlm.nih.gov/gene/284297):

> Predicted to enable fibronectin binding activity; laminin binding activity; and scavenger receptor activity. Predicted to be involved in defense response; detection of bacterial lipoprotein; and negative regulation of interleukin-8 production. Predicted to act upstream of or within regulation of interleukin-8 production. Predicted to be located in cytoplasm; extracellular region; and membrane. Predicted to be active in extracellular matrix and obsolete extracellular space. [provided by Alliance …

**Accessions** — [HGNC:26641](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26641) · Entrez [284297](https://www.ncbi.nlm.nih.gov/gene/284297) · UniProt [A1L4H1](https://www.uniprot.org/uniprotkb/A1L4H1) · Ensembl [ENSG00000179954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179954)

## Data

Gene col 11070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11070); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11070]; `tensor/DDL_lfc|DDL_z.npy` [11070]; `embed/gene_vectors.npy` [11070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11070 or target_col == 11070). Every well: [[SSC5D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSC5D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

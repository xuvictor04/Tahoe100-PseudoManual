---
symbol: "ARHGAP20"
type: "gene"
col: 6057
ensembl_id: "ENSG00000137727"
name: "Rho GTPase activating protein 20"
location: "11q22.3-q23.1"
module: 152
arm: "+"
pooled_cpm: 7.36
n_lines_expressing: 16
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 8
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# ARHGAP20

*Rho GTPase activating protein 20* — 11q22.3-q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.90× (z +12.6, q 9e-34, up in 4 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.0696×, NCI-H2347 0.175×, NCI-H1792 0.323×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.174×); [[Digitoxin (drug)]] 5 µM in 1 line (A498 0.0637×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.123×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMAT4]] (+0.54, fdr 3e-05), [[TDRD9]] (+0.51, fdr 5e-05), [[LRAT]] (+0.51, fdr 5e-04); moves opposite to [[NPHP3-ACAD11]] (-0.46, fdr 2e-04), [[HMGA2-AS1]] (-0.43, fdr 4e-04), [[COPB2-DT]] (-0.41, fdr 4e-04).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NYAP2]] → it (grade B ⚠); 8 go from it, the strongest it → [[ST6GALNAC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6057.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.90×** | +12.6 | 9e-34 | 4/12 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.12×** | +11.9 | 4e-30 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.99×** | +11.2 | 1e-26 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.48×** | +10.5 | 2e-23 | 11/13 (SW 900, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.32×** | +10.0 | 2e-21 | 11/14 (C-33 A, hTERT-HPNE, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.11×** | +9.5 | 1e-19 | 10/13 (SW 900, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.44×** | +9.3 | 9e-19 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.42×** | +7.4 | 9e-12 | 11/13 (SW 900, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.17×** | +6.5 | 5e-09 | 8/12 (C-33 A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.12×** | +6.3 | 2e-08 | 9/13 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +5.1 | 2e-05 | 3/10 (hTERT-HPNE, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +4.6 | 2e-04 | 1/10 (hTERT-HPNE) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.72×** | +4.4 | 5e-04 | 2/9 (hTERT-HPNE, J82) | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.68×** | +4.4 | 5e-04 | 0/11 | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.8 | 0.006 | 0/10 | top dose only | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +3.5 | 0.014 | 1/12 (J82) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +3.5 | 0.018 | 5/11 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.57×** | +3.4 | 0.019 | 0/11 | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.021 | 1/10 (A498) | inconsistent across doses |  |
| [[Resveratrol (drug)]] 0.05 µM |  | **1.44×** | +3.1 | 0.053 | 0/12 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6057.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A498 0.0696×, NCI-H2347 0.175×, NCI-H1792 0.323×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.174×); [[Digitoxin (drug)]] 5 µM in 1 line (A498 0.0637×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.123×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -3.4 | 0.42 | 5/14 (HS-578T, H4, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.665× | -3.1 | 0.42 | 0/13 | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.679× | -3.1 | 0.42 | 1/12 (A498) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 146 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -10.6) |
| [[A498 (line)]] | wt | 3.48 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0696× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 18.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -8.5) |
| [[A-172 (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.707 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.802 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.692 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.795 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.588 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMAT4]] | +0.54 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[TDRD9]] | +0.51 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[LRAT]] | +0.51 | +0.23 / +0.51 | both halves | 5e-04 |  |
| [[A2M]] | +0.49 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[GNAO1]] | +0.47 | +0.35 / +0.41 | both halves | 1e-04 |  |
| [[ST6GALNAC3]] | +0.47 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[CNTNAP3C]] | +0.47 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[TMEM108]] | +0.46 | +0.42 / +0.35 | both halves | 1e-04 |  |
| [[LINGO2]] | +0.45 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[CNTNAP3P2]] | +0.45 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[ENDOD1]] | +0.45 | +0.41 / +0.37 | both halves | 8e-05 |  |
| [[LOXL4]] | +0.44 | +0.52 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP3-ACAD11]] | -0.46 | -0.34 / -0.29 | both halves | 2e-04 |  |
| [[HMGA2-AS1]] | -0.43 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[COPB2-DT]] | -0.41 | -0.26 / -0.34 | both halves | 4e-04 |  |
| [[LRRC39]] | -0.40 | -0.29 / -0.23 | both halves | 5e-04 |  |
| [[SOX2-OT]] | -0.40 | -0.25 / -0.29 | both halves | 4e-04 |  |
| [[SLC35E2B]] | -0.39 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[TBCE-1]] | -0.39 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[FMNL3]] | -0.38 | -0.34 / -0.26 | both halves | 4e-04 | pathway: CDC42 GTPase cycle |
| [[ZCWPW1]] | -0.38 | -0.20 / -0.32 | both halves | 7e-04 |  |
| [[NPHP3]] | -0.38 | -0.34 / -0.26 | both halves | 4e-04 |  |
| [[NQO1-DT]] | -0.38 | -0.25 / -0.30 | both halves | 4e-04 |  |
| [[NEK11]] | -0.38 | -0.24 / -0.29 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NYAP2]] | B | NYAP2 activity raises ARHGAP20's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 2.07× lower at baseline in the lines without NYAP2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[DUOX2]] | C | DUOX2 activity raises ARHGAP20's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 1.91× lower at baseline in the lines without DUOX2 | 0.033 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB; co-absent with the target |
| [[CNTNAP3C]] | C | CNTNAP3C activity raises ARHGAP20's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 2.14× lower at baseline in the lines without CNTNAP3C | 0.052 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |
| [[SHROOM4]] | C | SHROOM4 activity raises ARHGAP20's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 2.00× lower at baseline in the lines without SHROOM4 | 0.085 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539; co-absent with the target |
| [[CFI]] | C | CFI activity raises ARHGAP20's level | lines that do not express CFI (31) vs lines expressing it (19) | 2.12× lower at baseline in the lines without CFI | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST6GALNAC3]] | B | ARHGAP20 activity raises ST6GALNAC3's level | lines that do not express ARHGAP20 (34) vs lines expressing it (16) | 3.63× lower at baseline in the lines without ARHGAP20 | 0.005 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, GYPC |
| [[STRIP2]] | B | ARHGAP20 activity raises STRIP2's level | lines that do not express ARHGAP20 (34) vs lines expressing it (16) | 1.68× lower at baseline in the lines without ARHGAP20 | 0.027 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, GYPC |
| [[ENDOD1]] | B | ARHGAP20 activity raises ENDOD1's level | lines that do not express ARHGAP20 (34) vs lines expressing it (16) | 1.20× lower at baseline in the lines without ARHGAP20 | 0.082 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, GYPC |
| [[DAAM2]] | C | ARHGAP20 activity raises DAAM2's level | lines that do not express ARHGAP20 (34) vs lines expressing it (16) | 2.44× lower at baseline in the lines without ARHGAP20 | 0.019 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, GYPC; co-absent with the target |
| [[CFI]] | C | ARHGAP20 activity raises CFI's level | lines that do not express ARHGAP20 (34) vs lines expressing it (16) | 2.77× lower at baseline in the lines without ARHGAP20 | 0.061 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, GYPC; co-absent with the target |
| [[RHOJ]] | C | ARHGAP20 activity raises RHOJ's level | lines that do not express ARHGAP20 (34) vs lines expressing it (16) | 2.51× lower at baseline in the lines without ARHGAP20 | 0.070 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, GYPC; co-absent with the target |
| [[LHFPL3-AS1]] | C | ARHGAP20 activity raises LHFPL3-AS1's level | lines that do not express ARHGAP20 (34) vs lines expressing it (16) | 2.78× lower at baseline in the lines without ARHGAP20 | 0.075 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, GYPC; co-absent with the target |
| [[SOX10]] | C | ARHGAP20 activity raises SOX10's level | lines that do not express ARHGAP20 (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without ARHGAP20 | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, GYPC; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.497). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.7, 30.6); signed map (31.2, 40.5). **Vector** length 31.8, 7.24% of its response variance represented; |z| ≥ 3 in 376 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.7 | +6.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | +1.1 | +2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.1 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.9 | +9.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.7 | -1.0 |
|  | [[EX229 (drug)]] 5 µM |  | +0.6 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.6 | +3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.6 | +1.4 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | +0.6 |
|  | [[crizotinib (drug)]] 5 µM |  | -0.7 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.7 | -1.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.6 | -3.4 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -0.5 | -1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3-q23.1 — chr11:110,577,042-110,713,189 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1391 |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 6 pathways, smallest: RHOA GTPase cycle; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2F6](https://www.uniprot.org/uniprotkb/Q9P2F6) (Rho GTPase-activating protein 20):

> GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state.

**Summary**, from NCBI Gene [57569](https://www.ncbi.nlm.nih.gov/gene/57569):

> The protein encoded by this gene is an activator of RHO-type GTPases, transducing a signal from RAP1 to RHO and impacting neurite outgrowth. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:18357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18357) · Entrez [57569](https://www.ncbi.nlm.nih.gov/gene/57569) · UniProt [Q9P2F6](https://www.uniprot.org/uniprotkb/Q9P2F6) · Ensembl [ENSG00000137727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137727)

## Data

Gene col 6057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6057); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6057]; `tensor/DDL_lfc|DDL_z.npy` [6057]; `embed/gene_vectors.npy` [6057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6057 or target_col == 6057). Every well: [[ARHGAP20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

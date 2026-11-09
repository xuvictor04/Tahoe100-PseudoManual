---
symbol: "TDRD9"
type: "gene"
col: 7978
ensembl_id: "ENSG00000156414"
name: "tudor domain containing 9"
location: "14q32.33"
module: 87
arm: "+"
pooled_cpm: 4.82
n_lines_expressing: 13
n_dd_up: 31
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 19
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# TDRD9

*tudor domain containing 9* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.48× (z +21.3, q 0e+00, up in 2 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.589× (z -4.4, q 0.008, down in 3 of 10 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.169×, SNU-423 0.287×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-1 0.176×, C32 0.126×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (C32 0.0964×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF175]] (+0.63, fdr 7e-06), [[MIR3681HG]] (+0.60, fdr 7e-06), [[LEF1-AS1]] (+0.60, fdr 8e-06); moves opposite to [[TRIQK]] (-0.40, fdr 2e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[COL19A1]] → it (grade C ⚠); 19 go from it, the strongest it → [[SYN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.48×** | +21.3 | 0e+00 | 2/7 (HOP62, hTERT-HPNE) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.97×** | +15.2 | 0e+00 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.46×** | +13.2 | 9e-38 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.56×** | +10.4 | 4e-23 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +7.9 | 4e-13 | 2/9 (hTERT-HPNE, HepG2/C3A) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.2 | 5e-08 | 6/10 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.67×** | +6.2 | 5e-08 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +5.7 | 7e-07 | 0/5 | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +5.1 | 2e-05 | 0/6 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.6 | 2e-04 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +4.0 | 0.004 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.005 | 1/7 (HOP62) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.82×** | +3.8 | 0.007 | 1/10 (A498) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +3.7 | 0.009 | 2/7 (A498, NCI-H1573) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +3.6 | 0.013 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.50×** | +3.6 | 0.013 | 1/8 (RPMI-7951) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.016 | 5/10 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.021 | 0/10 | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.025 | 0/9 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.025 | 1/9 (SK-MEL-2) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.039 | 0/6 | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.050 | 0/6 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7978.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.169×, SNU-423 0.287×); [[Dinaciclib (drug)]] 5 µM in 2 lines (SNU-1 0.176×, C32 0.126×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (C32 0.0964×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.589×** | -4.4 | 0.008 | 3/10 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses |  |
| [[Lopinavir (drug)]] 0.5 µM |  | 0.681× | -3.4 | 0.18 | 1/10 (RPMI-7951) | inconsistent across doses |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 0.677× | -3.3 | 0.19 | 1/10 (HOP62) | inconsistent across doses |  |
| [[Verapamil (drug)]] 0.05 µM |  | 0.687× | -3.1 | 0.28 | 1/9 (hTERT-HPNE) | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | 0.524× | -3.0 | 0.29 | 0/10 | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 24.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -12.7) |
| [[SNU-1 (line)]] | wt | 81.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 27.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.8) |
| [[A-172 (line)]] | wt | 0.702 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.763 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.872 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.904 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.999 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.667 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.570 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF175]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[MIR3681HG]] | +0.60 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[LEF1-AS1]] | +0.60 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[A2M]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[LRAT]] | +0.58 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[AEBP1]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[C10orf90]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[STAG3]] | +0.55 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[SOX10]] | +0.54 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[DPYSL4]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[GLDC]] | +0.53 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[CACNA1H]] | +0.53 | +0.46 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIQK]] | -0.40 | -0.41 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL19A1]] | C | COL19A1 activity raises TDRD9's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 1.19× lower at baseline in the lines without COL19A1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[IHO1]] | C | IHO1 activity raises TDRD9's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 1.69× lower at baseline in the lines without IHO1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[CTTNBP2]] | C | CTTNBP2 activity raises TDRD9's level | lines that do not express CTTNBP2 (31) vs lines expressing it (19) | 1.38× lower at baseline in the lines without CTTNBP2 | 0.039 | ⚠ within organs, on part of the lines; also absent: DCT, ENSG00000266976, TYR; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises TDRD9's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 1.40× lower at baseline in the lines without AEBP1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[LHFPL3-AS1]] | C | LHFPL3-AS1 activity raises TDRD9's level | lines that do not express LHFPL3-AS1 (44) vs lines expressing it (6) | 1.96× lower at baseline in the lines without LHFPL3-AS1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: TYR, DCT, CHL1; co-absent with the target |
| [[FCRLA]] | C | FCRLA activity raises TDRD9's level | lines that do not express FCRLA (41) vs lines expressing it (9) | 1.55× lower at baseline in the lines without FCRLA | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SOX10, TYR, ENSG00000287474; co-absent with the target |
| [[LEF1]] | C | LEF1 activity raises TDRD9's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 1.25× lower at baseline in the lines without LEF1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1; co-absent with the target |
| [[ITIH5]] | C | ITIH5 activity raises TDRD9's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 2.46× lower at baseline in the lines without ITIH5 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 6, C 13. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYN3]] | B | TDRD9 activity raises SYN3's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 2.31× lower at baseline in the lines without TDRD9 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT |
| [[ALK]] | B | TDRD9 activity raises ALK's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 2.14× lower at baseline in the lines without TDRD9 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT |
| [[EFCAB13-DT]] | B | TDRD9 activity raises EFCAB13-DT's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 1.50× lower at baseline in the lines without TDRD9 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT |
| [[KCNS3]] | B | TDRD9 activity raises KCNS3's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 2.25× lower at baseline in the lines without TDRD9 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT |
| [[SRPX]] | B | TDRD9 activity raises SRPX's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 3.61× lower at baseline in the lines without TDRD9 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT |
| cells under [[Tucidinostat (drug)]] 5 µM | B | TDRD9 activity lowers the cells' numbers under Tucidinostat 5 µM (makes them more sensitive) | lines that do not express TDRD9 (37) vs lines expressing it (11) | the lines without TDRD9: 1.11× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT |
| [[AEBP1]] | C | TDRD9 activity raises AEBP1's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 4.01× lower at baseline in the lines without TDRD9 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |
| [[DAAM2]] | C | TDRD9 activity raises DAAM2's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 2.80× lower at baseline in the lines without TDRD9 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |
| [[LOXL3]] | C | TDRD9 activity raises LOXL3's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 4.81× lower at baseline in the lines without TDRD9 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |
| [[C10orf90]] | C | TDRD9 activity raises C10orf90's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 3.70× lower at baseline in the lines without TDRD9 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |
| [[A2M]] | C | TDRD9 activity raises A2M's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 5.16× lower at baseline in the lines without TDRD9 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |
| [[CTTNBP2]] | C | TDRD9 activity raises CTTNBP2's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 2.98× lower at baseline in the lines without TDRD9 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.9, 28.7); signed map (28.6, 39.2). **Vector** length 20.5, 4.41% of its response variance represented; |z| ≥ 3 in 230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.2 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +2.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.5 | +1.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.5 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.9 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -0.7 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.5 | -1.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | -1.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.5 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.5 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.4 | -1.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | tudor domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:103,928,456-104,052,667 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434N0820, FLJ36164, NET54; previously C14orf75 |
| Gene groups (HGNC) | Tudor domain containing |
| Reactome | 2 pathways, smallest: PIWI-interacting RNA (piRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDG6](https://www.uniprot.org/uniprotkb/Q8NDG6) (ATP-dependent RNA helicase TDRD9):

> ATP-binding RNA helicase required during spermatogenesis. Required to repress transposable elements and prevent their mobilization, which is essential for the germline integrity. Acts via the piRNA metabolic process, which mediates the repression of transposable elements during meiosis by forming complexes composed of piRNAs and Piwi proteins and governs the methylation and subsequent repression of transposons. Acts downstream of piRNA biogenesis: exclusively required for transposon silencing …

**Summary**, from NCBI Gene [122402](https://www.ncbi.nlm.nih.gov/gene/122402):

> Predicted to enable ATP hydrolysis activity; RNA binding activity; and helicase activity. Involved in spermatogenesis. Located in cytoplasm and nucleus. Implicated in spermatogenic failure 30. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20122) · Entrez [122402](https://www.ncbi.nlm.nih.gov/gene/122402) · UniProt [Q8NDG6](https://www.uniprot.org/uniprotkb/Q8NDG6) · Ensembl [ENSG00000156414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156414)

## Data

Gene col 7978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7978); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7978]; `tensor/DDL_lfc|DDL_z.npy` [7978]; `embed/gene_vectors.npy` [7978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7978 or target_col == 7978). Every well: [[TDRD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TDRD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

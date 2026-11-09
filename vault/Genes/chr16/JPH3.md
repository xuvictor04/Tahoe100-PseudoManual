---
symbol: "JPH3"
type: "gene"
col: 7771
ensembl_id: "ENSG00000154118"
name: "junctophilin 3"
location: "16q24.2"
module: 128
arm: "+"
pooled_cpm: 4.42
n_lines_expressing: 21
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 21
direction_downstream: 21
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# JPH3

*junctophilin 3* — 16q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.80× (z +15.9, q 0e+00, up in 2 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.556× (z -6.5, q 5e-08, down in 14 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNA1B]] (+0.71, fdr 7e-06), [[RFPL1S]] (+0.64, fdr 1e-05), [[ADGRB1]] (+0.63, fdr 1e-05).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[FSD1]] → it (grade B ⚠); 21 go from it, the strongest it → [[ID2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +15.9 | 0e+00 | 2/19 (HOP62, BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.19×** | +15.6 | 0e+00 | 4/11 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.91×** | +14.3 | 4e-44 | 5/7 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +10.6 | 3e-24 | 3/9 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +5.1 | 4e-05 | 6/18 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +4.9 | 8e-05 | 0/17 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.8 | 1e-04 | 4/18 (SW480, NCI-H460, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.79×** | +4.5 | 4e-04 | 2/12 (SW480, A549) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.4 | 5e-04 | 2/14 (BT-474, A-172) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.77×** | +4.4 | 5e-04 | 1/11 (HOP62) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.7 | 0.010 | 0/11 | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.024 | 2/18 (HOP62, H4) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.4 | 0.035 | 2/18 (A-172, C-33 A) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.2 | 0.059 | 1/16 (H4) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.061 | 2/18 (A-427, C-33 A) | rises with dose | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.061 | 1/18 (BT-474) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.061 | 2/19 (PANC-1, NCI-H2030) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.064 | 4/16 (NCI-H460, BT-474, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +2.9 | 0.100 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7771.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.556×** | -6.5 | 5e-08 | 14/18 (NCI-H23, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.667×** | -4.5 | 0.002 | 11/18 (SW 900, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.704×** | -3.9 | 0.019 | 3/18 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.710×** | -3.8 | 0.021 | 9/17 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.714×** | -3.7 | 0.021 | 13/18 (NCI-H23, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 32.7 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.159× (z -12.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C-33 A (line)]] | alt | 48.1 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 9.34 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0196× (z -16.5) |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.6) |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0520× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 2.97 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0713× (z -10.6) |
| [[A-172 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.609 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.582 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.875 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNA1B]] | +0.71 | +0.68 / +0.59 | both halves | 7e-06 | STRING 491 |
| [[RFPL1S]] | +0.64 | +0.59 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[ADGRB1]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[LRRC36]] | +0.62 | +0.59 / +0.46 | both halves | 3e-05 | **novel candidate** |
| [[PALM]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[RNF212]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[DPYSL5]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[RASGEF1A]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[LINC00466]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[MYT1]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[GRID1]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[KIF1A]] | +0.57 | +0.61 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 3, C 18. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSD1]] | B | FSD1 activity raises JPH3's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 2.35× lower at baseline in the lines without FSD1 | 0.033 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[SSPOP]] | B | SSPOP activity raises JPH3's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 2.32× lower at baseline in the lines without SSPOP | 0.094 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[ID2-AS1]] | B | ID2-AS1 activity raises JPH3's level | lines that do not express ID2-AS1 (8) vs lines expressing it (42) | 2.35× lower at baseline in the lines without ID2-AS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ID2, RDM1P5 |
| [[CHD5]] | C | CHD5 activity raises JPH3's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 3.54× lower at baseline in the lines without CHD5 | 0.002 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; co-absent with the target |
| [[DPYSL5]] | C | DPYSL5 activity raises JPH3's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 4.28× lower at baseline in the lines without DPYSL5 | 0.003 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |
| [[JAKMIP1]] | C | JAKMIP1 activity raises JPH3's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 4.24× lower at baseline in the lines without JAKMIP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[PLEKHG4B]] | C | PLEKHG4B activity raises JPH3's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 3.38× lower at baseline in the lines without PLEKHG4B | 0.005 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[KCNQ2]] | C | KCNQ2 activity raises JPH3's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.80× lower at baseline in the lines without KCNQ2 | 0.013 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P; co-absent with the target |
| [[SLC6A17]] | C | SLC6A17 activity raises JPH3's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.09× lower at baseline in the lines without SLC6A17 | 0.014 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[MYT1]] | C | MYT1 activity raises JPH3's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 3.13× lower at baseline in the lines without MYT1 | 0.020 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2; co-absent with the target |
| [[RET]] | C | RET activity raises JPH3's level | lines that do not express RET (28) vs lines expressing it (22) | 3.24× lower at baseline in the lines without RET | 0.021 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises JPH3's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 3.21× lower at baseline in the lines without KIF1A | 0.021 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 7, C 14. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ID2-AS1]] | B | JPH3 activity raises ID2-AS1's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 1.92× lower at baseline in the lines without JPH3 | 0.010 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent |
| [[TCEA2]] | B | JPH3 activity raises TCEA2's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without JPH3 | 0.030 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent |
| [[CDH23]] | B | JPH3 activity strengthens CDH23's drug response | lines that do not express JPH3 (29) vs lines expressing it (17) | the lines without JPH3 respond 0.65× as strongly (z diff +0.87); strongest at Dinaciclib 5 µM: 0.84x vs 2.68x (z diff +3.9) | 0.036 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MIR1915HG]] | B | JPH3 activity raises MIR1915HG's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 1.74× lower at baseline in the lines without JPH3 | 0.060 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent |
| [[CELF5]] | B | JPH3 activity raises CELF5's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 1.62× lower at baseline in the lines without JPH3 | 0.067 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent |
| [[TMEM150C]] | B | JPH3 activity raises TMEM150C's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 2.72× lower at baseline in the lines without JPH3 | 0.079 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent |
| [[LINC02026]] | B | JPH3 activity raises LINC02026's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 1.33× lower at baseline in the lines without JPH3 | 0.081 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent |
| [[SCN8A]] | C | JPH3 activity raises SCN8A's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 3.31× lower at baseline in the lines without JPH3 | 0.009 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |
| [[PDZD4]] | C | JPH3 activity raises PDZD4's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 2.62× lower at baseline in the lines without JPH3 | 0.010 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |
| [[CACNA2D2]] | C | JPH3 activity raises CACNA2D2's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 2.27× lower at baseline in the lines without JPH3 | 0.017 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |
| [[CTNNA2]] | C | JPH3 activity raises CTNNA2's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 3.79× lower at baseline in the lines without JPH3 | 0.020 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |
| [[KIF1A]] | C | JPH3 activity raises KIF1A's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 6.36× lower at baseline in the lines without JPH3 | 0.020 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.832). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.4, 37.6); signed map (24.7, 25.4). **Vector** length 40.4, 8.71% of its response variance represented; |z| ≥ 3 in 453 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -6.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.3 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.8 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | junctophilin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.2 — chr16:87,601,835-87,698,156 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JP-3, CAGL237, HDL2, JP3; previously TNRC22 |
| Gene groups (HGNC) | Junctophilins; MORN repeat containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXH2](https://www.uniprot.org/uniprotkb/Q8WXH2) (Junctophilin-3):

> Junctophilins contribute to the formation of junctional membrane complexes (JMCs) which link the plasma membrane with the endoplasmic or sarcoplasmic reticulum in excitable cells. Provides a structural foundation for functional cross-talk between the cell surface and intracellular calcium release channels. JPH3 is brain-specific and appears to have an active role in certain neurons involved in motor coordination and memory.

**Summary**, from NCBI Gene [57338](https://www.ncbi.nlm.nih.gov/gene/57338):

> Junctional complexes between the plasma membrane and endoplasmic/sarcoplasmic reticulum are a common feature of all excitable cell types and mediate cross talk between cell surface and intracellular ion channels. The protein encoded by this gene is a component of junctional complexes and is composed of a C-terminal hydrophobic segment spanning the endoplasmic/sarcoplasmic reticulum membrane and a remaining cytoplasmic domain that shows specific affinity for the plasma membrane. CAG/CTG repeat …

**Accessions** — [HGNC:14203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14203) · Entrez [57338](https://www.ncbi.nlm.nih.gov/gene/57338) · UniProt [Q8WXH2](https://www.uniprot.org/uniprotkb/Q8WXH2) · Ensembl [ENSG00000154118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154118)

## Data

Gene col 7771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7771); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7771]; `tensor/DDL_lfc|DDL_z.npy` [7771]; `embed/gene_vectors.npy` [7771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7771 or target_col == 7771). Every well: [[JPH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JPH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

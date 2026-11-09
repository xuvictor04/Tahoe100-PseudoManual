---
symbol: "KCNQ2"
type: "gene"
col: 1098
ensembl_id: "ENSG00000075043"
name: "potassium voltage-gated channel subfamily Q member 2"
location: "20q13.33"
module: 128
arm: "+"
pooled_cpm: 4.21
n_lines_expressing: 21
n_dd_up: 27
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 27
direction_downstream: 20
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# KCNQ2

*potassium voltage-gated channel subfamily Q member 2* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.38× (z +19.8, q 0e+00, up in 13 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.612× (z -4.3, q 0.008, down in 1 of 17 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.100×, NCI-H23 0.252×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.142×, AN3 CA 0.0849×; ⚠ cell-cycle shift, explains ~47% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.206×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPYSL5]] (+0.70, fdr 7e-06), [[CACNA2D2]] (+0.68, fdr 7e-06), [[CAMK2B]] (+0.67, fdr 7e-06); moves opposite to [[DECR1]] (-0.51, fdr 1e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[GNAO1]] → it (grade B ⚠); 20 go from it, the strongest it → [[CACNA2D2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.38×** | +19.8 | 0e+00 | 13/17 (SW480, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.32×** | +19.6 | 0e+00 | 6/13 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **6.08×** | +17.1 | 0e+00 | 13/18 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.82×** | +14.9 | 0e+00 | 11/17 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.20×** | +13.1 | 4e-37 | 1/6 (MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.56×** | +12.0 | 2e-31 | 3/9 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.46×** | +11.8 | 4e-30 | 9/17 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +11.5 | 1e-28 | 5/16 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.45×** | +10.9 | 1e-25 | 2/6 (PANC-1, MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.71×** | +9.5 | 2e-19 | 5/16 (SW480, SW1417, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.18×** | +7.4 | 7e-12 | 5/15 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.16×** | +7.3 | 1e-11 | 9/17 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.2 | 7e-06 | 3/13 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.83×** | +5.2 | 1e-05 | 1/6 (MIA PaCa-2) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +4.4 | 4e-04 | 1/9 (NCI-H23) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.88×** | +4.3 | 7e-04 | 1/13 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.47×** | +3.3 | 0.025 | 3/11 (SW480, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.62×** | +3.3 | 0.031 | 1/9 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.043 | 0/16 | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.043 | 3/11 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1098.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.100×, NCI-H23 0.252×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.142×, AN3 CA 0.0849×; ⚠ cell-cycle shift, explains ~47% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.206×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.612×** | -4.3 | 0.008 | 1/17 (H4) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.486×** | -3.6 | 0.092 | 4/15 (MIA PaCa-2, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.721× | -3.1 | 0.34 | 1/17 (KATO III) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.83 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.0787× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 16.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.100× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 82.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -11.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 7.80 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 12.2× (z +14.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.32× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0849× (z -9.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H23 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.252× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 3.47 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.03× (z +11.1) | — |
| [[A-172 (line)]] | wt | 0.764 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.771 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.946 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.609 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.826 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.956 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.480 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.830 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.611 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPYSL5]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[CACNA2D2]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 | pathway: Neuronal System |
| [[CAMK2B]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 | pathway: Neuronal System |
| [[KIF26A]] | +0.66 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PDZD4]] | +0.65 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[RET]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[JAKMIP1]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[FSD1]] | +0.65 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[BRSK2]] | +0.64 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[RASGEF1C]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[PALM]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CDH23]] | +0.63 | +0.61 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.51 | -0.36 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 8, C 19. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAO1]] | B | GNAO1 activity raises KCNQ2's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 1.95× lower at baseline in the lines without GNAO1 | 0.019 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[ELFN1]] | B | ELFN1 activity raises KCNQ2's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without ELFN1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[KIF26A]] | B | KIF26A activity raises KCNQ2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.23× lower at baseline in the lines without KIF26A | 0.061 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[MED12L]] | B | MED12L activity raises KCNQ2's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.36× lower at baseline in the lines without MED12L | 0.072 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[ADGRB1]] | B | ADGRB1 activity raises KCNQ2's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.34× lower at baseline in the lines without ADGRB1 | 0.074 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[KREMEN2]] | B | KREMEN2 activity raises KCNQ2's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without KREMEN2 | 0.080 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[RFPL1S]] | B | RFPL1S activity raises KCNQ2's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.30× lower at baseline in the lines without RFPL1S | 0.088 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[SDK2]] | B | SDK2 activity raises KCNQ2's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 2.26× lower at baseline in the lines without SDK2 | 0.097 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent |
| [[KIF1A]] | C | KIF1A activity raises KCNQ2's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 4.26× lower at baseline in the lines without KIF1A | 0.002 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[CHD5]] | C | CHD5 activity raises KCNQ2's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.67× lower at baseline in the lines without CHD5 | 0.005 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; co-absent with the target |
| [[NFASC]] | C | NFASC activity raises KCNQ2's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.41× lower at baseline in the lines without NFASC | 0.007 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[LRRC4B]] | C | LRRC4B activity raises KCNQ2's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 2.51× lower at baseline in the lines without LRRC4B | 0.010 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 10, C 10. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA2D2]] | B | KCNQ2 activity raises CACNA2D2's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.67× lower at baseline in the lines without KCNQ2 | 0.006 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[SYN2]] | B | KCNQ2 activity raises SYN2's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.86× lower at baseline in the lines without KCNQ2 | 0.027 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[OLFM2]] | B | KCNQ2 activity raises OLFM2's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.46× lower at baseline in the lines without KCNQ2 | 0.041 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[ADGRB1]] | B | KCNQ2 activity raises ADGRB1's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.05× lower at baseline in the lines without KCNQ2 | 0.053 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[KREMEN2]] | B | KCNQ2 activity raises KREMEN2's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 1.73× lower at baseline in the lines without KCNQ2 | 0.056 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[EFHD1]] | B | KCNQ2 activity raises EFHD1's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 1.97× lower at baseline in the lines without KCNQ2 | 0.058 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[APC2]] | B | KCNQ2 activity raises APC2's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 1.50× lower at baseline in the lines without KCNQ2 | 0.063 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[SDK2]] | B | KCNQ2 activity raises SDK2's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.33× lower at baseline in the lines without KCNQ2 | 0.069 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[GDF1]] | B | KCNQ2 activity raises GDF1's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 1.39× lower at baseline in the lines without KCNQ2 | 0.079 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[SRCIN1]] | B | KCNQ2 activity raises SRCIN1's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.05× lower at baseline in the lines without KCNQ2 | 0.091 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[CACNA1H]] | C | KCNQ2 activity raises CACNA1H's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.24× lower at baseline in the lines without KCNQ2 | 0.011 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P; co-absent with the target |
| [[SBK1]] | C | KCNQ2 activity raises SBK1's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.91× lower at baseline in the lines without KCNQ2 | 0.013 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.9, 38.7); signed map (26.4, 26.5). **Vector** length 35.9, 7.38% of its response variance represented; |z| ≥ 3 in 463 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +19.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +9.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.2 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | +0.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -4.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily Q member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,400,208-63,472,677 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kv7.2, ENB1, BFNC, KCNA11, HNSPC; previously EBN, EBN1 |
| Gene groups (HGNC) | Potassium voltage-gated channels |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 7 pathways, smallest: Voltage gated Potassium channels; Interaction between L1 and Ankyrins; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [O43526](https://www.uniprot.org/uniprotkb/O43526) (Potassium voltage-gated channel subfamily KQT member 2):

> Pore-forming subunit of the voltage-gated potassium (Kv) M-channel which is responsible for the M-current, a key controller of neuronal excitability. M-channel is composed of pore-forming subunits KCNQ2 and KCNQ3 assembled as heterotetramers. The native M-current has a slowly activating and deactivating potassium conductance which plays a critical role in determining the subthreshold electrical excitability of neurons as well as the responsiveness to synaptic inputs. KCNQ2-KCNQ3 M-channel is …

**Summary**, from NCBI Gene [3785](https://www.ncbi.nlm.nih.gov/gene/3785):

> The M channel is a slowly activating and deactivating potassium channel that plays a critical role in the regulation of neuronal excitability. The M channel is formed by the association of the protein encoded by this gene and a related protein encoded by the KCNQ3 gene, both integral membrane proteins. M channel currents are inhibited by M1 muscarinic acetylcholine receptors and activated by retigabine, a novel anti-convulsant drug. Defects in this gene are a cause of benign familial neonatal …

**Accessions** — [HGNC:6296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6296) · Entrez [3785](https://www.ncbi.nlm.nih.gov/gene/3785) · UniProt [O43526](https://www.uniprot.org/uniprotkb/O43526) · Ensembl [ENSG00000075043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075043)

## Data

Gene col 1098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1098); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1098]; `tensor/DDL_lfc|DDL_z.npy` [1098]; `embed/gene_vectors.npy` [1098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1098 or target_col == 1098). Every well: [[KCNQ2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNQ2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

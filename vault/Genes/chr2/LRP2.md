---
symbol: "LRP2"
type: "gene"
col: 1319
ensembl_id: "ENSG00000081479"
name: "LDL receptor related protein 2"
location: "2q31.1"
module: 152
arm: "+"
pooled_cpm: 3.56
n_lines_expressing: 28
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# LRP2

*LDL receptor related protein 2* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.11× (z +20.2, q 0e+00, up in 11 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.587× (z -4.7, q 0.002, down in 11 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA3]] (+0.70, fdr 7e-06), [[LRRC7]] (+0.65, fdr 1e-05), [[ADGRL3]] (+0.63, fdr 7e-06).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NRN1]] → it (grade B ⚠); 10 go from it, the strongest it → [[NRN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1319.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.11×** | +20.2 | 0e+00 | 11/16 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.00×** | +13.6 | 9e-40 | 18/23 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.44×** | +10.8 | 5e-25 | 4/10 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +9.8 | 1e-20 | 1/3 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.62×** | +8.4 | 4e-15 | 16/23 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.60×** | +8.3 | 7e-15 | 14/19 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.36×** | +7.5 | 4e-12 | 9/22 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +7.2 | 5e-11 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.17×** | +6.8 | 8e-10 | 11/23 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.15×** | +6.7 | 1e-09 | 14/23 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +5.9 | 2e-07 | 4/15 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.90×** | +5.6 | 1e-06 | 6/23 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +4.4 | 4e-04 | 3/19 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.47×** | +4.1 | 0.001 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +3.8 | 0.005 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.009 | 7/22 (NCI-H23, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.17×** | +3.6 | 0.013 | 9/20 (NCI-H23, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.017 | 0/12 | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.035 | 8/16 (NCI-H23, BT-474, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.043 | 1/17 (C-33 A) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.65×** | +3.1 | 0.043 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1319.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.587×** | -4.7 | 0.002 | 11/23 (NCI-H1792, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.637×** | -4.0 | 0.022 | 6/19 (LoVo, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.639×** | -3.7 | 0.035 | 9/21 (BT-474, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.690× | -3.2 | 0.16 | 8/21 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.774× | -3.2 | 0.17 | 2/23 (SHP-77, H4) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 21.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0648× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.104× (z -8.6) |
| [[C32 (line)]] | wt | 74.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 1.62 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.7× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0290× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 6.33 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.44× (z +8.6) | — |
| [[A-172 (line)]] | wt | 0.860 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.744 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.888 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.886 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.968 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.944 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.856 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.700 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.962 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.746 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA3]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[LRRC7]] | +0.65 | +0.53 / +0.72 | both halves | 1e-05 | STRING 459 |
| [[ADGRL3]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[NREP]] | +0.62 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[GRID2]] | +0.61 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[ASXL3]] | +0.59 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[GABRA2]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ARHGAP28]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ADGRV1]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[EPHA6]] | +0.57 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[IQCM]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[TMEM108]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRN1]] | B | NRN1 activity raises LRP2's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without NRN1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[CFI]] | B | CFI activity raises LRP2's level | lines that do not express CFI (31) vs lines expressing it (19) | 1.53× lower at baseline in the lines without CFI | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[KCNJ6]] | C | KCNJ6 activity raises LRP2's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 2.11× lower at baseline in the lines without KCNJ6 | 0.016 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[ZMAT4]] | C | ZMAT4 activity raises LRP2's level | lines that do not express ZMAT4 (31) vs lines expressing it (19) | 2.14× lower at baseline in the lines without ZMAT4 | 0.045 | ⚠ within organs, on part of the lines; also absent: UBE2QL1, SHISAL1, SOX11; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRN1]] | B | LRP2 activity raises NRN1's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 3.11× lower at baseline in the lines without LRP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent |
| [[CNTNAP2]] | B | LRP2 activity raises CNTNAP2's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without LRP2 | 0.040 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent |
| [[SUSD4]] | B | LRP2 activity raises SUSD4's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 1.58× lower at baseline in the lines without LRP2 | 0.050 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent |
| [[SEMA6D]] | B | LRP2 activity raises SEMA6D's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 1.73× lower at baseline in the lines without LRP2 | 0.074 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent |
| [[SNAP25]] | C | LRP2 activity raises SNAP25's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 4.22× lower at baseline in the lines without LRP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent; co-absent with the target |
| [[RARB]] | C | LRP2 activity raises RARB's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 4.36× lower at baseline in the lines without LRP2 | 0.039 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent; co-absent with the target |
| [[EPHA3]] | C | LRP2 activity raises EPHA3's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 2.85× lower at baseline in the lines without LRP2 | 0.047 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent; co-absent with the target |
| [[KCTD16]] | C | LRP2 activity raises KCTD16's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 3.01× lower at baseline in the lines without LRP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent; co-absent with the target |
| [[KCNJ6]] | C | LRP2 activity raises KCNJ6's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 2.75× lower at baseline in the lines without LRP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent; co-absent with the target |
| [[ZMAT4]] | C | LRP2 activity raises ZMAT4's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 2.68× lower at baseline in the lines without LRP2 | 0.087 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.3, 29.6); signed map (32.2, 41.1). **Vector** length 42.1, 7.84% of its response variance represented; |z| ≥ 3 in 608 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +13.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +20.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +10.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +0.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.3 | -4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:169,127,109-169,362,534 (-) |
| Ensembl biotype | protein_coding |
| Also known as | gp330, DBS |
| Gene groups (HGNC) | Low density lipoprotein receptors |
| Reactome | 15 pathways, smallest: Transport of RCbl within the body; Vitamin D (calciferol) metabolism; Cobalamin (Cbl, vitamin B12) transport and metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P98164](https://www.uniprot.org/uniprotkb/P98164) (Low-density lipoprotein receptor-related protein 2):

> Multiligand endocytic receptor (By similarity). Acts together with CUBN to mediate endocytosis of high-density lipoproteins (By similarity). Mediates receptor-mediated uptake of polybasic drugs such as aprotinin, aminoglycosides and polymyxin B (By similarity). In the kidney, mediates the tubular uptake and clearance of leptin (By similarity). Also mediates transport of leptin across the blood-brain barrier through endocytosis at the choroid plexus epithelium (By similarity). Endocytosis of …

**Summary**, from NCBI Gene [4036](https://www.ncbi.nlm.nih.gov/gene/4036):

> The protein encoded by this gene, low density lipoprotein-related protein 2 (LRP2) or megalin, is a multi-ligand endocytic receptor that is expressed in many different tissues but primarily in absorptive epithilial tissues such as the kidney. This glycoprotein has a large amino-terminal extracellular domain, a single transmembrane domain, and a short carboxy-terminal cytoplasmic tail. The extracellular ligand-binding-domains bind diverse macromolecules including albumin, apolipoproteins B and …

**Accessions** — [HGNC:6694](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6694) · Entrez [4036](https://www.ncbi.nlm.nih.gov/gene/4036) · UniProt [P98164](https://www.uniprot.org/uniprotkb/P98164) · Ensembl [ENSG00000081479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081479)

## Data

Gene col 1319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1319); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1319]; `tensor/DDL_lfc|DDL_z.npy` [1319]; `embed/gene_vectors.npy` [1319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1319 or target_col == 1319). Every well: [[LRP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

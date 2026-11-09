---
symbol: "ARHGAP45"
type: "gene"
col: 11109
ensembl_id: "ENSG00000180448"
name: "Rho GTPase activating protein 45"
location: "19p13.3"
module: 132
arm: "+"
pooled_cpm: 10.77
n_lines_expressing: 43
n_dd_up: 4
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# ARHGAP45

*Rho GTPase activating protein 45* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.76× (z +4.8, q 9e-04, up in 15 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.478× (z -8.2, q 1e-13, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACAP3]] (+0.58, fdr 3e-05), [[BAIAP3]] (+0.58, fdr 5e-05), [[KLHL26]] (+0.57, fdr 9e-05); moves opposite to [[METTL4]] (-0.53, fdr 1e-04), [[VBP1]] (-0.53, fdr 9e-05), [[ANGEL2]] (-0.53, fdr 4e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CRACR2B]] → it (grade B ⚠); 2 go from it, the strongest it → [[TNK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +4.8 | 9e-04 | 15/33 (PANC-1, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +4.6 | 0.001 | 14/41 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.3 | 0.004 | 14/41 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.025 | 9/34 (PANC-1, SW1417, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.46× | +3.2 | 0.15 | 5/36 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Omeprazole (drug)]] 0.5 µM |  | 1.30× | +3.1 | 0.20 | 7/38 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11109.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.478×** | -8.2 | 1e-13 | 23/38 (HOP62, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.517×** | -7.8 | 2e-12 | 28/41 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.641×** | -7.4 | 3e-11 | 23/41 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.546×** | -7.1 | 2e-10 | 22/40 (HT-29, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -6.4 | 1e-08 | 23/36 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.585×** | -6.1 | 1e-07 | 19/31 (HOP62, HCT15, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.603×** | -5.7 | 8e-07 | 19/33 (HCT15, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.631×** | -5.4 | 4e-06 | 22/41 (NCI-H1792, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -4.8 | 1e-04 | 18/36 (Panc 03.27, C32, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.689×** | -4.4 | 7e-04 | 16/41 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.493×** | -4.3 | 7e-04 | 16/37 (SW480, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.715×** | -3.9 | 0.004 | 18/36 (SK-MEL-2, C32, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.728×** | -3.7 | 0.008 | 14/40 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -3.3 | 0.034 | 14/37 (HEC-1-A, C32, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.759×** | -3.2 | 0.046 | 16/36 (SW480, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.763×** | -3.2 | 0.054 | 13/41 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.771×** | -3.1 | 0.075 | 3/41 (SW480, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.616×** | -3.0 | 0.090 | 12/36 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 64.9 | 0 | 6 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0185× (z -22.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -8.6) |
| [[HOP62 (line)]] | alt | 18.6 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -12.6) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.218× (z -8.9) |
| [[J82 (line)]] | alt | 27.7 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.308× (z -12.2) |
| [[HepG2_C3A (line)]] | wt | 26.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 9.07 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 14.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -9.7) |
| [[HT-29 (line)]] | alt | 18.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.124× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 7.01 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.110× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.376× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0345× (z -15.5) |
| [[PANC-1 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.281× (z -9.1) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 9.89 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0458× (z -12.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAP3]] | +0.58 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[BAIAP3]] | +0.58 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[KLHL26]] | +0.57 | +0.45 / +0.36 | both halves | 9e-05 |  |
| [[ABCA7]] | +0.56 | +0.50 / +0.43 | both halves | 3e-05 | STRING 886; ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[JAG2]] | +0.56 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[FOXO6]] | +0.56 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[PPP1R13L]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SLC16A3]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[EFEMP2]] | +0.55 | +0.54 / +0.43 | both halves | 4e-05 |  |
| [[APBB3]] | +0.53 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[MAPK8IP3]] | +0.53 | +0.50 / +0.31 | both halves | 2e-04 |  |
| [[SCN1B]] | +0.53 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[PTPRU]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL4]] | -0.53 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[VBP1]] | -0.53 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[ANGEL2]] | -0.53 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[PRKACB]] | -0.53 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[GPATCH2]] | -0.48 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[NAA50]] | -0.47 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[PSMB5]] | -0.46 | -0.49 / -0.22 | both halves | 6e-04 |  |
| [[TDRD3]] | -0.45 | -0.40 / -0.23 | both halves | 5e-04 |  |
| [[PAPOLA]] | -0.45 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[EPM2A]] | -0.45 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[QRSL1]] | -0.45 | -0.42 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRACR2B]] | B | CRACR2B activity raises ARHGAP45's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 2.11× lower at baseline in the lines without CRACR2B | 0.039 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[JAG2]] | B | JAG2 activity raises ARHGAP45's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without JAG2 | 0.045 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ARHGAP45's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNK2]] | B | ARHGAP45 activity raises TNK2's level | lines that do not express ARHGAP45 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without ARHGAP45 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PRXL2B]] | B | ARHGAP45 activity raises PRXL2B's level | lines that do not express ARHGAP45 (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without ARHGAP45 | 0.076 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.308). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.5, -3.1); signed map (-22.8, 27.1). **Vector** length 74.4, 14.0% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.2 | -7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.9 | -8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -6.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -7.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 45 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,065,923-1,086,628 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0223, HA-1; previously HMHA1 |
| Gene groups (HGNC) | Minor histocompatibility antigens; F-BAR domain containing; AH/BAR family Rho GTPase activating proteins |
| Reactome | 8 pathways, smallest: RHOA GTPase cycle; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92619](https://www.uniprot.org/uniprotkb/Q92619) (Rho GTPase-activating protein 45):

> Contains a GTPase activator for the Rho-type GTPases (RhoGAP) domain that would be able to negatively regulate the actin cytoskeleton as well as cell spreading. However, also contains N-terminally a BAR-domin which is able to play an autoinhibitory effect on this RhoGAP activity.; Precursor of the histocompatibility antigen HA-1. More generally, minor histocompatibility antigens (mHags) refer to immunogenic peptide which, when complexed with MHC, can generate an immune response after …

**Summary**, from NCBI Gene [23526](https://www.ncbi.nlm.nih.gov/gene/23526):

> Predicted to enable GTPase activator activity. Predicted to be involved in negative regulation of small GTPase mediated signal transduction. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17102) · Entrez [23526](https://www.ncbi.nlm.nih.gov/gene/23526) · UniProt [Q92619](https://www.uniprot.org/uniprotkb/Q92619) · Ensembl [ENSG00000180448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180448)

## Data

Gene col 11109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11109); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11109]; `tensor/DDL_lfc|DDL_z.npy` [11109]; `embed/gene_vectors.npy` [11109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11109 or target_col == 11109). Every well: [[ARHGAP45 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP45.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

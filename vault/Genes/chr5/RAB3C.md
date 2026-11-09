---
symbol: "RAB3C"
type: "gene"
col: 7668
ensembl_id: "ENSG00000152932"
name: "RAB3C, member RAS oncogene family"
location: "5q11.2"
module: 19
arm: "+"
pooled_cpm: 4.95
n_lines_expressing: 19
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# RAB3C

*RAB3C, member RAS oncogene family* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.37× (z +15.9, q 0e+00, up in 13 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mozavaptan (drug)]] 5 µM in 1 line (SW1417 0.0635×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.237×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01035]] (+0.80, fdr 7e-06), [[DPP10]] (+0.73, fdr 7e-06), [[ADARB2]] (+0.70, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[RIMS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7668.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.37×** | +15.9 | 0e+00 | 13/15 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.11×** | +15.9 | 0e+00 | 5/10 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.19×** | +13.1 | 6e-37 | 12/13 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.19×** | +13.1 | 7e-37 | 11/14 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.98×** | +10.6 | 5e-24 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.52×** | +10.0 | 1e-21 | 1/5 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.44×** | +9.8 | 6e-21 | 12/13 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +8.7 | 2e-16 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +7.8 | 6e-13 | 3/8 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.56×** | +7.5 | 4e-12 | 13/14 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.33×** | +6.7 | 8e-10 | 3/13 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.31×** | +6.7 | 1e-09 | 7/12 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +6.5 | 3e-09 | 1/5 (SW1417) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.3 | 2e-08 | 3/14 (SHP-77, AN3 CA, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +6.0 | 7e-08 | 3/6 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +4.9 | 3e-05 | 1/7 (SW480) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.77×** | +4.2 | 8e-04 | 7/11 (SW480, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.001 | 9/14 (SW1417, NCI-H23, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +3.2 | 0.038 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7668.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mozavaptan (drug)]] 5 µM in 1 line (SW1417 0.0635×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.237×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.684× | -3.0 | 0.52 | 0/14 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7668. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.77 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.66× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 4.54 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 15.9× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 36.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -8.9) |
| [[SW1417 (line)]] | alt | 5.52 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0635× (z -9.2) |
| [[A-172 (line)]] | wt | 0.965 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.889 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.968 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.982 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.959 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.918 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.944 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.903 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7668), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01035]] | +0.80 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[DPP10]] | +0.73 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[ADARB2]] | +0.70 | +0.50 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[KCNJ6]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[NKAIN2]] | +0.66 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[CTNND2]] | +0.66 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[MARCHF1]] | +0.66 | +0.45 / +0.66 | both halves | 3e-05 | **novel candidate** |
| [[ADGRD1]] | +0.66 | +0.51 / +0.73 | both halves | 1e-05 |  |
| [[LINC03000]] | +0.66 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[SCARA5]] | +0.64 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[PDE1C]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PAX7]] | +0.63 | +0.53 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RAB3C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BMP5]] | C | BMP5 activity raises RAB3C's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 3.07× lower at baseline in the lines without BMP5 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises RAB3C's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.72× lower at baseline in the lines without DPP10 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[ADARB2]] | C | ADARB2 activity raises RAB3C's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 2.80× lower at baseline in the lines without ADARB2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[LINC01035]] | C | LINC01035 activity raises RAB3C's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 4.14× lower at baseline in the lines without LINC01035 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2; co-absent with the target |
| [[PDE1A]] | C | PDE1A activity raises RAB3C's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.33× lower at baseline in the lines without PDE1A | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[LINC02945]] | C | LINC02945 activity raises RAB3C's level | lines that do not express LINC02945 (38) vs lines expressing it (12) | 2.21× lower at baseline in the lines without LINC02945 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02211, ENSG00000285751, ENSG00000275016; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises RAB3C's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 2.55× lower at baseline in the lines without CDH10 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[LIN7A]] | C | LIN7A activity raises RAB3C's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 1.83× lower at baseline in the lines without LIN7A | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[UNC13A]] | C | UNC13A activity raises RAB3C's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 2.03× lower at baseline in the lines without UNC13A | 0.076 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent; co-absent with the target |
| [[XKR7]] | C | XKR7 activity raises RAB3C's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 2.30× lower at baseline in the lines without XKR7 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIMS1]] | B | RAB3C activity raises RIMS1's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without RAB3C | 0.043 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent |
| [[BMP5]] | C | RAB3C activity raises BMP5's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 4.05× lower at baseline in the lines without RAB3C | 0.012 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[CHGB]] | C | RAB3C activity raises CHGB's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without RAB3C | 0.020 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[CDH10]] | C | RAB3C activity raises CDH10's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 4.75× lower at baseline in the lines without RAB3C | 0.041 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[UNC13A]] | C | RAB3C activity raises UNC13A's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 2.71× lower at baseline in the lines without RAB3C | 0.042 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[VIPR2]] | C | RAB3C activity raises VIPR2's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 1.65× lower at baseline in the lines without RAB3C | 0.046 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[XKR7]] | C | RAB3C activity raises XKR7's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 1.85× lower at baseline in the lines without RAB3C | 0.059 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[ADARB2]] | C | RAB3C activity raises ADARB2's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 2.80× lower at baseline in the lines without RAB3C | 0.060 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[LINC01035]] | C | RAB3C activity raises LINC01035's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 2.54× lower at baseline in the lines without RAB3C | 0.085 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.2, 35.8); signed map (42.5, 42.5). **Vector** length 36.1, 10.0% of its response variance represented; |z| ≥ 3 in 378 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +15.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +6.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RAB3C, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:58,582,221-58,859,394 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 1 pathways, smallest: RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96E17](https://www.uniprot.org/uniprotkb/Q96E17) (Ras-related protein Rab-3C):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different sets of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion.

**Summary**, from NCBI Gene [115827](https://www.ncbi.nlm.nih.gov/gene/115827):

> This gene is a member of the RAS oncogene family and encodes a small GTPase. Other similar small GTPases are known to be involved in vesicle trafficking, and the encoded protein was shown to play a role in recycling phagocytosed MHC class 1 complexes to the cell surface. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:30269](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30269) · Entrez [115827](https://www.ncbi.nlm.nih.gov/gene/115827) · UniProt [Q96E17](https://www.uniprot.org/uniprotkb/Q96E17) · Ensembl [ENSG00000152932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152932)

## Data

Gene col 7668: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7668); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7668, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7668]; `tensor/DDL_lfc|DDL_z.npy` [7668]; `embed/gene_vectors.npy` [7668]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7668 or target_col == 7668). Every well: [[RAB3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

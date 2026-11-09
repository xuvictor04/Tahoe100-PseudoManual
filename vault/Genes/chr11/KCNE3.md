---
symbol: "KCNE3"
type: "gene"
col: 10618
ensembl_id: "ENSG00000175538"
name: "potassium voltage-gated channel subfamily E regulatory subunit 3"
location: "11q13.4"
module: 55
arm: "+"
pooled_cpm: 2.71
n_lines_expressing: 13
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 16
direction_downstream: 63
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# KCNE3

*potassium voltage-gated channel subfamily E regulatory subunit 3* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.79× (z +9.7, q 1e-19, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.89× (z +4.8, q 2e-04, up in 0 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Fenofibrate (drug)]] 0.05 µM: 0.443× (z -4.1, q 0.027, down in 2 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C9orf152]] (+0.85, fdr 7e-06), [[B3GAT1-DT]] (+0.82, fdr 7e-06), [[CLRN3]] (+0.82, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[PROM1]] → it (grade C ⚠); 63 go from it, the strongest it → [[PTPN22]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 12 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10618.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.79×** | +9.7 | 1e-19 | 2/3 (SW1417, KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.25×** | +7.1 | 2e-10 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.80×** | +7.1 | 2e-10 | 3/5 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.89×** | +4.8 | 2e-04 | 0/11 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.44×** | +4.7 | 2e-04 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.10×** | +4.3 | 0.002 | 1/6 (HT-29) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.99×** | +4.2 | 0.002 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +4.0 | 0.005 | 0/6 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.78×** | +3.9 | 0.006 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +3.9 | 0.006 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.8 | 0.008 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.90×** | +3.4 | 0.031 | 0/6 | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.86×** | +3.3 | 0.045 | 2/6 (HT-29, SW48) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.3 | 0.045 | 1/8 (NCI-H2347) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +3.2 | 0.050 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10618.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.443×** | -4.1 | 0.027 | 2/11 (CFPAC-1, HCT15) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.501×** | -3.7 | 0.051 | 9/11 (KATO III, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.529×** | -3.5 | 0.085 | 8/10 (KATO III, SW1417, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.531×** | -3.4 | 0.085 | 5/11 (KATO III, SW48, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.566× | -3.1 | 0.23 | 8/11 (KATO III, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 55.5 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0452× (z -22.2) |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0509× (z -14.3) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0861× (z -11.8) |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0459× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -13.2) |
| [[SW480 (line)]] | alt | 7.76 | 0 | 5 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0387× (z -12.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HT-29 (line)]] | alt | 4.43 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0701× (z -10.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW48 (line)]] | wt | 16.1 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0620× (z -9.3) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A-172 (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.209 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.845 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.230 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.316 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.278 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.753 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.811 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.813 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.226 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.322 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C9orf152]] | +0.85 | +0.83 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[B3GAT1-DT]] | +0.82 | +0.79 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CLRN3]] | +0.82 | +0.77 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[PROM1]] | +0.81 | +0.83 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[VWA2]] | +0.78 | +0.78 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[VIL1]] | +0.78 | +0.65 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[AXIN2]] | +0.77 | +0.76 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[GJB1]] | +0.77 | +0.76 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC02058]] | +0.77 | +0.69 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[GPX2]] | +0.77 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[BMP4]] | +0.76 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.76 | +0.71 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROM1]] | C | PROM1 activity raises KCNE3's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 3.54× lower at baseline in the lines without PROM1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1; co-absent with the target |
| [[AZGP1]] | C | AZGP1 activity raises KCNE3's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 3.04× lower at baseline in the lines without AZGP1 | 0.036 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises KCNE3's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 2.53× lower at baseline in the lines without CLIC5 | 0.038 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |
| [[KLK6]] | C | KLK6 activity raises KCNE3's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 3.03× lower at baseline in the lines without KLK6 | 0.047 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15; co-absent with the target |
| [[CCR3]] | C | CCR3 activity raises KCNE3's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.52× lower at baseline in the lines without CCR3 | 0.048 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises KCNE3's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 3.20× lower at baseline in the lines without KRT23 | 0.049 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[RGCC]] | C | RGCC activity raises KCNE3's level | lines that do not express RGCC (25) vs lines expressing it (25) | 1.56× lower at baseline in the lines without RGCC | 0.052 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CLIC5; co-absent with the target |
| [[BMP4]] | C | BMP4 activity raises KCNE3's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 2.55× lower at baseline in the lines without BMP4 | 0.055 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B; co-absent with the target |
| [[SKAP1]] | C | SKAP1 activity raises KCNE3's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 3.21× lower at baseline in the lines without SKAP1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1; co-absent with the target |
| [[LINC01814]] | C | LINC01814 activity raises KCNE3's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 2.47× lower at baseline in the lines without LINC01814 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3; co-absent with the target |
| [[TSPOAP1]] | C | TSPOAP1 activity raises KCNE3's level | lines that do not express TSPOAP1 (25) vs lines expressing it (25) | 2.16× lower at baseline in the lines without TSPOAP1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RNF39, MAL2, VWA2; co-absent with the target |
| [[LINC02331]] | C | LINC02331 activity raises KCNE3's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 2.41× lower at baseline in the lines without LINC02331 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2; co-absent with the target |

### Downstream of this gene

*63 arrows, 63 of them with an alert ⚠; grade A 0, B 7, C 56. Shown: the 12 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN22]] | B | KCNE3 activity raises PTPN22's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 2.93× lower at baseline in the lines without KCNE3 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2 |
| [[FUT2]] | B | KCNE3 activity raises FUT2's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 2.85× lower at baseline in the lines without KCNE3 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2 |
| [[RAMP1]] | B | KCNE3 activity raises RAMP1's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 2.82× lower at baseline in the lines without KCNE3 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2 |
| [[TMEM184A]] | B | KCNE3 activity raises TMEM184A's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 2.45× lower at baseline in the lines without KCNE3 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2 |
| [[NSUN7]] | B | KCNE3 activity raises NSUN7's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 2.79× lower at baseline in the lines without KCNE3 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2 |
| [[FGD3]] | B | KCNE3 activity raises FGD3's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 2.79× lower at baseline in the lines without KCNE3 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2 |
| [[HNF4G]] | B | KCNE3 activity raises HNF4G's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 3.97× lower at baseline in the lines without KCNE3 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2 |
| [[SKAP1]] | C | KCNE3 activity raises SKAP1's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 9.84× lower at baseline in the lines without KCNE3 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2; co-absent with the target |
| [[SNTB1]] | C | KCNE3 activity raises SNTB1's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 5.86× lower at baseline in the lines without KCNE3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2; co-absent with the target |
| [[BCL2L15]] | C | KCNE3 activity raises BCL2L15's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 4.32× lower at baseline in the lines without KCNE3 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2; co-absent with the target |
| [[TSPOAP1]] | C | KCNE3 activity raises TSPOAP1's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 3.18× lower at baseline in the lines without KCNE3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2; co-absent with the target |
| [[MACC1]] | C | KCNE3 activity raises MACC1's level | lines that do not express KCNE3 (37) vs lines expressing it (13) | 10.40× lower at baseline in the lines without KCNE3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SKAP1, SLC5A1, VWA2; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.0, 47.2); signed map (62.5, 12.5). **Vector** length 51.0, 22.0% of its response variance represented; |z| ≥ 3 in 311 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +0.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily E regulatory subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:74,454,841-74,467,729 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MiRP2, HOKPP |
| Gene groups (HGNC) | Potassium voltage-gated channel regulatory subunits |
| Reactome | 4 pathways, smallest: Phase 3 - rapid repolarisation; Phase 2 - plateau phase; Cardiac conduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6H6](https://www.uniprot.org/uniprotkb/Q9Y6H6) (Potassium voltage-gated channel subfamily E member 3):

> Ancillary protein that functions as a regulatory subunit of the voltage-gated potassium (Kv) channel complex composed of pore-forming and potassium-conducting alpha subunits and of regulatory beta subunits. KCNE3 beta subunit modulates the gating kinetics and enhances stability of the channel complex. Alters the gating of the delayed rectifier Kv channel containing KCNB1 alpha subunit. Associates with KCNC4/Kv3.4 alpha subunit to form the subthreshold Kv channel in skeletal muscle and to …

**Summary**, from NCBI Gene [10008](https://www.ncbi.nlm.nih.gov/gene/10008):

> Voltage-gated potassium (Kv) channels represent the most complex class of voltage-gated ion channels from both functional and structural standpoints. Their diverse functions include regulating neurotransmitter release, heart rate, insulin secretion, neuronal excitability, epithelial electrolyte transport, smooth muscle contraction, and cell volume. This gene encodes a member of the potassium channel, voltage-gated, isk-related subfamily. This member is a type I membrane protein, and a beta …

**Accessions** — [HGNC:6243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6243) · Entrez [10008](https://www.ncbi.nlm.nih.gov/gene/10008) · UniProt [Q9Y6H6](https://www.uniprot.org/uniprotkb/Q9Y6H6) · Ensembl [ENSG00000175538](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175538)

## Data

Gene col 10618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10618); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10618]; `tensor/DDL_lfc|DDL_z.npy` [10618]; `embed/gene_vectors.npy` [10618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10618 or target_col == 10618). Every well: [[KCNE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

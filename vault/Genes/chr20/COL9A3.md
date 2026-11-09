---
symbol: "COL9A3"
type: "gene"
col: 1706
ensembl_id: "ENSG00000092758"
name: "collagen type IX alpha 3 chain"
location: "20q13.33"
module: 44
arm: "+"
pooled_cpm: 9.09
n_lines_expressing: 22
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# COL9A3

*collagen type IX alpha 3 chain* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.82× (z +14.5, q 7e-45, up in 7 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.94× (z +9.0, q 4e-17, up in 8 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.607× (z -4.8, q 9e-04, down in 11 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (SW480 0.166×, KATO III 0.211×, HT-29 0.176×); [[Verteporfin (drug)]] 5 µM in 2 lines (HepG2/C3A 0.0313×, KATO III 0.252×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 0.100×, SW480 0.303×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GAS7]] (+0.58, fdr 6e-05), [[MSLN]] (+0.53, fdr 3e-05), [[KLK6]] (+0.53, fdr 2e-05); moves opposite to [[TTC4]] (-0.44, fdr 1e-04), [[ZMYM1]] (-0.43, fdr 7e-05), [[BLOC1S5]] (-0.43, fdr 2e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[IGFBP2]] → it (grade B ⚠); 2 go from it, the strongest it → [[TTYH3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.82×** | +14.5 | 7e-45 | 7/9 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.03×** | +13.3 | 4e-38 | 10/11 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.79×** | +11.8 | 7e-30 | 8/10 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +9.0 | 4e-17 | 8/17 (Hs 766T, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +4.8 | 2e-04 | 6/17 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +4.6 | 3e-04 | 8/13 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.4 | 9e-04 | 7/19 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.033 | 4/16 (RPMI-7951, C32, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +3.4 | 0.036 | 2/7 (SW480, SK-MEL-2) | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.47×** | +3.4 | 0.036 | 2/14 (SW1417, SW480) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.3 | 0.057 | 1/13 (SW1417) | top dose only | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1706.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (SW480 0.166×, KATO III 0.211×, HT-29 0.176×); [[Verteporfin (drug)]] 5 µM in 2 lines (HepG2/C3A 0.0313×, KATO III 0.252×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HT-29 0.100×, SW480 0.303×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.607×** | -4.8 | 9e-04 | 11/15 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.700× | -3.4 | 0.15 | 1/18 (C-33 A) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.686× | -3.4 | 0.15 | 2/18 (C-33 A, HOP62) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.720× | -3.2 | 0.21 | 4/18 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.547× | -3.0 | 0.27 | 3/18 (NCI-H1792, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 54.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -10.8) |
| [[SW480 (line)]] | alt | 28.8 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.33× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -14.3) |
| [[HT-29 (line)]] | alt | 17.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 43.6 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0313× (z -21.5) |
| [[PANC-1 (line)]] | alt | 7.20 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -9.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SK-MEL-2 (line)]] | alt | 89.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.79× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 51.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.840 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAS7]] | +0.58 | +0.39 / +0.45 | both halves | 6e-05 |  |
| [[MSLN]] | +0.53 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[KLK6]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[KLK7]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 | pathway: Degradation of the extracellular matrix |
| [[AZGP1]] | +0.51 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[SPINT2]] | +0.51 | +0.31 / +0.59 | both halves | 2e-04 |  |
| [[CELSR2]] | +0.50 | +0.42 / +0.29 | both halves | 2e-04 |  |
| [[LRP2]] | +0.50 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[SOD3]] | +0.50 | +0.34 / +0.35 | both halves | 1e-04 |  |
| [[ZNF536]] | +0.50 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[SNX32]] | +0.50 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[GJB1]] | +0.49 | +0.58 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC4]] | -0.44 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[ZMYM1]] | -0.43 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[BLOC1S5]] | -0.43 | -0.32 / -0.29 | both halves | 2e-04 |  |
| [[ABRAXAS2]] | -0.41 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[NUP37]] | -0.41 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[KATNBL1]] | -0.40 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[TATDN1]] | -0.40 | -0.34 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGFBP2]] | B | IGFBP2 activity raises COL9A3's level | lines that do not express IGFBP2 (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without IGFBP2 | 0.099 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |
| [[NTRK2]] | C | NTRK2 activity raises COL9A3's level | lines that do not express NTRK2 (28) vs lines expressing it (22) | 2.27× lower at baseline in the lines without NTRK2 | 0.016 | ⚠ within organs, on part of the lines; also absent: ANKRD20A9P, ONECUT3, LINC00408; maybe low, not absent; co-absent with the target |
| [[GJB1]] | C | GJB1 activity raises COL9A3's level | lines that do not express GJB1 (38) vs lines expressing it (12) | 5.15× lower at baseline in the lines without GJB1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: AZGP1, LYZ, ATP10B; co-absent with the target |
| [[ESPN]] | C | ESPN activity raises COL9A3's level | lines that do not express ESPN (26) vs lines expressing it (24) | 2.99× lower at baseline in the lines without ESPN | 0.057 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3; co-absent with the target |
| [[AZGP1]] | C | AZGP1 activity raises COL9A3's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 3.45× lower at baseline in the lines without AZGP1 | 0.091 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |
| [[TF]] | C | TF activity raises COL9A3's level | lines that do not express TF (41) vs lines expressing it (9) | 2.80× lower at baseline in the lines without TF | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: A2M, TYR, LHFPL3-AS1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTYH3]] | B | COL9A3 activity raises TTYH3's level | lines that do not express COL9A3 (28) vs lines expressing it (22) | 1.41× lower at baseline in the lines without COL9A3 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000259639, AK4P3, LINC01169 |
| [[PCSK9]] | B | COL9A3 activity lowers PCSK9's level | lines that do not express COL9A3 (28) vs lines expressing it (22) | 1.46× higher at baseline in the lines without COL9A3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000259639, AK4P3, LINC01169 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.338). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.7, 60.1); signed map (67.5, 4.7). **Vector** length 31.0, 5.49% of its response variance represented; |z| ≥ 3 in 365 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.0 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.9 | +1.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.9 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | collagen type IX alpha 3 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,816,244-62,841,159 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IDD, MED, EDM3, FLJ90759, DJ885L7.4.1 |
| Gene groups (HGNC) | Collagen proteoglycans; Fibril associated collagens with interrupted triple helices |
| Reactome | 15 pathways, smallest: NCAM1 interactions; Collagen chain trimerization; Collagen degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14050](https://www.uniprot.org/uniprotkb/Q14050) (Collagen alpha-3(IX) chain):

> Structural component of hyaline cartilage and vitreous of the eye.

**Summary**, from NCBI Gene [1299](https://www.ncbi.nlm.nih.gov/gene/1299):

> This gene encodes one of the three alpha chains of type IX collagen, the major collagen component of hyaline cartilage. Type IX collagen, a heterotrimeric molecule, is usually found in tissues containing type II collagen, a fibrillar collagen. Mutations in this gene are associated with multiple epiphyseal dysplasia type 3. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:2219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2219) · Entrez [1299](https://www.ncbi.nlm.nih.gov/gene/1299) · UniProt [Q14050](https://www.uniprot.org/uniprotkb/Q14050) · Ensembl [ENSG00000092758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092758)

## Data

Gene col 1706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1706); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1706]; `tensor/DDL_lfc|DDL_z.npy` [1706]; `embed/gene_vectors.npy` [1706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1706 or target_col == 1706). Every well: [[COL9A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL9A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "BEX4"
type: "gene"
col: 2247
ensembl_id: "ENSG00000102409"
name: "brain expressed X-linked 4"
location: "Xq22.1"
module: 74
arm: "+"
pooled_cpm: 2.58
n_lines_expressing: 28
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# BEX4

*brain expressed X-linked 4* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.21× (z +9.9, q 2e-20, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.89× (z +7.6, q 7e-12, up in 15 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.464× (z -5.6, q 1e-05, down in 16 of 25 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (SW 900 0.0719×); [[Ranolazine (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0618×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BEX2]] (+0.79, fdr 7e-06), [[UBE2B]] (+0.63, fdr 1e-05), [[PGPEP1]] (+0.62, fdr 3e-05); moves opposite to [[ARMC8]] (-0.53, fdr 6e-05), [[TTF2]] (-0.53, fdr 1e-04), [[GSTCD]] (-0.52, fdr 9e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SGSM1]] → it (grade B ⚠); 2 go from it, the strongest it → [[INSR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2247.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.21×** | +9.9 | 2e-20 | 1/6 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.89×** | +7.6 | 7e-12 | 15/21 (A498, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.07×** | +7.3 | 4e-11 | 14/24 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **2.02×** | +7.1 | 2e-10 | 13/24 (A498, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +6.4 | 2e-08 | 2/7 (J82, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +5.5 | 5e-06 | 3/11 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.8 | 2e-04 | 6/18 (J82, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.5 | 5e-04 | 7/16 (NCI-H2030, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +4.3 | 0.001 | 12/21 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.77×** | +4.1 | 0.003 | 4/11 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.012 | 3/20 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.05×** | +3.7 | 0.012 | 1/8 (SK-MEL-2) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.6 | 0.016 | 2/17 (SW480, A498) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.98×** | +3.5 | 0.020 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.059 | 11/24 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.85×** | +3.1 | 0.059 | 1/14 (CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.059 | 2/15 (NCI-H2347, SK-MEL-2) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +3.1 | 0.060 | 10/24 (PANC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.067 | 1/15 (SW 900) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2247.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (SW 900 0.0719×); [[Ranolazine (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0618×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.464×** | -5.6 | 1e-05 | 16/25 (A498, NCI-H2030, …) | all doses, flat |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.723× | -3.4 | 0.20 | 4/26 (H4, CFPAC-1, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.660× | -3.0 | 0.43 | 7/24 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2247. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 3.32 | 0 | 1 | — | [[Ranolazine (drug)]] 0.05 µM 0.0618× (z -9.5) |
| [[SW 900 (line)]] | alt | 9.78 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0719× (z -11.2) |
| [[A-172 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.176 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.245 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.850 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.249 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.226 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.219 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.706 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.812 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.188 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.757 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.250 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2247), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEX2]] | +0.79 | +0.73 / +0.80 | both halves | 7e-06 | same gene group; STRING 551 |
| [[UBE2B]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[PGPEP1]] | +0.62 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[YPEL3]] | +0.62 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[MOSPD1]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[CCNDBP1]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ABHD8]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[HDAC5]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[DEDD2]] | +0.56 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[KLC3]] | +0.56 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[C7orf57]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ATP6V0D2]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC8]] | -0.53 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[TTF2]] | -0.53 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[GSTCD]] | -0.52 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[GEN1]] | -0.52 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[XRCC5]] | -0.52 | -0.37 / -0.54 | both halves | 7e-05 |  |
| [[ZRANB3]] | -0.52 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SRFBP1]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[PRKDC]] | -0.52 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[CPSF3]] | -0.52 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CTPS1]] | -0.50 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[CSE1L]] | -0.49 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[UTP4]] | -0.49 | -0.39 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGSM1]] | B | SGSM1 activity raises BEX4's level | lines that do not express SGSM1 (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without SGSM1 | 0.094 | ⚠ within organs, on part of the lines; also absent: DANT2, KCNIP3, PIK3C2B; maybe low, not absent |
| [[BEX2]] | C | BEX2 activity raises BEX4's level | lines that do not express BEX2 (18) vs lines expressing it (32) | 2.97× lower at baseline in the lines without BEX2 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, BEX4, PAPLN; co-absent with the target |
| [[ATP6V0D2]] | C | ATP6V0D2 activity raises BEX4's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 2.70× lower at baseline in the lines without ATP6V0D2 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent; co-absent with the target |
| [[CRTAC1]] | C | CRTAC1 activity raises BEX4's level | lines that do not express CRTAC1 (27) vs lines expressing it (23) | 2.41× lower at baseline in the lines without CRTAC1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ITGB3, ADAMTS9-AS2, CRLF2; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INSR]] | B | BEX4 activity lowers INSR's level | lines that do not express BEX4 (22) vs lines expressing it (28) | 1.80× higher at baseline in the lines without BEX4 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, ZNF229, BEX2 |
| [[BEX2]] | C | BEX4 activity raises BEX2's level | lines that do not express BEX4 (22) vs lines expressing it (28) | 2.88× lower at baseline in the lines without BEX4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, ZNF229, BEX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.463). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.7, -48.1); signed map (-20.0, 13.8). **Vector** length 39.0, 7.15% of its response variance represented; |z| ≥ 3 in 509 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +4.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +9.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -5.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | brain expressed X-linked 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:103,215,108-103,217,246 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10097; previously BEXL1 |
| Gene groups (HGNC) | Brain expressed X-linked family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWD9](https://www.uniprot.org/uniprotkb/Q9NWD9) (Protein BEX4):

> May play a role in microtubule deacetylation by negatively regulating the SIRT2 deacetylase activity toward alpha-tubulin and thereby participate in the control of cell cycle progression and genomic stability. In absence of reductive stress, acts as a pseudosubstrate for the CRL2(FEM1B) complex: associates with FEM1B via zinc, thereby preventing association between FEM1B and its substrates (By similarity).

**Summary**, from NCBI Gene [56271](https://www.ncbi.nlm.nih.gov/gene/56271):

> This gene is a member of the brain expressed X-linked gene family. The proteins encoded by some of the other members of this family act as transcription elongation factors which allow RNA polymerase II to escape pausing during elongation. Multiple alternatively spliced variants, encoding the same protein, have been identified. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:25475](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25475) · Entrez [56271](https://www.ncbi.nlm.nih.gov/gene/56271) · UniProt [Q9NWD9](https://www.uniprot.org/uniprotkb/Q9NWD9) · Ensembl [ENSG00000102409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102409)

## Data

Gene col 2247: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2247); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2247, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2247]; `tensor/DDL_lfc|DDL_z.npy` [2247]; `embed/gene_vectors.npy` [2247]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2247 or target_col == 2247). Every well: [[BEX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BEX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ARNT2-DT"
type: "gene"
col: 15205
ensembl_id: "ENSG00000259495"
name: "ARNT2 divergent transcript"
location: "15q25.1"
module: 87
arm: "+"
pooled_cpm: 2.3
n_lines_expressing: 23
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# ARNT2-DT

*ARNT2 divergent transcript* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.54× (z +19.3, q 0e+00, up in 13 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.0687×, SW480 0.115×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (C-33 A 0.0951×, C32 0.0725×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 5 µM in 1 line (SK-MEL-2 0.103×; ⚠ cell-cycle shift, explains ~0% of this change); [[Rosiglitazone (drug)]] 5 µM in 1 line (LoVo 0.0788×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARNT2]] (+0.73, fdr 7e-06, ⚠ same locus), [[CD96]] (+0.72, fdr 1e-05), [[MAGI2-AS3]] (+0.65, fdr 3e-05), [[RMEL3]] (+0.63, fdr 1e-05); moves opposite to [[ANKRD27]] (-0.57, fdr 6e-04), [[CLTCL1]] (-0.56, fdr 3e-04), [[PCMT1]] (-0.54, fdr 0.003, ⚠ one half only (not replicated)), [[PPP1R12B]] (-0.53, fdr 2e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 9 go from it, the strongest it → [[TMSB15B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15205.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.54×** | +19.3 | 0e+00 | 13/14 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.53×** | +13.0 | 6e-36 | 8/14 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.05×** | +11.3 | 2e-27 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.26×** | +8.6 | 1e-15 | 3/9 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.06×** | +8.2 | 2e-14 | 1/4 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.86×** | +6.4 | 2e-08 | 7/19 (A-172, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +6.3 | 3e-08 | 7/11 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +6.2 | 3e-08 | 10/16 (SW 900, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.82×** | +6.2 | 5e-08 | 4/19 (A549, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +5.2 | 1e-05 | 3/11 (A-172, A549, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.55×** | +4.9 | 6e-05 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.99×** | +4.8 | 7e-05 | 9/18 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +4.7 | 1e-04 | 7/16 (PANC-1, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.43×** | +4.6 | 2e-04 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +4.6 | 2e-04 | 3/12 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.13×** | +3.9 | 0.003 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.007 | 4/19 (PANC-1, NCI-H1792, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +3.7 | 0.007 | 4/17 (HOP62, HCT15, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +3.6 | 0.008 | 5/19 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Orlistat (drug)]] 0.05 µM |  | **1.82×** | +3.5 | 0.011 | 0/11 | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.0687×, SW480 0.115×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (C-33 A 0.0951×, C32 0.0725×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 5 µM in 1 line (SK-MEL-2 0.103×; ⚠ cell-cycle shift, explains ~0% of this change); [[Rosiglitazone (drug)]] 5 µM in 1 line (LoVo 0.0788×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 36.9 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0687× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.11 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +12.2) | — |
| [[LoVo (line)]] | wt | 3.68 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.28× (z +8.8) | [[Rosiglitazone (drug)]] 5 µM 0.0788× (z -9.1) |
| [[A549 (line)]] | wt | 8.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.07× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0951× (z -8.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.44 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0725× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 2.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 1.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 4.83 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0412× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 4.67 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.794 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.661 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.835 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.286 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 9 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARNT2]] | +0.73 | +0.68 / +0.63 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[CD96]] | +0.72 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MAGI2-AS3]] | +0.65 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[RMEL3]] | +0.63 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[C1QTNF1-AS1]] | +0.63 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[ANKRD18B]] | +0.62 | +0.48 / +0.30 | both halves | 2e-04 |  |
| [[LPXN]] | +0.62 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[FRG1-DT]] | +0.62 | +0.52 / +0.46 | both halves | 3e-05 | same gene group |
| [[LEF1-AS1]] | +0.62 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[LINC00491]] | +0.61 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[GRIA4]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[NPAS3]] | +0.60 | +0.59 / +0.29 | both halves | 3e-04 |  |
| [[MAP3K7CL]] | +0.60 | +0.60 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | -0.57 | -0.53 / -0.22 | both halves | 6e-04 |  |
| [[CLTCL1]] | -0.56 | -0.41 / -0.29 | both halves | 3e-04 |  |
| [[PCMT1]] | -0.54 | -0.51 / -0.08 | ⚠ one half (not replicated) | 0.003 |  |
| [[PPP1R12B]] | -0.53 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[PHKA2]] | -0.53 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[LCMT1]] | -0.52 | -0.48 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARNT2-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.7% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[LINC01358]] | B | LINC01358 activity raises ARNT2-DT's level | lines that do not express LINC01358 (14) vs lines expressing it (36) | 1.50× lower at baseline in the lines without LINC01358 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, BMPER, FRMD4A; maybe low, not absent |
| [[ARNT2]] | C | ARNT2 activity raises ARNT2-DT's level | lines that do not express ARNT2 (22) vs lines expressing it (28) | 2.50× lower at baseline in the lines without ARNT2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ARNT2-DT, NRN1, LINC02015; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMSB15B]] | B | ARNT2-DT activity raises TMSB15B's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 1.46× lower at baseline in the lines without ARNT2-DT | 0.073 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491 |
| [[LCMT1]] | B | ARNT2-DT activity raises LCMT1's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 1.23× lower at baseline in the lines without ARNT2-DT | 0.075 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491 |
| [[SLCO5A1]] | B | ARNT2-DT activity raises SLCO5A1's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without ARNT2-DT | 0.076 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491 |
| [[C1QTNF1]] | B | ARNT2-DT activity raises C1QTNF1's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 2.60× lower at baseline in the lines without ARNT2-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491 |
| [[DPY19L2P2-1]] | B | ARNT2-DT activity raises DPY19L2P2-1's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 1.60× lower at baseline in the lines without ARNT2-DT | 0.089 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491 |
| [[ARNT2]] | C | ARNT2-DT activity raises ARNT2's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 6.95× lower at baseline in the lines without ARNT2-DT | 1e-05 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491; co-absent with the target |
| [[LEF1]] | C | ARNT2-DT activity raises LEF1's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 2.99× lower at baseline in the lines without ARNT2-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491; co-absent with the target |
| [[L3MBTL4]] | C | ARNT2-DT activity raises L3MBTL4's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 3.00× lower at baseline in the lines without ARNT2-DT | 0.039 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491; co-absent with the target |
| [[ARHGAP25]] | C | ARNT2-DT activity raises ARHGAP25's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 1.47× lower at baseline in the lines without ARNT2-DT | 0.088 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.2, 30.5); signed map (30.2, 37.7). **Vector** length 44.1, 10.4% of its response variance represented; |z| ≥ 3 in 499 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +19.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.0 | -0.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ARNT2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q25.1 — chr15:80,344,853-80,404,214 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56077) · Entrez [101929560](https://www.ncbi.nlm.nih.gov/gene/101929560) · Ensembl [ENSG00000259495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259495)

## Data

Gene col 15205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15205); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15205]; `tensor/DDL_lfc|DDL_z.npy` [15205]; `embed/gene_vectors.npy` [15205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15205 or target_col == 15205). Every well: [[ARNT2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARNT2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

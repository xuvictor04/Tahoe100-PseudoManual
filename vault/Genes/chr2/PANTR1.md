---
symbol: "PANTR1"
type: "gene"
col: 13916
ensembl_id: "ENSG00000233639"
name: "POU3F3 adjacent non-coding transcript 1"
location: "2q12.1"
module: 87
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 13
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# PANTR1

*POU3F3 adjacent non-coding transcript 1* — 2q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.86× (z +19.5, q 0e+00, up in 4 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LOX-IMVI 0.0634×, NCI-H2030 0.175×, C32 0.0997×, HEC-1-A 0.341×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.0721×, LOX-IMVI 0.112×); [[Panobinostat (drug)]] 5 µM in 1 line (HEC-1-A 0.157×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (C32 0.0946×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEF1-AS1]] (+0.56, fdr 2e-05), [[POU3F3]] (+0.55, fdr 1e-05, ⚠ same locus), [[CTTNBP2]] (+0.55, fdr 3e-05), [[GHR]] (+0.55, fdr 1e-05); moves opposite to [[MKNK1]] (-0.43, fdr 7e-04), [[DYNC1LI2]] (-0.38, fdr 2e-04), [[ARAF]] (-0.38, fdr 1e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[TMEM266]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.86×** | +19.5 | 0e+00 | 4/9 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.86×** | +12.4 | 5e-33 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.67×** | +9.0 | 4e-17 | 1/4 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.02×** | +8.8 | 2e-16 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +6.4 | 1e-08 | 4/11 (LoVo, SW480, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.56×** | +5.7 | 9e-07 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.22×** | +5.1 | 3e-05 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +4.8 | 1e-04 | 0/10 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +4.7 | 2e-04 | 1/6 (A498) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.7 | 2e-04 | 2/11 (LoVo, AN3 CA) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +4.5 | 3e-04 | 0/10 | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +4.0 | 0.003 | 3/9 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.15×** | +3.8 | 0.006 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.80×** | +3.7 | 0.008 | 1/10 (AN3 CA) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.22×** | +3.6 | 0.012 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.72×** | +3.4 | 0.022 | 0/10 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +3.4 | 0.026 | 1/10 (SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.033 | 0/11 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.66×** | +3.2 | 0.039 | 1/10 (C32) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.048 | 0/9 | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.048 | 2/10 (SW480, LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.93×** | +3.0 | 0.068 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.60×** | +3.0 | 0.068 | 0/11 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13916.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LOX-IMVI 0.0634×, NCI-H2030 0.175×, C32 0.0997×, HEC-1-A 0.341×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.0721×, LOX-IMVI 0.112×); [[Panobinostat (drug)]] 5 µM in 1 line (HEC-1-A 0.157×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (C32 0.0946×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.581× | -3.2 | 0.58 | 1/11 (SW480) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.599× | -3.1 | 0.58 | 2/11 (AN3 CA, H4) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.341× (z -8.9) |
| [[C32 (line)]] | wt | 7.30 | 0 | 4 | — | [[Selinexor (drug)]] 5 µM 0.0946× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 6.50 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0634× (z -15.7) |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0721× (z -12.4) |
| [[A498 (line)]] | wt | 6.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.67× (z +13.0) | — |
| [[A-172 (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.239 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.226 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.187 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.216 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.220 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.192 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.282 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.340 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.226 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.806 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEF1-AS1]] | +0.56 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[POU3F3]] | +0.55 | +0.66 / +0.57 | both halves | 1e-05 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[CTTNBP2]] | +0.55 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[GHR]] | +0.55 | +0.55 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[NLGN1]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CD96]] | +0.54 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[PI15]] | +0.52 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[LRRK2]] | +0.52 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[A2M]] | +0.52 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[LRIG3-DT]] | +0.52 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[PTPRD]] | +0.51 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[CHST9]] | +0.51 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[LEF1]] | +0.51 | +0.36 / +0.49 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKNK1]] | -0.43 | -0.21 / -0.41 | both halves | 7e-04 |  |
| [[DYNC1LI2]] | -0.38 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[ARAF]] | -0.38 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[TPCN2]] | -0.38 | -0.31 / -0.29 | both halves | 2e-04 |  |
| [[GRIPAP1]] | -0.37 | -0.24 / -0.40 | both halves | 4e-04 |  |
| [[STAM2]] | -0.37 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[TRAK2]] | -0.37 | -0.19 / -0.40 | ⚠ not reproduced | 8e-04 |  |
| [[C18orf32]] | -0.36 | -0.30 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PANTR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[POU3F3]] | C | POU3F3 activity raises PANTR1's level | lines that do not express POU3F3 (34) vs lines expressing it (16) | 3.53× lower at baseline in the lines without POU3F3 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PANTR1, EPGN, ENSG00000244468; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM266]] | B | PANTR1 activity raises TMEM266's level | lines that do not express PANTR1 (37) vs lines expressing it (13) | 1.35× lower at baseline in the lines without PANTR1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: POU3F3, LINC01508, TIMD4 |
| [[CACNB4]] | B | PANTR1 activity raises CACNB4's level | lines that do not express PANTR1 (37) vs lines expressing it (13) | 1.92× lower at baseline in the lines without PANTR1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: POU3F3, LINC01508, TIMD4 |
| [[NEGR1]] | B | PANTR1 activity raises NEGR1's level | lines that do not express PANTR1 (37) vs lines expressing it (13) | 1.76× lower at baseline in the lines without PANTR1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: POU3F3, LINC01508, TIMD4 |
| [[POU3F3]] | C | PANTR1 activity raises POU3F3's level | lines that do not express PANTR1 (37) vs lines expressing it (13) | 5.87× lower at baseline in the lines without PANTR1 | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: POU3F3, LINC01508, TIMD4; co-absent with the target |
| [[PAX3]] | C | PANTR1 activity raises PAX3's level | lines that do not express PANTR1 (37) vs lines expressing it (13) | 2.93× lower at baseline in the lines without PANTR1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: POU3F3, LINC01508, TIMD4; co-absent with the target |
| [[GHR]] | C | PANTR1 activity raises GHR's level | lines that do not express PANTR1 (37) vs lines expressing it (13) | 3.36× lower at baseline in the lines without PANTR1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: POU3F3, LINC01508, TIMD4; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (51.6, 30.3); signed map (31.0, 38.6). **Vector** length 34.3, 9.64% of its response variance represented; |z| ≥ 3 in 299 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +19.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +12.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | +1.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.7 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.7 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.6 | +3.0 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | +0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -0.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.7 | -1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.6 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.6 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | POU3F3 adjacent non-coding transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q12.1 — chr2:104,764,932-104,853,183 (-) |
| Ensembl biotype | lncRNA |
| Also known as | linc-Brn1a, linc-POU3F3; previously LINC01114, LINC01158 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49513) · Entrez [100506421](https://www.ncbi.nlm.nih.gov/gene/100506421) · Ensembl [ENSG00000233639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233639)

## Data

Gene col 13916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13916); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13916]; `tensor/DDL_lfc|DDL_z.npy` [13916]; `embed/gene_vectors.npy` [13916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13916 or target_col == 13916). Every well: [[PANTR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PANTR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

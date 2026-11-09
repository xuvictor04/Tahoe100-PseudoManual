---
symbol: "SOD3"
type: "gene"
col: 3065
ensembl_id: "ENSG00000109610"
name: "superoxide dismutase 3"
location: "4p15.2"
module: 44
arm: "+"
pooled_cpm: 2.23
n_lines_expressing: 16
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# SOD3

*superoxide dismutase 3* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 10.4× (z +11.4, q 2e-27, up in 6 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.34× (z +5.8, q 5e-07, up in 5 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Rutin (trihydrate) (drug)]] 0.05 µM: 0.397× (z -4.2, q 0.014, down in 1 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.234×, LoVo 0.128×; ⚠ cell-cycle shift, would explain all of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (LoVo 0.0724×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSLN]] (+0.67, fdr 1e-05), [[CTSH]] (+0.61, fdr 1e-05), [[SUMF2]] (+0.60, fdr 3e-05); moves opposite to [[PPID]] (-0.52, fdr 5e-05), [[PTER]] (-0.51, fdr 9e-05), [[NSRP1]] (-0.49, fdr 4e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PLA2G4A]] → it (grade C ⚠); 6 go from it, the strongest it → [[MTIF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **10.4×** | +11.4 | 2e-27 | 6/6 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **11.3×** | +11.4 | 2e-27 | 5/5 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **8.81×** | +9.8 | 2e-20 | 4/5 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.32×** | +5.8 | 5e-07 | 3/5 (LS 180, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +5.8 | 5e-07 | 5/12 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.47×** | +5.8 | 5e-07 | 3/7 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **2.20×** | +5.4 | 5e-06 | 0/14 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.89×** | +4.7 | 2e-04 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.60×** | +4.7 | 2e-04 | 0/8 | top dose only |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.48×** | +4.4 | 6e-04 | 1/9 (hTERT-HPNE) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.56×** | +4.4 | 6e-04 | 1/7 (LoVo) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +4.3 | 1e-03 | 0/8 | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **2.42×** | +4.1 | 0.002 | 0/8 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.46×** | +3.8 | 0.006 | 2/5 (NCI-H2347, LoVo) | top dose only | noisy plate (z scaled) |
| [[Vortioxetine (drug)]] 5 µM | ⚠ toxic | **1.98×** | +3.3 | 0.032 | 0/9 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.60×** | +3.3 | 0.032 | 4/7 (LoVo, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **2.08×** | +3.3 | 0.033 | 1/7 (A-172) | inconsistent across doses | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.92×** | +3.2 | 0.048 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.99×** | +3.1 | 0.060 | 1/7 (LS 180) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +3.0 | 0.078 | 1/10 (HEC-1-A) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3065.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LS 180 0.234×, LoVo 0.128×; ⚠ cell-cycle shift, would explain all of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (LoVo 0.0724×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.397×** | -4.2 | 0.014 | 1/14 (RPMI-7951) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.481× | -3.4 | 0.23 | 0/13 | inconsistent across doses | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.535× | -3.1 | 0.27 | 2/14 (RPMI-7951, HOP62) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.511× | -3.1 | 0.27 | 1/12 (LoVo) | inconsistent across doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.515× | -3.0 | 0.27 | 0/14 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 3.04 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -9.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0724× (z -8.5) |
| [[LS 180 (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.116 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.163 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.0959 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.940 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.164 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.349 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.157 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.173 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.660 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.142 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.122 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.160 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.132 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.148 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.116 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.150 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.237 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.139 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.155 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.177 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.274 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.128 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSLN]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[CTSH]] | +0.61 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SUMF2]] | +0.60 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[CD74]] | +0.56 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[CTSF]] | +0.56 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[AZGP1]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[PIGR]] | +0.55 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[REG4]] | +0.55 | +0.67 / +0.29 | both halves | 2e-04 |  |
| [[ECM1]] | +0.54 | +0.61 / +0.29 | both halves | 2e-04 |  |
| [[ZNF710-AS1]] | +0.53 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[FUCA1]] | +0.52 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PIGS]] | +0.52 | +0.59 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPID]] | -0.52 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[PTER]] | -0.51 | -0.51 / -0.37 | both halves | 9e-05 |  |
| [[NSRP1]] | -0.49 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[UBXN4]] | -0.46 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[FCF1]] | -0.46 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[MTIF2]] | -0.45 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[MPHOSPH6]] | -0.45 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[MRPL58]] | -0.44 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[GTF2H3]] | -0.44 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[ZRANB2]] | -0.43 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[THAP5]] | -0.42 | -0.44 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLA2G4A]] | C | PLA2G4A activity raises SOD3's level | lines that do not express PLA2G4A (22) vs lines expressing it (28) | 1.72× lower at baseline in the lines without PLA2G4A | 0.041 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3; co-absent with the target |
| [[PIGR]] | C | PIGR activity raises SOD3's level | lines that do not express PIGR (45) vs lines expressing it (5) | 3.27× lower at baseline in the lines without PIGR | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[HLA-DRA]] | C | HLA-DRA activity raises SOD3's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 2.44× lower at baseline in the lines without HLA-DRA | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530; co-absent with the target |
| [[MUC6]] | C | MUC6 activity raises SOD3's level | lines that do not express MUC6 (45) vs lines expressing it (5) | 2.26× lower at baseline in the lines without MUC6 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230975, APOB; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTIF2]] | B | SOD3 activity lowers MTIF2's level | lines that do not express SOD3 (34) vs lines expressing it (16) | 1.30× higher at baseline in the lines without SOD3 | 0.033 | ⚠ within organs, on part of the lines; also absent: PIGR, PHGR1, KRT20 |
| [[CD46]] | B | SOD3 activity raises CD46's level | lines that do not express SOD3 (34) vs lines expressing it (16) | 1.40× lower at baseline in the lines without SOD3 | 0.035 | ⚠ within organs, on part of the lines; also absent: PIGR, PHGR1, KRT20 |
| [[CREB3L1]] | C | SOD3 activity raises CREB3L1's level | lines that do not express SOD3 (34) vs lines expressing it (16) | 3.24× lower at baseline in the lines without SOD3 | 0.049 | ⚠ within organs, on part of the lines; also absent: PIGR, PHGR1, KRT20; co-absent with the target |
| [[CD74]] | C | SOD3 activity raises CD74's level | lines that do not express SOD3 (34) vs lines expressing it (16) | 2.37× lower at baseline in the lines without SOD3 | 0.056 | ⚠ within organs, on part of the lines; also absent: PIGR, PHGR1, KRT20; co-absent with the target |
| [[AMBP]] | C | SOD3 activity raises AMBP's level | lines that do not express SOD3 (34) vs lines expressing it (16) | 1.12× lower at baseline in the lines without SOD3 | 0.058 | ⚠ within organs, on part of the lines; also absent: PIGR, PHGR1, KRT20; co-absent with the target |
| [[PIGR]] | C | SOD3 activity raises PIGR's level | lines that do not express SOD3 (34) vs lines expressing it (16) | 2.32× lower at baseline in the lines without SOD3 | 0.072 | ⚠ within organs, on part of the lines; also absent: PIGR, PHGR1, KRT20; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.424). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.1, 57.3); signed map (60.9, -5.8). **Vector** length 19.0, 3.23% of its response variance represented; |z| ≥ 3 in 238 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.5 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -0.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.6 | +0.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.5 | -0.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.5 | -0.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | superoxide dismutase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:24,789,912-24,800,842 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EC-SOD |
| Gene groups (HGNC) | Superoxide dismutases |
| Hallmark sets | MYOGENESIS |
| Reactome | 7 pathways, smallest: NFE2L2 regulating anti-oxidant/detoxification enzymes; Detoxification of Reactive Oxygen Species; Nuclear events mediated by NFE2L2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P08294](https://www.uniprot.org/uniprotkb/P08294) (Extracellular superoxide dismutase):

> Secreted antioxidant enzyme that acts as the primary scavenger of superoxide radicals in the extracellular space, converting them to hydrogen peroxide and thereby protecting tissues from oxidative damage. Also preserves nitric oxide bioavailability by preventing the formation of harmful peroxynitrite. Stored in intracellular pre-formed vesicles of macrophages and neutrophils and released upon stimulation by inflammatory mediators.

**Summary**, from NCBI Gene [6649](https://www.ncbi.nlm.nih.gov/gene/6649):

> This gene encodes a member of the superoxide dismutase (SOD) protein family. SODs are antioxidant enzymes that catalyze the conversion of superoxide radicals into hydrogen peroxide and oxygen, which may protect the brain, lungs, and other tissues from oxidative stress. Proteolytic processing of the encoded protein results in the formation of two distinct homotetramers that differ in their ability to interact with the extracellular matrix (ECM). Homotetramers consisting of the intact protein, or …

**Accessions** — [HGNC:11181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11181) · Entrez [6649](https://www.ncbi.nlm.nih.gov/gene/6649) · UniProt [P08294](https://www.uniprot.org/uniprotkb/P08294) · Ensembl [ENSG00000109610](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109610)

## Data

Gene col 3065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3065); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3065]; `tensor/DDL_lfc|DDL_z.npy` [3065]; `embed/gene_vectors.npy` [3065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3065 or target_col == 3065). Every well: [[SOD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

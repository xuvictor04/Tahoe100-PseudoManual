---
symbol: "BNC1"
type: "gene"
col: 9821
ensembl_id: "ENSG00000169594"
name: "basonuclin zinc finger protein 1"
location: "15q25.2"
module: 13
arm: "+"
pooled_cpm: 2.3
n_lines_expressing: 14
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# BNC1

*basonuclin zinc finger protein 1* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.63× (z +12.3, q 5e-32, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.11× (z +6.6, q 4e-09, up in 0 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.212×; ⚠ cell-cycle shift, explains ~15% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (RPMI-7951 0.0956×; ⚠ cell-cycle shift, explains ~45% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.392×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLRP3]] (+0.67, fdr 7e-06), [[RFTN1]] (+0.64, fdr 1e-05), [[ETS1]] (+0.63, fdr 1e-05); moves opposite to [[ABHD16A]] (-0.51, fdr 3e-05), [[TXNDC16]] (-0.46, fdr 9e-05), [[PSME1]] (-0.46, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[VEPH1]] → it (grade C ⚠); 6 go from it, the strongest it → [[LINC00941]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.63×** | +12.3 | 5e-32 | 1/4 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.27×** | +11.6 | 2e-28 | 1/4 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.03×** | +8.2 | 5e-14 | 1/4 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +6.6 | 4e-09 | 0/7 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.14×** | +6.4 | 2e-08 | 0/3 | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.49×** | +5.7 | 9e-07 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.41×** | +5.5 | 2e-06 | 0/7 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +5.2 | 2e-05 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +5.0 | 3e-05 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.31×** | +4.8 | 9e-05 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.002 | 0/11 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.93×** | +4.1 | 0.002 | 0/6 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.85×** | +3.9 | 0.005 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.12×** | +3.7 | 0.007 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.25×** | +3.6 | 0.010 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.78×** | +3.6 | 0.010 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.71×** | +3.4 | 0.024 | 0/6 | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.027 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.66×** | +3.2 | 0.040 | 3/10 (SW 900, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.040 | 4/10 (SW 900, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +3.0 | 0.057 | 3/10 (HEC-1-A, SW 900, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.96×** | +3.0 | 0.058 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | **1.65×** | +3.0 | 0.058 | 0/7 | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +3.0 | 0.060 | 0/8 | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.58×** | +2.9 | 0.086 | 1/6 (HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9821.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.212×; ⚠ cell-cycle shift, explains ~15% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (RPMI-7951 0.0956×; ⚠ cell-cycle shift, explains ~45% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.392×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.603× | -3.2 | 0.41 | 0/10 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.535× | -3.2 | 0.41 | 0/10 | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 40.0 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0956× (z -10.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.9) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H23 (line)]] | alt | 3.43 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.392× (z -8.7) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.178 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.181 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.976 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.204 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.218 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.199 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.173 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.188 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.162 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.571 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.221 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.176 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.194 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.204 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.803 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.184 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLRP3]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[RFTN1]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ETS1]] | +0.63 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[FGF5]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[RGMB]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ADAM12]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RPSAP52]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[VEPH1]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ARHGAP22]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[WNT5B]] | +0.56 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[EVC]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[DSCAM]] | +0.55 | +0.58 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABHD16A]] | -0.51 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[TXNDC16]] | -0.46 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[PSME1]] | -0.46 | -0.33 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VEPH1]] | C | VEPH1 activity raises BNC1's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without VEPH1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC; co-absent with the target |
| [[ROBO4]] | C | ROBO4 activity raises BNC1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.06× lower at baseline in the lines without ROBO4 | 0.044 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |
| [[ADTRP]] | C | ADTRP activity raises BNC1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without ADTRP | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00941]] | B | BNC1 activity raises LINC00941's level | lines that do not express BNC1 (36) vs lines expressing it (14) | 2.15× lower at baseline in the lines without BNC1 | 0.045 | ⚠ within organs, on part of the lines; also absent: SIM1, AJAP1, ENSG00000254337 |
| [[ETS1]] | B | BNC1 activity raises ETS1's level | lines that do not express BNC1 (36) vs lines expressing it (14) | 2.72× lower at baseline in the lines without BNC1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SIM1, AJAP1, ENSG00000254337 |
| [[ROBO4]] | C | BNC1 activity raises ROBO4's level | lines that do not express BNC1 (36) vs lines expressing it (14) | 2.58× lower at baseline in the lines without BNC1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SIM1, AJAP1, ENSG00000254337; co-absent with the target |
| [[ADTRP]] | C | BNC1 activity raises ADTRP's level | lines that do not express BNC1 (36) vs lines expressing it (14) | 2.72× lower at baseline in the lines without BNC1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SIM1, AJAP1, ENSG00000254337; co-absent with the target |
| [[VEPH1]] | C | BNC1 activity raises VEPH1's level | lines that do not express BNC1 (36) vs lines expressing it (14) | 2.62× lower at baseline in the lines without BNC1 | 0.052 | ⚠ within organs, on part of the lines; also absent: SIM1, AJAP1, ENSG00000254337; co-absent with the target |
| [[NLRP3]] | C | BNC1 activity raises NLRP3's level | lines that do not express BNC1 (36) vs lines expressing it (14) | 2.74× lower at baseline in the lines without BNC1 | 0.099 | ⚠ within organs, on part of the lines; also absent: SIM1, AJAP1, ENSG00000254337; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.3, 13.9); signed map (17.8, 46.1). **Vector** length 26.5, 7.23% of its response variance represented; |z| ≥ 3 in 255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.2 | +6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.9 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.6 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.6 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.5 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.5 | -1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | basonuclin zinc finger protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:83,255,884-83,284,664 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HsT19447, bn1, BSN1; previously BNC |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Basonuclin zinc finger proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01954](https://www.uniprot.org/uniprotkb/Q01954) (Zinc finger protein basonuclin-1):

> Transcriptional activator (By similarity). It is likely involved in the regulation of keratinocytes terminal differentiation in squamous epithelia and hair follicles. Required for the maintenance of spermatogenesis (By similarity). It is involved in the positive regulation of oocyte maturation, probably acting through the control of BMP15 levels and regulation of AKT signaling cascade. May also play a role in the early development of embryos (By similarity).

**Summary**, from NCBI Gene [646](https://www.ncbi.nlm.nih.gov/gene/646):

> This gene encodes a zinc finger protein present in the basal cell layer of the epidermis and in hair follicles. It is also found in abundance in the germ cells of testis and ovary. This protein is thought to play a regulatory role in keratinocyte proliferation and it may also be a regulator for rRNA transcription. Disruption of this gene has been implicated in premature ovarian failure as well as testicular premature aging. [provided by RefSeq, Sep 2020]

**Accessions** — [HGNC:1081](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1081) · Entrez [646](https://www.ncbi.nlm.nih.gov/gene/646) · UniProt [Q01954](https://www.uniprot.org/uniprotkb/Q01954) · Ensembl [ENSG00000169594](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169594)

## Data

Gene col 9821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9821); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9821]; `tensor/DDL_lfc|DDL_z.npy` [9821]; `embed/gene_vectors.npy` [9821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9821 or target_col == 9821). Every well: [[BNC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BNC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "SIPA1"
type: "gene"
col: 13104
ensembl_id: "ENSG00000213445"
name: "signal-induced proliferation-associated 1"
location: "11q13.1"
module: 23
arm: "-"
pooled_cpm: 7.01
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 17
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SIPA1

*signal-induced proliferation-associated 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.73× (z +13.1, q 2e-36, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.475× (z -13.8, q 2e-40, down in 29 of 42 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PITPNM1]] (+0.64, fdr 1e-05), [[PEDS1]] (+0.63, fdr 1e-05), [[EHD4]] (+0.63, fdr 2e-05); moves opposite to [[HEXIM2-AS1]] (-0.66, fdr 2e-04), [[OXA1L-DT]] (-0.64, fdr 1e-04), [[TSTD3]] (-0.63, fdr 1e-04).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.73×** | +13.1 | 2e-36 | 41/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.59×** | +12.4 | 5e-33 | 37/47 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.25×** | +10.6 | 4e-24 | 33/47 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +6.0 | 3e-07 | 17/47 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +6.0 | 3e-07 | 14/46 (A498, A-172, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +5.2 | 2e-05 | 14/45 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.2 | 0.002 | 12/36 (AsPC-1, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.011 | 6/41 (SW48, LS 180, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.021 | 4/45 (CFPAC-1, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.034 | 11/39 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.1 | 0.098 | 0/18 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.475×** | -13.8 | 2e-40 | 29/42 (SW 900, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.379×** | -12.7 | 2e-34 | 33/38 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.384×** | -12.5 | 1e-33 | 31/40 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.451×** | -10.4 | 3e-23 | 33/47 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.466×** | -9.6 | 9e-20 | 27/43 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.527×** | -8.4 | 5e-15 | 32/45 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.564×** | -7.5 | 5e-12 | 27/44 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.648×** | -5.5 | 3e-06 | 19/45 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.779×** | -4.6 | 2e-04 | 20/45 (CFPAC-1, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.704×** | -4.6 | 2e-04 | 16/44 (A-427, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -4.6 | 2e-04 | 16/42 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.720×** | -4.1 | 0.002 | 13/31 (SK-MEL-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.757×** | -3.6 | 0.012 | 14/45 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -3.5 | 0.022 | 11/40 (SK-MEL-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.773×** | -3.4 | 0.028 | 2/45 (HT-29, A498) | top dose only | position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | 0.839× | -3.2 | 0.042 | 10/45 (C32, BT-474, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -3.1 | 0.068 | 13/37 (PANC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.199× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 17.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -9.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 5.85 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 9.01 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.1) |
| [[A-427 (line)]] | wt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -11.2) |
| [[A549 (line)]] | wt | 5.57 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0727× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 6.83 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0662× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 8.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 3.12 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0951× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -9.9) |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -11.4) |
| [[A-172 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNM1]] | +0.64 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.63 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[EHD4]] | +0.63 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[FCHO1]] | +0.62 | +0.48 / +0.37 | both halves | 9e-05 |  |
| [[GPRIN1]] | +0.62 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[ST6GALNAC4]] | +0.61 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[LPCAT1]] | +0.61 | +0.48 / +0.48 | both halves | 2e-05 | same gene group |
| [[CADM4]] | +0.61 | +0.38 / +0.42 | both halves | 6e-05 |  |
| [[TWF2]] | +0.60 | +0.56 / +0.29 | both halves | 2e-04 |  |
| [[USP35]] | +0.60 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[KCTD17]] | +0.60 | +0.47 / +0.30 | both halves | 2e-04 |  |
| [[LRFN3]] | +0.60 | +0.54 / +0.29 | both halves | 3e-04 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEXIM2-AS1]] | -0.66 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[OXA1L-DT]] | -0.64 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[TSTD3]] | -0.63 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[WAC-AS1]] | -0.63 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[TRMT13]] | -0.63 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ITPA]] | -0.63 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[DNAI4]] | -0.62 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[MFF-DT]] | -0.62 | -0.50 / -0.23 | both halves | 5e-04 |  |
| [[CCAR1]] | -0.61 | -0.52 / -0.43 | both halves | 3e-05 | same gene group |
| [[UBXN2A]] | -0.61 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[TCEAL4]] | -0.61 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[TMEM192]] | -0.61 | -0.59 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SIPA1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TCIRG1]] | B | TCIRG1 activity lowers SIPA1's level | lines that do not express TCIRG1 (5) vs lines expressing it (45) | 1.15× higher at baseline in the lines without TCIRG1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000255031, SUSD1, MGST2; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SIPA1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SIPA1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (0.4, 13.3); signed map (-27.8, 19.9). **Vector** length 76.1, 13.2% of its response variance represented; |z| ≥ 3 in 1,094 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +12.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +13.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +10.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +6.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -12.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -13.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -9.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | signal-induced proliferation-associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,638,101-65,650,918 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPA1 |
| Gene groups (HGNC) | PDZ domain containing; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Rap1 signalling; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FS4](https://www.uniprot.org/uniprotkb/Q96FS4) (Signal-induced proliferation-associated protein 1):

> GTPase activator for the nuclear Ras-related regulatory proteins Rap1 and Rap2 in vitro, converting them to the putatively inactive GDP-bound state. Affects cell cycle progression (By similarity).

**Summary**, from NCBI Gene [6494](https://www.ncbi.nlm.nih.gov/gene/6494):

> The product of this gene is a mitogen induced GTPase activating protein (GAP). It exhibits a specific GAP activity for Ras-related regulatory proteins Rap1 and Rap2, but not for Ran or other small GTPases. This protein may also hamper mitogen-induced cell cycle progression when abnormally or prematurely expressed. It is localized to the perinuclear region. Two alternatively spliced variants encoding the same isoform have been characterized to date. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10885) · Entrez [6494](https://www.ncbi.nlm.nih.gov/gene/6494) · UniProt [Q96FS4](https://www.uniprot.org/uniprotkb/Q96FS4) · Ensembl [ENSG00000213445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213445)

## Data

Gene col 13104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13104); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13104]; `tensor/DDL_lfc|DDL_z.npy` [13104]; `embed/gene_vectors.npy` [13104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13104 or target_col == 13104). Every well: [[SIPA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIPA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

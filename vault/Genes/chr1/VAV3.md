---
symbol: "VAV3"
type: "gene"
col: 5523
ensembl_id: "ENSG00000134215"
name: "vav guanine nucleotide exchange factor 3"
location: "1p13.3"
module: 9
arm: "+"
pooled_cpm: 13.97
n_lines_expressing: 20
n_dd_up: 33
n_dd_down: 2
n_dd_up_clean: 27
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# VAV3

*vav guanine nucleotide exchange factor 3* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.03× (z +18.6, q 0e+00, up in 16 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.636× (z -5.4, q 4e-05, down in 12 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (BT-474 0.225×, NCI-H2030 0.261×, NCI-H1573 0.313×); [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H23 0.256×, NCI-H1573 0.114×, H4 0.0691×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H1573 0.173×, NCI-H2030 0.174×, NCI-H23 0.361×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.175×, NCI-H2030 0.229×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGAT4C]] (+0.66, fdr 1e-05), [[PDGFD]] (+0.64, fdr 7e-06), [[ERBB4]] (+0.63, fdr 1e-05); moves opposite to [[CRYGS]] (-0.45, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ANO5]] → it (grade B ⚠); 7 go from it, the strongest it → [[CYP39A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5523.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.03×** | +18.6 | 0e+00 | 16/18 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.72×** | +15.6 | 0e+00 | 4/14 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +13.8 | 8e-41 | 6/17 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.08×** | +13.4 | 1e-38 | 4/16 (LOX-IMVI, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +12.1 | 2e-31 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.75×** | +12.0 | 3e-31 | 12/18 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.46×** | +10.7 | 8e-25 | 16/18 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.27×** | +9.7 | 2e-20 | 12/18 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.12×** | +8.9 | 3e-17 | 11/16 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +8.0 | 8e-14 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +7.4 | 8e-12 | 10/17 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +6.5 | 4e-09 | 8/17 (LS 180, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.55×** | +4.9 | 4e-05 | 9/18 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.16×** | +4.8 | 7e-05 | 10/17 (BT-474, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +4.7 | 1e-04 | 11/16 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 2e-04 | 3/17 (LS 180, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +4.4 | 4e-04 | 1/17 (LOX-IMVI) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.44×** | +4.1 | 0.001 | 5/17 (LS 180, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5523.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (BT-474 0.225×, NCI-H2030 0.261×, NCI-H1573 0.313×); [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H23 0.256×, NCI-H1573 0.114×, H4 0.0691×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H1573 0.173×, NCI-H2030 0.174×, NCI-H23 0.361×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 0.175×, NCI-H2030 0.229×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.636×** | -5.4 | 4e-05 | 12/18 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.720×** | -3.9 | 0.026 | 9/16 (NCI-H1573, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | 0.740× | -3.4 | 0.14 | 3/17 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.765× | -3.2 | 0.21 | 9/16 (C-33 A, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Abiraterone acetate (drug)]] 0.5 µM |  | 0.769× | -3.1 | 0.21 | 1/17 (RPMI-7951) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5523. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 90.4 | 1 | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.00× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0814× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -9.0) |
| [[LS 180 (line)]] | wt | 41.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.51× (z +11.4) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Trametinib (drug)]] 5 µM 4.08× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.258× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 69.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -13.7) |
| [[BT-474 (line)]] | alt | 261 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -13.3) |
| [[H4 (line)]] | wt | 27.3 | 0 | 4 (2 ⚠) | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0403× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 56.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 4.80 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 5.32× (z +10.0) | [[Digitoxin (drug)]] 0.05 µM 0.123× (z -8.9) |
| [[C-33 A (line)]] | alt | 8.28 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0659× (z -8.9) |
| [[A-172 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.63 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5523), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAT4C]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[PDGFD]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ERBB4]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 | same gene group; STRING 426 |
| [[LGSN]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[SLITRK6]] | +0.62 | +0.48 / +0.46 | both halves | 3e-05 | **novel candidate** |
| [[CTNNA2]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[LINC02484]] | +0.60 | +0.64 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[MID1]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[FSTL5]] | +0.60 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[GABRA2]] | +0.58 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[ANO5]] | +0.58 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[CDH10]] | +0.57 | +0.51 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYGS]] | -0.45 | -0.35 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO5]] | B | ANO5 activity raises VAV3's level | lines that do not express ANO5 (25) vs lines expressing it (25) | 2.49× lower at baseline in the lines without ANO5 | 0.087 | ⚠ within organs, on part of the lines; also absent: CNKSR2, SLC6A15, CNTN1; maybe low, not absent |
| [[NRXN3]] | C | NRXN3 activity raises VAV3's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.77× lower at baseline in the lines without NRXN3 | 0.065 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |
| [[SLITRK6]] | C | SLITRK6 activity raises VAV3's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 2.61× lower at baseline in the lines without SLITRK6 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; co-absent with the target |
| [[KLHL13]] | C | KLHL13 activity raises VAV3's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.56× lower at baseline in the lines without KLHL13 | 0.084 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |
| [[UPK1B]] | C | UPK1B activity raises VAV3's level | lines that do not express UPK1B (39) vs lines expressing it (11) | 2.12× lower at baseline in the lines without UPK1B | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CES1, CGA, SLC15A5; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP39A1]] | B | VAV3 activity raises CYP39A1's level | lines that do not express VAV3 (30) vs lines expressing it (20) | 1.78× lower at baseline in the lines without VAV3 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM |
| [[MAP7]] | B | VAV3 activity raises MAP7's level | lines that do not express VAV3 (30) vs lines expressing it (20) | 1.28× lower at baseline in the lines without VAV3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM |
| cells under [[AZD1390 (drug)]] 5 µM | B | VAV3 activity lowers the cells' numbers under AZD1390 5 µM (makes them more sensitive) | lines that do not express VAV3 (30) vs lines expressing it (18) | the lines without VAV3: 1.19× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM |
| cells under [[Encorafenib (drug)]] 5 µM | B | VAV3 activity raises the cells' numbers under Encorafenib 5 µM (protects the cells) | lines that do not express VAV3 (30) vs lines expressing it (18) | the lines without VAV3: 0.84× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM |
| cells under [[XRK3F2 (drug)]] 5 µM | B | VAV3 activity raises the cells' numbers under XRK3F2 5 µM (protects the cells) | lines that do not express VAV3 (30) vs lines expressing it (18) | the lines without VAV3: 0.84× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM |
| [[PPARGC1A]] | C | VAV3 activity raises PPARGC1A's level | lines that do not express VAV3 (30) vs lines expressing it (20) | 1.85× lower at baseline in the lines without VAV3 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM; co-absent with the target |
| [[SFMBT2]] | C | VAV3 activity raises SFMBT2's level | lines that do not express VAV3 (30) vs lines expressing it (20) | 4.33× lower at baseline in the lines without VAV3 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.0, 35.3); signed map (39.7, 35.9). **Vector** length 50.5, 11.9% of its response variance represented; |z| ≥ 3 in 576 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +13.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +4.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | vav guanine nucleotide exchange factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:107,571,161-107,965,180 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; SH2 domain containing; MicroRNA protein coding host genes; SH3 domain containing |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 41 pathways, smallest: Azathioprine ADME; DAP12 signaling; FCERI mediated Ca+2 mobilization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKW4](https://www.uniprot.org/uniprotkb/Q9UKW4) (Guanine nucleotide exchange factor VAV3):

> Exchange factor for GTP-binding proteins RhoA, RhoG and, to a lesser extent, Rac1. Binds physically to the nucleotide-free states of those GTPases. Plays an important role in angiogenesis. Its recruitment by phosphorylated EPHA2 is critical for EFNA1-induced RAC1 GTPase activation and vascular endothelial cell migration and assembly (By similarity). May be important for integrin-mediated signaling, at least in some cell types. In osteoclasts, along with SYK tyrosine kinase, required for …

**Summary**, from NCBI Gene [10451](https://www.ncbi.nlm.nih.gov/gene/10451):

> This gene is a member of the VAV gene family. The VAV proteins are guanine nucleotide exchange factors (GEFs) for Rho family GTPases that activate pathways leading to actin cytoskeletal rearrangements and transcriptional alterations. This gene product acts as a GEF preferentially for RhoG, RhoA, and to a lesser extent, RAC1, and it associates maximally with the nucleotide-free states of these GTPases. Alternatively spliced transcript variants encoding different isoforms have been described for …

**Accessions** — [HGNC:12659](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12659) · Entrez [10451](https://www.ncbi.nlm.nih.gov/gene/10451) · UniProt [Q9UKW4](https://www.uniprot.org/uniprotkb/Q9UKW4) · Ensembl [ENSG00000134215](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134215)

## Data

Gene col 5523: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5523); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5523, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5523]; `tensor/DDL_lfc|DDL_z.npy` [5523]; `embed/gene_vectors.npy` [5523]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5523 or target_col == 5523). Every well: [[VAV3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAV3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

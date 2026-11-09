---
symbol: "SPP1"
type: "gene"
col: 4018
ensembl_id: "ENSG00000118785"
name: "secreted phosphoprotein 1"
location: "4q22.1"
module: 19
arm: "+"
pooled_cpm: 44.66
n_lines_expressing: 15
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 9
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SPP1

*secreted phosphoprotein 1* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.83× (z +15.1, q 0e+00, up in 12 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +6.5, q 1e-08, up in 7 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.0169×, NCI-H460 0.125×, CFPAC-1 0.0534×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (SHP-77 0.0540×, CFPAC-1 0.0431×, NCI-H460 0.222×); [[Harringtonine (drug)]] 5 µM in 1 line (SHP-77 0.154×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAK3]] (+0.57, fdr 1e-05), [[PCDH9]] (+0.56, fdr 3e-05), [[BCHE]] (+0.54, fdr 2e-05); moves opposite to [[RNF135]] (-0.43, fdr 6e-05), [[HSF2BP]] (-0.43, fdr 2e-04), [[RAB11FIP3]] (-0.43, fdr 8e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[AKR1C3]] → it (grade B ⚠); 9 go from it, the strongest it → [[AKR1C3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.83×** | +15.1 | 0e+00 | 12/13 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.58×** | +14.3 | 8e-44 | 11/12 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.31×** | +9.9 | 8e-21 | 11/12 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.5 | 1e-08 | 7/14 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.03×** | +5.2 | 2e-05 | 4/13 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +4.3 | 0.002 | 4/14 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.006 | 6/13 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.47×** | +3.5 | 0.038 | 4/9 (HEC-1-A, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | 1.54× | +3.0 | 0.14 | 9/13 (NCI-H1792, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | 1.51× | +3.0 | 0.14 | 1/13 (HepG2/C3A) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4018.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.0169×, NCI-H460 0.125×, CFPAC-1 0.0534×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (SHP-77 0.0540×, CFPAC-1 0.0431×, NCI-H460 0.222×); [[Harringtonine (drug)]] 5 µM in 1 line (SHP-77 0.154×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.637× | -3.3 | 0.52 | 0/13 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.659× | -3.1 | 0.61 | 3/13 (HepG2/C3A, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 12.6 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 9.98× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 118 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0169× (z -29.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0540× (z -15.1) |
| [[A549 (line)]] | wt | 14.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.9× (z +10.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 33.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0534× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0431× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 85.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.50× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 30.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.1× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 249 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -8.9) |
| [[A498 (line)]] | wt | 422 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 4.51 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.21 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.84 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.73 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.70 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.03 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAK3]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PCDH9]] | +0.56 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[BCHE]] | +0.54 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[ADGRV1]] | +0.54 | +0.24 / +0.52 | both halves | 4e-04 |  |
| [[MAP2K6]] | +0.53 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[NCKAP5]] | +0.53 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[SNTG1]] | +0.53 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ESRRG]] | +0.53 | +0.38 / +0.42 | both halves | 7e-05 |  |
| [[PALMD]] | +0.52 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[PBX1]] | +0.51 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[CPE]] | +0.51 | +0.45 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[AKR1C2]] | +0.51 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF135]] | -0.43 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[HSF2BP]] | -0.43 | -0.39 / -0.30 | both halves | 2e-04 |  |
| [[RAB11FIP3]] | -0.43 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[RNF166]] | -0.42 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[ZBTB8A]] | -0.41 | -0.44 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C3]] | B | AKR1C3 activity raises SPP1's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.22× lower at baseline in the lines without AKR1C3 | 0.091 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[GPRIN3]] | C | GPRIN3 activity raises SPP1's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 4.02× lower at baseline in the lines without GPRIN3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises SPP1's level | lines that do not express BCHE (35) vs lines expressing it (15) | 3.02× lower at baseline in the lines without BCHE | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[WDR72]] | C | WDR72 activity raises SPP1's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 1.70× lower at baseline in the lines without WDR72 | 0.063 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2; co-absent with the target |
| [[AKR1C2]] | C | AKR1C2 activity raises SPP1's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 4.10× lower at baseline in the lines without AKR1C2 | 0.091 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C3]] | B | SPP1 activity raises AKR1C3's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 3.16× lower at baseline in the lines without SPP1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG |
| [[WDR72]] | C | SPP1 activity raises WDR72's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 2.63× lower at baseline in the lines without SPP1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |
| [[AKR1B10]] | C | SPP1 activity raises AKR1B10's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 2.70× lower at baseline in the lines without SPP1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |
| [[GPRIN3]] | C | SPP1 activity raises GPRIN3's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 3.54× lower at baseline in the lines without SPP1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |
| [[NCKAP5]] | C | SPP1 activity raises NCKAP5's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 3.12× lower at baseline in the lines without SPP1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |
| [[PALMD]] | C | SPP1 activity raises PALMD's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 2.02× lower at baseline in the lines without SPP1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |
| [[PDGFD]] | C | SPP1 activity raises PDGFD's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 2.18× lower at baseline in the lines without SPP1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |
| [[TCN1]] | C | SPP1 activity raises TCN1's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 1.40× lower at baseline in the lines without SPP1 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |
| [[TSPAN7]] | C | SPP1 activity raises TSPAN7's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 2.32× lower at baseline in the lines without SPP1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.454). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.2, 37.4); signed map (43.7, 37.4). **Vector** length 44.4, 14.6% of its response variance represented; |z| ≥ 3 in 290 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | -1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | secreted phosphoprotein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:87,975,667-87,983,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BSPI, ETA-1, lnc-PKD2-2-3; previously BNSP, OPN |
| Gene groups (HGNC) | Receptor ligands; SIBLING family |
| Hallmark sets | ANGIOGENESIS, KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 12 pathways, smallest: RUNX3 Regulates Immune Response and Cell Migration; Mechanical load activates signaling by PIEZO1 and integrins in osteocytes; Signaling by PDGF |
| Matched by | ensembl_id |

**Function**, from UniProt [P10451](https://www.uniprot.org/uniprotkb/P10451) (Osteopontin):

> Major non-collagenous bone protein that binds tightly to hydroxyapatite. Appears to form an integral part of the mineralized matrix. Probably important to cell-matrix interaction.; Acts as a cytokine involved in enhancing production of interferon-gamma and interleukin-12 and reducing production of interleukin-10 and is essential in the pathway that leads to type I immunity.

**Summary**, from NCBI Gene [6696](https://www.ncbi.nlm.nih.gov/gene/6696):

> The protein encoded by this gene is involved in the attachment of osteoclasts to the mineralized bone matrix. The encoded protein is secreted and binds hydroxyapatite with high affinity. The osteoclast vitronectin receptor is found in the cell membrane and may be involved in the binding to this protein. This protein is also a cytokine that upregulates expression of interferon-gamma and interleukin-12. Several transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:11255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11255) · Entrez [6696](https://www.ncbi.nlm.nih.gov/gene/6696) · UniProt [P10451](https://www.uniprot.org/uniprotkb/P10451) · Ensembl [ENSG00000118785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118785)

## Data

Gene col 4018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4018); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4018]; `tensor/DDL_lfc|DDL_z.npy` [4018]; `embed/gene_vectors.npy` [4018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4018 or target_col == 4018). Every well: [[SPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "EFEMP2"
type: "gene"
col: 10276
ensembl_id: "ENSG00000172638"
name: "EGF-like fibulin extracellular matrix protein 2"
location: "11q13.1"
module: 136
arm: "+"
pooled_cpm: 10.25
n_lines_expressing: 44
n_dd_up: 5
n_dd_down: 31
n_dd_up_clean: 5
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# EFEMP2

*EGF-like fibulin extracellular matrix protein 2* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Gallic acid (hydrate) (drug)]] 0.5 µM: 1.59× (z +4.5, q 0.003, up in 14 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.245× (z -13.6, q 2e-39, down in 38 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APBB3]] (+0.64, fdr 1e-05), [[SH3D21]] (+0.63, fdr 1e-05), [[EPOR]] (+0.62, fdr 7e-06); moves opposite to [[HNF4G]] (-0.60, fdr 2e-05), [[QRSL1]] (-0.56, fdr 2e-05), [[GATC]] (-0.53, fdr 6e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF404]] → it (grade B ⚠); 2 go from it, the strongest it → [[LRP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10276.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.59×** | +4.5 | 0.003 | 14/40 (hTERT-HPNE, COLO 205, …) | two highest doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.017 | 19/41 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.017 | 14/41 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +3.6 | 0.049 | 12/35 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.051 | 15/37 (NCI-H2030, SNU-423, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10276.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.245×** | -13.6 | 2e-39 | 38/42 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.293×** | -11.9 | 5e-30 | 35/41 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.294×** | -11.4 | 8e-28 | 26/30 (NCI-H1792, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.321×** | -11.0 | 7e-26 | 33/36 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.327×** | -10.4 | 3e-23 | 32/41 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.343×** | -10.4 | 4e-23 | 33/40 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.369×** | -9.6 | 4e-20 | 34/41 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.410×** | -8.6 | 5e-16 | 30/41 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.466×** | -7.4 | 1e-11 | 24/37 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.496×** | -6.8 | 7e-10 | 27/41 (RPMI-7951, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.517×** | -6.4 | 1e-08 | 26/42 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.835× | -6.2 | 2e-08 | 26/42 (A549, SW 1271, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.547×** | -5.8 | 3e-07 | 23/42 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.539×** | -5.6 | 7e-07 | 25/41 (CFPAC-1, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.565×** | -5.5 | 1e-06 | 21/39 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.639×** | -4.3 | 5e-04 | 13/42 (C32, NCI-H2030, …) | top dose only | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.441×** | -4.1 | 0.001 | 11/35 (PANC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.462×** | -3.9 | 0.003 | 14/41 (BT-474, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 17.6 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0290× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0351× (z -15.2) |
| [[PANC-1 (line)]] | alt | 23.9 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -12.5) |
| [[J82 (line)]] | alt | 10.4 | 0 | 5 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0740× (z -12.2) |
| [[SNU-423 (line)]] | alt | 8.31 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0286× (z -14.0) |
| [[C32 (line)]] | wt | 14.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0412× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0503× (z -11.6) |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.145× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 8.87 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0647× (z -10.3) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.0934× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 8.45 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0390× (z -12.9) |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0354× (z -13.6) |
| [[H4 (line)]] | wt | 11.8 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0470× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0700× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 9.94 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0750× (z -11.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -10.3) |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0507× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.119× (z -9.8) |
| [[A-172 (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 9.04 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0800× (z -9.9) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 4.73 | 0 | 1 | — | [[Lopinavir (drug)]] 0.05 µM 0.0546× (z -9.8) |
| [[BT-474 (line)]] | alt | 5.97 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0410× (z -9.5) |
| [[Hs 766T (line)]] | wt | 29.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.169× (z -9.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.187× (z -8.7) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 4.52 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -8.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 7.49 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0414× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APBB3]] | +0.64 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[SH3D21]] | +0.63 | +0.51 / +0.73 | both halves | 1e-05 |  |
| [[EPOR]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SIDT2]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[EHBP1L1]] | +0.60 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[CPNE5]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ABCA7]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[FSCN1]] | +0.56 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[PC]] | +0.56 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[ACAP3]] | +0.56 | +0.59 / +0.35 | both halves | 1e-04 |  |
| [[TNNT1]] | +0.56 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[LOXL2]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF4G]] | -0.60 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[QRSL1]] | -0.56 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[GATC]] | -0.53 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[SLC25A13]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PHACTR2]] | -0.49 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[NSMAF]] | -0.48 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[SPR]] | -0.48 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[RNASEH2B]] | -0.47 | -0.49 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF404]] | B | ZNF404 activity raises EFEMP2's level | lines that do not express ZNF404 (14) vs lines expressing it (36) | 2.56× lower at baseline in the lines without ZNF404 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: MIR130AHG, RAB34, PYGO1 |
| [[CACNG7]] | B | CACNG7 activity raises EFEMP2's level | lines that do not express CACNG7 (21) vs lines expressing it (29) | 1.82× lower at baseline in the lines without CACNG7 | 0.048 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[BRSK1]] | B | BRSK1 activity raises EFEMP2's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 2.00× lower at baseline in the lines without BRSK1 | 0.065 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP1]] | B | EFEMP2 activity raises LRP1's level | lines that do not express EFEMP2 (6) vs lines expressing it (44) | 2.03× lower at baseline in the lines without EFEMP2 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000198106, ZMIZ1-AS1; maybe low, not absent |
| [[CLDN14-AS1]] | B | EFEMP2 activity raises CLDN14-AS1's level | lines that do not express EFEMP2 (6) vs lines expressing it (44) | 3.35× lower at baseline in the lines without EFEMP2 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000198106, ZMIZ1-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.0, -2.1); signed map (-24.1, 25.6). **Vector** length 81.5, 16.7% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.7 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.1 | -3.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | -0.1 |
|  | [[Pimitespib (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.4 | +3.5 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.4 | +1.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.5 | -10.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.2 | -11.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | -11.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -11.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.4 | -5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -6.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -8.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | EGF-like fibulin extracellular matrix protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,866,441-65,873,592 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBLN4, UPH1 |
| Gene groups (HGNC) | Fibulins |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 3 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O95967](https://www.uniprot.org/uniprotkb/O95967) (EGF-containing fibulin-like extracellular matrix protein 2):

> Plays a crucial role in elastic fiber formation in tissue, and in the formation of ultrastructural connections between elastic laminae and smooth muscle cells in the aorta, therefore participates in terminal differentiation and maturation of smooth muscle cell (SMC) and in the mechanical properties and wall integrity maintenance of the aorta. In addition, is involved in the control of collagen fibril assembly in tissue throught proteolytic activation of LOX leading to cross- linking of collagen …

**Summary**, from NCBI Gene [30008](https://www.ncbi.nlm.nih.gov/gene/30008):

> A large number of extracellular matrix proteins have been found to contain variations of the epidermal growth factor (EGF) domain and have been implicated in functions as diverse as blood coagulation, activation of complement and determination of cell fate during development. The protein encoded by this gene contains four EGF2 domains and six calcium-binding EGF2 domains. This gene is necessary for elastic fiber formation and connective tissue development. Defects in this gene are cause of an …

**Accessions** — [HGNC:3219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3219) · Entrez [30008](https://www.ncbi.nlm.nih.gov/gene/30008) · UniProt [O95967](https://www.uniprot.org/uniprotkb/O95967) · Ensembl [ENSG00000172638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172638)

## Data

Gene col 10276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10276); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10276]; `tensor/DDL_lfc|DDL_z.npy` [10276]; `embed/gene_vectors.npy` [10276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10276 or target_col == 10276). Every well: [[EFEMP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFEMP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

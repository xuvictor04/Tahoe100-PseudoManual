---
symbol: "ADGRA3"
type: "gene"
col: 7677
ensembl_id: "ENSG00000152990"
name: "adhesion G protein-coupled receptor A3"
location: "4p15.2"
module: 143
arm: "+"
pooled_cpm: 77.08
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# ADGRA3

*adhesion G protein-coupled receptor A3* — 4p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +7.5, q 3e-11, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.402× (z -12.0, q 1e-30, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ME3]] (+0.67, fdr 1e-05), [[PARD3B]] (+0.67, fdr 7e-06), [[CTPS1]] (+0.65, fdr 7e-06); moves opposite to [[ANG]] (-0.62, fdr 1e-05), [[RIOK3]] (-0.62, fdr 1e-05), [[SRP54]] (-0.61, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PPP1R9A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7677.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +7.5 | 3e-11 | 30/48 (NCI-H2347, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.73×** | +7.2 | 1e-10 | 35/48 (HS-578T, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +5.3 | 2e-05 | 30/48 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +5.2 | 4e-05 | 26/48 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.1 | 4e-05 | 28/47 (HOP62, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.47×** | +5.1 | 4e-05 | 37/47 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.9 | 8e-05 | 28/47 (NCI-H1573, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.049 | 23/48 (NCI-H2347, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.064 | 23/47 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +3.1 | 0.096 | 20/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7677.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.402×** | -12.0 | 1e-30 | 42/48 (SW48, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.451×** | -10.5 | 2e-23 | 38/48 (HT-29, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.536×** | -8.2 | 3e-14 | 32/48 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.610×** | -6.5 | 9e-09 | 36/48 (LoVo, SW48, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.766×** | -5.0 | 7e-05 | 27/48 (SW48, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.737×** | -4.0 | 0.005 | 28/47 (C-33 A, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.765×** | -3.5 | 0.032 | 24/46 (PANC-1, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Artesunate (drug)]] 5 µM |  | **0.832×** | -3.5 | 0.038 | 21/48 (Hs 766T, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.787×** | -3.2 | 0.091 | 25/48 (SW48, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7677. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 140 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -14.5) |
| [[SW48 (line)]] | wt | 264 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -16.4) |
| [[A-427 (line)]] | wt | 97.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -20.5) |
| [[C-33 A (line)]] | alt | 185 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.222× (z -14.0) |
| [[HT-29 (line)]] | alt | 75.9 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.128× (z -18.0) |
| [[A549 (line)]] | wt | 70.0 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -13.7) |
| [[LoVo (line)]] | wt | 112 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 73.2 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.3) | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -13.4) |
| [[PANC-1 (line)]] | alt | 71.2 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -10.2) |
| [[AN3 CA (line)]] | alt | 160 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.242× (z -9.0) |
| [[CHP-212 (line)]] | wt | 100 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 78.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 31.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +15.3) | — |
| [[KATO III (line)]] | alt | 49.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -10.7) |
| [[LS 180 (line)]] | wt | 152 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 52.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 49.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.54× (z +23.8) | — |
| [[NCI-H460 (line)]] | wt | 89.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -12.8) |
| [[SW480 (line)]] | alt | 84.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.221× (z -12.7) |
| [[A498 (line)]] | wt | 82.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.344× (z -9.5) |
| [[H4 (line)]] | wt | 106 | 0 | 2 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.125× (z -10.4) |
| [[HOP62 (line)]] | alt | 62.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.7) | — |
| [[HS-578T (line)]] | alt | 48.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 108 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.28× (z +8.8) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.274× (z -9.3) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 30.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +11.0) | — |
| [[SNU-1 (line)]] | wt | 117 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.359× (z -11.2) |
| [[SNU-423 (line)]] | alt | 86.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -9.9) |
| [[SW1417 (line)]] | alt | 74.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 30.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 89.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +14.9) | — |
| [[HCT15 (line)]] | alt | 74.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.256× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 96.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -9.3) |
| [[J82 (line)]] | alt | 68.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 81.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 71.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 62.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.376× (z -8.8) |
| [[SW 900 (line)]] | alt | 119 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.268× (z -9.9) |
| [[A-172 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 82.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7677), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ME3]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PARD3B]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CTPS1]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[SLC12A2-DT]] | +0.65 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[CACHD1]] | +0.64 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[USP13]] | +0.62 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[BCL2]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SLC39A10]] | +0.61 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[PKP4]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[POGLUT1]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A13]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[PRMT3]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANG]] | -0.62 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[RIOK3]] | -0.62 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[SRP54]] | -0.61 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ACBD3]] | -0.60 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[ZSWIM8]] | -0.58 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[PMM1]] | -0.58 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[RNASE4]] | -0.57 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[GYS1]] | -0.57 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[PLD3]] | -0.57 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[GMPPA]] | -0.57 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[COPA]] | -0.57 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[DHDDS]] | -0.56 | -0.58 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R9A]] | B | PPP1R9A activity raises ADGRA3's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without PPP1R9A | 0.013 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity strengthens ADGRA3's drug response | lines that do not express TMEM92-AS1 (16) vs lines expressing it (32) | the lines without TMEM92-AS1 respond 0.74× as strongly (z diff +1.04); strongest at Homoharringtonine 5 µM: 0.95x vs 1.96x (z diff +5.7) | 0.081 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2; target measured in part of the lines; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises ADGRA3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NUP210]] | B | NUP210 activity raises ADGRA3's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.70× lower at baseline in the lines without NUP210 | 0.091 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.3, 7.1); signed map (24.3, -33.2). **Vector** length 142, 47.0% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.4 | +5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.4 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +7.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.0 | +7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.7 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +3.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.8 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.9 | -6.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -12.0 |
|  | [[Artesunate (drug)]] 5 µM |  | -4.8 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.2 | -8.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -10.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.9 | -1.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.7 | -2.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -3.7 | -2.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -3.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.2 — chr4:22,345,071-22,516,066 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38547, PGR21; previously GPR125 |
| Gene groups (HGNC) | I-set domain containing; Adhesion G protein-coupled receptors, subfamily A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWK6](https://www.uniprot.org/uniprotkb/Q8IWK6) (Adhesion G protein-coupled receptor A3):

> Orphan receptor that may have a role in planar cell polarity pathway.

**Summary**, from NCBI Gene [166647](https://www.ncbi.nlm.nih.gov/gene/166647):

> This gene encodes a member of the G protein-coupled receptor superfamily. This membrane protein may play a role in tumor angiogenesis through its interaction with the human homolog of the Drosophila disc large tumor suppressor gene. This gene is mapped to a candidate region of chromosome 4 which may be associated with bipolar disorder and schizophrenia. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:13839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13839) · Entrez [166647](https://www.ncbi.nlm.nih.gov/gene/166647) · UniProt [Q8IWK6](https://www.uniprot.org/uniprotkb/Q8IWK6) · Ensembl [ENSG00000152990](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152990)

## Data

Gene col 7677: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7677); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7677, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7677]; `tensor/DDL_lfc|DDL_z.npy` [7677]; `embed/gene_vectors.npy` [7677]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7677 or target_col == 7677). Every well: [[ADGRA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

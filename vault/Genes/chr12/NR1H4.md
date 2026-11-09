---
symbol: "NR1H4"
type: "gene"
col: 257
ensembl_id: "ENSG00000012504"
name: "nuclear receptor subfamily 1 group H member 4"
location: "12q23.1"
module: 9
arm: "+"
pooled_cpm: 2.64
n_lines_expressing: 16
n_dd_up: 38
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 13
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# NR1H4

*nuclear receptor subfamily 1 group H member 4* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 23.9× (z +27.4, q 0e+00, up in 8 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00882]] (+0.61, fdr 1e-05), [[SLCO2B1]] (+0.61, fdr 1e-05), [[ANKRD30B]] (+0.61, fdr 2e-05); moves opposite to [[CTNNBIP1]] (-0.54, fdr 3e-05), [[SPATA33]] (-0.51, fdr 8e-05), [[UHRF2]] (-0.51, fdr 2e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 13 go from it, the strongest it → [[RFTN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 257.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **23.9×** | +27.4 | 0e+00 | 8/9 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.83×** | +16.6 | 0e+00 | 6/8 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **8.91×** | +13.4 | 2e-38 | 6/8 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.32×** | +12.1 | 1e-31 | 1/2 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.19×** | +12.1 | 2e-31 | 1/2 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **6.28×** | +11.2 | 3e-27 | 4/7 (SK-MEL-2, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **5.09×** | +9.3 | 1e-18 | 8/10 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.94×** | +9.0 | 1e-17 | 1/2 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.91×** | +6.5 | 4e-09 | 7/12 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.99×** | +5.9 | 2e-07 | 7/11 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.48×** | +5.5 | 2e-06 | 5/12 (SK-MEL-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.48×** | +5.2 | 1e-05 | 1/2 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.39×** | +5.0 | 3e-05 | 3/4 (A498, HepG2/C3A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.7 | 1e-04 | 1/12 (HEC-1-A) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.94×** | +4.7 | 1e-04 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.07×** | +4.4 | 3e-04 | 2/9 (A549, HEC-1-A) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.04×** | +4.4 | 4e-04 | 1/4 (HEC-1-A) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +4.2 | 7e-04 | 6/11 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +4.0 | 0.001 | 4/7 (HepG2/C3A, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.50×** | +4.0 | 0.002 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.551× | -3.4 | 0.42 | 2/9 (HEC-1-A, HT-29) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.25 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 91.2× (z +12.9) | — |
| [[A498 (line)]] | wt | 46.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +12.4) | — |
| [[C32 (line)]] | wt | 0.878 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 74.5× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 1.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 63.8× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 1.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.2× (z +10.8) | — |
| [[A-427 (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.961 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.410 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.794 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.756 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.339 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.369 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.496 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.407 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00882]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SLCO2B1]] | +0.61 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ANKRD30B]] | +0.61 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[KMO]] | +0.59 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[MSR1]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[LINC01320]] | +0.59 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[MIR4300HG]] | +0.58 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[LINC01695]] | +0.58 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[CNTN6]] | +0.57 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TRIML2]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[DISC1FP1]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[LINC02241]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNBIP1]] | -0.54 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[SPATA33]] | -0.51 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[UHRF2]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[ETV5]] | -0.50 | -0.48 / -0.35 | both halves | 1e-04 | pathway: HALLMARK_KRAS_SIGNALING_UP |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NR1H4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00958]] | C | LINC00958 activity raises NR1H4's level | lines that do not express LINC00958 (39) vs lines expressing it (11) | 1.56× lower at baseline in the lines without LINC00958 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SSX1, LINC01320, LINC00879; co-absent with the target |
| [[EIF1AY]] | C | EIF1AY activity raises NR1H4's level | lines that do not express EIF1AY (31) vs lines expressing it (19) | 1.27× lower at baseline in the lines without EIF1AY | 0.084 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 3, C 10. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFTN2]] | B | NR1H4 activity raises RFTN2's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 1.45× lower at baseline in the lines without NR1H4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent |
| [[C12orf50]] | B | NR1H4 activity raises C12orf50's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 1.84× lower at baseline in the lines without NR1H4 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent |
| [[LINC02398]] | B | NR1H4 activity raises LINC02398's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 1.80× lower at baseline in the lines without NR1H4 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent |
| [[PSG4]] | C | NR1H4 activity raises PSG4's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 1.61× lower at baseline in the lines without NR1H4 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[LINC01320]] | C | NR1H4 activity raises LINC01320's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 4.26× lower at baseline in the lines without NR1H4 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[PDZRN3]] | C | NR1H4 activity raises PDZRN3's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 2.53× lower at baseline in the lines without NR1H4 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[EIF1AY]] | C | NR1H4 activity raises EIF1AY's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 2.78× lower at baseline in the lines without NR1H4 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[DCT]] | C | NR1H4 activity raises DCT's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 2.66× lower at baseline in the lines without NR1H4 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[GPNMB]] | C | NR1H4 activity raises GPNMB's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 3.21× lower at baseline in the lines without NR1H4 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[DISC1FP1]] | C | NR1H4 activity raises DISC1FP1's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without NR1H4 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[ANKRD30B]] | C | NR1H4 activity raises ANKRD30B's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 2.13× lower at baseline in the lines without NR1H4 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |
| [[CPED1]] | C | NR1H4 activity raises CPED1's level | lines that do not express NR1H4 (34) vs lines expressing it (16) | 2.45× lower at baseline in the lines without NR1H4 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01320, DCT, S100A1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.504). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.3, 23.4); signed map (39.1, 25.1). **Vector** length 25.0, 5.89% of its response variance represented; |z| ≥ 3 in 294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +27.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +12.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.1 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +16.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +11.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +1.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -0.8 | +4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | +1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.6 | +0.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.6 | -1.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.5 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 1 group H member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:100,473,708-100,564,414 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FXR, RIP14, HRR1, HRR-1 |
| Gene groups (HGNC) | Nuclear receptor subfamily 1 group H |
| Hallmark sets | BILE_ACID_METABOLISM, KRAS_SIGNALING_UP |
| Reactome | 17 pathways, smallest: Synthesis of bile acids and bile salts via 27-hydroxycholesterol; Recycling of bile acids and salts; Endogenous sterols |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RI1](https://www.uniprot.org/uniprotkb/Q96RI1) (Bile acid receptor):

> Ligand-activated transcription factor. Receptor for bile acids (BAs) such as chenodeoxycholic acid (CDCA), lithocholic acid, deoxycholic acid (DCA) and allocholic acid (ACA). Plays a essential role in BA homeostasis through the regulation of genes involved in BA synthesis, conjugation and enterohepatic circulation. Also regulates lipid and glucose homeostasis and is involved innate immune response. The FXR-RXR heterodimer binds predominantly to farnesoid X receptor response elements (FXREs) …

**Summary**, from NCBI Gene [9971](https://www.ncbi.nlm.nih.gov/gene/9971):

> This gene encodes a ligand-activated transcription factor that shares structural features in common with nuclear hormone receptor family members. This protein functions as a receptor for bile acids, and when bound to bile acids, binds to DNA and regulates the expression of genes involved in bile acid synthesis and transport. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:7967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7967) · Entrez [9971](https://www.ncbi.nlm.nih.gov/gene/9971) · UniProt [Q96RI1](https://www.uniprot.org/uniprotkb/Q96RI1) · Ensembl [ENSG00000012504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000012504)

## Data

Gene col 257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 257); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 257]; `tensor/DDL_lfc|DDL_z.npy` [257]; `embed/gene_vectors.npy` [257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 257 or target_col == 257). Every well: [[NR1H4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR1H4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "TLL1"
type: "gene"
col: 452
ensembl_id: "ENSG00000038295"
name: "tolloid like 1"
location: "4q32.3"
module: 9
arm: "+"
pooled_cpm: 3.04
n_lines_expressing: 22
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# TLL1

*tolloid like 1* — 4q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.25× (z +16.2, q 0e+00, up in 9 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Mebendazole (drug)]] 5 µM: 0.622× (z -3.7, q 0.100, down in 4 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.0655×); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 0.0806×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0874×; ⚠ cell-cycle shift, explains ~82% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.217×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPOCK3]] (+0.64, fdr 7e-06), [[ADAMTS3]] (+0.63, fdr 1e-05), [[MAPK10]] (+0.63, fdr 7e-06); moves opposite to [[CTNNBIP1]] (-0.52, fdr 4e-05), [[ZCCHC17]] (-0.51, fdr 5e-05), [[YIPF1]] (-0.51, fdr 8e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PPM1E]] → it (grade B ⚠); 4 go from it, the strongest it → [[SYNPO2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.25×** | +16.2 | 0e+00 | 9/15 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.64×** | +12.2 | 1e-31 | 4/9 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.90×** | +12.1 | 1e-31 | 2/5 (J82, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.90×** | +10.0 | 3e-21 | 3/6 (J82, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.41×** | +9.8 | 8e-21 | 8/16 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +7.9 | 2e-13 | 11/18 (NCI-H2347, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +5.4 | 7e-06 | 2/10 (NCI-H1792, A498) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.96×** | +5.3 | 8e-06 | 7/18 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +5.1 | 2e-05 | 5/16 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.0 | 4e-05 | 3/13 (J82, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +4.5 | 3e-04 | 5/18 (A498, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +4.5 | 3e-04 | 2/15 (J82, HOP62) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +4.5 | 3e-04 | 4/12 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.69×** | +4.1 | 0.001 | 2/17 (NCI-H2347, J82) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +3.8 | 0.006 | 7/15 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.012 | 8/18 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.84×** | +3.4 | 0.018 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +3.0 | 0.060 | 6/15 (A498, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 452.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.0655×); [[Auranofin (drug)]] 5 µM in 1 line (LoVo 0.0806×); [[Panobinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0874×; ⚠ cell-cycle shift, explains ~82% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.217×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | **0.622×** | -3.7 | 0.100 | 4/18 (HS-578T, CHP-212, …) | top dose only |  |
| [[Verapamil (drug)]] 0.05 µM |  | **0.618×** | -3.6 | 0.100 | 1/16 (NCI-H2347) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 27.7 | 0 | 7 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0655× (z -12.0) |
| [[A-427 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0436× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 0.922 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 1.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.1× (z +12.5) | — |
| [[A-172 (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.819 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.715 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.680 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.855 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.571 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.601 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.663 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.801 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.473 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOCK3]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 | pathway: Degradation of the extracellular matrix |
| [[ADAMTS3]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 | pathway: Collagen biosynthesis and modifying enzymes |
| [[MAPK10]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[TSPAN2]] | +0.62 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[LAMA2]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[SOHLH2]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[MARCOL]] | +0.58 | +0.62 / +0.38 | both halves | 7e-05 |  |
| [[ANGPT1]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[LINC00457]] | +0.56 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[LYPD1]] | +0.56 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[RHOU]] | +0.56 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ERG]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNBIP1]] | -0.52 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ZCCHC17]] | -0.51 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[YIPF1]] | -0.51 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[FBH1]] | -0.51 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[RAB43]] | -0.50 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[TANGO2]] | -0.49 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[CARD19]] | -0.49 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[MAP2K1]] | -0.49 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[MYO9B]] | -0.49 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[OGG1]] | -0.49 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[PBX4]] | -0.49 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[ZFYVE21]] | -0.48 | -0.51 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPM1E]] | B | PPM1E activity lowers TLL1's level | lines that do not express PPM1E (16) vs lines expressing it (34) | 1.08× higher at baseline in the lines without PPM1E | 0.067 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, SNRPN; maybe low, not absent |
| [[ANGPT1]] | C | ANGPT1 activity raises TLL1's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.09× lower at baseline in the lines without ANGPT1 | 0.009 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |
| [[GUCY1A1]] | C | GUCY1A1 activity raises TLL1's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 2.41× lower at baseline in the lines without GUCY1A1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046; co-absent with the target |
| [[ERG]] | C | ERG activity raises TLL1's level | lines that do not express ERG (30) vs lines expressing it (20) | 2.08× lower at baseline in the lines without ERG | 0.025 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNPO2]] | B | TLL1 activity raises SYNPO2's level | lines that do not express TLL1 (28) vs lines expressing it (22) | 2.21× lower at baseline in the lines without TLL1 | 0.032 | ⚠ within organs, on part of the lines; also absent: GUCY1A1, CDH6, COL1A1; maybe low, not absent |
| [[DSC3]] | C | TLL1 activity raises DSC3's level | lines that do not express TLL1 (28) vs lines expressing it (22) | 3.04× lower at baseline in the lines without TLL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: GUCY1A1, CDH6, COL1A1; maybe low, not absent; co-absent with the target |
| [[HS6ST2]] | C | TLL1 activity raises HS6ST2's level | lines that do not express TLL1 (28) vs lines expressing it (22) | 3.14× lower at baseline in the lines without TLL1 | 0.022 | ⚠ within organs, on part of the lines; also absent: GUCY1A1, CDH6, COL1A1; maybe low, not absent; co-absent with the target |
| [[TEX15]] | C | TLL1 activity raises TEX15's level | lines that do not express TLL1 (28) vs lines expressing it (22) | 2.34× lower at baseline in the lines without TLL1 | 0.066 | ⚠ within organs, on part of the lines; also absent: GUCY1A1, CDH6, COL1A1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.5, 27.1); signed map (44.8, 27.4). **Vector** length 38.0, 8.57% of its response variance represented; |z| ≥ 3 in 401 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.0 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -1.1 | +1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | tolloid like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.3 — chr4:165,873,237-166,104,457 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Astacins |
| Reactome | 7 pathways, smallest: Anchoring fibril formation; Crosslinking of collagen fibrils; Assembly of collagen fibrils and other multimeric structures |
| Matched by | ensembl_id |

**Function**, from UniProt [O43897](https://www.uniprot.org/uniprotkb/O43897) (Tolloid-like protein 1):

> Protease which processes procollagen C-propeptides, such as chordin, pro-biglycan and pro-lysyl oxidase. Required for the embryonic development. Predominant protease, which in the development, influences dorsal-ventral patterning and skeletogenesis.

**Summary**, from NCBI Gene [7092](https://www.ncbi.nlm.nih.gov/gene/7092):

> This gene encodes an astacin-like, zinc-dependent, metalloprotease that belongs to the peptidase M12A family. This protease processes procollagen C-propeptides, such as chordin, pro-biglycan and pro-lysyl oxidase. Studies in mice suggest that this gene plays multiple roles in the development of mammalian heart, and is essential for the formation of the interventricular septum. Allelic variants of this gene are associated with atrial septal defect type 6. Alternatively spliced transcript …

**Accessions** — [HGNC:11843](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11843) · Entrez [7092](https://www.ncbi.nlm.nih.gov/gene/7092) · UniProt [O43897](https://www.uniprot.org/uniprotkb/O43897) · Ensembl [ENSG00000038295](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000038295)

## Data

Gene col 452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 452); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 452]; `tensor/DDL_lfc|DDL_z.npy` [452]; `embed/gene_vectors.npy` [452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 452 or target_col == 452). Every well: [[TLL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "SLC2A14"
type: "gene"
col: 10363
ensembl_id: "ENSG00000173262"
name: "solute carrier family 2 member 14"
location: "12p13.31"
module: 53
arm: "+"
pooled_cpm: 4.8
n_lines_expressing: 37
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# SLC2A14

*solute carrier family 2 member 14* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.13× (z +14.6, q 1e-45, up in 19 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.659× (z -3.8, q 0.082, down in 12 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.104×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0509×; ⚠ toxic); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HepG2/C3A 0.0957×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.129×); [[Auranofin (drug)]] 5 µM in 1 line (HepG2/C3A 0.155×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TG]] (+0.65, fdr 7e-06), [[DYNLRB2-AS1]] (+0.63, fdr 8e-06), [[AOX1]] (+0.61, fdr 1e-05); moves opposite to [[AP3M2]] (-0.47, fdr 2e-04).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ARHGAP40]] → it (grade B ⚠); 3 go from it, the strongest it → [[SVEP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.13×** | +14.6 | 1e-45 | 19/26 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.89×** | +13.6 | 1e-39 | 18/27 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.31×** | +12.7 | 6e-35 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.85×** | +12.2 | 3e-32 | 22/31 (SW480, H4, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.35×** | +10.9 | 9e-26 | 22/31 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.23×** | +10.6 | 2e-24 | 8/15 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.41×** | +10.3 | 7e-23 | 3/8 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.35×** | +7.7 | 7e-13 | 13/24 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +6.4 | 1e-08 | 13/27 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +5.1 | 2e-05 | 13/32 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.67×** | +4.6 | 2e-04 | 5/7 (SW480, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +4.3 | 8e-04 | 9/31 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.56×** | +4.0 | 0.002 | 7/30 (BT-474, HS-578T, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.34×** | +4.0 | 0.002 | 4/17 (SW480, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.55×** | +4.0 | 0.003 | 1/26 (SW1417) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.016 | 10/26 (SW480, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.45×** | +3.3 | 0.029 | 2/30 (SW480, SW 900) | all doses, stronger at high dose |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.036 | 5/29 (SW 900, RPMI-7951, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.036 | 5/32 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.057 | 10/30 (A498, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10363.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.104×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HepG2/C3A 0.0509×; ⚠ toxic); [[Ixazomib citrate (drug)]] 5 µM in 1 line (HepG2/C3A 0.0957×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.129×); [[Auranofin (drug)]] 5 µM in 1 line (HepG2/C3A 0.155×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.659×** | -3.8 | 0.082 | 12/30 (HepG2/C3A, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.692× | -3.2 | 0.44 | 2/31 (RPMI-7951, HOP62) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | 0.790× | -3.0 | 0.46 | 6/25 (HOP62, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 141 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -19.5) |
| [[A498 (line)]] | wt | 1.77 | 2 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 29.8× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 3.86 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 125× (z +8.6) | — |
| [[C32 (line)]] | wt | 5.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 64.2× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 1.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.0× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 4.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 85.5× (z +20.0) | — |
| [[hTERT-HPNE (line)]] | wt | 6.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.5× (z +9.0) | — |
| [[J82 (line)]] | alt | 2.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 5.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 2.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 7.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +8.6) | — |
| [[SW480 (line)]] | alt | 11.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.51× (z +8.6) | — |
| [[A-172 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.892 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.807 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.849 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TG]] | +0.65 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[DYNLRB2-AS1]] | +0.63 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[AOX1]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[MYO3B]] | +0.60 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[TNFSF14]] | +0.60 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[LINC01170]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[KCNN1]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[PLB1]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[KCNG2]] | +0.57 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[HPN]] | +0.56 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[SPDYA]] | +0.56 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ELAPOR1]] | +0.55 | +0.56 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP3M2]] | -0.47 | -0.53 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP40]] | B | ARHGAP40 activity raises SLC2A14's level | lines that do not express ARHGAP40 (16) vs lines expressing it (34) | 1.58× lower at baseline in the lines without ARHGAP40 | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000282943, ENSG00000225096, ENSG00000239462; maybe low, not absent |
| [[RTN4RL1]] | B | RTN4RL1 activity raises SLC2A14's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 1.91× lower at baseline in the lines without RTN4RL1 | 0.099 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[DYSF]] | C | DYSF activity raises SLC2A14's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without DYSF | 0.052 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SVEP1]] | B | SLC2A14 activity raises SVEP1's level | lines that do not express SLC2A14 (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without SLC2A14 | 0.060 | ⚠ within organs, on part of the lines; also absent: NPAS3, SLC2A3, HEY1; maybe low, not absent |
| [[PDZD2]] | B | SLC2A14 activity raises PDZD2's level | lines that do not express SLC2A14 (13) vs lines expressing it (37) | 2.02× lower at baseline in the lines without SLC2A14 | 0.076 | ⚠ within organs, on part of the lines; also absent: NPAS3, SLC2A3, HEY1; maybe low, not absent |
| [[SYT16]] | B | SLC2A14 activity raises SYT16's level | lines that do not express SLC2A14 (13) vs lines expressing it (37) | 1.87× lower at baseline in the lines without SLC2A14 | 0.089 | ⚠ within organs, on part of the lines; also absent: NPAS3, SLC2A3, HEY1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.6, 21.7); signed map (25.0, 12.6). **Vector** length 61.9, 11.5% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +14.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +12.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +6.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.1 | +1.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.0 | +2.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.0 | +4.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +0.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +0.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -2.0 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -0.9 | -0.0 |
|  | [[Benztropine (mesylate) (drug)]] 0.5 µM |  | -0.9 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 2 member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:7,812,512-7,891,148 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GLUT14; previously SLC2A3P3 |
| Gene groups (HGNC) | Solute carrier family 2 |
| Reactome | 3 pathways, smallest: Cellular hexose transport; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDB8](https://www.uniprot.org/uniprotkb/Q8TDB8) (Solute carrier family 2, facilitated glucose transporter member 14):

> Hexose transporter that can mediate the transport of glucose and dehydroascorbate across the cell membrane.

**Summary**, from NCBI Gene [144195](https://www.ncbi.nlm.nih.gov/gene/144195):

> Members of the glucose transporter (GLUT) family, including SLC2A14, are highly conserved integral membrane proteins that transport hexoses such as glucose and fructose into all mammalian cells. GLUTs show tissue and cell-type specific expression (Wu and Freeze, 2002 [PubMed 12504846]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18301) · Entrez [144195](https://www.ncbi.nlm.nih.gov/gene/144195) · UniProt [Q8TDB8](https://www.uniprot.org/uniprotkb/Q8TDB8) · Ensembl [ENSG00000173262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173262)

## Data

Gene col 10363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10363); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10363]; `tensor/DDL_lfc|DDL_z.npy` [10363]; `embed/gene_vectors.npy` [10363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10363 or target_col == 10363). Every well: [[SLC2A14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC2A14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

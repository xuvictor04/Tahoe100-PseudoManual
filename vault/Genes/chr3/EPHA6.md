---
symbol: "EPHA6"
type: "gene"
col: 1277
ensembl_id: "ENSG00000080224"
name: "EPH receptor A6"
location: "3q11.2"
module: 9
arm: "+"
pooled_cpm: 33.83
n_lines_expressing: 21
n_dd_up: 26
n_dd_down: 13
n_dd_up_clean: 20
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# EPHA6

*EPH receptor A6* — 3q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.50× (z +26.7, q 0e+00, up in 8 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.678× (z -5.8, q 3e-06, down in 10 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD16]] (+0.63, fdr 1e-05), [[NRXN1]] (+0.62, fdr 1e-05), [[ERBB4]] (+0.62, fdr 9e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 3 go from it, the strongest it → [[IKZF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1277.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.50×** | +26.7 | 0e+00 | 8/19 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.34×** | +18.1 | 0e+00 | 15/19 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +11.8 | 7e-30 | 7/19 (SW 900, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +10.1 | 6e-22 | 16/19 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +9.3 | 1e-18 | 5/18 (BT-474, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.72×** | +8.2 | 3e-14 | 7/19 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +7.5 | 5e-12 | 3/18 (LOX-IMVI, BT-474, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.5 | 7e-09 | 5/19 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +6.4 | 8e-09 | 15/19 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.4 | 8e-09 | 3/17 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.54×** | +6.3 | 2e-08 | 18/19 (HEC-1-A, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.3 | 2e-08 | 7/19 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.3 | 6e-04 | 1/17 (A498) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.33×** | +4.3 | 8e-04 | 8/19 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +4.3 | 8e-04 | 11/19 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.002 | 10/19 (HEC-1-A, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.004 | 10/19 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.004 | 0/19 | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.004 | 7/19 (SHP-77, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1277.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -5.8 | 3e-06 | 10/19 (NCI-H1792, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.682×** | -5.7 | 3e-06 | 12/19 (NCI-H1792, J82, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.690×** | -5.6 | 4e-06 | 12/19 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.734×** | -4.6 | 5e-04 | 15/19 (HEC-1-A, CFPAC-1, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.821×** | -4.2 | 0.003 | 7/19 (SNU-423, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.765×** | -3.9 | 0.010 | 12/19 (CFPAC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.782×** | -3.7 | 0.018 | 13/19 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.784×** | -3.7 | 0.019 | 9/19 (NCI-H460, SW 900, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.785×** | -3.5 | 0.029 | 5/19 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -3.4 | 0.046 | 8/19 (NCI-H1792, A-427, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **0.806×** | -3.2 | 0.063 | 4/19 (H4, HEC-1-A, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.863× | -3.1 | 0.080 | 3/19 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.813×** | -3.1 | 0.080 | 7/19 (LOX-IMVI, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.807×** | -3.1 | 0.080 | 10/19 (SNU-423, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1277. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 171 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 74.8 | 1 | 7 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.00× (z +8.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0939× (z -12.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 60.0 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -11.3) |
| [[NCI-H2030 (line)]] | alt | 52.4 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0939× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.215× (z -9.7) |
| [[SHP-77 (line)]] | alt | 368 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -12.3) |
| [[A-427 (line)]] | wt | 413 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0579× (z -26.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 10.8 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 11.3× (z +18.5) | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 5.33× (z +15.0) | — |
| [[HEC-1-A (line)]] | alt | 32.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +11.4) | — |
| [[J82 (line)]] | alt | 52.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -11.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 11.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 25.2 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.17× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.0362× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[A498 (line)]] | wt | 39.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.41× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 8.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +11.8) | — |
| [[A-172 (line)]] | wt | 3.42 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.53 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.91 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.96 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.52 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.77 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.32 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.93 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.80 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1277), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD16]] | +0.63 | +0.53 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[NRXN1]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ERBB4]] | +0.62 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[GPM6A]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PEX5L]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CDH12]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[RALYL]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[RNF165]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[CDH8]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[EPHA3]] | +0.58 | +0.57 / +0.59 | both halves | 1e-05 | same gene group; pathway: EPH-Ephrin signaling; STRING 681 |
| [[LRP2]] | +0.57 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[KHDRBS2]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers EPHA6's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[NOVA1]] | C | NOVA1 activity raises EPHA6's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 4.39× lower at baseline in the lines without NOVA1 | 0.031 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IKZF2]] | B | EPHA6 activity raises IKZF2's level | lines that do not express EPHA6 (29) vs lines expressing it (21) | 2.42× lower at baseline in the lines without EPHA6 | 0.095 | ⚠ within organs, on part of the lines; also absent: SLITRK4, NOVA1, KCTD8 |
| [[RNF165]] | C | EPHA6 activity raises RNF165's level | lines that do not express EPHA6 (29) vs lines expressing it (21) | 2.63× lower at baseline in the lines without EPHA6 | 0.029 | ⚠ within organs, on part of the lines; also absent: SLITRK4, NOVA1, KCTD8; co-absent with the target |
| [[NOVA1]] | C | EPHA6 activity raises NOVA1's level | lines that do not express EPHA6 (29) vs lines expressing it (21) | 5.95× lower at baseline in the lines without EPHA6 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLITRK4, NOVA1, KCTD8; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.8, 33.2); signed map (41.9, 33.1). **Vector** length 75.2, 23.5% of its response variance represented; |z| ≥ 3 in 663 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +18.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.5 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.1 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +6.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +4.3 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.0 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -5.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -5.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -2.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor A6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q11.2 — chr3:96,814,581-97,761,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35246 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors |
| Reactome | 5 pathways, smallest: EPHA-mediated growth cone collapse; EPH-ephrin mediated repulsion of cells; EPH-Ephrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UF33](https://www.uniprot.org/uniprotkb/Q9UF33) (Ephrin type-A receptor 6):

> Receptor tyrosine kinase which binds promiscuously GPI-anchored ephrin-A family ligands residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling (By similarity).

**Summary**, from NCBI Gene [285220](https://www.ncbi.nlm.nih.gov/gene/285220):

> Predicted to enable transmembrane-ephrin receptor activity. Predicted to be involved in axon guidance and ephrin receptor signaling pathway. Predicted to be located in membrane. Predicted to be active in dendrite and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19296) · Entrez [285220](https://www.ncbi.nlm.nih.gov/gene/285220) · UniProt [Q9UF33](https://www.uniprot.org/uniprotkb/Q9UF33) · Ensembl [ENSG00000080224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080224)

## Data

Gene col 1277: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1277); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1277, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1277]; `tensor/DDL_lfc|DDL_z.npy` [1277]; `embed/gene_vectors.npy` [1277]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1277 or target_col == 1277). Every well: [[EPHA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

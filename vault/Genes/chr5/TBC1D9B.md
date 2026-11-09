---
symbol: "TBC1D9B"
type: "gene"
col: 12367
ensembl_id: "ENSG00000197226"
name: "TBC1 domain family member 9B"
location: "5q35.3"
module: 103
arm: "+"
pooled_cpm: 101.76
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# TBC1D9B

*TBC1 domain family member 9B* — 5q35.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A498 2.62×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 2.48×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.327× (z -32.5, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP250]] (+0.72, fdr 7e-06), [[YEATS2]] (+0.72, fdr 7e-06), [[PPFIA4]] (+0.69, fdr 7e-06); moves opposite to [[CPNE8]] (-0.49, fdr 1e-04), [[PELI2]] (-0.49, fdr 3e-05), [[ARHGAP42]] (-0.44, fdr 1e-04).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12367.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (A498 2.62×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 2.48×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | 1.41× | +3.7 | 0.10 | 18/48 (HOP62, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Adenosine (drug)]] 5 µM |  | 1.11× | +3.0 | 0.65 | 3/48 (CFPAC-1, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12367.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.327×** | -32.5 | 0e+00 | 45/48 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.313×** | -22.9 | 0e+00 | 46/48 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.482×** | -21.2 | 0e+00 | 45/49 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.392×** | -19.2 | 0e+00 | 45/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.407×** | -18.5 | 0e+00 | 47/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.427×** | -17.4 | 0e+00 | 46/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -15.8 | 0e+00 | 43/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.482×** | -15.0 | 0e+00 | 46/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.495×** | -13.9 | 4e-42 | 41/47 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.554×** | -11.7 | 1e-29 | 40/48 (SK-MEL-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.670×** | -11.6 | 2e-29 | 39/48 (SNU-423, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -11.1 | 7e-27 | 40/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.685×** | -11.0 | 2e-26 | 39/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.610×** | -10.1 | 2e-22 | 44/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -8.5 | 1e-15 | 38/50 (SK-MEL-2, SW480, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.680×** | -7.9 | 8e-14 | 40/48 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.690×** | -7.6 | 1e-12 | 34/48 (C32, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 120 | 0 | 20 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -28.6) |
| [[C32 (line)]] | wt | 129 | 0 | 18 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -26.7) |
| [[SK-MEL-2 (line)]] | alt | 154 | 0 | 15 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -29.9) |
| [[MIA PaCa-2 (line)]] | alt | 167 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -38.2) |
| [[J82 (line)]] | alt | 115 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -28.7) |
| [[PANC-1 (line)]] | alt | 88.8 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -24.5) |
| [[SNU-423 (line)]] | alt | 121 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -27.3) |
| [[HEC-1-A (line)]] | alt | 186 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -26.6) |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -27.9) |
| [[SW480 (line)]] | alt | 66.0 | 0 | 12 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -18.1) |
| [[A-172 (line)]] | wt | 217 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -32.1) |
| [[A549 (line)]] | wt | 92.5 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -28.0) |
| [[C-33 A (line)]] | alt | 175 | 0 | 10 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.359× (z -12.9) |
| [[HOP62 (line)]] | alt | 133 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -26.2) |
| [[NCI-H1573 (line)]] | alt | 109 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -30.7) |
| [[SW 900 (line)]] | alt | 126 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -24.5) |
| [[H4 (line)]] | wt | 162 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -16.7) |
| [[LoVo (line)]] | wt | 126 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -15.7) |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -19.3) |
| [[NCI-H23 (line)]] | alt | 71.2 | 0 | 8 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -17.0) |
| [[RKO (line)]] | wt | 91.1 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -18.6) |
| [[SW48 (line)]] | wt | 85.2 | 0 | 7 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0909× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -12.1) |
| [[A-427 (line)]] | wt | 87.3 | 0 | 6 | — | [[Harringtonine (drug)]] 5 µM 0.306× (z -12.7) |
| [[BT-474 (line)]] | alt | 80.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -21.2) |
| [[hTERT-HPNE (line)]] | wt | 80.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 72.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 111 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -23.4) |
| [[HCT15 (line)]] | alt | 154 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -20.1) |
| [[HS-578T (line)]] | alt | 85.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -15.0) |
| [[NCI-H2347 (line)]] | alt | 93.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -19.4) |
| [[AN3 CA (line)]] | alt | 133 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0517× (z -20.9) |
| [[HepG2_C3A (line)]] | wt | 79.0 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.231× (z -11.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.383× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 62.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -27.1) |
| [[Hs 766T (line)]] | wt | 82.6 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.488× (z -10.8) |
| [[LS 180 (line)]] | wt | 76.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.465× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 77.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -14.2) |
| [[A498 (line)]] | wt | 31.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | — |
| [[HT-29 (line)]] | alt | 58.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -11.8) |
| [[SNU-1 (line)]] | wt | 131 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.160× (z -15.5) |
| [[SW1417 (line)]] | alt | 67.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.2) |
| [[SW 1088 (line)]] | alt | 119 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0974× (z -9.0) |
| [[SW 1271 (line)]] | alt | 117 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.276× (z -8.7) |
| [[CHP-212 (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP250]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[YEATS2]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[PPFIA4]] | +0.69 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[GYS1]] | +0.63 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[ARFGEF3]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CRYBG3]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[INTS13]] | +0.59 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[SLX9]] | +0.58 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[CCDC47]] | +0.58 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[DDX41]] | +0.58 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[DPYSL4]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[CABIN1]] | +0.58 | +0.67 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE8]] | -0.49 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[PELI2]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ARHGAP42]] | -0.44 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[CREBRF]] | -0.42 | -0.39 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TBC1D9B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SMAD9]] | B | SMAD9 activity raises TBC1D9B's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without SMAD9 | 0.046 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.1, -17.2); signed map (-38.3, 25.9). **Vector** length 87.5, 28.7% of its response variance represented; |z| ≥ 3 in 1,398 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.2 | +1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | -18.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | -17.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.4 | +0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | -0.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +0.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.7 | -11.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -13.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -3.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -15.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -11.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -0.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.3 | -0.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 9B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:179,862,066-179,907,897 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0676, GRAMD9B |
| Gene groups (HGNC) | EF-hand domain containing; GRAM domain containing; TBC1 domain family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q66K14](https://www.uniprot.org/uniprotkb/Q66K14) (TBC1 domain family member 9B):

> May act as a GTPase-activating protein for Rab family protein(s).

**Summary**, from NCBI Gene [23061](https://www.ncbi.nlm.nih.gov/gene/23061):

> Predicted to enable GTPase activator activity. Predicted to be involved in system process. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29097) · Entrez [23061](https://www.ncbi.nlm.nih.gov/gene/23061) · UniProt [Q66K14](https://www.uniprot.org/uniprotkb/Q66K14) · Ensembl [ENSG00000197226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197226)

## Data

Gene col 12367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12367); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12367]; `tensor/DDL_lfc|DDL_z.npy` [12367]; `embed/gene_vectors.npy` [12367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12367 or target_col == 12367). Every well: [[TBC1D9B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D9B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

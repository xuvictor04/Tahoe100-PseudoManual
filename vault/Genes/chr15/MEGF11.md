---
symbol: "MEGF11"
type: "gene"
col: 8112
ensembl_id: "ENSG00000157890"
name: "multiple EGF like domains 11"
location: "15q22.31"
module: 102
arm: "+"
pooled_cpm: 7.45
n_lines_expressing: 45
n_dd_up: 44
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# MEGF11

*multiple EGF like domains 11* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.63× (z +25.0, q 0e+00, up in 28 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.111×, C-33 A 0.300×); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 0.153×, LoVo 0.213×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.155×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYN2]] (+0.68, fdr 7e-06), [[RBPMS2]] (+0.68, fdr 1e-05), [[MED12L]] (+0.67, fdr 7e-06); moves opposite to [[TMEM254]] (-0.56, fdr 2e-05), [[ASB8]] (-0.54, fdr 4e-05), [[DOP1A]] (-0.51, fdr 2e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CHD5]] → it (grade B ⚠); 2 go from it, the strongest it → [[TMEM254]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.63×** | +25.0 | 0e+00 | 28/35 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.57×** | +18.3 | 0e+00 | 28/42 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.27×** | +15.7 | 0e+00 | 4/11 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +12.9 | 4e-36 | 19/36 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.56×** | +12.9 | 7e-36 | 24/38 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +12.2 | 3e-32 | 6/13 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.38×** | +11.9 | 1e-30 | 10/21 (LoVo, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.14×** | +10.4 | 2e-23 | 24/36 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.95×** | +9.2 | 3e-18 | 19/42 (A-172, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +9.0 | 2e-17 | 15/42 (A549, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.23×** | +8.4 | 2e-15 | 15/21 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.84×** | +8.4 | 3e-15 | 17/37 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +8.2 | 8e-15 | 22/42 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.86×** | +8.2 | 1e-14 | 14/31 (A549, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +8.0 | 4e-14 | 19/41 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.73×** | +7.5 | 2e-12 | 14/33 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +6.5 | 2e-09 | 11/40 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +6.4 | 5e-09 | 14/36 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.9 | 1e-07 | 8/32 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.19×** | +5.6 | 5e-07 | 5/39 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.002 | 10/41 (NCI-H2347, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8112.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.111×, C-33 A 0.300×); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 0.153×, LoVo 0.213×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.155×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Busulfan (drug)]] 5 µM |  | 0.844× | -3.3 | 0.26 | 4/40 (Hs 766T, A-427, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.783× | -3.3 | 0.26 | 12/34 (SW 900, Hs 766T, …) | rises with dose |  |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.788× | -3.1 | 0.26 | 3/37 (NCI-H1792, SW1417, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.854× | -3.1 | 0.26 | 6/43 (PANC-1, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 30.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -22.9) |
| [[LoVo (line)]] | wt | 14.1 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.36× (z +9.1) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -12.3) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.213× (z -9.7) |
| [[C-33 A (line)]] | alt | 57.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 3.12 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.77× (z +11.9) | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0711× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 7.72 | 1 | 1 | [[Auranofin (drug)]] 5 µM 11.4× (z +9.9) | [[Thymol (drug)]] 0.5 µM 0.0864× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 25.1 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.223× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 5.37 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.07× (z +10.2) | — |
| [[A-172 (line)]] | wt | 3.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.22× (z +8.6) | — |
| [[A549 (line)]] | wt | 6.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.22× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 2.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 2.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 3.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.49× (z +8.9) | — |
| [[A498 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYN2]] | +0.68 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[RBPMS2]] | +0.68 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[MED12L]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SUGCT]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[CDH23]] | +0.65 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[PHF21B]] | +0.65 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[SDK2]] | +0.64 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[GALNT14]] | +0.61 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[GNAL]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[KCNG3]] | +0.60 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[GRID1]] | +0.60 | +0.43 / +0.68 | both halves | 4e-05 |  |
| [[RASGEF1C]] | +0.58 | +0.46 / +0.68 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM254]] | -0.56 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ASB8]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[DOP1A]] | -0.51 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[KIDINS220]] | -0.50 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[ABITRAM]] | -0.50 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[NPHP1]] | -0.50 | -0.29 / -0.32 | both halves | 2e-04 |  |
| [[PKN2]] | -0.49 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[SPEF2]] | -0.49 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[SENP2]] | -0.49 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[ISCA2]] | -0.48 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[IFT22]] | -0.48 | -0.29 / -0.32 | both halves | 3e-04 |  |
| [[DCTN3]] | -0.48 | -0.38 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHD5]] | B | CHD5 activity raises MEGF11's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.49× lower at baseline in the lines without CHD5 | 0.006 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[MED12L]] | B | MED12L activity raises MEGF11's level | lines that do not express MED12L (18) vs lines expressing it (32) | 2.18× lower at baseline in the lines without MED12L | 0.042 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[RFPL1S]] | B | RFPL1S activity raises MEGF11's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.37× lower at baseline in the lines without RFPL1S | 0.058 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MEGF11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNG3]] | B | KCNG3 activity raises MEGF11's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 2.04× lower at baseline in the lines without KCNG3 | 0.082 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM254]] | B | MEGF11 activity raises TMEM254's level | lines that do not express MEGF11 (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without MEGF11 | 0.060 | ⚠ within organs, on part of the lines; also absent: CLIP3, UNC5CL, ZNF385C; maybe low, not absent; its own permutation p |
| [[DNAL4]] | B | MEGF11 activity raises DNAL4's level | lines that do not express MEGF11 (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without MEGF11 | 0.060 | ⚠ within organs, on part of the lines; also absent: CLIP3, UNC5CL, ZNF385C; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.1, 36.5); signed map (27.9, 24.8). **Vector** length 72.9, 12.4% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +18.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +25.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +6.1 | +11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +12.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +3.9 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -0.0 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | multiple EGF like domains 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,895,079-66,253,756 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1781, DKFZp434L121 |
| Matched by | ensembl_id |

**Function**, from UniProt [A6BM72](https://www.uniprot.org/uniprotkb/A6BM72) (Multiple epidermal growth factor-like domains protein 11):

> May regulate the mosaic spacing of specific neuron subtypes in the retina through homotypic retinal neuron repulsion. Mosaics provide a mechanism to distribute each cell type evenly across the retina, ensuring that all parts of the visual field have access to a full set of processing elements (By similarity).

**Summary**, from NCBI Gene [84465](https://www.ncbi.nlm.nih.gov/gene/84465):

> Predicted to be an extracellular matrix structural constituent. Predicted to be involved in homotypic cell-cell adhesion; retina layer formation; and substrate adhesion-dependent cell spreading. Predicted to be located in basolateral plasma membrane. Predicted to be active in basement membrane and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29635](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29635) · Entrez [84465](https://www.ncbi.nlm.nih.gov/gene/84465) · UniProt [A6BM72](https://www.uniprot.org/uniprotkb/A6BM72) · Ensembl [ENSG00000157890](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157890)

## Data

Gene col 8112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8112); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8112]; `tensor/DDL_lfc|DDL_z.npy` [8112]; `embed/gene_vectors.npy` [8112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8112 or target_col == 8112). Every well: [[MEGF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEGF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

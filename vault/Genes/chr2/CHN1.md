---
symbol: "CHN1"
type: "gene"
col: 4911
ensembl_id: "ENSG00000128656"
name: "chimerin 1"
location: "2q31.1"
module: 41
arm: "-"
pooled_cpm: 43.58
n_lines_expressing: 40
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# CHN1

*chimerin 1* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.48× (z +9.4, q 2e-18, up in 23 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.756× (z -4.7, q 0.001, down in 19 of 37 measured lines) ⚠ transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.775× (z -4.3, q 0.004, down in 19 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 0.130×, SHP-77 0.214×, NCI-H2030 0.206×, A549 0.367×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2030 0.215×, C-33 A 0.247×, SW480 0.471×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.273×, SW480 0.462×; ⚠ cell-cycle shift, explains ~24% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SW480 0.493×, NCI-H2030 0.369×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2E3]] (+0.62, fdr 1e-05), [[MIPOL1]] (+0.57, fdr 1e-05), [[CDH2]] (+0.56, fdr 1e-05); moves opposite to [[CCS]] (-0.56, fdr 2e-05), [[GOLGA2]] (-0.56, fdr 1e-05), [[KRBOX4]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DOCK3]] → it (grade B ⚠); 3 go from it, the strongest it → [[MPDZ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4911.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +9.4 | 2e-18 | 23/38 (SW1417, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +8.2 | 5e-14 | 26/38 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +7.5 | 1e-11 | 22/38 (LoVo, SW1417, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +5.3 | 1e-05 | 19/38 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +5.0 | 5e-05 | 14/34 (RPMI-7951, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +5.0 | 5e-05 | 18/38 (LoVo, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.8 | 1e-04 | 18/36 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.21×** | +4.5 | 4e-04 | 14/38 (HOP62, A498, …) | top dose only | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.007 | 13/38 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.011 | 13/37 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.011 | 15/37 (Panc 03.27, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.012 | 17/38 (HOP62, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.22×** | +3.4 | 0.033 | 16/37 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.033 | 13/37 (H4, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.033 | 9/38 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.033 | 11/37 (LOX-IMVI, J82, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.051 | 14/37 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.051 | 11/38 (SW1417, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.055 | 10/38 (A498, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4911.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (C-33 A 0.130×, SHP-77 0.214×, NCI-H2030 0.206×, A549 0.367×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2030 0.215×, C-33 A 0.247×, SW480 0.471×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.273×, SW480 0.462×; ⚠ cell-cycle shift, explains ~24% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SW480 0.493×, NCI-H2030 0.369×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.756×** | -4.7 | 0.001 | 19/37 (PANC-1, NCI-H661, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -4.3 | 0.004 | 19/38 (SW480, A-427, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.783×** | -4.0 | 0.013 | 15/37 (NCI-H2030, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4911. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 279 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.369× (z -8.6) |
| [[SW480 (line)]] | alt | 98.7 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.462× (z -10.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.493× (z -9.2) |
| [[A549 (line)]] | wt | 78.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 94.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 17.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.99× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 18.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.18× (z +10.8) | — |
| [[A-172 (line)]] | wt | 44.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.00× (z +8.8) ⚠ toxic | — |
| [[A-427 (line)]] | wt | 74.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.417× (z -8.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -9.2) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.17× (z +11.1) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 19.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.66× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW48 (line)]] | wt | 55.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 84.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.76 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.30 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.14 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4911), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2E3]] | +0.62 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[MIPOL1]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CDH2]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TBL1XR1]] | +0.56 | +0.36 / +0.59 | both halves | 9e-05 |  |
| [[AGPS]] | +0.54 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[DPH6]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ADGRA3]] | +0.53 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[USP25]] | +0.53 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[CTPS1]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[SMAD2]] | +0.53 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[ANKRD44]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[DNAH14]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCS]] | -0.56 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[GOLGA2]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[KRBOX4]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PMM1]] | -0.54 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[OSBPL2]] | -0.53 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[KLC4]] | -0.53 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[GOLGA5]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TARS3]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[SPTY2D1]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TMF1]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[ERCC5]] | -0.51 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[SWI5]] | -0.51 | -0.51 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DOCK3]] | B | DOCK3 activity raises CHN1's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 3.20× lower at baseline in the lines without DOCK3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[FTCDNL1]] | B | FTCDNL1 activity raises CHN1's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 3.02× lower at baseline in the lines without FTCDNL1 | 0.012 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPDZ]] | B | CHN1 activity raises MPDZ's level | lines that do not express CHN1 (10) vs lines expressing it (40) | 4.59× lower at baseline in the lines without CHN1 | 0.074 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HHIPL2, CARMIL2; maybe low, not absent |
| [[FIGN]] | B | CHN1 activity raises FIGN's level | lines that do not express CHN1 (10) vs lines expressing it (40) | 3.72× lower at baseline in the lines without CHN1 | 0.093 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HHIPL2, CARMIL2; maybe low, not absent |
| [[PPM1L]] | B | CHN1 activity raises PPM1L's level | lines that do not express CHN1 (10) vs lines expressing it (40) | 1.49× lower at baseline in the lines without CHN1 | 0.098 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HHIPL2, CARMIL2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.613). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (7.5, -39.8); signed map (12.2, -51.2). **Vector** length 84.2, 18.3% of its response variance represented; |z| ≥ 3 in 797 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.1 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.8 | +1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | -0.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Infigratinib (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | chimerin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:174,798,809-175,005,381 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RhoGAP2, ARHGAP2, n-chimerin; previously CHN, DURS2 |
| Gene groups (HGNC) | Rho GTPase activating proteins; SH2 domain containing |
| Reactome | 5 pathways, smallest: CDC42 GTPase cycle; RAC1 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P15882](https://www.uniprot.org/uniprotkb/P15882) (N-chimaerin):

> GTPase-activating protein for p21-rac and a phorbol ester receptor. Involved in the assembly of neuronal locomotor circuits as a direct effector of EPHA4 in axon guidance.

**Summary**, from NCBI Gene [1123](https://www.ncbi.nlm.nih.gov/gene/1123):

> This gene encodes GTPase-activating protein for ras-related p21-rac and a phorbol ester receptor. It is predominantly expressed in neurons, and plays an important role in neuronal signal-transduction mechanisms. Mutations in this gene are associated with Duane's retraction syndrome 2 (DURS2). Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Apr 2011]

**Accessions** — [HGNC:1943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1943) · Entrez [1123](https://www.ncbi.nlm.nih.gov/gene/1123) · UniProt [P15882](https://www.uniprot.org/uniprotkb/P15882) · Ensembl [ENSG00000128656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128656)

## Data

Gene col 4911: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4911); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4911, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4911]; `tensor/DDL_lfc|DDL_z.npy` [4911]; `embed/gene_vectors.npy` [4911]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4911 or target_col == 4911). Every well: [[CHN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

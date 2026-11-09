---
symbol: "MAPK1"
type: "gene"
col: 1848
ensembl_id: "ENSG00000100030"
name: "mitogen-activated protein kinase 1"
location: "22q11.22"
module: 50
arm: "+"
pooled_cpm: 115.25
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# MAPK1

*mitogen-activated protein kinase 1* — 22q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.99× (z +13.5, q 8e-39, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.765× (z -5.1, q 2e-04, down in 29 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.805× (z -4.3, q 0.005, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.287×, NCI-H1573 0.449×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (C32 0.337×, NCI-H23 0.337×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (BT-474 0.418×, NCI-H23 0.480×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.568×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW 1088 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOMO1]] (+0.65, fdr 1e-05), [[PRKACA]] (+0.64, fdr 2e-05), [[SLC25A39]] (+0.63, fdr 2e-05); moves opposite to [[BTN2A3P]] (-0.63, fdr 1e-05), [[CCDC174]] (-0.62, fdr 1e-05), [[GOSR1]] (-0.61, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1848.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.99×** | +13.5 | 8e-39 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +9.1 | 2e-17 | 40/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +9.0 | 4e-17 | 38/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +8.5 | 4e-15 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +8.2 | 3e-14 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +7.2 | 7e-11 | 38/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +6.5 | 6e-09 | 37/49 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.20×** | +5.1 | 2e-05 | 23/48 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +4.9 | 5e-05 | 26/48 (KATO III, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +4.5 | 5e-04 | 28/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.007 | 22/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1848.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.287×, NCI-H1573 0.449×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (C32 0.337×, NCI-H23 0.337×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (BT-474 0.418×, NCI-H23 0.480×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.568×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW 1088 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.765×** | -5.1 | 2e-04 | 29/47 (NCI-H2347, SW 1271, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.805×** | -4.3 | 0.005 | 23/48 (BT-474, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | **0.808×** | -4.2 | 0.005 | 27/48 (H4, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.852× | -3.2 | 0.22 | 21/49 (C-33 A, NCI-H1573, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 84.2 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +13.8) | — |
| [[SW480 (line)]] | alt | 114 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +18.4) | — |
| [[PANC-1 (line)]] | alt | 84.2 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +17.9) | — |
| [[KATO III (line)]] | alt | 108 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 118 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.418× (z -9.9) |
| [[H4 (line)]] | wt | 58.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.64× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +9.0) | [[Docetaxel (drug)]] 0.05 µM 0.292× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~13% of this change |
| [[NCI-H1573 (line)]] | alt | 106 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 116 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.480× (z -8.6) |
| [[SW1417 (line)]] | alt | 162 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +12.2) | — |
| [[HepG2_C3A (line)]] | wt | 108 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 100.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 125 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.568× (z -8.9) |
| [[A498 (line)]] | wt | 74.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.08× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 120 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 67.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 152 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 135 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +8.5) | — |
| [[LoVo (line)]] | wt | 102 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 185 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 109 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.6) | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.109× (z -8.8) |
| [[A-172 (line)]] | wt | 96.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 95.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 169 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 184 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 186 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 89.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 86.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 129 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 139 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO1]] | +0.65 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PRKACA]] | +0.64 | +0.46 / +0.59 | both halves | 2e-05 | pathway: Activation of NMDA receptors and postsynaptic events; STRING 929 |
| [[SLC25A39]] | +0.63 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[NAGA]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[PACS2]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PLP2]] | +0.62 | +0.70 / +0.38 | both halves | 6e-05 |  |
| [[SELENON]] | +0.61 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[STX2]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[DGKZ]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 | pathway: G alpha (q) signalling events |
| [[COLGALT1]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.60 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[TBCD]] | +0.60 | +0.43 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN2A3P]] | -0.63 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.62 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[GOSR1]] | -0.61 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[SART3]] | -0.58 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[BTN2A3P-1]] | -0.58 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[RSRC2]] | -0.58 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CCDC59]] | -0.58 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[DAXX]] | -0.56 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[BTN2A1]] | -0.56 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZNF226]] | -0.55 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[TRIP11]] | -0.55 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[BRD2]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MAPK1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.6, -23.4); signed map (-28.1, -39.6). **Vector** length 92.2, 25.5% of its response variance represented; |z| ≥ 3 in 817 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.2 | -3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.1 | -0.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +9.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +4.1 | +4.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +0.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.6 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.8 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.22 — chr22:21,759,657-21,867,680 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERK, ERK2, p41mapk, MAPK2; previously PRKM2, PRKM1 |
| Gene groups (HGNC) | Mitogen-activated protein kinase 3 and 1 (ERK1/2) family |
| Hallmark sets | PROTEIN_SECRETION, PI3K_AKT_MTOR_SIGNALING |
| Reactome | 171 pathways, smallest: Signaling by MAP2K mutants; Estrogen-stimulated signaling through PRKCZ; Negative feedback regulation of MAPK pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P28482](https://www.uniprot.org/uniprotkb/P28482) (Mitogen-activated protein kinase 1):

> Serine/threonine kinase which acts as an essential component of the MAP kinase signal transduction pathway. MAPK1/ERK2 and MAPK3/ERK1 are the 2 MAPKs which play an important role in the MAPK/ERK cascade. They participate also in a signaling cascade initiated by activated KIT and KITLG/SCF. Depending on the cellular context, the MAPK/ERK cascade mediates diverse biological functions such as cell growth, adhesion, survival and differentiation through the regulation of transcription, translation, …

**Summary**, from NCBI Gene [5594](https://www.ncbi.nlm.nih.gov/gene/5594):

> This gene encodes a member of the MAP kinase family. MAP kinases, also known as extracellular signal-regulated kinases (ERKs), act as an integration point for multiple biochemical signals, and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation and development. The activation of this kinase requires its phosphorylation by upstream kinases. Upon activation, this kinase translocates to the nucleus of the stimulated cells, where it …

**Accessions** — [HGNC:6871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6871) · Entrez [5594](https://www.ncbi.nlm.nih.gov/gene/5594) · UniProt [P28482](https://www.uniprot.org/uniprotkb/P28482) · Ensembl [ENSG00000100030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100030)

## Data

Gene col 1848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1848); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1848]; `tensor/DDL_lfc|DDL_z.npy` [1848]; `embed/gene_vectors.npy` [1848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1848 or target_col == 1848). Every well: [[MAPK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

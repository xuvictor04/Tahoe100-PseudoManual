---
symbol: "YY1"
type: "gene"
col: 2025
ensembl_id: "ENSG00000100811"
name: "YY1 transcription factor"
location: "14q32.2"
module: 74
arm: "+"
pooled_cpm: 181.21
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# YY1

*YY1 transcription factor* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.84× (z +9.0, q 1e-16, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.09× (z +5.7, q 1e-06, up in 43 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.689× (z -5.4, q 3e-05, down in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (AN3 CA 0.325×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL24]] (+0.66, fdr 1e-05), [[REST]] (+0.66, fdr 7e-06), [[SCAF11]] (+0.65, fdr 7e-06); moves opposite to [[JMJD7]] (-0.62, fdr 1e-05), [[HARS1]] (-0.61, fdr 1e-05), [[MTG1]] (-0.60, fdr 6e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[TNRC6C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.84×** | +9.0 | 1e-16 | 45/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.83×** | +8.9 | 2e-16 | 45/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +6.6 | 8e-09 | 32/48 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.52×** | +6.1 | 1e-07 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.51×** | +5.8 | 7e-07 | 41/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.09×** | +5.7 | 1e-06 | 43/49 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.44×** | +5.3 | 7e-06 | 35/48 (A549, SK-MEL-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.42×** | +5.2 | 2e-05 | 35/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +4.8 | 1e-04 | 35/48 (C-33 A, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **1.39×** | +4.7 | 1e-04 | 35/48 (A549, NCI-H1792, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +4.2 | 0.001 | 33/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.31×** | +4.0 | 0.003 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~98% of this change | **1.28×** | +3.6 | 0.014 | 32/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.27×** | +3.4 | 0.028 | 23/44 (SW480, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.40×** | +3.4 | 0.028 | 31/49 (PANC-1, LoVo, …) | all doses, flat | composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2025.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (AN3 CA 0.325×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.689×** | -5.4 | 3e-05 | 37/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.757×** | -4.1 | 0.012 | 29/48 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -3.7 | 0.034 | 26/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.848× | -3.4 | 0.092 | 23/48 (HCT15, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.800× | -3.3 | 0.12 | 31/49 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.803× | -3.2 | 0.12 | 26/48 (SK-MEL-2, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.811× | -3.1 | 0.17 | 24/48 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 154 | 9 (8 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.75× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Gefitinib (drug)]] 5 µM 2.08× (z +8.8) | — |
| [[SW480 (line)]] | alt | 200 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +15.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[COLO 205 (line)]] | alt | 139 | 4 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.91× (z +9.6) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.87× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 154 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +14.1) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 161 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +13.0) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[LS 180 (line)]] | wt | 182 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +16.9) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SW48 (line)]] | wt | 230 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +13.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 6.93× (z +10.0) | — |
| [[A549 (line)]] | wt | 145 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +16.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 139 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 205 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +10.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SW1417 (line)]] | alt | 205 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.11× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 164 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[KATO III (line)]] | alt | 156 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.71× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 171 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.57× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SHP-77 (line)]] | alt | 160 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[AN3 CA (line)]] | alt | 222 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.325× (z -9.1) |
| [[BT-474 (line)]] | alt | 181 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +8.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[C-33 A (line)]] | alt | 204 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.47× (z +9.7) | — |
| [[C32 (line)]] | wt | 146 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 7.64× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 180 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 187 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 181 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 144 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 143 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 163 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 190 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 155 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 198 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL24]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[REST]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 | same gene group |
| [[SCAF11]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[RSF1]] | +0.65 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[KMT2A]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 | pathway: Differentiation of T cells |
| [[CREBRF]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ARID4A]] | +0.64 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[ANKRD12]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[UBN2]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ASH1L]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[NIPBL]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 | STRING 557 |
| [[UBXN7]] | +0.62 | +0.53 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JMJD7]] | -0.62 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[HARS1]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[MTG1]] | -0.60 | -0.39 / -0.64 | both halves | 6e-05 |  |
| [[RABGGTB]] | -0.55 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[BMS1P2]] | -0.54 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[POMGNT1]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[DELE1]] | -0.54 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[AGK]] | -0.53 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[C3orf52]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[NCLN]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[APEX2]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[EFTUD2]] | -0.53 | -0.46 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNRC6C]] | C | YY1's natural level weakens TNRC6C's drug response | YY1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.17; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.3, -44.8); signed map (-8.0, 9.9). **Vector** length 90.1, 31.7% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +0.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | -0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.9 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | +0.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.6 | -0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | +0.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | +0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | YY1 transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:100,238,298-100,282,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NF-E1, DELTA, UCRBP, YIN-YANG-1, INO80S |
| Gene groups (HGNC) | Zinc fingers C2H2-type; INO80 complex subunits |
| Reactome | 15 pathways, smallest: TFAP2 (AP-2) family regulates transcription of growth factors and their receptors; Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors; DNA Damage Recognition in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [P25490](https://www.uniprot.org/uniprotkb/P25490) (Transcriptional repressor protein YY1):

> Multifunctional transcription factor that exhibits positive and negative control on a large number of cellular and viral genes by binding to sites overlapping the transcription start site. Binds to the consensus sequence 5'-CCGCCATNTT-3'; some genes have been shown to contain a longer binding motif allowing enhanced binding; the initial CG dinucleotide can be methylated greatly reducing the binding affinity. The effect on transcription regulation is depending upon the context in which it binds …

**Summary**, from NCBI Gene [7528](https://www.ncbi.nlm.nih.gov/gene/7528):

> YY1 is a ubiquitously distributed transcription factor belonging to the GLI-Kruppel class of zinc finger proteins. The protein is involved in repressing and activating a diverse number of promoters. YY1 may direct histone deacetylases and histone acetyltransferases to a promoter in order to activate or repress the promoter, thus implicating histone modification in the function of YY1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12856) · Entrez [7528](https://www.ncbi.nlm.nih.gov/gene/7528) · UniProt [P25490](https://www.uniprot.org/uniprotkb/P25490) · Ensembl [ENSG00000100811](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100811)

## Data

Gene col 2025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2025); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2025]; `tensor/DDL_lfc|DDL_z.npy` [2025]; `embed/gene_vectors.npy` [2025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2025 or target_col == 2025). Every well: [[YY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

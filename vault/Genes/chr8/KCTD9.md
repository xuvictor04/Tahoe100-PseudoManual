---
symbol: "KCTD9"
type: "gene"
col: 2492
ensembl_id: "ENSG00000104756"
name: "potassium channel tetramerization domain containing 9"
location: "8p21.2"
module: 233
arm: "+"
pooled_cpm: 112.92
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/233"]
generated_by: "tahoemap"
---

# KCTD9

*potassium channel tetramerization domain containing 9* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.53× (z +7.2, q 3e-10, up in 39 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.50× (z +6.9, q 2e-09, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 0.773× (z -4.4, q 0.006, down in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 0.403×, AsPC-1 0.364×, NCI-H1792 0.337×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.436×, NCI-H1573 0.494×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.303×; ⚠ cell-cycle shift, would explain all of this change); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H2347 0.479×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNRH1]] (+0.65, fdr 7e-06, ⚠ read-through risk), [[PPP1R2]] (+0.63, fdr 1e-05), [[DCAF6]] (+0.63, fdr 1e-05), [[HDAC3]] (+0.63, fdr 1e-05); moves opposite to [[CHTOP]] (-0.60, fdr 2e-05), [[HNRNPF]] (-0.59, fdr 1e-05), [[SRCAP]] (-0.59, fdr 2e-05).
> It is in [[Module 233]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +7.2 | 3e-10 | 39/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +6.9 | 2e-09 | 37/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +6.2 | 1e-07 | 32/48 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +5.7 | 1e-06 | 32/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 2e-05 | 32/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.29×** | +4.3 | 0.002 | 24/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +3.9 | 0.007 | 26/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.24×** | +3.6 | 0.027 | 21/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2492.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 0.403×, AsPC-1 0.364×, NCI-H1792 0.337×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A549 0.436×, NCI-H1573 0.494×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.303×; ⚠ cell-cycle shift, would explain all of this change); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H2347 0.479×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.773×** | -4.4 | 0.006 | 30/48 (HOP62, A549, …) | all doses, flat | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.828× | -3.2 | 0.27 | 20/48 (HOP62, A549, …) | all doses, flat | position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 0.835× | -3.1 | 0.27 | 19/48 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.836× | -3.1 | 0.27 | 20/48 (A549, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 449 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -16.9) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 71.7 | 5 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.72× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.34× (z +16.1) | — |
| [[LoVo (line)]] | wt | 45.9 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 105 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.98× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +13.7) | — |
| [[LS 180 (line)]] | wt | 72.4 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.62× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 146 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.69× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 39.9 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +14.7) | — |
| [[SW480 (line)]] | alt | 85.6 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.34× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +10.1) | — |
| [[A-172 (line)]] | wt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.403× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 208 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 79.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 166 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.479× (z -8.5) |
| [[A-427 (line)]] | wt | 84.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 153 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 197 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 73.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 84.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNRH1]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 | ⚠ **readthrough risk**: GNRH1 lies 3.2 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[PPP1R2]] | +0.63 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[DCAF6]] | +0.63 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.63 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[ATP11B]] | +0.61 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[VDAC3]] | +0.59 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[MACO1]] | +0.59 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[WASF2]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[RAB8B]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ECI2]] | +0.58 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[STRN]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[KATNA1]] | +0.58 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[TMEM65]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHTOP]] | -0.60 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[HNRNPF]] | -0.59 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.59 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[PPRC1]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[UTP14A]] | -0.56 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[MCPH1]] | -0.56 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[NCR3LG1]] | -0.55 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[MRRF]] | -0.55 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[DUS3L]] | -0.55 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[MGA]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers KCTD9's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 233]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.8, -12.8); signed map (-23.5, 16.8). **Vector** length 106, 30.3% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.7 | -0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | -0.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.8 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.6 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:25,427,847-25,458,476 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20038, BTBD27 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L273](https://www.uniprot.org/uniprotkb/Q7L273) (BTB/POZ domain-containing protein KCTD9):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex, which mediates the ubiquitination of target proteins, leading to their degradation by the proteasome.

**Summary**, from NCBI Gene [54793](https://www.ncbi.nlm.nih.gov/gene/54793):

> Enables cullin family protein binding activity and identical protein binding activity. Predicted to be involved in intracellular signal transduction; protein homooligomerization; and protein ubiquitination. Predicted to act upstream of or within several processes, including NK T cell lineage commitment; natural killer cell activation; and response to virus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22401) · Entrez [54793](https://www.ncbi.nlm.nih.gov/gene/54793) · UniProt [Q7L273](https://www.uniprot.org/uniprotkb/Q7L273) · Ensembl [ENSG00000104756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104756)

## Data

Gene col 2492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2492); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2492]; `tensor/DDL_lfc|DDL_z.npy` [2492]; `embed/gene_vectors.npy` [2492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2492 or target_col == 2492). Every well: [[KCTD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

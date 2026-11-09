---
symbol: "ARF4"
type: "gene"
col: 9636
ensembl_id: "ENSG00000168374"
name: "ARF GTPase 4"
location: "3p14.3"
module: 41
arm: "+"
pooled_cpm: 196.6
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ARF4

*ARF GTPase 4* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.06× (z +4.9, q 5e-04, up in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 2.71×, NCI-H460 2.41×; ⚠ cell-cycle shift, explains ~51% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (BT-474 2.63×; ⚠ cell-cycle shift, explains ~24% of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.559× (z -7.2, q 3e-10, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB5A]] (+0.79, fdr 7e-06), [[COQ10B]] (+0.79, fdr 7e-06), [[SPTY2D1]] (+0.77, fdr 7e-06); moves opposite to [[USP24]] (-0.59, fdr 1e-05), [[NDUFAF5]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9636.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 2.71×, NCI-H460 2.41×; ⚠ cell-cycle shift, explains ~51% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (BT-474 2.63×; ⚠ cell-cycle shift, explains ~24% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +4.9 | 5e-04 | 37/49 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.26×** | +4.3 | 0.005 | 26/48 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.050 | 33/49 (RPMI-7951, HS-578T, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.63× | +3.3 | 0.12 | 25/48 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.27× | +3.1 | 0.18 | 23/48 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.58× | +3.1 | 0.18 | 25/48 (HepG2/C3A, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9636.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.559×** | -7.2 | 3e-10 | 43/48 (LoVo, J82, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -6.4 | 5e-08 | 36/49 (SW 900, HCT15, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.620×** | -6.2 | 1e-07 | 44/48 (J82, HepG2/C3A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.611×** | -6.1 | 1e-07 | 37/47 (hTERT-HPNE, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.617×** | -5.8 | 9e-07 | 39/45 (NCI-H23, HCT15, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -5.4 | 6e-06 | 31/44 (C-33 A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -5.3 | 8e-06 | 38/48 (hTERT-HPNE, SW 900, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.751×** | -5.2 | 1e-05 | 34/48 (HS-578T, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.757×** | -5.1 | 2e-05 | 37/48 (HS-578T, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.678×** | -5.0 | 3e-05 | 32/49 (J82, HCT15, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.677×** | -4.8 | 6e-05 | 39/48 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.692×** | -4.8 | 9e-05 | 33/48 (hTERT-HPNE, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.710×** | -4.4 | 4e-04 | 29/48 (SW 900, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.712×** | -4.2 | 1e-03 | 31/47 (HepG2/C3A, NCI-H1573, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.800×** | -4.0 | 0.002 | 32/48 (AsPC-1, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.735×** | -4.0 | 0.002 | 30/48 (hTERT-HPNE, SW 900, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.739×** | -3.9 | 0.003 | 31/48 (SW 900, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.747×** | -3.7 | 0.006 | 38/48 (J82, HCT15, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.750×** | -3.7 | 0.006 | 34/48 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **0.825×** | -3.5 | 0.013 | 21/48 (HOP62, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 474 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 223 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.377× (z -9.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.412× (z -8.5) |
| [[LoVo (line)]] | wt | 256 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.402× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 385 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 371 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.447× (z -8.9) |
| [[BT-474 (line)]] | alt | 84.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +8.6) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[C-33 A (line)]] | alt | 80.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -14.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 119 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.0) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[HS-578T (line)]] | alt | 303 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.625× (z -8.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[HT-29 (line)]] | alt | 223 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -9.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 244 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 203 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.361× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 104 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.9) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[Panc 03.27 (line)]] | alt | 234 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -8.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 247 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -8.8) |
| [[SW1417 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 134 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 185 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 179 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 235 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 141 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 204 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 218 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB5A]] | +0.79 | +0.81 / +0.78 | both halves | 7e-06 | STRING 476 |
| [[COQ10B]] | +0.79 | +0.83 / +0.70 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.77 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[SEC24A]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC31A]] | +0.75 | +0.74 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[COPE]] | +0.74 | +0.67 / +0.72 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 707 |
| [[KCNQ1OT1]] | +0.74 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[SLC35A2]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[BLZF1]] | +0.72 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[SRA1]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[TINCR]] | +0.71 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP24]] | -0.59 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[NDUFAF5]] | -0.56 | -0.46 / -0.66 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARF4's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PDXDC1]] | C | PDXDC1's natural level strengthens ARF4's drug response | PDXDC1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.43; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.8, -36.6); signed map (-50.7, 14.2). **Vector** length 138, 53.5% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +3.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.2 | +4.3 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | +3.0 | +3.0 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.1 | -7.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.7 | -6.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -4.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.6 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | ARF GTPase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:57,571,363-57,598,220 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARF2 |
| Gene groups (HGNC) | ARF GTPase family |
| Hallmark sets | COAGULATION |
| Reactome | 14 pathways, smallest: VxPx cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [P18085](https://www.uniprot.org/uniprotkb/P18085) (ADP-ribosylation factor 4):

> GTP-binding protein that functions as an allosteric activator of the cholera toxin catalytic subunit, an ADP-ribosyltransferase. Involved in protein trafficking; may modulate vesicle budding and uncoating within the Golgi apparatus. Part of the ciliary targeting complex containing Rab11, ASAP1, Rabin8/RAB3IP, RAB11FIP3 and ARF4, which direct preciliary vesicle trafficking to mother centriole and ciliogenesis initiation.

**Summary**, from NCBI Gene [378](https://www.ncbi.nlm.nih.gov/gene/378):

> This gene is a member of the human ARF gene family whose members encode small guanine nucleotide-binding proteins that stimulate the ADP-ribosyltransferase activity of cholera toxin and play a role in vesicular trafficking and as activators of phospholipase D. The gene products include 5 ARF proteins and 11 ARF-like proteins and constitute one family of the RAS superfamily. The ARF proteins are categorized as class I, class II and class III; this gene is a class II member. The members of each …

**Accessions** — [HGNC:655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:655) · Entrez [378](https://www.ncbi.nlm.nih.gov/gene/378) · UniProt [P18085](https://www.uniprot.org/uniprotkb/P18085) · Ensembl [ENSG00000168374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168374)

## Data

Gene col 9636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9636); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9636]; `tensor/DDL_lfc|DDL_z.npy` [9636]; `embed/gene_vectors.npy` [9636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9636 or target_col == 9636). Every well: [[ARF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

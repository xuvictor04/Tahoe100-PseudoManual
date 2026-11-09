---
symbol: "ERLEC1"
type: "gene"
col: 905
ensembl_id: "ENSG00000068912"
name: "endoplasmic reticulum lectin 1"
location: "2p16.2"
module: 56
arm: "+"
pooled_cpm: 119.62
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# ERLEC1

*endoplasmic reticulum lectin 1* — 2p16.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 2.26×).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.572× (z -12.3, q 3e-32, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG6]] (+0.83, fdr 7e-06), [[ACBD3]] (+0.79, fdr 7e-06), [[SSR2]] (+0.78, fdr 7e-06); moves opposite to [[PRRC2B]] (-0.67, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[FBXO16]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 905.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 2.26×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.73 | 16/48 (NCI-H2347, HOP62, …) | two highest doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.73 | 5/49 (CFPAC-1, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 905.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.572×** | -12.3 | 3e-32 | 45/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.551×** | -10.2 | 7e-22 | 41/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -8.5 | 3e-15 | 37/49 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.670×** | -7.1 | 2e-10 | 42/48 (NCI-H460, AsPC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.743×** | -6.3 | 4e-08 | 30/48 (RPMI-7951, HOP62, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.705×** | -6.2 | 6e-08 | 31/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.706×** | -6.2 | 6e-08 | 35/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.694×** | -5.8 | 4e-07 | 34/48 (hTERT-HPNE, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.720×** | -5.8 | 4e-07 | 35/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.728×** | -5.6 | 1e-06 | 32/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.737×** | -5.4 | 4e-06 | 30/48 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -5.4 | 4e-06 | 30/48 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.743×** | -5.0 | 2e-05 | 24/44 (NCI-H1573, SHP-77, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.770×** | -4.6 | 2e-04 | 30/48 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.762×** | -4.6 | 2e-04 | 27/47 (H4, hTERT-HPNE, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.780×** | -4.4 | 4e-04 | 31/48 (NCI-H661, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.748×** | -3.9 | 0.003 | 26/47 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.667×** | -3.7 | 0.005 | 28/48 (AsPC-1, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.722×** | -3.0 | 0.064 | 19/48 (AsPC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.846× | -2.9 | 0.082 | 16/48 (NCI-H460, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 905. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 173 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -16.0) |
| [[A498 (line)]] | wt | 205 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -22.6) |
| [[KATO III (line)]] | alt | 165 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.328× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.347× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 129 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 138 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -18.1) |
| [[A-172 (line)]] | wt | 119 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -12.4) |
| [[H4 (line)]] | wt | 232 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -11.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 147 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.569× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 164 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.26× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -21.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 141 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 124 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.7) |
| [[HT-29 (line)]] | alt | 107 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.1) |
| [[LoVo (line)]] | wt | 98.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -11.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 126 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.5) |
| [[PANC-1 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.474× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 186 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -11.3) |
| [[A-427 (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.435× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[A549 (line)]] | wt | 154 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -9.9) |
| [[AN3 CA (line)]] | alt | 66.5 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.175× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 92.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -10.9) |
| [[HCT15 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[HEC-1-A (line)]] | alt | 90.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -8.9) |
| [[Hs 766T (line)]] | wt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 155 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -14.8) |
| [[J82 (line)]] | alt | 66.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[SHP-77 (line)]] | alt | 174 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -21.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 90.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.8) |
| [[SW 900 (line)]] | alt | 166 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.8) |
| [[SW1417 (line)]] | alt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -10.0) |
| [[SW48 (line)]] | wt | 73.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -14.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 122 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 79.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 93.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 905), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG6]] | +0.83 | +0.85 / +0.75 | both halves | 7e-06 | STRING 500 |
| [[ACBD3]] | +0.79 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[SSR2]] | +0.78 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.78 | +0.83 / +0.70 | both halves | 7e-06 |  |
| [[PGM3]] | +0.78 | +0.83 / +0.75 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.78 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.77 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[SUCO]] | +0.77 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.76 | +0.78 / +0.73 | both halves | 7e-06 |  |
| [[TMED9]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[COPB1]] | +0.75 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[SRP54]] | +0.75 | +0.78 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC2B]] | -0.67 | -0.64 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO16]] | C | ERLEC1's natural level strengthens FBXO16's drug response | ERLEC1's natural level across 40 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.39; direction not clear | 0.055 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.852). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, -34.3); signed map (-50.7, 11.4). **Vector** length 143, 49.6% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.67 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.69 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.69 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | -0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.6 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | -2.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -0.0 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | +2.9 | +3.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +2.8 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -10.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -5.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.9 | -4.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.8 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | endoplasmic reticulum lectin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.2 — chr2:53,787,009-53,833,038 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CL25084, XTP3TPB, XTP3-B, ERLECTIN; previously C2orf30 |
| Gene groups (HGNC) | MRH domain containing |
| Reactome | 16 pathways, smallest: Hh mutants are degraded by ERAD; Hh mutants abrogate ligand secretion; Defective CFTR causes cystic fibrosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DZ1](https://www.uniprot.org/uniprotkb/Q96DZ1) (Endoplasmic reticulum lectin 1):

> Probable lectin that binds selectively to improperly folded lumenal proteins. May function in endoplasmic reticulum quality control and endoplasmic reticulum-associated degradation (ERAD) of both non-glycosylated proteins and glycoproteins.

**Summary**, from NCBI Gene [27248](https://www.ncbi.nlm.nih.gov/gene/27248):

> This gene encodes a resident endoplasmic reticulum (ER) protein that functions in N-glycan recognition. This protein is thought to be involved in ER-associated degradation via its interaction with the membrane-associated ubiquitin ligase complex. It also functions as a regulator of multiple cellular stress-response pathways in a manner that promotes metastatic cell survival. Alternative splicing results in multiple transcript variants. A related pseudogene has been identified on chromosome 21. …

**Accessions** — [HGNC:25222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25222) · Entrez [27248](https://www.ncbi.nlm.nih.gov/gene/27248) · UniProt [Q96DZ1](https://www.uniprot.org/uniprotkb/Q96DZ1) · Ensembl [ENSG00000068912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068912)

## Data

Gene col 905: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 905); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 905, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 905]; `tensor/DDL_lfc|DDL_z.npy` [905]; `embed/gene_vectors.npy` [905]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 905 or target_col == 905). Every well: [[ERLEC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERLEC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

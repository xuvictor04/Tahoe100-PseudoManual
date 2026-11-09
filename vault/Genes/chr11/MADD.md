---
symbol: "MADD"
type: "gene"
col: 3146
ensembl_id: "ENSG00000110514"
name: "MAP kinase activating death domain"
location: "11p11.2"
module: 127
arm: "+"
pooled_cpm: 35.72
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# MADD

*MAP kinase activating death domain* — 11p11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 3.14×, NCI-H460 2.71×, A498 2.18×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.560× (z -13.7, q 9e-40, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC9A3R1]] (+0.61, fdr 1e-05), [[SNAP47]] (+0.54, fdr 1e-04), [[ILVBL]] (+0.53, fdr 4e-05); moves opposite to [[RNF217-AS1]] (-0.53, fdr 7e-05), [[SEC24B-AS1]] (-0.52, fdr 9e-05), [[KPNB1-DT]] (-0.52, fdr 8e-05).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3146.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LoVo 3.14×, NCI-H460 2.71×, A498 2.18×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.6 | 0.19 | 0/48 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | 1.20× | +3.1 | 0.54 | 15/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3146.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.560×** | -13.7 | 9e-40 | 39/48 (SW1417, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.515×** | -11.1 | 5e-26 | 33/45 (A-427, KATO III, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -9.8 | 3e-20 | 40/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.546×** | -9.7 | 4e-20 | 35/47 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.650×** | -6.6 | 3e-09 | 28/41 (SNU-423, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.670×** | -6.4 | 1e-08 | 24/38 (NCI-H460, SW1417, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.698×** | -5.8 | 6e-07 | 27/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.785×** | -4.0 | 0.004 | 21/47 (Panc 03.27, H4, …) | two highest doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.805×** | -3.5 | 0.030 | 17/47 (NCI-H1792, Panc 03.27, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.814×** | -3.4 | 0.035 | 18/48 (A-172, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.830×** | -3.1 | 0.098 | 15/47 (H4, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 71.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 22.7 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.112× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -9.9) |
| [[SNU-423 (line)]] | alt | 48.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 35.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -15.5) |
| [[HOP62 (line)]] | alt | 30.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.1) |
| [[HT-29 (line)]] | alt | 54.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -9.1) |
| [[KATO III (line)]] | alt | 46.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -11.9) |
| [[LS 180 (line)]] | wt | 44.1 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -13.2) |
| [[SW1417 (line)]] | alt | 97.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 30.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -11.0) |
| [[CHP-212 (line)]] | wt | 62.1 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.116× (z -9.7) |
| [[LoVo (line)]] | wt | 30.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +15.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 40.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 34.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 36.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 51.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -16.3) |
| [[A-427 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -12.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 27.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -8.9) |
| [[Hs 766T (line)]] | wt | 48.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.268× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -10.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 51.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -12.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A3R1]] | +0.61 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SNAP47]] | +0.54 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[ILVBL]] | +0.53 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[PDK2]] | +0.53 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[PIP4P1]] | +0.53 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[LRCH4]] | +0.51 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[KLHL26]] | +0.51 | +0.38 / +0.42 | both halves | 6e-05 |  |
| [[RNF40]] | +0.51 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[EDC4]] | +0.51 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[ABHD16A]] | +0.50 | +0.40 / +0.37 | both halves | 7e-05 |  |
| [[HIF1AN]] | +0.49 | +0.37 / +0.47 | both halves | 8e-05 |  |
| [[BCAM]] | +0.49 | +0.40 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF217-AS1]] | -0.53 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[SEC24B-AS1]] | -0.52 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[KPNB1-DT]] | -0.52 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[SAP30L-AS1]] | -0.51 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[RNF170]] | -0.51 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[CCNO-DT]] | -0.51 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[C2orf76]] | -0.50 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[PPP2CB]] | -0.50 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[EHBP1-AS1]] | -0.50 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[GCC2-AS1]] | -0.48 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[ANGEL2]] | -0.48 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[HGSNAT]] | -0.48 | -0.36 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MADD's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.433). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, -6.8); signed map (-7.0, 20.6). **Vector** length 85.0, 17.6% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.2 | +2.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +4.0 | +3.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.5 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -13.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -9.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -9.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | MAP kinase activating death domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,269,161-47,330,031 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DENN, KIAA0358, RAB3GEP, IG20 |
| Gene groups (HGNC) | DENN domain containing |
| Hallmark sets | APOPTOSIS |
| Reactome | 7 pathways, smallest: Regulation of TNFR1 signaling; TNF signaling; RAB GEFs exchange GTP for GDP on RABs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXG6](https://www.uniprot.org/uniprotkb/Q8WXG6) (MAP kinase-activating death domain protein):

> Guanyl-nucleotide exchange factor that regulates small GTPases of the Rab family. Converts GDP-bound inactive form of RAB27A and RAB27B to the GTP-bound active forms. Converts GDP-bound inactive form of RAB3A, RAB3C and RAB3D to the GTP-bound active forms, GTPases involved in synaptic vesicle exocytosis and vesicle secretion (By similarity). Plays a role in synaptic vesicle formation and in vesicle trafficking at the neuromuscular junction (By similarity). Involved in up-regulating a …

**Summary**, from NCBI Gene [8567](https://www.ncbi.nlm.nih.gov/gene/8567):

> Tumor necrosis factor alpha (TNF-alpha) is a signaling molecule that interacts with one of two receptors on cells targeted for apoptosis. The apoptotic signal is transduced inside these cells by cytoplasmic adaptor proteins. The protein encoded by this gene is a death domain-containing adaptor protein that interacts with the death domain of TNF-alpha receptor 1 to activate mitogen-activated protein kinase (MAPK) and propagate the apoptotic signal. It is membrane-bound and expressed at a higher …

**Accessions** — [HGNC:6766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6766) · Entrez [8567](https://www.ncbi.nlm.nih.gov/gene/8567) · UniProt [Q8WXG6](https://www.uniprot.org/uniprotkb/Q8WXG6) · Ensembl [ENSG00000110514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110514)

## Data

Gene col 3146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3146); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3146]; `tensor/DDL_lfc|DDL_z.npy` [3146]; `embed/gene_vectors.npy` [3146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3146 or target_col == 3146). Every well: [[MADD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MADD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

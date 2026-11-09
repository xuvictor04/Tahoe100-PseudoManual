---
symbol: "SLC30A5"
type: "gene"
col: 7021
ensembl_id: "ENSG00000145740"
name: "solute carrier family 30 member 5"
location: "5q13.1-q13.2"
module: 49
arm: "+"
pooled_cpm: 63.5
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SLC30A5

*solute carrier family 30 member 5* — 5q13.1-q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.46× (z +8.4, q 2e-14, up in 36 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.23× (z +4.8, q 4e-04, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 2.45×, AsPC-1 2.28×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 2.08×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.769× (z -8.4, q 3e-14, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG3]] (+0.82, fdr 7e-06), [[KDELR2]] (+0.74, fdr 7e-06), [[MCEE]] (+0.73, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7021.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 2.45×, AsPC-1 2.28×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 2.08×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +8.4 | 2e-14 | 36/47 (MIA PaCa-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +4.8 | 4e-04 | 22/48 (LOX-IMVI, A-427, …) | top dose only |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.12 | 8/48 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.15 | 6/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7021.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.769×** | -8.4 | 3e-14 | 33/48 (A498, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.708×** | -7.9 | 6e-13 | 33/48 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.717×** | -7.1 | 3e-10 | 28/45 (RKO, HCT15, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -6.4 | 3e-08 | 27/48 (HT-29, NCI-H460, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.818×** | -6.3 | 3e-08 | 25/49 (A498, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.760×** | -6.0 | 1e-07 | 25/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.779×** | -5.7 | 8e-07 | 24/48 (LoVo, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.792×** | -5.1 | 2e-05 | 23/41 (A-427, H4, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.800×** | -5.1 | 2e-05 | 23/49 (SW480, LoVo, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.805×** | -5.0 | 4e-05 | 22/48 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.809×** | -4.5 | 4e-04 | 20/47 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.828×** | -4.2 | 0.001 | 22/50 (NCI-H23, AN3 CA, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.837× | -3.9 | 0.004 | 20/48 (LoVo, PANC-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.844× | -3.9 | 0.004 | 20/48 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.849× | -3.8 | 0.007 | 15/48 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.851× | -3.7 | 0.008 | 16/49 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.903× | -3.2 | 0.044 | 12/48 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.870× | -3.2 | 0.044 | 13/49 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.049 | 9/49 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Drospirenone (drug)]] 0.5 µM |  | 0.873× | -3.1 | 0.056 | 10/48 (SW 900, AN3 CA, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.877× | -3.0 | 0.066 | 16/48 (HT-29, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7021. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 90.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.463× (z -11.0) |
| [[HS-578T (line)]] | alt | 55.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.427× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 102 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.478× (z -10.1) |
| [[A-172 (line)]] | wt | 54.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 79.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.28× (z +8.6) ⚠ toxic | [[Niclosamide (olamine) (drug)]] 5 µM 0.432× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~51% of this change |
| [[KATO III (line)]] | alt | 79.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LoVo (line)]] | wt | 121 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[MIA PaCa-2 (line)]] | alt | 57.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 73.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.343× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[AN3 CA (line)]] | alt | 74.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -11.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 66.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HCT15 (line)]] | alt | 83.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -11.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 68.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -8.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 59.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 53.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -8.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H460 (line)]] | wt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.517× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[RKO (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -12.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 66.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 75.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A549 (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7021), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG3]] | +0.82 | +0.77 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[KDELR2]] | +0.74 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[MCEE]] | +0.73 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[SEC23IP]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[RINT1]] | +0.71 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[OSTC]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[SEC13]] | +0.68 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[TMEM39A]] | +0.67 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[GOLGA5]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ERLEC1]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[SSR2]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SLC30A5's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.803). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.2, -36.5); signed map (-52.2, 12.5). **Vector** length 125, 34.1% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.51 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.51 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.9 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +4.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.4 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +0.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.2 | +2.9 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -7.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.2 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 30 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.1-q13.2 — chr5:69,093,991-69,131,069 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZTL1, ZnT-5, FLJ12496, FLJ12756, ZNT5, MGC5499, ZNTL1 |
| Gene groups (HGNC) | Solute carrier family 30 |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 6 pathways, smallest: Zinc transporters; Insulin processing; Metal ion SLC transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAD4](https://www.uniprot.org/uniprotkb/Q8TAD4) (Proton-coupled zinc antiporter SLC30A5):

> Together with SLC30A6 forms a functional proton-coupled zinc ion antiporter mediating zinc entry into the lumen of organelles along the secretory pathway. By contributing to zinc ion homeostasis within the early secretory pathway, regulates the activation and folding of enzymes like alkaline phosphatases and enzymes involved in phosphatidylinositol glycan anchor biosynthesis. Through the transport of zinc into secretory granules of pancreatic beta-cells, plays an important role in the storage …

**Summary**, from NCBI Gene [64924](https://www.ncbi.nlm.nih.gov/gene/64924):

> This gene encodes a member of the SLC30A/ZnT family of zinc transporter proteins. ZnT proteins mediate both cellular zinc efflux and zinc sequestration into membrane-bound organelles. The encoded protein plays a role in the early secretory pathway as a heterodimer with zinc transporter 6, and may also regulate zinc sequestration into secretory granules of pancreatic beta cells. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene, and a …

**Accessions** — [HGNC:19089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19089) · Entrez [64924](https://www.ncbi.nlm.nih.gov/gene/64924) · UniProt [Q8TAD4](https://www.uniprot.org/uniprotkb/Q8TAD4) · Ensembl [ENSG00000145740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145740)

## Data

Gene col 7021: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7021); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7021, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7021]; `tensor/DDL_lfc|DDL_z.npy` [7021]; `embed/gene_vectors.npy` [7021]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7021 or target_col == 7021). Every well: [[SLC30A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC30A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

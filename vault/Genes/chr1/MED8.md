---
symbol: "MED8"
type: "gene"
col: 8259
ensembl_id: "ENSG00000159479"
name: "mediator complex subunit 8"
location: "1p34.2"
module: 49
arm: "+"
pooled_cpm: 29.58
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 21
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# MED8

*mediator complex subunit 8* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.81× (z +5.0, q 3e-04, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.575× (z -12.0, q 2e-30, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RARS1]] (+0.76, fdr 1e-05), [[ACBD3]] (+0.76, fdr 7e-06), [[GMPPA]] (+0.76, fdr 7e-06); moves opposite to [[PSPC1]] (-0.59, fdr 4e-05), [[PRRC2B]] (-0.59, fdr 1e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8259.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +5.0 | 3e-04 | 24/48 (A498, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +4.3 | 0.004 | 20/47 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 1.50× | +3.5 | 0.10 | 16/46 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8259.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.575×** | -12.0 | 2e-30 | 37/47 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.579×** | -8.8 | 3e-16 | 31/48 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.583×** | -8.7 | 6e-16 | 29/42 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -8.3 | 2e-14 | 34/46 (SW1417, H4, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -7.9 | 2e-13 | 33/46 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.632×** | -7.1 | 1e-10 | 30/45 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -6.8 | 1e-09 | 31/48 (SW48, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.660×** | -6.7 | 2e-09 | 31/48 (SW 900, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.747×** | -6.4 | 1e-08 | 30/48 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -5.9 | 2e-07 | 21/35 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.790×** | -5.1 | 2e-05 | 25/47 (NCI-H2347, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.736×** | -4.9 | 4e-05 | 24/48 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.732×** | -4.7 | 1e-04 | 21/40 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.823×** | -4.2 | 9e-04 | 20/48 (A549, HS-578T, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.773×** | -3.9 | 0.003 | 22/47 (HS-578T, RKO, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.811×** | -3.2 | 0.038 | 16/48 (SNU-1, COLO 205, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.821×** | -3.2 | 0.044 | 9/48 (SW480, LoVo, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.828×** | -2.9 | 0.092 | 14/48 (HCT15, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 29.8 | 0 | 5 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 36.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -13.4) |
| [[A498 (line)]] | wt | 47.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -15.9) |
| [[Hs 766T (line)]] | wt | 55.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 29.5 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 33.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 33.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -10.1) |
| [[SNU-1 (line)]] | wt | 40.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -9.8) |
| [[A-172 (line)]] | wt | 26.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -9.7) |
| [[A-427 (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -9.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -11.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 52.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 63.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -13.4) |
| [[HT-29 (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -9.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0817× (z -17.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 28.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -10.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -11.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.169× (z -12.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.216× (z -12.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 30.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -9.0) |
| [[SW480 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.139× (z -9.0) ⚠ toxic |
| [[A549 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RARS1]] | +0.76 | +0.77 / +0.52 | both halves | 1e-05 |  |
| [[ACBD3]] | +0.76 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.76 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[SEC13]] | +0.75 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[ZNF526]] | +0.74 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[NPRL2]] | +0.74 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[TMEM208]] | +0.73 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.73 | +0.74 / +0.57 | both halves | 9e-06 |  |
| [[ARL1]] | +0.73 | +0.83 / +0.59 | both halves | 7e-06 |  |
| [[SSR2]] | +0.73 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[GOLGA5]] | +0.72 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[ERLEC1]] | +0.71 | +0.73 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSPC1]] | -0.59 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[PRRC2B]] | -0.59 | -0.50 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MED8's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.803). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.7, -33.7); signed map (-52.3, 11.2). **Vector** length 113, 28.9% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.58 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.58 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.58 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.5 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.2 | +4.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +1.9 | +2.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.0 | -8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -7.5 | -8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -7.2 | -6.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -7.0 | -4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -6.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.0 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -3.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:43,383,917-43,389,808 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17544, MGC19641, ARC32 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96G25](https://www.uniprot.org/uniprotkb/Q96G25) (Mediator of RNA polymerase II transcription subunit 8):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [112950](https://www.ncbi.nlm.nih.gov/gene/112950):

> This gene encodes a protein component of the mediator complex, which aids in transcriptional activation through interaction with RNA polymerase II and gene-specific transcription factors. The encoded protein may also function in ubiquitin ligation and protein degradation. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:19971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19971) · Entrez [112950](https://www.ncbi.nlm.nih.gov/gene/112950) · UniProt [Q96G25](https://www.uniprot.org/uniprotkb/Q96G25) · Ensembl [ENSG00000159479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159479)

## Data

Gene col 8259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8259); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8259]; `tensor/DDL_lfc|DDL_z.npy` [8259]; `embed/gene_vectors.npy` [8259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8259 or target_col == 8259). Every well: [[MED8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

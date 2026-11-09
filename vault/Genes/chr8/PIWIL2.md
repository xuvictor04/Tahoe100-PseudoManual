---
symbol: "PIWIL2"
type: "gene"
col: 12361
ensembl_id: "ENSG00000197181"
name: "piwi like RNA-mediated gene silencing 2"
location: "8p21.3"
module: 37
arm: "+"
pooled_cpm: 3.84
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# PIWIL2

*piwi like RNA-mediated gene silencing 2* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.15× (z +18.5, q 0e+00, up in 36 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM: 0.659× (z -3.9, q 0.065, down in 13 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Berbamine (drug)]] 0.05 µM in 1 line (HCT15 0.0271×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 0.114×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HS-578T 0.151×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP53]] (+0.83, fdr 7e-06), [[TMEM225B]] (+0.82, fdr 7e-06), [[SNX31]] (+0.80, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.15×** | +18.5 | 0e+00 | 36/36 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.55×** | +12.2 | 1e-31 | 25/37 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +9.3 | 3e-18 | 5/18 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.57×** | +8.7 | 5e-16 | 27/44 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +8.1 | 6e-14 | 23/35 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +6.9 | 4e-10 | 17/33 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +6.8 | 1e-09 | 11/21 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +6.7 | 1e-09 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +6.6 | 2e-09 | 21/46 (HS-578T, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +5.6 | 1e-06 | 20/42 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +4.9 | 5e-05 | 15/45 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +4.8 | 6e-05 | 19/44 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +4.4 | 6e-04 | 2/8 (SW480, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.1 | 0.002 | 14/35 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.002 | 12/46 (A498, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.011 | 15/40 (LS 180, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.012 | 8/45 (A498, HepG2/C3A, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.97×** | +3.3 | 0.035 | 6/41 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.042 | 9/44 (NCI-H2347, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12361.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Berbamine (drug)]] 0.05 µM in 1 line (HCT15 0.0271×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 0.114×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HS-578T 0.151×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.659×** | -3.9 | 0.065 | 13/46 (HT-29, SW480, …) | all doses, flat | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.695× | -3.4 | 0.14 | 7/46 (A-172, RPMI-7951, …) | all doses, flat | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.699× | -3.3 | 0.14 | 15/46 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | 0.702× | -3.3 | 0.14 | 9/46 (SW 1088, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.709× | -3.2 | 0.14 | 9/44 (LoVo, CHP-212, …) | inconsistent across doses |  |
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | 0.709× | -3.2 | 0.14 | 7/45 (A549, H4, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.788× | -3.1 | 0.14 | 11/46 (RPMI-7951, NCI-H460, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.722× | -3.0 | 0.18 | 9/44 (HS-578T, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 11.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 6.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 2.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 1 | — | [[Berbamine (drug)]] 0.05 µM 0.0271× (z -11.5) |
| [[HT-29 (line)]] | alt | 2.81 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 0.5 µM 0.0528× (z -8.9) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 4.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 4.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 4.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +8.5) | — |
| [[A-172 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP53]] | +0.83 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[TMEM225B]] | +0.82 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[SNX31]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.79 | +0.86 / +0.73 | both halves | 7e-06 |  |
| [[CASS4]] | +0.78 | +0.81 / +0.69 | both halves | 7e-06 |  |
| [[UPP2]] | +0.76 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[H2AZ1-DT]] | +0.76 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.75 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.75 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.73 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[ADCY10]] | +0.73 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[ZNNT1]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PIWIL2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.6, -16.9); signed map (12.0, 4.7). **Vector** length 68.9, 11.0% of its response variance represented; |z| ≥ 3 in 1,102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +18.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +8.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.7 | +3.3 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | piwi like RNA-mediated gene silencing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,275,316-22,357,568 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HILI, FLJ10351, Mili, CT80 |
| Gene groups (HGNC) | Piwi like RNA-mediated gene silencing family |
| Reactome | 2 pathways, smallest: PIWI-interacting RNA (piRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TC59](https://www.uniprot.org/uniprotkb/Q8TC59) (Piwi-like protein 2):

> Endoribonuclease that plays a central role during spermatogenesis by repressing transposable elements and preventing their mobilization, which is essential for the germline integrity (By similarity). Plays an essential role in meiotic differentiation of spermatocytes, germ cell differentiation and in self-renewal of spermatogonial stem cells (By similarity). Acts via the piRNA metabolic process, which mediates the repression of transposable elements during meiosis by forming complexes composed …

**Summary**, from NCBI Gene [55124](https://www.ncbi.nlm.nih.gov/gene/55124):

> PIWIL2 belongs to the Argonaute family of proteins, which function in development and maintenance of germline stem cells (Sasaki et al., 2003 [PubMed 12906857]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17644) · Entrez [55124](https://www.ncbi.nlm.nih.gov/gene/55124) · UniProt [Q8TC59](https://www.uniprot.org/uniprotkb/Q8TC59) · Ensembl [ENSG00000197181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197181)

## Data

Gene col 12361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12361); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12361]; `tensor/DDL_lfc|DDL_z.npy` [12361]; `embed/gene_vectors.npy` [12361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12361 or target_col == 12361). Every well: [[PIWIL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIWIL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

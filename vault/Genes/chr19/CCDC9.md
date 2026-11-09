---
symbol: "CCDC9"
type: "gene"
col: 2580
ensembl_id: "ENSG00000105321"
name: "coiled-coil domain containing 9"
location: "19q13.32"
module: 41
arm: "+"
pooled_cpm: 35.96
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# CCDC9

*coiled-coil domain containing 9* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.18× (z +6.3, q 1e-07, up in 12 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.26× (z +3.7, q 0.068, up in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 4.13×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 3.77×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 3.60×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 3.28×).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.611× (z -5.7, q 4e-06, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK19]] (+0.78, fdr 7e-06), [[GOLGA2]] (+0.71, fdr 7e-06), [[SAFB2]] (+0.68, fdr 7e-06); moves opposite to [[DOCK7]] (-0.52, fdr 5e-05), [[SLC35B4]] (-0.50, fdr 6e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2580.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 4.13×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 3.77×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 3.60×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 3.28×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +6.3 | 1e-07 | 12/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.068 | 20/47 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 1.32× | +3.4 | 0.15 | 24/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | 1.69× | +3.3 | 0.15 | 24/49 (RKO, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.31× | +3.2 | 0.16 | 21/46 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2580.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -5.7 | 4e-06 | 36/47 (H4, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.709×** | -5.7 | 4e-06 | 32/48 (CFPAC-1, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.630×** | -5.5 | 6e-06 | 34/48 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.639×** | -5.4 | 9e-06 | 31/48 (A498, RPMI-7951, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.721×** | -5.4 | 9e-06 | 33/48 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.648×** | -5.2 | 2e-05 | 42/48 (SW1417, AsPC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -4.4 | 9e-04 | 28/48 (HT-29, H4, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.697×** | -4.3 | 9e-04 | 27/48 (Hs 766T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.768×** | -4.3 | 9e-04 | 25/48 (H4, NCI-H23, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.706×** | -4.2 | 0.002 | 23/48 (AsPC-1, A498, …) | all doses, flat | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.713×** | -4.1 | 0.002 | 23/46 (H4, SNU-1, …) | all doses, flat | composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.714×** | -4.1 | 0.002 | 26/48 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.780×** | -4.0 | 0.003 | 25/48 (SNU-423, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.716×** | -3.9 | 0.004 | 25/46 (MIA PaCa-2, HS-578T, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.727×** | -3.8 | 0.005 | 25/48 (H4, A498, …) | inconsistent across doses | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.013 | 24/48 (NCI-H1792, A498, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.758×** | -3.2 | 0.040 | 20/48 (COLO 205, NCI-H2030, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.771×** | -3.1 | 0.049 | 18/48 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.773×** | -3.1 | 0.051 | 17/48 (A-427, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +13.8) | — |
| [[H4 (line)]] | wt | 77.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0298× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -8.6) |
| [[SNU-1 (line)]] | wt | 34.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A498 (line)]] | wt | 72.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A549 (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[C-33 A (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.237× (z -9.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 25.9 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0858× (z -9.6) |
| [[HS-578T (line)]] | alt | 73.7 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.109× (z -8.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[SK-MEL-2 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SW 900 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0457× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A-172 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK19]] | +0.78 | +0.73 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[GOLGA2]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[SAFB2]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[FOXRED1]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[POFUT2]] | +0.67 | +0.73 / +0.57 | both halves | 9e-06 |  |
| [[TSPYL2]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ZNF417]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[ARFIP2]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SUPT5H]] | +0.64 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[ELP5]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[PDXDC1]] | +0.63 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[AKAP17A]] | +0.62 | +0.71 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK7]] | -0.52 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[SLC35B4]] | -0.50 | -0.59 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CCDC9's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.5% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (9.6, -37.2); signed map (-50.5, 16.4). **Vector** length 97.8, 25.2% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.5 | +1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.8 | -3.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.6 | -4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.0 |
|  | [[Oxaliplatin (drug)]] 0.05 µM |  | +2.2 | +1.6 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.8 | +1.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +0.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.1 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -5.4 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.9 | -5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:47,255,980-47,273,701 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586M1019 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3X0](https://www.uniprot.org/uniprotkb/Q9Y3X0) (Coiled-coil domain-containing protein 9):

> Probable component of the exon junction complex (EJC), a multiprotein complex that associates immediately upstream of the exon-exon junction on mRNAs and serves as a positional landmark for the intron exon structure of genes and directs post-transcriptional processes in the cytoplasm such as mRNA export, nonsense-mediated mRNA decay (NMD) or translation.

**Summary**, from NCBI Gene [26093](https://www.ncbi.nlm.nih.gov/gene/26093):

> Enables RNA binding activity. Part of exon-exon junction complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24560](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24560) · Entrez [26093](https://www.ncbi.nlm.nih.gov/gene/26093) · UniProt [Q9Y3X0](https://www.uniprot.org/uniprotkb/Q9Y3X0) · Ensembl [ENSG00000105321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105321)

## Data

Gene col 2580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2580); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2580]; `tensor/DDL_lfc|DDL_z.npy` [2580]; `embed/gene_vectors.npy` [2580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2580 or target_col == 2580). Every well: [[CCDC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

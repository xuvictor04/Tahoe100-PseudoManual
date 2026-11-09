---
symbol: "TAOK2"
type: "gene"
col: 7419
ensembl_id: "ENSG00000149930"
name: "TAO kinase 2"
location: "16p11.2"
module: 138
arm: "+"
pooled_cpm: 18.41
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# TAOK2

*TAO kinase 2* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.23× (z +14.8, q 0e+00, up in 43 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C-33 A 0.105×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.224×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (SW48 0.0800×); [[Naproxen (drug)]] 0.05 µM in 1 line (SW48 0.0916×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP19]] (+0.72, fdr 7e-06), [[SRCAP]] (+0.66, fdr 7e-06), [[CACTIN]] (+0.65, fdr 1e-05); moves opposite to [[DUXAP10]] (-0.55, fdr 2e-05), [[EIF2A]] (-0.53, fdr 2e-05), [[ADGRL3-AS1]] (-0.51, fdr 3e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Erythromycin (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +14.8 | 0e+00 | 43/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.94×** | +8.6 | 2e-15 | 41/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +7.2 | 1e-10 | 29/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +6.6 | 5e-09 | 34/47 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +5.8 | 8e-07 | 29/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +5.6 | 2e-06 | 29/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +5.0 | 4e-05 | 26/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 6e-04 | 23/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.2 | 0.002 | 20/44 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.36×** | +4.0 | 0.004 | 18/47 (MIA PaCa-2, SW480, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.36×** | +3.7 | 0.010 | 16/47 (SW480, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +3.7 | 0.011 | 18/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.5 | 0.024 | 15/47 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +3.4 | 0.026 | 14/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.033 | 15/48 (SW1417, COLO 205, …) | rises with dose | position effect removed |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.041 | 10/48 (SW1417, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7419.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (C-33 A 0.105×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.224×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (SW48 0.0800×); [[Naproxen (drug)]] 0.05 µM in 1 line (SW48 0.0916×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.727× | -3.7 | 0.12 | 12/47 (RKO, PANC-1, …) | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.784× | -3.2 | 0.37 | 14/47 (RKO, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 27.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 16.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.29× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 28.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 15.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SW48 (line)]] | wt | 18.2 | 0 | 2 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0800× (z -10.5) |
| [[SW480 (line)]] | alt | 17.8 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +9.7) | — |
| [[A549 (line)]] | wt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 29.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.105× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +15.2) | — |
| [[A-172 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP19]] | +0.72 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[SRCAP]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[CACTIN]] | +0.65 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[DMWD]] | +0.65 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[CELSR3]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CNOT3]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R37]] | +0.63 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[CHTOP]] | +0.62 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[STRN4]] | +0.62 | +0.57 / +0.69 | both halves | 1e-05 | STRING 455 |
| [[KMT2B]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[SCAF1]] | +0.61 | +0.67 / +0.65 | both halves | 7e-06 | STRING 669 |
| [[REXO1]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUXAP10]] | -0.55 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[EIF2A]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ADGRL3-AS1]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[USP3]] | -0.49 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[RNMT]] | -0.48 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[RPL39]] | -0.48 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[RBPJ]] | -0.47 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Erythromycin (drug)]] 0.5 µM | C | TAOK2's natural level lowers the cells' numbers under Erythromycin 0.5 µM (makes them more sensitive) | TAOK2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.352 over the table, 0.095 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.5, -23.3); signed map (2.0, -8.7). **Vector** length 82.2, 16.1% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +14.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.6 | +8.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.5 | +2.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.1 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.8 | +3.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +1.8 | +2.2 |
|  | [[Altretamine (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +1.7 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -0.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.4 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | TAO kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,973,868-29,992,261 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAO1, KIAA0881, PSK, PSK1, TAO2, MAP3K17, hKFC-C, PSK-1 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; TAO kinase family |
| Hallmark sets | APICAL_JUNCTION, MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL54](https://www.uniprot.org/uniprotkb/Q9UL54) (Serine/threonine-protein kinase TAO2):

> Serine/threonine-protein kinase involved in different processes such as membrane blebbing and apoptotic bodies formation DNA damage response and MAPK14/p38 MAPK stress-activated MAPK cascade. Phosphorylates itself, MBP, activated MAPK8, MAP2K3, MAP2K6 and tubulins. Activates the MAPK14/p38 MAPK signaling pathway through the specific activation and phosphorylation of the upstream MAP2K3 and MAP2K6 kinases. In response to DNA damage, involved in the G2/M transition DNA damage checkpoint by …

**Summary**, from NCBI Gene [9344](https://www.ncbi.nlm.nih.gov/gene/9344):

> Enables mitogen-activated protein kinase kinase binding activity; neuropilin binding activity; and protein serine/threonine kinase activity. Involved in several processes, including focal adhesion assembly; intracellular signal transduction; and positive regulation of MAPK cascade. Located in cytoplasmic vesicle; nucleolus; and nucleoplasm. Part of signaling receptor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16835](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16835) · Entrez [9344](https://www.ncbi.nlm.nih.gov/gene/9344) · UniProt [Q9UL54](https://www.uniprot.org/uniprotkb/Q9UL54) · Ensembl [ENSG00000149930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149930)

## Data

Gene col 7419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7419); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7419]; `tensor/DDL_lfc|DDL_z.npy` [7419]; `embed/gene_vectors.npy` [7419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7419 or target_col == 7419). Every well: [[TAOK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAOK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

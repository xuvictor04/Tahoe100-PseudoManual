---
symbol: "ISY1"
type: "gene"
col: 14246
ensembl_id: "ENSG00000240682"
name: "ISY1 spliceosome associated protein"
location: "3q21.3"
module: 41
arm: "+"
pooled_cpm: 51.53
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ISY1

*ISY1 spliceosome associated protein* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.59× (z +12.0, q 2e-30, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.800× (z -5.7, q 8e-06, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.193×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0836×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.554×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ING4]] (+0.71, fdr 7e-06), [[GLUD1P3]] (+0.69, fdr 1e-05), [[KLC4]] (+0.65, fdr 2e-05); moves opposite to [[PANK3]] (-0.62, fdr 7e-06), [[EFR3A]] (-0.59, fdr 1e-05), [[SACS]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ASB7]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.59×** | +12.0 | 2e-30 | 44/49 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +11.9 | 4e-30 | 43/48 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +9.1 | 1e-17 | 39/48 (A-427, SHP-77, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.46×** | +8.5 | 4e-15 | 34/48 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +7.0 | 4e-10 | 39/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.6 | 2e-06 | 36/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +5.5 | 3e-06 | 37/48 (A498, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.4 | 6e-06 | 31/47 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.28×** | +4.5 | 5e-04 | 24/47 (PANC-1, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +4.3 | 0.001 | 27/49 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.26×** | +4.1 | 0.002 | 23/48 (PANC-1, SW480, …) | inconsistent across doses | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.003 | 25/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.25×** | +3.9 | 0.004 | 21/48 (MIA PaCa-2, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14246.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.193×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0836×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.554×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.800×** | -5.7 | 8e-06 | 31/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.830× | -3.4 | 0.22 | 22/48 (SW480, H4, …) | rises with dose |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.882× | -3.2 | 0.22 | 10/48 (HT-29, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.838× | -3.2 | 0.22 | 13/48 (SW 1088, NCI-H2347, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.843× | -3.1 | 0.24 | 13/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 82.1 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.45× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 57.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +11.8) | — |
| [[A-427 (line)]] | wt | 68.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.28× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 47.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 50.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.19× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 39.1 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.08× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 58.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 60.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.4× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 43.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.4) | — |
| [[J82 (line)]] | alt | 45.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.3) | — |
| [[LoVo (line)]] | wt | 35.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.96× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 52.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.62× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 50.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 62.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.20× (z +8.5) | — |
| [[RKO (line)]] | wt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 51.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.38× (z +8.6) | — |
| [[SW 1271 (line)]] | alt | 56.4 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0836× (z -9.1) |
| [[SW480 (line)]] | alt | 59.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.02× (z +9.0) | — |
| [[A-172 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING4]] | +0.71 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[GLUD1P3]] | +0.69 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[KLC4]] | +0.65 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[ERCC5]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 | pathway: Dual incision in TC-NER |
| [[APPBP2]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[MED6]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[NOXRED1]] | +0.65 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[SCNM1]] | +0.64 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[RPL34-DT]] | +0.63 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[MED4]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[AKAP17A]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SLC4A1AP]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PANK3]] | -0.62 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[EFR3A]] | -0.59 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[SACS]] | -0.58 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[JPH1]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ZMIZ2]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[IDH3A]] | -0.54 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[DNAH14]] | -0.53 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[TMEM185B]] | -0.53 | -0.38 / -0.62 | both halves | 6e-05 |  |
| [[ANKRD50]] | -0.52 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[ARHGDIA]] | -0.52 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[TAF1B]] | -0.52 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[CLN6]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ISY1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASB7]] | C | ISY1's natural level strengthens ASB7's drug response | ISY1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.03; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-12.6, 2.1); signed map (-3.8, -2.8). **Vector** length 93.0, 22.6% of its response variance represented; |z| ≥ 3 in 859 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +11.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +9.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +3.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +0.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | +0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ISY1 spliceosome associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:129,127,415-129,161,063 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1160, fSAP33 |
| Gene groups (HGNC) | Spliceosomal B complex; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 13 pathways, smallest: Formation of TC-NER Pre-Incision Complex; Gap-filling DNA repair synthesis and ligation in TC-NER; Dual incision in TC-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULR0](https://www.uniprot.org/uniprotkb/Q9ULR0) (Pre-mRNA-splicing factor ISY1 homolog):

> Component of the spliceosome C complex required for the selective processing of microRNAs during embryonic stem cell differentiation (By similarity). Required for the biogenesis of all miRNAs from the pri-miR-17-92 primary transcript except miR-92a (By similarity). Only required for the biogenesis of miR-290 and miR-96 from the pri-miR-290-295 and pri-miR-96-183 primary transcripts, respectively (By similarity). Required during the transition of embryonic stem cells (ESCs) from the naive to …

**Summary**, from NCBI Gene [57461](https://www.ncbi.nlm.nih.gov/gene/57461):

> Enables RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in nuclear speck. Part of U2-type catalytic step 1 spliceosome and catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29201) · Entrez [57461](https://www.ncbi.nlm.nih.gov/gene/57461) · UniProt [Q9ULR0](https://www.uniprot.org/uniprotkb/Q9ULR0) · Ensembl [ENSG00000240682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240682)

## Data

Gene col 14246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14246); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14246]; `tensor/DDL_lfc|DDL_z.npy` [14246]; `embed/gene_vectors.npy` [14246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14246 or target_col == 14246). Every well: [[ISY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

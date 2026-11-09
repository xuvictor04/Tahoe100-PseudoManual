---
symbol: "CCDC137"
type: "gene"
col: 11656
ensembl_id: "ENSG00000185298"
name: "coiled-coil domain containing 137"
location: "17q25.3"
module: 11
arm: "+"
pooled_cpm: 37.05
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CCDC137

*coiled-coil domain containing 137* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 3.16× (z +11.1, q 1e-25, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 0.102×, A549 0.178×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Monocrotaline (drug)]] 5 µM in 1 line (AN3 CA 0.0581×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW48 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRM2]] (+0.79, fdr 7e-06), [[CEBPZ]] (+0.76, fdr 7e-06), [[DNTTIP2]] (+0.76, fdr 7e-06); moves opposite to [[LAPTM4A]] (-0.69, fdr 7e-06), [[CLSTN1]] (-0.66, fdr 7e-06), [[TWSG1]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11656.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.16×** | +11.1 | 1e-25 | 44/47 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.74×** | +9.7 | 1e-19 | 45/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.77×** | +9.4 | 1e-18 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.99×** | +9.4 | 1e-18 | 38/47 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.28×** | +7.9 | 3e-13 | 45/48 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +7.4 | 1e-11 | 42/46 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.61×** | +6.4 | 9e-09 | 35/48 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.90×** | +6.2 | 5e-08 | 36/48 (LS 180, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.90×** | +6.1 | 5e-08 | 37/48 (COLO 205, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.83×** | +5.4 | 5e-06 | 36/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +4.9 | 5e-05 | 34/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.69×** | +4.8 | 7e-05 | 33/47 (CFPAC-1, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.6 | 2e-04 | 35/48 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.56×** | +4.1 | 0.002 | 29/48 (CFPAC-1, KATO III, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.35×** | +4.0 | 0.002 | 33/48 (A498, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.002 | 28/47 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.005 | 27/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.021 | 25/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | **1.37×** | +2.9 | 0.092 | 23/47 (A-172, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11656.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 0.102×, A549 0.178×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Monocrotaline (drug)]] 5 µM in 1 line (AN3 CA 0.0581×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW48 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.708× | -3.3 | 0.46 | 25/48 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 57.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +12.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.40× (z +11.9) | — |
| [[A498 (line)]] | wt | 43.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.50× (z +9.5) | — |
| [[A549 (line)]] | wt | 29.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +11.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.70× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 99.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.84× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.72× (z +10.2) | — |
| [[KATO III (line)]] | alt | 47.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.4) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1792 (line)]] | alt | 23.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.24× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 35.3 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.0581× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.23× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.83× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 73.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 24.5 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.06× (z +8.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 37.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.10× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 35.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.55× (z +9.6) | — |
| [[SW48 (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 57.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRM2]] | +0.79 | +0.77 / +0.83 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.76 | +0.74 / +0.81 | both halves | 7e-06 |  |
| [[DNTTIP2]] | +0.76 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[SURF6]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[UTP3]] | +0.75 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.75 | +0.72 / +0.76 | both halves | 7e-06 | STRING 467 |
| [[RPL7L1]] | +0.74 | +0.85 / +0.69 | both halves | 7e-06 |  |
| [[REXO4]] | +0.73 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[NIFK]] | +0.73 | +0.75 / +0.74 | both halves | 7e-06 | STRING 601 |
| [[DDX28]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[RPP38]] | +0.73 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAPTM4A]] | -0.69 | -0.77 / -0.63 | both halves | 7e-06 |  |
| [[CLSTN1]] | -0.66 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[TWSG1]] | -0.66 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[LAMP2]] | -0.65 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[TMEM30A]] | -0.65 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[PSAP]] | -0.65 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[SUMF2]] | -0.64 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[CREG1]] | -0.64 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[TMED10]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[TM9SF2]] | -0.63 | -0.68 / -0.62 | both halves | 7e-06 |  |
| [[CRTAP]] | -0.62 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[MGAT4A]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC137's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MRPL58]] | C | MRPL58's natural level strengthens CCDC137's drug response | MRPL58's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.01; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.8, 1.7); signed map (-1.8, -21.1). **Vector** length 101, 32.5% of its response variance represented; |z| ≥ 3 in 851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.2 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.4 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +11.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.5 | +9.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.7 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -6.9 | +1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -6.7 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.4 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -1.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.6 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 137 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,666,737-81,673,904 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC16597 |
| Matched by | ensembl_id |

UniProt [Q6PK04](https://www.uniprot.org/uniprotkb/Q6PK04) carries no function annotation.

**Summary**, from NCBI Gene [339230](https://www.ncbi.nlm.nih.gov/gene/339230):

> Enables RNA binding activity. Located in chromosome; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33451) · Entrez [339230](https://www.ncbi.nlm.nih.gov/gene/339230) · UniProt [Q6PK04](https://www.uniprot.org/uniprotkb/Q6PK04) · Ensembl [ENSG00000185298](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185298)

## Data

Gene col 11656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11656); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11656]; `tensor/DDL_lfc|DDL_z.npy` [11656]; `embed/gene_vectors.npy` [11656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11656 or target_col == 11656). Every well: [[CCDC137 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC137.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

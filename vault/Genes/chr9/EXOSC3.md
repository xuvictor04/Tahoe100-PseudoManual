---
symbol: "EXOSC3"
type: "gene"
col: 2848
ensembl_id: "ENSG00000107371"
name: "exosome component 3"
location: "9p13.2"
module: 83
arm: "+"
pooled_cpm: 29.02
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# EXOSC3

*exosome component 3* — 9p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +18.0, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.743× (z -3.9, q 0.062, down in 10 of 46 measured lines) ⚠ cell-cycle shift, explains ~31% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0814×); [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.170×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.238×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Bendamustine (drug)]] 5 µM in 1 line (SW48 0.160×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLIPR1-AS1]] (+0.69, fdr 1e-05), [[MSH4]] (+0.68, fdr 1e-05), [[KANSL1L-AS1]] (+0.67, fdr 1e-05); moves opposite to [[USP2]] (-0.61, fdr 4e-05), [[HAUS4]] (-0.59, fdr 1e-04), [[TTBK2]] (-0.59, fdr 2e-04).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2848.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +18.0 | 0e+00 | 40/48 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +14.1 | 2e-42 | 38/48 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +13.3 | 7e-38 | 38/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +12.1 | 9e-32 | 37/48 (HOP62, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +9.8 | 1e-20 | 32/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +9.4 | 4e-19 | 32/48 (A-427, SW1417, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.8 | 7e-13 | 28/48 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +6.4 | 8e-09 | 21/47 (COLO 205, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.28×** | +5.8 | 3e-07 | 17/39 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.23×** | +5.1 | 2e-05 | 15/48 (NCI-H23, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +5.1 | 2e-05 | 17/47 (A549, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.23×** | +5.1 | 2e-05 | 13/48 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.25×** | +5.0 | 2e-05 | 13/47 (LOX-IMVI, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.22×** | +4.9 | 4e-05 | 17/47 (MIA PaCa-2, H4, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.22×** | +4.9 | 4e-05 | 16/48 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.9 | 0.003 | 14/48 (HT-29, SW480, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +3.8 | 0.004 | 10/48 (HEC-1-A, A549, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.7 | 0.007 | 9/48 (H4, HCT15, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.010 | 7/46 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.011 | 8/47 (MIA PaCa-2, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.041 | 3/47 (A498, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2848.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0814×); [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.170×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.238×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Bendamustine (drug)]] 5 µM in 1 line (SW48 0.160×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.743×** | -3.9 | 0.062 | 10/46 (SNU-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Pimitespib (drug)]] 0.05 µM |  | 0.866× | -3.2 | 0.37 | 4/48 (A549, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 2 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0870× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 21.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.0) | — |
| [[SW480 (line)]] | alt | 42.4 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.14× (z +10.6) | — |
| [[A-172 (line)]] | wt | 23.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.6) | — |
| [[A-427 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 32.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +11.5) | — |
| [[A549 (line)]] | wt | 36.6 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.42× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 32.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.106× (z -9.4) |
| [[COLO 205 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +17.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 27.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0814× (z -12.8) |
| [[LoVo (line)]] | wt | 27.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 63.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.68× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +11.9) | — |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 1 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.170× (z -10.6) |
| [[SW1417 (line)]] | alt | 27.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +11.3) | — |
| [[SW48 (line)]] | wt | 32.8 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.160× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLIPR1-AS1]] | +0.69 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[MSH4]] | +0.68 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[KANSL1L-AS1]] | +0.67 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[BAAT]] | +0.65 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[CSTF3]] | +0.64 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[PTCD1]] | +0.63 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ZNF596]] | +0.63 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[EEF1AKMT1]] | +0.63 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[MSANTD2]] | +0.62 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[UQCC1]] | +0.62 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ZFHX2-AS1]] | +0.62 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[DCTN5]] | +0.62 | +0.37 / +0.53 | both halves | 8e-05 | pathway: Affinity selection of immunoglobulins |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP2]] | -0.61 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[HAUS4]] | -0.59 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[TTBK2]] | -0.59 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[NOS1AP]] | -0.57 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[FOXO6]] | -0.56 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[CFD]] | -0.56 | -0.54 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[KMT2C]] | -0.56 | -0.54 / -0.41 | both halves | 4e-05 | pathway: Affinity selection of immunoglobulins |
| [[CXADR]] | -0.55 | -0.68 / -0.34 | both halves | 1e-04 |  |
| [[ALAD]] | -0.55 | -0.51 / -0.26 | both halves | 4e-04 |  |
| [[HMGN3]] | -0.54 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[AMOT]] | -0.54 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[MPP7]] | -0.53 | -0.43 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EXOSC3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (28.7, -11.2); signed map (16.0, 2.0). **Vector** length 76.5, 13.2% of its response variance represented; |z| ≥ 3 in 856 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.5 | +14.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.5 | +12.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +13.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +18.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +9.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.8 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.8 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.6 | +5.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | exosome component 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.2 — chr9:37,759,234-37,832,117 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hRrp40p, Rrp40p, RRP40, CGI-102, p10, hRrp-40 |
| Gene groups (HGNC) | Exosome complex |
| Reactome | 20 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; KSRP (KHSRP) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQT5](https://www.uniprot.org/uniprotkb/Q9NQT5) (Exosome complex component RRP40):

> Non-catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the nucleus, the RNA exosome complex is involved in proper maturation of stable RNA species such as rRNA, snRNA and snoRNA, in the elimination of RNA processing by-products and non-coding 'pervasive' transcripts, such as antisense RNA species and promoter-upstream transcripts (PROMPTs), and of mRNAs with processing …

**Summary**, from NCBI Gene [51010](https://www.ncbi.nlm.nih.gov/gene/51010):

> This gene encodes a non-catalytic component of the human exosome, a complex with 3'-5' exoribonuclease activity that plays a role in numerous RNA processing and degradation activities. Related pseudogenes of this gene are found on chromosome 19 and 21. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:17944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17944) · Entrez [51010](https://www.ncbi.nlm.nih.gov/gene/51010) · UniProt [Q9NQT5](https://www.uniprot.org/uniprotkb/Q9NQT5) · Ensembl [ENSG00000107371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107371)

## Data

Gene col 2848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2848); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2848]; `tensor/DDL_lfc|DDL_z.npy` [2848]; `embed/gene_vectors.npy` [2848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2848 or target_col == 2848). Every well: [[EXOSC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOSC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

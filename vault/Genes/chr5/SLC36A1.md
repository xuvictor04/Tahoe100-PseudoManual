---
symbol: "SLC36A1"
type: "gene"
col: 4453
ensembl_id: "ENSG00000123643"
name: "solute carrier family 36 member 1"
location: "5q33.1"
module: 65
arm: "-"
pooled_cpm: 8.3
n_lines_expressing: 50
n_dd_up: 44
n_dd_down: 1
n_dd_up_clean: 33
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# SLC36A1

*solute carrier family 36 member 1* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.16× (z +19.4, q 0e+00, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Bosentan (hydrate) (drug)]] 5 µM: 0.712× (z -4.1, q 0.023, down in 12 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.165×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.266×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.175×; ⚠ cell-cycle shift, explains ~41% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEPD]] (+0.60, fdr 2e-05), [[PEA15]] (+0.59, fdr 1e-05), [[PVR]] (+0.56, fdr 1e-05); moves opposite to [[MED26]] (-0.57, fdr 4e-05), [[PDXDC2P]] (-0.54, fdr 3e-05), [[TXNDC11]] (-0.54, fdr 7e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4453.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.16×** | +19.4 | 0e+00 | 41/43 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.30×** | +18.3 | 0e+00 | 43/47 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.14×** | +17.8 | 0e+00 | 45/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.44×** | +15.5 | 0e+00 | 44/47 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.68×** | +12.3 | 7e-33 | 39/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.46×** | +11.3 | 1e-27 | 32/41 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +9.9 | 4e-21 | 32/44 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **2.15×** | +9.2 | 2e-18 | 24/34 (HT-29, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +9.0 | 2e-17 | 34/45 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.93×** | +8.2 | 1e-14 | 32/47 (NCI-H460, HEC-1-A, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.91×** | +8.1 | 3e-14 | 24/43 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.83×** | +7.6 | 2e-12 | 31/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +7.6 | 2e-12 | 25/47 (LOX-IMVI, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +7.1 | 4e-11 | 23/48 (A-172, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +7.1 | 5e-11 | 27/48 (SW1417, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +6.8 | 4e-10 | 26/47 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.80×** | +6.7 | 5e-10 | 26/47 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +6.0 | 7e-08 | 21/47 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4453.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.165×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.266×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.175×; ⚠ cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.712×** | -4.1 | 0.023 | 12/40 (J82, SNU-1, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.771× | -3.2 | 0.46 | 6/47 (SW 900, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.66 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +19.5) | — |
| [[PANC-1 (line)]] | alt | 7.91 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +11.5) | — |
| [[A-172 (line)]] | wt | 15.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +14.3) | — |
| [[LoVo (line)]] | wt | 11.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.70× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 12.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +8.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -9.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A-427 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 10.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.40× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 3.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +8.6) | — |
| [[J82 (line)]] | alt | 7.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 2.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 3.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 8.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +9.9) | — |
| [[SW480 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A498 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEPD]] | +0.60 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[PEA15]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PVR]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[COA7]] | +0.56 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[WSB2]] | +0.56 | +0.53 / +0.26 | both halves | 4e-04 |  |
| [[PSEN2]] | +0.56 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[GNPDA1]] | +0.55 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ZBTB40]] | +0.55 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[VAC14]] | +0.55 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[OSTM1]] | +0.54 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[TNFRSF12A]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[SLC25A13]] | +0.54 | +0.60 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED26]] | -0.57 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[PDXDC2P]] | -0.54 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[TXNDC11]] | -0.54 | -0.66 / -0.37 | both halves | 7e-05 |  |
| [[KMT5C]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[CNOT8]] | -0.53 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[SEC31A]] | -0.52 | -0.64 / -0.38 | both halves | 7e-05 |  |
| [[GMCL1]] | -0.51 | -0.64 / -0.38 | both halves | 7e-05 |  |
| [[OXNAD1]] | -0.51 | -0.56 / -0.29 | both halves | 3e-04 |  |
| [[APAF1]] | -0.51 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[PRRC1]] | -0.51 | -0.67 / -0.25 | both halves | 4e-04 |  |
| [[CNOT6L]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[SPICE1]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC36A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.407). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (19.4, -12.7); signed map (-6.0, 24.4). **Vector** length 58.9, 9.07% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.9 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +3.8 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +7.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +5.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.4 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.3 | +17.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.2 | +15.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.0 | -0.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 36 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:151,437,046-151,492,379 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LYAAT-1, PAT1, TRAMD3 |
| Gene groups (HGNC) | Solute carrier family 36 |
| Reactome | 4 pathways, smallest: Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z2H8](https://www.uniprot.org/uniprotkb/Q7Z2H8) (Proton-coupled amino acid transporter 1):

> Electrogenic proton/amino acid symporter with selectivity for small apolar L-amino acids, their D-enantiomers and selected amino acid derivatives such as 4-aminobutanoate/GABA. May be involved in the efflux from the lysosomal compartment of neutral amino acids resulting from proteolysis (By similarity). May play a role in specifying sites for exocytosis in neurons (By similarity).

**Summary**, from NCBI Gene [206358](https://www.ncbi.nlm.nih.gov/gene/206358):

> This gene encodes a member of the eukaryote-specific amino acid/auxin permease (AAAP) 1 transporter family. The encoded protein functions as a proton-dependent, small amino acid transporter. This gene is clustered with related family members on chromosome 5q33.1. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:18761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18761) · Entrez [206358](https://www.ncbi.nlm.nih.gov/gene/206358) · UniProt [Q7Z2H8](https://www.uniprot.org/uniprotkb/Q7Z2H8) · Ensembl [ENSG00000123643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123643)

## Data

Gene col 4453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4453); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4453]; `tensor/DDL_lfc|DDL_z.npy` [4453]; `embed/gene_vectors.npy` [4453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4453 or target_col == 4453). Every well: [[SLC36A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC36A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "AMMECR1"
type: "gene"
col: 2190
ensembl_id: "ENSG00000101935"
name: "AMMECR nuclear protein 1"
location: "Xq23"
module: 137
arm: "+"
pooled_cpm: 48.24
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# AMMECR1

*AMMECR nuclear protein 1* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.22× (z +5.6, q 1e-05, up in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.17× (z +4.5, q 0.001, up in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (NCI-H2347 1.95×; ⚠ cell-cycle shift, explains ~52% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.517× (z -13.1, q 3e-36, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP5M1]] (+0.63, fdr 2e-05), [[NSUN3]] (+0.60, fdr 3e-05), [[MTMR2]] (+0.56, fdr 1e-04); moves opposite to [[DNAAF3]] (-0.62, fdr 5e-05), [[SH2B2]] (-0.61, fdr 4e-05), [[GMCL1]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2190.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (NCI-H2347 1.95×; ⚠ cell-cycle shift, explains ~52% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.22×** | +5.6 | 1e-05 | 23/48 (NCI-H2347, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.6 | 0.001 | 21/46 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.5 | 0.001 | 17/48 (SW1417, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.003 | 19/48 (C32, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.012 | 16/48 (HOP62, J82, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +3.7 | 0.024 | 17/48 (BT-474, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.17× | +3.2 | 0.11 | 8/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.14 | 17/47 (HT-29, A498, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.14 | 14/48 (C32, NCI-H460, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2190.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.517×** | -13.1 | 3e-36 | 43/48 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.600×** | -10.1 | 1e-21 | 40/48 (SW480, KATO III, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.686×** | -7.5 | 2e-11 | 32/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -7.1 | 2e-10 | 33/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.734×** | -6.1 | 1e-07 | 28/47 (PANC-1, SW480, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.765×** | -4.6 | 4e-04 | 21/48 (A549, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.796×** | -4.5 | 5e-04 | 22/48 (KATO III, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.785×** | -4.2 | 0.002 | 18/46 (A-427, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | 0.838× | -3.5 | 0.029 | 20/47 (PANC-1, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.884× | -3.5 | 0.032 | 9/48 (H4, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.847× | -3.3 | 0.052 | 18/48 (SW480, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.893× | -3.2 | 0.074 | 11/48 (hTERT-HPNE, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 84.6 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -16.0) |
| [[KATO III (line)]] | alt | 58.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.395× (z -9.8) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.395× (z -9.8) |
| [[A-427 (line)]] | wt | 46.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -22.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 56.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.435× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 43.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 71.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.383× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 81.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.431× (z -9.8) |
| [[BT-474 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.288× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HEC-1-A (line)]] | alt | 40.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -12.2) |
| [[HOP62 (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 32.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 33.3 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.95× (z +9.5) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[NCI-H460 (line)]] | wt | 71.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.404× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 57.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -10.5) |
| [[SNU-423 (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP5M1]] | +0.63 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[NSUN3]] | +0.60 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[MTMR2]] | +0.56 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[ST7]] | +0.56 | +0.44 / +0.34 | both halves | 1e-04 |  |
| [[FZD6]] | +0.55 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[POGLUT1]] | +0.55 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[CLHC1]] | +0.55 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[GCFC2]] | +0.55 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[DNAJC11]] | +0.55 | +0.50 / +0.37 | both halves | 9e-05 |  |
| [[GTF3C6]] | +0.54 | +0.36 / +0.32 | both halves | 2e-04 |  |
| [[ECHDC1]] | +0.54 | +0.36 / +0.40 | both halves | 1e-04 |  |
| [[ZNF346]] | +0.54 | +0.46 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF3]] | -0.62 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[SH2B2]] | -0.61 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[GMCL1]] | -0.59 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[PLA2G15]] | -0.59 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[CARHSP1]] | -0.59 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[EFNA3]] | -0.59 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[MOSPD3]] | -0.58 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[EFNA4]] | -0.57 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[SPSB3]] | -0.56 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[MTMR14]] | -0.55 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[MPND]] | -0.54 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[CBFA2T2]] | -0.54 | -0.46 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises AMMECR1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.7, -2.6); signed map (19.8, -30.2). **Vector** length 94.9, 20.5% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.9 | +3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +1.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.2 | -10.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.1 | -13.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -3.3 | -2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Silodosin (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | AMMECR nuclear protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq23 — chrX:110,194,186-110,440,318 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

UniProt [Q9Y4X0](https://www.uniprot.org/uniprotkb/Q9Y4X0) carries no function annotation.

**Summary**, from NCBI Gene [9949](https://www.ncbi.nlm.nih.gov/gene/9949):

> The exact function of this gene is not known, however, submicroscopic deletion of the X chromosome including this gene, COL4A5, and FACL4 genes, result in a contiguous gene deletion syndrome, the AMME complex (Alport syndrome, mental retardation, midface hypoplasia, and elliptocytosis). Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:467) · Entrez [9949](https://www.ncbi.nlm.nih.gov/gene/9949) · UniProt [Q9Y4X0](https://www.uniprot.org/uniprotkb/Q9Y4X0) · Ensembl [ENSG00000101935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101935)

## Data

Gene col 2190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2190); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2190]; `tensor/DDL_lfc|DDL_z.npy` [2190]; `embed/gene_vectors.npy` [2190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2190 or target_col == 2190). Every well: [[AMMECR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMMECR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

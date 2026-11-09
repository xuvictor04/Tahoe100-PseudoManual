---
symbol: "DCTN3"
type: "gene"
col: 5967
ensembl_id: "ENSG00000137100"
name: "dynactin subunit 3"
location: "9p13.3"
module: 24
arm: "+"
pooled_cpm: 13.41
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# DCTN3

*dynactin subunit 3* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.42× (z +9.7, q 2e-19, up in 35 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.64× (z +3.9, q 0.007, up in 28 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 4.87×, A498 4.43×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 4.50×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.528× (z -5.1, q 2e-04, down in 31 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.726× (z -3.6, q 0.087, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.136×; ⚠ cell-cycle shift, explains ~89% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.161×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Hydroxyurea (drug)]] 5 µM in 1 line (CHP-212 0.0520×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2J]] (+0.71, fdr 7e-06, ⚠ POLR2J in the vector space only through flagged drug-doses), [[IFT22]] (+0.70, fdr 7e-06), [[NUDT16L1]] (+0.69, fdr 1e-05), [[PIN1]] (+0.67, fdr 3e-05); moves opposite to [[BEND3]] (-0.60, fdr 3e-05), [[LINC01357]] (-0.59, fdr 1e-05), [[DDX21]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IFI27L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5967.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 4.87×, A498 4.43×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 4.50×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.42×** | +9.7 | 2e-19 | 35/37 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.97×** | +8.3 | 4e-14 | 23/25 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **2.08×** | +5.8 | 2e-06 | 31/44 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.03×** | +5.6 | 3e-06 | 37/48 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.00×** | +5.1 | 5e-05 | 24/32 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.87×** | +4.9 | 8e-05 | 38/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.76×** | +4.5 | 6e-04 | 35/47 (PANC-1, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +3.9 | 0.007 | 28/45 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.54×** | +3.3 | 0.072 | 15/47 (NCI-H23, LS 180, …) | rises with dose | composition shift; position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.33×** | +3.2 | 0.089 | 15/48 (SK-MEL-2, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5967.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.136×; ⚠ cell-cycle shift, explains ~89% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.161×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Hydroxyurea (drug)]] 5 µM in 1 line (CHP-212 0.0520×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.528×** | -5.1 | 2e-04 | 31/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.726×** | -3.6 | 0.087 | 20/48 (A-172, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.663× | -3.3 | 0.20 | 15/48 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.71 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.43× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[BT-474 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.161× (z -8.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 1 | — | [[Hydroxyurea (drug)]] 5 µM 0.0520× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -9.7) ⚠ cell-cycle shift, explains ~89% of this change |
| [[PANC-1 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.50× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW480 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 12 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2J]] ⚠ | +0.71 | +0.64 / +0.67 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; ⚠ in the vector space only through flagged drug-doses |
| [[IFT22]] | +0.70 | +0.59 / +0.66 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium |
| [[NUDT16L1]] | +0.69 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[PIN1]] | +0.67 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[ISCA2]] | +0.66 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[MORN2]] | +0.64 | +0.58 / +0.74 | both halves | 8e-06 |  |
| [[BAD]] | +0.64 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[RNF5]] | +0.63 | +0.48 / +0.69 | both halves | 2e-05 | pathway: Asparagine N-linked glycosylation |
| [[BLOC1S1]] | +0.62 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[GABARAP]] ⚠ | +0.62 | +0.60 / +0.60 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ARID4A]] | +0.60 | +0.40 / +0.70 | both halves | 5e-05 |  |
| [[ASB8]] | +0.60 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[DNAL4]] | +0.59 | +0.46 / +0.74 | both halves | 3e-05 |  |
| [[TMEM205]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEND3]] | -0.60 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[LINC01357]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[DDX21]] | -0.59 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[RCC1]] | -0.58 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[MRPS25]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[KCTD15]] | -0.56 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[SNHG16]] | -0.56 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[EPM2A]] | -0.56 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[EEF1AKMT1]] | -0.56 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[NCR3LG1]] | -0.56 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[GABPB1-AS1]] | -0.55 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[SLC9B2]] | -0.55 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI27L2]] | B | IFI27L2 activity raises DCTN3's level | lines that do not express IFI27L2 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without IFI27L2 | 0.031 | ⚠ within organs, on part of the lines |
| [[HDAC6]] | B | HDAC6 activity lowers DCTN3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.9, -13.9); signed map (-11.0, -2.3). **Vector** length 60.4, 13.4% of its response variance represented; |z| ≥ 3 in 530 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.4 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.1 | +3.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.0 | +5.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.0 | +4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.0 | +0.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | dynactin subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,613,545-34,620,523 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DCTN-22 |
| Gene groups (HGNC) | Dynactin subunits |
| Reactome | 34 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; Loss of Nlp from mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [O75935](https://www.uniprot.org/uniprotkb/O75935) (Dynactin subunit 3):

> Part of the dynactin complex that activates the molecular motor dynein for ultra-processive transport along microtubules (By similarity). Together with dynein may be involved in spindle assembly and cytokinesis.

**Summary**, from NCBI Gene [11258](https://www.ncbi.nlm.nih.gov/gene/11258):

> This gene encodes the smallest subunit of dynactin, a macromolecular complex consisting of 10 subunits ranging in size from 22 to 150 kD. Dynactin binds to both microtubules and cytoplasmic dynein. It is involved in a diverse array of cellular functions, including ER-to-Golgi transport, the centripetal movement of lysosomes and endosomes, spindle formation, cytokinesis, chromosome movement, nuclear positioning, and axonogenesis. This subunit, like most other dynactin subunits, exists only as a …

**Accessions** — [HGNC:2713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2713) · Entrez [11258](https://www.ncbi.nlm.nih.gov/gene/11258) · UniProt [O75935](https://www.uniprot.org/uniprotkb/O75935) · Ensembl [ENSG00000137100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137100)

## Data

Gene col 5967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5967); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5967]; `tensor/DDL_lfc|DDL_z.npy` [5967]; `embed/gene_vectors.npy` [5967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5967 or target_col == 5967). Every well: [[DCTN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCTN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

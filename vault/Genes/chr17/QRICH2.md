---
symbol: "QRICH2"
type: "gene"
col: 4993
ensembl_id: "ENSG00000129646"
name: "glutamine rich 2"
location: "17q25.1"
module: 38
arm: "+"
pooled_cpm: 5.42
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# QRICH2

*glutamine rich 2* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.25× (z +18.9, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.545× (z -4.9, q 5e-04, down in 22 of 46 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (HOP62 0.0558×, HepG2/C3A 0.119×; ⚠ cell-cycle shift, explains ~41% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.114×; ⚠ cell-cycle shift, explains ~46% of this change); [[Aprepitant (drug)]] 0.05 µM in 1 line (KATO III 0.0499×); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.114×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (A-427 0.0531×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GARIN1A]] (+0.75, fdr 7e-06), [[ANKDD1B]] (+0.74, fdr 9e-06), [[MYH3]] (+0.74, fdr 7e-06); moves opposite to [[PEX2]] (-0.63, fdr 7e-06), [[MRPS31P4]] (-0.62, fdr 2e-05), [[ATG4C]] (-0.61, fdr 3e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.25×** | +18.9 | 0e+00 | 40/40 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.79×** | +10.3 | 2e-22 | 35/38 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +8.0 | 3e-13 | 5/10 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +6.9 | 9e-10 | 25/38 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +6.3 | 4e-08 | 14/26 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +5.2 | 1e-05 | 2/14 (A-172, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.57×** | +5.1 | 3e-05 | 21/41 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +4.9 | 6e-05 | 18/46 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.6 | 3e-04 | 19/46 (HOP62, A498, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.018 | 14/46 (LoVo, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.019 | 13/38 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.022 | 6/46 (HOP62, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +3.1 | 0.078 | 9/45 (C-33 A, KATO III, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.48×** | +3.1 | 0.078 | 9/44 (PANC-1, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4993.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (HOP62 0.0558×, HepG2/C3A 0.119×; ⚠ cell-cycle shift, explains ~41% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.114×; ⚠ cell-cycle shift, explains ~46% of this change); [[Aprepitant (drug)]] 0.05 µM in 1 line (KATO III 0.0499×); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.114×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (A-427 0.0531×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.545×** | -4.9 | 5e-04 | 22/46 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.558×** | -4.7 | 5e-04 | 23/45 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.561×** | -4.7 | 5e-04 | 22/38 (SNU-423, HepG2/C3A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.612×** | -4.0 | 0.009 | 18/45 (H4, MIA PaCa-2, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.645×** | -3.6 | 0.039 | 20/44 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.653×** | -3.3 | 0.078 | 13/33 (HepG2/C3A, LOX-IMVI, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.486× | -3.1 | 0.18 | 13/44 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 2 (1 ⚠) | — | [[Bestatin (drug)]] 0.05 µM 0.0986× (z -8.5) |
| [[HOP62 (line)]] | alt | 6.21 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0558× (z -11.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[LoVo (line)]] | wt | 5.95 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.114× (z -9.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[NCI-H23 (line)]] | alt | 8.55 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.114× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 3.59 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.88× (z +13.1) | — |
| [[A-172 (line)]] | wt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -8.9) |
| [[A-427 (line)]] | wt | 4.57 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0531× (z -8.9) |
| [[A498 (line)]] | wt | 8.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +8.8) | — |
| [[A549 (line)]] | wt | 4.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.91× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 2.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.58× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 4.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.68× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 2.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +8.9) | — |
| [[KATO III (line)]] | alt | 4.61 | 0 | 1 | — | [[Aprepitant (drug)]] 0.05 µM 0.0499× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 4.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.01× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 2.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.21× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 3.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.74× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 5.62 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0678× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 3.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.68× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 7.30 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0886× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 5.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.28× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARIN1A]] | +0.75 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.74 | +0.83 / +0.57 | both halves | 9e-06 |  |
| [[MYH3]] | +0.74 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[TRPV1]] | +0.74 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[SLC23A3]] | +0.73 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[PRC1-AS1]] | +0.72 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[SLC7A9]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.71 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[PSMG3-AS1]] | +0.70 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.70 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[MFSD2B]] | +0.70 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[LINC01588]] | +0.70 | +0.73 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX2]] | -0.63 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[MRPS31P4]] | -0.62 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[ATG4C]] | -0.61 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers QRICH2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PRDX2]] | B | PRDX2 activity lowers QRICH2's level | lines that do not express PRDX2 (9) vs lines expressing it (41) | 1.40× higher at baseline in the lines without PRDX2 | 0.088 | ⚠ within organs, on part of the lines; also absent: RAB20 |
| [[SLC26A4]] | B | SLC26A4 activity raises QRICH2's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without SLC26A4 | 0.099 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.6, -15.0); signed map (15.1, 3.1). **Vector** length 75.4, 13.2% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +18.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.0 | +1.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +0.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -0.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | glutamine rich 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,274,049-76,308,276 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434P0316 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0J4](https://www.uniprot.org/uniprotkb/Q9H0J4) (Glutamine-rich protein 2):

> Has an essential role in the formation of sperm flagella and flagellar structure maintainance. It acts as a suppressor of ubiquitination and degradation of proteins involved in flagellar development and motility.

**Summary**, from NCBI Gene [84074](https://www.ncbi.nlm.nih.gov/gene/84074):

> Involved in flagellated sperm motility and negative regulation of ubiquitin-dependent protein catabolic process. Located in sperm flagellum. Implicated in spermatogenic failure 35. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25326) · Entrez [84074](https://www.ncbi.nlm.nih.gov/gene/84074) · UniProt [Q9H0J4](https://www.uniprot.org/uniprotkb/Q9H0J4) · Ensembl [ENSG00000129646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129646)

## Data

Gene col 4993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4993); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4993]; `tensor/DDL_lfc|DDL_z.npy` [4993]; `embed/gene_vectors.npy` [4993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4993 or target_col == 4993). Every well: [[QRICH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QRICH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

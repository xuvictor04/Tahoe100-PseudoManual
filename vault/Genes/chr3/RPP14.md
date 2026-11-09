---
symbol: "RPP14"
type: "gene"
col: 8753
ensembl_id: "ENSG00000163684"
name: "ribonuclease P/MRP subunit p14"
location: "3p14.3"
module: 156
arm: "+"
pooled_cpm: 26.99
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# RPP14

*ribonuclease P/MRP subunit p14* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.69× (z +10.1, q 2e-21, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.586× (z -10.4, q 2e-22, down in 28 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.794× (z -4.2, q 0.002, down in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HCT15 0.105×, HT-29 0.123×, HEC-1-A 0.277×, LoVo 0.295×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SK-MEL-2 0.137×, LS 180 0.197×, HOP62 0.208×, HEC-1-A 0.344×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.109×, HCT15 0.173×, C32 0.158×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.303×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF557]] (+0.80, fdr 7e-06), [[ZNF75A]] (+0.74, fdr 7e-06), [[KTI12]] (+0.74, fdr 7e-06); moves opposite to [[VAMP1]] (-0.61, fdr 1e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WHRN]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8753.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +10.1 | 2e-21 | 34/47 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +7.4 | 3e-11 | 30/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +6.8 | 2e-09 | 4/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.8 | 8e-07 | 26/46 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +5.2 | 2e-05 | 20/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | **1.21×** | +5.1 | 3e-05 | 19/48 (NCI-H2347, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +4.4 | 7e-04 | 20/48 (SW480, A549, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 9e-04 | 12/47 (NCI-H2347, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.004 | 15/45 (LS 180, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.005 | 16/48 (HEC-1-A, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.005 | 11/47 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.005 | 14/48 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.006 | 16/47 (Hs 766T, COLO 205, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.023 | 12/47 (SW480, RKO, …) | all doses, flat | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.050 | 4/46 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.064 | 8/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.069 | 2/48 (AsPC-1, HCT15) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8753.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HCT15 0.105×, HT-29 0.123×, HEC-1-A 0.277×, LoVo 0.295×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (SK-MEL-2 0.137×, LS 180 0.197×, HOP62 0.208×, HEC-1-A 0.344×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.109×, HCT15 0.173×, C32 0.158×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.303×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.586×** | -10.4 | 2e-22 | 28/44 (HCT15, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.652×** | -7.7 | 5e-12 | 28/41 (SK-MEL-2, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.667×** | -7.4 | 2e-11 | 19/34 (LoVo, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -6.1 | 2e-07 | 24/47 (A549, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -4.2 | 0.002 | 19/47 (SNU-423, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.814×** | -3.8 | 0.014 | 22/48 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.872× | -3.7 | 0.015 | 15/48 (A-172, RPMI-7951, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.854× | -3.0 | 0.16 | 7/48 (J82, A549, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 43.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 21.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.370× (z -9.5) ⚠ cell-cycle shift, explains ~1% of this change |
| [[C32 (line)]] | wt | 22.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -11.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 46.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -16.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 27.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -12.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 43.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -22.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -11.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0996× (z -11.7) ⚠ toxic |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -15.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -9.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -13.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -10.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -15.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 36.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF557]] | +0.80 | +0.83 / +0.78 | both halves | 7e-06 |  |
| [[ZNF75A]] | +0.74 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[KTI12]] | +0.74 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[ZNF3]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[LLPH]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[MRM2]] | +0.73 | +0.72 / +0.74 | both halves | 7e-06 | pathway: rRNA processing |
| [[ALKBH1]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[FAF2]] | +0.73 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[ISG20L2]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol |
| [[TRIM4]] | +0.71 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[ZNF146]] | +0.71 | +0.63 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAMP1]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WHRN]] | C | WHRN activity raises RPP14's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.15× lower at baseline in the lines without WHRN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.3, 3.2); signed map (-4.8, -15.3). **Vector** length 91.6, 18.7% of its response variance represented; |z| ≥ 3 in 776 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +5.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +3.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.2 | -7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -3.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -0.2 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease P/MRP subunit p14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:58,306,245-58,324,695 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P14 |
| Gene groups (HGNC) | Nuclear RNase P complex subunits; RNase MRP complex subunits |
| Reactome | 6 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Major pathway of rRNA processing in the nucleolus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [O95059](https://www.uniprot.org/uniprotkb/O95059) (Ribonuclease P protein subunit p14):

> Component of ribonuclease P, a ribonucleoprotein complex that generates mature tRNA molecules by cleaving their 5'-ends.

**Summary**, from NCBI Gene [11102](https://www.ncbi.nlm.nih.gov/gene/11102):

> This gene encodes a subunit of ribonuclease P and has 3' to 5' exoribonuclease activity. Transcripts for this gene are bicistronic and include a conserved downstream open reading frame for the hydroxyacyl-thioester dehydratase type 2 (HTD2) gene. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:30327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30327) · Entrez [11102](https://www.ncbi.nlm.nih.gov/gene/11102) · UniProt [O95059](https://www.uniprot.org/uniprotkb/O95059) · Ensembl [ENSG00000163684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163684)

## Data

Gene col 8753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8753); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8753]; `tensor/DDL_lfc|DDL_z.npy` [8753]; `embed/gene_vectors.npy` [8753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8753 or target_col == 8753). Every well: [[RPP14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPP14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "VWCE"
type: "gene"
col: 9573
ensembl_id: "ENSG00000167992"
name: "von Willebrand factor C and EGF domains"
location: "11q12.2"
module: 38
arm: "+"
pooled_cpm: 8.18
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# VWCE

*von Willebrand factor C and EGF domains* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.19× (z +13.5, q 2e-38, up in 43 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.467× (z -6.3, q 1e-07, down in 26 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.467× (z -6.3, q 1e-07, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PYGM]] (+0.88, fdr 7e-06), [[COL20A1]] (+0.86, fdr 7e-06), [[HPX]] (+0.83, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TAF13]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9573.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.19×** | +13.5 | 2e-38 | 43/44 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.41×** | +7.2 | 1e-10 | 29/45 (SW480, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +6.3 | 4e-08 | 29/44 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +5.3 | 2e-05 | 26/43 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.75×** | +4.4 | 0.001 | 15/36 (NCI-H460, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.013 | 18/47 (A-172, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.58×** | +3.7 | 0.013 | 18/47 (A-172, PANC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +3.7 | 0.013 | 11/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.036 | 13/47 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.46× | +3.1 | 0.12 | 13/46 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 1.44× | +3.0 | 0.14 | 8/46 (KATO III, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9573.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.467×** | -6.3 | 1e-07 | 26/44 (RPMI-7951, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.467×** | -6.3 | 1e-07 | 27/47 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.502×** | -5.7 | 2e-06 | 27/46 (SW1417, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.541×** | -5.1 | 6e-05 | 24/45 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.552×** | -4.9 | 1e-04 | 21/46 (H4, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.539×** | -4.8 | 1e-04 | 22/45 (SW 900, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | **0.695×** | -4.3 | 0.002 | 25/47 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.610×** | -4.1 | 0.003 | 18/46 (J82, RPMI-7951, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.620×** | -4.0 | 0.005 | 19/48 (AsPC-1, NCI-H2030, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.405×** | -3.9 | 0.006 | 13/41 (SW 900, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.622×** | -3.8 | 0.008 | 19/46 (H4, AsPC-1, …) | two highest doses | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.636×** | -3.6 | 0.015 | 18/45 (LoVo, J82, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.654×** | -3.5 | 0.019 | 21/47 (A498, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | **0.660×** | -3.4 | 0.026 | 12/48 (HCT15, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.670×** | -3.3 | 0.035 | 15/47 (NCI-H2030, AsPC-1, …) | top dose only | position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **0.668×** | -3.2 | 0.045 | 19/45 (RKO, HOP62, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.761×** | -3.2 | 0.045 | 12/48 (BT-474, SW 1088, …) | top dose only |  |
| [[Radotinib (drug)]] 0.5 µM |  | **0.686×** | -3.1 | 0.057 | 12/44 (SW1417, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9573. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 11.1 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +8.5) | [[Digitoxin (drug)]] 0.05 µM 0.0350× (z -10.9) |
| [[H4 (line)]] | wt | 38.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.123× (z -10.1) |
| [[KATO III (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -9.7) |
| [[LoVo (line)]] | wt | 15.2 | 0 | 2 (1 ⚠) | — | [[Belumosudil (drug)]] 5 µM 0.0977× (z -9.4) |
| [[RKO (line)]] | wt | 9.18 | 0 | 2 (1 ⚠) | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0637× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0719× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0902× (z -9.0) |
| [[A-427 (line)]] | wt | 15.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -9.3) |
| [[A549 (line)]] | wt | 5.74 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0714× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 6.84 | 0 | 1 | — | [[Radotinib (drug)]] 5 µM 0.163× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0722× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 6.44 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0710× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 4.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.82× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 2.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 3.87 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM 0.0422× (z -9.2) |
| [[A-172 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9573), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYGM]] | +0.88 | +0.87 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[COL20A1]] | +0.86 | +0.87 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[HPX]] | +0.83 | +0.78 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[SMIM41]] | +0.81 | +0.80 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[IDI2-AS1]] | +0.79 | +0.77 / +0.81 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[PILRA]] | +0.78 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.78 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[ISY1-RAB43]] | +0.77 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[PHYHD1]] | +0.77 | +0.72 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers VWCE's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[XG]] | B | XG activity raises VWCE's level | lines that do not express XG (5) vs lines expressing it (45) | 1.74× lower at baseline in the lines without XG | 0.079 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TAF13]] | C | VWCE's natural level weakens TAF13's drug response | VWCE's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.17; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.883). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.2, -18.4); signed map (14.2, 12.0). **Vector** length 111, 27.0% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +13.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +2.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.8 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.7 | -5.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -4.5 | -4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.5 | -4.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.9 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | von Willebrand factor C and EGF domains |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,258,286-61,295,316 (-) |
| Ensembl biotype | protein_coding |
| Also known as | URG11, FLJ32009, VWC1 |
| Gene groups (HGNC) | Cysteine rich transmembrane BMP regulators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DN2](https://www.uniprot.org/uniprotkb/Q96DN2) (von Willebrand factor C and EGF domain-containing protein):

> May be a regulatory element in the beta-catenin signaling pathway and a target for chemoprevention of hapatocellular carcinoma.

**Summary**, from NCBI Gene [220001](https://www.ncbi.nlm.nih.gov/gene/220001):

> Predicted to enable calcium ion binding activity. Predicted to be involved in cellular response to virus. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26487](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26487) · Entrez [220001](https://www.ncbi.nlm.nih.gov/gene/220001) · UniProt [Q96DN2](https://www.uniprot.org/uniprotkb/Q96DN2) · Ensembl [ENSG00000167992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167992)

## Data

Gene col 9573: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9573); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9573, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9573]; `tensor/DDL_lfc|DDL_z.npy` [9573]; `embed/gene_vectors.npy` [9573]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9573 or target_col == 9573). Every well: [[VWCE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VWCE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

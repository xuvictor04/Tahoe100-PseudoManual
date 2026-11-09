---
symbol: "FAM221A"
type: "gene"
col: 12043
ensembl_id: "ENSG00000188732"
name: "family with sequence similarity 221 member A"
location: "7p15.3"
module: 55
arm: "+"
pooled_cpm: 5.41
n_lines_expressing: 37
n_dd_up: 25
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# FAM221A

*family with sequence similarity 221 member A* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.31× (z +11.7, q 1e-28, up in 22 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.426× (z -11.9, q 7e-30, down in 21 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNE3]] (+0.64, fdr 7e-06), [[SLC27A2]] (+0.63, fdr 1e-05), [[FUT2]] (+0.61, fdr 1e-05); moves opposite to [[PDK1-AS1]] (-0.57, fdr 2e-05), [[ANXA2R-OT1]] (-0.53, fdr 8e-05), [[PCNT]] (-0.50, fdr 5e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[PIK3C2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12043.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +11.7 | 1e-28 | 22/34 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.24×** | +11.3 | 5e-27 | 21/34 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +10.0 | 3e-21 | 19/33 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.88×** | +8.8 | 2e-16 | 15/34 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +7.0 | 3e-10 | 10/34 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +6.3 | 4e-08 | 10/32 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +5.8 | 5e-07 | 13/34 (NCI-H460, SW 900, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +5.7 | 6e-07 | 2/11 (LS 180, J82) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.6 | 2e-06 | 9/19 (SHP-77, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +5.0 | 3e-05 | 6/19 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.0 | 3e-05 | 3/9 (HT-29, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.001 | 4/34 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.2 | 0.001 | 5/28 (A-172, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.001 | 11/26 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.002 | 10/29 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.002 | 4/32 (Panc 03.27, SW48, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +3.6 | 0.009 | 1/33 (PANC-1) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.031 | 4/34 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.036 | 1/26 (SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.044 | 2/27 (J82, HT-29) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12043.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.426×** | -11.9 | 7e-30 | 21/34 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.431×** | -11.7 | 2e-29 | 22/32 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.466×** | -10.7 | 3e-24 | 21/33 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.565×** | -8.0 | 2e-13 | 15/27 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.632×** | -6.4 | 2e-08 | 13/32 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -4.0 | 0.005 | 6/35 (J82, RKO, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.761×** | -3.8 | 0.011 | 7/34 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.767×** | -3.7 | 0.015 | 8/32 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.784×** | -3.3 | 0.069 | 1/34 (SW480) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.798× | -3.0 | 0.14 | 6/26 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.28 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0704× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -13.3) |
| [[HT-29 (line)]] | alt | 20.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.256× (z -8.8) |
| [[KATO III (line)]] | alt | 26.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW1417 (line)]] | alt | 5.37 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0912× (z -10.1) |
| [[COLO 205 (line)]] | alt | 8.28 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0429× (z -11.0) |
| [[LoVo (line)]] | wt | 6.37 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0762× (z -14.0) |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.655 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNE3]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SLC27A2]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[FUT2]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[LINC01012]] | +0.60 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[DDX19B]] | +0.60 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[CLRN3]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[FGD3]] | +0.58 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[SULT1C2]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[KCTD14]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[USH1C]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[BBS5]] | +0.55 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[CYP2S1]] | +0.55 | +0.57 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK1-AS1]] | -0.57 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ANXA2R-OT1]] | -0.53 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[PCNT]] | -0.50 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[TPTE2]] | -0.48 | -0.43 / -0.26 | both halves | 4e-04 |  |
| [[IBA57]] | -0.48 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[MZF1]] | -0.48 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[ATXN1L]] | -0.48 | -0.24 / -0.48 | both halves | 4e-04 |  |
| [[LINC00910]] | -0.47 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[PKNOX1]] | -0.47 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[SLC35F5]] | -0.47 | -0.36 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3C2B]] | B | FAM221A activity raises PIK3C2B's level | lines that do not express FAM221A (13) vs lines expressing it (37) | 2.34× lower at baseline in the lines without FAM221A | 0.012 | ⚠ within organs, on part of the lines; also absent: TRIM2, MICE |
| [[GALM]] | B | FAM221A activity weakens GALM's drug response | lines that do not express FAM221A (9) vs lines expressing it (28) | the lines without FAM221A respond 0.91× as strongly (z diff +0.48); strongest at Panobinostat 5 µM: 3.88x vs 2.59x (z diff -1.7) | 0.058 | ⚠ within organs, on part of the lines; also absent: TRIM2, MICE; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.1, 44.5); signed map (59.9, 13.4). **Vector** length 48.3, 7.24% of its response variance represented; |z| ≥ 3 in 718 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.8 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +5.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.9 | +4.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +1.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.0 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -10.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -11.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -11.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.0 | -8.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.8 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 221 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:23,680,130-23,703,249 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ45875, MGC72075, DKFZp686F0810; previously C7orf46 |
| Matched by | ensembl_id |

UniProt [A4D161](https://www.uniprot.org/uniprotkb/A4D161) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27977](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27977) · Entrez [340277](https://www.ncbi.nlm.nih.gov/gene/340277) · UniProt [A4D161](https://www.uniprot.org/uniprotkb/A4D161) · Ensembl [ENSG00000188732](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188732)

## Data

Gene col 12043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12043); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12043]; `tensor/DDL_lfc|DDL_z.npy` [12043]; `embed/gene_vectors.npy` [12043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12043 or target_col == 12043). Every well: [[FAM221A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM221A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

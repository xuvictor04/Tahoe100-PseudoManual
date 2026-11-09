---
symbol: "EDC3"
type: "gene"
col: 11005
ensembl_id: "ENSG00000179151"
name: "enhancer of mRNA decapping 3"
location: "15q24.1"
module: 52
arm: "+"
pooled_cpm: 35.39
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# EDC3

*enhancer of mRNA decapping 3* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 5.10× (z +13.4, q 2e-38, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.628× (z -10.4, q 1e-22, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXRED1]] (+0.69, fdr 7e-06), [[ZNF408]] (+0.68, fdr 7e-06), [[ZNF417]] (+0.65, fdr 7e-06); moves opposite to [[PTPRJ]] (-0.55, fdr 3e-05), [[EPS15]] (-0.51, fdr 5e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF229]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11005.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.10×** | +13.4 | 2e-38 | 44/48 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.98×** | +9.0 | 6e-17 | 36/47 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +7.0 | 5e-10 | 4/48 (A549, BT-474, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +5.2 | 2e-05 | 27/46 (SK-MEL-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.004 | 22/46 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.007 | 23/47 (HCT15, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11005.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -10.4 | 1e-22 | 39/47 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.552×** | -9.0 | 5e-17 | 29/38 (A549, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -7.5 | 9e-12 | 30/47 (HOP62, RKO, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.615×** | -7.4 | 2e-11 | 34/47 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.637×** | -7.1 | 1e-10 | 29/46 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.756×** | -6.3 | 4e-08 | 32/47 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.675×** | -6.2 | 4e-08 | 29/47 (A498, PANC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.700×** | -5.6 | 1e-06 | 28/47 (J82, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.735×** | -4.9 | 7e-05 | 22/47 (A498, SW1417, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.724×** | -4.7 | 1e-04 | 23/42 (C32, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.773×** | -4.1 | 0.002 | 23/47 (SW1417, AsPC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.786×** | -3.8 | 0.007 | 21/47 (BT-474, SW 1088, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.798×** | -3.4 | 0.026 | 21/46 (SNU-423, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11005. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 52.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.88× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[LS 180 (line)]] | wt | 33.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.2) | — |
| [[NCI-H2347 (line)]] | alt | 36.8 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -13.8) |
| [[RKO (line)]] | wt | 34.4 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 7.82× (z +8.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -13.5) |
| [[A-172 (line)]] | wt | 28.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -11.8) |
| [[COLO 205 (line)]] | alt | 32.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 34.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.73× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 32.8 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 45.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.0× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H23 (line)]] | alt | 35.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -9.5) |
| [[SW1417 (line)]] | alt | 36.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -9.3) |
| [[SW480 (line)]] | alt | 35.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.47× (z +10.6) | — |
| [[A-427 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 45.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -15.6) |
| [[A549 (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 36.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -12.5) |
| [[C32 (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[CHP-212 (line)]] | wt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[H4 (line)]] | wt | 60.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -9.4) |
| [[HCT15 (line)]] | alt | 51.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HS-578T (line)]] | alt | 27.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H460 (line)]] | wt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.386× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 36.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.65× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 58.4 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -9.0) |
| [[SHP-77 (line)]] | alt | 41.5 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.281× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 47.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.242× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[AN3 CA (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11005), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXRED1]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[ZNF408]] | +0.68 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ZNF417]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[DIABLO]] | +0.64 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[WDR24]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PES1]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SART1]] | +0.62 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[PRPF6]] | +0.62 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[SEC23IP]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[STK19]] | +0.62 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[MTERF4]] | +0.62 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[RNF40]] | +0.62 | +0.60 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRJ]] | -0.55 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[EPS15]] | -0.51 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF229]] | B | ZNF229 activity raises EDC3's level | lines that do not express ZNF229 (25) vs lines expressing it (25) | 1.28× lower at baseline in the lines without ZNF229 | 0.028 | ⚠ within organs, on part of the lines; also absent: CACNA2D1, STAC, C15orf48 |
| [[TOP2A]] | B | TOP2A activity raises EDC3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.512). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-35.3, -4.1); signed map (-11.9, -24.9). **Vector** length 88.3, 19.6% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.7 | +13.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | -0.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | -4.5 | -3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -7.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | enhancer of mRNA decapping 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:74,630,558-74,696,292 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21128, hYjeF_N2-15q23, YJEFN2, LSM16; previously YJDC |
| Gene groups (HGNC) | RNA decapping and exonuclease complex subunits |
| Reactome | 3 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Deadenylation-dependent mRNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96F86](https://www.uniprot.org/uniprotkb/Q96F86) (Enhancer of mRNA-decapping protein 3):

> Binds single-stranded RNA. Involved in the process of mRNA degradation and in the positive regulation of mRNA decapping. May play a role in spermiogenesis and oogenesis.

**Summary**, from NCBI Gene [80153](https://www.ncbi.nlm.nih.gov/gene/80153):

> This gene encodes a protein that is important in mRNA degradation. The encoded protein is a component of a decapping complex that promotes efficient removal of the monomethylguanosine (m7G) cap from mRNAs, as part of the 5' to 3' mRNA decay pathway. Mutations in this gene have been identified in human patients with an autosomal recessive form of intellectual disability. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:26114](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26114) · Entrez [80153](https://www.ncbi.nlm.nih.gov/gene/80153) · UniProt [Q96F86](https://www.uniprot.org/uniprotkb/Q96F86) · Ensembl [ENSG00000179151](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179151)

## Data

Gene col 11005: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11005); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11005, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11005]; `tensor/DDL_lfc|DDL_z.npy` [11005]; `embed/gene_vectors.npy` [11005]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11005 or target_col == 11005). Every well: [[EDC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

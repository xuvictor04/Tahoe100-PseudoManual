---
symbol: "GALNT13"
type: "gene"
col: 6860
ensembl_id: "ENSG00000144278"
name: "polypeptide N-acetylgalactosaminyltransferase 13"
location: "2q23.3-q24.1"
module: 9
arm: "+"
pooled_cpm: 66.16
n_lines_expressing: 19
n_dd_up: 28
n_dd_down: 13
n_dd_up_clean: 22
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# GALNT13

*polypeptide N-acetylgalactosaminyltransferase 13* — 2q23.3-q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +15.8, q 0e+00, up in 3 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.542× (z -5.1, q 2e-04, down in 16 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD8]] (+0.66, fdr 7e-06), [[SNCA]] (+0.66, fdr 7e-06), [[LINC02864]] (+0.63, fdr 2e-05); moves opposite to [[ARHGAP1]] (-0.45, fdr 5e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FSTL5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6860.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +15.8 | 0e+00 | 3/18 (A-427, H4, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +11.9 | 3e-30 | 0/18 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +9.6 | 1e-19 | 10/17 (NCI-H2030, NCI-H2347, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +6.4 | 3e-08 | 14/17 (HOP62, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.1 | 1e-07 | 1/19 (H4) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +6.1 | 1e-07 | 9/18 (NCI-H2030, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.9 | 3e-07 | 2/15 (HS-578T, CHP-212) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +5.7 | 1e-06 | 2/17 (NCI-H2030, HOP62) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +5.4 | 4e-06 | 7/17 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.4 | 4e-06 | 13/15 (HOP62, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.55×** | +5.0 | 3e-05 | 11/18 (HOP62, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 3e-05 | 0/18 | two highest doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +4.8 | 8e-05 | 13/17 (H4, LOX-IMVI, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.4 | 4e-04 | 2/17 (H4, SW 900) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.32×** | +4.4 | 5e-04 | 0/18 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 6e-04 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.3 | 6e-04 | 13/17 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.002 | 0/17 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6860.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.542×** | -5.1 | 2e-04 | 16/18 (LOX-IMVI, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.756×** | -4.1 | 0.012 | 0/17 | inconsistent across doses |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.777×** | -4.0 | 0.012 | 0/17 | inconsistent across doses |  |
| [[Phenytoin (sodium) (drug)]] 0.5 µM |  | **0.782×** | -3.9 | 0.013 | 0/17 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.784×** | -3.9 | 0.013 | 0/17 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -3.8 | 0.016 | 1/19 (NCI-H2122) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.650×** | -3.6 | 0.029 | 6/17 (NCI-H2030, NCI-H23, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.797×** | -3.3 | 0.064 | 0/17 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.801×** | -3.2 | 0.075 | 0/17 | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.754×** | -3.2 | 0.084 | 0/17 | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.761×** | -3.1 | 0.099 | 0/17 | inconsistent across doses | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.823×** | -3.1 | 0.099 | 0/17 | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.825×** | -3.0 | 0.099 | 5/17 (SHP-77, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lapatinib ditosylate (drug)]] 0.5 µM |  | **0.764×** | -3.0 | 0.099 | 0/17 | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 25.6 | 6 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.39× (z +13.4) | — |
| [[HOP62 (line)]] | alt | 81.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +17.8) | — |
| [[LOX-IMVI (line)]] | wt | 245 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.147× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 149 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0852× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.338× (z -14.7) |
| [[J82 (line)]] | alt | 94.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 425 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -19.9) |
| [[NCI-H2347 (line)]] | alt | 41.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 437 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.245× (z -8.5) |
| [[A549 (line)]] | wt | 160 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.2) |
| [[CHP-212 (line)]] | wt | 49.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0891× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.346× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[SHP-77 (line)]] | alt | 264 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.6) | — |
| [[A-172 (line)]] | wt | 8.64 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.66 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.64 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.38 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.00 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.65 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.03 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.41 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.67 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.97 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.69 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.18 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.08 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.99 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD8]] | +0.66 | +0.58 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SNCA]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[LINC02864]] | +0.63 | +0.48 / +0.63 | both halves | 2e-05 | **novel candidate** |
| [[MARCHF1]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[RBM20]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[LINGO2]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[ASXL3]] | +0.57 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[KHDRBS2]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[KCNJ6]] | +0.56 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[CACNB2]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[AUTS2]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[NOVA1]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP1]] | -0.45 | -0.51 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSTL5]] | B | FSTL5 activity lowers GALNT13's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 1.33× higher at baseline in the lines without FSTL5 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.3, 35.5); signed map (40.6, 37.9). **Vector** length 65.1, 20.2% of its response variance represented; |z| ≥ 3 in 525 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +4.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.7 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -3.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3-q24.1 — chr2:153,871,922-154,453,979 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1918, GalNAc-T13 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUC8](https://www.uniprot.org/uniprotkb/Q8IUC8) (Polypeptide N-acetylgalactosaminyltransferase 13):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine (GalNAc) residue from UDP-GalNAc to a serine or threonine residue on the protein receptor. Generates GalNAc-O-Ser/Thr structure also known as Tn antigen, which itself is immunogenic but also serves as a precursor for the synthesis of different mucin-type O-glycan core structures. Contributes to the synthesis of O-linked glycans on mucins and proteoglycans of the central nervous …

**Summary**, from NCBI Gene [114805](https://www.ncbi.nlm.nih.gov/gene/114805):

> The GALNT13 protein is a member of the UDP-N-acetyl-alpha-D-galactosamine:polypeptide N-acetylgalactosaminyltransferase (GalNAcT; EC 2.4.1.41) family, which initiate O-linked glycosylation of mucins (see MUC3A, MIM 158371) by the initial transfer of N-acetylgalactosamine (GalNAc) with an alpha-linkage to a serine or threonine residue.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:23242](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23242) · Entrez [114805](https://www.ncbi.nlm.nih.gov/gene/114805) · UniProt [Q8IUC8](https://www.uniprot.org/uniprotkb/Q8IUC8) · Ensembl [ENSG00000144278](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144278)

## Data

Gene col 6860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6860); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6860]; `tensor/DDL_lfc|DDL_z.npy` [6860]; `embed/gene_vectors.npy` [6860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6860 or target_col == 6860). Every well: [[GALNT13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

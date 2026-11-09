---
symbol: "PLXNB3"
type: "gene"
col: 12667
ensembl_id: "ENSG00000198753"
name: "plexin B3"
location: "Xq28"
module: 143
arm: "+"
pooled_cpm: 4.1
n_lines_expressing: 40
n_dd_up: 0
n_dd_down: 31
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# PLXNB3

*plexin B3* — Xq28

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.432× (z -7.4, q 7e-11, down in 24 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX41]] (+0.60, fdr 7e-06), [[ZNF17]] (+0.59, fdr 1e-05), [[DLST]] (+0.56, fdr 1e-05); moves opposite to [[FOXP1]] (-0.59, fdr 1e-05), [[ERBIN]] (-0.56, fdr 4e-05), [[ATXN7L1]] (-0.54, fdr 6e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[PPFIA4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12667.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.432×** | -7.4 | 7e-11 | 24/29 (SK-MEL-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.258×** | -7.0 | 7e-10 | 27/34 (NCI-H1792, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.396×** | -5.8 | 1e-06 | 23/37 (A-172, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.525×** | -5.7 | 2e-06 | 21/30 (A-172, CFPAC-1, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.427×** | -5.3 | 1e-05 | 18/35 (AsPC-1, KATO III, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.433×** | -5.2 | 1e-05 | 23/35 (A-172, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.424×** | -5.2 | 1e-05 | 18/35 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.367×** | -5.2 | 2e-05 | 20/30 (SK-MEL-2, SNU-423, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.442×** | -5.1 | 2e-05 | 21/30 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.450×** | -5.0 | 3e-05 | 22/38 (HOP62, BT-474, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.465×** | -4.8 | 9e-05 | 17/23 (HOP62, HS-578T, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **0.478×** | -4.5 | 3e-04 | 15/20 (SK-MEL-2, NCI-H1792, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.490×** | -4.5 | 4e-04 | 20/35 (A-172, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.506×** | -4.3 | 8e-04 | 18/32 (H4, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.501×** | -4.0 | 0.002 | 9/14 (NCI-H1792, HS-578T, …) | all doses, flat | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.537×** | -3.9 | 0.004 | 15/33 (C32, HS-578T, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.572×** | -3.5 | 0.014 | 15/33 (C32, SNU-423, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.575×** | -3.5 | 0.014 | 16/33 (SW480, H4, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.575×** | -3.4 | 0.018 | 13/35 (A549, SW480, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.580×** | -3.2 | 0.029 | 15/32 (SW 900, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -3.2 | 0.029 | 11/36 (SNU-423, A-427, …) | rises with dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.603×** | -3.2 | 0.032 | 14/35 (BT-474, H4, …) | top dose only |  |
| [[Neratinib (drug)]] 0.05 µM |  | **0.625×** | -2.9 | 0.066 | 11/30 (H4, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.571×** | -2.9 | 0.074 | 8/32 (LOX-IMVI, CFPAC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.628×** | -2.8 | 0.083 | 7/34 (H4, RPMI-7951, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.72 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -11.6) |
| [[A-172 (line)]] | wt | 20.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0737× (z -11.7) |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0317× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 4.80 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -10.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H1792 (line)]] | alt | 5.84 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 3.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0572× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 7.42 | 0 | 1 | — | [[Saquinavir (drug)]] 5 µM 0.118× (z -9.0) |
| [[A-427 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.860 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX41]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ZNF17]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[DLST]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[APBB3]] | +0.55 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[SARDH]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[MAN1B1]] | +0.54 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[ABHD17A]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ZNF70]] | +0.52 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[CSPG4]] | +0.52 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[EOLA1]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CACNB1]] | +0.51 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[OSBPL7]] | +0.51 | +0.64 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXP1]] | -0.59 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ERBIN]] | -0.56 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[ATXN7L1]] | -0.54 | -0.65 / -0.39 | both halves | 6e-05 |  |
| [[EIF4G3]] | -0.54 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[SRGAP1]] | -0.53 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[NFE2L2]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ZNF609]] | -0.52 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[PARD3]] | -0.51 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[STAU2]] | -0.50 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[NFIB]] | -0.48 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[JMJD1C]] | -0.47 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[NUTM2B-AS1]] | -0.47 | -0.56 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPFIA4]] | B | PLXNB3 activity raises PPFIA4's level | lines that do not express PLXNB3 (10) vs lines expressing it (40) | 1.82× lower at baseline in the lines without PLXNB3 | 0.051 | ⚠ within organs, on part of the lines |
| [[RALGAPA1]] | B | PLXNB3 activity lowers RALGAPA1's level | lines that do not express PLXNB3 (10) vs lines expressing it (40) | 1.70× higher at baseline in the lines without PLXNB3 | 0.061 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction -0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.6, -8.2); signed map (-43.4, -27.5). **Vector** length 61.0, 11.7% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.7 | +0.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +1.9 | -4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | +1.8 | -3.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.3 | -0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | +1.3 | -4.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.0 | +2.0 |
|  | [[Roxadustat (drug)]] 5 µM |  | +0.9 | +2.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +0.8 | +1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +0.8 | +0.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.5 | -4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.2 | -5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -2.0 | -5.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -2.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | plexin B3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,764,196-153,779,346 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PLEXR, PLEXB3; previously PLXN6 |
| Gene groups (HGNC) | Plexins; IPT domain containing |
| Reactome | 4 pathways, smallest: Other semaphorin interactions; Semaphorin interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULL4](https://www.uniprot.org/uniprotkb/Q9ULL4) (Plexin-B3):

> Receptor for SEMA5A that plays a role in axon guidance, invasive growth and cell migration. Stimulates neurite outgrowth and mediates Ca(2+)/Mg(2+)-dependent cell aggregation. In glioma cells, SEMA5A stimulation of PLXNB3 results in the disassembly of F-actin stress fibers, disruption of focal adhesions and cellular collapse as well as inhibition of cell migration and invasion through ARHGDIA-mediated inactivation of RAC1.

**Summary**, from NCBI Gene [5365](https://www.ncbi.nlm.nih.gov/gene/5365):

> The protein encoded by this gene is a member of the plexin family. It functions as a receptor for semaphorin 5A, and plays a role in axon guidance, invasive growth and cell migration. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:9105](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9105) · Entrez [5365](https://www.ncbi.nlm.nih.gov/gene/5365) · UniProt [Q9ULL4](https://www.uniprot.org/uniprotkb/Q9ULL4) · Ensembl [ENSG00000198753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198753)

## Data

Gene col 12667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12667); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12667]; `tensor/DDL_lfc|DDL_z.npy` [12667]; `embed/gene_vectors.npy` [12667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12667 or target_col == 12667). Every well: [[PLXNB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLXNB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

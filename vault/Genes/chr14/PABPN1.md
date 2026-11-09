---
symbol: "PABPN1"
type: "gene"
col: 2030
ensembl_id: "ENSG00000100836"
name: "poly(A) binding protein nuclear 1"
location: "14q11.2"
module: 21
arm: "+"
pooled_cpm: 120.77
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PABPN1

*poly(A) binding protein nuclear 1* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.35× (z +10.5, q 5e-23, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.81× (z +5.1, q 3e-05, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNISR]] (+0.73, fdr 7e-06), [[LUC7L3]] (+0.69, fdr 7e-06), [[MRPL33]] (+0.65, fdr 7e-06); moves opposite to [[GPS1]] (-0.65, fdr 1e-05), [[EIF2S1]] (-0.61, fdr 1e-05), [[MLX]] (-0.61, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2030.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.35×** | +10.5 | 5e-23 | 49/49 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +7.9 | 9e-13 | 44/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.26×** | +7.1 | 3e-10 | 47/48 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +6.8 | 2e-09 | 45/47 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +6.2 | 6e-08 | 42/45 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +5.1 | 3e-05 | 44/48 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.65×** | +4.4 | 0.001 | 38/48 (NCI-H460, NCI-H2030, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.62×** | +4.2 | 0.002 | 41/48 (HOP62, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.53×** | +3.6 | 0.022 | 37/47 (LoVo, PANC-1, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.022 | 45/48 (HT-29, HOP62, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.49×** | +3.5 | 0.026 | 36/48 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.026 | 29/49 (HS-578T, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.081 | 41/49 (NCI-H661, HCT15, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.86×** | +3.1 | 0.081 | 41/48 (COLO 205, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2030.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.467× | -3.4 | 0.32 | 40/49 (SK-MEL-2, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2030. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 93.5 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.70× (z +9.7) ⚠ toxic | — |
| [[HOP62 (line)]] | alt | 81.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +10.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 117 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 86.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 161 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 75.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 95.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 142 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 95.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 85.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 116 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +10.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 74.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +10.7) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 119 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 167 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 135 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 72.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 85.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 142 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 135 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +10.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 174 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 141 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.02× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[Panc 03.27 (line)]] | alt | 129 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 145 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 146 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 241 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 94.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 107 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 101 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 149 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2030), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[LUC7L3]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MRPL33]] | +0.65 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[NAA38]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[VAMP2]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MAFG]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[YBEY]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[RENO1]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[C1orf56]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[HOTAIRM1]] | +0.59 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | +0.58 | +0.57 / +0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF358]] | +0.58 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[TMEM91]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPS1]] | -0.65 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[EIF2S1]] | -0.61 | -0.51 / -0.66 | both halves | 1e-05 | STRING 678 |
| [[MLX]] | -0.61 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[PHB1]] | -0.61 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[TINF2]] | -0.61 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PRELID3B]] | -0.60 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[DPM2]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[TUBG1]] | -0.58 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[AP2M1]] | -0.58 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[CCT7]] | -0.57 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[BCS1L]] | -0.57 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[PRPS1]] | -0.56 | -0.49 / -0.67 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.513). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.3, -4.6); signed map (-6.4, 2.2). **Vector** length 84.5, 37.3% of its response variance represented; |z| ≥ 3 in 674 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.7 | +7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.9 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.6 | +4.4 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.6 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.4 | +0.8 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.4 | -0.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +2.3 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.1 | +7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.1 | +0.0 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -0.2 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | poly(A) binding protein nuclear 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,321,457-23,326,163 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAB2; previously OPMD, PABP2 |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 15 pathways, smallest: Z-decay: degradation of maternal mRNAs by zygotically expressed factors; Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86U42](https://www.uniprot.org/uniprotkb/Q86U42) (Polyadenylate-binding protein 2):

> Involved in the 3'-end formation of mRNA precursors (pre-mRNA) by the addition of a poly(A) tail of 200-250 nt to the upstream cleavage product (By similarity). Stimulates poly(A) polymerase (PAPOLA) conferring processivity on the poly(A) tail elongation reaction and also controls the poly(A) tail length (By similarity). Increases the affinity of poly(A) polymerase for RNA (By similarity). Is also present at various stages of mRNA metabolism including nucleocytoplasmic trafficking and …

**Summary**, from NCBI Gene [8106](https://www.ncbi.nlm.nih.gov/gene/8106):

> This gene encodes an abundant nuclear protein that binds with high affinity to nascent poly(A) tails. The protein is required for progressive and efficient polymerization of poly(A) tails at the 3' ends of eukaryotic transcripts and controls the size of the poly(A) tail to about 250 nt. At steady-state, this protein is localized in the nucleus whereas a different poly(A) binding protein is localized in the cytoplasm. This gene contains a GCG trinucleotide repeat at the 5' end of the coding …

**Accessions** — [HGNC:8565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8565) · Entrez [8106](https://www.ncbi.nlm.nih.gov/gene/8106) · UniProt [Q86U42](https://www.uniprot.org/uniprotkb/Q86U42) · Ensembl [ENSG00000100836](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100836)

## Data

Gene col 2030: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2030); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2030, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2030]; `tensor/DDL_lfc|DDL_z.npy` [2030]; `embed/gene_vectors.npy` [2030]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2030 or target_col == 2030). Every well: [[PABPN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PABPN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

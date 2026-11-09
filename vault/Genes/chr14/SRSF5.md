---
symbol: "SRSF5"
type: "gene"
col: 2009
ensembl_id: "ENSG00000100650"
name: "serine and arginine rich splicing factor 5"
location: "14q24"
module: 15
arm: "+"
pooled_cpm: 95.12
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SRSF5

*serine and arginine rich splicing factor 5* — 14q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.88× (z +11.5, q 5e-28, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.484× (z -13.3, q 7e-38, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT2E-AS1]] (+0.71, fdr 2e-05), [[SLC25A53]] (+0.70, fdr 1e-05), [[CCNT2-AS1]] (+0.70, fdr 1e-05); moves opposite to [[GPATCH11]] (-0.63, fdr 3e-05), [[METTL5]] (-0.62, fdr 2e-05), [[PUSL1]] (-0.60, fdr 2e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2009.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.88×** | +11.5 | 5e-28 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +11.1 | 2e-26 | 44/49 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +9.8 | 2e-20 | 41/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +8.7 | 5e-16 | 39/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +8.2 | 3e-14 | 38/48 (RKO, C32, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.9 | 5e-10 | 37/50 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +5.9 | 2e-07 | 32/45 (PANC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +5.9 | 2e-07 | 29/49 (A-427, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +5.9 | 3e-07 | 30/48 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +5.6 | 1e-06 | 34/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.6 | 1e-06 | 31/48 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +5.1 | 2e-05 | 26/44 (A-427, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.0 | 3e-05 | 29/48 (HOP62, A-172, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | **1.27×** | +4.4 | 4e-04 | 29/48 (LOX-IMVI, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.1 | 0.002 | 25/47 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.012 | 21/48 (H4, HOP62, …) | two highest doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.062 | 13/48 (KATO III, LS 180, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2009.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.484×** | -13.3 | 7e-38 | 47/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.550×** | -11.0 | 1e-25 | 43/48 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.574×** | -10.2 | 4e-22 | 45/48 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.606×** | -9.2 | 5e-18 | 45/48 (SW480, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.607×** | -9.2 | 5e-18 | 44/48 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.730×** | -5.8 | 6e-07 | 30/48 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.548×** | -5.8 | 6e-07 | 40/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.772×** | -4.0 | 0.004 | 31/49 (NCI-H2122, NCI-H2347, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.845× | -3.6 | 0.018 | 13/48 (RKO, SW480, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.040 | 22/48 (LoVo, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2009. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 73.1 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.54× (z +15.6) | — |
| [[KATO III (line)]] | alt | 89.6 | 5 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +14.8) | [[Belinostat (drug)]] 5 µM 0.456× (z -9.0) |
| [[SW480 (line)]] | alt | 133 | 3 (1 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +13.3) | [[Belinostat (drug)]] 5 µM 0.422× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 156 | 3 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +13.5) | [[Belinostat (drug)]] 5 µM 0.378× (z -12.0) |
| [[LoVo (line)]] | wt | 135 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +14.3) | [[Harringtonine (drug)]] 0.5 µM 0.455× (z -9.8) |
| [[HOP62 (line)]] | alt | 90.2 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.3) | [[Belinostat (drug)]] 5 µM 0.365× (z -11.2) |
| [[HS-578T (line)]] | alt | 60.5 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.1) | [[Belinostat (drug)]] 5 µM 0.392× (z -8.9) |
| [[SW1417 (line)]] | alt | 95.1 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +10.2) | [[Belinostat (drug)]] 0.5 µM 0.440× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 81.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 125 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.311× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 82.9 | 2 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.417× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 101 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +13.0) | — |
| [[NCI-H1792 (line)]] | alt | 70.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.354× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 145 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 162 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0938× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.384× (z -10.1) |
| [[A-427 (line)]] | wt | 90.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +11.5) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 60.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +13.4) | — |
| [[HCT15 (line)]] | alt | 124 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.372× (z -9.5) |
| [[LS 180 (line)]] | wt | 102 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +14.8) | — |
| [[NCI-H2347 (line)]] | alt | 101 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +8.9) | — |
| [[RKO (line)]] | wt | 90.5 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.80× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 74.4 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +12.9) | — |
| [[SNU-1 (line)]] | wt | 122 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.387× (z -8.8) |
| [[BT-474 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.23× (z +8.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 124 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.423× (z -9.0) |
| [[Hs 766T (line)]] | wt | 87.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 131 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.438× (z -9.4) |
| [[PANC-1 (line)]] | alt | 54.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.46× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 117 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.398× (z -8.9) |
| [[SW48 (line)]] | wt | 97.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +8.5) | — |
| [[A-172 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 89.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 103 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 84.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 90.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2009), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2E-AS1]] | +0.71 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[SLC25A53]] | +0.70 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[CCNT2-AS1]] | +0.70 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[PCED1A]] | +0.68 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[ARGLU1]] | +0.67 | +0.42 / +0.58 | both halves | 4e-05 | STRING 505 |
| [[PIPOX]] | +0.66 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ATXN1L]] | +0.65 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[AHSA2P]] | +0.65 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[CD27-AS1]] | +0.63 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[PBLD]] | +0.63 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[ARSD]] | +0.63 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[GTF3C2-AS2]] | +0.62 | +0.42 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH11]] | -0.63 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[METTL5]] | -0.62 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[PUSL1]] | -0.60 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[COMMD2]] | -0.59 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[ISCA2]] | -0.59 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[TAMM41]] | -0.59 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[MRPL17]] | -0.59 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[MRPS34]] | -0.58 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[POLR2I]] | -0.58 | -0.43 / -0.37 | both halves | 8e-05 | pathway: Dengue Virus-Host Interactions |
| [[PUS3]] | -0.57 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[NDUFA8]] | -0.57 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[RHOT1]] | -0.56 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SRSF5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises SRSF5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-1.6, 22.5); signed map (19.6, -3.1). **Vector** length 134, 43.5% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +11.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.2 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.3 | +3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +8.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +3.0 | +0.5 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +2.6 | +0.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.8 | -5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -8.1 | -13.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.3 | -9.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | -2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.7 | -11.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.9 | -5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | +0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.9 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.0 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine rich splicing factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24 — chr14:69,726,900-69,772,005 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRP40, HRS; previously SFRS5 |
| Gene groups (HGNC) | RNA binding motif containing; Serine and arginine rich splicing factors |
| Reactome | 11 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13243](https://www.uniprot.org/uniprotkb/Q13243) (Serine/arginine-rich splicing factor 5):

> Plays a role in constitutive splicing and can modulate the selection of alternative splice sites.

**Summary**, from NCBI Gene [6430](https://www.ncbi.nlm.nih.gov/gene/6430):

> The protein encoded by this gene is a member of the serine/arginine (SR)-rich family of pre-mRNA splicing factors, which constitute part of the spliceosome. Each of these factors contains an RNA recognition motif (RRM) for binding RNA and an RS domain for binding other proteins. The RS domain is rich in serine and arginine residues and facilitates interaction between different SR splicing factors. In addition to being critical for mRNA splicing, the SR proteins have also been shown to be …

**Accessions** — [HGNC:10787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10787) · Entrez [6430](https://www.ncbi.nlm.nih.gov/gene/6430) · UniProt [Q13243](https://www.uniprot.org/uniprotkb/Q13243) · Ensembl [ENSG00000100650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100650)

## Data

Gene col 2009: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2009); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2009, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2009]; `tensor/DDL_lfc|DDL_z.npy` [2009]; `embed/gene_vectors.npy` [2009]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2009 or target_col == 2009). Every well: [[SRSF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRSF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

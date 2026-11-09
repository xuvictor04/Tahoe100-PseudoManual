---
symbol: "C2orf92"
type: "gene"
col: 13650
ensembl_id: "ENSG00000228486"
name: "chromosome 2 open reading frame 92"
location: "2q11.2"
module: 80
arm: "+"
pooled_cpm: 14.62
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 13
direction_downstream: 1
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# C2orf92

*chromosome 2 open reading frame 92* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.00× (z +22.7, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.400× (z -10.6, q 2e-23, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPO9-AS1]] (+0.74, fdr 7e-06), [[WNK4]] (+0.73, fdr 7e-06), [[ACTR3-AS1]] (+0.68, fdr 1e-05); moves opposite to [[PTGES2]] (-0.58, fdr 6e-05), [[FYCO1]] (-0.56, fdr 1e-05), [[SOAT1]] (-0.55, fdr 3e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[APCDD1L]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FYCO1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13650.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.00×** | +22.7 | 0e+00 | 41/42 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +9.9 | 8e-21 | 29/43 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +6.9 | 1e-09 | 21/39 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.1 | 5e-05 | 17/41 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +4.6 | 6e-04 | 20/44 (MIA PaCa-2, A498, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.008 | 11/43 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.8 | 0.011 | 6/22 (SW1417, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.014 | 14/44 (SW480, PANC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.049 | 10/45 (LoVo, SW48, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.049 | 10/42 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13650.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.400×** | -10.6 | 2e-23 | 36/45 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.468×** | -8.8 | 4e-16 | 26/40 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.480×** | -8.5 | 4e-15 | 30/44 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.485×** | -8.4 | 8e-15 | 29/44 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.489×** | -8.3 | 1e-14 | 29/43 (HOP62, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.514×** | -7.7 | 1e-12 | 28/45 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.587×** | -5.8 | 5e-07 | 27/42 (HOP62, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.646×** | -5.0 | 3e-05 | 20/45 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.644×** | -4.9 | 6e-05 | 22/38 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.666×** | -4.7 | 1e-04 | 22/45 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.708×** | -4.0 | 0.003 | 15/43 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -4.0 | 0.004 | 17/44 (H4, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.727×** | -3.7 | 0.010 | 12/45 (SNU-1, C32, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.745×** | -3.4 | 0.026 | 12/39 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.577×** | -3.3 | 0.033 | 10/24 (NCI-H1573, A-172, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.578×** | -3.3 | 0.033 | 11/39 (SNU-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.765×** | -3.0 | 0.089 | 7/42 (hTERT-HPNE, NCI-H23, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.834× | -3.0 | 0.089 | 10/45 (NCI-H460, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 83.8 | 0 | 16 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0568× (z -18.0) |
| [[H4 (line)]] | wt | 59.4 | 0 | 10 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0514× (z -14.7) |
| [[RPMI-7951 (line)]] | alt | 49.6 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.151× (z -12.2) |
| [[J82 (line)]] | alt | 24.8 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0786× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.139× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 18.2 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.100× (z -11.6) |
| [[PANC-1 (line)]] | alt | 9.42 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +14.4) | [[Digitoxin (drug)]] 5 µM 0.209× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -10.1) |
| [[RKO (line)]] | wt | 18.6 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +8.7) | [[Canagliflozin (drug)]] 5 µM 0.0498× (z -14.0) |
| [[SNU-423 (line)]] | alt | 25.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0804× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0964× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 20.0 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.0865× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.144× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 17.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.118× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 9.27 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +8.8) | [[Bortezomib (drug)]] 0.05 µM 0.0818× (z -9.4) |
| [[SW480 (line)]] | alt | 9.12 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.91× (z +15.4) | — |
| [[A-172 (line)]] | wt | 40.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -9.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 5.02 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.20× (z +9.8) | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0688× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 25.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0653× (z -11.6) |
| [[LoVo (line)]] | wt | 8.39 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +13.0) | — |
| [[LS 180 (line)]] | wt | 4.46 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +12.4) | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0773× (z -9.2) |
| [[SNU-1 (line)]] | wt | 48.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.255× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.177× (z -9.0) |
| [[SW 900 (line)]] | alt | 12.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.0841× (z -11.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 6.09 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0850× (z -9.0) |
| [[A498 (line)]] | wt | 7.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +13.9) | — |
| [[A549 (line)]] | wt | 6.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.69× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +14.2) | — |
| [[HT-29 (line)]] | alt | 4.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.45× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 3.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 7.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.48× (z +12.5) | — |
| [[SW48 (line)]] | wt | 7.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.89× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9-AS1]] | +0.74 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[WNK4]] | +0.73 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[ACTR3-AS1]] | +0.68 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[MSANTD3-TMEFF1]] | +0.64 | +0.71 / +0.35 | both halves | 1e-04 |  |
| [[LPXN]] | +0.63 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[TGIF2-RAB5IF]] | +0.63 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | +0.62 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[LINC01500]] | +0.62 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[ZNF425]] | +0.62 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | +0.62 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[SPAG5-AS1]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[RPSAP52]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGES2]] | -0.58 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[FYCO1]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[SOAT1]] | -0.55 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[NAA40]] | -0.54 | -0.51 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APCDD1L]] | B | APCDD1L activity raises C2orf92's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.44× lower at baseline in the lines without APCDD1L | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[TOP2A]] | B | TOP2A activity lowers C2orf92's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises C2orf92's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.13× lower at baseline in the lines without APCDD1L-DT | 0.024 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[DOCK2]] | B | DOCK2 activity raises C2orf92's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without DOCK2 | 0.039 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent |
| [[CDH13]] | B | CDH13 activity raises C2orf92's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 1.87× lower at baseline in the lines without CDH13 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[SLC26A4]] | B | SLC26A4 activity raises C2orf92's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 2.41× lower at baseline in the lines without SLC26A4 | 0.046 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[DENND2A]] | B | DENND2A activity raises C2orf92's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.90× lower at baseline in the lines without DENND2A | 0.067 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[CYGB]] | B | CYGB activity raises C2orf92's level | lines that do not express CYGB (20) vs lines expressing it (30) | 1.74× lower at baseline in the lines without CYGB | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000269547, RNF175, FBXO17; maybe low, not absent |
| [[FRMD4A]] | B | FRMD4A activity raises C2orf92's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 1.74× lower at baseline in the lines without FRMD4A | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[ADAMTS18]] | B | ADAMTS18 activity raises C2orf92's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 1.83× lower at baseline in the lines without ADAMTS18 | 0.079 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent |
| [[IQCJ-SCHIP1]] | B | IQCJ-SCHIP1 activity raises C2orf92's level | lines that do not express IQCJ-SCHIP1 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without IQCJ-SCHIP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SCHIP1, ENSG00000281091, NPL; maybe low, not absent; its own permutation p |
| [[GDNF-AS1]] | B | GDNF-AS1 activity raises C2orf92's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without GDNF-AS1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FYCO1]] | C | C2orf92 activity raises FYCO1's level | lines that do not express C2orf92 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without C2orf92 | 0.065 | ⚠ few lines (3 vs 47); across organs; also absent: HHAT, TBCEL, RUNDC3A-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.0, -6.3); signed map (25.8, 9.0). **Vector** length 107, 26.5% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +22.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +2.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.4 | +0.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.0 | -8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -8.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.2 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 2 open reading frame 92 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:97,664,217-97,703,066 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LINC01125 |
| Matched by | ensembl_id |

UniProt [A0A1B0GVN3](https://www.uniprot.org/uniprotkb/A0A1B0GVN3) carries no function annotation.

**Summary**, from NCBI Gene [728537](https://www.ncbi.nlm.nih.gov/gene/728537):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:49272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49272) · Entrez [728537](https://www.ncbi.nlm.nih.gov/gene/728537) · UniProt [A0A1B0GVN3](https://www.uniprot.org/uniprotkb/A0A1B0GVN3) · Ensembl [ENSG00000228486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228486)

## Data

Gene col 13650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13650); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13650]; `tensor/DDL_lfc|DDL_z.npy` [13650]; `embed/gene_vectors.npy` [13650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13650 or target_col == 13650). Every well: [[C2orf92 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2orf92.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

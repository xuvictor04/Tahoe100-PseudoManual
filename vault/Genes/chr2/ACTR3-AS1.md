---
symbol: "ACTR3-AS1"
type: "gene"
col: 13679
ensembl_id: "ENSG00000228857"
name: "ACTR3 antisense RNA 1"
location: "2q14.1"
module: 35
arm: "+"
pooled_cpm: 19.26
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 28
n_dd_up_clean: 7
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 9
direction_downstream: 13
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ACTR3-AS1

*ACTR3 antisense RNA 1* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.26× (z +22.5, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.276× (z -14.1, q 1e-42, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSK3B-DT]] (+0.80, fdr 7e-06), [[LINC01191]] (+0.77, fdr 7e-06), [[PCBP1-AS1]] (+0.77, fdr 3e-05); moves opposite to [[NAA40]] (-0.66, fdr 1e-05), [[MAST3]] (-0.64, fdr 2e-04), [[NDRG3]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[AOX1]] → it (grade B ⚠); 13 go from it, the strongest it → cells under [[Canagliflozin (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13679.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.26×** | +22.5 | 0e+00 | 43/43 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.56×** | +13.4 | 1e-38 | 39/44 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.10×** | +11.5 | 2e-28 | 43/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +10.8 | 6e-25 | 35/45 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +9.1 | 1e-17 | 27/45 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.002 | 14/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.87×** | +3.6 | 0.027 | 10/40 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13679.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.276×** | -14.1 | 1e-42 | 42/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.312×** | -12.8 | 5e-35 | 42/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.315×** | -12.7 | 1e-34 | 38/44 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.326×** | -12.3 | 1e-32 | 40/48 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.377×** | -10.7 | 1e-24 | 40/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.403×** | -10.0 | 2e-21 | 33/48 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.397×** | -9.8 | 1e-20 | 34/43 (RPMI-7951, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.425×** | -9.4 | 4e-19 | 34/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.439×** | -9.0 | 9e-18 | 33/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.506×** | -7.5 | 4e-12 | 32/47 (PANC-1, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.527×** | -6.7 | 1e-09 | 28/46 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.614×** | -5.4 | 4e-06 | 22/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.605×** | -5.3 | 5e-06 | 22/44 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.617×** | -5.3 | 5e-06 | 25/47 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.427×** | -4.9 | 4e-05 | 21/44 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.632×** | -4.8 | 4e-05 | 23/46 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.785×** | -3.8 | 0.005 | 20/48 (RKO, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13679. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.7 | 4 | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.28× (z +14.5) | [[Digitoxin (drug)]] 5 µM 0.172× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.176× (z -12.3) |
| [[H4 (line)]] | wt | 32.8 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0391× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0426× (z -15.2) |
| [[SW480 (line)]] | alt | 15.0 | 3 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +13.1) | [[Digitoxin (drug)]] 0.5 µM 0.135× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 37.3 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.0423× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0965× (z -13.4) |
| [[PANC-1 (line)]] | alt | 19.3 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +13.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 47.8 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.222× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 40.0 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0308× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -10.8) |
| [[A549 (line)]] | wt | 24.2 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0858× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +9.9) | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0749× (z -10.2) |
| [[J82 (line)]] | alt | 25.8 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.43× (z +13.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.117× (z -11.4) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.0362× (z -9.6) |
| [[A-172 (line)]] | wt | 20.5 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +14.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -10.1) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 24.9 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.0801× (z -11.7) |
| [[LoVo (line)]] | wt | 11.8 | 3 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.69× (z +14.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.216× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0841× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 18.5 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.107× (z -11.7) |
| [[HOP62 (line)]] | alt | 25.1 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -9.0) |
| [[HT-29 (line)]] | alt | 11.9 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +11.4) | [[Belinostat (drug)]] 5 µM 0.137× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 30.7 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -12.7) |
| [[A498 (line)]] | wt | 37.8 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 13.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.28× (z +8.5) | [[Methotrexate (drug)]] 0.5 µM 0.0639× (z -10.0) |
| [[Hs 766T (line)]] | wt | 14.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +11.4) | — |
| [[HS-578T (line)]] | alt | 17.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -8.5) |
| [[LS 180 (line)]] | wt | 10.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +12.9) | — |
| [[NCI-H2347 (line)]] | alt | 4.85 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.90× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 25.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0759× (z -11.3) ⚠ toxic |
| [[SW 900 (line)]] | alt | 14.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.65× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 6.41 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.85× (z +10.3) | [[5-Azacytidine (drug)]] 0.5 µM 0.0641× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 7.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.80× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0961× (z -8.8) |
| [[C32 (line)]] | wt | 44.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 7.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.12× (z +9.1) | — |
| [[KATO III (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.100× (z -9.6) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.48× (z +11.1) | — |
| [[RKO (line)]] | wt | 22.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.65× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 23.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -8.6) |
| [[A-427 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13679), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSK3B-DT]] | +0.80 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.77 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[PCBP1-AS1]] | +0.77 | +0.75 / +0.45 | both halves | 3e-05 | same gene group |
| [[SMIM15-AS1]] | +0.76 | +0.77 / +0.48 | both halves | 2e-05 | same gene group |
| [[CCT6B]] | +0.74 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[NEK8]] | +0.74 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[ZNF341-AS1]] | +0.73 | +0.69 / +0.51 | both halves | 1e-05 | same gene group |
| [[THUMPD3-AS1]] | +0.73 | +0.72 / +0.59 | both halves | 7e-06 | same gene group |
| [[LINC00863]] | +0.73 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[MZF1-AS1]] | +0.72 | +0.69 / +0.42 | both halves | 4e-05 | same gene group |
| [[GARIN1A]] | +0.71 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[PBLD]] | +0.71 | +0.68 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA40]] | -0.66 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[MAST3]] | -0.64 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[NDRG3]] | -0.64 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[PLA2G12A]] | -0.63 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[RAB4A]] | -0.63 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[BRAT1]] | -0.63 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[SLC23A2]] | -0.62 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[HDAC1]] | -0.62 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[STX7]] | -0.62 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[SERAC1]] | -0.61 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[ACTR5]] | -0.61 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AOX1]] | B | AOX1 activity raises ACTR3-AS1's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.84× lower at baseline in the lines without AOX1 | 0.002 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ACTR3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.7% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABCA10]] | B | ABCA10 activity raises ACTR3-AS1's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.74× lower at baseline in the lines without ABCA10 | 0.049 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[CDK6-AS1]] | B | CDK6-AS1 activity raises ACTR3-AS1's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.89× lower at baseline in the lines without CDK6-AS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[COL27A1]] | B | COL27A1 activity raises ACTR3-AS1's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without COL27A1 | 0.075 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity lowers ACTR3-AS1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[CBX2]] | B | CBX2 activity raises ACTR3-AS1's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without CBX2 | 0.085 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[CAVIN4]] | C | CAVIN4 activity raises ACTR3-AS1's level | lines that do not express CAVIN4 (4) vs lines expressing it (46) | 1.89× lower at baseline in the lines without CAVIN4 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GPR135, SYCP2L, FAM229B; maybe low, not absent; its own permutation p |
| [[LINC01829]] | C | LINC01829 activity raises ACTR3-AS1's level | lines that do not express LINC01829 (3) vs lines expressing it (47) | 2.26× lower at baseline in the lines without LINC01829 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP11, GNG12-AS1, LINC02763; maybe low, not absent; its own permutation p |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Canagliflozin (drug)]] 5 µM | C | ACTR3-AS1's natural level lowers the cells' numbers under Canagliflozin 5 µM (makes them more sensitive) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.73 | 0.186 over the table, 0.004 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Adagrasib (drug)]] 0.5 µM | C | ACTR3-AS1's natural level lowers the cells' numbers under Adagrasib 0.5 µM (makes them more sensitive) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.71 | 0.260 over the table, 0.023 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | C | ACTR3-AS1's natural level raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.291 over the table, 0.097 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fumaric acid (drug)]] 5 µM | C | ACTR3-AS1's natural level raises the cells' numbers under Fumaric acid 5 µM (protects the cells) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.291 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Sulfatinib (drug)]] 5 µM | C | ACTR3-AS1's natural level raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.352 over the table, 0.067 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Almonertinib (mesylate) (drug)]] 5 µM | C | ACTR3-AS1's natural level raises the cells' numbers under Almonertinib (mesylate) 5 µM (protects the cells) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.360 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Neratinib (drug)]] 0.05 µM | C | ACTR3-AS1's natural level lowers the cells' numbers under Neratinib 0.05 µM (makes them more sensitive) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.360 over the table, 0.078 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | C | ACTR3-AS1's natural level lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.361 over the table, 0.078 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | ACTR3-AS1's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.361 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | ACTR3-AS1's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | ACTR3-AS1's natural level raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62 | 0.421 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | ACTR3-AS1's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.079 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (35.0, -7.2); signed map (21.8, -4.1). **Vector** length 116, 33.4% of its response variance represented; |z| ≥ 3 in 1,311 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.4 | +22.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +13.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.1 | +11.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.8 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Cinacalcet (drug)]] 5 µM |  | +1.6 | +2.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -9.3 | -12.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.4 | -10.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -8.0 | -9.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.6 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | -10.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.1 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | ACTR3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q14.1 — chr2:113,831,049-113,891,020 (-) |
| Ensembl biotype | lncRNA |
| Also known as | AC104653.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53965](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53965) · Entrez [101060091](https://www.ncbi.nlm.nih.gov/gene/101060091) · Ensembl [ENSG00000228857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228857)

## Data

Gene col 13679: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13679); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13679, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13679]; `tensor/DDL_lfc|DDL_z.npy` [13679]; `embed/gene_vectors.npy` [13679]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13679 or target_col == 13679). Every well: [[ACTR3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTR3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

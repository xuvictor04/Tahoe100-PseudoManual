---
symbol: "WNK2"
type: "gene"
col: 9091
ensembl_id: "ENSG00000165238"
name: "WNK lysine deficient protein kinase 2"
location: "9q22.31"
module: 18
arm: "+"
pooled_cpm: 13.47
n_lines_expressing: 34
n_dd_up: 33
n_dd_down: 16
n_dd_up_clean: 15
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 25
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# WNK2

*WNK lysine deficient protein kinase 2* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (18 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.61× (z +21.8, q 0e+00, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.658× (z -9.6, q 7e-19, down in 20 of 30 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.551× (z -9.2, q 7e-18, down in 18 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLB1L2]] (+0.73, fdr 7e-06), [[TMEM201]] (+0.69, fdr 8e-06), [[CCDC88C]] (+0.66, fdr 1e-05); moves opposite to [[METTL25B]] (-0.59, fdr 2e-05), [[STK16]] (-0.59, fdr 1e-05), [[ZNF226]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LAMC3]] → it (grade B ⚠); 25 go from it, the strongest it → [[HACD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 18 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9091.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +21.8 | 0e+00 | 26/31 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **3.52×** | +20.2 | 0e+00 | 27/32 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.89×** | +17.1 | 0e+00 | 26/32 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.06×** | +11.6 | 3e-29 | 23/32 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.80×** | +8.7 | 5e-16 | 16/23 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.66×** | +7.8 | 5e-13 | 17/31 (NCI-H460, A549, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +7.4 | 1e-11 | 16/31 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.61×** | +7.4 | 1e-11 | 7/15 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.50×** | +6.5 | 4e-09 | 13/32 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.50×** | +6.5 | 4e-09 | 16/32 (NCI-H460, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.47×** | +6.1 | 5e-08 | 12/26 (PANC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.48×** | +6.1 | 5e-08 | 13/31 (NCI-H460, LS 180, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.00×** | +5.8 | 2e-07 | 13/32 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.5 | 1e-06 | 13/31 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~88% of this change | **1.42×** | +5.4 | 3e-06 | 11/27 (NCI-H460, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.1 | 2e-05 | 8/32 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +5.0 | 2e-05 | 11/32 (RKO, NCI-H1792, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.52×** | +4.8 | 5e-05 | 6/32 (NCI-H460, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 6e-05 | 10/32 (NCI-H460, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.6 | 1e-04 | 8/32 (J82, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.31×** | +4.3 | 5e-04 | 7/31 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.003 | 9/31 (SW48, LoVo, …) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.027 | 1/32 (SW48) | inconsistent across doses | position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 1.14× | +3.0 | 0.043 | 5/32 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.046 | 4/32 (BT-474, PANC-1, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.046 | 3/31 (A-427, HepG2/C3A, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9091.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.658×** | -9.6 | 7e-19 | 20/30 (NCI-H23, RKO, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.551×** | -9.2 | 7e-18 | 18/32 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.674×** | -9.0 | 4e-17 | 22/32 (Panc 03.27, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.626×** | -7.6 | 6e-12 | 15/30 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.618×** | -5.6 | 3e-06 | 14/30 (LS 180, RKO, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.731×** | -4.9 | 1e-04 | 10/31 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.565×** | -4.8 | 1e-04 | 10/31 (HT-29, Panc 03.27, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.765×** | -4.3 | 0.001 | 13/32 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.837× | -4.1 | 0.003 | 10/32 (HT-29, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **0.789×** | -3.8 | 0.006 | 6/32 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.789×** | -3.8 | 0.006 | 8/32 (A549, HCT15, …) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.791×** | -3.8 | 0.006 | 10/31 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.791×** | -3.8 | 0.006 | 4/32 (LS 180, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.800×** | -3.6 | 0.012 | 7/32 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 5 µM | ⚠ toxic | **0.823×** | -3.2 | 0.058 | 5/31 (C32, C-33 A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.694×** | -3.1 | 0.070 | 11/32 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.830×** | -3.0 | 0.081 | 5/32 (RKO, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.80 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9091. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.2 | 7 (5 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.63× (z +19.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -9.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[PANC-1 (line)]] | alt | 8.30 | 4 (3 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.06× (z +11.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.0827× (z -17.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[RKO (line)]] | wt | 78.3 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +11.2) | [[Harringtonine (drug)]] 5 µM 0.0682× (z -21.1) |
| [[C-33 A (line)]] | alt | 57.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0730× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 86.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 18.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -10.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.279× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -17.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A549 (line)]] | wt | 6.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.0× (z +16.3) | — |
| [[AN3 CA (line)]] | alt | 42.8 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0801× (z -10.0) |
| [[C32 (line)]] | wt | 3.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.71× (z +8.5) | — |
| [[LoVo (line)]] | wt | 35.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +17.2) | — |
| [[LS 180 (line)]] | wt | 19.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +11.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -10.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H1792 (line)]] | alt | 6.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.55× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 3.51 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.05 µM 0.0444× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.223× (z -11.4) |
| [[A-172 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9091), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLB1L2]] | +0.73 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[TMEM201]] | +0.69 | +0.58 / +0.71 | both halves | 8e-06 |  |
| [[CCDC88C]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[TOMM40]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TCOF1]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ADCY3]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[LYRM4]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[LRRC20]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[TMEM97]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[VAV2]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[HACD3]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[SHANK3]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL25B]] | -0.59 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[STK16]] | -0.59 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[ZNF226]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SEPSECS]] | -0.57 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[COMMD3]] | -0.56 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[THAP6]] | -0.56 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[CUTALP]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ZNF585A]] | -0.54 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ZNF44]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[CHURC1]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[NDUFA5]] | -0.52 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[MED18]] | -0.52 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC3]] | B | LAMC3 activity raises WNK2's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without LAMC3 | 0.011 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[BTNL9]] | B | BTNL9 activity raises WNK2's level | lines that do not express BTNL9 (24) vs lines expressing it (26) | 2.63× lower at baseline in the lines without BTNL9 | 0.036 | ⚠ within organs, on part of the lines; also absent: PCSK6, CDX2, PIP5K1B |
| [[TOP2A]] | B | TOP2A activity lowers WNK2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IL17RB]] | C | IL17RB activity raises WNK2's level | lines that do not express IL17RB (22) vs lines expressing it (28) | 3.08× lower at baseline in the lines without IL17RB | 0.062 | ⚠ within organs, on part of the lines; also absent: CHDH, ESRP2, PRSS22; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 25, C 0. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HACD3]] | B | WNK2 activity raises HACD3's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without WNK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[DDX54]] | B | WNK2 activity raises DDX54's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.45× lower at baseline in the lines without WNK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[EBPL]] | B | WNK2 activity raises EBPL's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.52× lower at baseline in the lines without WNK2 | 0.021 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[SPINDOC]] | B | WNK2 activity raises SPINDOC's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.52× lower at baseline in the lines without WNK2 | 0.022 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[TMEM97]] | B | WNK2 activity raises TMEM97's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without WNK2 | 0.022 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[PARD6G]] | B | WNK2 activity raises PARD6G's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without WNK2 | 0.025 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[ZNRF3]] | B | WNK2 activity raises ZNRF3's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 2.29× lower at baseline in the lines without WNK2 | 0.026 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[LAMC3]] | B | WNK2 activity raises LAMC3's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.98× lower at baseline in the lines without WNK2 | 0.027 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[ST6GAL1]] | B | WNK2 activity raises ST6GAL1's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without WNK2 | 0.029 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[XPO5]] | B | WNK2 activity raises XPO5's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without WNK2 | 0.036 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[MACROD1]] | B | WNK2 activity raises MACROD1's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 2.05× lower at baseline in the lines without WNK2 | 0.041 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[UCK2]] | B | WNK2 activity raises UCK2's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without WNK2 | 0.047 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.5, -39.2); signed map (-7.0, -55.5). **Vector** length 77.8, 17.8% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +21.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.9 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | +3.8 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.8 | +6.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.5 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.2 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -5.0 | -7.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -9.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.0 | -9.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -4.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.4 | -5.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | WNK lysine deficient protein kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:93,184,122-93,320,572 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-CO-43, KIAA1760; previously SDCCAG43, PRKWNK2 |
| Gene groups (HGNC) | WNK lysine deficient protein kinases |
| Reactome | 3 pathways, smallest: Stimuli-sensing channels; Ion channel transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3S1](https://www.uniprot.org/uniprotkb/Q9Y3S1) (Serine/threonine-protein kinase WNK2):

> Serine/threonine-protein kinase component of the WNK2-SPAK/OSR1 kinase cascade, which plays an important role in the regulation of electrolyte homeostasis, cell signaling, survival, and proliferation. The WNK2-SPAK/OSR1 kinase cascade is composed of WNK2, which mediates phosphorylation and activation of downstream kinases OXSR1/OSR1 and STK39/SPAK (By similarity). Following activation, OXSR1/OSR1 and STK39/SPAK catalyze phosphorylation of ion cotransporters, regulating their activity (By …

**Summary**, from NCBI Gene [65268](https://www.ncbi.nlm.nih.gov/gene/65268):

> The protein encoded by this gene is a cytoplasmic serine-threonine kinase that belongs to the protein kinase superfamily. The protein plays an important role in the regulation of electrolyte homeostasis, cell signaling survival, and proliferation. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:14542](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14542) · Entrez [65268](https://www.ncbi.nlm.nih.gov/gene/65268) · UniProt [Q9Y3S1](https://www.uniprot.org/uniprotkb/Q9Y3S1) · Ensembl [ENSG00000165238](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165238)

## Data

Gene col 9091: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9091); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9091, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9091]; `tensor/DDL_lfc|DDL_z.npy` [9091]; `embed/gene_vectors.npy` [9091]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9091 or target_col == 9091). Every well: [[WNK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WNK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

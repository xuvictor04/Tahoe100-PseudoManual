---
symbol: "PRPF39"
type: "gene"
col: 11645
ensembl_id: "ENSG00000185246"
name: "pre-mRNA processing factor 39"
location: "14q21.2"
module: 17
arm: "+"
pooled_cpm: 68.82
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PRPF39

*pre-mRNA processing factor 39* — 14q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.61× (z +20.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.583× (z -11.4, q 2e-27, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS31P4]] (+0.75, fdr 7e-06), [[ZNF14]] (+0.70, fdr 7e-06), [[FAM133B]] (+0.70, fdr 7e-06); moves opposite to [[ZNF407]] (-0.67, fdr 1e-05), [[PDK1-AS1]] (-0.64, fdr 3e-05), [[SNTB2]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00888]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PTCD3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11645.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.61×** | +20.3 | 0e+00 | 47/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.38×** | +13.5 | 9e-39 | 44/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +8.7 | 6e-16 | 43/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +8.6 | 2e-15 | 44/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +7.9 | 3e-13 | 37/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +7.7 | 1e-12 | 43/49 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +6.0 | 2e-07 | 36/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.08×** | +5.9 | 2e-07 | 37/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.8 | 5e-07 | 34/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +5.3 | 6e-06 | 31/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +5.0 | 3e-05 | 31/48 (NCI-H1792, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +4.6 | 2e-04 | 29/48 (NCI-H1792, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.1 | 0.001 | 22/38 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.002 | 20/48 (SNU-1, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.005 | 26/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.010 | 24/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.010 | 22/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.013 | 25/48 (MIA PaCa-2, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +3.4 | 0.018 | 21/48 (RKO, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11645.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.583×** | -11.4 | 2e-27 | 41/49 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.524×** | -10.1 | 2e-21 | 41/49 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.582×** | -8.1 | 1e-13 | 35/43 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.740×** | -6.5 | 8e-09 | 34/48 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.706×** | -5.4 | 7e-06 | 29/48 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.782×** | -3.8 | 0.012 | 27/48 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.809×** | -3.3 | 0.061 | 20/48 (J82, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.809×** | -3.3 | 0.061 | 20/48 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.809×** | -3.3 | 0.061 | 17/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.080 | 19/48 (AsPC-1, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.816× | -3.0 | 0.12 | 17/50 (AN3 CA, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11645. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 47.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +22.3) | — |
| [[NCI-H460 (line)]] | wt | 60.2 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +17.7) | — |
| [[SW480 (line)]] | alt | 69.7 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 89.5 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -8.5) |
| [[LoVo (line)]] | wt | 57.6 | 4 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 121 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.571× (z -8.5) |
| [[RKO (line)]] | wt | 90.2 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -14.8) |
| [[SW48 (line)]] | wt | 111 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -9.6) |
| [[H4 (line)]] | wt | 74.1 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 104 | 2 | 1 | [[Homoharringtonine (drug)]] 0.05 µM 3.10× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 127 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -11.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 84.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -8.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 87.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 57.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +16.1) | — |
| [[HOP62 (line)]] | alt | 62.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.9) | [[Auranofin (drug)]] 5 µM 0.351× (z -9.5) |
| [[HT-29 (line)]] | alt | 33.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +15.3) | — |
| [[J82 (line)]] | alt | 66.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -11.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 44.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +14.7) | — |
| [[NCI-H1573 (line)]] | alt | 51.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +17.1) | — |
| [[NCI-H1792 (line)]] | alt | 97.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.47× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 59.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +18.3) | — |
| [[SW 900 (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 41.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.2) | — |
| [[A-427 (line)]] | wt | 77.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -9.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 60.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 49.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +12.9) | — |
| [[BT-474 (line)]] | alt | 88.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 36.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 86.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 46.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 50.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +12.7) | — |
| [[hTERT-HPNE (line)]] | wt | 61.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 55.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 58.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 72.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -10.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 45.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 54.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +14.0) | — |
| [[SW1417 (line)]] | alt | 73.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11645), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | +0.75 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[ZNF14]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[FAM133B]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[PRMT9]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[MFSD13A]] | +0.70 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[RIOK2]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[GEMIN2]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[METTL17]] | +0.68 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[BBS5]] | +0.68 | +0.57 / +0.63 | both halves | 9e-06 | STRING 400 |
| [[FIP1L1]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[METTL14]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[THOC1]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF407]] | -0.67 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[PDK1-AS1]] | -0.64 | -0.46 / -0.67 | both halves | 3e-05 |  |
| [[SNTB2]] | -0.64 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[MIATNB]] | -0.60 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[DDX5]] | -0.60 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[HCFC1]] | -0.60 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[KPNA4]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[HCG18]] | -0.59 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[C2CD3]] | -0.58 | -0.67 / -0.23 | both halves | 5e-04 |  |
| [[GATAD2A]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[PRDX1]] | -0.56 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[ASXL2]] | -0.55 | -0.59 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00888]] | B | LINC00888 activity raises PRPF39's level | lines that do not express LINC00888 (7) vs lines expressing it (43) | 1.38× lower at baseline in the lines without LINC00888 | 0.040 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTCD3]] | C | PRPF39's natural level weakens PTCD3's drug response | PRPF39's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.03; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.796). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-24.3, -3.6); signed map (-24.3, -12.3). **Vector** length 87.8, 26.3% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.7 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +20.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | -0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.3 | -11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA processing factor 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.2 — chr14:45,084,107-45,116,282 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20666, FLJ11128 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UA1](https://www.uniprot.org/uniprotkb/Q86UA1) (Pre-mRNA-processing factor 39):

> Involved in pre-mRNA splicing.

**Summary**, from NCBI Gene [55015](https://www.ncbi.nlm.nih.gov/gene/55015):

> Predicted to contribute to pre-mRNA 5'-splice site binding activity. Predicted to be involved in mRNA 5'-splice site recognition. Predicted to be part of U1 snRNP; U2-type prespliceosome; and commitment complex. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20314) · Entrez [55015](https://www.ncbi.nlm.nih.gov/gene/55015) · UniProt [Q86UA1](https://www.uniprot.org/uniprotkb/Q86UA1) · Ensembl [ENSG00000185246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185246)

## Data

Gene col 11645: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11645); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11645, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11645]; `tensor/DDL_lfc|DDL_z.npy` [11645]; `embed/gene_vectors.npy` [11645]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11645 or target_col == 11645). Every well: [[PRPF39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

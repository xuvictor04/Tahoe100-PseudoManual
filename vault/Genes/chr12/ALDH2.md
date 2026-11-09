---
symbol: "ALDH2"
type: "gene"
col: 3214
ensembl_id: "ENSG00000111275"
name: "aldehyde dehydrogenase 2 family member"
location: "12q24.12"
module: 72
arm: "+"
pooled_cpm: 27.81
n_lines_expressing: 41
n_dd_up: 26
n_dd_down: 10
n_dd_up_clean: 19
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 9
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# ALDH2

*aldehyde dehydrogenase 2 family member* — 12q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.60× (z +14.1, q 2e-42, up in 29 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 2.35× (z +11.9, q 4e-30, up in 33 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.517× (z -9.7, q 1e-19, down in 26 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST13]] (+0.65, fdr 7e-06), [[IDH1]] (+0.64, fdr 7e-06), [[UBE4B]] (+0.62, fdr 1e-05); moves opposite to [[CHAMP1]] (-0.62, fdr 1e-05), [[PFN1]] (-0.60, fdr 3e-05), [[TNFRSF12A]] (-0.58, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GOLT1A]] → it (grade B ⚠); 9 go from it, the strongest it → [[HSPB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +14.1 | 2e-42 | 29/35 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +12.7 | 1e-34 | 25/28 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.35×** | +11.9 | 4e-30 | 33/38 (AsPC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.14×** | +11.2 | 4e-27 | 29/38 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.88×** | +9.3 | 1e-18 | 32/39 (HOP62, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +9.3 | 2e-18 | 23/30 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +9.0 | 2e-17 | 26/38 (HOP62, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +8.3 | 9e-15 | 28/37 (SW 900, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +5.2 | 1e-05 | 17/39 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +5.2 | 1e-05 | 26/39 (SNU-423, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.6 | 3e-04 | 18/31 (AsPC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.003 | 13/38 (A549, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +3.9 | 0.005 | 19/39 (HOP62, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.005 | 15/38 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +3.6 | 0.012 | 14/39 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.012 | 14/37 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.029 | 12/38 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.035 | 11/39 (SW480, A549, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.040 | 12/38 (SNU-423, KATO III, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.045 | 10/39 (KATO III, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3214.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.517×** | -9.7 | 1e-19 | 26/36 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.707×** | -7.2 | 1e-10 | 22/37 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.612×** | -7.0 | 7e-10 | 22/39 (HCT15, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.647×** | -6.4 | 2e-08 | 22/39 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.667×** | -6.0 | 2e-07 | 24/38 (CFPAC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.667×** | -6.0 | 2e-07 | 26/39 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.716×** | -4.9 | 7e-05 | 22/37 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.735×** | -4.5 | 4e-04 | 20/39 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.745×** | -4.3 | 9e-04 | 18/37 (RPMI-7951, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Folic acid (drug)]] 5 µM |  | **0.829×** | -3.9 | 0.005 | 12/39 (Hs 766T, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 34.6 | 3 (2 ⚠) | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 6.65× (z +12.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 43.4 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.71× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 29.1 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.71× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.1) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -11.1) |
| [[LoVo (line)]] | wt | 57.6 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.62× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 79.8 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.60× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 28.0 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.12× (z +12.4) | — |
| [[KATO III (line)]] | alt | 53.3 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.02× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -12.2) |
| [[A549 (line)]] | wt | 39.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.20× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H2347 (line)]] | alt | 54.0 | 1 | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.41× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -13.3) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 55.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -13.8) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -13.1) |
| [[RKO (line)]] | wt | 39.4 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.08× (z +10.9) | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0738× (z -9.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[COLO 205 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -10.8) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HCT15 (line)]] | alt | 52.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.290× (z -8.6) |
| [[Hs 766T (line)]] | wt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.9× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 62.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 63.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 5.11 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 6.50 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.26 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.20 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST13]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[IDH1]] | +0.64 | +0.64 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS; STRING 541 |
| [[UBE4B]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SNX3]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[CSDE1]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[GHITM]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[CALCOCO2]] | +0.60 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CTSD]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[CYP4F3]] | +0.57 | +0.61 / +0.49 | both halves | 1e-05 | pathway: Biological oxidations |
| [[BABAM1]] | +0.56 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[DNASE2]] | +0.56 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[HECW1]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHAMP1]] | -0.62 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[PFN1]] | -0.60 | -0.67 / -0.46 | both halves | 3e-05 |  |
| [[TNFRSF12A]] | -0.58 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SPIN4]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CCND1]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[DUSP4]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[LINC00973]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[PHLDA1]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ZBTB9]] | -0.53 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[EPHA2]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[PPP1R1C]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[SFR1]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GOLT1A]] | B | GOLT1A activity raises ALDH2's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without GOLT1A | 0.053 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSPB1]] | B | ALDH2 activity lowers HSPB1's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 2.02× higher at baseline in the lines without ALDH2 | 0.043 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |
| [[C5orf24]] | B | ALDH2 activity lowers C5orf24's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without ALDH2 | 0.047 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |
| [[PFN1]] | B | ALDH2 activity lowers PFN1's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 1.33× higher at baseline in the lines without ALDH2 | 0.048 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |
| [[DUSP4]] | B | ALDH2 activity raises DUSP4's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 2.36× lower at baseline in the lines without ALDH2 | 0.066 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 0.5 µM | B | ALDH2 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express ALDH2 (9) vs lines expressing it (39) | the lines without ALDH2: 0.45× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |
| [[COPS2]] | B | ALDH2 activity raises COPS2's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 1.28× lower at baseline in the lines without ALDH2 | 0.079 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |
| [[ARHGEF26-AS1]] | B | ALDH2 activity strengthens ARHGEF26-AS1's drug response | lines that do not express ALDH2 (8) vs lines expressing it (32) | the lines without ALDH2 respond 0.90× as strongly (z diff +0.74); strongest at Idarubicin (hydrochloride) 5 µM: 2.47x vs 6.67x (z diff +4.2) | 0.086 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PSMB4]] | B | ALDH2 activity lowers PSMB4's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without ALDH2 | 0.087 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |
| [[FLYWCH1]] | B | ALDH2 activity lowers FLYWCH1's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 1.29× higher at baseline in the lines without ALDH2 | 0.089 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.1, -11.8); signed map (-22.2, 3.3). **Vector** length 95.5, 22.6% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.4 | +11.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.5 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +9.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.0 | +4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.1 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +9.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.5 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -6.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -1.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.4 | +0.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 2 family member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.12 — chr12:111,766,887-111,817,532 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Aldehyde dehydrogenases; MicroRNA protein coding host genes |
| Hallmark sets | XENOBIOTIC_METABOLISM, ADIPOGENESIS |
| Reactome | 9 pathways, smallest: Ethanol oxidation; Neurotransmitter clearance; Smooth Muscle Contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [P05091](https://www.uniprot.org/uniprotkb/P05091) (Aldehyde dehydrogenase, mitochondrial):

> Mitochondrial aldehyde dehydrogenase with broad substrate specificity which participates in the detoxification of ethanol-derived acetaldehyde and endogenous aldehydes, including those arising from lipid peroxidation. The reaction mechanism involves a nucleophilic attack on the aldehyde substrate, resulting in formation of a thiohemiacetal intermediate. Subsequent hydride transfer to NAD+, yields a thioester intermediate which is hydrolyzed to the carboxylic acid product through activation of a …

**Summary**, from NCBI Gene [217](https://www.ncbi.nlm.nih.gov/gene/217):

> This protein belongs to the aldehyde dehydrogenase family of proteins. Aldehyde dehydrogenase is the second enzyme of the major oxidative pathway of alcohol metabolism. Two major liver isoforms of aldehyde dehydrogenase, cytosolic and mitochondrial, can be distinguished by their electrophoretic mobilities, kinetic properties, and subcellular localizations. Most Caucasians have two major isozymes, while approximately 50% of East Asians have the cytosolic isozyme but not the mitochondrial …

**Accessions** — [HGNC:404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:404) · Entrez [217](https://www.ncbi.nlm.nih.gov/gene/217) · UniProt [P05091](https://www.uniprot.org/uniprotkb/P05091) · Ensembl [ENSG00000111275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111275)

## Data

Gene col 3214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3214); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3214]; `tensor/DDL_lfc|DDL_z.npy` [3214]; `embed/gene_vectors.npy` [3214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3214 or target_col == 3214). Every well: [[ALDH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

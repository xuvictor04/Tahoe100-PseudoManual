---
symbol: "GNG2"
type: "gene"
col: 11817
ensembl_id: "ENSG00000186469"
name: "G protein subunit gamma 2"
location: "14q22.1"
module: 94
arm: "+"
pooled_cpm: 12.87
n_lines_expressing: 28
n_dd_up: 24
n_dd_down: 24
n_dd_up_clean: 21
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 11
direction_downstream: 14
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# GNG2

*G protein subunit gamma 2* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.97× (z +22.0, q 0e+00, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.377× (z -13.9, q 2e-41, down in 24 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC44A2]] (+0.60, fdr 2e-05), [[GPCPD1]] (+0.59, fdr 3e-05), [[PRICKLE2]] (+0.59, fdr 1e-05); moves opposite to [[SNTB2]] (-0.52, fdr 2e-05), [[RUBCN]] (-0.51, fdr 2e-04), [[FBXW7]] (-0.50, fdr 1e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[PDZRN3]] → it (grade B ⚠); 14 go from it, the strongest it → [[ARL4D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.97×** | +22.0 | 0e+00 | 26/26 (SW480, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **3.34×** | +17.2 | 0e+00 | 25/26 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.66×** | +14.0 | 5e-42 | 25/26 (NCI-H460, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **2.61×** | +13.7 | 2e-40 | 24/26 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.38×** | +11.9 | 1e-30 | 21/26 (A-172, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +11.5 | 1e-28 | 15/26 (SW1417, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +8.9 | 3e-17 | 12/26 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.80×** | +8.0 | 6e-14 | 18/26 (NCI-H460, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +7.7 | 1e-12 | 14/26 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +5.6 | 1e-06 | 6/23 (HOP62, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.30×** | +5.3 | 6e-06 | 13/26 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +5.0 | 2e-05 | 7/22 (LOX-IMVI, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.0 | 3e-05 | 10/25 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adenine (drug)]] 5 µM |  | **1.26×** | +4.7 | 1e-04 | 14/26 (RPMI-7951, SW480, …) | top dose only | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.001 | 8/26 (SW1417, SW480, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.36×** | +4.1 | 0.001 | 9/26 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.003 | 7/26 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.67×** | +3.8 | 0.004 | 8/25 (A-172, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11817.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.377×** | -13.9 | 2e-41 | 24/26 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.489×** | -10.2 | 4e-22 | 22/26 (SHP-77, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.569×** | -8.0 | 2e-13 | 22/26 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.606×** | -6.9 | 9e-10 | 15/26 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.634×** | -6.5 | 8e-09 | 21/26 (SW 900, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.649×** | -6.2 | 6e-08 | 20/26 (SHP-77, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.650×** | -6.1 | 6e-08 | 13/26 (CHP-212, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.656×** | -6.0 | 1e-07 | 15/25 (HS-578T, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.656×** | -6.0 | 1e-07 | 16/26 (A-172, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.657×** | -6.0 | 1e-07 | 15/26 (CHP-212, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.695×** | -5.2 | 1e-05 | 13/26 (SW 900, SW 1088, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.701×** | -5.1 | 2e-05 | 12/26 (SNU-423, H4, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.780×** | -5.0 | 2e-05 | 16/26 (A-172, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.715×** | -4.8 | 6e-05 | 13/26 (CHP-212, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.719×** | -4.7 | 9e-05 | 12/26 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.712×** | -4.7 | 1e-04 | 13/25 (H4, A-172, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -4.6 | 1e-04 | 18/26 (C32, AN3 CA, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -4.6 | 2e-04 | 16/26 (hTERT-HPNE, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.3 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +18.2) | [[Daptomycin (drug)]] 5 µM 0.185× (z -9.4) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 0.5 µM 0.187× (z -9.4) |
| [[C32 (line)]] | wt | 73.2 | 2 | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.49× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -17.1) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -13.5) |
| [[CHP-212 (line)]] | wt | 270 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.135× (z -12.1) |
| [[SW 900 (line)]] | alt | 89.6 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -18.5) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.177× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 61.2 | 1 | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.16× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -12.0) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.370× (z -8.8) |
| [[SW1417 (line)]] | alt | 7.40 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +15.5) | — |
| [[SW480 (line)]] | alt | 9.52 | 5 | 0 | [[Selinexor (drug)]] 5 µM 5.77× (z +14.6) | — |
| [[AN3 CA (line)]] | alt | 182 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0491× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0913× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 79.1 | 2 | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.43× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.210× (z -10.9) |
| [[LoVo (line)]] | wt | 3.99 | 3 | 0 | [[Selinexor (drug)]] 5 µM 8.94× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 35.9 | 1 | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.10× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.195× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 3.84 | 3 | 0 | [[Selinexor (drug)]] 5 µM 11.2× (z +14.1) | — |
| [[SHP-77 (line)]] | alt | 16.6 | 1 | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 3.87× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.0531× (z -13.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 12.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +10.1) | [[Digitoxin (drug)]] 0.05 µM 0.140× (z -9.6) |
| [[J82 (line)]] | alt | 9.10 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.110× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 5.70 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 10.6× (z +12.6) | [[Docetaxel (drug)]] 0.05 µM 0.0838× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0696× (z -13.7) ⚠ toxic; cell-cycle shift, explains ~13% of this change |
| [[SW 1088 (line)]] | alt | 69.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0826× (z -9.9) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Lactate (calcium) (drug)]] 5 µM 0.0468× (z -8.6) |
| [[A498 (line)]] | wt | 11.4 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.15× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 8.72 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0474× (z -10.0) |
| [[HOP62 (line)]] | alt | 12.9 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.43× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 4.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +9.9) | — |
| [[A-427 (line)]] | wt | 0.967 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC44A2]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[GPCPD1]] | +0.59 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[PRICKLE2]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[STK32A]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[DUSP15]] | +0.57 | +0.43 / +0.60 | both halves | 4e-05 |  |
| [[RNF150]] | +0.57 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[ZNF727]] | +0.57 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[OSGEP]] | +0.53 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ARMCX1]] | +0.52 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ZSCAN12]] | +0.52 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[GALT]] | +0.52 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[CLN5]] | +0.52 | +0.38 / +0.62 | both halves | 7e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNTB2]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[RUBCN]] | -0.51 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[FBXW7]] | -0.50 | -0.49 / -0.50 | both halves | 1e-05 | pathway: Chaperonin-mediated protein folding |
| [[VPS53]] | -0.49 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[PSMD6-AS2]] | -0.47 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[MFSD14CP-1]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[NPLOC4]] | -0.47 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[KIAA0232]] | -0.46 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[RSKR]] | -0.46 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[NR2C2]] | -0.46 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | -0.46 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[TAF4]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDZRN3]] | B | PDZRN3 activity raises GNG2's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 3.60× lower at baseline in the lines without PDZRN3 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[TOP2A]] | B | TOP2A activity raises GNG2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM13C]] | B | FAM13C activity raises GNG2's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 3.48× lower at baseline in the lines without FAM13C | 0.085 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[GYPC]] | C | GYPC activity raises GNG2's level | lines that do not express GYPC (35) vs lines expressing it (15) | 4.49× lower at baseline in the lines without GYPC | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |
| [[BAALC]] | C | BAALC activity raises GNG2's level | lines that do not express BAALC (32) vs lines expressing it (18) | 4.73× lower at baseline in the lines without BAALC | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises GNG2's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 4.09× lower at baseline in the lines without PRRX1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[EDNRA]] | C | EDNRA activity raises GNG2's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 4.10× lower at baseline in the lines without EDNRA | 0.025 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[ARMCX1]] | C | ARMCX1 activity raises GNG2's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 4.41× lower at baseline in the lines without ARMCX1 | 0.025 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1; co-absent with the target |
| [[CTHRC1]] | C | CTHRC1 activity raises GNG2's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 4.19× lower at baseline in the lines without CTHRC1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[CSF1R]] | C | CSF1R activity raises GNG2's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 4.07× lower at baseline in the lines without CSF1R | 0.038 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent; co-absent with the target |
| [[COL7A1]] | C | COL7A1 activity raises GNG2's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 3.30× lower at baseline in the lines without COL7A1 | 0.091 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 9, C 5. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL4D]] | B | GNG2 activity raises ARL4D's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 2.07× lower at baseline in the lines without GNG2 | 0.005 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT |
| [[FAM13C]] | B | GNG2 activity raises FAM13C's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 2.16× lower at baseline in the lines without GNG2 | 0.011 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT |
| [[MEIS1]] | B | GNG2 activity raises MEIS1's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 2.81× lower at baseline in the lines without GNG2 | 0.028 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT |
| [[RUBCN]] | B | GNG2 activity strengthens RUBCN's drug response | lines that do not express GNG2 (22) vs lines expressing it (27) | the lines without GNG2 respond 0.80× as strongly (z diff +0.77); strongest at Panobinostat 0.5 µM: 1.61x vs 2.17x (z diff +1.9) | 0.033 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT; target measured in part of the lines; artifact flags |
| [[DIAPH2-AS1]] | B | GNG2 activity raises DIAPH2-AS1's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 1.53× lower at baseline in the lines without GNG2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT |
| [[RNF150]] | B | GNG2 activity raises RNF150's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 2.52× lower at baseline in the lines without GNG2 | 0.074 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT |
| [[RUBCN]] | B | GNG2 activity lowers RUBCN's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 1.27× higher at baseline in the lines without GNG2 | 0.076 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT |
| [[PKP4]] | B | GNG2 activity strengthens PKP4's drug response | lines that do not express GNG2 (22) vs lines expressing it (27) | the lines without GNG2 respond 0.76× as strongly (z diff +0.86); strongest at Idarubicin (hydrochloride) 5 µM: 1.09x vs 1.53x (z diff +4.2) | 0.081 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT; target measured in part of the lines; artifact flags |
| [[NEPRO]] | B | GNG2 activity weakens NEPRO's drug response | lines that do not express GNG2 (22) vs lines expressing it (27) | the lines without GNG2 respond 1.16× as strongly (z diff -0.72); strongest at Homoharringtonine 0.5 µM: 2.06x vs 1.62x (z diff -2.2) | 0.094 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT; target measured in part of the lines; artifact flags |
| [[COL7A1]] | C | GNG2 activity raises COL7A1's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 3.37× lower at baseline in the lines without GNG2 | 0.021 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT; co-absent with the target |
| [[PRICKLE2]] | C | GNG2 activity raises PRICKLE2's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 3.71× lower at baseline in the lines without GNG2 | 0.040 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT; co-absent with the target |
| [[ARMCX1]] | C | GNG2 activity raises ARMCX1's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 2.93× lower at baseline in the lines without GNG2 | 0.057 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT; co-absent with the target |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.9, 25.3); signed map (13.8, -15.6). **Vector** length 96.5, 26.6% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +11.3 | +22.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +7.4 | +13.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +8.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.1 | +14.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +8.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.9 | -6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -10.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.7 | -13.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -5.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:51,826,195-51,979,342 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | G protein subunits gamma |
| Hallmark sets | COMPLEMENT |
| Reactome | 66 pathways, smallest: G beta:gamma signalling through BTK; Prostacyclin signalling through prostacyclin receptor; G beta:gamma signalling through PLC beta |
| Matched by | ensembl_id |

**Function**, from UniProt [P59768](https://www.uniprot.org/uniprotkb/P59768) (Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-2):

> Gamma subunit of the heterotrimeric guanine nucleotide-binding protein (G proteins) that forms complexes with alpha and gamma subunits and participates in signal transduction downstream of G protein-coupled receptors (GPCRs). The beta-gamma dimer stabilizes the GDP-bound inactive alpha subunit by limiting spontaneous GDP dissociation. Upon GPCR activation, facilitates receptor-catalyzed GDP release and GTP binding on the alpha subunit. Following GPCR activation, the released beta-gamma dimer …

**Summary**, from NCBI Gene [54331](https://www.ncbi.nlm.nih.gov/gene/54331):

> This gene encodes one of the gamma subunits of a guanine nucleotide-binding protein. Such proteins are involved in signaling mechanisms across membranes. Various subunits forms heterodimers which then interact with the different signal molecules. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:4404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4404) · Entrez [54331](https://www.ncbi.nlm.nih.gov/gene/54331) · UniProt [P59768](https://www.uniprot.org/uniprotkb/P59768) · Ensembl [ENSG00000186469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186469)

## Data

Gene col 11817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11817); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11817]; `tensor/DDL_lfc|DDL_z.npy` [11817]; `embed/gene_vectors.npy` [11817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11817 or target_col == 11817). Every well: [[GNG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

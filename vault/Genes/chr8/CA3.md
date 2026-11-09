---
symbol: "CA3"
type: "gene"
col: 9018
ensembl_id: "ENSG00000164879"
name: "carbonic anhydrase 3"
location: "8q21.2"
module: 23
arm: "+"
pooled_cpm: 14.77
n_lines_expressing: 40
n_dd_up: 11
n_dd_down: 23
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CA3

*carbonic anhydrase 3* — 8q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.52× (z +14.2, q 1e-42, up in 33 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.170× (z -10.0, q 7e-21, down in 33 of 37 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD6-AS2]] (+0.66, fdr 1e-05), [[DARS1-AS1]] (+0.62, fdr 1e-05), [[CORIN]] (+0.59, fdr 2e-05); moves opposite to [[EHMT2]] (-0.63, fdr 1e-05), [[ALAD]] (-0.58, fdr 1e-04), [[CEP131]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ENKUR]] → it (grade B ⚠); 10 go from it, the strongest it → [[MOB3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +14.2 | 1e-42 | 33/37 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +8.9 | 2e-16 | 31/36 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +7.6 | 5e-12 | 28/36 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +6.5 | 9e-09 | 24/37 (LoVo, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +6.5 | 9e-09 | 20/36 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.6 | 5e-04 | 17/38 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.39×** | +3.5 | 0.032 | 8/36 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.034 | 11/37 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.034 | 12/36 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +3.3 | 0.049 | 8/37 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.49×** | +3.3 | 0.049 | 10/37 (A-172, RKO, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9018.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.170×** | -10.0 | 7e-21 | 33/37 (RKO, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.453×** | -8.6 | 2e-15 | 25/37 (KATO III, NCI-H1792, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.248×** | -7.9 | 5e-13 | 26/37 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.494×** | -7.7 | 3e-12 | 24/36 (NCI-H1792, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.493×** | -7.4 | 2e-11 | 21/34 (KATO III, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.505×** | -7.1 | 1e-10 | 26/35 (RKO, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.528×** | -6.9 | 3e-10 | 20/37 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.553×** | -6.4 | 1e-08 | 24/32 (KATO III, A498, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.566×** | -6.2 | 4e-08 | 21/37 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.579×** | -5.9 | 2e-07 | 21/37 (RKO, HT-29, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.563×** | -5.8 | 4e-07 | 19/29 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.587×** | -5.6 | 1e-06 | 14/22 (A498, PANC-1, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.600×** | -5.5 | 1e-06 | 20/37 (KATO III, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.606×** | -5.4 | 2e-06 | 21/37 (RPMI-7951, KATO III, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.404×** | -5.1 | 1e-05 | 22/35 (SHP-77, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.735×** | -4.7 | 8e-05 | 19/37 (RKO, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.704×** | -3.8 | 0.004 | 18/36 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.730×** | -3.4 | 0.018 | 16/37 (COLO 205, RKO, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.752×** | -3.1 | 0.055 | 10/37 (SW48, C32, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.757×** | -2.9 | 0.092 | 10/37 (NCI-H1792, SK-MEL-2, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 34.0 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0658× (z -25.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0478× (z -10.5) |
| [[HT-29 (line)]] | alt | 40.9 | 0 | 9 (5 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0168× (z -14.7) |
| [[LOX-IMVI (line)]] | wt | 40.1 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0301× (z -12.5) |
| [[RKO (line)]] | wt | 89.4 | 0 | 8 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0108× (z -17.1) |
| [[A498 (line)]] | wt | 39.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -15.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0382× (z -11.8) |
| [[H4 (line)]] | wt | 27.0 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0416× (z -14.0) ⚠ cell-cycle shift, explains ~82% of this change |
| [[SW1417 (line)]] | alt | 38.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.228× (z -10.2) |
| [[HS-578T (line)]] | alt | 4.42 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.32× (z +10.1) | [[Menadione (drug)]] 0.5 µM 0.0680× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0955× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 12.6 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.117× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 11.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 30.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -12.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.104× (z -11.7) |
| [[HCT15 (line)]] | alt | 28.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0429× (z -14.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.0328× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 17.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 7.99 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.137× (z -9.6) ⚠ cell-cycle shift, explains ~82% of this change |
| [[LoVo (line)]] | wt | 11.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +12.9) | [[Digitoxin (drug)]] 5 µM 0.234× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H1573 (line)]] | alt | 10.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0959× (z -11.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 11.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 7.44 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0843× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[J82 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SHP-77 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SK-MEL-2 (line)]] | alt | 8.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 7.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.88× (z +8.7) | — |
| [[A-427 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD6-AS2]] | +0.66 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[DARS1-AS1]] | +0.62 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[CORIN]] | +0.59 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[MCF2]] | +0.58 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[ZNF800]] | +0.56 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[SLC13A3]] | +0.55 | +0.55 / +0.27 | both halves | 3e-04 |  |
| [[MIATNB]] | +0.55 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[PELO-AS1]] | +0.55 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[MYRFL]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ENOX2]] | +0.54 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[PCAT1]] | +0.54 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[DGKH]] | +0.54 | +0.54 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHMT2]] | -0.63 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ALAD]] | -0.58 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[CEP131]] | -0.56 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[MRI1]] | -0.54 | -0.32 / -0.35 | both halves | 1e-04 |  |
| [[HDAC1]] | -0.54 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[IFT52]] | -0.53 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[SLC44A2]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[RAB3A]] | -0.52 | -0.46 / -0.22 | both halves | 6e-04 |  |
| [[BRAT1]] | -0.52 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[ECHS1]] | -0.52 | -0.25 / -0.50 | both halves | 4e-04 |  |
| [[TBC1D13]] | -0.52 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[HDGFL2]] | -0.51 | -0.49 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENKUR]] | B | ENKUR activity raises CA3's level | lines that do not express ENKUR (20) vs lines expressing it (30) | 2.61× lower at baseline in the lines without ENKUR | 0.007 | ⚠ within organs, on part of the lines; also absent: VNN1, MMP13, MILR1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CA3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MOB3B]] | B | MOB3B activity raises CA3's level | lines that do not express MOB3B (10) vs lines expressing it (40) | 2.52× lower at baseline in the lines without MOB3B | 0.068 | ⚠ within organs, on part of the lines; also absent: MYO1D; maybe low, not absent |
| [[CA13]] | C | CA13 activity raises CA3's level | lines that do not express CA13 (9) vs lines expressing it (41) | 5.08× lower at baseline in the lines without CA13 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CA3, PLSCR2, TRIB1; maybe low, not absent; co-absent with the target |
| [[PLSCR2]] | C | PLSCR2 activity raises CA3's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 4.69× lower at baseline in the lines without PLSCR2 | 0.002 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent; co-absent with the target |
| [[CADPS2]] | C | CADPS2 activity raises CA3's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 2.92× lower at baseline in the lines without CADPS2 | 0.027 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MOB3B]] | B | CA3 activity raises MOB3B's level | lines that do not express CA3 (10) vs lines expressing it (40) | 2.57× lower at baseline in the lines without CA3 | 0.031 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2 |
| [[TNFSF13B]] | B | CA3 activity raises TNFSF13B's level | lines that do not express CA3 (10) vs lines expressing it (40) | 2.03× lower at baseline in the lines without CA3 | 0.032 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2 |
| [[LINC01208]] | B | CA3 activity raises LINC01208's level | lines that do not express CA3 (10) vs lines expressing it (40) | 1.77× lower at baseline in the lines without CA3 | 0.042 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2 |
| [[ENKUR]] | B | CA3 activity raises ENKUR's level | lines that do not express CA3 (10) vs lines expressing it (40) | 2.78× lower at baseline in the lines without CA3 | 0.044 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2 |
| [[PELO-AS1]] | B | CA3 activity raises PELO-AS1's level | lines that do not express CA3 (10) vs lines expressing it (40) | 1.42× lower at baseline in the lines without CA3 | 0.065 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2 |
| [[GCNT4]] | B | CA3 activity strengthens GCNT4's drug response | lines that do not express CA3 (8) vs lines expressing it (28) | the lines without CA3 respond 0.84× as strongly (z diff +0.48); strongest at Epirubicin (hydrochloride) 5 µM: 1.77x vs 4.91x (z diff +2.8) | 0.087 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2; target measured in part of the lines; artifact flags |
| [[CA13]] | C | CA3 activity raises CA13's level | lines that do not express CA3 (10) vs lines expressing it (40) | 3.97× lower at baseline in the lines without CA3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2; co-absent with the target |
| [[MIR583HG]] | C | CA3 activity raises MIR583HG's level | lines that do not express CA3 (10) vs lines expressing it (40) | 3.60× lower at baseline in the lines without CA3 | 0.022 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2; co-absent with the target |
| [[CADPS2]] | C | CA3 activity raises CADPS2's level | lines that do not express CA3 (10) vs lines expressing it (40) | 3.87× lower at baseline in the lines without CA3 | 0.042 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2; co-absent with the target |
| [[PLSCR2]] | C | CA3 activity raises PLSCR2's level | lines that do not express CA3 (10) vs lines expressing it (40) | 2.22× lower at baseline in the lines without CA3 | 0.081 | ⚠ within organs, on part of the lines; also absent: CA13, NAALADL2, PLSCR2; co-absent with the target |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.377). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (24.9, -12.1); signed map (18.8, -0.3). **Vector** length 94.7, 23.3% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +14.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +8.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +0.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.4 | -6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.9 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -7.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.9 | -3.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | carbonic anhydrase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.2 — chr8:85,373,436-85,449,040 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Car3, CAIII |
| Gene groups (HGNC) | Carbonic anhydrases |
| Reactome | 1 pathways, smallest: Reversible hydration of carbon dioxide |
| Matched by | ensembl_id |

**Function**, from UniProt [P07451](https://www.uniprot.org/uniprotkb/P07451) (Carbonic anhydrase 3):

> Reversible hydration of carbon dioxide.

**Summary**, from NCBI Gene [761](https://www.ncbi.nlm.nih.gov/gene/761):

> Carbonic anhydrase III (CAIII) is a member of a multigene family (at least six separate genes are known) that encodes carbonic anhydrase isozymes. These carbonic anhydrases are a class of metalloenzymes that catalyze the reversible hydration of carbon dioxide and are differentially expressed in a number of cell types. The expression of the CA3 gene is strictly tissue specific and present at high levels in skeletal muscle and much lower levels in cardiac and smooth muscle. A proportion of …

**Accessions** — [HGNC:1374](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1374) · Entrez [761](https://www.ncbi.nlm.nih.gov/gene/761) · UniProt [P07451](https://www.uniprot.org/uniprotkb/P07451) · Ensembl [ENSG00000164879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164879)

## Data

Gene col 9018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9018); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9018]; `tensor/DDL_lfc|DDL_z.npy` [9018]; `embed/gene_vectors.npy` [9018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9018 or target_col == 9018). Every well: [[CA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

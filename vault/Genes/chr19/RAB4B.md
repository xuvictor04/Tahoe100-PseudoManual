---
symbol: "RAB4B"
type: "gene"
col: 9494
ensembl_id: "ENSG00000167578"
name: "RAB4B, member RAS oncogene family"
location: "19q13.2"
module: 37
arm: "+"
pooled_cpm: 19.68
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# RAB4B

*RAB4B, member RAS oncogene family* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.66× (z +19.8, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.520× (z -9.0, q 1e-16, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRSN2-AS1]] (+0.68, fdr 1e-05), [[GUCA1B]] (+0.62, fdr 1e-05), [[MAFG]] (+0.62, fdr 8e-06); moves opposite to [[MEST]] (-0.55, fdr 4e-05), [[TTLL12]] (-0.55, fdr 3e-05), [[PRPF19]] (-0.55, fdr 1e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +19.8 | 0e+00 | 43/46 (AsPC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.32×** | +11.3 | 5e-27 | 43/47 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.5 | 6e-06 | 2/48 (MIA PaCa-2, COLO 205) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.1 | 5e-05 | 20/44 (SW1417, HT-29, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.8 | 2e-04 | 23/48 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.3 | 0.002 | 22/46 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +4.2 | 0.002 | 18/47 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.006 | 15/46 (A549, C-33 A, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.010 | 11/47 (LS 180, LoVo, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +3.3 | 0.053 | 14/48 (NCI-H1792, hTERT-HPNE, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.26×** | +3.2 | 0.064 | 13/47 (H4, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.084 | 6/47 (A-427, LoVo, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.099 | 8/45 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | 1.16× | +3.0 | 0.099 | 12/48 (HS-578T, SW 900, …) | top dose only |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.099 | 6/47 (LS 180, HOP62, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9494.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.520×** | -9.0 | 1e-16 | 28/46 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.314×** | -8.7 | 1e-15 | 37/48 (SW480, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.667×** | -8.2 | 5e-14 | 30/48 (A-427, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.562×** | -7.7 | 2e-12 | 28/48 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.380×** | -7.2 | 5e-11 | 31/45 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.635×** | -6.5 | 8e-09 | 27/47 (LOX-IMVI, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.637×** | -6.5 | 8e-09 | 30/47 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.697×** | -4.8 | 1e-04 | 22/46 (PANC-1, LoVo, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -4.8 | 1e-04 | 21/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.725×** | -4.6 | 2e-04 | 21/47 (SW 1088, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.725×** | -4.4 | 5e-04 | 21/42 (HepG2/C3A, hTERT-HPNE, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.735×** | -4.4 | 5e-04 | 21/47 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.741×** | -4.3 | 8e-04 | 19/47 (HT-29, RKO, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.753×** | -4.1 | 0.002 | 19/47 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.767×** | -3.8 | 0.005 | 18/46 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 23.2 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.218× (z -10.1) |
| [[HT-29 (line)]] | alt | 46.3 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.21× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -20.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.247× (z -12.1) |
| [[LoVo (line)]] | wt | 18.8 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 27.7 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[SNU-423 (line)]] | alt | 14.2 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0976× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Bendamustine (drug)]] 5 µM 0.183× (z -9.0) |
| [[HOP62 (line)]] | alt | 18.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 14.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.44× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0654× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[HEC-1-A (line)]] | alt | 20.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.47× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 2 (1 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.101× (z -11.2) |
| [[KATO III (line)]] | alt | 26.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.288× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 10.3× (z +13.6) | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +9.7) | [[Harringtonine (drug)]] 5 µM 0.156× (z -10.4) |
| [[RKO (line)]] | wt | 9.73 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.0947× (z -9.9) ⚠ cell-cycle shift, explains ~22% of this change |
| [[SK-MEL-2 (line)]] | alt | 58.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.312× (z -9.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.440× (z -9.0) |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0894× (z -9.4) |
| [[A-172 (line)]] | wt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +11.0) | — |
| [[A-427 (line)]] | wt | 16.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.211× (z -14.5) |
| [[A498 (line)]] | wt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 18.3 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.0716× (z -8.8) |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.127× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 8.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 30.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.2) | — |
| [[J82 (line)]] | alt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.268× (z -9.0) |
| [[SW 900 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.32× (z +11.3) | — |
| [[SW480 (line)]] | alt | 22.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.97× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRSN2-AS1]] | +0.68 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[GUCA1B]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[MAFG]] | +0.62 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[SPAG7]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[NOXRED1]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[DNHD1]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[NMNAT1]] | +0.60 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[MON1B]] | +0.59 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[PGLS-DT]] | +0.59 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[TIRAP]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[BCL2L2-PABPN1]] | +0.58 | +0.36 / +0.60 | both halves | 1e-04 |  |
| [[LINC00685]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEST]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TTLL12]] | -0.55 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[PRPF19]] | -0.55 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[MTHFD1]] | -0.55 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[ZDHHC21]] | -0.54 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[HLTF]] | -0.54 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[NUBPL]] | -0.54 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[PTCD3]] | -0.54 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[DLD]] | -0.53 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[CDCA7L]] | -0.53 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[ATP5F1A]] | -0.53 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[C12orf29]] | -0.53 | -0.20 / -0.60 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RAB4B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.0, -21.0); signed map (5.7, 0.3). **Vector** length 100, 23.2% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +19.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.0 | +11.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.3 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +4.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.6 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +2.3 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.1 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | -4.3 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | -0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -7.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | RAB4B, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,778,216-40,796,942 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ78649, MGC52123 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Reactome | 6 pathways, smallest: MET receptor recycling; RAB geranylgeranylation; Signaling by MET |
| Matched by | ensembl_id |

**Function**, from UniProt [P61018](https://www.uniprot.org/uniprotkb/P61018) (Ras-related protein Rab-4B):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different set of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion (By similarity). RAB4B mediates endosomal tethering and fusion through the interaction with RUFY1 and RAB14. Acts as a …

**Summary**, from NCBI Gene [53916](https://www.ncbi.nlm.nih.gov/gene/53916):

> Enables G protein activity. Involved in D-glucose import across plasma membrane; early endosome to Golgi transport; and endosomal vesicle fusion. Located in insulin-responsive compartment; perinuclear region of cytoplasm; and recycling endosome. Is active in early endosome membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9782) · Entrez [53916](https://www.ncbi.nlm.nih.gov/gene/53916) · UniProt [P61018](https://www.uniprot.org/uniprotkb/P61018) · Ensembl [ENSG00000167578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167578)

## Data

Gene col 9494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9494); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9494]; `tensor/DDL_lfc|DDL_z.npy` [9494]; `embed/gene_vectors.npy` [9494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9494 or target_col == 9494). Every well: [[RAB4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

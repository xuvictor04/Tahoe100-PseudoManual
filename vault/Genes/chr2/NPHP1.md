---
symbol: "NPHP1"
type: "gene"
col: 6842
ensembl_id: "ENSG00000144061"
name: "nephrocystin 1"
location: "2q13"
module: 17
arm: "+"
pooled_cpm: 14.12
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 26
n_dd_up_clean: 15
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# NPHP1

*nephrocystin 1* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.18× (z +16.7, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.377× (z -14.0, q 7e-42, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC26]] (+0.79, fdr 7e-06), [[IFT22]] (+0.77, fdr 7e-06), [[DNAAF4]] (+0.70, fdr 7e-06); moves opposite to [[KLHL29]] (-0.63, fdr 1e-05), [[EPM2A]] (-0.62, fdr 2e-04), [[TBC1D4]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[DYNC2H1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.18×** | +16.7 | 0e+00 | 46/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.86×** | +15.2 | 0e+00 | 42/46 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.73×** | +14.5 | 3e-45 | 45/46 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +6.1 | 1e-07 | 28/46 (LS 180, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +5.3 | 1e-05 | 19/45 (HEC-1-A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +5.2 | 2e-05 | 17/43 (SW 900, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.96×** | +5.1 | 3e-05 | 19/46 (SW480, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +4.7 | 1e-04 | 22/46 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 3e-04 | 20/46 (HOP62, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.21×** | +3.9 | 0.005 | 16/46 (LS 180, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.011 | 12/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.020 | 5/46 (NCI-H1573, J82, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.035 | 9/46 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.041 | 9/45 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.053 | 12/45 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.056 | 9/46 (NCI-H23, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6842.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.377×** | -14.0 | 7e-42 | 40/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -13.2 | 2e-37 | 34/44 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.457×** | -11.3 | 3e-27 | 37/46 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.513×** | -9.6 | 1e-19 | 34/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -7.7 | 2e-12 | 26/38 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.615×** | -7.0 | 3e-10 | 28/46 (SW480, RPMI-7951, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.647×** | -6.3 | 3e-08 | 26/46 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -6.1 | 9e-08 | 25/43 (RPMI-7951, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.649×** | -6.0 | 2e-07 | 23/45 (SW480, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.693×** | -5.2 | 1e-05 | 17/45 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.709×** | -4.6 | 2e-04 | 17/45 (SW 1271, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.722×** | -4.6 | 2e-04 | 19/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.732×** | -4.5 | 3e-04 | 19/46 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.802×** | -4.5 | 3e-04 | 19/46 (MIA PaCa-2, CHP-212, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -4.3 | 7e-04 | 18/44 (HEC-1-A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -3.8 | 0.005 | 17/45 (RPMI-7951, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.781×** | -3.5 | 0.013 | 13/44 (Panc 03.27, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.781×** | -3.5 | 0.013 | 10/46 (PANC-1, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.647×** | -3.3 | 0.031 | 12/43 (Hs 766T, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.7 | 2 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -12.9) |
| [[SW480 (line)]] | alt | 12.8 | 3 | 3 | [[Panobinostat (drug)]] 5 µM 4.08× (z +10.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 23.0 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +16.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -9.6) |
| [[PANC-1 (line)]] | alt | 20.2 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.242× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -11.1) |
| [[A498 (line)]] | wt | 11.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.15× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 12.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +12.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.195× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -9.6) |
| [[A-172 (line)]] | wt | 23.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -10.4) |
| [[C32 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -9.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 19.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -10.0) |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.210× (z -9.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 7.78 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 16.0 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0518× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.235× (z -9.9) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0640× (z -10.2) |
| [[SNU-423 (line)]] | alt | 15.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -9.2) |
| [[SW 900 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC26]] | +0.79 | +0.68 / +0.73 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium |
| [[IFT22]] | +0.77 | +0.75 / +0.68 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium |
| [[DNAAF4]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[ASB8]] | +0.68 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[TBC1D19]] | +0.67 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[IFT52]] | +0.67 | +0.58 / +0.50 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 413 |
| [[GPATCH11]] | +0.66 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[DNAL1]] | +0.65 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[BBS5]] | +0.65 | +0.52 / +0.56 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 626 |
| [[ZNF205]] | +0.65 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[TMEM67]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 | pathway: Anchoring of the basal body to the plasma membrane; STRING 994 |
| [[CINP]] | +0.64 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL29]] | -0.63 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[EPM2A]] | -0.62 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[TBC1D4]] | -0.58 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[ZNF124]] | -0.57 | -0.16 / -0.40 | ⚠ not reproduced | 0.001 |  |
| [[SLC20A2]] | -0.57 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[NACC2]] | -0.55 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[PTPRG]] | -0.54 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[ATP11C]] | -0.54 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[JADE3]] | -0.53 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[RCC2]] | -0.53 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[RBPMS2]] | -0.53 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[PIGW]] | -0.53 | -0.23 / -0.36 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | B | DYNC2H1 activity raises NPHP1's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 2.86× lower at baseline in the lines without DYNC2H1 | 0.009 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[KLHL29]] | B | KLHL29 activity raises NPHP1's level | lines that do not express KLHL29 (7) vs lines expressing it (43) | 1.99× lower at baseline in the lines without KLHL29 | 0.032 | ⚠ within organs, on part of the lines; also absent: PCNX2, ENSG00000229983, ENSG00000271204; maybe low, not absent |
| [[ZNF594-DT]] | B | ZNF594-DT activity raises NPHP1's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 2.18× lower at baseline in the lines without ZNF594-DT | 0.037 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[ZNF567-DT]] | B | ZNF567-DT activity raises NPHP1's level | lines that do not express ZNF567-DT (6) vs lines expressing it (44) | 2.39× lower at baseline in the lines without ZNF567-DT | 0.055 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540 |
| [[BBS5]] | B | BBS5 activity raises NPHP1's level | lines that do not express BBS5 (6) vs lines expressing it (44) | 2.67× lower at baseline in the lines without BBS5 | 0.078 | ⚠ within organs, on part of the lines; also absent: GGT7, HLTF, FERMT2 |
| [[ZNF527]] | C | ZNF527 activity raises NPHP1's level | lines that do not express ZNF527 (3) vs lines expressing it (47) | 2.77× lower at baseline in the lines without ZNF527 | 0.028 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |
| [[CLIP3]] | C | CLIP3 activity raises NPHP1's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without CLIP3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.6, 0.2); signed map (-20.6, -18.5). **Vector** length 75.6, 15.0% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intraflagellar transport* (reactome, mean cos +0.64 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +0.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +16.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +15.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +5.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.2 | +14.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | -1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | +0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | nephrocystin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:110,122,311-110,205,066 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JBTS4, SLSN1; previously NPH1 |
| Gene groups (HGNC) | NPHP complex; SH3 domain containing |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [O15259](https://www.uniprot.org/uniprotkb/O15259) (Nephrocystin-1):

> Together with BCAR1 it may play a role in the control of epithelial cell polarity (By similarity). Involved in the organization of apical junctions in kidney cells together with NPHP4 and RPGRIP1L/NPHP8 (By similarity). Does not seem to be strictly required for ciliogenesis (By similarity). Seems to help to recruit PTK2B/PYK2 to cell matrix adhesions, thereby initiating phosphorylation of PTK2B/PYK2 and PTK2B/PYK2-dependent signaling (By similarity). May play a role in the regulation of …

**Summary**, from NCBI Gene [4867](https://www.ncbi.nlm.nih.gov/gene/4867):

> This gene encodes a protein with src homology domain 3 (SH3) patterns. This protein interacts with Crk-associated substrate, and it appears to function in the control of cell division, as well as in cell-cell and cell-matrix adhesion signaling, likely as part of a multifunctional complex localized in actin- and microtubule-based structures. Mutations in this gene cause familial juvenile nephronophthisis type 1, a kidney disorder involving both tubules and glomeruli. Defects in this gene are …

**Accessions** — [HGNC:7905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7905) · Entrez [4867](https://www.ncbi.nlm.nih.gov/gene/4867) · UniProt [O15259](https://www.uniprot.org/uniprotkb/O15259) · Ensembl [ENSG00000144061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144061)

## Data

Gene col 6842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6842); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6842]; `tensor/DDL_lfc|DDL_z.npy` [6842]; `embed/gene_vectors.npy` [6842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6842 or target_col == 6842). Every well: [[NPHP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPHP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "IFT46"
type: "gene"
col: 3963
ensembl_id: "ENSG00000118096"
name: "intraflagellar transport 46"
location: "11q23.3"
module: 28
arm: "+"
pooled_cpm: 8.79
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# IFT46

*intraflagellar transport 46* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +14.6, q 1e-45, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.417× (z -13.9, q 3e-41, down in 37 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.434× (z -13.3, q 7e-38, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C17orf75]] (+0.72, fdr 8e-06), [[ZSCAN21]] (+0.69, fdr 1e-05), [[PHYH]] (+0.68, fdr 1e-05); moves opposite to [[TRAPPC9]] (-0.57, fdr 4e-05), [[GMDS]] (-0.56, fdr 9e-05), [[LMBR1]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +14.6 | 1e-45 | 35/44 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +11.1 | 6e-26 | 11/18 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +9.7 | 5e-20 | 29/47 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.56×** | +7.1 | 2e-10 | 20/47 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +6.9 | 5e-10 | 19/32 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.8 | 1e-09 | 8/48 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 7e-05 | 17/46 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.4 | 6e-04 | 8/48 (KATO III, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 0.001 | 13/46 (NCI-H2347, PANC-1, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.002 | 10/47 (PANC-1, J82, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +4.1 | 0.002 | 7/42 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.27×** | +3.8 | 0.007 | 6/47 (SW1417, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.007 | 11/46 (NCI-H1573, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.5 | 0.019 | 8/38 (HCT15, HS-578T, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.5 | 0.020 | 9/47 (A-172, SW1417, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.048 | 9/41 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.052 | 3/47 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.071 | 5/47 (SW480, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3963.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.417×** | -13.9 | 3e-41 | 37/43 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.434×** | -13.3 | 7e-38 | 40/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.434×** | -13.3 | 7e-38 | 38/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.492×** | -11.3 | 3e-27 | 34/45 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.629×** | -7.4 | 2e-11 | 23/46 (NCI-H23, COLO 205, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.662×** | -6.3 | 3e-08 | 21/37 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.730×** | -5.0 | 4e-05 | 15/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.786×** | -3.8 | 0.009 | 12/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.808×** | -3.4 | 0.036 | 12/46 (C32, SW 1271, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.808×** | -3.4 | 0.036 | 9/46 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.665×** | -3.4 | 0.036 | 10/42 (LOX-IMVI, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | **0.823×** | -3.1 | 0.092 | 6/47 (A-427, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.819×** | -3.1 | 0.098 | 6/47 (MIA PaCa-2, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.1 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -12.6) |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0878× (z -10.8) |
| [[H4 (line)]] | wt | 12.9 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0993× (z -9.2) |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0832× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 7.16 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0981× (z -9.8) |
| [[PANC-1 (line)]] | alt | 4.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +9.5) | — |
| [[RKO (line)]] | wt | 6.52 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0708× (z -8.5) |
| [[SHP-77 (line)]] | alt | 9.04 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0658× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C17orf75]] | +0.72 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[ZSCAN21]] | +0.69 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[PHYH]] | +0.68 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[COQ5]] | +0.65 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[ZNF563]] | +0.64 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ZDHHC17]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ACAD11]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[RAD52]] | +0.64 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[FUNDC1]] | +0.62 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[NDUFAF1]] | +0.61 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[KCTD18]] | +0.61 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[FBXO8]] | +0.61 | +0.67 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC9]] | -0.57 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[GMDS]] | -0.56 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[LMBR1]] | -0.56 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[SLC25A5]] | -0.54 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[ARHGAP8]] | -0.54 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[PIP4K2A]] | -0.52 | -0.61 / -0.27 | both halves | 3e-04 |  |
| [[PAQR4]] | -0.52 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[FOXK2]] | -0.52 | -0.57 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.0, 7.0); signed map (7.5, -23.1). **Vector** length 59.2, 8.24% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.7 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +14.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +11.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +3.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -13.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -11.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -13.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | +1.2 |
|  | [[Acetohexamide (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 46 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,544,528-118,572,970 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C11orf2, FLJ21827, FAP32, CFAP32; previously C11orf60 |
| Gene groups (HGNC) | Cilia and flagella associated; IFT-B1 complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQC8](https://www.uniprot.org/uniprotkb/Q9NQC8) (Intraflagellar transport protein 46 homolog):

> Forms part of a complex involved in intraflagellar transport (IFT), the bi-directional movement of particles required for the assembly, maintenance and functioning of primary cilia. May play a role in chondrocyte maturation and skeletogenesis (By similarity).

**Summary**, from NCBI Gene [56912](https://www.ncbi.nlm.nih.gov/gene/56912):

> Predicted to be involved in cilium assembly; intraciliary transport; and protein stabilization. Predicted to act upstream of or within smoothened signaling pathway. Located in cytoplasm. Part of intraciliary transport particle A. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26146](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26146) · Entrez [56912](https://www.ncbi.nlm.nih.gov/gene/56912) · UniProt [Q9NQC8](https://www.uniprot.org/uniprotkb/Q9NQC8) · Ensembl [ENSG00000118096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118096)

## Data

Gene col 3963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3963); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3963]; `tensor/DDL_lfc|DDL_z.npy` [3963]; `embed/gene_vectors.npy` [3963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3963 or target_col == 3963). Every well: [[IFT46 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFT46.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

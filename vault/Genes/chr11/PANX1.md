---
symbol: "PANX1"
type: "gene"
col: 3123
ensembl_id: "ENSG00000110218"
name: "pannexin 1"
location: "11q21"
module: 98
arm: "+"
pooled_cpm: 32.87
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# PANX1

*pannexin 1* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.61× (z +14.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.496× (z -10.2, q 1e-21, down in 25 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.601× (z -7.7, q 3e-12, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXN2]] (+0.62, fdr 7e-06), [[BCL2L1]] (+0.60, fdr 8e-06), [[TBRG4]] (+0.60, fdr 1e-05); moves opposite to [[TULP3]] (-0.52, fdr 3e-05), [[ULK1]] (-0.48, fdr 6e-05), [[PNISR]] (-0.46, fdr 5e-05).
> It is in [[Module 098]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3123.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.61×** | +14.9 | 0e+00 | 46/48 (PANC-1, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.18×** | +6.2 | 2e-07 | 26/46 (C32, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.005 | 20/48 (HOP62, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.007 | 21/48 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.012 | 21/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +3.4 | 0.053 | 8/48 (KATO III, HepG2/C3A, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.4 | 0.056 | 12/33 (SNU-423, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3123.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.496×** | -10.2 | 1e-21 | 25/35 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.544×** | -9.2 | 1e-17 | 33/45 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.601×** | -7.7 | 3e-12 | 34/48 (NCI-H1792, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.647×** | -6.6 | 8e-09 | 29/48 (LOX-IMVI, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.672×** | -5.8 | 9e-07 | 33/48 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -5.4 | 5e-06 | 29/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.718×** | -5.0 | 5e-05 | 24/48 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.557×** | -4.6 | 3e-04 | 26/47 (SNU-1, SW480, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.755×** | -4.2 | 0.001 | 19/48 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.748×** | -4.2 | 0.001 | 21/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.763×** | -4.1 | 0.002 | 24/48 (KATO III, Hs 766T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.768×** | -4.0 | 0.003 | 18/47 (SW480, LoVo, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.785×** | -3.7 | 0.011 | 18/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.799×** | -3.4 | 0.029 | 13/47 (AN3 CA, SNU-423, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.727×** | -3.3 | 0.035 | 15/46 (C32, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.814×** | -3.1 | 0.067 | 17/48 (LoVo, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3123. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 66.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 27.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.49× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -13.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 46.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.35× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -9.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 15.0 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 23.2× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 25.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -10.3) |
| [[LoVo (line)]] | wt | 37.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.358× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 20.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 48.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -15.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 26.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.5) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 13.0× (z +9.8) | — |
| [[SW480 (line)]] | alt | 36.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.55× (z +9.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -9.0) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 21.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0802× (z -17.2) |
| [[A549 (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0907× (z -15.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -10.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 42.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.60× (z +8.7) | — |
| [[J82 (line)]] | alt | 73.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.95× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 22.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0800× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 12.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.2) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[RPMI-7951 (line)]] | alt | 55.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.9× (z +9.9) | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0945× (z -10.5) ⚠ transcription drop; cell-cycle shift, explains ~64% of this change |
| [[A-172 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3123), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXN2]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[BCL2L1]] | +0.60 | +0.62 / +0.57 | both halves | 8e-06 | pathway: Inflammasomes |
| [[TBRG4]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TTPAL]] | +0.56 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[COQ8B]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[SNAI2]] | +0.54 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ADAMTS9]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[LTBR]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[USP31]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[UBE2N]] | +0.52 | +0.54 / +0.50 | both halves | 1e-05 | pathway: Nucleotide-binding domain, leucine rich repeat containing receptor (NLR) signaling pathways |
| [[B3GNT5]] | +0.52 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[HNRNPF]] | +0.51 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TULP3]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[ULK1]] | -0.48 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[PNISR]] | -0.46 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[FBXL20]] | -0.46 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[AKAP9]] | -0.46 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[BSDC1]] | -0.46 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[BRWD1]] | -0.46 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[MRPS6]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TMEM167B]] | -0.44 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[TMF1]] | -0.44 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[GABARAPL2]] | -0.44 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[TESK2]] | -0.43 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.4, 7.2); signed map (8.7, 34.1). **Vector** length 108, 27.5% of its response variance represented; |z| ≥ 3 in 1,102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.5 | +14.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.6 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +3.7 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +3.5 | +4.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +3.3 | +2.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.2 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.5 | -5.0 |
|  | [[NG25 (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.4 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | pannexin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:94,128,841-94,181,968 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRS1, UNQ2529, PX1 |
| Gene groups (HGNC) | Pannexins |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 12 pathways, smallest: Electric Transmission Across Gap Junctions; Transmission across Electrical Synapses; The NLRP3 inflammasome |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RD7](https://www.uniprot.org/uniprotkb/Q96RD7) (Pannexin-1):

> Ion channel involved in a variety of physiological functions such as blood pressure regulation, apoptotic cell clearance and oogenesis. Forms anion-selective channels with relatively low conductance and an order of permeabilities: nitrate>iodide>chlroride>>aspartate=glutamate=gluconate (By similarity). Can release ATP upon activation through phosphorylation or cleavage at C-terminus. May play a role as a Ca(2+)-leak channel to regulate ER Ca(2+) homeostasis.; [Caspase-activated pannexin-1]: …

**Summary**, from NCBI Gene [24145](https://www.ncbi.nlm.nih.gov/gene/24145):

> The protein encoded by this gene belongs to the innexin family. Innexin family members are the structural components of gap junctions. This protein and pannexin 2 are abundantly expressed in central nerve system (CNS) and are coexpressed in various neuronal populations. Studies in Xenopus oocytes suggest that this protein alone and in combination with pannexin 2 may form cell type-specific gap junctions with distinct properties. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8599) · Entrez [24145](https://www.ncbi.nlm.nih.gov/gene/24145) · UniProt [Q96RD7](https://www.uniprot.org/uniprotkb/Q96RD7) · Ensembl [ENSG00000110218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110218)

## Data

Gene col 3123: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3123); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3123, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3123]; `tensor/DDL_lfc|DDL_z.npy` [3123]; `embed/gene_vectors.npy` [3123]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3123 or target_col == 3123). Every well: [[PANX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PANX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

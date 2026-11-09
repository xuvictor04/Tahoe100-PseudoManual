---
symbol: "PPP1R9B"
type: "gene"
col: 2997
ensembl_id: "ENSG00000108819"
name: "protein phosphatase 1 regulatory subunit 9B"
location: "17q21.33"
module: 126
arm: "+"
pooled_cpm: 24.46
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# PPP1R9B

*protein phosphatase 1 regulatory subunit 9B* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.72× (z +5.2, q 9e-05, up in 27 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.29× (z +4.6, q 5e-04, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.631× (z -5.8, q 3e-06, down in 32 of 46 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.634× (z -5.7, q 3e-06, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTA2]] (+0.69, fdr 7e-06), [[CCAR2]] (+0.64, fdr 2e-05), [[ATP13A1]] (+0.59, fdr 3e-05); moves opposite to [[PSMA7]] (-0.53, fdr 7e-05), [[ADGRL3-AS1]] (-0.50, fdr 4e-05), [[CSTB]] (-0.49, fdr 4e-05).
> It is in [[Module 126]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2997.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +5.2 | 9e-05 | 27/42 (MIA PaCa-2, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +5.1 | 1e-04 | 27/45 (LoVo, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.49×** | +4.9 | 2e-04 | 22/33 (Hs 766T, MIA PaCa-2, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +4.8 | 2e-04 | 24/40 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.6 | 5e-04 | 25/47 (A-427, A549, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +4.5 | 6e-04 | 23/46 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.28×** | +4.4 | 9e-04 | 22/47 (A549, SW480, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 0.001 | 25/46 (J82, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +4.1 | 0.003 | 19/47 (CFPAC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.32×** | +3.6 | 0.020 | 15/46 (HT-29, J82, …) | inconsistent across doses | position effect removed |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.029 | 14/47 (J82, HCT15, …) | inconsistent across doses | position effect removed |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.063 | 10/47 (HT-29, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2997.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.631×** | -5.8 | 3e-06 | 32/46 (A498, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.634×** | -5.7 | 3e-06 | 29/47 (LS 180, KATO III, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -4.6 | 6e-04 | 26/46 (LS 180, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.771×** | -4.6 | 6e-04 | 26/47 (BT-474, A-427, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.693×** | -4.3 | 0.002 | 26/47 (BT-474, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.710×** | -4.3 | 0.002 | 21/46 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.740×** | -3.8 | 0.013 | 22/47 (J82, SHP-77, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.738×** | -3.7 | 0.018 | 14/46 (BT-474, NCI-H23, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.822×** | -3.5 | 0.033 | 18/47 (NCI-H1573, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2997. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 30.4 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.68× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 25.4 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.107× (z -10.4) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Brimonidine (drug)]] 0.5 µM 0.161× (z -8.8) |
| [[A-172 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.4) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 23.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -15.3) ⚠ cell-cycle shift, explains ~76% of this change |
| [[A549 (line)]] | wt | 17.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +10.4) ⚠ cell-cycle shift, explains ~21% of this change | — |
| [[AN3 CA (line)]] | alt | 30.7 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0748× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +9.6) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[CHP-212 (line)]] | wt | 74.9 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.106× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 17.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +9.1) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.240× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -8.7) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H460 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -12.0) ⚠ cell-cycle shift, explains ~44% of this change |
| [[RKO (line)]] | wt | 24.6 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.124× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -12.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2997), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTA2]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[CCAR2]] | +0.64 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[ATP13A1]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[LDB1]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[AGPAT1]] | +0.57 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PRRC2A]] | +0.56 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[NOP9]] | +0.56 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[AGRN]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[SZRD1]] | +0.55 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[MLLT1]] | +0.55 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[WASH8P]] ⚠ | +0.55 | +0.43 / +0.58 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZBED6]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA7]] | -0.53 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[ADGRL3-AS1]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CSTB]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[UBE2B]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[MRPS36]] ⚠ | -0.47 | -0.36 / -0.47 | both halves | 9e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CAMLG]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[NACA4P]] ⚠ | -0.46 | -0.34 / -0.43 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PNPLA8]] | -0.46 | -0.53 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.2, -25.8); signed map (-13.0, -34.4). **Vector** length 94.4, 21.4% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.6 | +5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +4.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.5 | +2.8 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Artesunate (drug)]] 0.05 µM |  | +2.3 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +1.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.3 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.6 | -4.6 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -3.5 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.6 | -2.2 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 9B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,133,737-50,150,677 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Spn, SPINO; previously PPP1R6, PPP1R9 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SB3](https://www.uniprot.org/uniprotkb/Q96SB3) (Neurabin-2):

> Seems to act as a scaffold protein in multiple signaling pathways. Modulates excitatory synaptic transmission and dendritic spine morphology. Binds to actin filaments (F-actin) and shows cross-linking activity. Binds along the sides of the F-actin. May play an important role in linking the actin cytoskeleton to the plasma membrane at the synaptic junction. Believed to target protein phosphatase 1/PP1 to dendritic spines, which are rich in F-actin, and regulates its specificity toward ion …

**Summary**, from NCBI Gene [84687](https://www.ncbi.nlm.nih.gov/gene/84687):

> This gene encodes a scaffold protein that functions as a regulatory subunit of protein phosphatase 1a. Expression of this gene is particularly high in dendritic spines, suggesting that the encoded protein may play a role in receiving signals from the central nervous system. The encoded protein has putative tumor suppressor function and decreased expression has been observed in tumors. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:9298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9298) · Entrez [84687](https://www.ncbi.nlm.nih.gov/gene/84687) · UniProt [Q96SB3](https://www.uniprot.org/uniprotkb/Q96SB3) · Ensembl [ENSG00000108819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108819)

## Data

Gene col 2997: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2997); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2997, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2997]; `tensor/DDL_lfc|DDL_z.npy` [2997]; `embed/gene_vectors.npy` [2997]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2997 or target_col == 2997). Every well: [[PPP1R9B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R9B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

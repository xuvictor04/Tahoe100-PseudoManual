---
symbol: "TRMO"
type: "gene"
col: 5940
ensembl_id: "ENSG00000136932"
name: "tRNA methyltransferase O"
location: "9q22.33"
module: 51
arm: "+"
pooled_cpm: 9.65
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# TRMO

*tRNA methyltransferase O* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.31× (z +15.7, q 0e+00, up in 37 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.422× (z -11.5, q 1e-27, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YJU2]] (+0.79, fdr 7e-06), [[LANCL2]] (+0.77, fdr 7e-06), [[COQ7]] (+0.77, fdr 7e-06); moves opposite to [[PCMT1]] (-0.65, fdr 5e-05), [[LPCAT4]] (-0.64, fdr 4e-05), [[HEBP1]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5940.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +15.7 | 0e+00 | 37/45 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.66×** | +9.5 | 5e-19 | 34/48 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.75×** | +7.0 | 4e-10 | 30/47 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +6.8 | 2e-09 | 29/46 (SNU-423, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.8 | 7e-07 | 24/44 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +5.6 | 2e-06 | 21/46 (NCI-H1573, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +5.5 | 4e-06 | 13/27 (A498, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +5.2 | 1e-05 | 21/44 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.0 | 3e-05 | 18/41 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.6 | 2e-04 | 3/48 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.39×** | +4.3 | 8e-04 | 16/46 (LOX-IMVI, RKO, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.004 | 12/47 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.024 | 7/44 (A498, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.1 | 0.072 | 6/47 (A-172, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.26×** | +3.1 | 0.081 | 6/48 (J82, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5940.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.422×** | -11.5 | 1e-27 | 45/47 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.495×** | -9.3 | 3e-18 | 35/45 (C-33 A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.496×** | -9.3 | 3e-18 | 37/47 (NCI-H1792, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.580×** | -7.2 | 7e-11 | 31/47 (COLO 205, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~24% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -6.4 | 1e-08 | 28/46 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -6.2 | 5e-08 | 19/40 (SNU-423, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -4.7 | 2e-04 | 23/45 (RPMI-7951, SW 900, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.705×** | -4.6 | 2e-04 | 17/47 (NCI-H1792, COLO 205, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.792×** | -4.4 | 8e-04 | 15/48 (LoVo, SW48, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.758×** | -3.7 | 0.014 | 18/46 (A549, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.591×** | -3.6 | 0.014 | 13/48 (SW1417, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ritonavir (drug)]] 0.5 µM |  | **0.766×** | -3.5 | 0.020 | 11/45 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.781×** | -3.3 | 0.047 | 16/46 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 13.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +10.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0951× (z -13.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 8.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 6.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 1 | — | [[Arbutin (drug)]] 0.05 µM 0.0576× (z -10.6) |
| [[COLO 205 (line)]] | alt | 24.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.228× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 5.74 | 0 | 1 | — | [[5-Fluorouracil (drug)]] 0.5 µM 0.0415× (z -11.0) |
| [[J82 (line)]] | alt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +13.9) | — |
| [[LS 180 (line)]] | wt | 9.66 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 7.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 9.68 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.141× (z -9.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.5) | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -8.6) |
| [[SW48 (line)]] | wt | 14.2 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0707× (z -9.7) |
| [[A-427 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YJU2]] | +0.79 | +0.84 / +0.59 | both halves | 7e-06 |  |
| [[LANCL2]] | +0.77 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[COQ7]] | +0.77 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[RBM23]] | +0.75 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[POLR2M]] | +0.75 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[RABL3]] | +0.74 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[TOR1AIP1]] | +0.73 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[EPC2]] | +0.72 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[DNAJB12]] | +0.71 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[ZNF268]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[NUBP1]] | +0.70 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.70 | +0.70 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | -0.65 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[LPCAT4]] | -0.64 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[HEBP1]] | -0.64 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[CAMTA1]] | -0.63 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[STRN]] | -0.62 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[HDAC3]] | -0.62 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[MAP3K3]] | -0.60 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[KIAA1958]] | -0.60 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[PIGF]] | -0.60 | -0.68 / -0.39 | both halves | 5e-05 |  |
| [[HYCC2]] | -0.60 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[EPS15]] | -0.59 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[GMCL1]] | -0.59 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.6, 11.1); signed map (12.1, -29.8). **Vector** length 88.8, 17.2% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +15.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.3 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +5.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +1.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.8 | -9.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.3 | -9.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.6 | -11.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -3.1 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.8 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase O |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:97,904,489-97,922,500 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC219; previously C9orf156 |
| Gene groups (HGNC) | DNA/RNA methyltransferases; Methyltransferases with unique structures |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BU70](https://www.uniprot.org/uniprotkb/Q9BU70) (tRNA):

> S-adenosyl-L-methionine-dependent methyltransferase responsible for the addition of the methyl group in the formation of N6-methyl-N6-threonylcarbamoyladenosine at position 37 (m(6)t(6)A37) of the tRNA anticodon loop of tRNA(Ser)(GCU). The methyl group of m(6)t(6)A37 may improve the efficiency of the tRNA decoding ability (By similarity).

**Summary**, from NCBI Gene [51531](https://www.ncbi.nlm.nih.gov/gene/51531):

> Enables tRNA (L-threonylcarbamoyladenosine(37)-C2) methyltransferase activity. Involved in tRNA methylation. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30967) · Entrez [51531](https://www.ncbi.nlm.nih.gov/gene/51531) · UniProt [Q9BU70](https://www.uniprot.org/uniprotkb/Q9BU70) · Ensembl [ENSG00000136932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136932)

## Data

Gene col 5940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5940); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5940]; `tensor/DDL_lfc|DDL_z.npy` [5940]; `embed/gene_vectors.npy` [5940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5940 or target_col == 5940). Every well: [[TRMO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

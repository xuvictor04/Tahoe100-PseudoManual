---
symbol: "ZNF35"
type: "gene"
col: 9887
ensembl_id: "ENSG00000169981"
name: "zinc finger protein 35"
location: "3p21.31"
module: 114
arm: "+"
pooled_cpm: 9.35
n_lines_expressing: 48
n_dd_up: 36
n_dd_down: 5
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# ZNF35

*zinc finger protein 35* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.07× (z +25.5, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Glycyrrhizic acid (drug)]] 0.05 µM: 0.694× (z -5.4, q 3e-05, down in 18 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 0.0736×, HEC-1-A 0.0804×, A-172 0.154×, hTERT-HPNE 0.124×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.225×, SNU-423 0.118×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.0980×, MIA PaCa-2 0.130×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF16]] (+0.69, fdr 1e-05), [[ZNF3]] (+0.68, fdr 7e-06), [[ALKBH1]] (+0.66, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.07×** | +25.5 | 0e+00 | 42/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **13.7×** | +22.0 | 0e+00 | 41/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.92×** | +17.2 | 0e+00 | 35/41 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +14.6 | 0e+00 | 32/42 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.56×** | +14.5 | 1e-45 | 32/39 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.47×** | +14.3 | 3e-44 | 35/42 (SW480, LS 180, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.10×** | +11.9 | 7e-31 | 32/45 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.91×** | +10.4 | 2e-23 | 32/45 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.89×** | +10.2 | 2e-22 | 27/43 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.95×** | +10.1 | 3e-22 | 29/44 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.85×** | +9.9 | 2e-21 | 34/45 (LoVo, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.77×** | +9.2 | 2e-18 | 27/45 (SNU-423, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +9.0 | 9e-18 | 32/43 (C32, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.70×** | +8.5 | 5e-16 | 27/45 (PANC-1, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +7.7 | 4e-13 | 21/44 (HOP62, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +7.2 | 2e-11 | 19/45 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +6.9 | 1e-10 | 26/44 (KATO III, SHP-77, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +6.9 | 2e-10 | 18/45 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.39×** | +5.0 | 1e-05 | 14/44 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9887.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 0.0736×, HEC-1-A 0.0804×, A-172 0.154×, hTERT-HPNE 0.124×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.225×, SNU-423 0.118×; ⚠ toxic; transcription drop); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.0980×, MIA PaCa-2 0.130×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **0.694×** | -5.4 | 3e-05 | 18/42 (NCI-H2030, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **0.748×** | -4.7 | 8e-04 | 14/44 (C-33 A, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.758×** | -4.3 | 0.003 | 11/19 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.804×** | -3.5 | 0.057 | 8/46 (SW 1088, PANC-1, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 0.05 µM |  | **0.792×** | -3.5 | 0.057 | 6/44 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[Adenosine (drug)]] 5 µM |  | 0.873× | -3.1 | 0.18 | 9/46 (NCI-H1573, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 9.53 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +10.6) | [[Docetaxel (drug)]] 0.05 µM 0.105× (z -12.9) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 9.94 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 10.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0736× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 12.2 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 26.8× (z +13.7) | — |
| [[NCI-H1573 (line)]] | alt | 6.69 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +10.1) | — |
| [[A-172 (line)]] | wt | 9.16 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -9.5) ⚠ cell-cycle shift, explains ~94% of this change |
| [[A-427 (line)]] | wt | 11.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 24.8× (z +9.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~52% of this change |
| [[LoVo (line)]] | wt | 9.07 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 7.21 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.2) | — |
| [[A549 (line)]] | wt | 6.83 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 9.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0804× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 7.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.39 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.130× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 8.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.7× (z +8.7) | — |
| [[RKO (line)]] | wt | 20.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 21.0× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0980× (z -10.0) |
| [[SNU-423 (line)]] | alt | 8.35 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -9.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF16]] | +0.69 | +0.53 / +0.70 | both halves | 1e-05 | same gene group |
| [[ZNF3]] | +0.68 | +0.68 / +0.61 | both halves | 7e-06 | same gene group |
| [[ALKBH1]] | +0.66 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ALKBH4]] | +0.65 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ZNF653]] | +0.64 | +0.41 / +0.57 | both halves | 4e-05 | same gene group |
| [[ZNF721]] | +0.64 | +0.64 / +0.53 | both halves | 1e-05 | same gene group |
| [[ZNF271P]] | +0.64 | +0.69 / +0.45 | both halves | 3e-05 | same gene group |
| [[ZNF329]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 | same gene group |
| [[TRIM4]] | +0.63 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[MTG2]] | +0.63 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[LLPH]] | +0.63 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[ZNF75A]] | +0.63 | +0.73 / +0.44 | both halves | 3e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.4, 5.5); signed map (-5.2, -13.6). **Vector** length 61.3, 9.51% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +14.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +22.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +25.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +14.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +14.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +7.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +1.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | -3.6 | +3.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | +2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.4 | +6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.4 | +10.4 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.4 | +0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:44,648,732-44,660,791 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HF.10, HF10, Zfp105 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P13682](https://www.uniprot.org/uniprotkb/P13682) (Zinc finger protein 35):

> May be involved in transcriptional regulation. Involved in cell differentiation and/or proliferation.

**Summary**, from NCBI Gene [7584](https://www.ncbi.nlm.nih.gov/gene/7584):

> Enables DNA-binding transcription factor activity and sequence-specific DNA binding activity. Predicted to be involved in cellular response to retinoic acid; regulation of transcription by RNA polymerase II; and spermatogenesis. Located in nucleus and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13099](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13099) · Entrez [7584](https://www.ncbi.nlm.nih.gov/gene/7584) · UniProt [P13682](https://www.uniprot.org/uniprotkb/P13682) · Ensembl [ENSG00000169981](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169981)

## Data

Gene col 9887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9887); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9887]; `tensor/DDL_lfc|DDL_z.npy` [9887]; `embed/gene_vectors.npy` [9887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9887 or target_col == 9887). Every well: [[ZNF35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

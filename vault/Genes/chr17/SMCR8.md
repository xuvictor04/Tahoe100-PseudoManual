---
symbol: "SMCR8"
type: "gene"
col: 10777
ensembl_id: "ENSG00000176994"
name: "SMCR8-C9orf72 complex subunit"
location: "17p11.2"
module: 7
arm: "+"
pooled_cpm: 24.03
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 22
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SMCR8

*SMCR8-C9orf72 complex subunit* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.32× (z +12.2, q 3e-31, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.726× (z -6.5, q 4e-08, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.199×, SNU-423 0.257×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.121×, A-172 0.213×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (HCT15 0.0623×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (AN3 CA 0.116×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM199]] (+0.74, fdr 7e-06), [[AKT1S1]] (+0.69, fdr 7e-06), [[VPS11]] (+0.69, fdr 7e-06); moves opposite to [[KIF3A]] (-0.60, fdr 1e-04), [[POLB]] (-0.59, fdr 5e-05), [[PCMT1]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10777.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.32×** | +12.2 | 3e-31 | 44/47 (HOP62, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +11.3 | 5e-27 | 34/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +8.7 | 9e-16 | 35/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.61×** | +7.2 | 7e-11 | 38/48 (NCI-H23, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +7.1 | 2e-10 | 32/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +6.9 | 5e-10 | 34/48 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.1 | 8e-08 | 31/48 (HOP62, PANC-1, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +6.1 | 8e-08 | 30/47 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +6.0 | 1e-07 | 29/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.10×** | +5.6 | 1e-06 | 31/47 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +5.3 | 7e-06 | 28/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +5.2 | 1e-05 | 27/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 4e-05 | 22/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 8e-05 | 21/47 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.39×** | +4.5 | 2e-04 | 20/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +4.3 | 5e-04 | 21/47 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10777.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.199×, SNU-423 0.257×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.121×, A-172 0.213×); [[Palmatine (chloride) (drug)]] 0.5 µM in 1 line (HCT15 0.0623×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (AN3 CA 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.726×** | -6.5 | 4e-08 | 34/48 (SW480, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.691×** | -5.3 | 3e-05 | 27/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.592×** | -4.0 | 0.014 | 12/29 (SW480, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.776×** | -3.7 | 0.037 | 20/47 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.4 | 0.079 | 2/48 (HEC-1-A, NCI-H661) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.795× | -3.2 | 0.13 | 15/47 (RKO, Hs 766T, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.856× | -3.2 | 0.13 | 10/48 (RKO, NCI-H2030, …) | top dose only |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.860× | -3.1 | 0.16 | 9/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +17.6) | — |
| [[A-172 (line)]] | wt | 23.7 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -10.2) |
| [[RKO (line)]] | wt | 23.8 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -12.6) |
| [[A498 (line)]] | wt | 31.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 15.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 31.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 45.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.11× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 32.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 36.1 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.116× (z -8.7) |
| [[COLO 205 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 29.7 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0623× (z -15.7) |
| [[HEC-1-A (line)]] | alt | 14.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.87× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 16.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.09× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +12.3) | — |
| [[J82 (line)]] | alt | 34.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.6) | — |
| [[LoVo (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 22.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +12.4) | — |
| [[A-427 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM199]] | +0.74 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[AKT1S1]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[VPS11]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[GBA1]] | +0.69 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[DNAJB12]] | +0.67 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[RNF6]] | +0.66 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[LINC00571]] | +0.66 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[GTF2H1]] | +0.66 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[BLOC1S3]] | +0.66 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[ZFYVE26]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[ZNF543]] | +0.65 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ATXN1L]] | +0.64 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF3A]] | -0.60 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[POLB]] | -0.59 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[PCMT1]] | -0.58 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[INPP5F]] | -0.58 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[OSTF1]] | -0.58 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[DNAJC1]] | -0.56 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ANAPC11]] | -0.56 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[RASA2]] | -0.56 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[POGLUT2]] | -0.56 | -0.50 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.9, 14.3); signed map (5.3, -29.2). **Vector** length 108, 26.4% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +12.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +6.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +7.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.6 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +5.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.8 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.0 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.9 | -5.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -3.2 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | SMCR8-C9orf72 complex subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,315,293-18,328,056 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34716, DENND8A |
| Gene groups (HGNC) | DENN domain containing; SWC tripartite complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEV9](https://www.uniprot.org/uniprotkb/Q8TEV9) (Guanine nucleotide exchange protein SMCR8):

> Component of the C9orf72-SMCR8 complex, a complex that has guanine nucleotide exchange factor (GEF) activity and regulates autophagy. In the complex, C9orf72 and SMCR8 probably constitute the catalytic subunits that promote the exchange of GDP to GTP, converting inactive GDP-bound RAB8A and RAB39B into their active GTP-bound form, thereby promoting autophagosome maturation. The C9orf72-SMCR8 complex also acts as a negative regulator of autophagy initiation by interacting with the ULK1/ATG1 …

**Summary**, from NCBI Gene [140775](https://www.ncbi.nlm.nih.gov/gene/140775):

> Enables GTPase activator activity; protein kinase binding activity; and protein kinase inhibitor activity. Contributes to guanyl-nucleotide exchange factor activity. Involved in negative regulation of gene expression; regulation of TOR signaling; and regulation of macroautophagy. Located in Atg1/ULK1 kinase complex; chromatin; and nucleoplasm. Part of guanyl-nucleotide exchange factor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17921) · Entrez [140775](https://www.ncbi.nlm.nih.gov/gene/140775) · UniProt [Q8TEV9](https://www.uniprot.org/uniprotkb/Q8TEV9) · Ensembl [ENSG00000176994](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176994)

## Data

Gene col 10777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10777); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10777]; `tensor/DDL_lfc|DDL_z.npy` [10777]; `embed/gene_vectors.npy` [10777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10777 or target_col == 10777). Every well: [[SMCR8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMCR8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

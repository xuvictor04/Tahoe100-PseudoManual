---
symbol: "PYM1"
type: "gene"
col: 9960
ensembl_id: "ENSG00000170473"
name: "PYM1 exon junction complex associated factor"
location: "12q13.2"
module: 16
arm: "+"
pooled_cpm: 10.79
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# PYM1

*PYM1 exon junction complex associated factor* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.33× (z +13.9, q 6e-41, up in 36 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.84× (z +8.8, q 3e-16, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.444× (z -11.8, q 2e-29, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHAMP1]] (+0.71, fdr 7e-06), [[INTS14]] (+0.70, fdr 1e-05), [[UTP3]] (+0.70, fdr 1e-05); moves opposite to [[GNB2]] (-0.68, fdr 1e-05), [[DCUN1D4]] (-0.63, fdr 1e-05), [[HEBP1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9960.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.33×** | +13.9 | 6e-41 | 36/48 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +8.8 | 3e-16 | 30/46 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.6 | 1e-08 | 24/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +6.2 | 6e-08 | 22/45 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +5.4 | 7e-06 | 20/47 (PANC-1, A-427, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.7 | 2e-04 | 17/43 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.4 | 8e-04 | 17/45 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.4 | 0.041 | 11/40 (Panc 03.27, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM | ⚠ unreliable plate only; position correction uncertain | **1.26×** | +3.3 | 0.055 | 4/47 (KATO III, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 1.50× | +3.0 | 0.13 | 9/46 (HOP62, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 1.23× | +3.0 | 0.13 | 6/44 (HEC-1-A, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9960.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.444×** | -11.8 | 2e-29 | 37/47 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.490×** | -10.4 | 8e-23 | 38/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.535×** | -9.1 | 2e-17 | 33/47 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.580×** | -7.7 | 2e-12 | 29/47 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.643×** | -6.4 | 1e-08 | 22/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -6.1 | 1e-07 | 24/45 (LS 180, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.765×** | -5.5 | 2e-06 | 21/45 (A-427, NCI-H460, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.691×** | -5.4 | 5e-06 | 18/46 (HOP62, LoVo, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.706×** | -4.9 | 6e-05 | 18/41 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.706×** | -4.8 | 1e-04 | 17/43 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -4.4 | 5e-04 | 17/44 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.747×** | -4.2 | 0.001 | 13/47 (LoVo, LS 180, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.766×** | -3.9 | 0.005 | 18/46 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.763×** | -3.8 | 0.006 | 17/44 (RKO, BT-474, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.615×** | -3.7 | 0.008 | 6/47 (SW480, NCI-H661, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -3.7 | 0.009 | 14/48 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Naproxen (drug)]] 0.5 µM |  | **0.810×** | -3.1 | 0.067 | 3/47 (J82, NCI-H2030, …) | two highest doses | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.753×** | -2.9 | 0.095 | 6/46 (SHP-77, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 18.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.50× (z +8.6) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.231× (z -9.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 7.74 | 0 | 2 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.0881× (z -10.0) |
| [[KATO III (line)]] | alt | 13.0 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.62× (z +9.4) ⚠ position not correctable | [[Panobinostat (drug)]] 5 µM 0.212× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.154× (z -8.9) |
| [[PANC-1 (line)]] | alt | 14.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -9.1) |
| [[A-427 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -12.2) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A549 (line)]] | wt | 10.1 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.123× (z -10.7) |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.102× (z -10.3) |
| [[C32 (line)]] | wt | 7.04 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.103× (z -8.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 9.20 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 9.86 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.196× (z -10.9) ⚠ cell-cycle shift, explains ~18% of this change |
| [[RKO (line)]] | wt | 8.73 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0992× (z -9.3) |
| [[SW480 (line)]] | alt | 13.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.313× (z -9.2) |
| [[A-172 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHAMP1]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[INTS14]] | +0.70 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[UTP3]] | +0.70 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[FBXO38]] | +0.70 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.70 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ZNF614]] | +0.69 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[ZNF140]] | +0.69 | +0.58 / +0.71 | both halves | 8e-06 |  |
| [[ZC3H4]] | +0.69 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[VPS72]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[TMEM128]] | +0.69 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[MED18]] | +0.68 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[ICE2]] | +0.68 | +0.66 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB2]] | -0.68 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[DCUN1D4]] | -0.63 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[HEBP1]] | -0.62 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[STRN]] | -0.62 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[TMEM65]] | -0.61 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[RFX2]] | -0.61 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[RPS6KA5]] | -0.60 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[CBFA2T2]] | -0.60 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[CD81]] | -0.60 | -0.52 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-31.1, 9.6); signed map (3.5, -25.3). **Vector** length 76.2, 13.0% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +4.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +2.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.4 | -4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | -7.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -6.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -9.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | PYM1 exon junction complex associated factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,901,413-55,932,618 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PYM; previously WIBG |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRP8](https://www.uniprot.org/uniprotkb/Q9BRP8) (Partner of Y14 and mago):

> Key regulator of the exon junction complex (EJC), a multiprotein complex that associates immediately upstream of the exon-exon junction on mRNAs and serves as a positional landmark for the intron exon structure of genes and directs post-transcriptional processes in the cytoplasm such as mRNA export, nonsense-mediated mRNA decay (NMD) or translation. Acts as an EJC disassembly factor, allowing translation-dependent EJC removal and recycling by disrupting mature EJC from spliced mRNAs. Its …

**Summary**, from NCBI Gene [84305](https://www.ncbi.nlm.nih.gov/gene/84305):

> Enables ribosome binding activity. Involved in exon-exon junction complex disassembly; nuclear-transcribed mRNA catabolic process, nonsense-mediated decay; and positive regulation of translation. Located in cytosol; nucleolus; and nucleoplasm. Part of exon-exon junction complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30258) · Entrez [84305](https://www.ncbi.nlm.nih.gov/gene/84305) · UniProt [Q9BRP8](https://www.uniprot.org/uniprotkb/Q9BRP8) · Ensembl [ENSG00000170473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170473)

## Data

Gene col 9960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9960); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9960]; `tensor/DDL_lfc|DDL_z.npy` [9960]; `embed/gene_vectors.npy` [9960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9960 or target_col == 9960). Every well: [[PYM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

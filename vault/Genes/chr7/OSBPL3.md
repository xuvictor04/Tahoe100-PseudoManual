---
symbol: "OSBPL3"
type: "gene"
col: 970
ensembl_id: "ENSG00000070882"
name: "oxysterol binding protein like 3"
location: "7p15.3"
module: 34
arm: "+"
pooled_cpm: 174.36
n_lines_expressing: 47
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 19
direction_downstream: 6
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# OSBPL3

*oxysterol binding protein like 3* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.48× (z +10.0, q 7e-21, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.709× (z -6.1, q 5e-07, down in 26 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.778× (z -4.7, q 5e-04, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRMD5]] (+0.62, fdr 1e-05), [[ITGA6]] (+0.62, fdr 7e-06), [[TIAM1]] (+0.60, fdr 8e-06); moves opposite to [[DNAJC27]] (-0.47, fdr 4e-05), [[ENTPD3-AS1]] (-0.47, fdr 6e-05), [[KIAA0825]] (-0.46, fdr 7e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TINAGL1]] → it (grade B ⚠); 6 go from it, the strongest it → [[UBASH3B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +10.0 | 7e-21 | 33/45 (A-172, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +9.5 | 8e-19 | 28/45 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +7.0 | 6e-10 | 31/45 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +6.5 | 1e-08 | 31/45 (C32, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +5.7 | 1e-06 | 29/45 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.34×** | +5.6 | 2e-06 | 26/45 (HOP62, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 2e-05 | 25/46 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.30×** | +5.1 | 3e-05 | 25/45 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +4.5 | 4e-04 | 25/46 (A-172, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.27×** | +4.5 | 4e-04 | 24/45 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.25×** | +4.3 | 9e-04 | 23/45 (Hs 766T, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.22×** | +3.9 | 0.005 | 24/45 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.21×** | +3.6 | 0.016 | 17/44 (SW480, H4, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.047 | 12/45 (HOP62, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | 1.18× | +3.1 | 0.075 | 18/44 (HOP62, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 970.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.709×** | -6.1 | 5e-07 | 26/42 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.739×** | -5.8 | 2e-06 | 28/45 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.754×** | -5.4 | 1e-05 | 28/46 (A498, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.778×** | -4.7 | 5e-04 | 23/45 (SW480, Hs 766T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.802×** | -4.3 | 0.002 | 22/45 (Hs 766T, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.9 | 0.011 | 21/46 (SW480, Panc 03.27, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.829×** | -3.6 | 0.021 | 21/45 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.700×** | -3.6 | 0.021 | 14/45 (A498, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.824×** | -3.6 | 0.021 | 20/40 (SW48, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.719×** | -3.3 | 0.051 | 15/45 (SW480, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.843× | -3.3 | 0.051 | 20/46 (SW480, KATO III, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.840× | -3.2 | 0.058 | 16/46 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.848× | -3.2 | 0.065 | 20/46 (Hs 766T, SW480, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.891× | -3.0 | 0.10 | 13/45 (NCI-H1573, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 94.7 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +17.2) | — |
| [[A-172 (line)]] | wt | 153 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.38× (z +26.6) | — |
| [[HOP62 (line)]] | alt | 55.2 | 6 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.60× (z +10.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.34× (z +9.3) | — |
| [[J82 (line)]] | alt | 58.8 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +25.8) | — |
| [[NCI-H460 (line)]] | wt | 65.0 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +18.0) | — |
| [[A498 (line)]] | wt | 377 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 84.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +23.6) | — |
| [[SW48 (line)]] | wt | 408 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0896× (z -21.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 225 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 89.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -17.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 77.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +20.2) | — |
| [[SW1417 (line)]] | alt | 413 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.407× (z -10.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 463 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 362 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -9.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 146 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +16.4) | — |
| [[Hs 766T (line)]] | wt | 258 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.4) | — |
| [[NCI-H2030 (line)]] | alt | 67.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +18.3) | — |
| [[RPMI-7951 (line)]] | alt | 160 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.9) | — |
| [[A-427 (line)]] | wt | 74.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -21.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 110 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 205 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 76.7 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0708× (z -12.6) |
| [[HS-578T (line)]] | alt | 96.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.2) | — |
| [[HT-29 (line)]] | alt | 68.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.01× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +18.4) | — |
| [[KATO III (line)]] | alt | 234 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 96.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 65.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 46.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +8.5) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H2347 (line)]] | alt | 301 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 512 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 118 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 270 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 185 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 194 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRMD5]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ITGA6]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TIAM1]] | +0.60 | +0.58 / +0.59 | both halves | 8e-06 | same gene group |
| [[CD58]] | +0.59 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[TGFA]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[WNT7B]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[WNT7A]] | +0.56 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PDP1]] | +0.56 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[OSBPL10]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[BLACAT1]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[VSIG1]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[EML6]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC27]] | -0.47 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[ENTPD3-AS1]] | -0.47 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[KIAA0825]] | -0.46 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[AZI2]] | -0.46 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[MTERF1]] | -0.46 | -0.53 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TINAGL1]] | B | TINAGL1 activity raises OSBPL3's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.19× lower at baseline in the lines without TINAGL1 | 0.006 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[LAMC2]] | B | LAMC2 activity raises OSBPL3's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.10× lower at baseline in the lines without LAMC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[ADAM19]] | B | ADAM19 activity raises OSBPL3's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.36× lower at baseline in the lines without ADAM19 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[RAPGEF5]] | B | RAPGEF5 activity strengthens OSBPL3's drug response | lines that do not express RAPGEF5 (16) vs lines expressing it (30) | the lines without RAPGEF5 respond 1.15× as strongly (z diff -0.63); strongest at Docetaxel 0.05 µM: 0.95x vs 0.67x (z diff +3.5) | 0.012 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[LBH]] | B | LBH activity raises OSBPL3's level | lines that do not express LBH (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without LBH | 0.014 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, PLAT |
| [[TGFA]] | B | TGFA activity weakens OSBPL3's drug response | lines that do not express TGFA (16) vs lines expressing it (30) | the lines without TGFA respond 1.57× as strongly (z diff -1.38); strongest at Homoharringtonine 5 µM: 2.70x vs 1.30x (z diff -4.6) | 0.020 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1; target measured in part of the lines; artifact flags |
| [[WNT7B]] | B | WNT7B activity raises OSBPL3's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.47× lower at baseline in the lines without WNT7B | 0.034 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[WNT7A]] | B | WNT7A activity raises OSBPL3's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.80× lower at baseline in the lines without WNT7A | 0.039 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[LEMD1]] | B | LEMD1 activity raises OSBPL3's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.34× lower at baseline in the lines without LEMD1 | 0.059 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[ITGA2]] | B | ITGA2 activity raises OSBPL3's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.51× lower at baseline in the lines without ITGA2 | 0.060 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[LAMA3]] | B | LAMA3 activity raises OSBPL3's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without LAMA3 | 0.063 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[PTPRE]] | B | PTPRE activity raises OSBPL3's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without PTPRE | 0.063 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBASH3B]] | C | OSBPL3 activity raises UBASH3B's level | lines that do not express OSBPL3 (3) vs lines expressing it (47) | 8.62× lower at baseline in the lines without OSBPL3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: OAF, FOSL1, ENSG00000271204; its own permutation p |
| [[ITGA2]] | C | OSBPL3 activity raises ITGA2's level | lines that do not express OSBPL3 (3) vs lines expressing it (47) | 4.49× lower at baseline in the lines without OSBPL3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: OAF, FOSL1, ENSG00000271204; its own permutation p |
| [[CD58]] | C | OSBPL3 activity raises CD58's level | lines that do not express OSBPL3 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without OSBPL3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: OAF, FOSL1, ENSG00000271204; its own permutation p |
| [[ENDOD1]] | C | OSBPL3 activity raises ENDOD1's level | lines that do not express OSBPL3 (3) vs lines expressing it (47) | 2.16× lower at baseline in the lines without OSBPL3 | 0.064 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: OAF, FOSL1, ENSG00000271204 |
| [[MIR222HG]] | C | OSBPL3 activity raises MIR222HG's level | lines that do not express OSBPL3 (3) vs lines expressing it (47) | 7.05× lower at baseline in the lines without OSBPL3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: OAF, FOSL1, ENSG00000271204; co-absent with the target; its own permutation p |
| [[FAM107B]] | C | OSBPL3 activity raises FAM107B's level | lines that do not express OSBPL3 (3) vs lines expressing it (47) | 4.09× lower at baseline in the lines without OSBPL3 | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: OAF, FOSL1, ENSG00000271204 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.2, 19.4); signed map (2.1, 41.6). **Vector** length 120, 35.6% of its response variance represented; |z| ≥ 3 in 1,302 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.4 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.4 | +7.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | -0.7 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | +2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.5 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.5 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | oxysterol binding protein like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:24,796,540-24,981,634 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ORP-3, ORP3, KIAA0704; previously OSBP3 |
| Gene groups (HGNC) | Oxysterol binding proteins; Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: Synthesis of bile acids and bile salts; Bile acid and bile salt metabolism; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4L5](https://www.uniprot.org/uniprotkb/Q9H4L5) (Oxysterol-binding protein-related protein 3):

> Lipid transfer protein that mediates the non-vesicular transport of phosphoinositide 4-phosphate (1,2-diacyl-sn-glycero-3-phospho-(1D-myo-inositol 4-phosphate), or PI(4)P) at the plasma membrane (PM)/ endoplasmic reticulum (ER) contact sites. Extracts PI4P from the PM, in exchange for phosphatidylcholine. Can bind to the ER membrane protein VAPA and recruit VAPA to PM sites, thus linking these intracellular compartments. The ORP3-VAPA complex stimulates RRAS signaling which in turn attenuates …

**Summary**, from NCBI Gene [26031](https://www.ncbi.nlm.nih.gov/gene/26031):

> This gene encodes a member of the oxysterol-binding protein (OSBP) family, a group of intracellular lipid receptors. Most members contain an N-terminal pleckstrin homology domain and a highly conserved C-terminal OSBP-like sterol-binding domain. The encoded protein is involved in the regulation of cell adhesion and organization of the actin cytoskeleton. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:16370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16370) · Entrez [26031](https://www.ncbi.nlm.nih.gov/gene/26031) · UniProt [Q9H4L5](https://www.uniprot.org/uniprotkb/Q9H4L5) · Ensembl [ENSG00000070882](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070882)

## Data

Gene col 970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 970); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 970]; `tensor/DDL_lfc|DDL_z.npy` [970]; `embed/gene_vectors.npy` [970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 970 or target_col == 970). Every well: [[OSBPL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSBPL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "GEMIN8"
type: "gene"
col: 504
ensembl_id: "ENSG00000046647"
name: "gem nuclear organelle associated protein 8"
location: "Xp22.2"
module: 12
arm: "+"
pooled_cpm: 15.77
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 25
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# GEMIN8

*gem nuclear organelle associated protein 8* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 0.5 µM: 1.31× (z +5.1, q 2e-04, up in 14 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.503× (z -12.2, q 1e-31, down in 32 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.534× (z -11.6, q 1e-28, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DET1]] (+0.64, fdr 7e-06), [[EXOC1]] (+0.57, fdr 1e-05), [[ZNF397]] (+0.57, fdr 1e-05); moves opposite to [[SFXN5]] (-0.54, fdr 1e-05), [[ELOVL5]] (-0.51, fdr 1e-05), [[SPINDOC]] (-0.51, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 2e-04 | 14/46 (J82, C-33 A, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 0.001 | 15/47 (NCI-H1792, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.017 | 9/40 (PANC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.049 | 5/46 (KATO III, SW1417, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.12 | 5/47 (NCI-H1792, HEC-1-A, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.2 | 0.12 | 4/47 (COLO 205, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.14 | 11/38 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.19× | +3.1 | 0.15 | 5/43 (J82, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 504.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.503×** | -12.2 | 1e-31 | 32/41 (J82, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.534×** | -11.6 | 1e-28 | 31/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.545×** | -11.2 | 6e-27 | 30/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.675×** | -10.3 | 1e-22 | 31/45 (SNU-423, COLO 205, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.594×** | -9.6 | 7e-20 | 29/46 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.607×** | -9.2 | 3e-18 | 27/46 (SW480, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.634×** | -8.4 | 3e-15 | 26/45 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.660×** | -7.7 | 1e-12 | 23/46 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.655×** | -7.4 | 9e-12 | 21/44 (J82, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.671×** | -7.4 | 1e-11 | 19/36 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.777×** | -6.6 | 2e-09 | 19/44 (SW480, A549, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.694×** | -6.5 | 4e-09 | 18/23 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.575×** | -5.3 | 4e-06 | 13/43 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.736×** | -5.3 | 4e-06 | 20/45 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.771×** | -4.8 | 6e-05 | 15/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.830×** | -3.4 | 0.014 | 14/44 (MIA PaCa-2, SW48, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.701×** | -3.4 | 0.014 | 10/46 (SW480, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.713×** | -3.3 | 0.025 | 4/45 (J82, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.783×** | -3.2 | 0.027 | 6/47 (SW 1088, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.886× | -3.2 | 0.032 | 6/47 (SHP-77, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 33.8 | 0 | 13 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.188× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.204× (z -16.9) |
| [[NCI-H460 (line)]] | wt | 17.6 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.259× (z -11.7) |
| [[A-172 (line)]] | wt | 21.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0866× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.4) |
| [[COLO 205 (line)]] | alt | 23.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 27.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[hTERT-HPNE (line)]] | wt | 8.30 | 0 | 2 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0534× (z -9.9) |
| [[PANC-1 (line)]] | alt | 15.2 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.333× (z -10.2) |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0646× (z -10.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.374× (z -10.2) |
| [[SW48 (line)]] | wt | 11.4 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0773× (z -9.4) |
| [[A-427 (line)]] | wt | 17.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.51× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change |
| [[H4 (line)]] | wt | 7.48 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0390× (z -10.9) |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.232× (z -9.6) ⚠ toxic |
| [[J82 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0802× (z -15.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.273× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.231× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 7.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 8.31 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0590× (z -12.3) ⚠ toxic |
| [[SW 900 (line)]] | alt | 8.41 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.122× (z -8.6) |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -9.5) |
| [[A498 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DET1]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[EXOC1]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ZNF397]] | +0.57 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CCDC18-AS1]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ACAD10]] | +0.56 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[FRA10AC1]] | +0.55 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ZNF333]] | +0.55 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[XRRA1]] | +0.54 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[MTIF3]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[CBY1]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[FAM149B1]] | +0.54 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[ATP5MC2]] | +0.54 | +0.47 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFXN5]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ELOVL5]] | -0.51 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SPINDOC]] | -0.51 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.50 | -0.53 / -0.49 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[GATAD2A]] | -0.49 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[FKBP4]] | -0.49 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[TRRAP]] | -0.48 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[DNAJB6]] | -0.48 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[ACOT7]] | -0.48 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ACLY]] | -0.47 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[STIP1]] | -0.47 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[MELTF]] | -0.47 | -0.45 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-33.7, -13.3); signed map (-16.1, 1.4). **Vector** length 76.0, 13.7% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +2.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.1 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +2.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -5.3 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -4.9 | -7.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.4 | -12.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.2 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | -4.1 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -9.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -5.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | gem nuclear organelle associated protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:14,006,726-14,029,893 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20514; previously FAM51A1 |
| Gene groups (HGNC) | Gemins |
| Reactome | 8 pathways, smallest: SARS-CoV-2 modulates host translation machinery; Metabolism of non-coding RNA; snRNP Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWZ8](https://www.uniprot.org/uniprotkb/Q9NWZ8) (Gem-associated protein 8):

> The SMN complex catalyzes the assembly of small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome, and thereby plays an important role in the splicing of cellular pre-mRNAs. Most spliceosomal snRNPs contain a common set of Sm proteins SNRPB, SNRPD1, SNRPD2, SNRPD3, SNRPE, SNRPF and SNRPG that assemble in a heptameric protein ring on the Sm site of the small nuclear RNA to form the core snRNP (Sm core). In the cytosol, the Sm proteins SNRPD1, SNRPD2, SNRPE, SNRPF and …

**Summary**, from NCBI Gene [54960](https://www.ncbi.nlm.nih.gov/gene/54960):

> The protein encoded by this gene is part of the SMN complex, which is necessary for spliceosomal snRNP assembly in the cytoplasm and pre-mRNA splicing in the nucleus. The encoded protein binds to both SMN1 and the GEMIN6/GEMIN7 heterodimer, mediating their interaction. This protein is found in nuclear Gemini of Cajal bodies (gems) and in the cytoplasm. Three transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:26044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26044) · Entrez [54960](https://www.ncbi.nlm.nih.gov/gene/54960) · UniProt [Q9NWZ8](https://www.uniprot.org/uniprotkb/Q9NWZ8) · Ensembl [ENSG00000046647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000046647)

## Data

Gene col 504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 504); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 504]; `tensor/DDL_lfc|DDL_z.npy` [504]; `embed/gene_vectors.npy` [504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 504 or target_col == 504). Every well: [[GEMIN8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GEMIN8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

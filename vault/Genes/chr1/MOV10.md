---
symbol: "MOV10"
type: "gene"
col: 7890
ensembl_id: "ENSG00000155363"
name: "Mov10 RNA helicase"
location: "1p13.2"
module: 32
arm: "+"
pooled_cpm: 30.0
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 31
n_dd_up_clean: 10
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# MOV10

*Mov10 RNA helicase* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.46× (z +5.1, q 2e-04, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.194× (z -23.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAR]] (+0.76, fdr 7e-06), [[SLC15A3]] (+0.73, fdr 1e-05), [[TAP2]] (+0.73, fdr 7e-06); moves opposite to [[TOMM20]] (-0.58, fdr 5e-05), [[OSBPL8]] (-0.55, fdr 5e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[IFIT5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +5.1 | 2e-04 | 29/47 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +4.3 | 0.003 | 25/47 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +4.3 | 0.003 | 22/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.003 | 21/48 (A-172, SW1417, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.005 | 27/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.29×** | +3.9 | 0.008 | 24/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.010 | 22/48 (SW480, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.010 | 18/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.030 | 20/48 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.031 | 15/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.055 | 17/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.24× | +3.1 | 0.10 | 10/48 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.26× | +3.0 | 0.11 | 13/48 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.194×** | -23.3 | 0e+00 | 47/48 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.201×** | -22.8 | 0e+00 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.208×** | -22.3 | 0e+00 | 48/48 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.456×** | -15.8 | 0e+00 | 41/48 (NCI-H1573, SK-MEL-2, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.419×** | -12.3 | 6e-33 | 45/48 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.552×** | -8.4 | 3e-15 | 44/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.714×** | -6.8 | 1e-09 | 34/48 (LoVo, BT-474, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.420×** | -6.4 | 8e-09 | 38/48 (LoVo, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.643×** | -5.8 | 4e-07 | 23/41 (NCI-H460, SHP-77, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.664×** | -5.6 | 1e-06 | 31/47 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.676×** | -5.6 | 1e-06 | 29/47 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.680×** | -5.5 | 2e-06 | 29/48 (HS-578T, BT-474, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.722×** | -4.6 | 2e-04 | 25/48 (LoVo, HS-578T, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.719×** | -4.5 | 2e-04 | 24/47 (RKO, NCI-H661, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.729×** | -4.5 | 2e-04 | 26/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.800×** | -4.5 | 2e-04 | 24/48 (MIA PaCa-2, LoVo, …) | rises with dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.725×** | -4.4 | 4e-04 | 25/48 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.816×** | -4.1 | 0.001 | 23/48 (SK-MEL-2, AsPC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.786×** | -3.4 | 0.017 | 16/48 (SK-MEL-2, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 49.6 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -23.8) |
| [[A-172 (line)]] | wt | 41.3 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0375× (z -26.9) |
| [[NCI-H23 (line)]] | alt | 50.5 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 21.9 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -19.1) |
| [[SK-MEL-2 (line)]] | alt | 60.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -20.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.120× (z -17.6) |
| [[HS-578T (line)]] | alt | 38.6 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0789× (z -19.1) |
| [[NCI-H1573 (line)]] | alt | 30.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -20.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.101× (z -17.2) |
| [[RKO (line)]] | wt | 43.3 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 40.3 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -12.2) |
| [[A549 (line)]] | wt | 27.9 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0626× (z -17.7) |
| [[C-33 A (line)]] | alt | 58.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -16.0) |
| [[C32 (line)]] | wt | 19.1 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.174× (z -9.8) |
| [[H4 (line)]] | wt | 28.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -10.7) |
| [[Hs 766T (line)]] | wt | 51.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -16.8) |
| [[HT-29 (line)]] | alt | 27.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -14.9) |
| [[KATO III (line)]] | alt | 23.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0898× (z -18.0) |
| [[NCI-H1792 (line)]] | alt | 34.5 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0980× (z -16.5) |
| [[PANC-1 (line)]] | alt | 20.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -16.6) |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.117× (z -12.6) |
| [[SW 900 (line)]] | alt | 24.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -10.5) |
| [[SW480 (line)]] | alt | 20.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -19.7) |
| [[A498 (line)]] | wt | 36.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 23.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 25.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -12.5) |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.146× (z -12.4) |
| [[J82 (line)]] | alt | 28.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.235× (z -11.4) |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.158× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 49.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0932× (z -17.2) |
| [[NCI-H2347 (line)]] | alt | 29.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 37.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -10.7) |
| [[SNU-423 (line)]] | alt | 29.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -11.5) |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -13.1) |
| [[A-427 (line)]] | wt | 16.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.195× (z -10.2) |
| [[BT-474 (line)]] | alt | 25.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -10.7) |
| [[HCT15 (line)]] | alt | 41.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 28.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -14.3) |
| [[SNU-1 (line)]] | wt | 29.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0945× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 22.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.161× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.131× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -9.6) |
| [[NCI-H661 (line)]] | alt | 34.5 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0644× (z -8.7) |
| [[SW48 (line)]] | wt | 27.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -11.0) |
| [[AN3 CA (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAR]] | +0.76 | +0.68 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 534 |
| [[SLC15A3]] | +0.73 | +0.56 / +0.80 | both halves | 1e-05 |  |
| [[TAP2]] | +0.73 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[PARP10]] | +0.70 | +0.47 / +0.78 | both halves | 2e-05 |  |
| [[C5orf15]] | +0.70 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[TAP1]] | +0.70 | +0.49 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TRIM21]] | +0.69 | +0.46 / +0.71 | both halves | 2e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[ZC3HAV1]] | +0.68 | +0.51 / +0.70 | both halves | 1e-05 | STRING 665 |
| [[PARP14]] | +0.68 | +0.49 / +0.71 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 421 |
| [[HLA-C]] | +0.68 | +0.59 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[RNF213]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 | pathway: Signaling by ALK fusions and activated point mutants |
| [[APOBEC3F]] | +0.67 | +0.45 / +0.61 | both halves | 3e-05 | STRING 448 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOMM20]] | -0.58 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[OSBPL8]] | -0.55 | -0.48 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers MOV10's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity lowers MOV10's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[USP18]] | C | USP18 activity raises MOV10's level | lines that do not express USP18 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without USP18 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000280007, OAS3; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIT5]] | C | MOV10's natural level strengthens IFIT5's drug response | MOV10's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.52; direction not clear | 0.029 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.679). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.6, 54.8); signed map (63.8, 33.6). **Vector** length 105, 29.6% of its response variance represented; |z| ≥ 3 in 1,220 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.56 to 60); *interferon* (control, mean cos +0.57 to 23); *Interferon Signaling* (reactome, mean cos +0.56 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.9 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | -0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +4.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +3.8 | +4.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.5 | +4.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.2 | -12.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.2 | -4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.7 | -4.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.6 | -4.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | Mov10 RNA helicase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:112,673,141-112,700,756 (+) |
| Ensembl biotype | protein_coding |
| Also known as | gb110, MGC2948, fSAP113 |
| Gene groups (HGNC) | UPF1 like RNA helicases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Reactome | 65 pathways, smallest: Regulation of NPAS4 mRNA translation; Regulation of CDH11 mRNA translation by microRNAs; Regulation of PD-L1(CD274) translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCE1](https://www.uniprot.org/uniprotkb/Q9HCE1) (RNA helicase MOV-10):

> 5'-3' RNA helicase. Involved in a number of cellular roles ranging from mRNA metabolism and translation, modulation of viral infectivity, inhibition of retrotransposition, or regulation of synaptic transmission. Plays an important role in innate antiviral immunity by promoting type I interferon production. Mechanistically, specifically uses IKKepsilon/IKBKE as the mediator kinase for IRF3 activation. Blocks HIV-1 virus replication at a post-entry step. Counteracts HIV-1 Vif-mediated degradation …

**Summary**, from NCBI Gene [4343](https://www.ncbi.nlm.nih.gov/gene/4343):

> Enables 5'-3' RNA helicase activity and RNA binding activity. Involved in defense response to virus and mRNA destabilization. Located in P-body. Implicated in hypertension. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7200) · Entrez [4343](https://www.ncbi.nlm.nih.gov/gene/4343) · UniProt [Q9HCE1](https://www.uniprot.org/uniprotkb/Q9HCE1) · Ensembl [ENSG00000155363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155363)

## Data

Gene col 7890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7890); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7890]; `tensor/DDL_lfc|DDL_z.npy` [7890]; `embed/gene_vectors.npy` [7890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7890 or target_col == 7890). Every well: [[MOV10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOV10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

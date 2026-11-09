---
symbol: "DNAJA4"
type: "gene"
col: 6405
ensembl_id: "ENSG00000140403"
name: "DnaJ heat shock protein family (Hsp40) member A4"
location: "15q25.1"
module: 60
arm: "+"
pooled_cpm: 12.3
n_lines_expressing: 28
n_dd_up: 29
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# DNAJA4

*DnaJ heat shock protein family (Hsp40) member A4* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 17.5× (z +41.2, q 0e+00, up in 25 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.490× (z -10.3, q 7e-22, down in 18 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPH1]] (+0.68, fdr 7e-06), [[HSP90AA2P]] (+0.68, fdr 7e-06), [[AHSA2P]] (+0.68, fdr 1e-05); moves opposite to [[DOP1A]] (-0.56, fdr 9e-05), [[VWA1]] (-0.55, fdr 1e-04), [[WDPCP]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GCHFR]] → it (grade B ⚠); 5 go from it, the strongest it → [[MAP1A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6405.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **17.5×** | +41.2 | 0e+00 | 25/25 (SW480, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **8.94×** | +31.5 | 0e+00 | 25/25 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **7.17×** | +28.3 | 0e+00 | 25/25 (SW1417, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **6.83×** | +26.1 | 0e+00 | 25/25 (SW1417, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **14.7×** | +20.2 | 0e+00 | 22/22 (SW1417, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **6.14×** | +18.6 | 0e+00 | 25/25 (NCI-H2347, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.85×** | +15.1 | 0e+00 | 14/20 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +11.9 | 8e-31 | 18/25 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +11.8 | 4e-30 | 10/18 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +11.5 | 8e-29 | 18/25 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 5 µM |  | **4.58×** | +11.4 | 1e-28 | 25/25 (SW480, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +9.2 | 2e-18 | 8/18 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +9.1 | 4e-18 | 17/25 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +7.4 | 6e-12 | 10/23 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.98×** | +7.0 | 1e-10 | 11/23 (BT-474, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +6.9 | 1e-10 | 14/25 (J82, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.8 | 2e-07 | 14/24 (MIA PaCa-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[NG25 (drug)]] 5 µM |  | **2.11×** | +5.6 | 6e-07 | 13/25 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Hydroxyfasudil (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.005 | 7/25 (SW1417, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.60×** | +3.5 | 0.011 | 1/25 (Panc 03.27) | top dose only | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.013 | 9/25 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Pimitespib (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.014 | 3/25 (SW1417, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6405.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.490×** | -10.3 | 7e-22 | 18/25 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.536×** | -9.0 | 8e-17 | 22/25 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.545×** | -8.7 | 4e-16 | 21/25 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.564×** | -8.2 | 3e-14 | 17/25 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.498×** | -5.2 | 2e-05 | 11/25 (LoVo, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.703×** | -5.1 | 4e-05 | 17/25 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM |  | **0.734×** | -4.3 | 0.001 | 3/25 (J82, COLO 205, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.777×** | -3.6 | 0.019 | 12/25 (KATO III, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -3.6 | 0.019 | 14/25 (LoVo, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.7 | 10 (3 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 37.6× (z +27.4) | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -9.0) |
| [[LoVo (line)]] | wt | 77.2 | 6 (1 ⚠) | 4 | [[Auranofin (drug)]] 5 µM 9.95× (z +23.4) | [[Panobinostat (drug)]] 5 µM 0.124× (z -21.4) |
| [[KATO III (line)]] | alt | 27.4 | 6 (1 ⚠) | 3 | [[Ixazomib citrate (drug)]] 5 µM 15.8× (z +19.7) | [[Belinostat (drug)]] 5 µM 0.185× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 27.3 | 8 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 24.8× (z +19.7) | — |
| [[Panc 03.27 (line)]] | alt | 25.3 | 6 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 19.0× (z +19.1) | [[Panobinostat (drug)]] 5 µM 0.221× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 36.6 | 4 | 3 | [[Auranofin (drug)]] 5 µM 6.46× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -14.5) |
| [[HT-29 (line)]] | alt | 19.3 | 6 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 59.6× (z +25.2) | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -10.5) |
| [[SW48 (line)]] | wt | 41.8 | 4 | 3 | [[Auranofin (drug)]] 5 µM 17.7× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.162× (z -10.5) |
| [[BT-474 (line)]] | alt | 24.5 | 6 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 64.7× (z +21.6) | — |
| [[COLO 205 (line)]] | alt | 20.4 | 5 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 15.6× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.145× (z -9.2) |
| [[LS 180 (line)]] | wt | 19.0 | 4 | 2 | [[Ixazomib citrate (drug)]] 5 µM 12.7× (z +15.9) | [[Belinostat (drug)]] 5 µM 0.180× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 17.4 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 24.5× (z +19.9) | — |
| [[SW1417 (line)]] | alt | 34.4 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 24.1× (z +22.5) | — |
| [[HOP62 (line)]] | alt | 4.52 | 4 | 1 | [[Auranofin (drug)]] 5 µM 175× (z +20.5) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0993× (z -8.5) |
| [[Hs 766T (line)]] | wt | 20.1 | 4 | 1 | [[Auranofin (drug)]] 5 µM 11.5× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.183× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 5 | 0 | [[Auranofin (drug)]] 5 µM 43.5× (z +18.2) | — |
| [[A-427 (line)]] | wt | 13.5 | 4 | 0 | [[Auranofin (drug)]] 5 µM 39.4× (z +18.9) | — |
| [[J82 (line)]] | alt | 10.4 | 4 | 0 | [[Auranofin (drug)]] 5 µM 34.3× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 5.25 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 12.0× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 3.91 | 4 | 0 | [[Auranofin (drug)]] 5 µM 26.0× (z +15.9) | — |
| [[RKO (line)]] | wt | 12.5 | 4 | 0 | [[Auranofin (drug)]] 5 µM 26.6× (z +15.1) | — |
| [[SK-MEL-2 (line)]] | alt | 7.69 | 4 | 0 | [[Auranofin (drug)]] 5 µM 169× (z +19.3) | — |
| [[C32 (line)]] | wt | 8.54 | 3 | 0 | [[Auranofin (drug)]] 5 µM 123× (z +17.4) | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +11.2) | — |
| [[A-172 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.982 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.93 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPH1]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 | STRING 817 |
| [[HSP90AA2P]] | +0.68 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[AHSA2P]] | +0.68 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[SERPINH1]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[AIFM2]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[FKBP4]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 | pathway: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand |
| [[BAG2]] | +0.62 | +0.49 / +0.46 | both halves | 2e-05 | STRING 562 |
| [[PARD6G-AS1]] | +0.61 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[SOD1]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PSMD11]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[HSPE1-MOB4]] | +0.60 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[GPN1]] | +0.59 | +0.55 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1A]] | -0.56 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[VWA1]] | -0.55 | -0.50 / -0.32 | both halves | 1e-04 |  |
| [[WDPCP]] | -0.54 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ANAPC11]] | -0.53 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[EFHC1]] | -0.53 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[ARL13B]] | -0.53 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[TSTD1]] | -0.53 | -0.54 / -0.32 | both halves | 1e-04 |  |
| [[PIBF1]] | -0.52 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[GCHFR]] | -0.51 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[LAGE3]] | -0.50 | -0.54 / -0.37 | both halves | 9e-05 |  |
| [[CDKN2D]] | -0.49 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[ETFB]] | -0.49 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCHFR]] | B | GCHFR activity raises DNAJA4's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 2.55× lower at baseline in the lines without GCHFR | 0.068 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises DNAJA4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TSTD1]] | C | TSTD1 activity raises DNAJA4's level | lines that do not express TSTD1 (19) vs lines expressing it (31) | 2.93× lower at baseline in the lines without TSTD1 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CHMP4C, STYK1, SAMD12; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP1A]] | B | DNAJA4 activity lowers MAP1A's level | lines that do not express DNAJA4 (22) vs lines expressing it (28) | 2.55× higher at baseline in the lines without DNAJA4 | 0.055 | ⚠ within organs, on part of the lines; also absent: COL17A1, ENSG00000262302, KIAA0040 |
| [[MORC4]] | B | DNAJA4 activity strengthens MORC4's drug response | lines that do not express DNAJA4 (20) vs lines expressing it (25) | the lines without DNAJA4 respond 0.78× as strongly (z diff +0.73); strongest at Homoharringtonine 5 µM: 1.40x vs 2.07x (z diff +3.4) | 0.068 | ⚠ within organs, on part of the lines; also absent: COL17A1, ENSG00000262302, KIAA0040; target measured in part of the lines; artifact flags |
| cells under [[Entecavir (monohydrate) (drug)]] 5 µM | B | DNAJA4 activity lowers the cells' numbers under Entecavir (monohydrate) 5 µM (makes them more sensitive) | lines that do not express DNAJA4 (22) vs lines expressing it (26) | the lines without DNAJA4: 1.24× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: COL17A1, ENSG00000262302, KIAA0040 |
| [[RCC1L]] | B | DNAJA4 activity raises RCC1L's level | lines that do not express DNAJA4 (22) vs lines expressing it (28) | 1.08× lower at baseline in the lines without DNAJA4 | 0.082 | ⚠ within organs, on part of the lines; also absent: COL17A1, ENSG00000262302, KIAA0040 |
| [[ARL13B]] | B | DNAJA4 activity lowers ARL13B's level | lines that do not express DNAJA4 (22) vs lines expressing it (28) | 1.48× higher at baseline in the lines without DNAJA4 | 0.099 | ⚠ within organs, on part of the lines; also absent: COL17A1, ENSG00000262302, KIAA0040 |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-15.5, 10.2); signed map (-24.7, -28.9). **Vector** length 88.9, 25.2% of its response variance represented; |z| ≥ 3 in 664 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.2 | +41.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.1 | +26.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.7 | +31.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.0 | +28.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +11.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.0 | +18.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.5 | +11.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.1 | -8.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -9.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | +3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -5.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -3.0 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.9 | -0.7 |
|  | [[Levobupivacaine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member A4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:78,264,086-78,282,196 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRO1472 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 3 pathways, smallest: HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; Cellular responses to stress; Cellular responses to stimuli |
| Matched by | ensembl_id |

UniProt [Q8WW22](https://www.uniprot.org/uniprotkb/Q8WW22) carries no function annotation.

**Summary**, from NCBI Gene [55466](https://www.ncbi.nlm.nih.gov/gene/55466):

> Enables protein-folding chaperone binding activity and unfolded protein binding activity. Involved in several processes, including negative regulation of endothelial cell migration; negative regulation of inclusion body assembly; and protein refolding. Located in cytosol and membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14885) · Entrez [55466](https://www.ncbi.nlm.nih.gov/gene/55466) · UniProt [Q8WW22](https://www.uniprot.org/uniprotkb/Q8WW22) · Ensembl [ENSG00000140403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140403)

## Data

Gene col 6405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6405); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6405]; `tensor/DDL_lfc|DDL_z.npy` [6405]; `embed/gene_vectors.npy` [6405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6405 or target_col == 6405). Every well: [[DNAJA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

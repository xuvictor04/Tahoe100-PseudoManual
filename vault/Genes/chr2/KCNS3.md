---
symbol: "KCNS3"
type: "gene"
col: 9999
ensembl_id: "ENSG00000170745"
name: "potassium voltage-gated channel modifier subfamily S member 3"
location: "2p24.2"
module: 82
arm: "+"
pooled_cpm: 9.61
n_lines_expressing: 34
n_dd_up: 25
n_dd_down: 14
n_dd_up_clean: 16
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# KCNS3

*potassium voltage-gated channel modifier subfamily S member 3* — 2p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.72× (z +22.3, q 0e+00, up in 27 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.632× (z -7.2, q 4e-10, down in 19 of 31 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMOD2]] (+0.59, fdr 3e-05), [[OTULINL]] (+0.58, fdr 6e-05), [[BMP8B]] (+0.54, fdr 5e-05); moves opposite to [[ERCC6L2]] (-0.50, fdr 4e-05), [[LINC01004]] (-0.49, fdr 8e-05), [[UBE3B]] (-0.49, fdr 7e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TDRD9]] → it (grade B ⚠); 4 go from it, the strongest it → [[EPB41L4A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9999.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.72×** | +22.3 | 0e+00 | 27/31 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +15.5 | 0e+00 | 13/30 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.45×** | +14.1 | 6e-43 | 26/30 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.25×** | +12.8 | 2e-35 | 18/31 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.14×** | +12.0 | 4e-31 | 19/32 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +11.6 | 3e-29 | 20/31 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +10.1 | 4e-22 | 17/30 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +7.8 | 3e-13 | 2/13 (CFPAC-1, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +7.2 | 4e-11 | 6/24 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +4.9 | 6e-05 | 10/31 (SW1417, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +4.5 | 3e-04 | 3/24 (NCI-H1573, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +4.4 | 6e-04 | 8/31 (NCI-H1573, C32, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.31×** | +4.1 | 0.002 | 8/31 (A-427, J82, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.002 | 2/31 (HS-578T, LoVo) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.27×** | +3.8 | 0.005 | 4/31 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.007 | 2/30 (H4, A-427) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.008 | 4/30 (NCI-H2030, LoVo, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.014 | 4/31 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.021 | 7/30 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9999.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.632×** | -7.2 | 4e-10 | 19/31 (C32, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.629×** | -7.0 | 6e-10 | 15/31 (A498, Panc 03.27, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.640×** | -7.0 | 6e-10 | 17/31 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.701×** | -5.6 | 4e-06 | 17/28 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.704×** | -5.5 | 5e-06 | 13/30 (C32, H4, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.708×** | -5.4 | 6e-06 | 18/30 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[NG25 (drug)]] 5 µM |  | **0.541×** | -5.0 | 4e-05 | 7/27 (A549, A498, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.734×** | -4.8 | 1e-04 | 7/31 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.797×** | -3.5 | 0.025 | 3/30 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.790×** | -3.5 | 0.030 | 3/31 (A549, SW480, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.044 | 7/31 (SW 1088, BT-474, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.860× | -3.3 | 0.044 | 8/31 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.044 | 5/30 (RPMI-7951, HCT15, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.044 | 11/30 (A498, A-172, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.685×** | -3.1 | 0.073 | 10/31 (A498, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 25.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0837× (z -10.9) |
| [[C32 (line)]] | wt | 51.9 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0289× (z -14.7) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0813× (z -10.8) |
| [[SW480 (line)]] | alt | 5.95 | 4 | 1 | [[Tucidinostat (drug)]] 5 µM 5.39× (z +14.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 3.46 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 6.93× (z +11.9) | — |
| [[Panc 03.27 (line)]] | alt | 33.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -14.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -8.6) |
| [[PANC-1 (line)]] | alt | 2.60 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 6.91× (z +11.6) | — |
| [[A549 (line)]] | wt | 13.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0845× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.143× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 22.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -10.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 19.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -9.1) |
| [[LoVo (line)]] | wt | 3.43 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.98× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 20.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 7.07 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0936× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -11.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 7.82 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.66× (z +12.8) | — |
| [[A-172 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMOD2]] | +0.59 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[OTULINL]] | +0.58 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[BMP8B]] | +0.54 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[INPP5F]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[LPAR3]] | +0.54 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[PDZD7]] | +0.52 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[C1orf21]] | +0.51 | +0.51 / +0.37 | both halves | 8e-05 |  |
| [[SPTLC2]] | +0.51 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[CLMN]] | +0.51 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[RIMS3]] | +0.51 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[TDRD9]] | +0.51 | +0.40 / +0.53 | both halves | 4e-05 |  |
| [[SLAIN1]] | +0.50 | +0.29 / +0.53 | both halves | 2e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[LINC01004]] | -0.49 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[UBE3B]] | -0.49 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[LZIC]] | -0.48 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[MED13]] | -0.47 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[GPATCH2]] | -0.47 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[LINC01134]] | -0.47 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[RBM23]] | -0.47 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[RAB30-DT]] | -0.47 | -0.35 / -0.35 | both halves | 1e-04 |  |
| [[TIA1]] | -0.46 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[RC3H2]] | -0.45 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[ZBED5]] | -0.45 | -0.40 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TDRD9]] | B | TDRD9 activity raises KCNS3's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 2.25× lower at baseline in the lines without TDRD9 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT |
| [[COL4A4]] | C | COL4A4 activity raises KCNS3's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 2.31× lower at baseline in the lines without COL4A4 | 0.062 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L4A]] | B | KCNS3 activity raises EPB41L4A's level | lines that do not express KCNS3 (16) vs lines expressing it (34) | 3.04× lower at baseline in the lines without KCNS3 | 0.025 | ⚠ within organs, on part of the lines; also absent: EFCAB13, JHY, SAA1; maybe low, not absent |
| [[PBLD]] | B | KCNS3 activity raises PBLD's level | lines that do not express KCNS3 (16) vs lines expressing it (34) | 1.31× lower at baseline in the lines without KCNS3 | 0.033 | ⚠ within organs, on part of the lines; also absent: EFCAB13, JHY, SAA1; maybe low, not absent |
| [[CLMN]] | B | KCNS3 activity raises CLMN's level | lines that do not express KCNS3 (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without KCNS3 | 0.086 | ⚠ within organs, on part of the lines; also absent: EFCAB13, JHY, SAA1; maybe low, not absent |
| [[COL4A4]] | C | KCNS3 activity raises COL4A4's level | lines that do not express KCNS3 (16) vs lines expressing it (34) | 2.73× lower at baseline in the lines without KCNS3 | 0.060 | ⚠ within organs, on part of the lines; also absent: EFCAB13, JHY, SAA1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.578). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.0, 40.3); signed map (-23.6, 34.9). **Vector** length 78.6, 18.3% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.7 | +22.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +14.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.0 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -5.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.6 | -3.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel modifier subfamily S member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.2 — chr2:17,877,847-18,361,616 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kv9.3 |
| Gene groups (HGNC) | Potassium voltage-gated channels; BTB domain containing |
| Reactome | 6 pathways, smallest: Voltage gated Potassium channels; Glucagon-like Peptide-1 (GLP1) regulates insulin secretion; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ31](https://www.uniprot.org/uniprotkb/Q9BQ31) (Delayed-rectifier potassium channel regulatory subunit KCNS3):

> Potassium channel regulatory subunit that modulates the delayed rectifier potassium channel activity of KCNB1 by namely slowing down the deactivation and inactivation time constants. While it does not form functional channel on its own, it can form functional heterotetrameric channels with KCNB1.

**Summary**, from NCBI Gene [3790](https://www.ncbi.nlm.nih.gov/gene/3790):

> Voltage-gated potassium channels form the largest and most diversified class of ion channels and are present in both excitable and nonexcitable cells. Their main functions are associated with the regulation of the resting membrane potential and the control of the shape and frequency of action potentials. The alpha subunits are of 2 types: those that are functional by themselves and those that are electrically silent but capable of modulating the activity of specific functional alpha subunits. …

**Accessions** — [HGNC:6302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6302) · Entrez [3790](https://www.ncbi.nlm.nih.gov/gene/3790) · UniProt [Q9BQ31](https://www.uniprot.org/uniprotkb/Q9BQ31) · Ensembl [ENSG00000170745](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170745)

## Data

Gene col 9999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9999); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9999]; `tensor/DDL_lfc|DDL_z.npy` [9999]; `embed/gene_vectors.npy` [9999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9999 or target_col == 9999). Every well: [[KCNS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

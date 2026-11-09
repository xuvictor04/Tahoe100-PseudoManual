---
symbol: "TMEM97"
type: "gene"
col: 3025
ensembl_id: "ENSG00000109084"
name: "transmembrane protein 97"
location: "17q11.2"
module: 170
arm: "-"
pooled_cpm: 10.85
n_lines_expressing: 48
n_dd_up: 39
n_dd_down: 7
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# TMEM97

*transmembrane protein 97* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.69× (z +13.9, q 3e-41, up in 28 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.59× (z +10.1, q 8e-22, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.353× (z -15.6, q 0e+00, down in 36 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHRNA5]] (+0.68, fdr 7e-06), [[AHSA1]] (+0.67, fdr 7e-06), [[LDHB]] (+0.67, fdr 1e-05); moves opposite to [[CHMP4A]] (-0.64, fdr 9e-06), [[TJAP1]] (-0.63, fdr 1e-05), [[TCEANC]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[WNK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 22 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3025.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.69×** | +13.9 | 3e-41 | 28/30 (A549, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.80×** | +13.7 | 4e-40 | 15/18 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.59×** | +10.1 | 8e-22 | 37/44 (MIA PaCa-2, BT-474, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.50×** | +9.0 | 3e-17 | 17/23 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.99×** | +7.1 | 2e-10 | 27/39 (A549, Panc 03.27, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.89×** | +6.8 | 1e-09 | 26/45 (A549, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.55×** | +6.6 | 3e-09 | 26/41 (NCI-H2347, A549, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +6.4 | 1e-08 | 21/35 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +6.3 | 2e-08 | 25/45 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.81×** | +6.3 | 2e-08 | 26/45 (NCI-H1792, Panc 03.27, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.72×** | +5.5 | 2e-06 | 20/43 (NCI-H2347, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.66×** | +5.4 | 3e-06 | 22/44 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.41×** | +5.2 | 9e-06 | 27/45 (NCI-H2347, LoVo, …) | top dose only | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.40×** | +5.1 | 2e-05 | 15/45 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +4.9 | 4e-05 | 20/44 (J82, NCI-H2347, …) | rises with dose | position effect removed |
| [[Berbamine (drug)]] 5 µM |  | **1.32×** | +4.2 | 9e-04 | 17/44 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **2.06×** | +4.0 | 0.002 | 12/38 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.008 | 11/44 (A-427, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.89×** | +3.5 | 0.010 | 12/43 (NCI-H460, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.011 | 10/44 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.83×** | +3.4 | 0.017 | 10/40 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.023 | 17/43 (NCI-H1792, C32, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.027 | 12/44 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.034 | 9/44 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.72×** | +3.0 | 0.047 | 7/39 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3025.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.353×** | -15.6 | 0e+00 | 36/41 (PANC-1, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.426×** | -9.1 | 4e-17 | 32/41 (COLO 205, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.480×** | -7.5 | 1e-11 | 32/43 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.582×** | -5.7 | 1e-06 | 25/45 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.756×** | -4.2 | 0.003 | 20/45 (H4, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.685×** | -4.0 | 0.006 | 21/44 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.714×** | -3.3 | 0.080 | 10/41 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | 0.565× | -3.2 | 0.11 | 12/44 (MIA PaCa-2, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.81 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3025. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.1 | 2 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 5.43× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.33× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -12.5) |
| [[A498 (line)]] | wt | 10.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.0749× (z -13.8) |
| [[PANC-1 (line)]] | alt | 19.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -16.0) |
| [[A-427 (line)]] | wt | 16.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -11.2) |
| [[RKO (line)]] | wt | 23.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0898× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 12.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.6) |
| [[SW480 (line)]] | alt | 11.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.8) |
| [[A549 (line)]] | wt | 11.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.79× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0955× (z -9.1) |
| [[BT-474 (line)]] | alt | 14.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.42× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0284× (z -14.7) |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 1 | — | [[Baicalin (drug)]] 0.05 µM 0.0898× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 8.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -9.3) |
| [[Hs 766T (line)]] | wt | 4.75 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.05 µM 0.0749× (z -9.1) |
| [[J82 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[KATO III (line)]] | alt | 32.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -9.1) |
| [[LoVo (line)]] | wt | 9.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 6.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 7.82 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 5.01× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 9.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 8.76 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +9.3) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 6.51 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0419× (z -10.2) |
| [[SNU-1 (line)]] | wt | 19.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -10.7) |
| [[SNU-423 (line)]] | alt | 8.78 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.81× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -11.6) |
| [[SW48 (line)]] | wt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -14.4) |
| [[A-172 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3025), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHRNA5]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[AHSA1]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[LDHB]] | +0.67 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[HACD3]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[GGCT]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[BRI3BP]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[UTP18]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PRDX3]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[SHMT1]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[GLB1L2]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[HSPD1]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[SNRPA]] | +0.60 | +0.60 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP4A]] | -0.64 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[TJAP1]] | -0.63 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[TCEANC]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[MED18]] | -0.59 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[CIRBP]] | -0.58 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[TAB3]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CYP20A1]] | -0.57 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[METTL25B]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[WASHC1]] | -0.57 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[TERF2IP]] | -0.56 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[LRCH3]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[H3-3B]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNK2]] | B | WNK2 activity raises TMEM97's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without WNK2 | 0.022 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[PDE3B]] | B | PDE3B activity raises TMEM97's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.56× lower at baseline in the lines without PDE3B | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[MCM3]] | C | MCM3 activity raises TMEM97's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 2.46× lower at baseline in the lines without MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **-** arm (projection on the module's main direction -0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-22.2, -11.5); signed map (-29.0, -33.3). **Vector** length 96.2, 22.8% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | +5.7 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.5 | +6.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.2 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.0 | +13.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.8 | +4.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.7 | +5.1 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +3.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -15.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -9.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Bergenin (drug)]] 5 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 97 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,319,200-28,328,685 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S2R, sigma2R, sigma(2)R, MAC30, σ2R |
| Gene groups (HGNC) | EXPERA domain containing; Sigma receptors |
| Hallmark sets | MYC_TARGETS_V2, CHOLESTEROL_HOMEOSTASIS, XENOBIOTIC_METABOLISM, MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5BJF2](https://www.uniprot.org/uniprotkb/Q5BJF2) (Sigma intracellular receptor 2):

> Sigma-2 receptor implicated in the regulation of multiple cellular processes, including cholesterol biosynthesis and trafficking, membrane trafficking, autophagy, lipid membrane-associated protein trafficking, and stabilization of receptors at the cell surface, thereby contributing to the maintenance of cellular homeostasis. Forms a ternary complex with PGRMC1 and LDLR at the plasma membrane, promoting LDLR-mediated internalization of LDL cholesterol. Reduces the availability of the lysosomal …

**Summary**, from NCBI Gene [27346](https://www.ncbi.nlm.nih.gov/gene/27346):

> TMEM97 is a conserved integral membrane protein that plays a role in controlling cellular cholesterol levels (Bartz et al., 2009 [PubMed 19583955]).[supplied by OMIM, Aug 2009]

**Accessions** — [HGNC:28106](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28106) · Entrez [27346](https://www.ncbi.nlm.nih.gov/gene/27346) · UniProt [Q5BJF2](https://www.uniprot.org/uniprotkb/Q5BJF2) · Ensembl [ENSG00000109084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109084)

## Data

Gene col 3025: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3025); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3025, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3025]; `tensor/DDL_lfc|DDL_z.npy` [3025]; `embed/gene_vectors.npy` [3025]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3025 or target_col == 3025). Every well: [[TMEM97 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM97.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

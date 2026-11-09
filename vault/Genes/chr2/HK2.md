---
symbol: "HK2"
type: "gene"
col: 8252
ensembl_id: "ENSG00000159399"
name: "hexokinase 2"
location: "2p12"
module: 99
arm: "+"
pooled_cpm: 248.12
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 20
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# HK2

*hexokinase 2* — 2p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.20× (z +7.6, q 2e-11, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.156× (z -20.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERO1A]] (+0.83, fdr 7e-06), [[INSIG2]] (+0.80, fdr 7e-06), [[FAM210A]] (+0.77, fdr 7e-06); moves opposite to [[RNF115]] (-0.64, fdr 3e-05), [[ITPA]] (-0.62, fdr 2e-04), [[ZNF518A]] (-0.59, fdr 3e-04).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NDRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8252.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.20×** | +7.6 | 2e-11 | 49/49 (Hs 766T, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.35×** | +5.0 | 1e-04 | 39/48 (C32, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.73×** | +4.4 | 0.002 | 37/48 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.039 | 41/49 (HT-29, LS 180, …) | top dose only | plate-row cell shift |
| [[Abemaciclib (drug)]] 5 µM |  | **2.24×** | +3.4 | 0.084 | 38/48 (LoVo, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 2.16× | +3.2 | 0.12 | 35/48 (SW480, LOX-IMVI, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.33× | +3.2 | 0.12 | 29/49 (SNU-1, A-427, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8252.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.156×** | -20.0 | 0e+00 | 47/48 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.208×** | -11.9 | 2e-30 | 47/48 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.240×** | -10.9 | 3e-25 | 42/44 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.258×** | -10.7 | 1e-24 | 48/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.296×** | -9.3 | 2e-18 | 47/47 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.330×** | -8.8 | 2e-16 | 46/49 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.329×** | -8.5 | 2e-15 | 43/47 (A549, SW1417, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.490×** | -7.7 | 9e-13 | 46/49 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.503×** | -5.4 | 4e-06 | 46/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.610×** | -5.3 | 6e-06 | 40/48 (RKO, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.555×** | -4.5 | 4e-04 | 38/48 (BT-474, SW1417, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | **0.589×** | -4.2 | 0.001 | 43/48 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.590×** | -4.2 | 0.001 | 44/48 (A-172, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.604×** | -4.0 | 0.003 | 42/48 (HOP62, A498, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.714×** | -3.6 | 0.013 | 47/48 (SW1417, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.640×** | -3.5 | 0.016 | 32/48 (A498, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.738×** | -3.2 | 0.038 | 32/48 (BT-474, SW 1271, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.662×** | -3.2 | 0.038 | 36/48 (A498, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.684×** | -3.0 | 0.082 | 36/48 (CHP-212, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 570 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0662× (z -25.4) |
| [[NCI-H2347 (line)]] | alt | 324 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0813× (z -24.9) |
| [[Hs 766T (line)]] | wt | 362 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 18.8× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -19.2) |
| [[KATO III (line)]] | alt | 249 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -19.4) |
| [[A549 (line)]] | wt | 145 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0773× (z -22.6) |
| [[BT-474 (line)]] | alt | 283 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0578× (z -23.7) |
| [[HCT15 (line)]] | alt | 404 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -15.0) |
| [[LOX-IMVI (line)]] | wt | 491 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0808× (z -20.2) |
| [[NCI-H23 (line)]] | alt | 256 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 16.3× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -19.8) |
| [[RKO (line)]] | wt | 282 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0799× (z -23.7) |
| [[SW1417 (line)]] | alt | 110 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.2) |
| [[HEC-1-A (line)]] | alt | 177 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -18.0) |
| [[HepG2_C3A (line)]] | wt | 396 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0452× (z -25.3) |
| [[HT-29 (line)]] | alt | 129 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -21.6) |
| [[NCI-H1573 (line)]] | alt | 472 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 208 | 2 | 3 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 5.48× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -14.4) |
| [[PANC-1 (line)]] | alt | 111 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -20.9) |
| [[SW48 (line)]] | wt | 274 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0956× (z -16.0) |
| [[SW480 (line)]] | alt | 158 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.98× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.8) |
| [[A-172 (line)]] | wt | 90.2 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0970× (z -15.1) |
| [[CFPAC-1 (line)]] | alt | 575 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.345× (z -8.7) |
| [[CHP-212 (line)]] | wt | 313 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -16.4) |
| [[HOP62 (line)]] | alt | 429 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.1) |
| [[LS 180 (line)]] | wt | 238 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 398 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 253 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -14.2) |
| [[SNU-1 (line)]] | wt | 289 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 19.1× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 215 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -17.3) |
| [[C-33 A (line)]] | alt | 103 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0819× (z -15.4) |
| [[H4 (line)]] | wt | 488 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -14.9) |
| [[HS-578T (line)]] | alt | 369 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -15.9) |
| [[hTERT-HPNE (line)]] | wt | 188 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 160 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.345× (z -10.8) |
| [[SW 1271 (line)]] | alt | 406 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -13.5) |
| [[A-427 (line)]] | wt | 88.7 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 13.4× (z +10.0) | [[Harringtonine (drug)]] 5 µM 0.298× (z -8.6) |
| [[AN3 CA (line)]] | alt | 255 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0597× (z -15.1) |
| [[COLO 205 (line)]] | alt | 153 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 27.1× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -8.7) |
| [[LoVo (line)]] | wt | 154 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -16.6) |
| [[NCI-H2030 (line)]] | alt | 219 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -16.8) |
| [[SW 1088 (line)]] | alt | 624 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -10.7) |
| [[SW 900 (line)]] | alt | 248 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.4) |
| [[J82 (line)]] | alt | 131 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 286 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.8) |
| [[SHP-77 (line)]] | alt | 165 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.5) |
| [[SNU-423 (line)]] | alt | 257 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.7) |
| [[A498 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 355 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERO1A]] | +0.83 | +0.89 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[INSIG2]] | +0.80 | +0.84 / +0.71 | both halves | 7e-06 |  |
| [[FAM210A]] | +0.77 | +0.80 / +0.75 | both halves | 7e-06 |  |
| [[TPD52]] | +0.75 | +0.77 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[PDK1]] | +0.73 | +0.84 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 753 |
| [[ALKBH5]] | +0.71 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[SLC2A1]] | +0.71 | +0.79 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 811 |
| [[WDR45B]] | +0.69 | +0.80 / +0.56 | both halves | 1e-05 |  |
| [[PGK1]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 743 |
| [[PDK3]] | +0.69 | +0.78 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[UBE2O]] | +0.68 | +0.79 / +0.40 | both halves | 5e-05 |  |
| [[FAM162A]] | +0.68 | +0.77 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | -0.64 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[ITPA]] | -0.62 | -0.66 / -0.29 | both halves | 2e-04 |  |
| [[ZNF518A]] | -0.59 | -0.66 / -0.28 | both halves | 3e-04 |  |
| [[ST7L]] | -0.59 | -0.69 / -0.21 | both halves | 7e-04 |  |
| [[ZC3H7B]] | -0.59 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[CPLANE1]] | -0.59 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[C11orf58]] | -0.59 | -0.66 / -0.22 | both halves | 6e-04 |  |
| [[ZC3HC1]] | -0.59 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[PMF1]] | -0.58 | -0.56 / -0.22 | both halves | 6e-04 |  |
| [[PPP3CB-AS1]] | -0.58 | -0.63 / -0.23 | both halves | 5e-04 |  |
| [[ZNF764]] | -0.58 | -0.60 / -0.36 | both halves | 1e-04 |  |
| [[NFYC]] | -0.58 | -0.54 / -0.38 | both halves | 7e-05 | pathway: HALLMARK_MTORC1_SIGNALING |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | B | NDRG1 activity raises HK2's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without NDRG1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[SLC2A1]] | C | SLC2A1 activity raises HK2's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 2.14× lower at baseline in the lines without SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[RBMS1]] | C | RBMS1 activity lowers HK2's level | lines that do not express RBMS1 (4) vs lines expressing it (46) | 1.26× higher at baseline in the lines without RBMS1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with EP300, TGFBR2, BRCA2; also absent: ENSG00000285155, TBC1D9, TCEA2; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.838). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.1, -16.4); signed map (-36.5, 24.5). **Vector** length 140, 60.6% of its response variance represented; |z| ≥ 3 in 1,278 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.61 to 7); *Gluconeogenesis* (reactome, mean cos +0.56 to 6); *Regulation of pyruvate metabolism* (reactome, mean cos +0.57 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +10.4 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +10.0 | -0.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +9.5 | +0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.1 | -0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | -1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.2 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +0.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +3.2 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.5 | -11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -11.0 | -20.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -10.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.4 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +0.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.9 | -4.0 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -3.3 | -4.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.1 | -2.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.8 | -4.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | hexokinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p12 — chr2:74,834,127-74,893,359 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HKII |
| Gene groups (HGNC) | Hexokinase family |
| Hallmark sets | MYC_TARGETS_V2, IL2_STAT5_SIGNALING, GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING |
| Reactome | 3 pathways, smallest: Glycolysis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P52789](https://www.uniprot.org/uniprotkb/P52789) (Hexokinase-2):

> Catalyzes the phosphorylation of hexose, such as D-glucose and D-fructose, to hexose 6-phosphate (D-glucose 6-phosphate and D-fructose 6-phosphate, respectively). Mediates the initial step of glycolysis by catalyzing phosphorylation of D-glucose to D-glucose 6-phosphate. Plays a key role in maintaining the integrity of the outer mitochondrial membrane by preventing the release of apoptogenic molecules from the intermembrane space and subsequent apoptosis.

**Summary**, from NCBI Gene [3099](https://www.ncbi.nlm.nih.gov/gene/3099):

> Hexokinases phosphorylate glucose to produce glucose-6-phosphate, the first step in most glucose metabolism pathways. This gene encodes hexokinase 2, the predominant form found in skeletal muscle. It localizes to the outer membrane of mitochondria. Expression of this gene is insulin-responsive, and studies in rat suggest that it is involved in the increased rate of glycolysis seen in rapidly growing cancer cells. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:4923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4923) · Entrez [3099](https://www.ncbi.nlm.nih.gov/gene/3099) · UniProt [P52789](https://www.uniprot.org/uniprotkb/P52789) · Ensembl [ENSG00000159399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159399)

## Data

Gene col 8252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8252); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8252]; `tensor/DDL_lfc|DDL_z.npy` [8252]; `embed/gene_vectors.npy` [8252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8252 or target_col == 8252). Every well: [[HK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

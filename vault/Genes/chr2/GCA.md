---
symbol: "GCA"
type: "gene"
col: 3647
ensembl_id: "ENSG00000115271"
name: "grancalcin"
location: "2q24.2"
module: 32
arm: "+"
pooled_cpm: 22.41
n_lines_expressing: 47
n_dd_up: 18
n_dd_down: 26
n_dd_up_clean: 15
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 31
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# GCA

*grancalcin* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.88× (z +28.2, q 0e+00, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.737× (z -8.1, q 3e-13, down in 24 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIH1]] (+0.78, fdr 7e-06, ⚠ same locus), [[HLA-F]] (+0.76, fdr 7e-06), [[DDX60]] (+0.73, fdr 7e-06), [[GBP5]] (+0.72, fdr 7e-06); moves opposite to [[HERC2P3]] (-0.57, fdr 1e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PHF11]] → it (grade C ⚠); 31 go from it, the strongest it → cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3647.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.88×** | +28.2 | 0e+00 | 39/45 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +14.0 | 6e-42 | 35/45 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +13.6 | 4e-40 | 36/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +13.5 | 4e-39 | 32/45 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +11.8 | 3e-30 | 31/45 (SW1417, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +11.2 | 3e-27 | 32/44 (SW1417, HT-29, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +9.3 | 2e-18 | 30/44 (LoVo, SW 900, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +6.4 | 8e-09 | 22/44 (LoVo, HS-578T, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +6.4 | 8e-09 | 2/45 (NCI-H23, MIA PaCa-2) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.9 | 2e-07 | 22/45 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.2 | 9e-06 | 16/45 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 1e-05 | 16/44 (HT-29, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.0 | 2e-05 | 19/44 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +5.0 | 2e-05 | 19/45 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +4.5 | 2e-04 | 9/45 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.9 | 0.003 | 17/45 (LoVo, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.005 | 13/45 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3647.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.737×** | -8.1 | 3e-13 | 24/45 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.594×** | -7.6 | 6e-12 | 30/45 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.667×** | -7.6 | 6e-12 | 25/44 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.679×** | -7.3 | 6e-11 | 26/44 (SW480, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.708×** | -6.5 | 1e-08 | 24/45 (PANC-1, HS-578T, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.540×** | -6.0 | 2e-07 | 24/44 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.801×** | -5.9 | 3e-07 | 20/45 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.736×** | -5.7 | 7e-07 | 19/44 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.749×** | -5.2 | 1e-05 | 14/33 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.767×** | -5.0 | 4e-05 | 19/45 (NCI-H661, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.769×** | -4.9 | 4e-05 | 21/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.769×** | -4.9 | 4e-05 | 19/44 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.842× | -4.6 | 2e-04 | 19/45 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.631×** | -4.5 | 3e-04 | 16/37 (RKO, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.796×** | -4.3 | 7e-04 | 22/44 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.797×** | -4.3 | 7e-04 | 15/44 (NCI-H23, SK-MEL-2, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.650×** | -4.2 | 1e-03 | 19/45 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.736×** | -4.1 | 0.001 | 15/45 (MIA PaCa-2, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3647. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.3 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 83.7× (z +37.5) | — |
| [[A-172 (line)]] | wt | 25.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +22.0) | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +21.4) | — |
| [[LoVo (line)]] | wt | 21.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 22.1 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +23.2) | [[Ixazomib citrate (drug)]] 0.5 µM 0.405× (z -9.3) |
| [[SW1417 (line)]] | alt | 42.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +11.1) | — |
| [[SW480 (line)]] | alt | 21.5 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.281× (z -12.2) |
| [[C32 (line)]] | wt | 27.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +14.4) | — |
| [[HCT15 (line)]] | alt | 30.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change |
| [[HT-29 (line)]] | alt | 29.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +14.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 3 | — | [[Tofacitinib (citrate) (drug)]] 5 µM 0.175× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 25.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.6) | — |
| [[A-427 (line)]] | wt | 56.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -13.2) |
| [[HOP62 (line)]] | alt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +16.3) | — |
| [[J82 (line)]] | alt | 22.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +19.8) | — |
| [[LS 180 (line)]] | wt | 26.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.72× (z +24.8) | — |
| [[NCI-H1573 (line)]] | alt | 23.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.233× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 20.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +30.6) | — |
| [[SK-MEL-2 (line)]] | alt | 36.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.83× (z +18.2) | — |
| [[SW 900 (line)]] | alt | 14.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +13.6) | — |
| [[A498 (line)]] | wt | 25.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +9.2) | — |
| [[A549 (line)]] | wt | 17.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.236× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +11.2) | — |
| [[H4 (line)]] | wt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 8.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 13.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.82× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 14.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +11.0) | — |
| [[NCI-H2122 (line)]] | alt | 29.4 | 0 | 1 | — | [[Berbamine (drug)]] 5 µM 0.150× (z -17.3) |
| [[NCI-H23 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 31.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.8) | — |
| [[SW 1271 (line)]] | alt | 36.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +8.8) | — |
| [[SW48 (line)]] | wt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.25× (z +12.6) | — |
| [[AN3 CA (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3647), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIH1]] | +0.78 | +0.80 / +0.75 | both halves | 7e-06 | STRING 663; ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[HLA-F]] | +0.76 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[DDX60]] | +0.73 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[GBP5]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[RIGI]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[DHX58]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[TRIM5]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[CCL5]] | +0.70 | +0.70 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[PLEKHA4]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[TRANK1]] | +0.69 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[HERC5]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[BATF2]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[STAT1]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P3]] | -0.57 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHF11]] | C | PHF11 activity raises GCA's level | lines that do not express PHF11 (3) vs lines expressing it (47) | 2.91× lower at baseline in the lines without PHF11 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 0, C 31. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | [[CEBPD]], GCA activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.67× the cells of the other lines | 0.006 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM | C | [[CEBPD]], GCA activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.69× the cells of the other lines | 0.010 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Sulfatinib (drug)]] 5 µM | C | [[CEBPD]], GCA activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.65× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Entecavir (monohydrate) (drug)]] 0.5 µM | C | [[CEBPD]], GCA activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.66× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | [[CEBPD]], GCA activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 1.40× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Cepharanthine (drug)]] 5 µM | C | [[CEBPD]], GCA activity lowers the cells' numbers under Cepharanthine 5 µM (makes them more sensitive) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 1.30× the cells of the other lines | 0.031 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | [[CEBPD]], GCA activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.74× the cells of the other lines | 0.031 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | [[CEBPD]], GCA activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.74× the cells of the other lines | 0.035 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Homoharringtonine (drug)]] 0.05 µM | C | [[CEBPD]], GCA activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.54× the cells of the other lines | 0.035 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Tranilast (drug)]] 0.5 µM | C | [[CEBPD]], GCA activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.74× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | C | [[CEBPD]], GCA activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.36× the cells of the other lines | 0.038 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | C | [[CEBPD]], GCA activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.66× the cells of the other lines | 0.038 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.2, 51.0); signed map (64.1, 28.6). **Vector** length 104, 25.5% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.57 to 56); *interferon gamma response* (hallmark, mean cos +0.57 to 60); *interferon* (control, mean cos +0.64 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +28.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +13.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~5% of this change | +3.4 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.9 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.2 | -7.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.9 | -8.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.8 | -7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -6.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.5 | -5.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.5 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | grancalcin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:162,318,840-162,371,595 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GCL |
| Gene groups (HGNC) | EF-hand domain containing |
| Hallmark sets | COMPLEMENT |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P28676](https://www.uniprot.org/uniprotkb/P28676) (Grancalcin):

> Calcium-binding protein that may play a role in the adhesion of neutrophils to fibronectin. May play a role in the formation of focal adhesions.

**Summary**, from NCBI Gene [25801](https://www.ncbi.nlm.nih.gov/gene/25801):

> This gene encodes a calcium-binding protein that is abundant in neutrophils and macrophages. In the absence of divalent cation, this protein localizes to the cytosolic fraction; with magnesium alone, it partitions with the granule fraction; and in the presence of magnesium and calcium, it associates with both the granule and membrane fractions. Alternative splicing and use of alternative promoters results in multiple transcript variants. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:15990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15990) · Entrez [25801](https://www.ncbi.nlm.nih.gov/gene/25801) · UniProt [P28676](https://www.uniprot.org/uniprotkb/P28676) · Ensembl [ENSG00000115271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115271)

## Data

Gene col 3647: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3647); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3647, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3647]; `tensor/DDL_lfc|DDL_z.npy` [3647]; `embed/gene_vectors.npy` [3647]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3647 or target_col == 3647). Every well: [[GCA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

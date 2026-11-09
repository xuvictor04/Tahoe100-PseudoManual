---
symbol: "MMADHC-DT"
type: "gene"
col: 13827
ensembl_id: "ENSG00000231969"
name: "MMADHC divergent transcript"
location: "2q23.3"
module: 26
arm: "+"
pooled_cpm: 12.71
n_lines_expressing: 48
n_dd_up: 32
n_dd_down: 8
n_dd_up_clean: 26
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# MMADHC-DT

*MMADHC divergent transcript* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.80× (z +36.0, q 0e+00, up in 42 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.440× (z -10.2, q 1e-21, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC90B-AS1]] (+0.87, fdr 7e-06), [[PKN2-AS1]] (+0.86, fdr 1e-05), [[PPP1R12A-AS2]] (+0.85, fdr 5e-05); moves opposite to [[MAST3]] (-0.76, fdr 1e-04), [[YIF1B]] (-0.75, fdr 9e-04, ⚠ one half only (not replicated)), [[RSAD1]] (-0.74, fdr 1e-05), [[BRAT1]] (-0.74, fdr 1e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[FER1L6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13827.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.80×** | +36.0 | 0e+00 | 42/42 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.78×** | +27.4 | 0e+00 | 43/43 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **4.19×** | +25.1 | 0e+00 | 41/46 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.28×** | +19.8 | 0e+00 | 40/42 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.43×** | +18.4 | 0e+00 | 41/42 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.39×** | +14.5 | 0e+00 | 40/43 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.20×** | +14.4 | 4e-45 | 34/44 (A-172, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.38×** | +10.7 | 6e-25 | 37/45 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.81×** | +10.3 | 3e-23 | 31/46 (AsPC-1, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +8.7 | 2e-16 | 29/45 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +5.8 | 3e-07 | 12/25 (SW 900, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.8 | 3e-07 | 22/45 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +5.7 | 4e-07 | 19/45 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +5.7 | 5e-07 | 20/43 (A549, COLO 205, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +5.5 | 1e-06 | 15/33 (HOP62, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **1.37×** | +5.5 | 2e-06 | 17/46 (HOP62, NCI-H460, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.49×** | +4.9 | 3e-05 | 20/44 (NCI-H460, HepG2/C3A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13827.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.440×** | -10.2 | 1e-21 | 30/45 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.488×** | -8.9 | 1e-16 | 25/45 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.558×** | -7.2 | 8e-11 | 24/42 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.584×** | -6.7 | 3e-09 | 23/45 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.615×** | -5.5 | 6e-06 | 18/45 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.802×** | -3.9 | 0.008 | 14/46 (SNU-423, SW 900, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.550×** | -3.9 | 0.008 | 12/46 (LoVo, HepG2/C3A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.738×** | -3.4 | 0.044 | 12/44 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13827. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 74.7 | 7 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +17.5) | [[Belinostat (drug)]] 5 µM 0.137× (z -15.3) |
| [[SW480 (line)]] | alt | 12.2 | 8 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0835× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.221× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 55.4 | 5 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +20.0) | [[Belinostat (drug)]] 5 µM 0.100× (z -12.3) |
| [[HOP62 (line)]] | alt | 6.82 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.9× (z +18.9) | — |
| [[HT-29 (line)]] | alt | 18.7 | 5 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.01× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -11.0) |
| [[A-172 (line)]] | wt | 14.0 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +11.9) | — |
| [[HEC-1-A (line)]] | alt | 35.5 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.44× (z +16.7) | — |
| [[AsPC-1 (line)]] | alt | 24.3 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +12.5) | [[Belinostat (drug)]] 5 µM 0.146× (z -10.4) |
| [[J82 (line)]] | alt | 8.70 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.45× (z +13.2) | — |
| [[KATO III (line)]] | alt | 7.15 | 4 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +15.4) | [[Bendamustine (drug)]] 5 µM 0.0643× (z -11.5) |
| [[A498 (line)]] | wt | 12.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +14.0) | — |
| [[C32 (line)]] | wt | 8.75 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +12.3) | [[Arbutin (drug)]] 5 µM 0.0685× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 6.59 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.84× (z +15.1) | — |
| [[SNU-423 (line)]] | alt | 7.09 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +12.2) | [[Pyridoxine (drug)]] 0.5 µM 0.0605× (z -10.2) |
| [[SW1417 (line)]] | alt | 13.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +15.4) | — |
| [[A549 (line)]] | wt | 5.27 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.58× (z +10.1) | [[Bestatin (drug)]] 5 µM 0.0491× (z -9.7) |
| [[COLO 205 (line)]] | alt | 30.0 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +11.5) | [[Belinostat (drug)]] 5 µM 0.121× (z -10.6) |
| [[HCT15 (line)]] | alt | 9.60 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +12.0) | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0634× (z -9.2) |
| [[LS 180 (line)]] | wt | 23.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 3.76 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +11.8) | [[Mozavaptan (drug)]] 0.5 µM 0.0838× (z -8.5) |
| [[PANC-1 (line)]] | alt | 4.23 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +17.5) | — |
| [[SW 900 (line)]] | alt | 8.84 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +14.1) | — |
| [[CFPAC-1 (line)]] | alt | 7.18 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 5.83 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.71× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 4.40 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 6.18 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.48× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +12.9) | — |
| [[NCI-H1792 (line)]] | alt | 7.81 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.67× (z +11.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.118× (z -8.6) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 6.52 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +14.8) | — |
| [[BT-474 (line)]] | alt | 5.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.55× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 4.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.0× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +8.7) | — |
| [[RKO (line)]] | wt | 6.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.45× (z +11.2) | — |
| [[A-427 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13827), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B-AS1]] | +0.87 | +0.82 / +0.60 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.86 | +0.84 / +0.57 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.85 | +0.86 / +0.40 | both halves | 5e-05 |  |
| [[TMEM202-AS1]] | +0.85 | +0.85 / +0.39 | both halves | 5e-05 |  |
| [[PBLD]] | +0.84 | +0.81 / +0.43 | both halves | 3e-05 |  |
| [[PCNX4-DT]] | +0.84 | +0.84 / +0.45 | both halves | 3e-05 | same gene group |
| [[LINC00571]] | +0.83 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[ARRDC3-AS1]] | +0.83 | +0.81 / +0.58 | both halves | 8e-06 |  |
| [[NEB]] | +0.81 | +0.83 / +0.45 | both halves | 3e-05 |  |
| [[CIBAR1-DT]] | +0.81 | +0.72 / +0.51 | both halves | 1e-05 | same gene group |
| [[EFCAB5]] | +0.80 | +0.82 / +0.28 | both halves | 3e-04 |  |
| [[LINC01004]] | +0.80 | +0.75 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.76 | -0.68 / -0.34 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.75 | -0.69 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[RSAD1]] | -0.74 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[BRAT1]] | -0.74 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[CEP131]] | -0.73 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[HACE1]] | -0.73 | -0.71 / -0.44 | both halves | 3e-05 |  |
| [[RNF41]] | -0.72 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[SLC27A1]] | -0.72 | -0.69 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[ELP1]] | -0.71 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[ATG4C]] | -0.71 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[ARRB2]] | -0.71 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[NBPF3]] | -0.70 | -0.66 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FER1L6]] | B | FER1L6 activity raises MMADHC-DT's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 2.03× lower at baseline in the lines without FER1L6 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MMADHC-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises MMADHC-DT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises MMADHC-DT's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 2.14× lower at baseline in the lines without ZNF341-AS1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[WASF3]] | B | WASF3 activity raises MMADHC-DT's level | lines that do not express WASF3 (21) vs lines expressing it (29) | 1.20× lower at baseline in the lines without WASF3 | 0.069 | ⚠ within organs, on part of the lines; also absent: SDC2, COL4A4, IGF2BP1 |
| [[ZHX2]] | B | ZHX2 activity raises MMADHC-DT's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without ZHX2 | 0.088 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[LINC00705]] | B | LINC00705 activity raises MMADHC-DT's level | lines that do not express LINC00705 (8) vs lines expressing it (42) | 1.77× lower at baseline in the lines without LINC00705 | 0.090 | ⚠ within organs, on part of the lines; also absent: SMAD3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.863). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (7.8, 11.7); signed map (23.7, -6.9). **Vector** length 114, 28.8% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +36.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +10.9 | +25.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +19.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.7 | +18.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +27.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.5 | +14.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +5.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.5 | -10.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.7 | -7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.7 | -8.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -6.8 | -6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.7 | -5.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.8 | -3.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.5 | -3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | MMADHC divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q23.3 — chr2:149,587,196-150,047,447 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41087) · Entrez [101929231](https://www.ncbi.nlm.nih.gov/gene/101929231) · Ensembl [ENSG00000231969](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231969)

## Data

Gene col 13827: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13827); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13827, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13827]; `tensor/DDL_lfc|DDL_z.npy` [13827]; `embed/gene_vectors.npy` [13827]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13827 or target_col == 13827). Every well: [[MMADHC-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMADHC-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

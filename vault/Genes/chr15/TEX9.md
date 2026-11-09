---
symbol: "TEX9"
type: "gene"
col: 7537
ensembl_id: "ENSG00000151575"
name: "testis expressed 9"
location: "15q21.3"
module: 28
arm: "+"
pooled_cpm: 21.18
n_lines_expressing: 47
n_dd_up: 44
n_dd_down: 18
n_dd_up_clean: 33
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# TEX9

*testis expressed 9* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.85× (z +16.3, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.426× (z -10.3, q 6e-22, down in 37 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.526× (z -7.7, q 4e-12, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDAP1]] (+0.62, fdr 1e-05), [[TAB2]] (+0.61, fdr 1e-05), [[FNBP1P1]] (+0.59, fdr 4e-05); moves opposite to [[DCUN1D2]] (-0.62, fdr 3e-05), [[SS18L1]] (-0.56, fdr 1e-04), [[LPCAT1]] (-0.55, fdr 8e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[CCDC148]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7537.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.85×** | +16.3 | 0e+00 | 44/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.70×** | +15.8 | 0e+00 | 44/44 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.08×** | +13.6 | 6e-40 | 43/44 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +12.8 | 3e-35 | 34/44 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.74×** | +9.5 | 2e-19 | 40/45 (A-172, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +9.5 | 2e-19 | 32/44 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.34×** | +9.3 | 2e-18 | 39/45 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.61×** | +8.2 | 3e-14 | 33/45 (LOX-IMVI, LoVo, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.79×** | +7.1 | 9e-11 | 31/45 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.78×** | +7.0 | 2e-10 | 36/44 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.93×** | +6.8 | 6e-10 | 39/45 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +5.9 | 2e-07 | 22/34 (SHP-77, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.65×** | +5.8 | 2e-07 | 27/44 (A498, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.58×** | +5.6 | 1e-06 | 25/44 (HOP62, LoVo, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +5.5 | 2e-06 | 22/37 (LS 180, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.4 | 2e-06 | 24/45 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +4.8 | 6e-05 | 21/44 (A-427, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +4.7 | 6e-05 | 28/44 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 2e-04 | 21/44 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 3e-04 | 23/44 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7537.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.426×** | -10.3 | 6e-22 | 37/44 (NCI-H23, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.526×** | -7.7 | 4e-12 | 36/45 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -7.3 | 4e-11 | 34/44 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.575×** | -6.6 | 4e-09 | 35/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.698×** | -6.1 | 1e-07 | 30/45 (COLO 205, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.594×** | -5.6 | 2e-06 | 26/44 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.626×** | -5.6 | 2e-06 | 24/44 (CFPAC-1, AN3 CA, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.650×** | -5.2 | 2e-05 | 25/44 (COLO 205, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.650×** | -5.0 | 4e-05 | 25/44 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.676×** | -4.7 | 2e-04 | 21/44 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.475×** | -4.7 | 2e-04 | 19/44 (CHP-212, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.651×** | -4.6 | 2e-04 | 23/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.691×** | -4.2 | 0.001 | 19/45 (PANC-1, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.518×** | -4.1 | 0.001 | 16/36 (HCT15, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.712×** | -4.1 | 0.002 | 20/45 (PANC-1, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.735×** | -3.5 | 0.014 | 19/44 (CFPAC-1, NCI-H661, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.756×** | -3.3 | 0.027 | 17/44 (NCI-H23, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7537. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 98.6 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0796× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -17.6) |
| [[LoVo (line)]] | wt | 27.0 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.229× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.268× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 39.9 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0913× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.184× (z -12.6) |
| [[PANC-1 (line)]] | alt | 13.8 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 8.62× (z +13.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.176× (z -10.7) |
| [[SW480 (line)]] | alt | 29.0 | 1 | 6 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.07× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -11.5) |
| [[A-172 (line)]] | wt | 15.1 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 23.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.54× (z +11.9) | — |
| [[NCI-H460 (line)]] | wt | 13.9 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +13.3) | — |
| [[A498 (line)]] | wt | 9.30 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.63× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 8.61 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 15.3× (z +10.8) | — |
| [[J82 (line)]] | alt | 11.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.45× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.01× (z +9.2) | — |
| [[H4 (line)]] | wt | 23.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 35.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 16.6 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 5.10× (z +9.1) | [[Digitoxin (drug)]] 0.05 µM 0.120× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 23.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.44× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -9.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 9.64 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.86× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 28.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 14.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.99× (z +9.3) | — |
| [[RKO (line)]] | wt | 13.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.61× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 44.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 49.1 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.31× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0625× (z -13.0) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A-427 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7537), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDAP1]] | +0.62 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[TAB2]] | +0.61 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[FNBP1P1]] | +0.59 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[KCNMB2-AS1]] | +0.58 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[FAM227B]] | +0.58 | +0.73 / +0.45 | both halves | 3e-05 |  |
| [[DNAH7]] | +0.58 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[NDUFA5]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[FAM204A]] | +0.57 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[DZIP3]] | +0.57 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[RPS6KA6]] | +0.57 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PMPCB]] | +0.57 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[CCDC148]] | +0.57 | +0.73 / +0.54 | both halves | 1e-05 | STRING 631 |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCUN1D2]] | -0.62 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[SS18L1]] | -0.56 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[LPCAT1]] | -0.55 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[TMEM184B]] | -0.55 | -0.68 / -0.36 | both halves | 1e-04 |  |
| [[GAN]] | -0.54 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[BET1L]] | -0.54 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[CCNQ]] | -0.53 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[HEATR5A]] | -0.53 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[ZMYND19]] | -0.53 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[LDLRAP1]] | -0.52 | -0.65 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[TPST2]] | -0.52 | -0.69 / -0.30 | both halves | 2e-04 |  |
| [[TMEM104]] | -0.51 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[FBH1]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TEX9's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.3% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[GDAP1]] | B | GDAP1 activity raises TEX9's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 2.41× lower at baseline in the lines without GDAP1 | 0.050 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent |
| [[LINC01876]] | B | LINC01876 activity raises TEX9's level | lines that do not express LINC01876 (24) vs lines expressing it (26) | 1.49× lower at baseline in the lines without LINC01876 | 0.096 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B |
| [[ZFHX2]] | C | ZFHX2 activity raises TEX9's level | lines that do not express ZFHX2 (3) vs lines expressing it (47) | 3.30× lower at baseline in the lines without ZFHX2 | 0.049 | ⚠ few lines (3 vs 47); across organs; also absent: FOXP4-AS1, ENSG00000256673, WWOX; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC148]] | C | TEX9 activity raises CCDC148's level | lines that do not express TEX9 (3) vs lines expressing it (47) | 3.26× lower at baseline in the lines without TEX9 | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: ZMAT3, PDE4C, LCA5; maybe low, not absent; co-absent with the target |
| [[SPEF2]] | C | TEX9 activity raises SPEF2's level | lines that do not express TEX9 (3) vs lines expressing it (47) | 4.57× lower at baseline in the lines without TEX9 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: ZMAT3, PDE4C, LCA5; maybe low, not absent |
| [[MEGF8]] | C | TEX9 activity raises MEGF8's level | lines that do not express TEX9 (3) vs lines expressing it (47) | 2.10× lower at baseline in the lines without TEX9 | 0.031 | ⚠ few lines (3 vs 47); across organs; also absent: ZMAT3, PDE4C, LCA5; maybe low, not absent |
| [[ZMAT3]] | C | TEX9 activity raises ZMAT3's level | lines that do not express TEX9 (3) vs lines expressing it (47) | 3.85× lower at baseline in the lines without TEX9 | 0.084 | ⚠ few lines (3 vs 47); across organs; also absent: ZMAT3, PDE4C, LCA5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.481). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.9, 13.1); signed map (9.8, -25.0). **Vector** length 66.4, 14.7% of its response variance represented; |z| ≥ 3 in 1,269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +9.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.4 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +7.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.0 | +15.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.0 | -5.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.0 | -5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -6.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -5.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:56,243,971-56,445,997 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

UniProt [Q8N6V9](https://www.uniprot.org/uniprotkb/Q8N6V9) carries no function annotation.

**Summary**, from NCBI Gene [374618](https://www.ncbi.nlm.nih.gov/gene/374618):

> Located in centriolar satellite. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29585) · Entrez [374618](https://www.ncbi.nlm.nih.gov/gene/374618) · UniProt [Q8N6V9](https://www.uniprot.org/uniprotkb/Q8N6V9) · Ensembl [ENSG00000151575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151575)

## Data

Gene col 7537: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7537); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7537, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7537]; `tensor/DDL_lfc|DDL_z.npy` [7537]; `embed/gene_vectors.npy` [7537]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7537 or target_col == 7537). Every well: [[TEX9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEX9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

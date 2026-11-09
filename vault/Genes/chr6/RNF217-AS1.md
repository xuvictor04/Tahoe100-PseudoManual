---
symbol: "RNF217-AS1"
type: "gene"
col: 14085
ensembl_id: "ENSG00000236548"
name: "RNF217 antisense RNA 1"
location: "6q22.31"
module: 15
arm: "+"
pooled_cpm: 9.37
n_lines_expressing: 41
n_dd_up: 9
n_dd_down: 26
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 7
direction_downstream: 4
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# RNF217-AS1

*RNF217 antisense RNA 1* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.74× (z +29.5, q 0e+00, up in 35 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.207× (z -15.2, q 0e+00, down in 32 of 38 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.517× (z -6.4, q 1e-08, down in 25 of 35 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PXDNL]] (+0.73, fdr 1e-05), [[MYLK4]] (+0.72, fdr 6e-05), [[CCDC90B-AS1]] (+0.71, fdr 2e-05); moves opposite to [[MRPS31P4]] (-0.65, fdr 1e-04), [[RADX]] (-0.63, fdr 8e-05), [[MAST3]] (-0.62, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[STAT4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14085.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.74×** | +29.5 | 0e+00 | 35/35 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.74×** | +14.4 | 1e-44 | 27/32 (PANC-1, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.94×** | +12.7 | 9e-35 | 27/32 (LS 180, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.07×** | +9.9 | 7e-21 | 24/39 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.96×** | +6.2 | 5e-08 | 22/35 (NCI-H460, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.80×** | +5.7 | 1e-06 | 21/38 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.70×** | +5.1 | 3e-05 | 17/36 (Panc 03.27, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.081 | 12/37 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.87×** | +3.2 | 0.100 | 5/37 (H4, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.41× | +3.1 | 0.11 | 6/39 (NCI-H460, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 1.82× | +3.0 | 0.13 | 5/35 (Hs 766T, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14085.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.207×** | -15.2 | 0e+00 | 32/38 (LS 180, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.209×** | -15.1 | 0e+00 | 35/37 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.256×** | -13.2 | 3e-37 | 29/37 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.469×** | -10.3 | 6e-23 | 27/33 (NCI-H1573, LoVo, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.415×** | -8.2 | 4e-14 | 22/36 (NCI-H1573, NCI-H460, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.433×** | -8.1 | 6e-14 | 24/34 (LS 180, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.437×** | -8.0 | 1e-13 | 27/38 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.487×** | -6.9 | 3e-10 | 24/37 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.517×** | -6.4 | 1e-08 | 25/35 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.510×** | -6.3 | 2e-08 | 17/29 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.526×** | -6.2 | 3e-08 | 22/37 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.305×** | -6.0 | 1e-07 | 25/35 (LS 180, SW 900, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.472×** | -6.0 | 1e-07 | 22/38 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.573×** | -5.4 | 3e-06 | 18/36 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.350×** | -5.3 | 4e-06 | 22/37 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.414×** | -4.5 | 3e-04 | 17/32 (LS 180, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.679×** | -3.7 | 0.005 | 16/37 (A-427, PANC-1, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **0.693×** | -3.6 | 0.010 | 12/36 (HCT15, RKO, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.625×** | -3.2 | 0.031 | 6/39 (LS 180, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.549×** | -3.0 | 0.061 | 8/34 (NCI-H460, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.558×** | -2.9 | 0.076 | 9/32 (LOX-IMVI, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.741×** | -2.9 | 0.080 | 9/38 (BT-474, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.57 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14085. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 33.9 | 1 | 11 (11 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -18.3) ⚠ cell-cycle shift, explains ~51% of this change |
| [[LS 180 (line)]] | wt | 46.2 | 3 | 8 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.0633× (z -17.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 14.3 | 2 | 9 (9 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.61× (z +15.9) | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -14.4) ⚠ cell-cycle shift, explains ~51% of this change |
| [[LoVo (line)]] | wt | 22.1 | 1 | 7 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -16.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.169× (z -10.8) |
| [[PANC-1 (line)]] | alt | 7.70 | 3 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +19.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -12.1) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.127× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 11.8 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.02× (z +16.7) | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 16.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -15.0) ⚠ cell-cycle shift, explains ~51% of this change |
| [[C32 (line)]] | wt | 15.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.58× (z +12.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -9.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 6.98 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +15.8) | — |
| [[Hs 766T (line)]] | wt | 18.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.105× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 8.31 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.87× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.0703× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[LOX-IMVI (line)]] | wt | 10.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.68× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.0849× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 9.16 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.33× (z +11.3) | [[Belinostat (drug)]] 5 µM 0.0565× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 5.43 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +14.6) | — |
| [[A549 (line)]] | wt | 12.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -12.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[COLO 205 (line)]] | alt | 8.00 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.07× (z +9.5) | [[Belinostat (drug)]] 5 µM 0.0463× (z -9.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 7.69 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +12.7) | [[Fluvoxamine (drug)]] 5 µM 0.0436× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 6.07 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +11.7) | [[Clofarabine (drug)]] 5 µM 0.0575× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 6.57 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.0524× (z -9.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 12.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.68× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.0463× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 7.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.41× (z +10.7) | — |
| [[BT-474 (line)]] | alt | 9.57 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -9.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[C-33 A (line)]] | alt | 2.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 7.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +13.3) | — |
| [[HCT15 (line)]] | alt | 6.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 5.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +12.6) | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.74× (z +12.6) | — |
| [[NCI-H2030 (line)]] | alt | 9.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.69× (z +12.5) | — |
| [[NCI-H2347 (line)]] | alt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.26× (z +9.5) | — |
| [[RKO (line)]] | wt | 4.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 5.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +12.0) | — |
| [[A-427 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14085), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PXDNL]] | +0.73 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[MYLK4]] | +0.72 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[CCDC90B-AS1]] | +0.71 | +0.49 / +0.46 | both halves | 2e-05 | same gene group |
| [[DARS1-AS1]] | +0.71 | +0.48 / +0.59 | both halves | 2e-05 | same gene group |
| [[CHD1-DT]] | +0.71 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[SIAH2-AS1]] | +0.71 | +0.42 / +0.51 | both halves | 4e-05 | same gene group |
| [[LINC01829]] | +0.70 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.70 | +0.62 / +0.40 | both halves | 5e-05 | same gene group |
| [[PKN2-AS1]] | +0.70 | +0.46 / +0.50 | both halves | 2e-05 | same gene group |
| [[MFF-DT]] | +0.70 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[PBLD]] | +0.69 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[C2orf88]] | +0.69 | +0.45 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | -0.65 | -0.34 / -0.62 | both halves | 1e-04 |  |
| [[RADX]] | -0.63 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[MAST3]] | -0.62 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[PAFAH1B3]] | -0.62 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[RMND1]] | -0.61 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ARRB2]] | -0.61 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[ALAD]] | -0.61 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[COMMD2]] | -0.60 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[SLC27A1]] | -0.60 | -0.43 / -0.18 | ⚠ not reproduced | 0.001 |  |
| [[TTC26]] | -0.60 | -0.25 / -0.62 | both halves | 4e-04 |  |
| [[TTC38]] | -0.59 | -0.27 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RNF217-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FLRT2]] | B | FLRT2 activity raises RNF217-AS1's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 2.05× lower at baseline in the lines without FLRT2 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[LINC01762]] | B | LINC01762 activity raises RNF217-AS1's level | lines that do not express LINC01762 (5) vs lines expressing it (45) | 2.16× lower at baseline in the lines without LINC01762 | 0.064 | ⚠ within organs, on part of the lines; also absent: MPP4, LINC01429, DNAH6; maybe low, not absent |
| [[STAT4]] | B | STAT4 activity raises RNF217-AS1's level | lines that do not express STAT4 (7) vs lines expressing it (43) | 3.12× lower at baseline in the lines without STAT4 | 0.089 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ZPLD1, SMAD7; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity lowers RNF217-AS1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[RNF217]] | C | RNF217 activity raises RNF217-AS1's level | lines that do not express RNF217 (9) vs lines expressing it (41) | 3.68× lower at baseline in the lines without RNF217 | 0.001 | ⚠ within organs, on part of the lines; also absent: RNF217-AS1, LRP12, BEX3; co-absent with the target |
| [[RNF217]] | C | RNF217's natural level strengthens RNF217-AS1's drug response | RNF217's natural level across 38 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.47; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAT4]] | B | RNF217-AS1 activity raises STAT4's level | lines that do not express RNF217-AS1 (9) vs lines expressing it (41) | 2.39× lower at baseline in the lines without RNF217-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: RNF217, LRP12, CCDC149; maybe low, not absent |
| [[ANKRD17-DT]] | B | RNF217-AS1 activity raises ANKRD17-DT's level | lines that do not express RNF217-AS1 (9) vs lines expressing it (41) | 1.50× lower at baseline in the lines without RNF217-AS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: RNF217, LRP12, CCDC149; maybe low, not absent |
| [[PPP1R12A-AS2]] | B | RNF217-AS1 activity lowers PPP1R12A-AS2's level | lines that do not express RNF217-AS1 (9) vs lines expressing it (41) | 1.24× higher at baseline in the lines without RNF217-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: RNF217, LRP12, CCDC149; maybe low, not absent |
| [[RNF217]] | C | RNF217-AS1 activity raises RNF217's level | lines that do not express RNF217-AS1 (9) vs lines expressing it (41) | 7.38× lower at baseline in the lines without RNF217-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: RNF217, LRP12, CCDC149; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (8.4, 13.9); signed map (24.6, -5.7). **Vector** length 94.2, 22.6% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +14.4 | +29.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +14.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +12.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.9 | -15.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.0 | -6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.8 | -13.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -6.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.4 | -15.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -0.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | RNF217 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q22.31 — chr6:124,644,434-124,963,165 (-) |
| Ensembl biotype | lncRNA |
| Also known as | STL |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50866) · Entrez [7955](https://www.ncbi.nlm.nih.gov/gene/7955) · Ensembl [ENSG00000236548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236548)

## Data

Gene col 14085: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14085); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14085, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14085]; `tensor/DDL_lfc|DDL_z.npy` [14085]; `embed/gene_vectors.npy` [14085]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14085 or target_col == 14085). Every well: [[RNF217-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF217-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

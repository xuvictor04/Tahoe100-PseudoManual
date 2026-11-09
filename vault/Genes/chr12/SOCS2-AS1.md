---
symbol: "SOCS2-AS1"
type: "gene"
col: 14477
ensembl_id: "ENSG00000246985"
name: "SOCS2 antisense RNA 1"
location: "12q22"
module: 68
arm: "+"
pooled_cpm: 5.31
n_lines_expressing: 37
n_dd_up: 19
n_dd_down: 22
n_dd_up_clean: 15
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 7
direction_downstream: 16
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# SOCS2-AS1

*SOCS2 antisense RNA 1* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.41× (z +24.5, q 0e+00, up in 23 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.477× (z -8.7, q 3e-15, down in 20 of 31 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOCS2]] (+0.83, fdr 7e-06, ⚠ same locus), [[PLA2G4C]] (+0.69, fdr 1e-05), [[IPO9-AS1]] (+0.68, fdr 2e-05), [[DENND5B-AS1]] (+0.66, fdr 7e-05); moves opposite to [[TTLL5]] (-0.63, fdr 1e-05), [[PACSIN2]] (-0.60, fdr 5e-05), [[ZDHHC9]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[IGF2BP1]] → it (grade B ⚠); 16 go from it, the strongest it → [[APLF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.41×** | +24.5 | 0e+00 | 23/28 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.74×** | +21.8 | 0e+00 | 21/25 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.71×** | +15.3 | 0e+00 | 19/25 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.80×** | +11.6 | 9e-29 | 22/32 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.91×** | +10.7 | 1e-24 | 17/33 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +9.2 | 5e-18 | 2/9 (NCI-H2030, PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.22×** | +8.6 | 6e-16 | 2/10 (HOP62, PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +8.3 | 1e-14 | 13/23 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +6.8 | 6e-10 | 3/15 (HOP62, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +5.8 | 3e-07 | 9/28 (SW480, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +5.5 | 2e-06 | 8/31 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.4 | 3e-06 | 13/33 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.49×** | +4.6 | 2e-04 | 6/21 (C-33 A, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.4 | 5e-04 | 5/32 (LoVo, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.0 | 0.002 | 2/16 (LoVo, SNU-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.006 | 10/27 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.006 | 9/30 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.007 | 6/27 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.037 | 6/27 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14477.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.477×** | -8.7 | 3e-15 | 20/31 (A-172, A549, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.582×** | -6.3 | 7e-08 | 14/31 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.590×** | -6.2 | 1e-07 | 15/33 (A-172, A549, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.673×** | -4.6 | 5e-04 | 8/29 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.708×** | -4.0 | 0.006 | 5/22 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.710×** | -4.0 | 0.006 | 8/32 (NCI-H460, J82, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.719×** | -3.9 | 0.009 | 8/33 (hTERT-HPNE, CHP-212, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.737×** | -3.5 | 0.025 | 6/33 (SNU-423, NCI-H2030, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.741×** | -3.5 | 0.025 | 9/34 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.738×** | -3.5 | 0.025 | 8/30 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.734×** | -3.5 | 0.025 | 9/17 (NCI-H23, A-172, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.745×** | -3.3 | 0.041 | 8/29 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.754×** | -3.3 | 0.041 | 8/28 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Pemetrexed (drug)]] 5 µM |  | **0.749×** | -3.3 | 0.044 | 4/25 (NCI-H2030, Panc 03.27, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.758×** | -3.2 | 0.044 | 5/29 (hTERT-HPNE, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.764×** | -3.1 | 0.058 | 7/32 (NCI-H460, SNU-423, …) | two highest doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.761×** | -3.1 | 0.071 | 6/23 (A498, SNU-423, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.767×** | -3.0 | 0.082 | 5/32 (hTERT-HPNE, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.86 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +14.5) | [[Digitoxin (drug)]] 5 µM 0.234× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 39.5 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0790× (z -13.8) |
| [[LoVo (line)]] | wt | 6.39 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.5× (z +18.8) | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~36% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 11.7 | 2 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 6.23× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.171× (z -9.2) |
| [[A498 (line)]] | wt | 4.49 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +15.3) | — |
| [[hTERT-HPNE (line)]] | wt | 22.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0704× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.101× (z -8.6) |
| [[C-33 A (line)]] | alt | 7.58 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0714× (z -8.5) ⚠ cell-cycle shift, explains ~66% of this change |
| [[HOP62 (line)]] | alt | 3.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.60× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 3.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0767× (z -11.9) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 3.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.83× (z +9.2) | — |
| [[A-427 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.623 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOCS2]] | +0.83 | +0.81 / +0.76 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PLA2G4C]] | +0.69 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[IPO9-AS1]] | +0.68 | +0.66 / +0.47 | both halves | 2e-05 | same gene group |
| [[DENND5B-AS1]] | +0.66 | +0.64 / +0.37 | both halves | 7e-05 | same gene group |
| [[CFAP54]] | +0.66 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[RGS20]] | +0.65 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[PPP1R12A-AS2]] | +0.64 | +0.60 / +0.31 | both halves | 2e-04 | same gene group |
| [[LRRC8C-DT]] | +0.64 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[ZBED5]] | +0.63 | +0.60 / +0.39 | both halves | 5e-05 |  |
| [[SSPN]] | +0.63 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[ARHGAP15]] | +0.63 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[COL28A1]] | +0.63 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[RIPK2-DT]] | +0.62 | +0.59 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL5]] | -0.63 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[PACSIN2]] | -0.60 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[ZDHHC9]] | -0.60 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[GUSBP1]] | -0.59 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[PHKA2]] | -0.58 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[RALGAPA2]] | -0.58 | -0.52 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGF2BP1]] | B | IGF2BP1 activity raises SOCS2-AS1's level | lines that do not express IGF2BP1 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without IGF2BP1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SLFN11, RUNX3, DPY19L2 |
| [[TOP2A]] | B | TOP2A activity lowers SOCS2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR3C1]] | B | NR3C1 activity lowers SOCS2-AS1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TENM3-AS1]] | B | TENM3-AS1 activity raises SOCS2-AS1's level | lines that do not express TENM3-AS1 (19) vs lines expressing it (31) | 1.65× lower at baseline in the lines without TENM3-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: TENM3, LRCH2, FBXL7; maybe low, not absent |
| [[PAMR1]] | B | PAMR1 activity raises SOCS2-AS1's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 1.92× lower at baseline in the lines without PAMR1 | 0.079 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[SOCS2]] | C | SOCS2 activity raises SOCS2-AS1's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 3.17× lower at baseline in the lines without SOCS2 | 0.005 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A; co-absent with the target |
| [[MIR1915HG]] | C | MIR1915HG activity raises SOCS2-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without MIR1915HG | 0.032 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLF]] | B | SOCS2-AS1 activity raises APLF's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 2.25× lower at baseline in the lines without SOCS2-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[GPR137]] | B | SOCS2-AS1 activity raises GPR137's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without SOCS2-AS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[SOCS5]] | B | SOCS2-AS1 activity raises SOCS5's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without SOCS2-AS1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[LINC00486]] | B | SOCS2-AS1 activity raises LINC00486's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 1.27× lower at baseline in the lines without SOCS2-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[IGF2BP1]] | B | SOCS2-AS1 activity raises IGF2BP1's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 4.37× lower at baseline in the lines without SOCS2-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[RGS20]] | B | SOCS2-AS1 activity raises RGS20's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 2.28× lower at baseline in the lines without SOCS2-AS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[ZFPM2]] | B | SOCS2-AS1 activity raises ZFPM2's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without SOCS2-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[MAILR]] | B | SOCS2-AS1 activity raises MAILR's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without SOCS2-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[FMNL3]] | B | SOCS2-AS1 activity raises FMNL3's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 2.64× lower at baseline in the lines without SOCS2-AS1 | 0.061 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[SLC13A3]] | B | SOCS2-AS1 activity weakens SLC13A3's drug response | lines that do not express SOCS2-AS1 (7) vs lines expressing it (31) | the lines without SOCS2-AS1 respond 1.17× as strongly (z diff -0.32); strongest at Epirubicin (hydrochloride) 5 µM: 3.66x vs 2.25x (z diff -2.8) | 0.075 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2; target measured in part of the lines; artifact flags |
| [[CYRIB]] | B | SOCS2-AS1 activity lowers CYRIB's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 1.45× higher at baseline in the lines without SOCS2-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[GJC1]] | B | SOCS2-AS1 activity raises GJC1's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 2.81× lower at baseline in the lines without SOCS2-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (17.4, 9.8); signed map (26.5, 8.1). **Vector** length 71.8, 14.7% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +24.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +21.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +15.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +5.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.4 | -6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -8.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.9 | -6.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | SOCS2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q22 — chr12:93,542,022-93,571,768 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27054) · Entrez [144481](https://www.ncbi.nlm.nih.gov/gene/144481) · Ensembl [ENSG00000246985](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246985)

## Data

Gene col 14477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14477); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14477]; `tensor/DDL_lfc|DDL_z.npy` [14477]; `embed/gene_vectors.npy` [14477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14477 or target_col == 14477). Every well: [[SOCS2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOCS2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

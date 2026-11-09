---
symbol: "ANKFN1"
type: "gene"
col: 7751
ensembl_id: "ENSG00000153930"
name: "ankyrin repeat and fibronectin type III domain containing 1"
location: "17q22"
module: 133
arm: "+"
pooled_cpm: 10.04
n_lines_expressing: 42
n_dd_up: 29
n_dd_down: 13
n_dd_up_clean: 19
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# ANKFN1

*ankyrin repeat and fibronectin type III domain containing 1* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 5.74× (z +24.7, q 0e+00, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.494× (z -10.0, q 1e-20, down in 25 of 36 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02112]] (+0.62, fdr 1e-05), [[PLAC1]] (+0.59, fdr 6e-05), [[LINC00616]] (+0.59, fdr 5e-05); moves opposite to [[DOP1A]] (-0.56, fdr 2e-04), [[ZNF512B]] (-0.44, fdr 3e-04).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02932]] → it (grade B ⚠); 5 go from it, the strongest it → [[RBM44]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7751.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **5.74×** | +24.7 | 0e+00 | 35/36 (BT-474, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +13.8 | 6e-41 | 22/35 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.16×** | +10.5 | 2e-23 | 26/36 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +10.1 | 1e-21 | 23/37 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.3 | 4e-11 | 3/14 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +7.1 | 2e-10 | 17/36 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.3 | 3e-08 | 9/28 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +5.0 | 5e-05 | 14/37 (RPMI-7951, SNU-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.44×** | +4.9 | 7e-05 | 10/36 (BT-474, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.93×** | +4.8 | 7e-05 | 9/23 (BT-474, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.8 | 7e-05 | 10/34 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.35×** | +4.3 | 8e-04 | 13/37 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +4.3 | 8e-04 | 3/19 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.33×** | +4.0 | 0.002 | 11/36 (BT-474, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.004 | 8/34 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.004 | 11/36 (BT-474, A-172, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.006 | 3/36 (LS 180, HS-578T, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.007 | 5/35 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.025 | 9/38 (A498, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.033 | 8/36 (SNU-1, NCI-H460, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.53×** | +3.1 | 0.041 | 5/32 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.50×** | +3.0 | 0.064 | 4/28 (RPMI-7951, A549, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7751.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.494×** | -10.0 | 1e-20 | 25/36 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.526×** | -9.1 | 2e-17 | 24/38 (SNU-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.540×** | -8.4 | 1e-14 | 22/37 (COLO 205, KATO III, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.616×** | -6.9 | 1e-09 | 19/36 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.674×** | -5.6 | 3e-06 | 17/33 (KATO III, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.766×** | -5.3 | 8e-06 | 21/35 (KATO III, A498, …) | all doses, stronger at high dose | composition shift |
| [[crizotinib (drug)]] 5 µM |  | **0.729×** | -4.3 | 0.001 | 7/36 (LoVo, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.739×** | -4.1 | 0.003 | 14/34 (COLO 205, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.788×** | -3.4 | 0.042 | 6/36 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.634×** | -3.4 | 0.042 | 14/34 (COLO 205, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.793×** | -3.3 | 0.052 | 9/36 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -3.2 | 0.056 | 5/39 (A549, SW480, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.854× | -3.2 | 0.069 | 4/40 (SW 1088, SW480, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.800×** | -3.0 | 0.098 | 6/32 (NCI-H1792, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 54.7 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0946× (z -17.5) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 42.8 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0465× (z -25.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.148× (z -11.1) |
| [[SNU-1 (line)]] | wt | 92.3 | 4 (1 ⚠) | 3 (3 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.57× (z +12.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -12.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 30.7 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0934× (z -13.8) |
| [[A498 (line)]] | wt | 13.7 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 16.6× (z +15.6) | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -18.2) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 10.3 | 3 | 0 | [[Auranofin (drug)]] 5 µM 57.4× (z +15.9) | — |
| [[H4 (line)]] | wt | 17.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 3.47 | 1 | 1 | [[Auranofin (drug)]] 5 µM 12.5× (z +8.8) | [[Asciminib (drug)]] 0.05 µM 0.0643× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 31.7 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.19× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.117× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 6.80 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.7× (z +9.2) | — |
| [[A549 (line)]] | wt | 7.74 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.114× (z -8.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HOP62 (line)]] | alt | 3.56 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.8× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 3.92 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.0× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0772× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 3.69 | 1 | 0 | [[Auranofin (drug)]] 5 µM 23.4× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 4.36 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0727× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 6.03 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.3× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 7.53 | 1 | 0 | [[Auranofin (drug)]] 5 µM 15.1× (z +15.7) | — |
| [[RKO (line)]] | wt | 12.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.0× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 33.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.40× (z +9.4) | — |
| [[SW480 (line)]] | alt | 6.45 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.99× (z +8.8) | — |
| [[A-427 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02112]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[PLAC1]] | +0.59 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[LINC00616]] | +0.59 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[ARHGEF2]] | +0.57 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[GRK3]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[TRD-AS1]] | +0.56 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[MYO18B]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[LINC01524]] | +0.55 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[LINC02885]] | +0.54 | +0.38 / +0.62 | both halves | 7e-05 |  |
| [[GTPBP2]] | +0.54 | +0.40 / +0.56 | both halves | 4e-05 |  |
| [[TTTY14]] | +0.53 | +0.30 / +0.59 | both halves | 2e-04 |  |
| [[FAM27C]] | +0.53 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1A]] | -0.56 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[ZNF512B]] | -0.44 | -0.27 / -0.42 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02932]] | B | LINC02932 activity raises ANKFN1's level | lines that do not express LINC02932 (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without LINC02932 | 0.082 | ⚠ within organs, on part of the lines; also absent: RBFOX1, DNAH6, ESRRB; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM44]] | B | ANKFN1 activity raises RBM44's level | lines that do not express ANKFN1 (8) vs lines expressing it (42) | 1.97× lower at baseline in the lines without ANKFN1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000214803, LINC00298; maybe low, not absent |
| [[MINAR1]] | B | ANKFN1 activity raises MINAR1's level | lines that do not express ANKFN1 (8) vs lines expressing it (42) | 2.25× lower at baseline in the lines without ANKFN1 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000214803, LINC00298; maybe low, not absent |
| [[LINC02935]] | B | ANKFN1 activity raises LINC02935's level | lines that do not express ANKFN1 (8) vs lines expressing it (42) | 1.38× lower at baseline in the lines without ANKFN1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000214803, LINC00298; maybe low, not absent |
| [[TNNI3K]] | B | ANKFN1 activity raises TNNI3K's level | lines that do not express ANKFN1 (8) vs lines expressing it (42) | 1.82× lower at baseline in the lines without ANKFN1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000214803, LINC00298; maybe low, not absent |
| [[NMRK1]] | B | ANKFN1 activity strengthens NMRK1's drug response | lines that do not express ANKFN1 (7) vs lines expressing it (40) | the lines without ANKFN1 respond 0.74× as strongly (z diff +1.40); strongest at Homoharringtonine 5 µM: 0.52x vs 0.22x (z diff +4.7) | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000214803, LINC00298; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.487). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.0, -19.2); signed map (7.4, 7.9). **Vector** length 76.3, 14.6% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.2 | +24.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and fibronectin type III domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:55,882,301-56,517,016 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38335 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Fibronectin type III domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N957](https://www.uniprot.org/uniprotkb/Q8N957) (Ankyrin repeat and fibronectin type-III domain-containing protein 1):

> May play a role in neuronal function.

**Summary**, from NCBI Gene [162282](https://www.ncbi.nlm.nih.gov/gene/162282):

> Predicted to be involved in establishment of mitotic spindle orientation and regulation of establishment of bipolar cell polarity. Predicted to act upstream of or within behavioral fear response; equilibrioception; and locomotor rhythm. Predicted to be active in spindle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26766) · Entrez [162282](https://www.ncbi.nlm.nih.gov/gene/162282) · UniProt [Q8N957](https://www.uniprot.org/uniprotkb/Q8N957) · Ensembl [ENSG00000153930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153930)

## Data

Gene col 7751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7751); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7751]; `tensor/DDL_lfc|DDL_z.npy` [7751]; `embed/gene_vectors.npy` [7751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7751 or target_col == 7751). Every well: [[ANKFN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKFN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
